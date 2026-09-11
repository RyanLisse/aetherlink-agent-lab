#!/usr/bin/env python3
"""Turn a trace/<session>.jsonl file into a readable "what happened" timeline.

Usage:
    python3 scenarios/agent-menu/tools/trace_summary.py                 # newest trace
    python3 scenarios/agent-menu/tools/trace_summary.py trace/<id>.jsonl

The summary answers the four observability questions used in the lab:
  1. What did the human ask?            (UserPromptSubmit)
  2. Which sources did the agent read?  (Read / Glob / Grep events)
  3. Which subagents ran and stopped?   (Task/Agent tool + SubagentStop)
  4. Did it try to write or run things? (Write / Edit / Bash events)
It is a readback of observed events, not a judgement of output quality.
"""

from __future__ import annotations

import json
import sys
from collections import Counter
from pathlib import Path

READ_TOOLS = {"Read", "Glob", "Grep"}
WRITE_TOOLS = {"Write", "Edit", "MultiEdit", "NotebookEdit", "Bash"}
SUBAGENT_TOOLS = {"Task", "Agent"}


def load(path: Path) -> list[dict]:
    events = []
    for line in path.read_text(encoding="utf-8").splitlines():
        line = line.strip()
        if line:
            try:
                events.append(json.loads(line))
            except json.JSONDecodeError:
                continue
    return events


def newest_trace() -> Path | None:
    candidates = sorted(Path("trace").glob("*.jsonl"), key=lambda p: p.stat().st_mtime)
    return candidates[-1] if candidates else None


def main() -> int:
    path = Path(sys.argv[1]) if len(sys.argv) > 1 else newest_trace()
    if path is None or not path.exists():
        print("No trace file found. Run the agent once with the starter hooks installed.")
        return 2
    events = load(path)
    tools = Counter(e.get("tool") for e in events if e.get("tool"))
    reads = [e for e in events if e.get("tool") in READ_TOOLS]
    writes = [e for e in events if e.get("tool") in WRITE_TOOLS]
    subagents = [e for e in events if e.get("tool") in SUBAGENT_TOOLS or e.get("event") == "SubagentStop"]
    prompts = [e for e in events if e.get("event") == "UserPromptSubmit"]

    print(f"Trace: {path}  ({len(events)} events)")
    print()
    print("1. Human asked")
    for e in prompts or [{}]:
        print(f"   - {e.get('prompt') or 'OPEN — no UserPromptSubmit event recorded'}")
    print()
    print("2. Sources read (in order)")
    for e in reads:
        print(f"   - {e['ts']}  {e['tool']:<5} {e.get('summary','')}")
    if not reads:
        print("   - none recorded")
    print()
    print("3. Subagents")
    for e in subagents:
        label = e.get("event") if e.get("event") == "SubagentStop" else e.get("tool")
        print(f"   - {e['ts']}  {label:<13} {e.get('agent_type') or ''} {e.get('summary','')}")
    if not subagents:
        print("   - none recorded")
    print()
    print("4. Writes, edits, or shell commands")
    for e in writes:
        print(f"   - {e['ts']}  {e['tool']:<6} {e.get('summary','')}")
    if not writes:
        print("   - none recorded (preview-only run)")
    print()
    print("Tool counts: " + ", ".join(f"{k}={v}" for k, v in tools.most_common()) )
    stop = [e for e in events if e.get("event") == "Stop"]
    print(f"Stop events: {len(stop)}; final message length: {stop[-1].get('last_message_chars') if stop else 'OPEN'} chars")
    print()
    print("OPEN: the trace shows which tools ran, not whether the output is correct. Use the checker and a human review for that.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
