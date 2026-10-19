# GLOBAL REGIE CANON AUDIT — 2026-08-23

Status: ACTIVE REGIE GUARDRAIL
Purpose: prevent INDIA8/INDIA9+ from re-presenting already-decided locations, missing sleep anchors, or using stale summaries over later Mark decisions.

**PARTIALLY STALE (flagged 2026-08-23, task 008 optimization pass):** this file still
lists Turiya Niwas (080) as an active sleep-anchor/A-destination below. Mark
subsequently confirmed directly that the entire Kasar Devi/Crank's Ridge/Almora module
— Turiya Niwas (080) AND Bodh Ashram (081), both `LOCKED_BY_MARK` — is dropped from the
working route (heavier candidates found elsewhere). See
`runs/active/INDIA8-MARK-CLUSTER-DECISIONS-2026-08-20/MARK_DECISION_KASAR_ALMORA_MODULE_DROPPED_2026-08-23.md`
(commit `53c7484` on `agent/cci-mark-decision-kasar-almora-dropped`) for the exact
decision record. This is a route-inclusion decision, not a canon/value edit — the
underlying site grades in `PROTECTED_CANON_BASELINE.csv` are unchanged — but any
regie/route text below that still treats Turiya Niwas as an active stop is superseded
by that later decision. This file is otherwise NOT fully re-verified in this pass;
treat every other claim below with the same "check PROTECTED_CANON_BASELINE.csv and
governance/PRECEDENCE_MAP.jsonl first" discipline as any other pre-baseline file.

## ROOT CAUSE OF 2026-08-23 REGIE MISS
The regie chat over-weighted recent runs/worker branches and under-read legacy-but-still-valid root canon such as `CLUSTER_ANCHORS.md`, `LOCKED_A.md`, `LOCKED_B.md`, `LOCKED_C.md` and later accommodation decision files. This caused already-known facts (e.g. Jageshwar A, Binsar C, Kumaon sleep anchors) to be presented as if new.

The repository contains multiple generations of truth:
1. legacy region/root locks and anchors;
2. current global numbering/master/reconciliation runs;
3. later explicit Mark decisions and cluster-level decisions.
A global regisseur MUST reconcile these layers before presenting choices.

## PRECEDENCE FOR TRAVEL REGIE
For a claim of type A/B/C, cluster status, hotel/stay, or route preference, apply in this order:

1. **Latest explicit Mark decision file** for the exact item/cluster.
2. **Latest accommodation register / hotel decision** for sleep-base status.
3. **Current central all-findings master + current physical-resolution/access outputs** for factual site identity, person links, micro-sites, access and continuity.
4. **Current governance / live handoff** for project scope, method and route-family decisions.
5. **Legacy LOCKED_A/B/C and CLUSTER_ANCHORS** as protected benchmark when no later explicit override exists.
6. Candidate files, old summaries and historical cluster overviews are NON-authoritative when contradicted by any higher layer.

Hard rule: `latest explicit Mark decision > older Mark decision`; but an old Mark decision remains protected if no explicit later override exists. Never infer an override from research alone.

## DO-NOT-REPRESENT-AS-NEW CHECK
Before presenting ANY site to Mark for A/B/C:
1. search current Mark-decision runs;
2. check legacy protected locks if region predates the current global master;
3. check parent/microcluster map so a micro-site is not re-presented separately;
4. check whether current cluster status makes the site only an opportunistic add-on;
5. if an existing decision is found, present it as `ALREADY A/B/C` and only surface new decision-relevant information.

## CURRENT TRAVEL DATES
18 Dec 2026 through 21 Jan 2027 = 34 days. Flights booked. Final calendar/festival/closure layer must use these dates.

## CURRENT CLUSTER-LEVEL DECISIONS
- Kumaon / Nainital / Kainchi / Babaji: A.
- Vrindavan / Braj / Mathura: A, route-sensitive.
- Varanasi / Sarnath: A.
- Bodh Gaya / Gaya: A.
- Tiruvannamalai / Arunachala: A, fixed.
- Mysore / Bengaluru: C as cluster; individual site A/B/C remains preserved.
- Haridwar / Kankhal / Rishikesh: B/reserve; Rishikesh atmosphere appeals; Kankhal Anandamayi Mahasamadhi remains site A.
- Agra: A but Taj Mahal only as route driver; sunrise/earliest practical visit is HARD requirement.
- East / Kolkata route family: parked unless capacity/exceptional override.

