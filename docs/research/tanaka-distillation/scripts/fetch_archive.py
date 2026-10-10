#!/usr/bin/env python3
"""Archive Tatsuya Tanaka's Miniature Calendar images for private research.

Source: ../tanaka-catalog/posts.json (image URLs from the public WP REST API).
Layout: images/<YYYY>/<slug>.jpg for the first image, <slug>-2.jpg ... for extra
images. manifest.tsv tracks slug/date/index/url/file/bytes/sha256/status so the
run is resumable and auditable. Polite fetch: 1 request every 0.6 s, 3 retries.
Never run from inside the repo's tracked tree; outputs/ is gitignored.
"""
import ast
import hashlib
import json
import re
import sys
import time
import urllib.request
from pathlib import Path

HERE = Path(__file__).resolve().parent
CATALOG = HERE.parent / "tanaka-catalog" / "posts.json"
IMG = HERE / "images"
MANIFEST = HERE / "manifest.tsv"
DELAY = 0.6
UA = {"User-Agent": "Mozilla/5.0 (private research archive; contact owner)"}
ONLY_FIRST = "--all" not in sys.argv


def load_done():
    done = {}
    if MANIFEST.exists():
        for line in MANIFEST.read_text(encoding="utf-8").splitlines()[1:]:
            f = line.split("\t")
            if len(f) >= 8 and f[7] == "ok":
                done[(f[0], f[2])] = f
    return done


def fetch(url):
    last = None
    for attempt in range(3):
        try:
            r = urllib.request.urlopen(urllib.request.Request(url, headers=UA), timeout=60)
            return r.read()
        except Exception as e:  # noqa: BLE001
            last = e
            time.sleep(2 * (attempt + 1))
    raise last


posts = [p for p in json.loads(CATALOG.read_text(encoding="utf-8")) if re.fullmatch(r"\d{6}", p["slug"])]
posts.sort(key=lambda p: p["slug"])
done = load_done()
new = not MANIFEST.exists()
mf = MANIFEST.open("a", encoding="utf-8")
if new:
    mf.write("slug\tdate\tidx\turl\tfile\tbytes\tsha256\tstatus\n")

todo = []
for p in posts:
    imgs = p["images"]
    imgs = ast.literal_eval(imgs) if isinstance(imgs, str) else imgs
    for i, u in enumerate(imgs, 1):
        if ONLY_FIRST and i > 1:
            break
        if (p["slug"], str(i)) in done:
            continue
        todo.append((p, i, u))
print(f"posts={len(posts)} already={len(done)} todo={len(todo)} only_first={ONLY_FIRST}", flush=True)

ok = fail = 0
t0 = time.time()
for n, (p, i, u) in enumerate(todo, 1):
    year = p["date"][:4]
    ext = Path(u.split("?")[0]).suffix.lower() or ".jpg"
    name = p["slug"] + ("" if i == 1 else f"-{i}") + ext
    out = IMG / year / name
    out.parent.mkdir(parents=True, exist_ok=True)
    try:
        data = fetch(u)
        out.write_bytes(data)
        sha = hashlib.sha256(data).hexdigest()
        mf.write(f"{p['slug']}\t{p['date']}\t{i}\t{u}\t{out.relative_to(HERE)}\t{len(data)}\t{sha}\tok\n")
        ok += 1
    except Exception as e:  # noqa: BLE001
        mf.write(f"{p['slug']}\t{p['date']}\t{i}\t{u}\t\t0\t\tfail:{type(e).__name__}\n")
        fail += 1
    mf.flush()
    if n % 100 == 0:
        el = time.time() - t0
        print(f"{n}/{len(todo)} ok={ok} fail={fail} {el/60:.1f}min eta={(len(todo)-n)*el/n/60:.0f}min", flush=True)
    time.sleep(DELAY)
mf.close()
print(f"done ok={ok} fail={fail} total_ok={len(done)+ok} minutes={(time.time()-t0)/60:.1f}", flush=True)
