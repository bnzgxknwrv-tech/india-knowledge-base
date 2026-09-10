# INPUT CONTRACT — FROZEN PRE-SOLVE PACKET (PHASE 1)

Status: **PHASE 1 / INPUT FREEZE ONLY — NO ROUTE SOLVE HAS HAPPENED**
Built by: CCI (ClaudeCodeIndia)
Task source: PR #23, INDIA19 dispatch "CCI_TASK — INDIA19 INPUT FREEZE PHASE 1 — BUILD PACKET ONLY", referencing INDIA19_READY_NEXT_TASK comment `5617090677`.
Branch: `agent/india8-cluster-casting`
**Central HEAD/SHA used to build this packet: `8e7419d6120556c8151f2654bce33bcac85ca678`**
Packet directory: `runs/active/INDIA19-FINAL-ITINERARY-REBUILD-001/`
**Packet version: v3 (repaired). v2 = commit `e9e5603c770d822c198045ed3b0002a2fc41ea55`; v1 = commit `c0338559222959d4a2fe4ac67ef5f8bf877c6b58`.**

## PACKET REVISION LOG

- **v3 — 2026-09-10 — CCI repair pass following independent auditor WORK's second `FAIL_WITH_GAPS` review, of v2 (commit `e9e5603c770d822c198045ed3b0002a2fc41ea55`).** WORK confirmed all v2 repairs landed correctly and raised exactly two residual defects, both independently re-verified before acting (see `INPUT_COMPLETENESS_GATE.md` Part A2). (1) `VNS-13`/`VNS-19` (Bhaskarananda Samadhi/Anand Bagh, Tulsi Manas Temple): v2 had left these `CONFLICT_UNRESOLVED`, reasoning the 2026-09-09 file's later date and its own grade-disclaimer "cut both ways." Re-checked directly: that file explicitly states "It does NOT change any Mark grade," so it cannot be read as a fresh regrade regardless of date; the actual latest grade-setting record is `A_PLUS_MARK_DECISION_LOG.md`'s section headed "LATEST VARANASI ORDINARY GRADES — MARK 2026-08-27," which records both as B. Both rows corrected to B and **removed from the CSV** (B is out of scope for this A+/A/A* ledger by design); the two associated `MARK_DECISION_REQUIRED` items removed as invalid (canon repair, not a new Mark choice). (2) The coverage checksum in `LEDGER_SUMMARY.md` incorrectly totalled all 89 CSV rows (including the accommodation row and, at the time, the 2 conflict rows) as `TOTAL_PHYSICAL_A_PLUS_A`; corrected to scope that figure to the actual 86 A+/A/A*-graded population, with the full CSV row count stated separately. Net: total rows 89 → 87 (86 A+/A/A* + 1 accommodation). No Mark grade, lock, or duration was invented on this pass either — see `INPUT_COMPLETENESS_GATE.md` Part A2 for full reasoning and citations.
- **v2 — 2026-09-10 — CCI repair pass following independent auditor WORK's `FAIL_WITH_GAPS` review of v1 (commit `c0338559222959d4a2fe4ac67ef5f8bf877c6b58`).** Every one of WORK's claims was independently re-verified against the actual cited source files (not taken on trust) before any fix was made; see `INPUT_COMPLETENESS_GATE.md` for the full CONFIRMED/DISPUTED/PARTIALLY-CONFIRMED breakdown per gap. Summary of what changed: added 21 previously-omitted physical rows to the coverage ledger (19 Varanasi/Sarnath entities reconciled against `PROTECTED_CANON_BASELINE.csv`/`MARK_DECISIONS_2026-08-02.jsonl`/`A_PLUS_MARK_DECISION_LOG.md`, plus the Bodh Gaya international monastery belt and Gaya Tilkut) — total physical rows 68 → 89; corrected one row's identity from a generic label to its actual sourced name (`BOD-05`, the Ancient Pragbodhi/Dungeshwari stupa ridge); corrected one stale provenance citation (`DEL-02` PVR Priya IMAX, now citing its actual 2026-09-02 supersede decision instead of a superseded 2026-08-31 ledger entry); corrected one grade (`VNS-20` Lahiri Mahasaya family house, A → A+, per an explicit "Mark: A+" baseline entry); flagged two grades as `CONFLICT_UNRESOLVED` rather than guessing (`VNS-13` Bhaskarananda Samadhi, `VNS-19` Tulsi Manas Temple — see the conflict register in `CLOSED_FACTS_OPEN_VARIABLES.md`); corrected three stale/superseded grade claims in `CLOSED_FACTS_OPEN_VARIABLES.md` Category-5 prose (Mangala Gauri Temple B→C, Patharkatti/Sher Shah Suri Tomb "open"→C, Gaya Tilkut "not yet graded"→A*, now its own ledger row); corrected the north/Kumaon start-preference wording in `OBJECTIVE_AND_HUMANE_GATES.md` from "mild tie-break after tiers 1-8" to the actual "strong preference, overridden only by ~8-10+ waking hours of material whole-trip gain" recorded in `decisions/QUIET_NORTH_START_OVERRIDE_THRESHOLD_MARK_DECISION_2026-09-09.md`; removed/reframed the invalid Gate item 7 that treated already-decided A-grade inclusion as an open preference question; added a `STABLE_SOURCE_ID` column to the ledger CSV mapping every row to its immutable canon permanent ID where one exists (see §10 below); improved WHY text for rows WORK correctly flagged as provenance-only. No Mark grade, lock, or duration was invented — every change above is a citation of an existing source, a correction of a stale/incorrect citation, or an explicit unresolved-conflict flag. See `INPUT_COMPLETENESS_GATE.md` for the new overall verdict.
- **v1 — 2026-09-10 (originally built same day as v2, see PR #23 task) — commit `c0338559222959d4a2fe4ac67ef5f8bf877c6b58`.** Original Phase-1 packet build, 68 physical rows, `CONDITIONAL PASS` self-verdict. Superseded in place by v2 above (same files, versioned in place per this project's working-packet convention — not an append-only receipt).

This file pins the binding inputs that any later route/calendar solve (by CCI, WORK or INDIA19) must treat as fixed. It changes nothing; it only freezes and cites current truth.

---

## 1. AUTHORITY / PRECEDENCE RULES

- Newest explicit Mark truth and later-dated decision files outrank stale summaries (`governance/CURRENT_STATE.md` line 13).
- Where `governance/CURRENT_STATE.md` / `governance/SUCCESSOR_SAFE_STATE.md` (both dated 2026-09-09) conflict with `governance/CURRENT_DECISIONS_MASTER.md` / `governance/INDIA_CURRENT_KNOWLEDGE_MAP.md`, the newer of the two wins. At the pinned HEAD, `CURRENT_DECISIONS_MASTER.md` and `INDIA_CURRENT_KNOWLEDGE_MAP.md` are both dated **2026-09-10** and already agree with `CURRENT_STATE.md`/`SUCCESSOR_SAFE_STATE.md` on the two previously-flagged staleness points (Bodh Gaya and Tiruvannamalai duration are correctly shown as LIVE/reopened, not closed). **No stale-content workaround was needed in this packet** — see `CLOSED_FACTS_OPEN_VARIABLES.md` §5 for the full staleness-check trail.
- Only Mark assigns/changes subjective `A+/A/A*/B/C` grades, personal hotel/base selection, subjective dwell/pace and optional-world inclusion (`governance/CURRENT_DECISIONS_MASTER.md` §1; `governance/DECISION_LEDGER.jsonl` DL-0002).
- `RESEARCH_COMPLETE_ENOUGH != MARK_TRIAGE_COMPLETE != DURATION_CLOSED` (DL-0054).
- Worker `COMPLETE` does not equal central adoption; old handoffs/worker files/PR comments are provenance unless reconciled (DL-0037).
- A+/A/A*/B/C letters are reserved exclusively for Mark grades; never used as scenario/option/bundle labels (DL-0056, `decisions/PRESENTATION_GRADE_LETTERS_RESERVED_MARK_RULE_2026-09-02.md`). This packet uses plain Arabic numbers for row IDs only.

## 2. EXACT 33-NIGHT ENVELOPE AND INTERNATIONAL FLIGHTS

- **AI156 AMS -> DEL**: depart 18 Dec 2026 ~20:35, arrive 19 Dec 2026 ~10:15 (already owned/booked by Mark).
- **AI155 DEL -> AMS**: depart 21 Jan 2027 ~12:20 (already owned/booked by Mark).
- Exactly **33 physical India nights**: night of 19 Dec 2026 through night of 20 Jan 2027 inclusive.
- Exactly **one final Delhi night** immediately before AI155, i.e. the night of 20 Jan 2027.
- AI155 safety/failure-tolerance outranks any sightseeing content on 20 Jan (`decisions/NIRMAL_DHAM_FINAL_DELHI_PLACEMENT_MARK_DECISION_2026-09-09.md`).
- Source: `governance/CURRENT_STATE.md` §HARD ENVELOPE; `governance/SUCCESSOR_SAFE_STATE.md` §HARD ENVELOPE; `governance/DECISION_LEDGER.jsonl` DL-0010.

## 3. TRULY LOCKED DURATIONS / PROTECTED DAYS (HARD)

| World | Locked duration | Source |
|---|---|---|
| Nainital | 3 nights | `CURRENT_STATE.md`, `SUCCESSOR_SAFE_STATE.md`, DL-0022 |
| Dunagiri / Kukuchina | 3 nights | same |
| Haidakhan Vishwa Mahadham | 3 nights, **including 2 complete protected quiet days** (not transfer/checkout/logistics days) | DL-0023, `KUMAON_COMPLETE_EXECUTION_DRAFT_2026-08-26.md` |
| Agra | 1 hotel night (current retained architecture); Taj Mahal [A+] protected | DL-0048, `decisions/AGRA_TAJ_ONLY_DEPART_ASAP_MARK_DECISION_2026-09-09.md` |
| Varanasi / Sarnath | 8 nights `LOCKED_BY_MARK` | DL-0026, `VARANASI_DURATION_MARK_DECISION_2026-08-27.md` |
| Final Delhi | exactly 1 night, 20 Jan 2027, immediately before AI155 | `CURRENT_STATE.md`, `decisions/FINAL_DELHI_ONE_NIGHT_MARK_DECISION_2026-09-07.md` |

Kumaon total footprint through the final Dunagiri night = 9 occupied days/nights, `DURATION_CLOSED` (DL-0022); the eastern Kumaon exit is a separate mandatory adjacent travel edge charged once, never twice, when the next fixed-core connection is built.

## 4. OPEN DURATION VARIABLES (LIVE, NOT LOCKED) — DO NOT TREAT AS CLOSED

| World | Live sensitivity | Source |
|---|---|---|
| Bodh Gaya / Gaya | 3 nights strongly supported/current review surface; 2 nights is the comparison baseline. **NOT `TRUE_DURATION_CLOSED`.** | `CURRENT_STATE.md`, `SUCCESSOR_SAFE_STATE.md`, `CURRENT_DECISIONS_MASTER.md` §9 (2026-09-10) |
| Tiruvannamalai / Arunachala | 4 nights is a serious live option; 5 nights is the older state explicitly reopened by Mark on 2026-09-09. Sri Chakra Puja is an optional bonus, not a mandatory anchor and not a Tiru5 veto. | same, `CURRENT_DECISIONS_MASTER.md` §11 |
| Kolkata / Dakshineswar | current serious working block = 3 nights; not itself locked, to be derived from retained content + calendar geometry | `CURRENT_STATE.md`; `decisions/KOLKATA_REMAINING_MARK_GRADES_2026-09-07.md` |
| Chennai | logistics/content buffer only, not a full content world; night count not yet fixed (current working assumption ~1 transport/logistics night) | `INDIA18_FINAL_EXTRACTION_2026-09-09.md` §1.4; `decisions/CHENNAI_BUFFER_AND_EARLY_DELHI_FLIGHT_PREFERENCE_2026-09-07.md` |
| Global macro order (world sequence) | explicitly REOPENED 2026-09-09; incumbent order is a falsification target, not a preferred answer | `decisions/FULL_A_COVERAGE_AND_GLOBAL_ROUTE_TOPOLOGY_REOPTIMIZATION_2026-09-09.md` |

## 5. NIRMAL DHAM — LATEST PLACEMENT/SAFETY RULE

- Nirmal Dham / Shri Mataji Nirmala Devi ashram (Chhawla, southwest Delhi) [A+] remains IN and its grade is unchanged.
- **NOT** planned on arrival day, 19 Dec 2026; 19 Dec is free to be optimized solely for onward movement (no same-day-onward penalty for missing Nirmal on arrival).
- Default placement: final Delhi safety/buffer day, normally **20 Jan 2027**, after domestic positioning into Delhi.
- AI155 flight-safety function outranks Nirmal content; if disruption on 20 Jan consumes the buffer, Nirmal Dham may be shortened or skipped operationally rather than weakening AI155 protection.
- Source: `decisions/NIRMAL_DHAM_FINAL_DELHI_PLACEMENT_MARK_DECISION_2026-09-09.md` (verbatim decision).

## 6. AGRA / TAJ-ONLY RULE

- Taj Mahal [A+] [UNESCO WH] is the **sole** protected fixed-core Agra visit.
- Visit as early as practical (ideally near opening/sunrise), roughly 3–3.5 hours protected dwell.
- After the Taj: **no filler Agra sightseeing** merely to fill time (Agra Fort, Mehtab Bagh etc. remain optional/non-required unless Mark later explicitly promotes them).
- Leave Agra as soon as the first genuinely good whole-human onward connection permits; do not sacrifice a meaningful Taj visit, and do not create a worse daytime-heavy connection merely to leave earlier by the clock.
- Source: `decisions/AGRA_TAJ_ONLY_DEPART_ASAP_MARK_DECISION_2026-09-09.md` (verbatim decision).

## 7. FINAL OUT WORLDS — MUST PRODUCE ZERO LEDGER ROWS

Per `decisions/FINAL_TRIP_WORLDS_LOCK_2026-09-07.md` and reaffirmed by `decisions/FULL_A_COVERAGE_AND_GLOBAL_ROUTE_TOPOLOGY_REOPTIMIZATION_2026-09-09.md` §2, the following are **FINAL EXCLUDED** and must never be re-presented as candidate rows unless Mark explicitly reopens them:

1. **Puri / Odisha** — FINAL EXCLUDED.
2. **Serampore / Srirampur** as a trip stop/world/sleep base/excursion — FINAL EXCLUDED (historical AOAY/Sri Yukteswar provenance is preserved as history, not as a trip candidate).
3. **Vrindavan / Braj / Mathura–Vrindavan–Govardhan** — FINAL EXCLUDED.

Additional final-skipped optional clusters (not FINAL OUT "worlds" in the same sense, but confirmed do-not-re-present unless Mark reopens): Haridwar–Kankhal–Rishikesh; Prayagraj/Allahabad (cluster-level skip; individual pre-existing site grades such as Triveni Sangam [A], Akshayavat [A], Bade Hanuman Ji Temple [A], Red House/4 Church Lane [B] remain preserved as history/provenance, not as active ledger rows — `decisions/FINAL_TRIP_WORLDS_LOCK_2026-09-07.md`, `runs/active/AGRA_GAYA_CORRIDOR_OPERATIONAL_DELTA_RESULT_2026-09-09.md` §2); Mysuru/Mysore–Bengaluru; Kasar Devi–Almora/Crank's Ridge module; Ranchi; Sri Aurobindo Ashram/Puducherry.

**Zero rows for any of the above appear in `PHYSICAL_A_PLUS_A_COVERAGE_LEDGER.csv`.**

## 8. NO-BOOKING / LIVE_RECHECK_LATER BOUNDARY

- No booking, contact, PDF or calendar has been produced in this Phase-1 packet.
- Exact Jan-2027 transport inventory (trains, flights, hotel/ashram acceptance, opening hours, cinema titles, festival dates, weather) is `LIVE_RECHECK_LATER` until decision/booking/calendar-critical (DL-0038; `INDIA18_FINAL_EXTRACTION_2026-09-09.md` §15 gives a consolidated 30-item list of such items — reused here by reference, not reproduced).
- The Agra->Gaya corridor result (`runs/active/AGRA_GAYA_CORRIDOR_OPERATIONAL_DELTA_RESULT_2026-09-09.md`, commit `928052f16edfeaf75aba1e60d8c587036eb94e64` on `worker/agra-gaya-corridor-opportunity-stop`) is a **prior analytical conclusion** (`KEEP_12988_DIRECT`), not a Mark lock. It is classified in `CLOSED_FACTS_OPEN_VARIABLES.md` category 3 and must be treated as reusable evidence for a later solve, not as binding canon.

## 9. PRESENTATION REQUIREMENT

Any later day-card/calendar build must show every retained physical A+/A/A* site **individually**, even where a parent/child pair legitimately shares one visit block — never hidden under a vague cluster label (`governance/CURRENT_STATE.md` §PDF/DAY-CARD RULE; `governance/MARK_TO_INDIA_SUCCESSOR_HUMAN_HANDOFF.md` FOUT 21/22). Cluster status (e.g. "duration live", "world reopened") and individual site grade are separate axes — a cluster being under review never blanks or erases an existing site-level grade.

## 10. STABLE IDENTIFIER MAPPING (ADDED v2, 2026-09-10)

WORK's audit found that this packet's own `VNS-01`, `VNS-02`... row-numbering sequence is a packet-local convenience label, not the project's actual immutable physical-entity ID scheme — e.g. packet `VNS-01` = Manikarnika Ghat, while the real immutable permanent ID for Manikarnika Ghat (`runs/active/INDIAZILVER-ENTITY-ID-PROXIMITY-BACKFILL-001/PROTECTED_CANON_BASELINE.csv`) is `003`, and permanent `001` is a different site (Lahiri Mahasaya Samadhi / Satyalok) that was missing from the packet entirely.

Renumbering the packet's existing `VNS-`/`KUM-`/`BOD-`/`DEL-`/`KOL-`/`TIR-` row IDs to the canon permanent numbers was **not** done on this pass: those IDs are already cross-referenced throughout this packet's own `PARENT_CHILD_RELATION` prose and would require a full internal-reference rewrite for no lossless-reconciliation gain, and several in-scope clusters (Delhi, Agra, Kolkata, Tiruvannamalai) have **no** canon permanent-ID coverage in `PROTECTED_CANON_BASELINE.csv` at all, so a full renumbering could not be uniform anyway.

Instead, `PHYSICAL_A_PLUS_A_COVERAGE_LEDGER.csv` now carries a **`STABLE_SOURCE_ID`** column on every row:
- `PERMANENT-NNN` — the immutable numeric ID from `PROTECTED_CANON_BASELINE.csv` (e.g. `PERMANENT-001`), for every Varanasi/Bodh Gaya/Kumaon entity that has one.
- `LEGACY-<name>` — a legacy (non-global) protected identifier from the same file (e.g. `LEGACY-KAINCHI_EXISTING`), for the few rows that only have a legacy ID.
- The literal accommodation ID `VNS-HOTEL-001` for the Sahi River View Guesthouse row.
- `NOT_IN_PERMANENT_REGISTRY` for every row whose cluster or entity type (Delhi, Agra, Kolkata, Tiruvannamalai; food/restaurant items; experience-blocks such as walks/boat rides; a few Kumaon/Bodh Gaya items) has no canon permanent-ID entry at all — this is an honest "no stable ID exists yet," not a claim that one was assigned and lost.

A later solver or successor doing entity reconciliation should join on `STABLE_SOURCE_ID` wherever it is a real `PERMANENT-`/`LEGACY-` value, and treat the packet's own `ID` column as a display-only convenience label, never as a claim of canonical numbering.

## 11. COMPANION FILES

- `PHYSICAL_A_PLUS_A_COVERAGE_LEDGER.csv` — the full inventory (see also `LEDGER_SUMMARY.md`).
- `CLOSED_FACTS_OPEN_VARIABLES.md` — the four-category evidence separation.
- `OBJECTIVE_AND_HUMANE_GATES.md` — objective hierarchy + humane-fit metrics for the later solve.
- `INPUT_COMPLETENESS_GATE.md` — CCI's own self-check pass over this packet.

`ROUTE_SOLVE_STARTED = NO`. This packet contains no route, calendar, day-plan, or itinerary of any kind.

END INPUT CONTRACT