## CURRENT KNOWN SLEEP ANCHORS / STAY DECISIONS
### Kumaon / Babaji / Dwarahat
- **Joshi Guest House, Kukuchina — LOCKED** sleep base for Babaji Cave, Babaji Smriti Bhavan, Dunagiri Temple, YSS Dwarahat.

### Kumaon / Nainital
- **Hotel Evelyn, Nainital — CLUSTER_ANCHOR and site-level A.**
- Final route MUST resolve actual overnight feasibility and Ram Dass historic cave-room/top-floor/patio mapping/access before travel.

### Kumaon / Kasar Devi / Almora
- **Turiya Niwas, Crank's Ridge — PROVISIONAL LOCK as sleep anchor; A as destination.**
- Correct property: Crank's Ridge, Kasar Devi, managed by Harshit Karki / booking registration Mayank Karki; NOT unrelated Lovedeep/Mall Road listing.
- Direct host confirmation already obtained: private whole house, hot water, room heating, electric blanket, sufficient blankets, year-round access, meal option via neighbour, cafes nearby, power/WiFi backup, taxi/train advice.
- Only open: exact dates, length, final reservation/direct vs Airbnb.
- Fallback #1 Kripal House; fallback #2 Rudra Himalayan Retreat.
- Lali's Organic Gift Shop & Stay = social hub, not sleep anchor.
- Canon: Nainital and Kasar Devi are NOT one base (~50 km/~2 h); Kumaon needs at least two, likely three bases. Kakrighat is a transit stop, not separate base.

### Varanasi
- **Sahi River View Guesthouse, Assi Ghat — LOCKED_BY_MARK (VNS-HOTEL-001).**
- Room preference: **balcony room**.
- Named contact: **Jitendre; give regards from Debby**.
- Do not replace without explicit Mark decision.
- This supersedes older `provisional` language in legacy CLUSTER_ANCHORS.

### Agra
- Max one night / positioning night if needed for Taj Mahal at sunrise/first practical opening. Do not expand Agra merely to fill time.

### Not yet locked in currently audited canon
- Vrindavan/Braj: sleep anchor still requires current decision/verification.
- Bodh Gaya: sleep anchor still requires current decision/verification.
- Tiruvannamalai/Arunachala: sleep anchor still requires current decision/verification.
- Prayagraj: no current locked sleep anchor identified in this audit.
- Haridwar/Kankhal/Rishikesh: only investigate stay if B-cluster survives route fit.

## CURRENT KUMAON DECISION GUARDRAIL
Known current/legacy decisions that MUST NOT be re-asked as new unless a true decision conflict appears include:
- Mahavatar Babaji Cave / Dunagiri landscape: A.
- Turiya Niwas: A.
- Bodh Ashram: A.
- Kainchi Dham: A.
- Bhumiadhar: A.
- Hotel Evelyn: A.
- Hanuman Garhi/Hanumangarh: A.
- Jageshwar: A (legacy protected; do not re-ask).
- Binsar: C (legacy protected; do not re-ask).
- Dhaulchina Anandamayi: C.
- K.K. Sah private family home: C / no normal visit.
- Ramsay Hospital: C absent shrine/visitor function.
- Patal Devi: C/reserve.
- Haidakhan main site: A; additional Haidakhan-lineage sites default C unless exceptional.

## CURRENT PROJECT-WIDE PRESENTATION RULES
- One physical parent complex = one decision number. Micro-sites stay nested.
- Final A-site/day guide must surface high-value microdetails BEFORE travel: rooms, caves, kuti, shrines, samadhi, cremation places, terraces, platforms, photo positions, etc.; who/what happened, access and confidence.
- Functional buildings still in ordinary use (school, hospital, town hall, office, ordinary private home) generally B/C unless active shrine/pilgrimage function or effectively free route add-on.
- Site ABC and cluster ABC are separate.
- Preserve breathing room; do not maximize site count.

