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

## EXE-029

Mahabodhi operational facts, current 2026 (Bihar Tourism page updated Aug 2026): UNESCO WH; listed hours 06:00-18:00; free entry; cameras and electronic gadgets PROHIBITED per the tourism page; Bodh Gaya local movement by auto/cycle-rickshaw, and the target sleep zone allows much on foot.

- **Class:** `CURRENT_FACT_WITH_RECHECK_TRIGGER`  |  **Integration state:** `ADOPTED`
- **Source:** a37423639f7dabb0dfd55c8656d4689bb8a25351:runs/active/INDIA10-CLUSTER-COVERAGE-REAUDIT-001/BODHGAYA_PREP_PACKET_2026-08-27.md
- **Note:** PARITY REPAIR (iteration 1). This item-level Mark grade is NOT present in any of the eight always-read central boot files; it lives only in a register the current boot demotes to a CONDITIONAL read. A successor booting the central layer alone would not see it.

## EXE-030

Bodh Gaya historical sleep/duration provenance — NOT a lock: the old V2 calculation used 3 Bodh Gaya nights with a hotel anchor in the Bodh Gaya temple core, preferably about 0.8 km walking distance from Mahabodhi / Thai Temple / Do Muhan Road side. The exact hotel is NOT locked by Mark, and Maya Heritage was at most a CALCULATION property, never a choice. Treat 3 nights only as an old comparison baseline — retained LP/traveler magnets may increase it.

- **Class:** `HISTORICAL_PROVENANCE_ONLY`  |  **Integration state:** `PROVENANCE_ONLY`
- **Source:** a37423639f7dabb0dfd55c8656d4689bb8a25351:runs/active/INDIA10-CLUSTER-COVERAGE-REAUDIT-001/BODHGAYA_PREP_PACKET_2026-08-27.md
- **Note:** PARITY REPAIR (iteration 1). This item-level Mark grade is NOT present in any of the eight always-read central boot files; it lives only in a register the current boot demotes to a CONDITIONAL read. A successor booting the central layer alone would not see it.

## EXE-031

The seven traditional post-enlightenment week-places inside the Mahabodhi complex (Animeshlochan Chaitya, Ratnachakrama, Ratnaghar Chaitya, Ajapala Nigrodh, Muchalinda pond, Rajyatana tree) are handled as SUBLOCATIONS of 046 Mahabodhi, deliberately NOT separately numbered — the umbrella decision was taken to avoid over-fragmentation. Muchalinda was formally classified MODERN_COMPLEX_REPRESENTATION_VS_HISTORICAL_SITE: Bihar Tourism confirms a Muchalinda Sarovar inside the complex while a separate Mocharim village lies about 1 km south; nothing was numbered independently.

- **Class:** `CURRENT_CANON`  |  **Integration state:** `ADOPTED`
- **Source:** commits a7a88d0c (2026-08-04), ad641131 (2026-08-05), d62f00f3 (2026-08-05)
- **Note:** PARITY REPAIR (iteration 1). This item-level Mark grade is NOT present in any of the eight always-read central boot files; it lives only in a register the current boot demotes to a CONDITIONAL read. A successor booting the central layer alone would not see it.

## EXE-032

PERMANENT IMMUTABLE NUMBER ALLOCATION 001-081, the only scheme that is current: Varanasi 001-045; Bodh Gaya / Gaya 046-078; Kumaon 079-081 (079 Mahavatar Babaji Cave, 080 Turiya Niwas, 081 Bodh Ashram). Accommodation IDs are SEPARATE and never share this space (VNS-HOTEL-001). Numbers are never reused, and an EXCLUDED candidate keeps its number reserved forever.

- **Class:** `CURRENT_CANON`  |  **Integration state:** `ADOPTED`
- **Source:** commits a7a88d0c, de9f5ca7, 9d91476a, 114ada55, a5a1b5be
- **Note:** PARITY REPAIR (iteration 1). This item-level Mark grade is NOT present in any of the eight always-read central boot files; it lives only in a register the current boot demotes to a CONDITIONAL read. A successor booting the central layer alone would not see it.

