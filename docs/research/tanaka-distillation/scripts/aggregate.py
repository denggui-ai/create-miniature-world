#!/usr/bin/env python3
"""Turn full/classified.json into by-object.json + by-object-summary.md.

Steps (run in order):
  labels  -> labels.tsv (distinct main_object labels with counts + examples)
  canon   -> canonical.json via Codex: merge synonyms into one canonical Chinese
             object name (chunked pass, then a second pass over the canonicals)
  build   -> ../by-object.json and ../by-object-summary.md
"""
import csv
import json
import subprocess
import sys
import time
from collections import Counter, defaultdict
from pathlib import Path

HERE = Path(__file__).resolve().parent
CATALOG = HERE.parent
CLS = json.loads((HERE / "classified.json").read_text(encoding="utf-8"))
ITEMS = CLS["items"]
UNDET = {"无法判断", ""}
MODEL = CLS.get("model", "gpt-5.6-terra")

CANON_SCHEMA = {
    "type": "object", "additionalProperties": False, "required": ["mapping"],
    "properties": {"mapping": {"type": "array", "items": {
        "type": "object", "additionalProperties": False, "required": ["label", "canonical"],
        "properties": {"label": {"type": "string"}, "canonical": {"type": "string"}}}}},
}

CANON_PROMPT = """你是词表整理员。下面是一批中文日常物件名（来自对田中达也微缩作品的主物件标注），每行：物件名<TAB>出现次数<TAB>示例标题。
任务：把指的是同一种具体物件的不同写法归并为一个规范名。
规则：
1. 只合并"同一种具体物件"的异名/同义/繁简/口语差异（剃刀／剃须刀／刮胡刀→剃须刀；字典／词典→字典；手机／智能手机→手机；洗衣夹／晾衣夹／衣夹→晾衣夹）。
2. 不要把不同物件合并成大类（面包和吐司不合并；苹果和橙子不合并；剪刀和美工刀不合并）。品牌名若与通用物件同指，用通用物件名（德芙巧克力→巧克力）。
3. 规范名用最常见的中文日常叫法，2–5 个字，不带修饰语。
4. 每个输入 label 都必须出现一次，canonical 为规范名；本身已是规范名的，canonical 写它自己。
5. 不要联网，不要读写文件，不要调用工具，直接按 schema 输出 JSON。

"""


def main_label(it):
    return it["main_object"].strip()


def cmd_labels():
    cnt = Counter()
    ex = defaultdict(list)
    for it in ITEMS:
        lab = main_label(it)
        if lab in UNDET:
            continue
        cnt[lab] += 1
        if len(ex[lab]) < 2:
            ex[lab].append(it["title"])
    with (HERE / "labels.tsv").open("w", encoding="utf-8", newline="") as f:
        w = csv.writer(f, delimiter="\t")
        for lab, n in cnt.most_common():
            w.writerow([lab, n, " / ".join(ex[lab])])
    print(f"distinct labels={len(cnt)} labelled items={sum(cnt.values())}")


def codex_map(rows, tag):
    """rows: list of (label, count, example). Returns dict label->canonical."""
    schema = HERE / "canon-schema.json"
    schema.write_text(json.dumps(CANON_SCHEMA, ensure_ascii=False))
    out = HERE / f"canon-{tag}.json"
    prompt = CANON_PROMPT + "\n".join(f"{l}\t{n}\t{e}" for l, n, e in rows) + "\n"
    cmd = ["codex", "exec", "--skip-git-repo-check", "-C", str(CATALOG), "-s", "read-only",
           "-m", MODEL, "-c", "model_reasoning_effort=low",
           "--output-schema", str(schema), "-o", str(out), "--json", "-"]
    t0 = time.time()
    with (HERE / f"canon-{tag}.events.jsonl").open("w") as fo, (HERE / f"canon-{tag}.stderr.log").open("w") as fe:
        p = subprocess.run(cmd, input=prompt, text=True, stdout=fo, stderr=fe)
    data = json.loads(out.read_text(encoding="utf-8").strip())
    m = {d["label"]: d["canonical"].strip() for d in data["mapping"]}
    missing = [l for l, _, _ in rows if l not in m]
    print(f"[canon {tag}] rc={p.returncode} {round(time.time()-t0)}s in={len(rows)} mapped={len(m)} missing={len(missing)}")
    for l in missing:
        m[l] = l
    return m


