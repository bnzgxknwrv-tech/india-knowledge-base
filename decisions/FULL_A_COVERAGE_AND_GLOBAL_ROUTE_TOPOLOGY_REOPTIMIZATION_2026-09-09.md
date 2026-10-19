# FULL A-COVERAGE + GLOBAL ROUTE TOPOLOGY REOPTIMIZATION — MARK INSTRUCTION

Date: 2026-09-09
Source: explicit Mark instruction in ChatGPT India-regie.
Status: ACTIVE OVERRIDE / NEW TEST. This reopens MACRO ORDER / ROUTE TOPOLOGY for optimization. It does NOT change any Mark grade and does NOT reopen FINAL OUT worlds.

## 1. WHY THIS TASK EXISTS

Mark likes the current waking-hours planning document, but noticed that many retained A/A+ locations are not individually visible. That makes it impossible to judge honestly whether the current durations really fit.

Separately, Mark explicitly asks whether the current macro-order is truly globally optimal. He authorizes a full shuffle of the INCLUDED worlds: reverse-ish orders, Agra late/last, different east/west/south sequencing, train-heavy vs flight-heavy vs hybrid, and any other feasible topology. The incumbent must be treated as a falsification target, not as a preferred answer.

## 2. HARD SCOPE THAT DOES NOT REOPEN

International envelope:
- AI156 AMS→DEL: depart 18 Dec 2026 ~20:35; arrive DEL 19 Dec ~10:15.
- AI155 DEL→AMS: depart 21 Jan 2027 ~12:20.
- Exactly 33 physical India nights: night 19 Dec through night 20 Jan inclusive.

Hard retained worlds / locks:
- Delhi arrival operation including Nirmal Dham [A+] if safely feasible.
- Kumaon included: Nainital 3n, Dunagiri/Kukuchina 3n, Haidakhan Vishwa Mahadham 3n with 2 full protected quiet days. Do not silently alter these durations.
- Agra/Taj world retained; 1 Agra hotel night unless a demonstrably superior topology can preserve the locked Taj experience without violating prior Mark decisions. Do not change the Taj [A+] grade.
- Bodh Gaya retained; 2-vs-3 remains a live duration sensitivity. The current stress-test is 3n.
- Varanasi/Sarnath retained; 8 nights LOCKED_BY_MARK.
- Kolkata/Dakshineswar retained; current working block 3n.
- Tiruvannamalai/Arunachala retained; 4-vs-5 remains a live sensitivity. The current stress-test is 4n.
- Chennai may remain as content-plus-buffer if objectively useful; do not assume it must be a full content world.
- Exactly ONE final Delhi night immediately before AI155.

FINAL OUT — NEVER REOPEN OR RE-PRESENT unless Mark separately says so:
- Puri/Odisha
- Serampore/Srirampur as trip stop/world/sleep/excursion
- Vrindavan/Braj/Mathura–Vrindavan–Govardhan

No booking/contact/PDF in this task. Exact Jan-2027 transport inventory remains LIVE_RECHECK_LATER where not yet bookable.

## 3. FIRST REQUIRED STEP — FULL A/A+ COVERAGE AUDIT

Before solving topology, build an exact inventory from the CURRENT canonical decision files/registers of every retained physical A+ and A visit/content anchor. Do not rely on the current PDF as canon.

For every retained A/A+ item classify the current 22-page waking-hours PDF as exactly one of:
- EXPLICIT_GUARANTEED: individually named and given a real visit/time block;
- HIDDEN_IN_CLUSTER: intended inside a broader block but not individually visible, so Mark cannot judge its time;
- CONDITIONAL: mentioned only if access/time/energy allows, so not safely guaranteed;
- MISSING: absent from the schedule;
- SPECIAL_STATUS: e.g. A*/SKIP_FIRST, parent-world label, accommodation-grade, or experience-grade that should not be double-counted as an ordinary physical A/A+ visit.

No parent/child double-counting. No accommodation [A+] counted as a sightseeing omission unless it is itself a retained visit anchor.

### Audit seed already found by regisseur — MUST independently verify/repair against all later decision files

Confirmed outright omissions from the current PDF, based on retained current A/A+ canon already checked:
1. Bodh Gaya same-hill ridge/viewpoint/context [A].
2. Maa Annapurna Temple, Varanasi [A].
3. Vishalakshi Gauri Temple, Varanasi [A].
4. Bhaskarananda Samadhi / Anand Bagh, Varanasi [A].
5. Saranganath Temple, Sarnath [A].
6. Tulsi Manas Temple, Varanasi [A].

Currently mentioned but not safely guaranteed:
7. Lahiri Mahasaya original/family house, Varanasi [A] — current plan says only if exact access is confirmed.
8. Shitala Mata Temple, Varanasi [A] — current plan only gives Shitala context/position near Ganga Aarti, not a real visit block.