## EXE-033

COLLIDING NUMBERING SCHEMES — a successor WILL meet several incompatible ID spaces for the same places and must never reconcile them by number: (1) the CURRENT permanent immutable 001-081 plus VNS-HOTEL-001; (2) legacy CLUSTER_LOCATIONS.md 1-46 (an india1/india2 neutral inventory; its numbers 39-45 were deliberately RESERVED for Bodh Gaya candidates, so the gap is intentional, not a bug); (3) the DECISION-0013 cluster-block LOCATION_ID scheme — Delhi 100-199 RESERVED, Braj 200-299 (assigned 200-228), corridor/stations 300-399 (assigned 300-315), Kumaon 400-499 (assigned 400-443); (4) run-local temporary IDs: OLD31-01..31, KB2-001..045, KUM-CAND-001..047, KUM-SWEEP-A-001..008, BRJ-TMP-*, VNS-CAND-001..040, BGY-WATCH-*; (5) LC-* GEEL keys and IND-PLACE-000001..000008. The cluster-block scheme was NEVER actually applied for Kumaon (no LOCATION_ID was ever filled in PLACE-0001), so the assumption 'Babaji cave = LOCATION_ID 400' was an explicit, documented GUESS that was NOT adopted; the cave is 079.

- **Class:** `CURRENT_CANON`  |  **Integration state:** `ADOPTED`
- **Source:** commits 9d91476a (2026-08-14), 525ea75c (2026-07-11); branch-only KUMAON/BRAJ/CORRIDOR GOUD candidate files
- **Note:** This map exists nowhere as a single statement. Without it a successor can silently merge two different places or split one.

## EXE-034

PERSON-FREEZE CORPUS MAP — how much research already exists per person per independent detector, so no successor re-sweeps a saturated person. INDIAGEEL: Ramakrishna 55, Ramana 51, Neem Karoli Baba 46, Ram Dass 55, Vivekananda 9, Hariharananda 7 records. INDIAROOD: Babaji 50, Lahiri Mahasaya 40 (+6), Sri Yukteswar 42 (+14). PARALLEL-CHATGPT external sweep: Yogananda 127, Babaji 35, Lahiri 60, Sri Yukteswar 38, Neem Karoli Baba 113, Ram Dass 57, Ramana 103, Ramakrishna 175. Internal METHOD_V2 pre-external freezes: Babaji 14, Lahiri 19, Sri Yukteswar 7, Neem Karoli Baba 19-21, Ram Dass 5-13, Ramana 23, Ramakrishna 19. ONLY Lahiri (ChatGPT) and Ramakrishna (ChatGPT) ever claimed SATURATION: JA, and only for DISCOVERY saturation — never for physical-identity saturation.

- **Class:** `CURRENT_FACT_WITH_RECHECK_TRIGGER`  |  **Integration state:** `REVIEWED_NOT_ADOPTED`
- **Source:** branch-only TOP11-INDIAGEEL / TOP11-INDIAROOD / TOP11-PARALLEL-CHATGPT freeze files; commits 087-095 series
- **Note:** PARITY REPAIR (iteration 1). This item-level Mark grade is NOT present in any of the eight always-read central boot files; it lives only in a register the current boot demotes to a CONDITIONAL read. A successor booting the central layer alone would not see it.

## EXE-035

AOAY full-text atlas scale and its biggest open finding: the reproducible three-detector extraction over the complete Project Gutenberg #7452 text (48 chapters, sha256 recorded) produced 1,359 raw occurrence records normalising to 123 places. THIRTY places are AOAY_FOUND_BUT_MISSING_FROM_REPO, and the strongest single signal is a COMPLETE KASHMIR REGION CLUSTER spanning two full chapters (Simla/Srinagar/Shalimar/Nishat Bagh/Gulmarg) absent from every existing sweep — later confirmed to be Sri Yukteswar's own journey too ('I will accompany you to Kashmir', ch. 21), not only Yogananda's. Nineteen places independently confirm existing Top-11 atlas points from AOAY's own text. Status was honestly AOAY_LOCATION_SWEEP_SATURATED: NEE, with about 6,691 candidate token types left UNRESOLVED_BUT_RECORDED (sampled and found overwhelmingly to be personal names/titles, but not individually verified).

