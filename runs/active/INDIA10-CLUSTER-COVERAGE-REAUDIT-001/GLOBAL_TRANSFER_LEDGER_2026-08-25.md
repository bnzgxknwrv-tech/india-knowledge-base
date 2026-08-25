# INDIA10 — GLOBAL TRANSFER LEDGER — 2026-08-25

status: ACTIVE_TOPOLOGY_BUILD_NO_CALENDAR
branch: agent/india8-cluster-casting
updated: 2026-08-25

## PURPOSE
This ledger is the mandatory bridge between selected destinations and any future calendar. No exact date plan may be trusted until every used edge has a realistic door-to-door occupied-time range.

Companion topology audit:
`runs/active/INDIA10-CLUSTER-COVERAGE-REAUDIT-001/CLUSTER_TOPOLOGY_FEASIBILITY_2026-08-25.md`.

## FIXED / RETAINED CORE WORLDS TO CONNECT
1. KUMAON — protected A+/A world; detailed local corridor below.
2. VARANASI / SARNATH — protected A+ world.
3. BODH GAYA / GAYA — protected A+ world.
4. TIRUVANNAMALAI / ARUNACHALA — protected A+ world.
5. DELHI — contains at least DELHI / CHHAWLA / Nirmal Dham A+.
6. AGRA — contains AGRA / AGRA / Taj Mahal A+.

Potential/deferred worlds such as Rishikesh/Haridwar/Kankhal, Braj, Prayagraj and out-of-radius challengers are NOT silently inserted. They enter the route only after topology/Mark selection supports them.

## HARD TRANSFER FIELDS
Every used edge must eventually contain:
- origin full name/status / HOTEL if sleeping base;
- destination full name/status / HOTEL if sleeping base;
- mode sequence;
- checkout/pickup/loading;
- ground access to terminal if any;
- check-in/security/platform buffer;
- scheduled flight/train;
- arrival/baggage/exit;
- ground transfer to next HOTEL/site;
- meal/rest/toilet allowance;
- winter/traffic/fog/roadwork/delay buffer;
- realistic DOOR_TO_DOOR occupied-time range;
- usable daylight/energy remaining;
- same-day A+/A feasibility;
- confidence + recheck date.

Raw drive/rail/flight duration NEVER equals calendar occupied time by itself.

---

# A. KUMAON LOCAL CORRIDOR — CURRENT VERIFIED WORKING GEOMETRY

## A1. KUMAON / HAIDAKHAN -> KUMAON / NAINITAL
Origin:
`KUMAON / HAIDAKHAN / HOTEL Haidakhan Ashram (overnachtingsbasis in het Haidakhan Babaji-ashramcomplex; naam-prefix HOTEL alleen als slaapbasis) — accommodatie-status: planned/selected, exact booking status to reconcile`
Destination sleeping world:
`KUMAON / NAINITAL / HOTEL [Nainital sleeping base — exact current accommodation lock to reconcile]`
Protected site context:
`KUMAON / NAINITAL / Hotel Evelyn (historisch hotel waar Ram Dass verbleef; exacte kamer niet bewezen) — huidige status: A+`

Existing corridor evidence:
- road-distance working class: ~50–65 km;
- raw road-time class: ~1h20–2h30 depending exact Haidakhan approach/road source.

Calendar status:
- `INTRA_CLUSTER_TRANSFER / BASE_CHANGE`.
- Door-to-door occupied time is NOT yet closed because exact sleeping-origin access, checkout/loading, Nainital drop/check-in and winter road buffer still need to be added.
- No calendar date may use the raw road time as the whole transfer block.

## A2. KUMAON / NAINITAL -> KUMAON / KAINCHI
Origin context:
`KUMAON / NAINITAL / Naini Lake-rondwandeling (ca. 3,2 km / 55–75 min vanaf The Flatts/lakefront; volledige lus via Mall Road en de autovrije Thandi Road; voorkeur vroeg in de ochtend) — huidige status: A+`
Destination:
`KUMAON / KAINCHI / Kainchi Dham (Neem Karoli Baba-ashramcomplex; kernplek voor Neem Karoli Baba en Ram Dass) — huidige status: A+`

Existing evidence:
- road distance ~17 km;
- raw road time ~40–60 min;
- route-builder option: A+ Naini Lake loop before transfer with effectively 0 extra road km;
- combined morning walk + transitions + Nainital->Kainchi movement before Kainchi visit: working class ~1h40–2h25.

Calendar consequence:
- rare movement day where a protected A+ walk can be integrated without road detour;
- exact hotel pickup/check-out and Kainchi visit opening window still need to be attached before assigning a clock schedule.

