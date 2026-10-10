#!/usr/bin/env python3
"""Classify all daily posts by main object with one Codex model, in batches.

- Input: ../posts.tsv (daily works = six-digit slug). Posts with empty caption
  are not sent to the model; they go to unresolved as reason "no_text".
- Each batch -> batch-NN.tsv, result-NN.json, events-NN.jsonl, timing-NN.txt.
- Validates each result (JSON parses, every slug present); missing slugs are
  re-sent in one or more follow-up batches. Then merges to classified.json.

Usage: run_full.py [--model gpt-5.6-terra] [--batch 150] [--jobs 3] [--only-merge]
"""
import argparse
import csv
import json
import re
import subprocess
import sys
import time
from concurrent.futures import ThreadPoolExecutor, as_completed
from pathlib import Path

HERE = Path(__file__).resolve().parent
CATALOG = HERE.parent
SRC = CATALOG / "posts.tsv"
PROMPT_TMPL = (CATALOG / "bench" / "prompt.md").read_text(encoding="utf-8")
SCHEMA = CATALOG / "bench" / "schema.json"

ap = argparse.ArgumentParser()
ap.add_argument("--model", default="gpt-5.6-terra")
ap.add_argument("--batch", type=int, default=150)
ap.add_argument("--jobs", type=int, default=3)
ap.add_argument("--effort", default="low")
ap.add_argument("--only-merge", action="store_true")
ap.add_argument("--slugs", default="", help="json file: list of slugs to classify (subset)")
ap.add_argument("--outdir", default="", help="output dir (default: this dir)")
ap.add_argument("--limit", type=int, default=0, help="smoke test: only first N posts")
args = ap.parse_args()
if args.outdir:
    HERE = Path(args.outdir).resolve()
    HERE.mkdir(parents=True, exist_ok=True)


def load_posts():
    daily, no_text = [], []
    with SRC.open(encoding="utf-8") as f:
        for r in csv.DictReader(f, delimiter="\t"):
            if not re.fullmatch(r"\d{6}", r["slug"]):
                continue
            (daily if r["caption"].strip() else no_text).append(r)
    daily.sort(key=lambda r: r["slug"])
    return daily, no_text


def write_batch(path, rows):
    with path.open("w", encoding="utf-8", newline="") as f:
        w = csv.writer(f, delimiter="\t")
        w.writerow(["slug", "date", "title", "caption", "tags"])
        for r in rows:
            w.writerow([r["slug"], r["date"], r["title"], r["caption"], r["tags"]])


def build_prompt(rows):
    body = PROMPT_TMPL.replace(
        "60 条记录", f"{len(rows)} 条记录"
    ).replace("`items` 共 60 条", f"`items` 共 {len(rows)} 条")
    lines = ["slug\tdate\ttitle\tcaption\ttags"]
    for r in rows:
        lines.append("\t".join([r["slug"], r["date"], r["title"], r["caption"], r["tags"]]))
    return body + "\n".join(lines) + "\n"


def run_batch(tag, rows):
    bpath = HERE / f"batch-{tag}.tsv"
    write_batch(bpath, rows)
    out = HERE / f"result-{tag}.json"
    ev = HERE / f"events-{tag}.jsonl"
    err = HERE / f"stderr-{tag}.log"
    cmd = [
        "codex", "exec", "--skip-git-repo-check", "-C", str(CATALOG), "-s", "read-only",
        "-m", args.model, "-c", f"model_reasoning_effort={args.effort}",
        "--output-schema", str(SCHEMA), "-o", str(out), "--json", "-",
    ]
    t0 = time.time()
    with ev.open("w") as fo, err.open("w") as fe:
        p = subprocess.run(cmd, input=build_prompt(rows), text=True, stdout=fo, stderr=fe)
    secs = round(time.time() - t0)
    usage = {}
    for line in ev.read_text(encoding="utf-8", errors="replace").splitlines():
        if '"usage"' in line:
            try:
                usage = json.loads(line).get("usage", {})
            except json.JSONDecodeError:
                pass
    (HERE / f"timing-{tag}.txt").write_text(
        json.dumps({"rc": p.returncode, "seconds": secs, "n": len(rows), "usage": usage}, ensure_ascii=False)
    )
    return tag, p.returncode, secs, usage


def read_result(tag):
    p = HERE / f"result-{tag}.json"
    if not p.exists():
        return {}
    try:
        data = json.loads(p.read_text(encoding="utf-8").strip())
        return {it["slug"]: it for it in data["items"]}
    except (json.JSONDecodeError, KeyError, TypeError):
        return {}


def run_all(batches):
    with ThreadPoolExecutor(max_workers=args.jobs) as ex:
        futs = [ex.submit(run_batch, tag, rows) for tag, rows in batches]
        for fu in as_completed(futs):
            tag, rc, secs, usage = fu.result()
            got = len(read_result(tag))
            print(f"[{tag}] rc={rc} {secs}s got={got} usage={usage}", flush=True)


daily, no_text = load_posts()
if args.limit:
    daily = daily[: args.limit]
if args.slugs:
    keep = set(json.loads(Path(args.slugs).read_text()))
    daily = [r for r in daily if r["slug"] in keep]
print(f"daily={len(daily)} to_classify={len(daily)} no_text={len(no_text)}", flush=True)

if not args.only_merge:
    batches = []
    for i in range(0, len(daily), args.batch):
        batches.append((f"{i // args.batch:02d}", daily[i:i + args.batch]))
    print(f"batches={len(batches)} model={args.model} jobs={args.jobs}", flush=True)
    run_all(batches)

    # follow-up for missing slugs (up to 2 rounds)
    for rnd in range(1, 3):
        have = {}
        for p in HERE.glob("result-*.json"):
            have.update(read_result(p.stem.split("-", 1)[1]))
        missing = [r for r in daily if r["slug"] not in have]
        print(f"round {rnd}: missing={len(missing)}", flush=True)
        if not missing:
            break
        fb = [(f"fix{rnd}-{i // args.batch:02d}", missing[i:i + args.batch]) for i in range(0, len(missing), args.batch)]
        run_all(fb)

# merge
have = {}
for p in sorted(HERE.glob("result-*.json")):
    have.update(read_result(p.stem.split("-", 1)[1]))
meta = {r["slug"]: r for r in daily}
items = []
for r in daily:
    it = have.get(r["slug"])
    if it is None:
        continue
    it = dict(it)
    it["date"] = r["date"]
    it["title"] = r["title"]
    items.append(it)
still_missing = [r["slug"] for r in daily if r["slug"] not in have]
(HERE / "classified.json").write_text(
    json.dumps({"model": args.model, "effort": args.effort, "n": len(items), "items": items}, ensure_ascii=False, indent=0),
    encoding="utf-8",
)
(HERE / "unresolved.json").write_text(
    json.dumps(
        {
            "no_text": [r["slug"] for r in no_text],
            "missing_from_model": still_missing,
            "model_undetermined": [it["slug"] for it in items if it["main_object"].strip() in ("无法判断", "")],
        },
        ensure_ascii=False, indent=1,
    ),
    encoding="utf-8",
)
tot_in = sum(json.loads(p.read_text())["usage"].get("input_tokens", 0) for p in HERE.glob("timing-*.txt"))
tot_out = sum(json.loads(p.read_text())["usage"].get("output_tokens", 0) for p in HERE.glob("timing-*.txt"))
und = sum(1 for it in items if it["main_object"].strip() in ("无法判断", ""))
print(f"classified={len(items)} undetermined={und} missing={len(still_missing)} no_text={len(no_text)} tokens in={tot_in} out={tot_out}", flush=True)