- **Class:** `CURRENT_FACT_WITH_RECHECK_TRIGGER`  |  **Integration state:** `REVIEWED_NOT_ADOPTED`
- **Source:** commits da27aba5 (2026-08-16), ea60ba59 (2026-08-19)
- **Note:** PARITY REPAIR (iteration 1). This item-level Mark grade is NOT present in any of the eight always-read central boot files; it lives only in a register the current boot demotes to a CONDITIONAL read. A successor booting the central layer alone would not see it. Kashmir is outside the current six fixed worlds, so this is not an action item — but it is the largest known unexplored AOAY finding and must not be rediscovered from scratch.

## EXE-036

MASTER LOCATION LIST — where the repository-wide person/place findings actually live: ALL_FINDINGS_LOCATION_MASTER, built row-level from six colour-worker family branches (BLAUW/ROOD/GEEL/WIT/TURQUOISE/ZILVER) at 459 rows and then closed out to 700 rows. The 459-row accounting equation closes as 459 = 259 physical-entity-linked (13 already matching canon 001-081/legacy IDs) + 0 explicit-duplicate + 33 negative/non-presence + 167 still-unresolved. MASTER_BUILD_EXCEPTIONS.md names 7 concrete irreducible gaps rather than silently dropping anything.

- **Class:** `CURRENT_FACT_WITH_RECHECK_TRIGGER`  |  **Integration state:** `ADOPTED`
- **Source:** commits d1fa886c (2026-08-20), 7baab306 (2026-08-20)
- **Note:** PARITY REPAIR (iteration 1). This item-level Mark grade is NOT present in any of the eight always-read central boot files; it lives only in a register the current boot demotes to a CONDITIONAL read. A successor booting the central layer alone would not see it.

## EXE-037

BRANCH-DELTA MAP — what actually sits on non-central branches, classified by INDIA9-006 into four categories over 867 blobs / 4,993,696 bytes: 62 UNIQUE_SEMANTIC_NOT_CENTRALLY_REPRESENTED, 40 SEMANTICALLY_REPRESENTED_IN_CENTRAL, 601 HISTORICAL_INTERMEDIATE_SUPERSEDED, 164 MECHANICAL_OR_REDUNDANT_SOURCE_ARTIFACT. The 62 unique-semantic blobs were packaged and read in seven volumes (344,876 bytes) and registered in governance/SEMANTIC_IMPORT_REGISTRY_2026-08-23.jsonl, with 50 archived as provenance.

- **Class:** `CURRENT_FACT_WITH_RECHECK_TRIGGER`  |  **Integration state:** `ADOPTED`
- **Source:** commits 1b7f7d78, 6f2bed99, de2da202 (2026-08-23)
- **Note:** PARITY REPAIR (iteration 1). This item-level Mark grade is NOT present in any of the eight always-read central boot files; it lives only in a register the current boot demotes to a CONDITIONAL read. A successor booting the central layer alone would not see it.

## EXE-038

Anandamayi Ma / Kankhal: the mahasamadhi shrine at Kankhal-Haridwar is very probably her single most important physical point in all India, and it was COMPLETELY ABSENT from the repository at the time of the person-centric pilot — not in Varanasi, Bodh Gaya or Kumaon. It is now graded A, but it sits in the DEFERRED Haridwar/Kankhal/Rishikesh optional world, and the corridor registry classifies it HEAVY_A_GATE_PASS_CANDIDATE_ROUTE_FAIL / MAJOR_OFF_CORRIDOR_DETOUR. If the optional-world ballot ever drops Haridwar, this is the single most significant content casualty and Mark should see that trade-off explicitly rather than losing it silently.

