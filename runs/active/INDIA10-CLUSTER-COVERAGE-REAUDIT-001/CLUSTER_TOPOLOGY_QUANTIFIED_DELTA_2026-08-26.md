# INDIA10 — CLUSTER TOPOLOGY QUANTIFIED DELTA — 2026-08-26

status: ACTIVE_DELTA / NO_EXACT_DATES
branch: agent/india8-cluster-casting
updated: 2026-08-26
read_after: `CLUSTER_TOPOLOGY_FEASIBILITY_2026-08-25.md`

## PURPOSE
This delta separates two things that earlier route discussion too easily mixed:

1. `CONTENT_DAYS` — how much meaningful time Mark actually wants inside a cluster;
2. `LOGISTICS_TAX` — extra occupied transfer time + base changes caused by including that cluster compared with the cleanest route without it.

No exact calendar dates are authorized here.

## FIXED CORE RESULT
The six fixed core worlds remain structurally feasible when travel time is treated honestly:
- Kumaon;
- Delhi;
- Agra / Taj Mahal;
- Bodh Gaya / Gaya;
- Varanasi / Sarnath;
- Tiruvannamalai / Arunachala.

Their unavoidable expensive pieces are especially the Kumaon mountain corridor/exit and the east/north -> south transition.

---

## 1. HARIDWAR–RISHIKESH / HARIDWAR–KANKHAL–RISHIKESH / spirituele Ganges-cluster (Rishikesh-yoga/ashramwereld plus Haridwar/Kankhal-heilige Gangeslaag) — huidige status: OPEN

### Correct topology
Preferred insertion:
`DELHI -> HARIDWAR/KANKHAL/RISHIKESH -> KUMAON`.

Do NOT insert it after the eastern end of Kumaon at Dwarahat/Dunagiri; that creates a long westward bounce before travelling east/south again.

### Current movement evidence
- Delhi -> Rishikesh: current public planning evidence ~218 km; raw road estimate ~3h23, while public-transport/practical planning is roughly 5h+. Treat as a SUBSTANTIAL movement block, not a 3-hour calendar slot.
- Rishikesh -> Nainital: current public figures roughly 236–253 km; practical private-road planning roughly 5.5–7h depending route/traffic.
- Rishikesh -> Dwarahat: roughly 271–275 km / about 8h planning class; this proves why inserting this cluster AFTER eastern Kumaon is poor.
- Public route planning to a Haidakhan-labelled destination gives roughly 266 km / ~4h50 raw from Rishikesh, but exact-entity confidence is lower than official Haidakhan access evidence. Do NOT calendar-lock this figure yet.
- Official Haidakhandi Samaj access information for the true `KUMAON / HAIDAKHAN / Haidakhan Vishwa Mahadham (hoofdashram van Haidakhan Babaji bij Village Haidakhan aan de Gautami Ganga; historische grot waar hij volgens de traditie in 1970 verscheen) — huidige status: A+` gives Delhi -> Haidakhan roughly 337 km / 8–9h. Therefore a direct Delhi->Kumaon approach is itself already a major northern movement.

### LOGISTICS_TAX interpretation
Including this Ganges cluster BEFORE Kumaon does NOT add an entirely separate cross-country crossing on top of a cheap Delhi->Kumaon transfer. Instead it converts one already-large northern approach into TWO substantial road legs and adds one base change.

Working class:
`LOGISTICS_TAX = MATERIAL / BIGGEST CURRENT OPTIONAL NORTHERN INSERT`, but `NOT ROUTE-BREAKING` if used once before Kumaon.

### CONTENT_DAYS interpretation
- If Mark wants only a single New Year's Eve or brief sightseeing stop, the logistics value is weak.
- If Mark genuinely wants roughly 2–3 meaningful days of Ganges/ashram/rest content, the insertion can plausibly justify itself and may even function as decompression before the heavy Kumaon mountain corridor.

### Special dates
- `31 Dec 2026` remains `DATE_WISH`, not route lock.
- Haridwar's announced 14 Jan 2027 Kumbh/Ardh Kumbh opening + Makar Sankranti Snan is a discovery signal only. Do NOT create a later westward return for it unless Mark later gives it exceptional priority and the final route mathematics supports it.

