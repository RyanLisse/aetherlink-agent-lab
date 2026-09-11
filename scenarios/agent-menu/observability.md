# Observability — understanding what the agent did

"It gave an answer" is not evidence. In this lab you can always show **what
happened**: which prompt started the run, which files the agent read and in
what order, which subagents ran, whether anything was written or executed, and
where the run stopped. Three views give you that.

## 1. The trace file (hook-based, local)

The starter's `.claude/settings.json` runs `.claude/hooks/trace_hook.py` on
four Claude Code hook events. Each event appends one JSON line to
`trace/<session_id>.jsonl` in your checkout.

| Hook event | What the line tells you |
| --- | --- |
| `UserPromptSubmit` | the exact prompt a human typed (first 200 characters) |
| `PostToolUse` | tool name, its target (file path, pattern, command, or subagent description), and the size of what came back |
| `SubagentStop` | a subagent finished, and which type |
| `Stop` | the main agent finished, and how long its final message was |

The hook copies **no file contents and no model text** into the trace — only
the shape of the run. It exits 0 and prints nothing, so it can never change
the agent's behaviour. Contract: <https://code.claude.com/docs/en/hooks>.

Read it with:

```sh
python3 scenarios/agent-menu/tools/trace_summary.py            # newest trace
python3 scenarios/agent-menu/tools/trace_summary.py trace/<id>.jsonl
```

The summary prints the four questions to answer in your run log:

1. **What did the human ask?**
2. **Which sources did the agent read, in which order?** Compare with the
   sources your output cites. A cited file that was never read is a finding.
3. **Which subagents ran and stopped?**
4. **Did it write, edit, or run anything?** For every menu agent the expected
   answer is "none recorded (preview-only run)".

## 2. The transcript (built into Claude Code)

In the Claude Code session, expand a tool call to see its full input and
result. The transcript path is also in every trace line's source payload
(`transcript_path`), for anyone who needs the complete record. Use the trace
for the story and the transcript for the detail.

## 3. The checker and the human gate

`check_menu_output.py` proves the output has the contract's shape and that
cited paths or issue keys exist. Your review proves the content. Record all
three in the run log: trace summary, checker result, human decision.

## What the trace cannot prove

- that the content is correct, or that arithmetic was right;
- that the model "understood" anything — it records tools, not reasoning;
- anything about a run that happened without the hooks installed.

Say `OPEN` for those, exactly as on Day 3.

## Reading exercise (Day 5, 10 minutes, groups of 3–4)

Swap trace summaries with a neighbour who chose a different option. Without
looking at their output, tell them: what they asked, the first file their
agent read, whether a subagent ran, and whether anything was written. Then
check against their output's citations. One mismatch found = one lesson for
the handoff.