Currently hidden within a broad Sarnath block rather than individually inspectable:
9. Dhamek Stupa [A].
10. Mulagandha Kuti Vihara [A].
11. Chaukhandi Stupa [A].
12. Deer Park [A].

Special separate status:
- Karkrighat [A*/SKIP_FIRST] is not a normal A/A+ omission and must be reported separately, not silently converted into required content.

The solver must verify whether later additions/overrides create any further A/A+ items not captured in this seed. The final count must be exact and evidence-based.

## 4. ROUTE SEARCH SPACE — FULL SHUFFLE AUTHORIZED

Treat the included travel worlds as graph nodes and real transport options as edges. Do NOT assume the incumbent order is correct.

At minimum test:
1. current incumbent family: Delhi → Kumaon → Agra → Bodh Gaya → Varanasi → Kolkata → Tiruvannamalai/Chennai → Delhi;
2. reverse-ish / south-first feasible family;
3. Agra as late as possible / last substantive world before final Delhi, including whether arriving into Agra by air is actually useful under current airport connectivity;
4. Agra inserted at alternative positions where rail geometry may reduce dead travel;
5. Bodh Gaya ↔ Varanasi ↔ Kolkata permutations that remain date/transport-feasible;
6. Kolkata before vs after Varanasi where rational;
7. train-heavy family using overnight rail where sleepable rail replaces daytime dead travel;
8. flight-heavy family where airports truly save whole-human hours after airport/road/buffer costs;
9. hybrid family selected from the best edges, not by transport ideology;
10. any topology the solver discovers that beats all of the above.

Do not mechanically enumerate impossible permutations. Prune with transparent reasons, but search broadly enough to support a GLOBAL-OPTIMUM claim or explicitly state that only a bounded optimum was proved.

## 5. EDGE COST MODEL — WHOLE HUMAN, NOT MAP DISTANCE

For each candidate inter-world edge measure:
- door-to-door elapsed time;
- waking travel time;
- sleepable travel time;
- road time;
- airport access + 2h-ish process + baggage + airport egress;
- station access + platform buffer + egress;
- hotel/base churn;
- wake-up before 05:30;
- arrival after 22:00;
- winter fog/delay exposure;
- same-day recovery alternatives if cancelled;
- whether a night train replaces a hotel night without destroying sleep;
- whether a flight looks fast airborne but loses on door-to-door burden;
- date-specific weekly service/closures/festivals/crowds.

## 6. OBJECTIVE FUNCTION — LEXICOGRAPHIC

1. HARD FEASIBILITY: 33/33, international flights, locked durations, FINAL OUT, all retained A+/A content.
2. SAFETY / FAILURE TOLERANCE: especially AI155 protection and fragile connections.
3. WHOLE-HUMAN DEAD TRAVEL BURDEN: minimize waking hours lost to getting from world to world.
4. DATE QUALITY: closures, weekdays, festivals/crowds and visit quality.
5. PROTECTED EXPERIENCE + REST: preserve slow/ashram/meditation/recovery time; do not win by making 12-hour activity days.
6. TRANSPORT QUALITY: sleep quality, hotel churn, early starts, luggage burden.
7. MARK TIE-BREAK: if genuinely discretionary, north/Kumaon has preference over generic city slack; Chennai may beat it where safety/content/rest is stronger.
8. COST/CONVENIENCE only after higher-order criteria.

## 7. REQUIRED OUTPUT

A. Exact A/A+ coverage matrix and counts: EXPLICIT / HIDDEN / CONDITIONAL / MISSING / SPECIAL.
B. World-node table: hard duration, movable duration, date constraints, strongest content constraints.
C. Edge matrix for every serious neighboring-world transport pairing considered: best train/flight/road option + whole-human cost.
D. Search/pruning log: which route families were tested, which were discarded, and why.
E. TOP 5 exact-dated 33-night candidate routes, each with:
- full night geometry;
- all retained A/A+ fit proof;
- total intercity waking travel hours;
- total road hours;
- airport-process hours;
- awake rail hours;
- sleepable rail hours;
- number of flights;
- number of hotel/base changes;
- number of <05:30 wake-ups;
- heavy days;
- fragile edges;
- closure/festival conflicts;
- A+/A content hours;
- explicit rest/slow hours;
- 33/33 proof.
F. Direct head-to-head against the current incumbent.
G. Explicit answers:
1. Is the current macro-order still the best?
2. Does Agra-last help or lose, and exactly why?
3. Does reversing the trip help?
4. Which flights should become trains?
5. Which trains should become flights?
6. What is the single largest avoidable block of dead travel in the current route?
7. Can any topology create a genuinely free extra night without violating locks/rest/content?
8. If no global optimum can be proved because Jan-2027 schedules are not final, what topology is robustly best under current recurring patterns?

No final Mark lock. Return evidence and recommendation only.
