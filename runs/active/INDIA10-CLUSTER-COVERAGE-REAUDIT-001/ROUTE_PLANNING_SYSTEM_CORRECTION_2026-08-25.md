# INDIA — ROUTE PLANNING SYSTEM CORRECTION — 2026-08-25

status: HARD_CORRECTION / METHOD_VALID / OLD_SUCCESSOR_FRONTIER_SUPERSEDED
branch: agent/india8-cluster-casting
updated: 2026-08-26

## INCIDENT
Earlier calendar/day sketches undercharged travel. Raw road/rail/flight durations were sometimes treated too loosely next to visit blocks, and one Kumaon sketch even created unnecessary backtracking.

Therefore all older exact-date/day sketches remain NON-AUTHORITATIVE unless rebuilt through the current transfer/accounting method.

## WHAT REMAINS VALID
- Mark's A+/A/A*/B/C decisions;
- accommodation locks;
- protected location/person canon;
- traveler/LP/Komoot research;
- corridor geography that survives current verification;
- YSS Dwarahat FULL DAY;
- Kumaon one-way internal direction.

## WHAT IS SUPERSEDED
The old successor frontier in earlier versions of this file said to compare optional clusters before fully closing the six fixed-core time footprints. That frontier is SUPERSEDED.

Current controlling method:
`TRIP_PLANNING_META_CONTROLLER_2026-08-26.md`.

Current order:
`SIX FIXED A+ WORLDS -> PER-CORE CONTENT CLOSURE -> EXECUTION GEOMETRY -> MARK PACE/DWELL -> DURATION_CLOSED x6 -> REAL INTER-CORE TRANSFERS -> FIXED_CORE_34_DAY_BUDGET -> OPTIONAL-CLUSTER SURVIVAL -> FINAL TOPOLOGY -> LIVE LOGISTICS -> EXACT CALENDAR`.

Do NOT jump from transfer research directly to Rishikesh/Braj/Prayagraj selection.

## DOOR-TO-DOOR RULE — STILL HARD
Every used transfer must account for applicable:
- packing/check-out/loading;
- station/airport/road access;
- check-in/security/platform waiting;
- scheduled transport;
- winter/fog/traffic/delay buffer;
- baggage/exit;
- onward road;
- next sleeping-base check-in;
- food/toilet/rest;
- usable daylight and traveller energy.

Raw transport time is evidence, not occupied-day time by itself.

## CURRENT TOPOLOGY PRINCIPLES
- Fixed core worlds: Delhi, Kumaon, Agra/Taj Mahal, Bodh Gaya/Gaya, Varanasi/Sarnath, Tiruvannamalai/Arunachala.
- Kumaon internal direction: `HAIDAKHAN VISHWA MAHADHAM -> NAINITAL -> KAINCHI -> DWARAHAT -> DUNAGIRI/KUKUCHINA`.
- Do not use `Haidakhan -> Dwarahat/Dunagiri -> Nainital/Kainchi`.
- Eastern Kumaon exit is a FULL TRAVEL DAY class edge and must be counted once.
- Bodh Gaya/Gaya + Varanasi/Sarnath remain a natural eastern pair.
- Varanasi remains a strong southbound gateway hypothesis toward Chennai/Bengaluru -> Tiruvannamalai, subject to actual-date service recheck.
- If optional Rishikesh survives later, its natural position is before Kumaon.
- Braj is geographically near Delhi/Agra.
- Prayagraj is eastbound-corridor compatible but not route-required.

These topology facts prevent bad local assumptions; they do NOT authorize premature optional-cluster selection.

## KUMAON CURRENT ACCOUNTING EXAMPLE
For the fixed-core baseline:
- K0 `DELHI -> HAIDAKHAN VISHWA MAHADHAM` is included as a full occupied travel day in Kumaon's current footprint;
- internal base changes consume real day time;
- the eastern Dunagiri exit remains visible and will be charged exactly once to the next fixed-core bridge/global budget.

If an optional world is later inserted, calculate its marginal delta against that baseline rather than silently replacing/losing an edge.

## CURRENT FRONTIER
Finish Kumaon execution/pace closure, then run the same closure cycle for the other five fixed A+ worlds. Only after all six are `DURATION_CLOSED` may the fixed-core 34-day budget and optional-cluster survival round begin.

END_OF_CORRECTION