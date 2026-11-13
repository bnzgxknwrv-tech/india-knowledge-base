# INDIA ↔ CCI — LIGHT COLLABORATION RULES

Status: active for INDIA10+
Effective: 2026-08-23

This is a personal travel research project. CCI is a second pair of eyes and worker, not a compliance department.

## Roles
- INDIA: regisseur/architect, decides sequencing, evaluates worker output, protects canon, integrates useful results.
- CCI: bounded researcher/worker/reviewer, may challenge INDIA, reports uncertainty clearly.
- Mark: decides personal A/B/C, hotel/base and other subjective travel choices. Mark is not the courier between INDIA and CCI.

## Default working pattern
`INDIA task -> CCI worker/review -> INDIA judgment -> central update when useful`

CCI normally works on a worker/task branch or read-only review. Direct central writes are exceptional, not the default.

## Polling
INDIA checks PR #23 only at two routine checkpoints:
1. before starting a major new build or architecture pass;
2. immediately before writing to the central regie branch.

If INDIA knows a CCI result is already pending and is about to send a long/final answer, a quick extra check is sensible, but this is judgment rather than ceremony.

## Task quality
A CCI task should state enough to avoid guessing: goal, relevant read scope, allowed writes/branch, protected Mark decisions, desired output and stop condition. Do not create elaborate contracts when a short bounded instruction is clear enough.

## Review
One CCI sanity review is normally enough for a material architecture or central-integration change. Re-review only meaningful fixes, not unchanged work.

CCI's PR #23 result comment is the review record. No separate cryptographic receipt or duplicate proof-of-review file is required.

## Central update safety
Before a central write:
- protected Mark canon is not silently changed;
- no unauthorized permanent-ID/A/B/C/lock mutation is introduced;
- branch comparison shows a normal non-force fast-forward or another explicitly understood safe integration path.

## Stop rule
If additional governance would mainly verify the governance itself rather than improve travel research, handoff quality or protection of Mark's decisions, stop optimizing.
