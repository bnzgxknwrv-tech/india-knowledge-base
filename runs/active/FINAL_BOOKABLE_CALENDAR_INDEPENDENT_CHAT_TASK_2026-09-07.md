# WORK TASK — INDEPENDENT FINAL BOOKABLE CALENDAR CHECK

Date: 2026-09-07
Role: INDIA-FINAL-BOOKABLE-CALENDAR-INDEPENDENT-CHECK
Branch only: `worker/final-bookable-calendar-independent-check`

## Goal
Independently calculate and stress-test the final dated India calendar so Mark can safely book hotels, ashrams, trains and domestic flights. This is a second opinion, not a rewrite of Mark's choices.

## Read first
1. Central branch `agent/india8-cluster-casting` current truth.
2. `runs/active/FINAL_TRIP_TOPOLOGY_CALENDAR_OPTIMIZATION_2026-09-07.md` and `runs/active/FINAL_TRIP_DATED_CALENDAR_2026-09-07.md` from `worker/final-route-calendar-optimizer`.
3. `decisions/FINAL_DELHI_ONE_NIGHT_MARK_DECISION_2026-09-07.md` from central.
4. `runs/active/FINAL_EXECUTION_READINESS_NO_SURPRISES_AUDIT_2026-09-07.md` from `worker/final-execution-readiness-audit`, commit `cb4f0d917d5fbdfe930464e7be1bba332e000f51`.
5. PR #23 CCI_RESULT comment `5571634572`.
6. PR #23 WORK_TASK comment `5571701657` as the required final-product specification.

## Hard fixed
- Arrival India 19 Dec 2026; AI155 DEL→AMS 21 Jan 2027 12:20; 33 India slots.
- Macrospine is baseline and must not be globally re-optimized: Delhi/Kumaon → Agra → Bodh Gaya → Varanasi/Sarnath → Kolkata/Dakshineswar → Tiruvannamalai → Chennai/Delhi.
- FINAL OUT: Puri, Serampore trip-world, Vrindavan/Braj.
- Final Delhi exactly 1 night LOCKED_BY_MARK.
- Do not change Mark grades or locked durations.

## Independently solve/check
1. Kumaon internal order only: Nainital→Dunagiri→Haidakhan versus Nainital→Haidakhan→Dunagiri.
2. Kolkata duration variants 2/3/4 nights with exact downstream date consequences.
3. Bodh Gaya 2 versus 3 nights as sensitivity.
4. Verify arithmetic for all 33 slots with no duplicated/missing night.
5. Verify each proposed domestic-flight day and rail day is logically bookable on the stated date; distinguish current timetable evidence from future live-recheck facts.
6. Verify major closure/festival/fog/crowd interactions that can change a date choice.
7. Verify the single final-Delhi-night rule and the Chennai-positioning buffer are both respected.
8. Identify any date that should NOT yet be booked because it depends on an unresolved Mark decision.
9. State exactly which hotel/ashram/flight/train dates are safe to book once Mark selects Kolkata duration.

## Required output
Create:
`runs/active/FINAL_BOOKABLE_CALENDAR_INDEPENDENT_CHECK_2026-09-07.md`

It must contain:
- VERDICT: PASS / PASS_WITH_CORRECTIONS / FAIL;
- exact recommended 33-slot calendar;
- Kumaon winner and why;
- 2/3/4 Kolkata comparison;
- Bodh 2/3 sensitivity;
- any arithmetic/date errors found in the existing worker calendar;
- transport/closure/festival contradictions;
- BOOK NOW AFTER DATE LOCK vs WAIT vs LIVE_RECHECK_LATER;
- max 10 highest-value corrections/additions;
- no invented grades or reopened excluded worlds.

Commit the result on this branch and report COMPLETE/BLOCKED + commit SHA + concise top findings.