- **Class:** `CURRENT_FACT_WITH_RECHECK_TRIGGER`  |  **Integration state:** `ADOPTED`
- **Source:** commit 1f0eeaed (2026-08-15) megasweep pilot; branch-only VRINDAVAN-KUMAON-CORRIDOR-001/GOUD/central_map_source.jsonl
- **Note:** PARITY REPAIR (iteration 1). This item-level Mark grade is NOT present in any of the eight always-read central boot files; it lives only in a register the current boot demotes to a CONDITIONAL read. A successor booting the central layer alone would not see it. The trade-off framing is new in this harvest.

## EXE-039

GLOBAL TRANSFER LEDGER — the current safe transfer layer for fixed-core planning. Hard accounting rule: every used edge eventually includes, as applicable, packing/check-out/loading; road/station/airport access; check-in/security/platform wait; scheduled transport; winter/fog/traffic/delay buffer; baggage/exit; onward road to the sleeping base; check-in; food/rest/toilet; and remaining daylight/energy. NO exact calendar may use raw transport time as the whole occupied block. For cluster costing: charge the known INBOUND occupied edge to that cluster; include ALL internal base-change movement; keep the OUTBOUND edge visible and charge it exactly once when the next bridge is built.

- **Class:** `CURRENT_CANON`  |  **Integration state:** `ADOPTED`
- **Source:** a37423639f7dabb0dfd55c8656d4689bb8a25351:runs/active/INDIA10-CLUSTER-COVERAGE-REAUDIT-001/GLOBAL_TRANSFER_LEDGER_2026-08-25.md
- **Note:** PARITY REPAIR (iteration 2). Not present in any of the eight always-read central boot files.

## EXE-040

KUMAON current safe edges, with their working values and their explicit reliability status: K0 Delhi -> Haidakhan Vishwa Mahadham: about 337 km / 8-9 h raw road per Haidakhandi Samaj material — classified a FULL OCCUPIED TRAVEL DAY. Do NOT substitute an ambiguous Haidakhan pin or an Anandpuri/Ranikhet site. K2 Nainital -> Kainchi: about 17 km / 40-60 min raw; the Naini Lake A+ morning walk combines naturally before movement without a road detour. K3 Kainchi -> Dwarahat via the efficient direct spine Kainchi -> Khairna -> Ranikhet -> Dwarahat: about 71.7 km / about 2h24 raw, winter buffer required; the YSS Dwarahat FULL DAY promise may NOT hide this transfer inside it, and Kakrighat (A*/SKIP_FIRST) may be captured only if the transfer day stays comfortable. K6 hard internal order: HAIDAKHAN -> NAINITAL -> KAINCHI -> DWARAHAT -> DUNAGIRI/KUKUCHINA. Do NOT reverse Dwarahat/Dunagiri ahead of Nainital/Kainchi.

- **Class:** `CURRENT_FACT_WITH_RECHECK_TRIGGER`  |  **Integration state:** `ADOPTED`
- **Source:** a37423639f7dabb0dfd55c8656d4689bb8a25351:runs/active/INDIA10-CLUSTER-COVERAGE-REAUDIT-001/GLOBAL_TRANSFER_LEDGER_2026-08-25.md
- **Note:** PARITY REPAIR (iteration 2). Not present in any of the eight always-read central boot files.

## EXE-041

Inter-core edge policy: do NOT over-research all possible edges now — close only edges actually required by the fixed-core sequence, and later by surviving optional clusters. Haridwar/Rishikesh is optional and must NOT silently replace Delhi as Kumaon's predecessor during fixed-core costing. Optional worlds enter the ledger only after the six fixed cores are duration-closed and the fixed-core 34-day budget shows remaining capacity — no silent insertion. Controlling files, in order: governance/CURRENT_STATE.md; TRIP_PLANNING_META_CONTROLLER_2026-08-26.md; the transfer ledger; CLUSTER_TOPOLOGY_FEASIBILITY_2026-08-25.md for topology evidence subject to later overrides; then the current cluster execution files.

