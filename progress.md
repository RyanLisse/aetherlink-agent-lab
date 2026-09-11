# Progress

Status: `TEMPLATE — replace with the latest verified participant state`

This is a current-state board, not a diary.

## Current verified state

- Repository structure: `VERIFIED — local templates, synthetic fixtures, route-specific checkers`
- n8n workflow import: `OPEN — learner must import the branch workflow in the n8n UI`
- n8n execution: `OPEN — requires learner-selected model credential and human readback`
- Claude Code preview: `OPEN — requires a learner run in the checkout`
- Route contract: `VERIFIED — Squad 1 ticket-coach and Squad 2 repository-review contracts are documented in intent.md`
- Last independently rechecked artifact: `n8n/workflows/repo-reviewer.json` parses as JSON; no live execution claimed

## Blockers

| Blocker | Mechanism or impact | Owner | Evidence | Status |
| --- | --- | --- | --- | --- |
| No live model credential or execution readback | n8n and Claude Code runs cannot be claimed from static files | Learner operator | n8n UI and local run log | `OPEN` |

## Next actions

| Action | Owner | Due | Acceptance check | Evidence |
| --- | --- | --- | --- | --- |
| Import the route workflow and select a model credential in the UI | `Learner operator` | `YYYY-MM-DD` | Selected workflow executes and its route-specific output passes the checker | `OPEN` |
| Run the Claude equivalent with the same route input and prompt | `Learner operator` | `YYYY-MM-DD` | Ticket or repository-review contract passes its checker | `OPEN` |
| Record the human review and unresolved questions | `Reviewer` | `YYYY-MM-DD` | Source paths, output, reviewer, and `OPEN` items are readable from the run log | `OPEN` |

## Evidence links

- n8n execution: `OPEN`
- Claude preview/output: `OPEN`
- Human review: `OPEN`
