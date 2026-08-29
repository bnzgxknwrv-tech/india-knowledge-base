# Current Travel Execution Canon

> Provenance note. This file was produced by the repository-wide knowledge harvest
> `CCI-FULL-REPO-KNOWLEDGE-HARVEST-001` on worker branch `agent/cci-full-repo-knowledge-harvest`,
> frozen against central commit `a37423639f7dabb0dfd55c8656d4689bb8a25351`.
> It is **archaeology and reconciliation**, not new decision-making. No Mark A/B/C grade, hotel or
> sleepbase lock, route lock or dwell decision was created, changed or inferred here.
> Every statement below carries its exact source so a successor can re-verify it independently.
> Where a statement contradicts a newer explicit Mark decision, **the newer Mark decision wins**.

The execution layer: planning sequence, current phase, route geometry, coordinates, access facts
and day-block structure. This is what a successor needs when it stops deciding *what* and starts
building *how*.

The coordinate material here is the single largest recovery in this harvest. The central branch
currently ships a Varanasi map whose pins are, for 34 of 40 candidates, older and less well
supported than points that exist in a **deleted** audit file. `EXE-009`, `EXE-010` and `EXE-011`
state that situation precisely.

---

## EXE-001

Active planning sequence (TRIP_PLANNING_META_CONTROLLER): FIXED CORE CONTENT/CANON -> FULL RELEVANT SOURCE VISIBILITY -> EXECUTION GEOMETRY -> MARK PACE/DWELL -> DURATION_CLOSED x6 -> REAL INTER-CORE EDGES -> FIXED_CORE_34_DAY_BUDGET -> OPTIONAL WORLD SURVIVAL -> FINAL TOPOLOGY -> LIVE LOGISTICS -> EXACT CALENDAR -> FINAL COMFORT SWEEP / DAY CARDS. No optional-world ballot and no exact final calendar before the fixed-core gates close.

- **Class:** `CURRENT_CANON`  |  **Integration state:** `ADOPTED`
- **Source:** a37423639f7dabb0dfd55c8656d4689bb8a25351:governance/INDIA_MASTER_BOOT.md §8

## EXE-002

Current phase: FIXED_CORE_DURATION_CLOSURE_ACTIVE. Two of six cores are DURATION_CLOSED (Kumaon 9/9, Varanasi 8/8). Bodh Gaya/Gaya is the live frontier. Tiruvannamalai, Delhi and Agra have prepared packets but are not duration-closed.

- **Class:** `CURRENT_CANON`  |  **Integration state:** `ADOPTED`
- **Source:** a37423639f7dabb0dfd55c8656d4689bb8a25351:governance/CURRENT_STATE.md

## EXE-003

Route geometry currently held: Bodh Gaya/Gaya + Varanasi form a natural eastern pair. The current south-gateway hypothesis may use Varanasi -> Chennai air plus road to Tiruvannamalai, but live service/date facts are rechecked only at the actual topology/calendar stage. If Rishikesh survives the optional budget it belongs BEFORE Kumaon. Braj has low geometric tax near Delhi/Agra. Prayagraj is corridor-compatible but not required.

- **Class:** `CURRENT_CANON`  |  **Integration state:** `ADOPTED`
- **Source:** a37423639f7dabb0dfd55c8656d4689bb8a25351:governance/CURRENT_DECISIONS_MASTER.md §14

## EXE-004

Old V1/V2 exact calendars and route grids are PROVENANCE_ONLY. They were superseded because travel occupancy had been UNDERCOUNTED. Useful old closure/festival/service facts may be rechecked later, but old dates never drive the route.

- **Class:** `SUPERSEDED`  |  **Integration state:** `PROVENANCE_ONLY`
- **Source:** a37423639f7dabb0dfd55c8656d4689bb8a25351:governance/INDIA_RECOVERY_DELTAS_CURRENT.md R05

## EXE-005