def cmd_canon(chunk=250):
    rows = list(csv.reader((HERE / "labels.tsv").open(encoding="utf-8"), delimiter="\t"))
    rows = [(l, int(n), e) for l, n, e in rows]
    # pass 1: chunked, sorted alphabetically so near-duplicates sit together
    rows_sorted = sorted(rows, key=lambda r: r[0])
    m1 = {}
    for i in range(0, len(rows_sorted), chunk):
        m1.update(codex_map(rows_sorted[i:i + chunk], f"p1-{i // chunk:02d}"))
    # pass 2: merge across chunks over the distinct canonicals
    cnt = Counter()
    ex = {}
    for l, n, e in rows:
        c = m1.get(l, l)
        cnt[c] += n
        ex.setdefault(c, e)
    rows2 = sorted(((c, n, ex[c]) for c, n in cnt.items()), key=lambda r: r[0])
    m2 = {}
    for i in range(0, len(rows2), chunk):
        m2.update(codex_map(rows2[i:i + chunk], f"p2-{i // chunk:02d}"))
    final = {l: m2.get(m1.get(l, l), m1.get(l, l)) for l, _, _ in rows}
    (HERE / "canonical.json").write_text(json.dumps(final, ensure_ascii=False, indent=1), encoding="utf-8")
    print(f"labels={len(final)} -> pass1 distinct={len(cnt)} -> final distinct={len(set(final.values()))}")


GENERIC = {"食物", "食品", "食材", "文具", "日用品", "蔬菜", "水果", "零食", "点心", "甜点", "甜食", "饮料",
           "家电", "电器", "工具", "玩具", "餐具", "厨具", "调味料", "调料", "衣服", "衣物", "杂物", "物品", "东西"}


