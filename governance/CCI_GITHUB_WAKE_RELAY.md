# CCI GITHUB WAKE RELAY — PROVEN BEHAVIOR

Status: CANONICAL OBSERVED BEHAVIOR
Observed: 2026-08-18

## Proven trigger
A new top-level PR comment on the relay PR (#23) generates a Claude Code external wake event of the form:

`<wake reason="external-event">`
with
`source="github" kind="issue_comment.created"`.

This was directly observed for `CCI_TASK 087R`.

## Operational rule
- INDIA posts the next `CCI_TASK` once as a top-level PR #23 comment.
- That comment itself is the wake trigger; Mark does NOT need to manually start Claude Code after INDIA has posted the task.
- Do not post duplicate recovery/tasks merely because no result is visible yet; duplicate wake events can create duplicate work.
- CCI reads GitHub durable state/checkpoints and returns `CCI_RESULT` to PR #23.
- If a Claude Code session hits max-context, create one recovery `CCI_TASK` that explicitly resumes from committed state and forbids restarting completed work.

## Precision / non-assumption
The observed evidence proves `issue_comment.created` on the relay PR as a wake trigger. It does NOT by itself prove that every arbitrary repository file commit triggers Claude Code. Therefore use PR #23 task comments as the explicit execution relay.

## Human-touch rule
Mark is not the message bus for routine CCI work. INDIA writes the CCI task to GitHub; CCI is automatically woken by the PR comment; INDIA later reads the returned result from GitHub.