## A3. KUMAON / KAINCHI -> KUMAON / DWARAHAT
Origin:
`KUMAON / KAINCHI / Kainchi Dham (Neem Karoli Baba-ashramcomplex; kernplek voor Neem Karoli Baba en Ram Dass) — huidige status: A+`
Destination:
`KUMAON / DWARAHAT / Yogoda Satsanga Sakha Ashram — Dwarahat (YSS-ashram van Paramahansa Yogananda’s organisatie; meditatiecentrum in de Mahavatar Babaji/Kriya-regio) — huidige status: A`

Direct efficient road spine:
`Kainchi -> Khairna -> Ranikhet -> Dwarahat`.
Existing raw road evidence:
- ~71.7 km / ~2h24 working road-time class to Dwarahat;
- winter/fog/traffic buffer required.

Calendar consequence:
- Mark wants a FULL DAY at the YSS A location, so this raw ~2h24 transfer MUST NOT be hidden inside that full day unless departure/arrival mathematics genuinely preserves the full visit block.
- likely transfer belongs on prior day, or YSS full day is based from HOTEL Dunagiri Retreat with separate commute; exact arrangement pending Dwarahat<->HOTEL Dunagiri Retreat timing closure.

### Optional transfer catch — do not let it endanger YSS/Babaji
`KUMAON / KAKRIGHAT / Kakrighat (Kosi-rivierplek waar Vivekananda in 1890 een belangrijke realisatie had; corridor-bijvangst) — huidige status: A* (formeel A; SKIP_FIRST)`
- roughly 14 km out-and-back from Khairna junction on direct spine;
- ~20–30 min extra raw driving;
- likely ~45–90 min total increment including visit;
- skip before compromising intrinsic A/A+ time.

## A4. KUMAON / DWARAHAT -> KUMAON / DUNAGIRI
Visit anchor:
`KUMAON / DWARAHAT / Yogoda Satsanga Sakha Ashram — Dwarahat (YSS-ashram van Paramahansa Yogananda’s organisatie; meditatiecentrum in de Mahavatar Babaji/Kriya-regio) — huidige status: A`
Sleeping destination:
`KUMAON / DUNAGIRI / HOTEL Dunagiri Retreat (spiritueel retreat/hotel bij de Mahavatar Babaji-grot; gekozen wandelbasis voor deze pelgrimswereld) — accommodatie-status: LOCKED_BY_MARK`

Existing relation:
- HOTEL Dunagiri Retreat material places the property about 25 km from Dwarahat;
- exact current winter road time is still `TO_VERIFY` before calendar use.

Hard user constraint:
- user is Ananda, not YSS/SRF; no overnight stay at the YSS ashram may be planned.
- therefore HOTEL Dunagiri Retreat is likely sleeping base for the full-day YSS visit if commute timing remains acceptable.

Required closure:
- exact HOTEL Dunagiri Retreat -> YSS ashram door-to-door morning drive;
- exact evening return in darkness/winter conditions;
- whether driver wait in/near Dwarahat all day is practical;
- if late return is undesirable, identify normal non-YSS HOTEL alternative only if needed, without unlocking HOTEL Dunagiri Retreat.

## A5. KUMAON / DUNAGIRI -> KUMAON / KUKUCHINA-DUNAGIRI / MAHAVATAR BABAJI'S CAVE
Origin:
`KUMAON / DUNAGIRI / HOTEL Dunagiri Retreat (spiritueel retreat/hotel bij de Mahavatar Babaji-grot; gekozen wandelbasis voor deze pelgrimswereld) — accommodatie-status: LOCKED_BY_MARK`
Destination experience:
`KUMAON / KUKUCHINA-DUNAGIRI / Mahavatar Babaji's Cave (bezoekbare YSS/Kriya-pelgrimsgrot waar Lahiri Mahasaya volgens de YSS/Kriya-traditie in 1861 door Mahavatar Babaji in Kriya Yoga werd ingewijd; hoofdreden voor de reis) — huidige status: A+`

Current planning principle:
- direct hotel-based walk is default;
- no taxi to a farther generic trailhead unless a longer variant is demonstrably exceptionally more beautiful/spiritually valuable;
- working retreat claim puts trek in ~2–3 km one-way class depending page/context;
- exact track/time/ascent/legal/wildlife/winter safety remains `TO_VERIFY`.

Calendar consequence:
- protected A+ local walking day/half-day, NOT inter-base transfer;
- sufficient daylight, unhurried cave time and safety take priority over squeezing other sites into same block.

## A6. WRONG KUMAON ORDER — PROHIBITED
Do NOT use:
`Haidakhan -> Dwarahat/Dunagiri -> Nainital/Kainchi`.
It creates unnecessary backtracking.

Efficient baseline:
`KUMAON / HAIDAKHAN -> KUMAON / NAINITAL -> KUMAON / KAINCHI -> KUMAON / DWARAHAT -> KUMAON / DUNAGIRI/KUKUCHINA`.

