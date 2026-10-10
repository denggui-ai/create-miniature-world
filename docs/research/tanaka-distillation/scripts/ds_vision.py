#!/usr/bin/env python3
"""Blind image read via DeepSeek (vision). Usage:
  ds_vision.py <image> [--model deepseek-flash] [--prompt "..."]
Key: env DEEPSEEK_API_KEY, else macOS keychain item codex-deepseek-api-key.
The key is never printed. Output: model answer + usage as JSON on stdout.
"""
import argparse
import base64
import json
import mimetypes
import os
import subprocess
import sys
import time
import urllib.request

DEFAULT_PROMPT = (
    "你是第一次看到这张照片的普通观众。只根据画面回答三句，每句一个短语，不要解释：\n"
    "1. 小人在干什么？\n2. 画面里的主物件（真实日常物品）是什么？\n3. 这个物件被当成了什么？\n"
    "另外用不超过 60 字客观描述画面里有哪些东西和位置关系。按 JSON 输出："
    '{"action":"","object":"","read_as":"","description":""}'
)


def get_key():
    k = os.environ.get("DEEPSEEK_API_KEY", "").strip()
    if k:
        return k
    r = subprocess.run(["/usr/bin/security", "find-generic-password", "-a", "denggui",
                        "-s", "codex-deepseek-api-key", "-w"], capture_output=True, text=True)
    return r.stdout.strip()


ap = argparse.ArgumentParser()
ap.add_argument("image")
ap.add_argument("--model", default="deepseek-flash")
ap.add_argument("--prompt", default=DEFAULT_PROMPT)
a = ap.parse_args()

mime = mimetypes.guess_type(a.image)[0] or "image/jpeg"
b64 = base64.b64encode(open(a.image, "rb").read()).decode()
body = {
    "model": a.model,
    "messages": [{"role": "user", "content": [
        {"type": "image_url", "image_url": {"url": f"data:{mime};base64,{b64}"}},
        {"type": "text", "text": a.prompt},
    ]}],
    "temperature": 0.2,
}
req = urllib.request.Request(
    "https://api.deepseek.com/chat/completions",
    data=json.dumps(body).encode(),
    headers={"Authorization": "Bearer " + get_key(), "Content-Type": "application/json"},
)
t0 = time.time()
try:
    resp = json.loads(urllib.request.urlopen(req, timeout=120).read())
except urllib.error.HTTPError as e:
    print(json.dumps({"error": e.code, "body": e.read().decode()[:500]}, ensure_ascii=False))
    sys.exit(1)
out = {
    "image": os.path.basename(a.image),
    "model": a.model,
    "seconds": round(time.time() - t0, 1),
    "answer": resp["choices"][0]["message"]["content"],
    "usage": resp.get("usage"),
}
print(json.dumps(out, ensure_ascii=False, indent=1))
