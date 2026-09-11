# Daily branch map

Branches make the day's scope visible to participants. They do not replace
the human review gate.

## Squad 2

| Branch | Work focus | Required handoff |
| --- | --- | --- |
| `squad-2/day-1` | AI-native SDLC foundations and intent | Intent, success criteria, lifecycle map, and human gate |
| `squad-2/day-2` | AI-native SDLC feedback loop | Small plan, positive and negative checks, and handoff |
| `squad-2/day-3` | First bounded n8n GitLab repository review | Workflow settings, findings, reviewer, and `OPEN` checks |
| `squad-2/day-4` | Same repository review in Claude Code | Read-only trace, checker result, and comparison |
| `squad-2/day-5` | Own team issue end to end | Issue brief, evidence, human gate, and handoff |

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
