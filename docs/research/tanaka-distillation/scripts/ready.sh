#!/bin/zsh
# Print batch-2 slugs that are archived but not yet blind-read.
cd "$(dirname "$0")"
for s in $(python3 -c "import json;print(' '.join(i['slug'] for i in json.load(open('../../tanaka-catalog/full/watchlist2.json'))['items']))"); do
  f=../../tanaka-archive/images/20${s:0:2}/$s.jpg
  [ -f "$f" ] && [ ! -f "$s.json" ] && echo -n "$s "
done; echo
