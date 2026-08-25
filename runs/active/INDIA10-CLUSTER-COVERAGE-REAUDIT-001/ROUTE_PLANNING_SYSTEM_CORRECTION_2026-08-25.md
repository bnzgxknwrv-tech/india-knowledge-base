# INDIA10 — ROUTE PLANNING SYSTEM CORRECTION — 2026-08-25

status: HARD_CORRECTION / SUCCESSOR_SAFE
branch: agent/india8-cluster-casting
updated: 2026-08-25

## INCIDENT
During the emerging calendar/day-planning layer, travel times had been researched in corridor files, but were NOT consistently charged as occupied time inside the day/calendar sketches. Raw road/rail/flight durations were sometimes treated too loosely alongside visit blocks. This made some conversational date/day sketches look more feasible than they were.

A concrete symptom was a loose Kumaon sequence that placed Dwarahat/Dunagiri before Nainital/Kainchi, creating unnecessary backtracking despite an older corridor file already containing the better geometry.

This is a REGIE/SYSTEM error in the calendar layer, not a failure of the underlying location research.

## WHAT IS INVALIDATED
All earlier conversational exact-date/day sketches are NON-AUTHORITATIVE unless rebuilt through the new transfer gate.

In particular, do not reuse any compact date sequence merely because it appeared plausible in chat. A date wish such as 31 Dec 2026 in Rishikesh is not a route lock until the complete route mathematics supports it.

## WHAT REMAINS VALID
The correction does NOT discard:
- Mark's A+/A/A*/B/C decisions;
- LOCKED_BY_MARK accommodation choices;
- protected person/location canon;
- regional/traveler/Lonely Planet research;
- Komoot discovery and walk findings;
- safety/legal research;
- corridor geography that remains consistent after recheck;
- direct Mark decisions such as a FULL DAY at the YSS Dwarahat A location.

Only the timing/calendar interpretation is invalidated where transfers were not fully consumed.

## NEW HARD PLANNING PIPELINE
No successor may jump directly from selected places to dates.

Mandatory order:
`SELECTED SITES / CLUSTERS`
`-> REAL DOOR-TO-DOOR TRANSFER LEDGER`
`-> GLOBAL CLUSTER TOPOLOGY / ROUTE DIRECTION`
`-> MARK DWELL-TIME CHOICES PER RETAINED CLUSTER`
`-> NIGHT / BASE-CHANGE SCENARIOS`
`-> EXACT CALENDAR DATES`
`-> SPECIAL-EVENT OPTIMIZATION ONLY WHERE IT STILL FITS`.

## DOOR-TO-DOOR MEANS DOOR-TO-DOOR
Every used transfer must charge, as applicable:
- packing/check-out/loading/pickup;
- road to station/airport;
- terminal/platform/check-in/security waiting;
- scheduled flight/train;
- delay/fog/winter buffer;
- baggage/exit;
- onward road transfer;
- next HOTEL check-in;
- food/toilet/rest;
- realistic lost daylight and traveller energy.

A 1-hour flight is never automatically a 1-hour travel block. A 3-hour mountain drive is never automatically a 3-hour calendar block.

## ROUTE-DIRECTION RULE
Internal corridor direction may not be frozen in isolation from global entry/exit geometry. Test the whole route first. However, as of the current 2026-08-25 topology audit the strongest north sequence is:
`DELHI -> optional HARIDWAR/RISHIKESH -> KUMAON / HAIDAKHAN -> NAINITAL -> KAINCHI -> DWARAHAT -> DUNAGIRI/KUKUCHINA -> plains/eastbound corridor`.

The previously seen conversational sequence `HAIDAKHAN -> DUNAGIRI/DWARAHAT -> NAINITAL/KAINCHI` is prohibited because it backtracks.

The Dwarahat/Dunagiri eastern Kumaon finish itself creates a FULL TRAVEL DAY class exit toward the plains. That burden exists even if Rishikesh is removed.

## CURRENT TOPOLOGY RESULT — NO DATES
Fixed core worlds remain structurally feasible:
- Kumaon;
- Delhi;
- Agra/Taj Mahal;
- Bodh Gaya/Gaya;
- Varanasi/Sarnath;
- Tiruvannamalai/Arunachala.

Current optional topology classes:
- Haridwar/Kankhal/Rishikesh: OPTIONAL / REALISTIC / MODERATE EXTRA BURDEN. Natural insertion is once between Delhi and Kumaon. It replaces one northern transfer with two substantial transfers and adds a base change + its own stay time; it is not inherently a route-breaking cross-country zigzag.
- Braj/Mathura/Vrindavan/Govardhan: OPTIONAL / LOW GEOMETRIC BURDEN near Agra; mostly costs visit/dwell time.
- Prayagraj: OPTIONAL / LOW-TO-MODERATE GEOMETRIC BURDEN on eastbound rail axis; mostly corridor-compatible.
- Mysore/Bengaluru sightseeing: not assumed. Bengaluru may be used purely as an air gateway for the southbound jump.

Current eastern/southbound hypothesis:
`... -> BODH GAYA/GAYA -> VARANASI/SARNATH -> Varanasi flight gateway -> Bengaluru/Chennai gateway as actually available -> road/rail to TIRUVANNAMALAI/ARUNACHALA`.
Exact Dec 2026/Jan 2027 service must be rechecked before calendar lock.

## RISHIKESH DECISION FRAME
Do NOT ask “does Rishikesh fit on 31 Dec?” yet.
Ask first:
1. Is the Haridwar/Kankhal/Rishikesh spiritual cluster worth its own dwell time to Mark?
2. Is roughly an extra half/full movement block + one base change acceptable relative to fixed-core travel load?
3. Does placing it once between Delhi and Kumaon preserve a clean one-way topology?
4. Only after these are answered may 31 Dec be tested as a special-event/date preference.

Current zoom-out answer: Rishikesh remains feasible and should NOT be cut solely because travel time is now counted correctly.

## YSS FULL-DAY CORRECTION
Canonical file:
`DWARAHAT_YSS_FULL_DAY_PLAN_2026-08-25.md`.
The older half-day file is superseded.

`KUMAON / DWARAHAT / Yogoda Satsanga Sakha Ashram — Dwarahat (YSS-ashram van Paramahansa Yogananda’s organisatie; meditatiecentrum in de Mahavatar Babaji/Kriya-regio) — huidige status: A` requires a FULL DAY.
Mark is Ananda, not YSS/SRF; YSS overnight accommodation must NOT be planned. Primary Babaji base remains `KUMAON / DUNAGIRI / HOTEL Dunagiri Retreat (...) — accommodatie-status: LOCKED_BY_MARK`.

## CURRENT CONTROLLING FILES
Read in this order for route work:
1. `governance/CURRENT_STATE.md`
2. this file
3. `GLOBAL_TRANSFER_LEDGER_2026-08-25.md`
4. `CLUSTER_TOPOLOGY_FEASIBILITY_2026-08-25.md`
5. protected canon / relevant cluster decisions
6. only then cluster-specific corridor/walk files.

## SUCCESSOR FRONTIER
If INDIA10 disappears now, INDIA11 must NOT reconstruct a calendar from old chat or old date sketches.

Active task is:
- keep exact dates open;
- compare retained/optional clusters against REAL travel burden;
- determine which optional worlds deserve dwell time;
- then close the exact route edges actually used;
- only after that build nights and exact dates.

No further calendar precision is authorized until that sequence is followed.
