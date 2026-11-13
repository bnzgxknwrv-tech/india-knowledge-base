# INDIA11 — EAST CORRIDOR TRANSFER TOPOLOGY

status: BLOCK_2_COMPLETE_PROVISIONAL
updated: 2026-08-26
branch: agent/india8-cluster-casting
web_recheck: 2026-08-26

## PURPOSE
Bounded Block 2 only. Close the practical eastbound topology between the Agra/Delhi gateway and the fixed Bodh Gaya/Gaya + Varanasi/Sarnath worlds using realistic occupied-time classes.

No south jump, no exact calendar dates, no new A/B/C decisions and no HOTEL reopening are authorized here.

## PROTECTED WORLDS — NOT RE-GRADED
- `AGRA / AGRA / Taj Mahal — huidige status: A+`.
- `BODH GAYA / BODH GAYA / Mahabodhi Temple Complex (Boeddha-verlichtingscomplex) — huidige status: A+`.
- `BODH GAYA / BAKRAUR / Sujata Stupa (plek waar Sujata volgens de traditie Siddhartha voedsel gaf vóór de verlichting) — huidige status: A+`.
- `BODH GAYA / DUNGESHWARI HILLS / Dungeshwari–Mahakala Caves (grotten van Siddhartha's extreme ascese vóór Sujata en de verlichting) — huidige status: A+`.
- `VARANASI / SARNATH / Sarnath sacred complex (Boeddhistische heilige en archeologische wereld van de eerste leerrede) — huidige status: A+`.
- `VARANASI / ASSI GHAT / HOTEL Sahi River View Guesthouse (door Mark gekozen verblijf aan/naast Assi Ghat) — accommodatie-status: LOCKED_BY_MARK`.

## CURRENT TRANSPORT EVIDENCE
### E1 — AGRA -> GAYA DIRECT OVERNIGHT RAIL
Current timetable evidence for train 12988 Ajmer–Sealdah SF Express:
- Agra Fort departure about 18:45;
- Gaya arrival about 07:50;
- scheduled rail time about 13h05;
- currently shown daily.

Operational interpretation:
- this is a one-seat direct eastbound movement without a Delhi return;
- hotel/check-out, station access and boarding buffer must be charged before 18:45;
- after arrival, Gaya Junction -> Bodh Gaya is only about 13–14 km / roughly 15 min raw by road, but use about 30–60 min operationally for pickup/traffic/arrival uncertainty before HOTEL/food/rest;
- realistic hotel-exit -> settled-in-Bodh-Gaya elapsed class is roughly 15.5–18h, mostly overnight.

Planning class:
`OVERNIGHT_TRANSFER / LOW_DAYLIGHT_LOSS / SLEEP_QUALITY_PENALTY`.

This is not automatically superior for Mark: the gain is daylight efficiency; the cost is sleeping on a train and possible next-morning recovery need.

Sources rechecked 2026-08-26:
- https://www.confirmtkt.com/train-schedule/12988
- https://www.ixigo.com/trains/12988
- https://www.rome2rio.com/s/Gaya-Junction-Station/Bodh-Gaya

### E2 — AGRA -> VARANASI/BANARAS DIRECT DAY RAIL
Current timetable evidence for train 20176 Agra Cantt–Banaras Vande Bharat:
- Agra Cantt departure about 06:00;
- Banaras arrival about 13:00;
- scheduled rail time about 7h;
- current operating pattern shown six days/week, not Wednesday.

Door-to-door interpretation to the locked Varanasi base:
- very early HOTEL departure and station buffer are required;
- after Banaras/Varanasi arrival, local ground transfer to Assi Ghat, HOTEL check-in, food and decompression still consume time;
- conservative planning class from HOTEL exit in Agra to settled at `VARANASI / ASSI GHAT / HOTEL Sahi River View Guesthouse (...) — accommodatie-status: LOCKED_BY_MARK` is roughly 9.5–11h depending station access and city traffic.

Planning class:
`SUBSTANTIAL/FULL TRAVEL DAY / BED_SLEEP_PRESERVED / HIGH_DAYLIGHT_LOSS`.

This is a clean and comfortable operational alternative, but it consumes most of a waking day.

Sources rechecked 2026-08-26:
- https://www.ixigo.com/trains/20176
- https://www.confirmtkt.com/train-schedule/20176
- https://indiarailinfo.com/train/-train-agra-cantt-banaras-vande-bharat-express-20176/236388/450/12892

### E3 — AGRA -> DELHI -> EAST BY AIR
Current Delhi -> Varanasi nonstops and Delhi -> Gaya services make Delhi a real fallback gateway. Air India has also published Delhi–Gaya winter-season services effective 25 October 2026.

But from Agra this requires:
1. Agra -> Delhi ground/rail movement;
2. airport access + preflight buffer;
3. flight;
4. baggage/exit;
5. destination ground transfer.

Topology class from Agra:
`VALID_FALLBACK / MULTI_MODE / BACKTRACKING / FULL_TRAVEL_DAY`.

