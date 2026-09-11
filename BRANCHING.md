# Daily branch map

Branches make the day's scope visible to participants. They do not replace
the human review gate.

## Squad 2

| Branch | Work focus | Required handoff |
| --- | --- | --- |
| `squad-2/day-1` | First local GitLab repository-review note | Source paths, finding, reviewer, and `OPEN` checks |
| `squad-2/day-2` | Same review agent in n8n and Claude Code | Two settings/output records and comparison |
| `squad-2/day-3` | Analyst → developer → tester relay | Role-preserving review packet |
| `squad-2/day-4` | Runbook and shared-skill handoff | Fresh-reader reproduction and mock GitLab fields |
| `squad-2/day-5` | Independent second review scope | Reproducible note and next owner |

## Squad 1 continuation

`squad-1/day-3`, `squad-1/day-4`, and `squad-1/day-5` preserve the existing
payment-operations ticket route. Use those branches only for that route.

## Daily commands

```sh
git fetch origin
git switch squad-2/day-1
git status
```

Replace the branch name with the current day. Commit only the learner's local
notes, evidence, and approved demo changes. Push only when the facilitator has
asked for a branch readback. Never commit credentials, customer data, or real
GitLab/Jira/Confluence records.
