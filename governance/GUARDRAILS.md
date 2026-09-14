# GUARDRAILS — THE HARD RULES THAT PREVENT REPEATED FAILURES

Status: **ACTIVE COCKPIT — read this before your first substantive reply**
Last updated: 2026-09-14

This file condenses the actual hard rules from several older, much longer governance files into one place. The originals stay as archive with their full reasoning, incident history and worked examples — read them only if something here is genuinely unclear or contested:
`governance/INDIA_BEHAVIORAL_EXECUTION_CONTRACT.md`, `governance/INDIA_ACTIVE_MEMORY_COMPILATION_GATE.md`, `governance/EXACT_DELEGATION_BINDING_RULE.md`, `governance/MAP_COORDINATE_VERIFICATION_RULE.md`, `governance/FINAL_COMFORT_SWEEP_RULE_2026-08-23.md`, `governance/INDIA_HUMAN_CENTERED_COMPLEX_TRIP_PLANNING_STANDARD.md`, `governance/MARK_TO_INDIA_SUCCESSOR_HUMAN_HANDOFF.md`.

## 1. AUTHORITY ORDER

When sources disagree: newest explicit Mark decision (chat, or a file recording one) > `governance/CURRENT_TRUTH.md` / `governance/CURRENT_FRONTIER.md` > other current durable standards > older frozen CCI/worker analysis > legacy/historical provenance.

If two current sources materially disagree and you can't resolve it from that order, **stop and say so** — don't silently pick one, and don't quietly average them.

## 2. NEVER SILENTLY REOPEN OR RE-PRESENT

- A place Mark graded `C`, or excluded, or a world marked FINAL OUT, stays that way until Mark explicitly reopens it. Seeing an old file that shows an earlier, different status is not permission to reopen — check `CURRENT_TRUTH.md` first.
- Don't confuse a cluster/world-level decision with the site-level grades inside it (dropping a cluster's priority doesn't erase a site's historical grade, and vice versa).
- Research being finished, Mark having triaged it, and a duration being locked are three different states — never treat one as proof of another.

## 3. GEOGRAPHY / COORDINATES

- Never invent a pin or a specific trail/path that isn't backed by a real source. If the exact building/path can't be confirmed, say so and offer the strongest safely-visitable target instead — don't fabricate precision.
- Distinguish an entity's own location from the route/access to reach it.
- Match verification effort to what's actually being decided: a small building needs a real address/listing; a compound/temple needs to know which part is meant; a large area needs a boundary, not a single point.
- Always give whole-human time, not raw map time: drive + realistic walking + dwell + luggage/check-in/check-out + a buffer, and note what a stop displaces elsewhere in the day.

## 4. DELEGATING TO CCI OR WORK

A dispatch to CCI or WORK must bind, explicitly: the PR/comment it's about, the exact task header, the exact commit/artifact it works from, what it must NOT redo, and the exact expected result header. A vague "do the latest task" is not enough once more than one task could be meant. Before sending a new dispatch, check PR #23 for whether that work is already running or already done — don't restart it.

## 5. DURABLE WRITE / CONTINUATION

- Checkpoint every material finding or Mark decision to its correct file in the same work cycle it happens — never leave it living only in chat or only in a PR comment.
- After a session ends, the next one must be able to pick up from GitHub alone. If something feels missing, ask the outgoing session (via Mark) to dump it first — don't reconstruct a guess from git archaeology when the real source might still be reachable.
- If a predecessor's answer is relayed to you and you can't independently verify it came from a real, live session, say so and ask Mark to confirm it himself before treating it as true.

## 6. SESSION-TRANSITION SAFETY NET (LIGHTWEIGHT ORPHAN-SCAN)

Once per fresh boot, do a quick check: is there a file in the repo that calls itself HARD/MANDATORY/MUST-READ but isn't part of the current active cockpit (`CURRENT_TRUTH.md`, `CURRENT_FRONTIER.md`, `HOW_TO_WORK_WITH_MARK.md`, this file)? If you find one that's still genuinely live, use it and fold its essential point into the cockpit files at the next safe moment — don't let it silently rot unread again. This does not mean re-reading the whole historical archive by default.

## 7. WHAT COUNTS AS A REAL PROBLEM WORTH NEW STRUCTURE

Don't add a new governance file, worker branch, redteam, or independent-solve process unless it demonstrably solves a real problem that the current compact cockpit can't. See `governance/CURRENT_TRUTH.md`'s project-level agreements: new parallel branches are frozen by default.

## PRE-ANSWER SELF-CHECK

Before a substantive answer, quickly check:
1. Does this match `CURRENT_TRUTH.md` / `CURRENT_FRONTIER.md`, including anything Mark said moments ago in this chat?
2. Am I about to mention a place without checking whether it's already decided?
3. Am I using recognition-rich names and real whole-human time, per `HOW_TO_WORK_WITH_MARK.md`?
4. Am I using A/B/C/A*/A+ only as real Mark grades, never as structure labels?
5. Is there something I already finished that I should have written to a file, not just said in chat?

Any "no" — fix it before answering, don't answer and fix later.

END GUARDRAILS
