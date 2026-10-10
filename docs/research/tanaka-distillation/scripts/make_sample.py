#!/usr/bin/env python3
"""Draw a deterministic 60-post sample from posts.tsv (daily works only).

Stratified by year so the sample spans 2011-2026 instead of clustering.
Output: bench/sample60.tsv with the same columns minus `image`.
"""
import csv
import random
import re
from collections import defaultdict
from pathlib import Path

HERE = Path(__file__).resolve().parent
SRC = HERE.parent / "posts.tsv"
OUT = HERE / "sample60.tsv"
SEED = 20261010
N = 60

rows = []
with SRC.open(encoding="utf-8") as f:
    for r in csv.DictReader(f, delimiter="\t"):
        if re.fullmatch(r"\d{6}", r["slug"]) and r["caption"].strip():
            rows.append(r)

by_year = defaultdict(list)
for r in rows:
    by_year[r["date"][:4]].append(r)
years = sorted(by_year)

rng = random.Random(SEED)
per_year = N // len(years)
extra = N - per_year * len(years)
sample = []
for i, y in enumerate(years):
    k = per_year + (1 if i < extra else 0)
    pool = sorted(by_year[y], key=lambda r: r["slug"])
    sample.extend(rng.sample(pool, min(k, len(pool))))
sample.sort(key=lambda r: r["slug"])

with OUT.open("w", encoding="utf-8", newline="") as f:
    w = csv.writer(f, delimiter="\t")
    w.writerow(["slug", "date", "title", "caption", "tags"])
    for r in sample:
        w.writerow([r["slug"], r["date"], r["title"], r["caption"], r["tags"]])

print(f"daily posts: {len(rows)}; years: {len(years)}; sampled: {len(sample)} -> {OUT}")