Recovered corridor/station geo nodes (LOCATION_ID 300-315) with coordinates: Mathura Jn 27.4924/77.6737; Kathgodam 29.2693/79.546; Lal Kuan 29.0665/79.5195; Haldwani 29.2183/79.5127; plus the remainder of the 52-row corridor map. Includes a `detour_class` vocabulary. Anandamayi Ma Samadhi Kankhal is classified HEAVY_A_GATE_PASS_CANDIDATE_ROUTE_FAIL / MAJOR_OFF_CORRIDOR_DETOUR.

- **Class:** `CURRENT_FACT_WITH_RECHECK_TRIGGER`  |  **Integration state:** `REVIEWED_NOT_ADOPTED`
- **Source:** branch-only runs/active/VRINDAVAN-KUMAON-CORRIDOR-001/GOUD/central_map_source.jsonl, blob 8551908d8519

## EXE-006

Recovered cross-cluster A/B coordinate registry (30 rows WITH coordinates), including: Lahiri Mahasaya Samadhi 25.3028/83.0074; Lahiri original home 25.3018/83.0068; Manikarnika 25.3109/83.0142; Tailanga Swami Math 25.3188/83.013; Anandamayi Bhadaini 25.2897/83.0068; Sarnath 25.3811/83.0214; Kashi Vishwanath 25.3109/83.0107; Mahabodhi 24.695/84.9914; Taj Mahal 27.1751/78.0421; Babaji Cave 29.8334/79.4654.

- **Class:** `CURRENT_FACT_WITH_RECHECK_TRIGGER`  |  **Integration state:** `REVIEWED_NOT_ADOPTED`
- **Source:** branch-only runs/active/VARANASI-COMPLETE-001/GOUD/MASTER_A_B_GEO_REGISTRY_VERIFIED.jsonl, blob da7be7eb5257

## EXE-007

Recovered legacy Kumaon LOCATION_ID table (400-443 plus station nodes 308-310) with formal_status. A rows: 400 Babaji Cave, 401 Babaji Smriti Bhavan, 402 Dunagiri Temple, 403 YSS Dwarahat, 404 Kainchi Dham, 405 Kasar Devi, 406 Crank's Ridge, 407 Kakrighat, 408 Jageshwar, 409 Hanuman Garhi, 412 Bhumiyadhar, 413 Ramakrishna Kutir, 414 Chitai Golu Devta, 420 Turiya Niwas, 421 Bodh Ashram, 423 Haidakhan Vishwa Mahadham. B: 424 Ghorakhal Golu Devta. C: 415 Mirtola, 416 Binsar, 417 Patal Bhuvaneshwar, 422 Dhaulchina. The GRADES here are legacy and superseded by Mark's current grading; the ID-to-place MAPPING remains useful.

- **Class:** `HISTORICAL_PROVENANCE_ONLY`  |  **Integration state:** `REVIEWED_NOT_ADOPTED`
- **Source:** branch-only runs/active/KUMAON-COMPLETE-001/GOUD/candidates.jsonl, blob 28ec04c9cea0

## EXE-008

Recovered Braj table: LOCATION_ID 200-228, of which ONLY 200 (Katyayani Peeth) and 201 (NKB Vrindavan Ashram) carry formal_status_preserved = A; all others are U. IND-PLACE-000001..000008 map to 200-207.

- **Class:** `HISTORICAL_PROVENANCE_ONLY`  |  **Integration state:** `REVIEWED_NOT_ADOPTED`
- **Source:** branch-only runs/active/BRAJ-COMPLETE-001/GOUD/place_candidates.jsonl, blob 4b0de93ac9c8

## EXE-009

