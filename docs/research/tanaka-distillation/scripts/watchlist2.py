#!/usr/bin/env python3
"""Second viewing batch: 30 posts sampled from unresolved.json (the 780 posts
text classification could not settle), stratified by year with a fixed seed.

Writes watchlist2.md / watchlist2.json next to this file. Images are read from
the private archive (outputs/tanaka-archive); nothing is downloaded here and
nothing enters the repo. Does not touch watchlist.py (first batch).

Usage: python3 watchlist2.py [--n 30] [--seed 20261010]
"""
import argparse
import csv
import json
import random
from collections import Counter, defaultdict
from pathlib import Path

HERE = Path(__file__).resolve().parent
CATALOG = HERE.parent
ARCHIVE = CATALOG.parent / "tanaka-archive"
GROUPS = ["no_text", "model_undetermined", "low_confidence", "generic_label"]


def slug_of(item):
    return item if isinstance(item, str) else item["slug"]


def load_pool():
    """Merge the four unresolved groups; a slug may sit in several groups."""
    u = json.load((HERE / "unresolved.json").open(encoding="utf-8"))
    groups = defaultdict(list)
    for g in GROUPS:
        for it in u[g]:
            groups[slug_of(it)].append(g)
    return groups


def allocate(pool, n, rng):
    """Proportional allocation per year (largest remainder), then sample."""
    by_year = defaultdict(list)
    for s in pool:
        by_year["20" + s[:2]].append(s)
    years = sorted(by_year)
    total = len(pool)
    quota = {y: n * len(by_year[y]) / total for y in years}
    base = {y: int(quota[y]) for y in years}
    left = n - sum(base.values())
    for y in sorted(years, key=lambda y: quota[y] - base[y], reverse=True)[:left]:
        base[y] += 1
    picks = []
    for y in years:
        k = min(base[y], len(by_year[y]))
        picks.extend(sorted(rng.sample(sorted(by_year[y]), k)))
    return picks, base, {y: len(by_year[y]) for y in years}


def archive_status():
    man = ARCHIVE / "manifest.tsv"
    if not man.exists():
        return {}
    with man.open(encoding="utf-8") as f:
        return {r["slug"]: r for r in csv.DictReader(f, delimiter="\t")}


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--n", type=int, default=30)
    ap.add_argument("--seed", type=int, default=20261010)
    a = ap.parse_args()

    pool = load_pool()
    rng = random.Random(a.seed)
    picks, quota, sizes = allocate(pool, a.n, rng)

    posts = {p["slug"]: p for p in json.load((CATALOG / "posts.json").open(encoding="utf-8"))
             if isinstance(p, dict) and "slug" in p}
    cls = {it["slug"]: it for it in json.load((HERE / "classified.json").open(encoding="utf-8"))["items"]}
    man = archive_status()

    rows = []
    for s in picks:
        p = posts.get(s, {})
        c = cls.get(s, {})
        m = man.get(s)
        archived = bool(m and m.get("status") == "ok")
        rows.append({
            "slug": s,
            "year": "20" + s[:2],
            "groups": pool[s],
            "title": p.get("title", ""),
            "caption": (p.get("caption") or "").strip(),
            "text_label": c.get("main_object", "") + ("→" + c["read_as"] if c.get("read_as") else ""),
            "text_confidence": c.get("confidence", ""),
            "link": p.get("link", f"https://miniature-calendar.com/{s}"),
            "archive_file": str(ARCHIVE / m["file"]) if m else "",
            "archived": archived,
        })

    (HERE / "watchlist2.json").write_text(
        json.dumps({"seed": a.seed, "n": a.n, "pool": len(pool), "quota": quota,
                    "pool_by_year": sizes, "items": rows}, ensure_ascii=False, indent=1),
        encoding="utf-8")

    out = [f"# 第二批看图清单（unresolved {len(pool)} 篇按年分层随机抽 {len(rows)}，seed={a.seed}）\n",
           "来源：unresolved.json 四组合并去重（" + "、".join(GROUPS) + "）。图片只从私有存档读取，不入仓库。\n",
           "| 年 | 待定篇数 | 抽取 |", "|---|---|---|"]
    out += [f"| {y} | {sizes[y]} | {quota[y]} |" for y in sorted(sizes)]
    out += ["", "| # | slug | 组 | 标题 | 说明 | 文本标签 | 已存档 |", "|---|---|---|---|---|---|---|"]
    for i, r in enumerate(rows, 1):
        cap = r["caption"].replace("|", "｜").replace("\n", " ")[:50] or "无"
        g = "、".join(r["groups"])
        lab = f"{r['text_label']}({r['text_confidence']})" if r["text_label"] else "—"
        out.append(f"| {i} | {r['slug']} | {g} | {r['title']} | {cap} | {lab} | {'✓' if r['archived'] else '待下载'} |")
    (HERE / "watchlist2.md").write_text("\n".join(out) + "\n", encoding="utf-8")

    print(f"pool={len(pool)} picked={len(rows)} archived={sum(r['archived'] for r in rows)}")
    print("groups:", dict(Counter(g for r in rows for g in r["groups"])))
    print("written", HERE / "watchlist2.md")


if __name__ == "__main__":
    main()