Global consequence: Kumaon EXIT is from the eastern/highland Dwarahat/Dunagiri end, not from Nainital. Global transfer calculations must use the actual last base.

---

# B. INTER-CLUSTER EDGES — CURRENT STATUS

## B1. DELHI <-> KUMAON
Potential modes:
- private car entire way;
- rail Delhi -> Kathgodam/Haldwani + driver;
- flight Delhi -> Pantnagar + road;
- combinations depending first/last Kumaon base.
Status: `TO_VERIFY_FINAL_DOOR_TO_DOOR`.
Do NOT choose mode from train/flight duration alone.

## B2. DELHI <-> AGRA
Potential modes:
- fast train + station transfers;
- private car/driver.
Status: `TO_VERIFY_FINAL_DOOR_TO_DOOR`.
Taj Mahal A+ opening/time-of-day may make prior-night arrival superior to same-day transfer.

## B3. DELHI <-> VARANASI
Potential modes:
- flight + both airport transfers;
- overnight train if it saves waking daylight without excessive fatigue.
Status: `SECONDARY_EDGE`; current best topology may not need this direct link.

## B4. AGRA -> EASTERN CORRIDOR
Direct Agra -> Varanasi is possible, but topology now also tests optional Prayagraj and Bodh Gaya before Varanasi. Do not lock this direct edge yet.
Status: `ROUTE_ORDER_DEPENDENT`.

## B5. BODH GAYA/GAYA -> VARANASI/SARNATH
Current research 2026-08-25:
- Gaya -> Varanasi train overview: fastest shown ~2h55; average ~4h23; multiple services;
- short enough to treat as a natural paired eastern chain, with final station/hotel overhead still to add.
Status: `TOPOLOGY_CLOSED_AS_NATURAL_PAIR / EXACT_DOOR_TO_DOOR_PENDING`.
Preferred direction for current global topology: `BODH GAYA/GAYA -> VARANASI/SARNATH`, because Varanasi is the stronger current southbound air gateway.

Source: https://www.rome2rio.com/Train/Gaya/Varanasi

## B6. BODH GAYA/GAYA -> SOUTH — OLD DIRECT-CHENNAI ASSUMPTION DOWNRANKED
Current Gaya -> Chennai search 2026-08-25 shows no nonstop service; connection required.
Status: `INFERIOR_CURRENT_TOPOLOGY`, not prohibited forever.

This makes a Gaya-finish before the south less attractive than finishing the eastern chain in Varanasi.

Source: https://www.flightconnections.com/flights-from-gay-to-maa

## B7. VARANASI -> BENGALURU -> TIRUVANNAMALAI/ARUNACHALA
Current 2026-08-25 evidence:
- Air India Express publishes Varanasi -> Bengaluru daily non-stop service; direct block ~2h35; frequency may vary;
- Dec 2026 / Jan 2027 fare inventory is not yet displayed on current route page, so exact trip-date service is NOT locked;
- Bengaluru Airport -> Tiruvannamalai ~231.5–232.7 km / ~3h33–3h34 raw drive.

Status: `STRONG_CURRENT_SOUTHBOUND_GATEWAY_HYPOTHESIS / DATE_RECHECK_REQUIRED`.

Calendar interpretation:
- this is still likely a FULL/SUBSTANTIAL TRAVEL DAY once airport access, preflight buffer, baggage, driver pickup, food/rest and hotel arrival are included;
- Bengaluru is an AIR GATEWAY only unless Mark separately selects it as sightseeing content.

Sources:
- https://flights.airindiaexpress.com/en-in/varanasi-to-bengaluru-flights
- https://www.rome2rio.com/s/Bengaluru-Airport-BLR/Tiruvann%C4%81malai

## B8. HARIDWAR–RISHIKESH / KANKHAL — OPTIONAL CLUSTER INSERT
Working combined world:
`HARIDWAR–RISHIKESH / HARIDWAR–KANKHAL–RISHIKESH / spirituele Ganges-cluster (Rishikesh-yoga/ashramwereld plus Haridwar/Kankhal-heilige Gangeslaag) — huidige status: OPEN`.

Current evidence:
- Delhi -> Rishikesh: public bus ~5h11; raw road calculator ~3h23; conservative winter planning class ~5–6h before final door-to-door closure;
- Rishikesh -> Nainital: ~236 km; cab planner ~5h15; public-transport path ~7h32; conservative private-driver class ~5.5–7h before exact endpoint/access closure.