- **Class:** `CURRENT_CANON`  |  **Integration state:** `ADOPTED`
- **Source:** a37423639f7dabb0dfd55c8656d4689bb8a25351:runs/active/INDIA10-CLUSTER-COVERAGE-REAUDIT-001/GLOBAL_TRANSFER_LEDGER_2026-08-25.md
- **Note:** PARITY REPAIR (iteration 2). Not present in any of the eight always-read central boot files.

## EXE-042

CURRENT BEST GLOBAL TOPOLOGY SKELETON (no dates, subject to later override): DELHI -> optional HARIDWAR-RISHIKESH -> KUMAON (exact HAIDAKHAN VISHWA MAHADHAM -> NAINITAL -> KAINCHI -> DWARAHAT -> DUNAGIRI/KUKUCHINA) -> FULL TRAVEL DAY eastern-Kumaon exit toward plains -> optional BRAJ -> AGRA -> optional PRAYAGRAJ OR direct overnight AGRA->GAYA -> BODH GAYA/GAYA -> VARANASI/SARNATH -> primary direct VNS->CHENNAI hypothesis -> road CHENNAI -> TIRUVANNAMALAI/ARUNACHALA. SOUTHERN GATEWAY CORRECTION: current operating flight evidence confirms IndiGo 6E6044 runs direct Varanasi (VNS) -> Chennai (MAA), scheduled block roughly 2h15 on operating days; Chennai Airport -> Tiruvannamalai is about 171 km / ~2.5h raw road. FALLBACK if the Chennai flight is unavailable/badly timed on the actual date: direct VNS->BLR service -> Bengaluru Airport -> Tiruvannamalai (about 232 km / ~3.5h raw road). This corrects an earlier Bengaluru-first assumption; Chennai is now primary. Caveat: current operation does NOT prove the exact Dec 2026/Jan 2027 weekday timetable; recheck actual dates before calendar lock and booking.

- **Class:** `CURRENT_FACT_WITH_RECHECK_TRIGGER`  |  **Integration state:** `ADOPTED`
- **Source:** a37423639f7dabb0dfd55c8656d4689bb8a25351:runs/active/INDIA10-CLUSTER-COVERAGE-REAUDIT-001/CLUSTER_TOPOLOGY_FEASIBILITY_2026-08-25.md sections 6-7
- **Note:** PARITY REPAIR (iteration 3). The current controlling route-topology hypothesis including the exact southbound gateway flight; not present in any of the eight always-read central boot files, nor previously anywhere in this harvest's atom set.

## EXE-043

Two corridor facts materially affect optional-world sequencing and must not be silently omitted. (1) EASTERN KUMAON EXIT working figures: HOTEL Dunagiri Retreat states Delhi is about 400 km / about 9-10h road, and Pantnagar Airport is roughly 160 km / about 5h road from the retreat; public route engines produce shorter raw figures, which is exactly why the local mountain-sourced estimate must control conservative calendar planning rather than a generic routing-API number. Direct road toward the Agra/plains corridor is geographically possible; a forced return to Delhi is NOT inherently required. This is the K7 edge named in OPN-011, now with its actual working distances. (2) AGRA -> GAYA DIRECT OVERNIGHT bypasses the need for Prayagraj as a routing bridge: train 12988 Ajmer-Sealdah SF Express runs daily through Agra Fort and Gaya, current timetable Agra Fort ~18:45 -> Gaya ~07:50, about 13h05 overnight. Prayagraj therefore must survive on its own spiritual/travel value, not because route engineering needs it as a bridge.

