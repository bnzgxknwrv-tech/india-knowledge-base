# INDIA10 — TRAVEL TIME INTEGRITY AUDIT — 2026-08-25

status: CALENDAR_LAYER_INVALID_UNTIL_REBUILT
branch: agent/india8-cluster-casting
updated: 2026-08-25

## MARK TRIGGER
Mark correctly flagged that a multi-cluster India itinerary cannot work if travel time is researched in corridor notes but not charged as hard occupied time in the daily calendar. Some inter-cluster movements will require flights/trains plus airport/station transfers and therefore cannot be represented by scheduled flight/train duration alone.

## AUDIT CONCLUSION
1. Travel times were NOT absent from the project. Existing corridor/route-builder files contain many road-distance and travel-time estimates, including the Kumaon A+ corridor and walk-instead-of-drive work.
2. HOWEVER, there is no sufficiently complete central calendar ledger found that consistently converts EVERY move into a hard door-to-door occupied-time block before assigning visit days/nights.
3. Therefore any earlier assistant-generated exact date sequence that was not backed by such a ledger is NOT authoritative and MUST NOT be used as a final itinerary.
4. This audit invalidates the calendar layer only. It does NOT invalidate Mark's A+/A/A*/B/C decisions, LOCKED_BY_MARK accommodations, person/site research, Komoot findings or corridor geometry.

## CONCRETE ERROR FOUND — KUMAON
The active Kumaon corridor matrix gives the efficient baseline order:
`HAIDAKHAN -> NAINITAL/HOTEL EVELYN -> KAINCHI -> KHAIRNA -> RANIKHET -> DWARAHAT -> KUKUCHINA/DUNAGIRI`.

A later conversational calendar sketch incorrectly placed Dwarahat/Dunagiri before Nainital/Kainchi, creating unnecessary backtracking. That sketch is explicitly INVALID as route planning.

Working corridor evidence already recorded:
- Haidakhan -> Nainital: roughly 50–65 km / ~1h20–2h30 working class, exact access dependent.
- Nainital -> Kainchi: ~17 km / ~40–60 min.
- Kainchi -> Dwarahat: ~71.7 km / ~2h24 working class; Dwarahat -> Kukuchina/Dunagiri roughly another ~20 km in existing Babaji-route evidence; winter/fog/traffic buffer required.
- Alternative via Almora/Kasar Devi is materially slower and is not justified by current Mark grades.

## HARD RULE — EVERY MOVE IS A TRANSFER_BLOCK
Before any calendar date is assigned, EVERY edge between sleeping bases, clusters and major sites must have one explicit `TRANSFER_BLOCK` containing:
1. full origin name + explanation + status; HOTEL prefix when origin is a sleeping base;
2. full destination name + explanation + status; HOTEL prefix when destination is a sleeping base;
3. transport mode(s);
4. hotel checkout / pickup / loading time where relevant;
5. road time to airport/station when applicable;
6. airport/station check-in, security and waiting allowance;
7. scheduled flight/train duration;
8. arrival, baggage and exit allowance;
9. road/boat/walk transfer from terminal to destination;
10. meal, toilet and rest buffer appropriate to trip length;
11. traffic / mountain-road / winter / fog / delay contingency;
12. total realistic door-to-door occupied-time RANGE;
13. earliest realistic arrival time for an assumed departure;
14. usable daylight remaining at destination;
15. whether a meaningful A+/A visit genuinely fits the same day;
16. what happens to luggage/driver during any walk/site visit.

## FLIGHT / TRAIN RULE — HARD
Never use scheduled flight/train duration as 'reistijd'.

For a flight day, planning time is:
`HOTEL checkout/pickup -> airport road transfer -> check-in/security/wait -> flight -> landing/baggage/exit -> destination ground transfer -> HOTEL/check-in or first site`.

A 1–2 hour flight can therefore occupy most of a practical day. Exact door-to-door time must be measured for the actual airports/flight windows before a same-day A+/A visit is promised.

Train days use the same principle including station access, platform buffer, scheduled journey, delay risk and destination transfer.

## ROAD RULE — HARD
- Mountain-road map time is not the calendar time by itself.
- Use a realistic route-specific range plus winter/fog/traffic/roadwork buffer.
- Long mountain transfers are `HEAVY_TRANSFER` unless evidence proves otherwise.
- No A+ visit is squeezed into a leftover sliver merely to preserve an attractive calendar.