def cmd_build():
    """Count only high/medium labels on concrete objects; low / generic / undetermined -> unresolved."""
    canon = json.loads((HERE / "canonical.json").read_text(encoding="utf-8"))
    unres = json.loads((HERE / "unresolved.json").read_text(encoding="utf-8"))
    by = defaultdict(lambda: {"count": 0, "slugs": [], "raw_labels": Counter(), "read_as": Counter(),
                              "conf": Counter(), "low_slugs": []})
    low, generic = [], []
    prom_path = HERE / "xcheck" / "promotions.json"
    promotions = json.loads(prom_path.read_text(encoding="utf-8"))["promotions"] if prom_path.exists() else {}
    for it in ITEMS:
        lab = main_label(it)
        conf = it.get("confidence", "low")
        if it["slug"] in promotions:  # terra low + astra agreed -> count as medium
            lab = promotions[it["slug"]]["main_object"]
            conf = "medium"
        if lab in UNDET:
            continue
        c = canon.get(lab, lab)
        if c in GENERIC:
            generic.append({"slug": it["slug"], "label": c, "confidence": conf})
            continue
        b = by[c]
        if conf == "low":
            low.append({"slug": it["slug"], "label": c})
            b["low_slugs"].append(it["slug"])
            continue
        b["count"] += 1
        b["slugs"].append(it["slug"])
        b["raw_labels"][lab] += 1
        if it.get("read_as"):
            b["read_as"][it["read_as"].strip()] += 1
        b["conf"][conf] += 1
    by = {c: b for c, b in by.items() if b["count"] > 0 or b["low_slugs"]}
    ordered = sorted(by.items(), key=lambda kv: (-kv[1]["count"], kv[0]))
    counted = [(c, b) for c, b in ordered if b["count"] > 0]

    unres["low_confidence"] = low
    unres["generic_label"] = generic
    unres["total_unresolved"] = (len(unres["no_text"]) + len(unres["missing_from_model"])
                                 + len(unres["model_undetermined"]) + len(low) + len(generic))
    (HERE / "unresolved.json").write_text(json.dumps(unres, ensure_ascii=False, indent=1), encoding="utf-8")

    out = {
        "source": "full/classified.json", "model": MODEL, "effort": CLS.get("effort"),
        "counting_rule": "count = high+medium confidence on concrete object labels; low/generic/undetermined/no_text listed in full/unresolved.json",
        "sent_to_model": len(ITEMS), "counted": sum(b["count"] for _, b in counted),
        "unresolved": unres["total_unresolved"], "classes": len(counted),
        "by_object": {
            c: {"count": b["count"], "high": b["conf"].get("high", 0), "medium": b["conf"].get("medium", 0),
                "low_not_counted": len(b["low_slugs"]),
                "raw_labels": dict(b["raw_labels"].most_common()),
                "read_as_top": [r for r, _ in b["read_as"].most_common(8)],
                "slugs": b["slugs"], "low_slugs": b["low_slugs"]}
            for c, b in ordered
        },
    }
    (CATALOG / "by-object.json").write_text(json.dumps(out, ensure_ascii=False, indent=1), encoding="utf-8")

    labelled = out["counted"]
    conf = Counter(it.get("confidence", "low") for it in ITEMS)
    lines = ["# 田中达也日更作品 · 按主物件归类（文本分类，Codex 产出；2026-10-10）\n"]
    lines.append(f"- 模型 {MODEL}（effort {CLS.get('effort')}），每批 150 条，输入为标题＋日语说明＋标签，不看图。")
    lines.append(f"- 送分类 {len(ITEMS)} 篇（另 {len(unres['no_text'])} 篇无文字未送）。模型置信度 high {conf['high']} / medium {conf['medium']} / low {conf['low']}，无法判断 {len(unres['model_undetermined'])}。")
    lines.append(f"- **计数口径**：只计 high+medium 且落在具体物件上的 {labelled} 篇。low {len(low)} 篇、泛类标签（食物／文具／日用品等）{len(generic)} 篇、无法判断 {len(unres['model_undetermined'])} 篇、无文字 {len(unres['no_text'])} 篇，合计 {unres['total_unresolved']} 篇待看图，见 `full/unresolved.json`。")
    lines.append(f"- 原始标签 {len(canon)} 个，经同义归并为 {len(canon) and len(set(canon.values()))} 个名；计入件数的物件类 {len(counted)} 个。归并表 `full/canonical.json`，逐篇结果 `full/classified.json`。")
    lines.append(f"- 交叉校验：744 篇待定项另交 gpt-6-astra 文本分类，其中 632 篇 astra 同样判不出（85%），证实是文本天花板；terra low 且两模型一致的 {len(promotions)} 篇提升为 medium 计入，astra 单方给出具体物件的 84 篇记在 `full/xcheck/promotions.json` 作看图参考。")
    lines.append("- 判读口径：件数是文本可见的下限，不是作品总数。2012–2014 年说明多为对白，待定项集中在那三年。全量跑时模型比 60 篇基准更敢猜（同模型自一致 36/60），medium 一列要带着这点看。\n")
    lines.append("## 件数 ≥ 5 的物件类\n")
    lines.append("| 物件 | 件数 | high | medium | low(未计) | 常见读成 | 归并自 |")
    lines.append("|---|---|---|---|---|---|---|")
    for c, b in counted:
        if b["count"] < 5:
            break
        ra = "、".join(r for r, _ in b["read_as"].most_common(4))
        raw = "、".join(l for l, _ in b["raw_labels"].most_common(4) if l != c)
        lines.append(f"| {c} | {b['count']} | {b['conf'].get('high',0)} | {b['conf'].get('medium',0)} | {len(b['low_slugs'])} | {ra} | {raw} |")
    small = [(c, b["count"]) for c, b in counted if b["count"] < 5]
    lines.append(f"\n## 件数 < 5 的物件类（{len(small)} 类）\n")
    lines.append("、".join(f"{c}×{n}" if n > 1 else c for c, n in small))
    (CATALOG / "by-object-summary.md").write_text("\n".join(lines) + "\n", encoding="utf-8")
    print(f"classes={len(counted)} counted={labelled} low={len(low)} generic={len(generic)} unresolved={unres['total_unresolved']}")
    print("top15=" + ", ".join(f"{c}:{b['count']}" for c, b in counted[:15]))


if __name__ == "__main__":
    {"labels": cmd_labels, "canon": cmd_canon, "build": cmd_build}[sys.argv[1]]()
