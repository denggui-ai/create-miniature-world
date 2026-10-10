#!/usr/bin/env python3
"""Compare main-object classifications from several Codex models.

Reads bench/result-<tag>.json, bench/events-<tag>.jsonl, bench/timing-<tag>.txt
and writes bench/compare.md (summary tables + disagreement rows).
Usage: compare.py gpt-6-luna gpt-5.6-terra gpt-6-astra
"""
import csv
import itertools
import json
import re
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
models = sys.argv[1:]
tags = {m: m.replace(".", "_") for m in models}


def norm(s: str) -> str:
    return re.sub(r"[\s（）()「」『』・·、,。]", "", s or "").strip()


def load_result(tag):
    p = HERE / f"result-{tag}.json"
    raw = p.read_text(encoding="utf-8").strip()
    data = json.loads(raw)
    return {it["slug"]: it for it in data["items"]}


def find_usage(obj):
    """Recursively find dicts that look like token usage."""
    found = []
    if isinstance(obj, dict):
        if "input_tokens" in obj or "output_tokens" in obj:
            found.append(obj)
        for v in obj.values():
            found.extend(find_usage(v))
    elif isinstance(obj, list):
        for v in obj:
            found.extend(find_usage(v))
    return found


def load_tokens(tag):
    p = HERE / f"events-{tag}.jsonl"
    last = None
    for line in p.read_text(encoding="utf-8").splitlines():
        line = line.strip()
        if not line.startswith("{"):
            continue
        try:
            ev = json.loads(line)
        except json.JSONDecodeError:
            continue
        us = find_usage(ev)
        if us:
            last = us[-1]
    return last or {}


def load_timing(tag):
    p = HERE / f"timing-{tag}.txt"
    d = {}
    for line in p.read_text().splitlines():
        k, _, v = line.partition(" ")
        d[k] = v
    return d


sample = list(csv.DictReader((HERE / "sample60.tsv").open(encoding="utf-8"), delimiter="\t"))
slugs = [r["slug"] for r in sample]
title = {r["slug"]: r["title"] for r in sample}
caption = {r["slug"]: r["caption"] for r in sample}

res = {m: load_result(tags[m]) for m in models}
tok = {m: load_tokens(tags[m]) for m in models}
tim = {m: load_timing(tags[m]) for m in models}

out = []
out.append("# 60 篇样本 · 主物件分类 · 三模型比对\n")
out.append("## 运行指标\n")
out.append("| 模型 | 返回条数 | slug 齐全 | 耗时(s) | input | cached | output | reasoning | rc |")
out.append("|---|---|---|---|---|---|---|---|---|")
for m in models:
    r = res[m]
    full = all(s in r for s in slugs)
    t = tok[m]
    out.append(
        f"| {m} | {len(r)} | {'是' if full else '否'} | {tim[m].get('seconds','?')} | "
        f"{t.get('input_tokens','?')} | {t.get('cached_input_tokens','?')} | "
        f"{t.get('output_tokens','?')} | {t.get('reasoning_output_tokens','?')} | {tim[m].get('rc','?')} |"
    )

out.append("\n## 置信度分布 / 无法判断\n")
out.append("| 模型 | high | medium | low | 无法判断 |")
out.append("|---|---|---|---|---|")
for m in models:
    r = res[m]
    c = {"high": 0, "medium": 0, "low": 0}
    na = 0
    for s in slugs:
        it = r.get(s)
        if not it:
            continue
        c[it.get("confidence", "low")] = c.get(it.get("confidence", "low"), 0) + 1
        if norm(it.get("main_object")) in ("无法判断", ""):
            na += 1
    out.append(f"| {m} | {c['high']} | {c['medium']} | {c['low']} | {na} |")


def main_of(m, s):
    it = res[m].get(s)
    return norm(it["main_object"]) if it else None


def all_objs(m, s):
    it = res[m].get(s)
    if not it:
        return set()
    return {norm(it["main_object"])} | {norm(o) for o in it.get("other_objects", [])}


out.append("\n## 两两一致率（n=60）\n")
out.append("严格 = main_object 字面相同；宽松 = 一方的 main_object 出现在另一方的 main_object 或 other_objects 中。\n")
out.append("| 模型对 | 严格一致 | 宽松一致 |")
out.append("|---|---|---|")
for a, b in itertools.combinations(models, 2):
    strict = sum(1 for s in slugs if main_of(a, s) and main_of(a, s) == main_of(b, s))
    loose = sum(
        1
        for s in slugs
        if main_of(a, s) and main_of(b, s)
        and (main_of(a, s) in all_objs(b, s) or main_of(b, s) in all_objs(a, s))
    )
    out.append(f"| {a} vs {b} | {strict}/60 ({strict/60:.0%}) | {loose}/60 ({loose/60:.0%}) |")

three_strict = sum(1 for s in slugs if len({main_of(m, s) for m in models}) == 1 and main_of(models[0], s))
out.append(f"\n三方严格一致：{three_strict}/60 ({three_strict/60:.0%})\n")

out.append("## 分歧条目（任一对严格不一致）\n")
out.append("| slug | 标题 | 说明（截断） | " + " | ".join(models) + " |")
out.append("|---|---|---|" + "---|" * len(models))
for s in slugs:
    mains = {main_of(m, s) for m in models}
    if len(mains) > 1:
        cells = []
        for m in models:
            it = res[m].get(s, {})
            cells.append(f"{it.get('main_object','—')} ({it.get('confidence','?')[0]})")
        cap = caption[s][:40].replace("|", "｜")
        out.append(f"| {s} | {title[s]} | {cap} | " + " | ".join(cells) + " |")

(HERE / "compare.md").write_text("\n".join(out) + "\n", encoding="utf-8")
print("\n".join(out[:40]))
print(f"... written to {HERE / 'compare.md'}")