Verdict: `KEEP_IN_FEASIBILITY_SET`. Do not cut yet.

---

## 2. BRAJ / MATHURA–VRINDAVAN–GOVARDHAN / Braj-pelgrimscluster (Krishna-landschap direct bij de Delhi–Agra-corridor) — huidige status: OPEN

Current geometry near Agra is cheap:
- Agra -> Mathura roughly 57 km / about 1h raw road class;
- Agra -> Vrindavan roughly 66–70 km / about 1–2h raw road class depending endpoint/traffic.

Working class:
`LOGISTICS_TAX = LOW`.

Most of the real cost is therefore its own `CONTENT_DAYS` / possible extra sleeping base, not a huge geographic detour.

Verdict: currently the cheapest major optional cluster geometrically. Content must still earn its dwell time.

---

## 3. PRAYAGRAJ / PRAYAGRAJ / heilige Ganges–Yamuna-samenvloeiingscluster (Triveni Sangam/Allahabad-pelgrimswereld op de west-oost spooras) — huidige status: OPEN

Current corridor relation:
- Agra -> Prayagraj is roughly a 6–7h rail/road movement class before full door-to-door overhead;
- Prayagraj -> Varanasi can be roughly a 2–3h rail/road movement class;
- direct Agra -> Gaya overnight rail exists, so Prayagraj is NOT required to make the eastern route work.

Working class:
`LOGISTICS_TAX = LOW_TO_MODERATE / CORRIDOR_COMPATIBLE`.

It can split the west-east crossing naturally, but still creates its own stop/base-change burden. Retain only for spiritual/travel value, not because routing needs it.

---

## 4. MYSORE / BENGALURU / optional south-west sightseeing extension (separate sightseeing world beyond the required Arunachala route) — huidige status: OPEN

Do not confuse Bengaluru airport use with Bengaluru sightseeing inclusion.

Current relation:
- Tiruvannamalai -> Bengaluru is roughly 203 km / ~3h raw road class or ~4h+ bus class before door-to-door overhead;
- Varanasi -> Chennai remains the stronger current primary air-gateway hypothesis when actual trip-date service supports it;
- Bengaluru remains a useful fallback air gateway, but that does NOT make Mysore/Bengaluru sightseeing free.

Working class:
`LOGISTICS_TAX = MATERIAL/HIGH for actual sightseeing extension`.

Verdict: do not assume inclusion until content is strong enough to justify a separate southern tail.

---

# CURRENT OPTIONAL ORDER BY LOGISTICS TAX — NOT BY QUALITY
From cheapest/easiest insertion to most burdensome current optional addition:

1. `BRAJ / MATHURA–VRINDAVAN–GOVARDHAN / Braj-pelgrimscluster (Krishna-landschap direct bij de Delhi–Agra-corridor) — huidige status: OPEN` — LOW geometric tax.
2. `PRAYAGRAJ / PRAYAGRAJ / heilige Ganges–Yamuna-samenvloeiingscluster (Triveni Sangam/Allahabad-pelgrimswereld op de west-oost spooras) — huidige status: OPEN` — LOW/MODERATE, corridor-compatible.
3. `HARIDWAR–RISHIKESH / HARIDWAR–KANKHAL–RISHIKESH / spirituele Ganges-cluster (Rishikesh-yoga/ashramwereld plus Haridwar/Kankhal-heilige Gangeslaag) — huidige status: OPEN` — biggest current optional northern insertion, but coherent before Kumaon.
4. `MYSORE / BENGALURU / optional south-west sightseeing extension (separate sightseeing world beyond the required Arunachala route) — huidige status: OPEN` — high unless exceptional content justifies a separate southern tail.

This ranking is ONLY logistics burden. It is not an A/B/C judgment.

# HARD NEXT-ZOOM RULE
Before nights or dates, compare each retained optional cluster on:
`CONTENT_DAYS_WANTED + LOGISTICS_TAX + BASE_CHANGES + REST_VALUE + UNIQUE_VALUE`.

Do not optimize a special festival/date first and then force the trip around it.