Varanasi delivered map state: the central DATASET_VARANASI_40.jsonl has final_latitude NULL for 35 of 40 candidates (geo_status GOOGLE_MAPS_MARKER_NOT_CONFIRMED), and the delivered KML falls back to OLD inherited pins labelled [ONBEVESTIGD]. VNS-CAND-008 carries NO point at all ([GEEN PUNT -- AFGEWEZEN COORDINAAT UITGESLOTEN]). Only 5 of 40 have a final coordinate: 3 VERIFIED_OFFICIAL_MAP_LINK + 2 EXACT_GOOGLE_MAPS_MARKER.

- **Class:** `CURRENT_CANON`  |  **Integration state:** `ADOPTED`
- **Source:** a37423639f7dabb0dfd55c8656d4689bb8a25351:runs/active/VARANASI-GEO-DELIVERY-REPAIR-001/GOUD/REGIONAL/DATASET_VARANASI_40.jsonl and USER/VARANASI_40_KANDIDATEN.kml

## EXE-010

RECOVERED and materially better: a deleted BRONS GEO audit supplies independently cross-checked working points for VNS-CAND-002 .. VNS-CAND-035 with per-candidate geo_status, point_type, nearby-anchor checks and an explicit residual-uncertainty sentence each. Notable divergences from the central [ONBEVESTIGD] fallback pins: VNS-CAND-008 Yogoda Satsanga Dhyana Mandali gets 25.303204/82.976039 APPROXIMATE_LOCAL_POINT ~250 m (central has NO point); VNS-CAND-013 Kaal Bhairav 25.3176834/83.010746 vs central 25.3223/83.009 (~520 m, with the warning that multiple same-name temples exist and the Visheshwarganj shrine is the intended one); VNS-CAND-023 Mrityunjay 25.3221891/83.0147241 vs 25.3291/83.0056 (~1.1 km); VNS-CAND-025 Lahartara 25.31467/82.96838 vs 25.304/82.966 (~1.2 km); VNS-CAND-034 Saranganath 25.375/83.0283 vs 25.3833/83.0225 (~1.0 km, explicitly a ~400 m locality point that must NOT be treated as the temple entrance).

- **Class:** `CURRENT_FACT_WITH_RECHECK_TRIGGER`  |  **Integration state:** `RECEIVED_UNREVIEWED`
- **Source:** recovered DELETED research/active/VARANASI-GEO-DELIVERY-REPAIR-001/BRONS/GEO_AUDIT.jsonl (36 rows) + SOURCES.jsonl (86 rows, BRGEO-S001..S085)
- **Note:** Working points, NOT surveyed points. Central currently ships worse pins for these candidates.

## EXE-011

VNS-CAND-001 (Lahiri Mahasaya Samadhi / Satyalok) is NOT_ESTABLISHED / UNRESOLVED_IDENTITY_SPLIT: the candidate label conflates two distinct public records (the 'Lahiri Mahasaya Samadhi' listing and the 'Satyalok' temple listing) and must be SPLIT or clarified before a single endpoint is chosen. The inherited 25.3028/83.0074 was explicitly NOT retained by that audit. Central keeps the label unsplit and still uses that pin in the delivered KML.

- **Class:** `CONFLICT_NEEDS_RECONCILIATION`  |  **Integration state:** `RECEIVED_UNREVIEWED`
- **Source:** recovered DELETED VARANASI-GEO-DELIVERY-REPAIR-001/BRONS/GEO_AUDIT.jsonl vs central DATASET_VARANASI_40.jsonl

## EXE-012

GEO_CONFLICT: the NKB Vrindavan Ashram coordinate differs between two branch-only registries — 27.5674/77.69215 (corridor central_map_source.jsonl) vs 27.5767/77.6865 (Varanasi MASTER_A_B_GEO_REGISTRY_VERIFIED.jsonl), about 1.1 km apart. Neither is reconciled in central.

- **Class:** `CONFLICT_NEEDS_RECONCILIATION`  |  **Integration state:** `RECEIVED_UNREVIEWED`
- **Source:** blobs 8551908d8519 and da7be7eb5257

## EXE-013