## ANANDAMAYI MA TRAVEL SCOPE
Approx. three truly important Anandamayi destinations total, not exhaustive house-by-house pilgrimage.
- Kankhal Mahasamadhi: A.
- Vrindavan Ashram: A.
- Bhadaini Varanasi: selected A in later review; treat as core contender/third site and living major ashram.
- Dhaulchina C; Patal Devi C/reserve.
- Hard override: any physically resolvable documented joint Anandamayi Ma × Yogananda photo location inside an included cluster must be surfaced as MUST_VISIT_WITHIN_INCLUDED_CLUSTER.

## CURRENT ROUTE-PLANNING ORDER — MARK UPDATE 2026-08-23
The generic older pipeline placed stay selection after route/nights. For the current cluster-planning phase, Mark identified a necessary tactical refinement:

For a retained cluster where a meaningful/historic stay base is already known, use:
`KNOWN/CHOSEN SLEEP BASE -> A SITES -> DISTANCE/COMBINATION MATRIX -> LONELY PLANET ADDONS -> opportunistic B sites -> NIGHTS`.

Reason: LP distances and site combinations are meaningless if calculated from an arbitrary city center when Mark already intends to sleep at a specific historical/spiritual base.

This does NOT mean hotels determine spiritual A/B/C. It means known sleep anchors are used as routing origins before deciding local day structure and nights.

## LONELY PLANET LAYER
Independent of person layer and spiritual-anchor layer. Can include huge or tiny finds. Tiny is welcome when unusually special and low-cost (historic pastry shop, regional cult sweet, small rock-art shelter, short viewpoint walk). Do not use generic 'best in town' material.

Kumaon current LP decisions from Mark (2026-08-23 chat; durable ingest pending/this file records them):
- Corbett: C.
- Jageshwar: A but ALREADY protected A before LP sweep.
- Lakhudiyar: A only if naturally on route; otherwise C.
- Binsar: C and ALREADY protected C.
- Naina Peak: treat as A candidate/day-option; final decision can be made locally, no separate cluster-opening cost from Nainital base.
- Dwarahat temple groups: C as LP destination; may return only as near-zero-cost Babaji-route add-on.
- Sakley's historic Nainital pastry shop: A-style micro-extra / definitely surface when in Nainital.
- Kheem Singh Mohan Singh Rautela / Bal Mithai Almora: A-style micro-extra / definitely surface when in Almora.

## CALENDAR / FESTIVAL RISK LAYER
Before final itinerary: check Indian national + relevant state holidays; major religious festivals/pilgrimage events; weekly and exceptional closures; crowd/security/road/flight/train impact. Do not assume a holiday stops flights. Each travel day later gets SEEK_EVENT / OK_NORMAL / CROWD_CAUTION / TRANSPORT_CAUTION / AVOID_IF_POSSIBLE / HARD_CLOSURE.

## KNOWN STALE / DANGEROUS DOCUMENT TYPES
- Old CLUSTERS_OVERVIEW or candidates files may contain superseded ratings.
- Old CLUSTER_ANCHORS can contain a valid historical base but stale status (e.g. Varanasi provisional vs later LOCKED_BY_MARK).
- Legacy numbering must not be reused as current global permanent IDs, but legacy Mark ratings remain protected benchmarks unless explicitly superseded.
- Worker TASK/STATUS files are task-local and must not be mistaken for global travel truth.

## REQUIRED REGIE CHECK BEFORE NEXT CHOICE BLOCK
Before the regisseur presents another block of locations or Lonely-Planet findings:
1. identify current sleep anchor for that cluster (or explicitly state none is locked);
2. load current Mark decisions + protected legacy locks for that cluster;
3. mark all already-decided items in the working set;
4. only present true new decision surfaces;
5. calculate proximity from the actual chosen/provisional sleep base where available;
6. bundle micro-sites under parents;
7. preserve final-guide details for A sites.

## NEXT EXECUTION STEP
Build a current `SLEEP_BASE_REGISTER + CLUSTER_PRECEDENCE_MAP` for all retained A/B clusters from existing repo evidence before continuing LP scoring or route-night calculations. Do not ask Mark to repeat known decisions.
