# AetherLink agent lab

This repository is a small participant lab for one bounded fictional payment
operations ticket. Build the same ticket-coach twice: first in n8n, then in
Claude Code. It contains templates, synthetic inputs, importable demo material,
and a shape checker. It does not contain a course schedule, trainer answer key,
facilitator notes, private feedback, or live team integrations.

Clone this repository once for the participant workspace:

```sh
git clone https://github.com/RyanLisse/aetherlink-agent-lab.git
cd aetherlink-agent-lab
```

## Daily branches

Use one branch for each training day. The branch tells you the current scope
before you start editing. Do not work directly on `main`.

| Training route | Branches | Start each day with |
| --- | --- | --- |
| Squad 2 | `squad-2/day-1` through `squad-2/day-5` | `git switch squad-2/day-N` |
| Squad 1 continuation | `squad-1/day-3` through `squad-1/day-5` | `git switch squad-1/day-N` |

Commit your evidence and notes on the day's branch. At the end of the day,
push that branch if the facilitator asks for a shared readback. The facilitator
reviews the branch before merging or carrying work into the next day. A branch
contains learner work only; `main` remains the clean starting template.

The branches are signposts, not proof that an agent ran. Record commands,
outputs, reviewer, and `OPEN` gaps in `progress.md` and the daily run log.

## Quickstart

1. Switch to the branch named for today's squad and day, then read
   [intent.md](intent.md) and [progress.md](progress.md), and fill the
   participant owners and today's boundary.
2. Read [the ticket input](scenarios/ticket-agent/ticket-inputs.md) and [the
   output contract](scenarios/ticket-agent/ticket-template.md). Use
   `TICKET-OPS-101` for this first run.
3. Build and run the n8n version using [the n8n quickstart](n8n/README.md).
   Import [the workflow JSON](n8n/workflows/ticket-coach.json), select a model
   credential in the UI, and record the execution readback.
4. Build and preview the same contract with the Claude Code starter using [the
   ticket-agent guide](scenarios/ticket-agent/README.md).
5. Run the checker on a human-previewed output. The checker confirms shape only;
   it does not prove that either agent ran or that the content is correct.
6. On Day 4 choose one agent from [the agent menu](scenarios/agent-menu/README.md),
   install its starter (subagents plus a trace hook), and build it step by step.
   On Day 5 harden it with the `evaluator` subagent and hand it over.

The first exercise is deliberately bounded. Do not connect a remote Jira,
GitLab, Confluence, PSP, bank, or production repository. Do not approve a
payout. Keep unsupported explanations and missing evidence as `OPEN`.

## Contents

| Path | Purpose |
| --- | --- |
| [intent.md](intent.md) | Empty participant outcome and evidence contract |
| [progress.md](progress.md) | Empty current-state board |
| [n8n/README.md](n8n/README.md) | Import, UI setup, smoke test, and evidence steps |
| [n8n/workflows/ticket-coach.json](n8n/workflows/ticket-coach.json) | Credential-free importable n8n demo (Anthropic chat model by default; provider swappable in the UI) |
| [scenarios/ticket-agent/](scenarios/ticket-agent/) | Same ticket input, shared instruction, contract, starter, examples, and checker |
| [scenarios/agent-menu/](scenarios/agent-menu/) | Day 4–5 menu: choose one of three Claude Code agents (plus a stretch option), trace hooks, evaluator, checker |
| [scenarios/payment-reconciliation/data/](scenarios/payment-reconciliation/data/) | Synthetic ledger, PSP, and bank CSVs for optional local context |
| [scenarios/payment-reconciliation/tickets/](scenarios/payment-reconciliation/tickets/) | Six fictional FIN-001–FIN-006 ticket templates |
| [templates/](templates/) | Session, recap, knowledge, decision, handoff, and run-log forms |
| [BRANCHING.md](BRANCHING.md) | Daily branch map and handoff rules |

All amounts are fictional integer minor EUR values. Examples are discussion
material and never learner evidence.

Worked ticket outputs are intentionally included as learner examples. They are
labelled examples, not observed run results or the full reconciliation trainer
answer key. Try the ticket yourself before comparing your draft with them.