Known earlier GEO_CONFLICT still on record: Madan Mohan Temple and Banke Bihari Temple returned IDENTICAL lat/lon from search — flagged GEO_CONFLICT and deliberately not used.

- **Class:** `CONFLICT_NEEDS_RECONCILIATION`  |  **Integration state:** `ADOPTED`
- **Source:** commit 3f2280ef (2026-08-23) Task A

## EXE-014

Rejected-as-unreliable coordinate precedent: two Google Earth entity links (Manikarnika Ghat, Dashashwamedh Ghat) were EXPLICITLY REJECTED because a generic search term ('Ghat') returned an IDENTICAL coordinate for two ghats 500-800 m apart — treated as a generic riverbank fallback, not a specific marker.

- **Class:** `CURRENT_CANON`  |  **Integration state:** `ADOPTED`
- **Source:** commit a15665fc (2026-08-02) ZILVER-Z01

## EXE-015

Bodh Gaya confirmed coordinates from direct Google Maps/Earth entity queries (structured API response, not aggregator estimate): 046 Mahabodhi Temple Complex 24.6959222 N / 84.9914193 E CONFIRMED; 047 Sujata Stupa 24.6979887 N / 85.0033228 E CONFIRMED (Plus Code M2X3+58W), which resolved a prior three-way coordinate conflict. 048 Dungeshwari and 049 Great Buddha Statue remain GOOGLE_MAPS_MARKER_NOT_CONFIRMED — no estimate was adopted.

- **Class:** `CURRENT_FACT_WITH_RECHECK_TRIGGER`  |  **Integration state:** `ADOPTED`
- **Source:** commit d597d6c5 (2026-08-04) Bodh Gaya ZILVER

## EXE-016

Delivered geo ledger (74 rows) from the retained-route QA: 10 EXACT_GOOGLE_MAPS_MARKER (Kainchi Dham, Har Ki Pauri, Triveni Sangam, Sri Ramanasramam, Arunachaleswarar Temple, Taj Mahal, Banke Bihari Temple, plus Mahabodhi/Sujata Stupa reused from ZILVER-verified canon), 12 ADDRESS_CONFIRMED_MARKER_NOT_CLOSED, 1 GEO_CONFLICT, 51 ZONE_ONLY — honestly marked as not independently closed rather than fabricated.

- **Class:** `CURRENT_FACT_WITH_RECHECK_TRIGGER`  |  **Integration state:** `ADOPTED`
- **Source:** commit 3f2280ef (2026-08-23) Task B

## EXE-017

Corridor fact: Gaya Airport to Mahabodhi Temple is 10.6 km via NH22 + Domuhan-Bodhgaya Road per gaya.nic.in, corroborated by multiple travel sources. The specific attribution 'AAI says 10 km' could NOT be independently confirmed (both AAI and gaya.nic.in returned 503 on direct fetch); a 5-17 km band is retained rather than a hard figure. Gaya Airport only became internationally operational for Buddhist pilgrims on 13 November 2002.

- **Class:** `CURRENT_FACT_WITH_RECHECK_TRIGGER`  |  **Integration state:** `ADOPTED`
- **Source:** commits 916b20ed, fddf5515 (2026-08-09/14)

## EXE-018

Bodh Gaya GEO cluster symmetry (poort L.1 applied): core cluster 046<->047 mutual; 'Bij Mahabodhi' cluster = 046, 049, 050, 061, 062, 068, 073, 074 now symmetric; Gaya-city cluster = 051, 070, 071, 078 fully 4-way symmetric; 060<->049 (Great Buddha Statue zone) symmetric; 048 explicitly 'no combination' (own ride, different zone); 052, 058, 063, 072, 077 explicitly 'combineerbaarheid niet betrouwbaar vast te stellen na GEO-controle'.

- **Class:** `CURRENT_CANON`  |  **Integration state:** `ADOPTED`
- **Source:** commit c4dcda24 (2026-08-08)

