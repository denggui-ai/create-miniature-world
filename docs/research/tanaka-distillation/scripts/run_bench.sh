#!/bin/zsh
# Run the 60-post main-object classification on several Codex models concurrently.
# Usage: bench/run_bench.sh gpt-6-luna gpt-5.6-terra gpt-6-astra
# Codex working root is outputs/tanaka-catalog (read-only sandbox); prompt forbids tools.
set -u
HERE=${0:A:h}
CATALOG=${HERE:h}
PROMPT_FILE=$HERE/prompt.md
DATA=$HERE/sample60.tsv
SCHEMA=$HERE/schema.json
EFFORT=${EFFORT:-low}

run_one() {
  local model=$1
  local tag=${model//./_}
  local prompt
  prompt="$(cat "$PROMPT_FILE")
$(cat "$DATA")"
  local t0=$(date +%s)
  echo "start $(date -Iseconds)" > "$HERE/timing-$tag.txt"
  codex exec --skip-git-repo-check -C "$CATALOG" -s read-only \
    -m "$model" -c model_reasoning_effort="$EFFORT" \
    --output-schema "$SCHEMA" -o "$HERE/result-$tag.json" --json \
    "$prompt" > "$HERE/events-$tag.jsonl" 2> "$HERE/stderr-$tag.log"
  local rc=$?
  local t1=$(date +%s)
  {
    echo "end $(date -Iseconds)"
    echo "rc $rc"
    echo "seconds $((t1 - t0))"
  } >> "$HERE/timing-$tag.txt"
  echo "[$model] rc=$rc seconds=$((t1 - t0))"
}

for m in "$@"; do
  run_one "$m" &
done
wait
echo "all done"
