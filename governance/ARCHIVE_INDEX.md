# ARCHIVE INDEX — WHERE TO FIND DEPTH, AND WHAT NOT TO RE-READ BY DEFAULT

Status: **ON-DEMAND — not required boot reading, use as a lookup table**
Built: 2026-09-14, as part of the successor-boot slimming (PR #23); updated the same day when the slim was found too aggressive and partly restored (see `governance/HOW_TO_WORK_WITH_MARK.md`'s history).

This is a map of everything outside the active cockpit — currently `BOOT_MANIFEST_V8.json`'s 15-file `central_required`: `FRESH_SESSION_BOOT_GATE.md`, `INDIA_MASTER_BOOT.md`, `CURRENT_TRUTH.md`, `CURRENT_FRONTIER.md`, `HOW_TO_WORK_WITH_MARK.md`, `GUARDRAILS.md`, `MARK_TRAVEL_PREFERENCES_CURRENT.md`, `INDIA_BEHAVIORAL_EXECUTION_CONTRACT.md`, `INDIA_ACTIVE_MEMORY_COMPILATION_GATE.md`, `MARK_LOCATION_NAMING_CONTEXT_PROTOCOL.md`, `INDIA_HUMAN_CENTERED_COMPLEX_TRIP_PLANNING_STANDARD.md`, `MARK_PERSON_PROVENANCE_PLACE_MEANING_RULE.md`, `MARK_FACING_PLACE_CARD_TRAVEL_VALUE_RULE_2026-09-13.md`, `MARK_DAY_BLOCK_ONLY_PDF_RULE_2026-09-13.md`, `MARK_TO_INDIA_SUCCESSOR_HUMAN_HANDOFF.md`. Nothing listed here was deleted or judged worthless — it's classified so a fresh successor knows what to leave alone versus what to open when a specific need arises.

**MUST NOT DELETE** applies to everything below unless a row says otherwise: this is provenance for a real personal trip, git history costs nothing to keep, and past incidents in this project were caused by losing knowledge, never by keeping too much of it.

## CLASSIFICATION KEY

- **ACTIVE NOW** — genuinely live work; check current status on PR #23 before touching.
- **ON-DEMAND EVIDENCE** — settled, but keep the sources for when a grade/claim/route reasoning is questioned.
- **HISTORICAL / SUPERSEDED** — an earlier attempt or dump, folded into current truth; read only for "why did we decide this" archaeology.

## GOVERNANCE FILES

| File(s) | Class | Note |
|---|---|---|
| `CURRENT_STATE.md`, `CURRENT_DECISIONS_MASTER.md`, `SUCCESSOR_SAFE_STATE.md` | HISTORICAL/SUPERSEDED | Replaced by `CURRENT_TRUTH.md`/`CURRENT_FRONTIER.md`. `CURRENT_STATE.md` and `SUCCESSOR_SAFE_STATE.md` must keep existing on disk with their exact current technical fields — a validator checks them directly, see `BOOT_MANIFEST_V8.json`'s notes. |
| `INDIA_CURRENT_KNOWLEDGE_MAP.md`, `INDIA_RECOVERY_DELTAS_CURRENT.md` | HISTORICAL/SUPERSEDED | Large recovery/routing dumps, content now in `CURRENT_TRUTH.md`. `INDIA_CURRENT_KNOWLEDGE_MAP.md` must keep existing on disk (validator cross-reference check). |
| `INDIA_BEHAVIORAL_EXECUTION_CONTRACT.md`, `INDIA_ACTIVE_MEMORY_COMPILATION_GATE.md`, `MARK_LOCATION_NAMING_CONTEXT_PROTOCOL.md`, `INDIA_HUMAN_CENTERED_COMPLEX_TRIP_PLANNING_STANDARD.md`, `MARK_PERSON_PROVENANCE_PLACE_MEANING_RULE.md`, `MARK_FACING_PLACE_CARD_TRAVEL_VALUE_RULE_2026-09-13.md`, `MARK_DAY_BLOCK_ONLY_PDF_RULE_2026-09-13.md` | **ACTIVE NOW (cockpit, restored 2026-09-14)** | Briefly moved to on-demand during the first slimming pass, then restored to `central_required` the same day after a confirmed `READ_COMPLETE != MARK_WORKING_MODEL_ACTIVE` failure. `GUARDRAILS.md`/`HOW_TO_WORK_WITH_MARK.md` summarize parts of these but do not replace them — read these in full. |
| `MAP_COORDINATE_VERIFICATION_RULE.md`, `FINAL_COMFORT_SWEEP_RULE_2026-08-23.md`, `EXACT_DELEGATION_BINDING_RULE.md` | ON-DEMAND EVIDENCE | Full reasoning/examples behind the condensed rules in `GUARDRAILS.md`. Read only if the condensed version is unclear or contested. These three were NOT restored to central_required — the 2026-09-14 hardening only restored the Mark-behavioral/naming/planning-standard files, not the geo/comfort/delegation ones. |
| `TRIP_FRAME_HARD.md` | ON-DEMAND EVIDENCE | Hard envelope content is in `CURRENT_TRUTH.md`. Note: this file claims a validator checks a "protected canon" blob-SHA anchor here — that check does not actually exist in `validate_successor_boot.py` today. Flagged as a stale claim, not fixed in this pass (see final report). |
| `INDIA14_START_AND_INDEPENDENT_CHECK.md` | ACTIVE NOW (mechanical) | Still the live procedure for CHECK-tier determination; not required as content-knowledge reading, but the receipt/CHECK mechanism still uses it. |
| `MARK_TRAVEL_PREFERENCES_CURRENT.md` | **ACTIVE NOW (cockpit, restored 2026-09-14)** | The full "why Mark feels this way" layer. Briefly moved out of the mandatory boot, then restored the same day — `HOW_TO_WORK_WITH_MARK.md` §15 summarizes it but does not replace it. |
| `DECISION_LEDGER.jsonl` | ON-DEMAND EVIDENCE | Append-only, one event per line. Consult when a specific decision's exact history/timing matters. |
| `ACTIVE_FRAMEWORK.md`, `ACTIVE_STATE.md` | HISTORICAL/SUPERSEDED | Already self-marked deprecated by an earlier session (2026-09-02); left as-is. |
| `HANDOFF_INDIA6_TO_INDIA7_2026-08-19.md`, `INDIA7_BOOTSTRAP_DELTA_2026-08-18.md`, `INDIA7_BOOTSTRAP_DELTA_2026-08-19.md`, `INDIA8_REGIE_READINESS_AUDIT_2026-08-23.md`, `INDIA9_CANON_RECONCILIATION_2026-08-23.md`, `INDIA11_RECOVERY_POSTMORTEM_AND_MUST_READ_2026-08-26.md` (already marked RETIRED), `INDIA12_FINAL_SUCCESSOR_CHECKPOINT_2026-08-29.md`, `INDIA14_TO_INDIA15_HANDOFF_2026-09-01.md`, `INDIA_ROUTE_TOPOLOGY_CHECKPOINT_2026-08-26.md`, `INDIA_SUCCESSOR_BOOT_PROTOCOL.md`, `INDIA_SUCCESSOR_CRASH_TEST_3PASS_2026-09-09.md` | HISTORICAL/SUPERSEDED | Session-transition dumps from earlier INDIA generations. Genuine audit trail; not needed for current work. |
| `INDIA_TRAIN_BOOKING_ROUND_CURRENT.md` | ON-DEMAND EVIDENCE | Pre-booking-phase train notes; relevant again once the booking/contact phase opens (see `CURRENT_FRONTIER.md`). |
| `MARK_INDIA_PACKING_LIST_CURRENT.md` | ACTIVE NOW | Canonical packing list; keep appending here. |
| `MARK_PACKING_LIST_CURRENT.md` | HISTORICAL/SUPERSEDED | Found to be an independent duplicate of the packing list above; now points to it. |
| Every other dated `governance/*_2026-*.md` rule/decision file not named above | ON-DEMAND EVIDENCE | Point-in-time rules and corrections, already folded into `CURRENT_TRUTH.md`/`GUARDRAILS.md`/`HOW_TO_WORK_WITH_MARK.md` where they still matter. |

## `decisions/` AND `research/`

**ON-DEMAND EVIDENCE**, all of it. Every file there is a real, dated Mark decision or research finding; `CURRENT_TRUTH.md` already reflects the current state of every one that still matters for planning. Open one only when a specific grade, exclusion or claim is questioned and you need the original reasoning/source.

## `runs/active/`

| Group | Class | Note |
|---|---|---|
| `WORK_KUMAON_CRANKS_RIDGE_GOVINDA_FINAL_BASE_CORRIDOR_SOLVE_2026-09-14.md`, `KUMAON-ORIGINAL-SWEEP-RECOVERY-2026-09-14.md`, `KUMAON-NORTH-CORRIDOR-SLEEPBASE-ENROUTE-OPTIMIZATION-2026-09-14.md`, `KUMAON-V2-RESWEEP-001/` | ON-DEMAND EVIDENCE | Source material behind the current Kumaon section of `CURRENT_TRUTH.md`. The live Kumaon 20–23 Dec solve itself runs as a separate WORK task (PR #23 comment `5670452609`) — see `CURRENT_FRONTIER.md`. |
| `INDIA20-LIVE-LEDGER-V4-REPAIR-001/` | ACTIVE NOW (background) | An internal memory-completeness check (making sure no B/C/Open place quietly disappears from records) — a housekeeping task, not a Mark-facing decision. Still technically open; does not block any current A-timing work. |
| `TOP11-*` (11 directories) | HISTORICAL/SUPERSEDED | Person-provenance research sweeps; marked complete, folded into current grades. |
| `INDIA8-*` (10 directories, Aug 2026) | HISTORICAL/SUPERSEDED | Early cluster-casting/decision work; folded into current grades. |
| `INDIA9-SUCCESSOR-BOOT-2026-08-23/`, `INDIA10-*` (5 directories), `INDIA11-SUCCESSOR-CHECKPOINT-2026-08-26/` | HISTORICAL/SUPERSEDED, except the Bodh Gaya duration question | `INDIA10-CLUSTER-COVERAGE-REAUDIT-001/` specifically still has residual value for the still-open Bodh Gaya 2-vs-3-night question (see `CURRENT_FRONTIER.md`) — consult it there, not by default. |
| `INDIA17-PARALLEL-ROUTE-RESEARCH-001/`, `INDIA18_FINAL_EXTRACTION_2026-09-09.md`, `INDIA19-*` (3 items), `INDIA20-FINAL-EXTRACTION*` (2 files) | HISTORICAL/SUPERSEDED | Successor handoff dumps; content now in `CURRENT_TRUTH.md`. Valuable "why" archaeology only. |
| `GLOBAL_ROUTE_TOPOLOGY_REOPTIMIZATION_*` (2 files), `FOUR_AI_ROUTE_RECONCILIATION_RESULT_2026-09-09.md`, `SIX_AI_ROUTE_RECONCILIATION_TASK_2026-09-09.md`, `FINAL_MULTI_AI_PROMPT_PACKAGE_2026-09-07.md` | HISTORICAL/SUPERSEDED | Macro route-solve artifacts; explicitly complete, not to be restarted (see `GUARDRAILS.md`). |
| `AOAY-FULL-LOCATION-ATLAS-001/`, `BODHGAYA-DISCOVERY-001/`, `GAYA-AIRPORT-BODHGAYA-CORRIDOR-001/`, `INDIAHOTEL-BODHGAYA-001/`, `TIRUVANNAMALAI-ARUNACHALA-CLUSTER-001/`, `VARANASI-GEO-DELIVERY-REPAIR-001/`, `YOGANANDA-ANANDAMAYI-PHOTO-LOCATION-001/`, `INDIAZILVER-ENTITY-ID-PROXIMITY-BACKFILL-001/`, `INDIA-LEGACY-EXTRACTION-001/` | HISTORICAL/SUPERSEDED | Region/topic-specific discovery work, folded into current grades in `CURRENT_TRUTH.md`. |

## BRANCHES AND PR #23

- `agent/india8-cluster-casting` is the one active working branch. Everything else — the many `worker/*`, `agent/india9-*`, `agent/india10-region-*`, `agent/india17-dr-*`, `run/*`, `transition/*`, `worktree-agent-*` branches, and dozens of others — is historical/parallel-audit work. **A fresh successor must not crawl these by default.** They stay as archive; nothing is deleted; no objective safety/benefit case was made in this pass for deleting any of them, which is the bar for removing one.
- PR #23 (currently ~490+ comments) is the historical relay/discussion channel between Mark, INDIA and CCI. A fresh successor does not need to read it back to front — `CURRENT_TRUTH.md` and `CURRENT_FRONTIER.md` already carry forward everything that matters from it. Open specific comments only when a specific claim needs its original wording.
- No new worker/redteam/cross-audit/independent-solve branch should be created unless CCI and INDIA jointly agree there's a real content blocker that the current compact cockpit can't resolve (see `CURRENT_TRUTH.md`'s project-level agreements).

END ARCHIVE INDEX