## EXE-019

Varanasi day-block geometry as delivered in the KML: Dagblok A Bhadaini/Assi (walkable from the hotel base); Dagblok B old city / ghats northward (boat + walk); Dagblok C Kriya/Bengali Tola, Kabir, northern old city (taxi-based); Dagblok D Sarnath (separate day trip). Each route line starts and ends at the hotel base.

- **Class:** `CURRENT_CANON`  |  **Integration state:** `ADOPTED`
- **Source:** a37423639f7dabb0dfd55c8656d4689bb8a25351:runs/active/VARANASI-GEO-DELIVERY-REPAIR-001/GOUD/REGIONAL/USER/VARANASI_40_KANDIDATEN.kml; commit 30c9a51c (2026-08-02) TRAVEL module

## EXE-020

Varanasi practical layer already produced: DAGROUTES.md (four day blocks + 2/3/4-day combinations), AARTI_EN_BOOT.md (Ganga Aarti Dashashwamedh evening, Subah-e-Banaras Assi Ghat morning, sunrise/evening boat trips), PRAKTISCHE_TIPS.md (weather/clothing, ghats/river incl. cremation-site etiquette, transport, money, health, respect/behaviour), RESTAURANTS.md around Assi Ghat.

- **Class:** `CURRENT_CANON`  |  **Integration state:** `ADOPTED`
- **Source:** commit 30c9a51c (2026-08-02)

## EXE-021

Live-fact boundary: do NOT globally revalidate volatile facts every boot. Recheck only when they influence real advice/calendar/booking — visa; trains/1A/2A; domestic flights; hotels/ashram acceptance; opening/access; weather/winter safety; prices/availability.

- **Class:** `CURRENT_CANON`  |  **Integration state:** `ADOPTED`
- **Source:** a37423639f7dabb0dfd55c8656d4689bb8a25351:governance/INDIA_MASTER_BOOT.md §11

## EXE-022

Kumaon non-merge rules that must survive: Bhumiadhar (Neem Karoli Baba) and Bhumiya Dhara (Anandamayi Ma) are DIFFERENT places and must NOT be merged on name similarity. Legacy confirms Bhumiyadhar specifically as the Ram Dass / Maharaj-ji FIRST MEETING site (DECISION-0002, verified via Be Love Now and Being Ram Dass — on/at the temple grounds, not inside the temple), distinct from Kainchi Dham itself, which was the later residence.

- **Class:** `CURRENT_CANON`  |  **Integration state:** `ADOPTED`
- **Source:** commits 51aa645c (2026-07-11), 9d91476a (2026-08-14); runs/active/KUMAON-V2-RESWEEP-001/INDIA_SWEEP_B.md

## EXE-023

Source warning that must survive: Incredible India WRONGLY claims a Neem Karoli Baba samadhi at Kainchi. Do not propagate.

- **Class:** `CURRENT_CANON`  |  **Integration state:** `REVIEWED_NOT_ADOPTED`
- **Source:** runs/active/KUMAON-V2-RESWEEP-001/INDIA_SWEEP_B.md (branch-only)

## EXE-024

Vivekananda's 17-point Almora circuit exists as a recorded research layer in the blind Kumaon Sweep B, alongside 45 KB2-* temporary candidates. Mayavati Advaita Ashrama = KB2-038, confirmed FOUND_AND_ALREADY_KNOWN. The Almora lecture stop was flagged as a possible Kumaon REGION_MISS for a later follow-up.

- **Class:** `HISTORICAL_PROVENANCE_ONLY`  |  **Integration state:** `REVIEWED_NOT_ADOPTED`
- **Source:** runs/active/KUMAON-V2-RESWEEP-001/INDIA_SWEEP_B.md; commit 5b2be9fe (2026-08-16)

## EXE-025