## TRANSFER CLASSES
- `LOCAL_MOVE` — short move inside one base/urban cluster.
- `INTRA_CLUSTER_TRANSFER` — meaningful move inside one wider cluster.
- `BASE_CHANGE` — checkout + travel + new sleeping base.
- `HEAVY_TRANSFER` — movement itself consumes a large part of useful daylight/energy.
- `FLIGHT_DAY` — full door-to-door aviation chain.
- `TRAIN_DAY` — full door-to-door rail chain.

## VISIT PROTECTION
- A+ = protected core experience; route/calendar must make real time for it.
- intrinsic A = planned/retained unless burden is demonstrably disproportionate.
- A* = formal A corridor/bycatch, operational SKIP_FIRST; may fill genuine spare corridor time but may not threaten transfer reliability or an A+/A experience.
- B = reserve only.
- C = do not plan unless explicitly reopened.

## BUILD ORDER — MANDATORY
The final trip must now be built in this order:
1. Freeze current selected destination/site set and locked accommodations.
2. Build GLOBAL TRANSFER LEDGER for every plausible inter-cluster edge, including flights/trains.
3. Build LOCAL/CORRIDOR TRANSFER LEDGERS inside each retained cluster.
4. Choose route order from total door-to-door burden, not geography alone.
5. Allocate sleeping bases/nights.
6. Only then assign calendar dates.
7. Fit special event dates (long meditations, retreats, festivals, etc.) only where they do not break the transfer logic.
8. Build hour-level day plans with meals/rest/daylight.
9. Stress-test delays/weather/fatigue and apply A* SKIP_FIRST logic.

## CURRENT KUMAON IMPLICATION
Do NOT yet assign exact Dec 2026 dates from earlier conversational sketches.

Efficient baseline to test is:
`KUMAON / HAIDAKHAN -> KUMAON / NAINITAL -> KUMAON / KAINCHI -> KUMAON / DWARAHAT -> KUMAON / DUNAGIRI/KUKUCHINA`.

Current user decisions to preserve inside that geometry:
- KUMAON / HAIDAKHAN / Haidakhan Ashram (Haidakhan Babaji-pelgrimsashram; desired overnight spiritual base) — current status A+.
- KUMAON / NAINITAL / Hotel Evelyn (historic hotel where Ram Dass stayed; exact room unproven) — current status A+.
- KUMAON / NAINITAL / Naini Lake loop (ca. 3.2 km / 55–75 min; selected early-morning lake loop) — current status A+ and proven zero-road-detour morning-before-transfer candidate.
- KUMAON / KAINCHI / Kainchi Dham (Neem Karoli Baba ashram complex; core Neem Karoli Baba/Ram Dass location) — current status A+.
- KUMAON / DWARAHAT / Yogoda Satsanga Sakha Ashram — Dwarahat (YSS ashram of Paramahansa Yogananda’s organisation; meditation centre in the Babaji/Kriya region) — current status A; Mark wants a FULL DAY, not a half-day. No YSS overnight stay should be assumed because Mark is not YSS/SRF and has said the ashram does not accept him as an overnight guest.
- KUMAON / DUNAGIRI / HOTEL Dunagiri Retreat (spiritual retreat/hotel near the Babaji cave; chosen walking base) — accommodation status LOCKED_BY_MARK.
- KUMAON / KUKUCHINA-DUNAGIRI / Mahavatar Babaji's Cave (visit-able YSS/Kriya pilgrimage cave; main reason for the trip) — current status A+; preferred approach is direct walk from HOTEL Dunagiri Retreat once exact track/safety is closed.

The full-day YSS visit plus road commute from HOTEL Dunagiri Retreat may justify extra nights there, but number of nights is NOT locked until the transfer ledger is built.

## DATE-WISH RULE
Any conversational target such as '31 December in Rishikesh' is a `DATE_WISH` until the global transfer ledger proves it fits. Do not call it LOCKED unless Mark explicitly locks it after seeing the travel-time consequence.

## REQUIRED NEXT OUTPUT
Build `GLOBAL_TRANSFER_LEDGER_2026-08-25.md` starting with all fixed core worlds and known sleeping bases. Every unknown flight/train/road edge must be marked `TO_VERIFY`, never filled with optimistic guesses. Only after that ledger is sufficiently closed may calendar dates be proposed again.
