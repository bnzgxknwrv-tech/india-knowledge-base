# INDIA — GLOBAL TRANSFER LEDGER — CURRENT OVERRIDE 2026-08-26

status: ACTIVE_TRANSFER_LEDGER / STALE_EDGES_REMOVED
branch: agent/india8-cluster-casting
updated: 2026-08-26

## PURPOSE
This is the current safe transfer layer for fixed-core planning. Older versions remain in Git history as provenance but contained stale/unsafe assumptions, especially around the exact Haidakhan Vishwa Mahadham route.

No exact calendar may use raw transport time as the whole occupied block.

## HARD ACCOUNTING RULE
Every used edge eventually includes, as applicable:
- packing/check-out/loading;
- road/station/airport access;
- check-in/security/platform wait;
- scheduled transport;
- winter/fog/traffic/delay buffer;
- baggage/exit;
- onward road to sleeping base;
- check-in;
- food/rest/toilet;
- remaining daylight/energy.

For cluster costing:
- charge the known inbound occupied edge to that cluster;
- include all internal base-change movement;
- keep the outbound edge visible and charge it exactly once when the next bridge is built.

## A. KUMAON — CURRENT SAFE EDGES

### K0. DELHI -> HAIDAKHAN VISHWA MAHADHAM
Destination:
`KUMAON / HAIDAKHAN / Haidakhan Vishwa Mahadham (hoofdashram van Haidakhan Babaji bij Village Haidakhan aan de Gautami Ganga; ashramovernachting) — A+ world / sleep base`.

Current official/topology relation:
- about 337 km / 8–9 h raw road journey from Delhi according to Haidakhandi Samaj material;
- classify as FULL OCCUPIED TRAVEL DAY for the current fixed-core baseline.

Do not substitute an ambiguous Haidakhan pin or Anandpuri/Ranikhet site.

### K1. TRUE HAIDAKHAN VISHWA MAHADHAM -> NAINITAL
Status: `P0_TO_RECLOSE / OLD SHORTCUT INVALIDATED`.

HARD OVERRIDE:
- older working values around `50–65 km / 1h20–2h30` are NOT calendar-safe for the true Haidakhan Vishwa Mahadham and must not be used;
- exact winter door-to-door road geometry must be reclosed before the detailed K3 day bundle is finalized;
- Sattal A* may be attached to this transfer only if the corrected route/daylight proves it genuinely practical.

Destination sleep base in Nainital must be read from current accommodation/cluster state; do not invent a new lock from an old placeholder.

### K2. NAINITAL -> KAINCHI
Current working road class:
- ~17 km;
- ~40–60 min raw road time;
- Naini Lake A+ morning walk can combine naturally before movement without road detour.

Final occupied block still depends on actual Nainital pickup/base and Kainchi visit timing.

### K3. KAINCHI -> DWARAHAT
Efficient direct spine:
`Kainchi -> Khairna -> Ranikhet -> Dwarahat`.

Current working raw relation:
- ~71.7 km / ~2h24;
- winter buffer required.

Hard rule:
- YSS Dwarahat gets a FULL DAY and that transfer may not be hidden inside the full-day promise.

Kakrighat is A* / SKIP_FIRST and may be captured only if the transfer day remains comfortable.

### K4. DWARAHAT <-> HOTEL DUNAGIRI RETREAT
Status: `P0_TO_RECLOSE`.

Current repo contains inconsistent old working relations (~17 km versus ~25 km). Do NOT choose one by habit.
Required closure:
- exact current HOTEL Dunagiri Retreat <-> YSS Dwarahat route/time;
- winter morning/evening practicality;
- driver waiting/repositioning practicality.

Hard accommodation truth:
- HOTEL Dunagiri Retreat = LOCKED_BY_MARK;
- YSS overnight = NOT planned.

### K5. HOTEL DUNAGIRI RETREAT -> MAHAVATAR BABAJI'S CAVE
Status: `P0_TO_RECLOSE_OPERATIONALLY`.

Current planning principle:
- direct HOTEL-based walk is default;
- existing working class roughly 2–3 km one way / around 1 h climbing before cave pause, but exact track/time/ascent/legal/wildlife/winter safety must be closed before final operating schedule;
- keep unhurried cave time/daylight protected.

### K6. KUMAON INTERNAL ORDER — HARD
Use:
`HAIDAKHAN VISHWA MAHADHAM -> NAINITAL -> KAINCHI -> DWARAHAT -> DUNAGIRI/KUKUCHINA`.

Do NOT reverse Dwarahat/Dunagiri ahead of Nainital/Kainchi.

### K7. EASTERN KUMAON EXIT
Status: `FULL TRAVEL DAY CLASS / NEXT EDGE TO ASSIGN ONCE`.

Start from HOTEL Dunagiri Retreat / eastern Kumaon end, not Nainital.
Do not omit this burden and do not double-count it.

## B. INTER-CORE EDGES — CURRENT POLICY
Do not over-research all possible edges now. Close only edges that are actually required by the fixed-core sequence and later by surviving optional clusters.

Current topology principles:
- Bodh Gaya/Gaya -> Varanasi/Sarnath = natural eastern pairing;
- Varanasi is current preferred southbound gateway hypothesis toward Chennai/Bengaluru -> Tiruvannamalai, actual Dec 2026/Jan 2027 service to be rechecked later;
- Agra/Braj/Prayagraj details remain route-dependent until optional-cluster survival;
- Haridwar/Rishikesh is optional and must not silently replace Delhi as Kumaon's predecessor during fixed-core costing.

## C. OPTIONAL WORLDS — NO SILENT INSERTION
- HARIDWAR / KANKHAL / RISHIKESH — deferred optional world;
- BRAJ / MATHURA / VRINDAVAN / GOVARDHAN — deferred optional world;
- PRAYAGRAJ — deferred optional world.

They enter the ledger only after the six fixed cores are duration-closed and the fixed-core 34-day budget shows remaining capacity.

## CONTROLLING FILES
1. `governance/CURRENT_STATE.md`
2. `TRIP_PLANNING_META_CONTROLLER_2026-08-26.md`
3. this ledger
4. `CLUSTER_TOPOLOGY_FEASIBILITY_2026-08-25.md` for topology evidence, subject to later overrides
5. current cluster execution files

END_OF_LEDGER