- **Class:** `CURRENT_FACT_WITH_RECHECK_TRIGGER`  |  **Integration state:** `ADOPTED`
- **Source:** a37423639f7dabb0dfd55c8656d4689bb8a25351:runs/active/INDIA10-CLUSTER-COVERAGE-REAUDIT-001/CLUSTER_TOPOLOGY_FEASIBILITY_2026-08-25.md section 2.4 and section 5
- **Note:** PARITY REPAIR (iteration 3). OPN-011 named the K7 edge as P0 work without these actual working distances; no atom previously recorded the Agra->Gaya direct-overnight alternative to Prayagraj.

## EXE-044

OPTIONAL-WORLD LOGISTICS-TAX comparison (quantified, not a quality judgment; content value is separate and unaffected), ranked cheapest to most burdensome current insertion: (1) BRAJ / Mathura-Vrindavan-Govardhan — LOW geometric tax: Agra -> Mathura roughly 57 km / about 1h raw road; Agra -> Vrindavan roughly 66-70 km / about 1-2h raw road. (2) PRAYAGRAJ — LOW_TO_MODERATE / corridor-compatible: Agra -> Prayagraj roughly 6-7h rail/road, Prayagraj -> Varanasi roughly 2-3h; NOT route-required because a direct Agra->Gaya overnight exists (EXE-043). (3) HARIDWAR-RISHIKESH/KANKHAL — MATERIAL / the biggest current optional northern insert, but NOT route-breaking if inserted exactly once BEFORE Kumaon: correct topology is DELHI -> HARIDWAR/RISHIKESH -> KUMAON, never inserted after the eastern Kumaon end, which would force a long westward bounce. Working movement classes: Delhi -> Rishikesh ~218 km, raw ~3h23 but practical planning ~5h+; Rishikesh -> Nainital ~236-253 km / practical ~5.5-7h; Rishikesh -> Dwarahat ~271-275 km / ~8h (proof against inserting after eastern Kumaon); Rishikesh -> a Haidakhan-labelled destination ~266 km / ~4h50 raw but LOWER entity confidence than EXE-040's official Haidakhan access evidence, so must not be calendar-locked. Net effect: converts one already-large northern approach into TWO substantial road legs plus one base change. (4) MYSORE/BENGALURU sightseeing extension — HIGH / do not assume inclusion: Tiruvannamalai -> Bengaluru ~203 km / ~3h raw road; using Bengaluru as a fallback AIR GATEWAY (EXE-042) does not make Mysore/Bengaluru SIGHTSEEING free — two separate questions.

- **Class:** `CURRENT_FACT_WITH_RECHECK_TRIGGER`  |  **Integration state:** `ADOPTED`
- **Source:** a37423639f7dabb0dfd55c8656d4689bb8a25351:runs/active/INDIA10-CLUSTER-COVERAGE-REAUDIT-001/CLUSTER_TOPOLOGY_QUANTIFIED_DELTA_2026-08-26.md
- **Note:** PARITY REPAIR (iteration 3). MRK-040/EXE-003 record the deferred-worlds list qualitatively, but none of these quantified figures or the Mysore/Bengaluru gateway-vs-sightseeing distinction existed anywhere in the successor layer before this repair.

## EXE-045

Varanasi day-sequencing preferences (2026-08-27, current): Day 1 in Varanasi should preferably connect immediately to Lahiri Mahasaya / Kriya with Assi Ghat/Ganges orientation, rather than a hotel-only inactive arrival; Manikarnika Ghat / the cremation world may be deliberately placed LATER in the stay so Mark can acclimatize first, not necessarily on day 1. These sit alongside the general pacing rule in `MRK-029` and refine it specifically for Varanasi's emotional sequencing, not just its physical geometry.

- **Class:** `CURRENT_CANON`  |  **Integration state:** `REVIEWED_NOT_ADOPTED`
- **Source:** a37423639f7dabb0dfd55c8656d4689bb8a25351:runs/active/INDIA10-CLUSTER-COVERAGE-REAUDIT-001/VARANASI_HISTORICAL_PACE_PREFERENCE_RECOVERY_2026-08-27.md
- **Note:** PARITY REPAIR (iteration 7). A small day-1/emotional-sequencing preference not covered by MRK-029 or EXE-019.

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
