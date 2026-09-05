# INDIA17 PARALLEL RESEARCH — RAIL NETWORK / GATEWAYS

ROLE: independent Deep Research worker. Work ONLY on branch `agent/india17-dr-rail-network`.

## READ FIRST
- `governance/CURRENT_STATE.md`
- `runs/active/INDIA10-CLUSTER-COVERAGE-REAUDIT-001/DELHI_ARRIVAL_RAIL_FIRST_SUPERSEDE_2026-09-05.md`
- `runs/active/INDIA10-CLUSTER-COVERAGE-REAUDIT-001/KUMAON_NAINITAL_FIRST_TOPOLOGY_RECHECK_2026-09-05.md`
- `runs/active/INDIA10-CLUSTER-COVERAGE-REAUDIT-001/KUMAON_CALENDAR_FIRST_LEG_2026-12-19_TO_29.md`
- current hard trip dates/flight logistics file(s) routed from central.

## FIXED INPUT
- AI156 Amsterdam -> Delhi lands **Saturday 19 Dec 2026 at 10:15 local**.
- Mark wants HOTEL FIRST -> freshen -> Nirmal Dham [A+] -> TRAIN FIRST northbound.
- Long Delhi -> Haidakhan car is fallback only.
- Target overnight class: 1A first; 2A only explicit fallback.
- Nainital-first is now the leading human preference.
- Current 9-night working Kumaon allocation under Nainital-first is:
  - Nainital nights 20/21/22 Dec;
  - Dunagiri nights 23/24/25 Dec;
  - Haidakhan nights 26/27/28 Dec;
  - therefore **Tuesday 29 Dec 2026** is the natural Haidakhan -> rail-gateway outbound date.
- Current structural finding: direct 12354 Lal Kuan -> Varanasi currently runs Saturday only, so it does NOT fit Tue 29 Dec without changing night allocation. Do not move nights merely to force that train unless whole-trip benefit proves it worthwhile.

## RESEARCH QUESTIONS
A. Find ALL serious rail products from the southwest/Delhi area on **Saturday evening 19 Dec 2026** toward Kumaon gateways (Kathgodam, Haldwani, Lal Kuan and only genuinely useful nearby railheads), not just 15013.
- departure station and time;
- arrival station and time;
- whether it terminates/continues;
- 1A/2A availability class;
- daily/weekly running pattern;
- whole-human fit after Nirmal Dham;
- whether any train yields a materially later/more humane morning arrival than ~05:05 without a bad detour.

B. Prove whether any train physically continues to Nainital. State rail terminus reality and exact last-road class to Hotel Evelyn.

C. Optimize **Tuesday 29 Dec 2026 Haidakhan -> Varanasi/Sarnath** train-first exit. Start from realistic gateways after a Haidakhan-last finish: Kathgodam, Haldwani, Lal Kuan.
- direct trains valid on Tuesday;
- one-change patterns with robust transfer margins;
- avoid fragile connections like a ~25-minute winter/fog change unless there is a protected through-booking mechanism;
- prefer night train / sleeper over long daytime car;
- target 1A first, 2A fallback;
- show exact current departure/arrival times and weekdays;
- explicitly test 13020 Bagh Express and all materially better alternatives;
- investigate whether any current/scheduled seasonal or special direct Lal Kuan/Kathgodam -> Varanasi train is actually expected to operate into late Dec 2026; do not rely on discontinued/summer-special data;
- compare whether a harmless extra rail night or a short intermediate rail stop beats a full wasted day in Lucknow.

D. Also test whether shifting the 9-night Kumaon sequence by exactly 1–2 nights creates a materially better rail exit (especially Saturday 12354 direct) WITHOUT degrading Nainital decompression, Dunagiri 3-night content, or Haidakhan 3-night / 2-full-day lock. This is scenario analysis only; do not alter central truth.

E. Identify whether reversing Kumaon to finish Haidakhan saves enough exit burden to offset internal road backtracking.

## EVIDENCE
Prefer Indian Railways/NTES/IRCTC-equivalent official information where accessible; cross-check current timetable aggregators. Exact Dec 2026 operation/inventory can be `LIVE_RECHECK_LATER`; distinguish current structural timetable from actual-date certainty.

## OUTPUT
Write:
`runs/active/INDIA17-PARALLEL-ROUTE-RESEARCH-001/RAIL_NETWORK_RESULT.md`

Include three ranked tables:
1. `SAT 19 DEC — DELHI/NIRMAL-DHAM -> KUMAON`;
2. `TUE 29 DEC — HAIDAKHAN/RAIL-GATEWAY -> VARANASI/SARNATH`;
3. `NIGHT-SHIFT SENSITIVITY` (0, +1/-1, +2/-2 nights only where genuinely useful).

End with:
- `BEST_INBOUND_RAIL_SPINE:`
- `BEST_OUTBOUND_RAIL_SPINE_FOR_29_DEC:`
- `WOULD_MOVING_NIGHTS_MATERIALLY_IMPROVE_IT:`
- `DATE_DEPENDENCIES:`
- `BOOKING_WINDOW_RECHECKS:`
- source list + confidence.

Commit only on this branch. Do not change any Mark grade/lock or central route decision.