Bodh Gaya identity resolutions that must not be re-litigated: Daijokyo Buddhist Temple (owner of 049) and Japanese Temple / Indosan Nippon are DIFFERENT_LOCATIONS, not aliases — separate founders (Nichidatsu Fujii / Nipponzan-Myohoji peace-pagoda movement, 1972 vs Tatsuko Sugiyama / Daijokyo, opened 13 Feb 1983). 063 Padmasambhava Grand Temple and 068 Shechen ('Shechen Tennyi Dargyeling') are also DIFFERENT_LOCATIONS, confirmed via tibet.net.

- **Class:** `CURRENT_CANON`  |  **Integration state:** `ADOPTED`
- **Source:** commits a790acbf (2026-08-04), 9cab2431 (2026-08-08)

## EXE-026

Bodh Gaya access facts: 051 Vishnupad Temple — multiple independent travel sources consistently report non-Hindus may not enter the temple itself (no official source confirms or denies). 071 Pretshila — no non-Hindu restriction found, in contrast to 051. 076 Akshayavat grows INSIDE the Vishnupad courtyard (051) and probably shares its restriction. 073 Jagannath Temple Bodh Gaya — non-Hindu access verified specifically for THIS temple via the official Bihar Tourism page (no restriction listed); NOT inferred from Puri. 053 Root Institute — free day visits to the gardens, daily meditation sessions open to all, and ordinary stays without a course are possible. 074 Dhamma Bodhi — residential courses ONLY, no day visit.

- **Class:** `CURRENT_FACT_WITH_RECHECK_TRIGGER`  |  **Integration state:** `ADOPTED`
- **Source:** commits e52b7a9c, 54b8ba9d, 9cab2431 (2026-08-07/08)

## EXE-027

Bodh Gaya event-date honesty: the Kagyu Monlam at 052 Tergar follows the TIBETAN LUNAR CALENDAR — 'usually January-February' was too firm. Last confirmed edition: 40th Kagyu Monlam Chenmo, 23 Dec 2025 - 3 Jan 2026. The next edition's dates are UNKNOWN and stated as such rather than estimated.

- **Class:** `CURRENT_FACT_WITH_RECHECK_TRIGGER`  |  **Integration state:** `ADOPTED`
- **Source:** commit e52b7a9c (2026-08-07)

## EXE-028

Rajgir ropeway current operating reality and the ARIES (Nainital) public-visit facts were corrected/hardened into their respective A+ slices; Taj full-moon calendar window is closed in the Agra A+ slice; Tiruvannamalai slice hardened with verified calendar and ashram rules; a fixed-date collision matrix was precomputed before A+ selection.

- **Class:** `CURRENT_FACT_WITH_RECHECK_TRIGGER`  |  **Integration state:** `ADOPTED`
- **Source:** commits "INDIA10: correct Rajgir ropeway current operating reality", "...harden Kumaon A+ slice with current ARIES public-visit facts", "...close Taj full-moon calendar window", "...harden Tiruvannamalai A+ slice", "...precompute fixed-date collision matrix"

---

### Coordinate trust ladder used throughout

Strongest to weakest: `EXACT_GOOGLE_MAPS_MARKER` / `VERIFIED_OFFICIAL_MAP_LINK` /
`VERIFIED_SITE_CENTRE` (structured entity response, identity matched) ->
`WORKING_CROSSCHECKED_MAP_POINT` (two or more independent public records agree) ->
`ADDRESS_CONFIRMED_MARKER_NOT_CLOSED` -> `APPROXIMATE_LOCAL_POINT` (locality-level, radius stated)
-> `ZONE_ONLY` -> `NOT_ESTABLISHED` / `GOOGLE_MAPS_MARKER_NOT_CONFIRMED`. `GEO_CONFLICT` is a
separate flag, not a rung. A point is never promoted by reuse, and a coordinate is never invented
to fill a gap — `EXE-014` is the standing precedent for rejecting a plausible-looking but generic
coordinate.
