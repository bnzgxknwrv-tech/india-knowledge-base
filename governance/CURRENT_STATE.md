# CURRENT STATE — INDIA

Last updated: 2026-08-23
Purpose: one human-readable page that tells the next INDIA session what is current.

## Project type
This is a personal India travel/pilgrimage knowledge base, not a software product. Governance exists only to prevent expensive repeat work, forgotten Mark decisions and confused handoffs. Prefer simple, recoverable workflows over formal ceremony.

## Start here
1. Read this file.
2. Read `runs/active/INDIAZILVER-ENTITY-ID-PROXIMITY-BACKFILL-001/PROTECTED_CANON_BASELINE.csv` before presenting any location/cluster/hotel/base as a new choice.
3. Read the current task/output files relevant to what Mark is asking now.
4. Check PR #23 back to the last CCI/INDIA exchange you have not handled when starting a major new build.
5. Read older governance/branches only when a concrete inconsistency, provenance question or missing decision requires it.

## Current central regie branch
`agent/india8-cluster-casting`

This branch contains the INDIA9 one-time knowledge-audit imports plus the final LIGHT successor architecture agreed by INDIA9 and CCI. The abandoned heavier candidate branch `agent/india9-successor-architecture-integration` is provenance only and is not a competing current authority.

## Protected canon
Canonical protected decision file:
`runs/active/INDIAZILVER-ENTITY-ID-PROXIMITY-BACKFILL-001/PROTECTED_CANON_BASELINE.csv`

Current protected blob:
`a607241caa41637e2167d0f56781bf663f038932`

Existing Mark decisions, permanent IDs and locks must not be silently changed. A later explicit Mark decision may supersede an earlier one; when that happens, update the durable canon rather than maintaining competing truth files.

## What is active vs historical
- Current Mark decisions/locks + protected canon: ACTIVE.
- Current task `TASK.md`/`STATUS.md` and current travel outputs: ACTIVE when actually relevant to the question.
- Worker branch marked COMPLETE: useful input, but not automatically central truth until integrated or explicitly adopted.
- `governance/ACTIVE_STATE.md`, old handoffs, old pipeline generations, audit read streams and old worker snapshots: provenance/history unless a current file explicitly points to them.
- `governance/PRECEDENCE_MAP.jsonl`, semantic-import and central-integration registries remain audit evidence; they are not required routine reading for every session.

## CCI collaboration
PR #23 is the relay/index. Repo files hold durable substance.

Normal pattern:
`INDIA defines bounded task -> CCI worker/review -> INDIA evaluates -> central update if useful`.

Polling is deliberately light:
- check PR #23 once before starting a major new build;
- check it again immediately before writing to the central regie branch.

No continuous polling. Mark should not need to copy long CCI results between chats when INDIA can read them from GitHub.

## Travel freshness
Do not maintain a global certification status for every live travel fact. Recheck visas, opening/access, timetables, availability, prices and similar changing facts when they are actually about to affect a recommendation or booking decision.

## Good-enough boot rule
A new IndiaN can responsibly continue when it has read:
- this page;
- protected canon;
- the relevant current task/output files;
- any unhandled recent PR #23 exchange that materially affects the task.

If those disagree, read deeper until the conflict is understood. A full-repository reread is an exceptional recovery tool, not the normal start procedure.

## Current architecture status
`INDIA9_SCOPE_SIMPLIFICATION: PASS`
`CCI_FINAL_SANITY_011: PASS`
`STOP_OPTIMIZING: JA`

CCI final review reported validator PASS, protected canon PASS, fast-forward PASS, scope-fit PASS, contradictions NONE and fixes required 0. The next INDIA session should move on to the actual travel/research work rather than further architecture optimization.
