#!/bin/zsh
# Blind read (template C) for batch-2 slugs via DeepSeek flash; one JSON per slug.
# Usage: run_blind.sh <slug> [<slug> ...]   (skips slugs already done)
cd "$(dirname "$0")"
P=$(cat prompt-c.txt)
for s in "$@"; do
  [ -f "$s.json" ] && { echo "skip $s"; continue; }
  f=../../tanaka-archive/images/20${s:0:2}/$s.jpg
  [ -f "$f" ] || { echo "missing $s"; continue; }
  python3 ../ds_vision.py "$f" --prompt "$P" > "$s.json" && echo "done $s $(python3 -c "import json;u=json.load(open('$s.json'))['usage'];print(u['prompt_tokens'],u['completion_tokens'])")"
done