It does not beat the direct Agra eastbound rail options on structural simplicity and should not be the default merely because the flight itself is short.

Sources rechecked 2026-08-26:
- https://www.airindia.com/in/en/newsroom/press-release/air-india-to-operate-additional-flights-to-gaya.html
- https://www.airindia.com/en-in/book-flights/delhi-to-varanasi-flights

## NATURAL EASTERN PAIR — BODH GAYA/GAYA <-> VARANASI/SARNATH
The two fixed eastern worlds remain a natural pair.

### Road option
Current public routing for Bodh Gaya -> Varanasi is about 242 km / roughly 3h40 raw road time.

For topology, do NOT use 3h40 as the calendar block. A private-driver HOTEL-to-HOTEL movement should be budgeted provisionally around `~5–6.5h occupied`, allowing pickup/loading, a stop, road/urban uncertainty and arrival transition. Final winter/date-specific routing remains later work.

### Rail option
Gaya -> Varanasi currently has multiple direct trains, with several daily services and scheduled rail times broadly in the ~4–5.5h class; faster non-daily services also exist.

Door-to-door rail must add:
- Bodh Gaya -> Gaya Junction ground leg;
- station buffer;
- train;
- Varanasi/Banaras station -> Assi Ghat ground leg;
- arrival/food/HOTEL transition.

Working rail class for a sensibly timed direct train:
`~5.5–8h door-to-door`, depending actual service.

Conclusion: private car is operationally competitive despite the apparently fast train, because it removes two local-transfer/station interfaces. Actual mode should be selected only when exact dates and departure preferences are known.

Sources rechecked 2026-08-26:
- https://www.rome2rio.com/s/Bodh-Gaya/Varanasi
- https://www.ixigo.com/by-train-rail/gaya-to-varanasi-by-train
- https://www.confirmtkt.com/trains/gaya-to-varanasi-train-tickets

## ORDER COMPARISON
### E-A — AGRA -> BODH GAYA/GAYA -> VARANASI/SARNATH
Strengths:
- direct daily Agra Fort -> Gaya overnight train creates a one-seat eastbound transfer;
- little waking-day loss if Mark tolerates sleeper travel;
- no Delhi backtrack;
- subsequent Bodh Gaya/Gaya -> Varanasi/Sarnath leg is a moderate paired-world transfer by car or rail.

Weakness:
- overnight rail may reduce sleep quality and therefore next-morning usable energy.

Status:
`BLOCK_2_PROVISIONAL_PREFERENCE`.

### E-B — AGRA -> VARANASI/SARNATH -> BODH GAYA/GAYA
Strengths:
- direct Vande Bharat gives a clean same-day rail move from Agra;
- preserves normal bed sleep before travel;
- Varanasi -> Gaya also has multiple direct rail options and road is possible.

Weaknesses:
- the Agra -> Banaras movement consumes most of a waking day;
- if later global topology wants to finish the eastern chain in Varanasi, this order would require reversing the pair.

Status:
`STRUCTURALLY_VALID_ALTERNATIVE / NOT_DEFAULT`.

## BLOCK 2 CONCLUSION
`AGRA -> BODH GAYA/GAYA -> VARANASI/SARNATH` is the strongest provisional east-corridor topology.

Reasoning independent of the south jump:
1. no Delhi backtrack is needed;
2. current daily direct Agra Fort -> Gaya overnight rail can preserve a waking day;
3. the fixed Bodh Gaya/Gaya and Varanasi/Sarnath worlds remain close enough to connect in one substantial but not full cross-country movement block;
4. the reverse order remains viable if actual dates, train quality or Mark's sleep preference later make the Vande Bharat/day-travel option better.

This file does NOT lock a train, departure time, overnight-train preference or exact date. Those remain later operational choices after global topology is closed.

## OCCUPIED-TIME CLASSES FOR GLOBAL STITCH
- `AGRA -> GAYA direct overnight rail`: overnight movement; approximately 15.5–18h elapsed HOTEL-exit to settled arrival, but low waking-day loss; recovery risk must be charged.
- `AGRA -> VARANASI direct Vande Bharat`: approximately 9.5–11h door-to-door; substantial/full waking travel day.
- `AGRA -> DELHI -> EAST by air`: full travel day and backtracking; fallback only.
- `BODH GAYA/GAYA -> VARANASI/SARNATH private car`: provisional ~5–6.5h occupied.
- `BODH GAYA/GAYA -> VARANASI/SARNATH rail`: provisional ~5.5–8h door-to-door for a useful direct service.

## CALENDAR / FRESHNESS GATE
No exact Dec 2026 / Jan 2027 train choice is locked here. Recheck the actual operating date, timetable, availability, station and class before booking/calendar lock.

## FRONTIER
BLOCK 2 EAST = `COMPLETE_PROVISIONAL`.

The next bounded autonomous scope is BLOCK 3 SOUTH only, per `TASK_SPLIT_2026-08-26.md`. No exact calendar and no global stitch until Block 3 exists.