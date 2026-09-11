#!/usr/bin/env python3
"""protect_output.py — PreToolUse hook for Write|Edit (works on macOS, Linux, Windows).

Blocks any file write outside participant-output/. Exit 2 blocks the tool and
sends the stderr message back to Claude as feedback; exit 0 lets it through.
Learner exercise: change ALLOWED, or add a rule for a file name you never want touched.
"""
import json, sys

ALLOWED = "participant-output/"

try:
    payload = json.load(sys.stdin)
except json.JSONDecodeError:
    sys.exit(0)
path = str(payload.get("tool_input", {}).get("file_path", "")).replace("\\", "/")
if not path or ("/" + ALLOWED) in path or path.startswith(ALLOWED):
    sys.exit(0)
print(f"Blocked by first-hook: agents may only write under {ALLOWED} (asked for: {path})", file=sys.stderr)
sys.exit(2)
