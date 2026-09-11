#!/bin/bash
# protect-output.sh — PreToolUse hook for Write|Edit.
# Blocks any file write outside participant-output/ (exit 2 = block, message on stderr).
# Learner exercise: change the allowed folder, or add a second rule.
INPUT=$(cat)
FILE_PATH=$(printf '%s' "$INPUT" | python3 -c 'import json,sys; print(json.load(sys.stdin).get("tool_input",{}).get("file_path",""))' 2>/dev/null \
  || printf '%s' "$INPUT" | python -c 'import json,sys; print(json.load(sys.stdin).get("tool_input",{}).get("file_path",""))')
FILE_PATH="${FILE_PATH//\\//}"   # normalise Windows backslashes
case "$FILE_PATH" in
  */participant-output/*|participant-output/*) exit 0 ;;
  "") exit 0 ;;
  *) echo "Blocked by first-hook: agents may only write under participant-output/ (asked for: $FILE_PATH)" >&2; exit 2 ;;
esac
