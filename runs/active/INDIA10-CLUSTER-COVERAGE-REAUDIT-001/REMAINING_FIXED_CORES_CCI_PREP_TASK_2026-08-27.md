# CCI PREP TASK — ALL REMAINING FIXED CORES — 2026-08-27

status: READY_FOR_CCI

## GOAL
Precompute the four remaining fixed A+ core worlds so future Mark review can start immediately without another long retrieval phase:
1. BODH GAYA / GAYA
2. TIRUVANNAMALAI / ARUNACHALA
3. DELHI
4. AGRA / TAJ MAHAL

Read first:
- governance/CURRENT_STATE.md
- governance/MARK_TRAVEL_PREFERENCES_CURRENT.md
- runs/active/INDIA10-CLUSTER-COVERAGE-REAUDIT-001/REMAINING_FIXED_CORES_PREP_CONTROLLER_2026-08-27.md
- runs/active/INDIA10-MULTIAI-TRAVELER-DISCOVERY-001/TRAVELER_EXPERIENCE_MASTER_UNION_LEDGER.md
- runs/active/INDIA10-REGIONAL-DISCOVERY-GAPS-001/TASK.md
- current A+ / grade decision files
- protected canon baseline
- all historical Mark decision files materially touching these four cores
- relevant regional worker freeze files on their worker branches
- PR #23 only where needed to recover protected Mark decisions or resolve contradictions.

## WORK
For EACH of the four cores:
1. reconstruct newest lossless current A+/A/A*/B/C canon; never infer a grade;
2. list superseded/historical conflicting grades separately, with newest Mark decision winning;
3. list every relevant OLD_LP_* traveler item, including corridor items; do not filter because it seems small;
4. list every other traveler/regional finding that could plausibly affect Mark's time or experience;
5. mark exact official UNESCO status for every active A+/A/A*/B item: `UNESCO WH`, `UNESCO TENTATIVE`, or none; do not over-extend component-property labels;
6. identify B+exact-WH candidates requiring Mark re-review;
7. mark date-impossible items for Dec 2026–Jan 2027 so they remain provenance but are NOT put in Mark's actionable ballot;
8. recover sleep-base/anchor-zone decisions and any old Mark pace/dwell wishes;
9. group retained/open content into real geographic modules with approximate road/walk burden from the actual/allowed sleep origin;
10. identify only the genuine `DAY_CHANGING_OPEN_SURVIVORS` that still require Mark judgment;
11. give a short Dutch recognition hook and suggested dwell RANGE for each open survivor, but DO NOT assign a grade;
12. explicitly flag any item where a 'small' visit could reasonably become half/full day for Mark.

## HARD RULES
- NO new A/B/C/A+.
- A* semantics newest Mark: host-dependent bycatch only, NOT intrinsic A, SKIP_FIRST.
- Do not re-present current C in actionable ballots.
- Do not conflate UNESCO Tentative with World Heritage.
- `kosten` means money only.
- no exact calendar.
- no hotel invention.
- no PDF.
- Mark is not courier; write results directly to GitHub.

## OUTPUT
Write ONE file on the active central branch:
`runs/active/INDIA10-CLUSTER-COVERAGE-REAUDIT-001/REMAINING_FIXED_CORES_CCI_PREP_AUDIT.md`

Structure:
- EXECUTIVE SUMMARY
- BODH GAYA/GAYA
- TIRUVANNAMALAI/ARUNACHALA
- DELHI
- AGRA/TAJ MAHAL
- CROSS-CORE UNESCO RE-REVIEW TRIGGERS
- DAY_CHANGING_OPEN_SURVIVORS BY CORE
- CONTRADICTIONS / BLOCKERS

If central-branch write is technically unsafe because HEAD moved, do not overwrite newer state. Write the output on your current branch and report exact branch/path/commit in PR #23.

END