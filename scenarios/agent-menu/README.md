# Agent menu — Day 4 build, Day 5 harden (Claude Code)

On Day 3 everyone built the same `ticket-coach`. On **Day 4 you choose one
agent** from this menu and build it step by step. On **Day 5 you harden the
same agent**: add an evaluator, read your own trace, and hand it over so a
fresh reader can reproduce it. Everything is local, fictional, and read-only
for the agent; you decide what to save.

| Option | Agent | Input it reads | Output it returns | Closest real task |
| --- | --- | --- | --- | --- |
| A | [`ticket-triage`](ticket-triage/README.md) | six `FIN-00n` tickets + CSV rows | Jira-shaped triage report per ticket | grooming the queue before stand-up |
| B | [`runbook-writer`](runbook-writer/README.md) | one reviewed run log + templates | Confluence-shaped runbook | turning a done ticket into a procedure |
| C | [`repo-reviewer`](repo-reviewer/README.md) | this repository's docs and data | findings report with file evidence | reviewing a merge request for consistency |
| Stretch | [`retro-writer`](retro-writer/README.md) | fictional Jira sprint export | retro draft with themes and actions | preparing the sprint retro |

Pick by the work you want to be faster at next week, not by difficulty; all
four use the same tools (`Read`, `Glob`, `Grep`) and the same rules. Groups
of 3–4 form **after** the individual block and are strongest when the group
mixes two different options.

## Install the starter once (Day 4, 5 minutes)

From your `aetherlink-agent-lab` checkout root:

```sh
cp -Rn scenarios/agent-menu/starter/.claude .claude
ls .claude/agents .claude/hooks .claude/settings.json
```

You now have five project subagents (`ticket-triage`, `runbook-writer`,
`repo-reviewer`, `retro-writer`, `evaluator`) and a hook that writes a trace
of every tool call to `trace/<session>.jsonl`. Start Claude Code in the
checkout root so it loads `.claude/settings.json`; if it was already running,
restart it. Nothing is committed: `/.claude/`, `trace/`, and
`participant-output/` are ignored.

## The same loop for every option

```
goal + contract  →  agent observes sources  →  decides one bounded step
→  tool action (Read/Glob/Grep)  →  you inspect the trace and the preview
→  repeat, or stop at the human gate (you accept, park, or redirect)
```

Rules that never change: the agent previews in chat and writes nothing; you
save what you accept under `participant-output/`; every claim cites a file
or row; unsupported details are `OPEN`; no Jira, GitLab, Confluence, PSP, or
bank record is created, changed, or implied.

## Day 4 — build (individual 25 min, then groups of 3–4)

1. Open your option's README. Read the **contract** and the **task cards**.
2. Fill `templates/run-log.md` header: option, model shown, tools, input.
3. Run the **first prompt** from the README. Preview only.
4. Run `python3 scenarios/agent-menu/tools/trace_summary.py` and answer the
   four questions it prints (asked, read, subagents, writes).
5. Save the preview you accept to `participant-output/<option>.md` yourself.
6. Run the checker: `python3 scenarios/agent-menu/tools/check_menu_output.py --agent <name> --output participant-output/<option>.md`.
7. Record PASS/FAIL/OPEN and one observed line in your run log.

## Day 5 — harden (evaluator-optimizer)

1. Run the `evaluator` subagent on your saved output and the option README.
2. If `REVISE`, apply **only** its numbered instructions by re-prompting your
   agent (the optimizer step). Maximum two rounds. Keep both traces.
3. Compare trace 1 and trace 2: what did the agent read differently?
4. Write the handoff with `templates/handoff.md`; a fresh reader must
   reproduce your run from it in ten minutes without asking you.

See [observability.md](observability.md) for how to read a trace and what it
can and cannot prove.
