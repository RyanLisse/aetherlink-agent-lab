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

## Quickstart

1. Read [intent.md](intent.md) and [progress.md](progress.md), then fill the
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

The first exercise is deliberately bounded. Do not connect a remote Jira,
GitLab, Confluence, PSP, bank, or production repository. Do not approve a
payout. Keep unsupported explanations and missing evidence as `OPEN`.

## Contents

| Path | Purpose |
| --- | --- |
| [intent.md](intent.md) | Empty participant outcome and evidence contract |
| [progress.md](progress.md) | Empty current-state board |
| [n8n/README.md](n8n/README.md) | Import, UI setup, smoke test, and evidence steps |
| [n8n/workflows/ticket-coach.json](n8n/workflows/ticket-coach.json) | Credential-free importable n8n demo |
| [scenarios/ticket-agent/](scenarios/ticket-agent/) | Same ticket input, shared instruction, contract, starter, examples, and checker |
| [scenarios/payment-reconciliation/data/](scenarios/payment-reconciliation/data/) | Synthetic ledger, PSP, and bank CSVs for optional local context |
| [scenarios/payment-reconciliation/tickets/](scenarios/payment-reconciliation/tickets/) | Six fictional FIN-001–FIN-006 ticket templates |
| [templates/](templates/) | Session, recap, knowledge, decision, and handoff forms |

All amounts are fictional integer minor EUR values. Examples are discussion
material and never learner evidence.

Worked ticket outputs are intentionally included as learner examples. They are
labelled examples, not observed run results or the full reconciliation trainer
answer key. Try the ticket yourself before comparing your draft with them.