Topology conclusion:
- natural insertion is `DELHI -> HARIDWAR/RISHIKESH -> KUMAON`;
- this avoids a mandatory return to Delhi;
- compared with direct Delhi -> Kumaon it likely adds roughly one half/full extra movement block plus an extra base change, BEFORE adding actual stay days;
- it is therefore MODERATE burden, not route-breaking;
- exact 31 Dec 2026 remains `DATE_WISH`, not a date lock, because forcing that date could create backtracking.

Status: `OPTIONAL_REALISTIC_MODERATE_BURDEN`.

Sources:
- https://www.rome2rio.com/s/Delhi/Rish%C4%ABkesh
- https://www.rome2rio.com/s/Rish%C4%ABkesh/Nainital
- https://www.makemytrip.com/routeplanner/rishikesh-nainital.html

## B9. BRAJ NEAR AGRA — OPTIONAL LOW-GEOMETRY INSERT
Working world:
`BRAJ / MATHURA–VRINDAVAN–GOVARDHAN / Braj-pelgrimscluster (Krishna-landschap direct bij de Delhi–Agra-corridor) — huidige status: OPEN`.

Current evidence:
- Agra -> Mathura ~57 km / ~51 min raw drive;
- Agra -> Vrindavan ~66 km / ~59 min raw drive.

Status: `OPTIONAL_LOW_GEOMETRIC_BURDEN`.
Its principal time cost is visit/base time, not detour geometry.

Sources:
- https://www.rome2rio.com/s/Agra/Mathura
- https://www.rome2rio.com/s/Agra/Vrind%C4%81van

## B10. PRAYAGRAJ EASTBOUND — OPTIONAL CORRIDOR INSERT
Working world:
`PRAYAGRAJ / PRAYAGRAJ / heilige Ganges–Yamuna-samenvloeiingscluster (Triveni Sangam/Allahabad-pelgrimswereld op de west-oost spooras) — huidige status: OPEN`.

Current evidence:
- Agra Fort -> Prayagraj: 21 direct trains in current data; fastest listed ~5h55, many slower;
- Prayagraj -> Gaya: many direct trains; fastest ~4h14; practical daily examples around ~5h35–6h30.

Topology conclusion:
- clean optional sequence: `AGRA -> PRAYAGRAJ -> BODH GAYA/GAYA`;
- not a dramatic geographic side excursion;
- adds its own visit/base time and station overhead.

Status: `OPTIONAL_LOW_TO_MODERATE_GEOMETRIC_BURDEN`.

Sources:
- https://www.railroute.in/trains/agra-fort-to-prayagraj-jn
- https://www.railroute.in/trains/prayagraj-jn-to-gaya-jn
- https://www.confirmtkt.com/trains/prayagraj-to-gaya-train-tickets

---

# C. CURRENT BEST TOPOLOGY — NO DATES
Working global spine to test first:

`DELHI`
`-> optional HARIDWAR–RISHIKESH`
`-> KUMAON: HAIDAKHAN -> NAINITAL -> KAINCHI -> DWARAHAT -> DUNAGIRI/KUKUCHINA`
`-> major Kumaon exit to plains`
`-> optional BRAJ`
`-> AGRA`
`-> optional PRAYAGRAJ`
`-> BODH GAYA/GAYA`
`-> VARANASI/SARNATH`
`-> VNS -> BLR nonstop hypothesis`
`-> road BLR -> TIRUVANNAMALAI/ARUNACHALA`.

This is topology only. It does NOT select optional clusters and it does NOT authorize exact nights/dates.

---

# D. CALENDAR GATE
No exact day numbers or dates are authorized from this ledger yet.

A calendar may be rebuilt only when:
1. selected route edges are closed to realistic door-to-door ranges;
2. each base change is charged checkout/loading/check-in time;
3. flights/trains include terminal access/wait/baggage/exit;
4. mountain transfers include winter/traffic/fog buffer;
5. A+ and intrinsic A experiences have protected usable time;
6. A* SKIP_FIRST extras occupy genuine slack only;
7. route order is checked for backtracking;
8. number of nights follows time mathematics rather than being chosen first;
9. any date wish (including Rishikesh 31 Dec) is tested against the natural route rather than allowed to distort it silently.

## ACTIVE FRONTIER
P0 — global cluster topology/feasibility: ACTIVE and now materially narrowed.
P1 — close exact eastern-Kumaon exit to plains based on the actual final HOTEL/base, because this is one of the largest fixed transfer blocks.
P2 — retain/drop optional clusters only after their route burden is visible; Mark remains sole subjective selector.
P3 — once dwell-time ranges per retained cluster are known, build total-night scenarios.
P4 — only then reintroduce exact calendar dates and event/date wishes.

## REPLACEABILITY NOTE
A successor must read this file together with `CLUSTER_TOPOLOGY_FEASIBILITY_2026-08-25.md` before reconstructing any day plan. Older conversational calendar sketches are non-authoritative.