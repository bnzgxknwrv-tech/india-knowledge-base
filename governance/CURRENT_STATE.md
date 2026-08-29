# CURRENT STATE — INDIA

state_revision: 2026-08-29_MAP_COORDINATE_VERIFICATION_HARDENED_CCI_COMPLETE
branch: `agent/india8-cluster-casting`
status: FIXED_CORE_DURATION_CLOSURE_ACTIVE
boot_authority: `governance/INDIA_MASTER_BOOT.md`
trip_frame: `governance/TRIP_FRAME_HARD.md`
current_decisions: `governance/CURRENT_DECISIONS_MASTER.md`
decision_ledger: `governance/DECISION_LEDGER.jsonl`
planning_service_standard: `governance/INDIA_HUMAN_CENTERED_COMPLEX_TRIP_PLANNING_STANDARD.md`
map_verification_rule: `governance/MAP_COORDINATE_VERIFICATION_RULE.md`
final_comfort_rule: `governance/FINAL_COMFORT_SWEEP_RULE_2026-08-23.md`

## LAST MATERIAL EVENT — MAP / COORDINATE DECISION-INTEGRITY HARDENING
Mark caught a dramatic user-facing map failure: the rendered pin for **Dungeshwari / Mahakala Caves — Siddhartha's ascetengrotten vóór de verlichting (Gaya district) [A+]** was wrong, which visually made **Brahmakund — heilige warmwaterbronnen in de verre Rajgir-cluster (Nalanda district) [A* / route-only]** appear to lie on the way. Because Mark uses maps and proximity to make A/B/C decisions, this is a decision-corrupting error class.

New hard governance:
- `governance/MAP_COORDINATE_VERIFICATION_RULE.md` is now ALWAYS-READ through `INDIA_MASTER_BOOT.md`;
- no decision-relevant map pin from a name-only/unverified geocoder result;
- resolve exact physical entity + authoritative identity/location where available + reliable coordinate/business ref/address + independent cross-check where practical + same-name disambiguation + geographic sanity check;
- unresolved coordinate = **NO PIN**, never a guessed pin;
- actual route/proximity conclusions require road/walk routing evidence, not visual map alignment;
- if Mark spots one map inconsistency, invalidate all map-derived conclusions from that rendering and reverify EVERY pin on the map;
- prefer no map over a plausible-looking wrong map.

Bodh cluster verified pin registry:
`runs/active/INDIA10-CLUSTER-COVERAGE-REAUDIT-001/BODHGAYA_VERIFIED_MAP_COORDINATES_2026-08-29.md`

Current verified map anchors include:
- Mahabodhi exact UNESCO property centre: `24.695280,84.993890`;
- Great Buddha exact object: `24.690468,84.981794`;
- Sujata Stupa exact object: `24.697920,85.003380`;
- Dungeshwari Cave Temple exact/cross-checked object: `24.736683,85.047584`;
- Rajgir Brahmakund exact locator `2C79+6C5`, recovered full code `7MQ72C79+6C5`, centre approximately `25.013013,85.418609`;
- Vishwa Shanti Stupa exact/cross-checked hilltop object: `25.004520,85.444530`;
- Maya Heritage: verified exact business identity/address; because secondary numeric pins conflict, use verified business entity/address rather than inventing a manual lat/lon.

Geographic sanity check: the verified Dungeshwari pin is only ~7.1 km straight from Mahabodhi and the official locality class is ~12 km north-east by road/local description. The verified Rajgir Brahmakund pin is ~48.4 km straight from Dungeshwari and therefore plainly NOT on the local Bodh Gaya -> Dungeshwari cave excursion.

## FINAL COMFORT / FOOD / HUMAN-TEXTURE HANDOFF — STILL HARD
Mark explicitly reminded INDIA that the end-stage comfort layer must survive successor handoff: when the real route/day is known, INDIA must tell him where, near the place he actually is, he can get genuinely good coffee, breakfast, lunch, dinner and other memorable/practical comfort stops.

Hardened state:
- `governance/FINAL_COMFORT_SWEEP_RULE_2026-08-23.md` anchors research to actual chosen hotel/ashram and actual day endpoints;
- mandatory categories include early breakfast, genuinely good coffee, lunch, dinner, historic/cult bakery/patisserie, local sweets/regional specialties, characterful café/tea, deliberately good restaurants and transfer-day comfort;
- each recommendation must show what to order, real distance/time, opening/daypart fit, reservation/access risk, detour cost and whether worth it;
- no generic top-10 restaurant dumps;
- volatile food/opening facts live-rechecked at final comfort stage;
- final day cards are not complete until the sweep exists for every retained base/relevant day corridor.

## SERVICE ARCHITECTURE UPGRADE — STILL CURRENT
Hard always-read standard:
`governance/INDIA_HUMAN_CENTERED_COMPLEX_TRIP_PLANNING_STANDARD.md`

Core service correction:
- Mark supplies subjective taste/meaning; INDIA supplies the decision environment.
- Before a burden-sensitive grade/choice, expose intrinsic value separately from marginal burden, robustness and confidence.
- Build pairwise proximity/microcluster matrices, not just hotel->site distances.
- Proactively state `je bent er toch` combinations and extra km/minutes.
- Compare WITH vs WITHOUT candidate and show NET marginal burden.
- State displacement/opportunity cost.
- Include opening/time-window/daypart/climate/daylight fit.
- Model human energy.
- Stress-test +30/+60 min and classify ROBUST / SENSITIVE / BRITTLE / OVERLOADED; name first sacrificial B/A*.
- Maintain VERIFIED / PROVISIONAL / DECISION-CRITICAL UNKNOWN / LIVE-RECHECK-LATER.
- Research priority follows value of information.
- Use rolling-wave detail, scenario deltas, reversibility/booking urgency, whole-trip cumulative burden and pre-mortems.

## BODH RECOVERY CONSEQUENCE
Current truth after the earlier burden correction remains:
- **Brahmakund — heilige warmwaterbronnen/badervaring in de verre Rajgir-cluster (Nalanda district) [A* / ONLY_IF_NATURAL_CORRIDOR_BYCATCH / SKIP_FIRST]**; no dedicated Rajgir excursion under current route.
- **Vishwa Shanti Stupa + Rajgir Ropeway — Peace Pagoda + kabelbaan in dezelfde verre Rajgir-cluster (Nalanda district) [B / ONLY_IF_RAJGIR_ALREADY_HAPPENS]**.
- the verified map now independently confirms these are a separate Rajgir microcluster, not on the local Dungeshwari cave excursion.

Canonical corrected artifacts:
- `runs/active/INDIA10-CLUSTER-COVERAGE-REAUDIT-001/BODHGAYA_OPEN_BATCH_MARK_DECISIONS_2026-08-28.md`
- `runs/active/INDIA10-CLUSTER-COVERAGE-REAUDIT-001/BODHGAYA_EXECUTION_GEOMETRY_2026-08-28.md`
- `runs/active/INDIA10-CLUSTER-COVERAGE-REAUDIT-001/BODHGAYA_VERIFIED_MAP_COORDINATES_2026-08-29.md`
- `runs/active/INDIA10-CLUSTER-COVERAGE-REAUDIT-001/A_PLUS_PROXIMITY_DECISION_MODEL.md`
- `governance/INDIA_BEHAVIORAL_EXECUTION_CONTRACT.md`
- `governance/MAP_COORDINATE_VERIFICATION_RULE.md`

## BODH STAY / HOTEL CURRENT
Mark selected **Maya Heritage — kleiner rustig middenklassehotel tegenover Wat Thai Buddhagaya, op praktische loopafstand van de Mahabodhi-tempelkern (Bodh Gaya) [HOTEL LOCKED_BY_MARK]**.

Bodh stay rhythm:
- arrival day must include a real **Mahabodhi Temple Complex + Bodhi Tree — verlichtingstempel + Bodhiboom waar Boeddha ontwaakte (Bodh Gaya) [A+] [UNESCO WH]** visit;
- next morning returns very early, nominally 05:00, with winter-darkness/first-light considered operationally;
- maximum 3 Bodh Gaya overnight stays;
- if inbound arrival is sufficiently early to create a genuinely usable first local day, preference is 2 overnight stays rather than 3.

Hotel practical Mahabodhi visitor-approach research: roughly 650–900 m / 9–13 min; use ~10–15 min conservative walk planning.

## CCI FULL-REPOSITORY HARVEST — COMPLETE / STILL RECONCILIATION EVIDENCE
Latest checked CCI head at 2026-08-29:
`b5349afe41f98eb4870728aaff2c633899afc1fa` — **checkpoint 19: HARVEST_COMPLETE**.

CCI reports:
- 4,192 manifest rows;
- 2,002 unique branch blobs;
- 89 recovered deleted blobs;
- 218 PR comments;
- 206 knowledge atoms;
- `100_PERCENT_SEMANTIC_COVERAGE = YES` in its task terminology;
- `SUCCESSOR_PARITY_TEST = PASS` after nine parity iterations;
- explicit bounded residual-risk statement rather than an absolute claim that no fact can ever be missed.

Useful outputs under `runs/active/CCI-FULL-REPO-KNOWLEDGE-HARVEST-001/` include:
- `SUCCESSOR_START_HERE.md`;
- `MARK_CURRENT_CANON_MASTER.md`;
- `PROJECT_PHILOSOPHY_AND_SELECTION_MODEL.md`;
- `CURRENT_TRAVEL_EXECUTION_CANON.md`;
- `OPEN_MARK_DECISIONS_ONLY.md`;
- `SUCCESSOR_EQUIVALENCE_ADDENDUM.md`;
- `KNOWLEDGE_ATOMS.jsonl`;
- `HARVEST_REPORT.md`.

CCI output is recovery/QA evidence and does not independently change Mark-only A+/A/A*/B/C or other subjective decisions.

## HARD TRIP FRAME
- Air India outbound: 18 Dec 2026 20:35 AMS -> DEL; arrival 19 Dec 10:15.
- Air India return: 21 Jan 2027 12:20 DEL -> AMS; arrival 18:35.
- 18 Dec night = aircraft, not Delhi hotel.
- 33 India accommodation / overnight-transport slots.
- 34-day planning-budget convention.
- no final exact calendar yet.

## SIX FIXED A+ WORLDS
1. DELHI
2. KUMAON
3. AGRA / TAJ MAHAL
4. BODH GAYA / GAYA
5. VARANASI / SARNATH
6. TIRUVANNAMALAI / ARUNACHALA

## DURATION_CLOSED
### KUMAON
- 9 occupied days / 9 nights through final Dunagiri night.
- includes Delhi -> Haidakhan occupied inbound day.
- Haidakhan Vishwa Mahadham/Ashram: 3 nights / 2 complete quiet days LOCKED_BY_MARK.
- eastern Kumaon exit = separate mandatory full-travel adjacent edge; charge once later.
- Hotel Evelyn active A+.
- Dunagiri Retreat = PRIMARY; Joshi Guest House, Kukuchina = FALLBACK_IF_DUNAGIRI_UNAVAILABLE.
- YSS Dwarahat A / FULL DAY; no YSS overnight.

### VARANASI / SARNATH
- 8 occupied days / 8 nights through final Varanasi night.
- includes Bodh Gaya/Gaya -> Varanasi arrival/wind-down day + 7 local days.
- outbound edge after final Varanasi night excluded.
- Sahi River View Guesthouse, Assi Ghat LOCKED_BY_MARK; balcony room; Jitendre; greetings from Debby.
- Manikarnika Ghat A+: final content block, no hard end.
- Bhrigu Karyalaya / Bhadury Sadan A+ LOCKED_BY_MARK; never on Manikarnika day.

## CURRENT FRONTIER — BODH GAYA / GAYA EXECUTION + DURATION CLOSURE
Mandatory sources:
- `runs/active/INDIA10-CLUSTER-COVERAGE-REAUDIT-001/BODHGAYA_PREP_PACKET_2026-08-27.md`
- `runs/active/INDIA10-CLUSTER-COVERAGE-REAUDIT-001/BODHGAYA_INDIA12_BOUNDED_CURRENT_CHECK_2026-08-27.md`
- `runs/active/INDIA10-CLUSTER-COVERAGE-REAUDIT-001/BODHGAYA_STRICT_LP_LAYER_GATE_2026-08-27.md`
- `runs/active/INDIA10-CLUSTER-COVERAGE-REAUDIT-001/INDIA12_RECOVERY_CANON_RECONCILIATION_2026-08-28.md`
- `runs/active/INDIA10-CLUSTER-COVERAGE-REAUDIT-001/BODHGAYA_OPEN_BATCH_MARK_DECISIONS_2026-08-28.md`
- `runs/active/INDIA10-CLUSTER-COVERAGE-REAUDIT-001/BODHGAYA_EXECUTION_GEOMETRY_2026-08-28.md`
- `runs/active/INDIA10-CLUSTER-COVERAGE-REAUDIT-001/BODHGAYA_VERIFIED_MAP_COORDINATES_2026-08-29.md`
- `runs/active/INDIAHOTEL-BODHGAYA-001/MARK_HOTEL_DECISION_2026-08-28.md`

Fixed current content:
- **Mahabodhi Temple Complex + Bodhi Tree — verlichtingstempel + Bodhiboom (Bodh Gaya) [A+] [UNESCO WH]**.
- **Sujata Stupa — melkrijst/Middenweg-plek (Bakraur) [A+]**.
- **Dungeshwari / Mahakala Caves — ascetengrotten vóór de verlichting (Bodh Gaya outer) [A+]**.
- **Great Buddha Statue — groot modern zittend Boeddhabeeld (Bodh Gaya) [A]**.
- **Brahmakund — heilige warmwaterbronnen/badervaring (Rajgir) [A* / ONLY_IF_NATURAL_CORRIDOR_BYCATCH / SKIP_FIRST]**; currently not in plan because current corridor does not naturally pass Rajgir.
- **Vishwa Shanti Stupa + Rajgir Ropeway — Peace Pagoda + kabelbaan (Rajgir) [B / ONLY_IF_RAJGIR_ALREADY_HAPPENS]**.
- **Archaeological Museum of Bodh Gaya — originele archeologische resten (Bodh Gaya) [B]**.
- **Tergar Monastery — Tibetaans/Kagyu-kloostercentrum (Bodh Gaya) [B]**.
- **Prachin Shree Jagannath Mandir — kleine levende hindoe-tempel bij de Mahabodhi-zone (Bodh Gaya) [B]**.
- **Gaya Tilkut — winterse lokale sesam-jaggeryzoetigheid (Gaya) [A* / SKIP_FIRST]**.
- Mangala Gauri Temple C; Nalanda/Patharkatti/Sher Shah Suri/Barabar-Nagarjuni and other current C excluded.
- Tutla Bhawani waterfall = winter-mismatch provenance, not Mark C.

Current proximity spine:
- hotel -> A+ sacred core ~0.65–0.9 km / ~10–15 min walk;
- hotel -> Archaeological Museum B ~0.4–0.6 km / ~5–10 min walk;
- hotel -> Great Buddha A ~0.7–1.0 km class / ~10–15 min walk;
- hotel -> Tergar B ~1.7 km / ~20–25 min walk or ~5–10 min auto;
- hotel/core -> Sujata A+ ~2–3 km road class / ~10–15 min vehicle until foot route confirmed;
- hotel/core -> Dungeshwari A+ ~12 km official locality class / ~30–40 min vehicle;
- Dungeshwari A+ -> Sujata A+ use ~30–40 min conservative connector pending live route closure.

Rebuilt duration default: **2 hotel nights if early inbound arrival around ~08:30–09:00 is achieved; maximum 3 per Mark if arrival is later or more sacred-core depth is desired.**

## CURRENT EAST-CORRIDOR STRUCTURE
Strongest provisional fixed-core order remains:
`AGRA -> [optional PRAYAGRAJ if it survives later fixed-core budget] -> BODH GAYA/GAYA -> VARANASI/SARNATH`.

If Prayagraj is omitted, current strongest inbound hypothesis is direct overnight rail Agra Fort -> Gaya (current timetable benchmark 18:45 -> 07:50), followed by road transfer to Maya Heritage. This creates an early-morning arrival and strongly supports Mark's 2-night preference.

If Prayagraj survives, it inserts before Bodh Gaya and changes the inbound edge/train/arrival hour.

Bodh Gaya -> Varanasi is a fixed eastern-world connection. Current evidence leaves private car and direct daytime rail both viable; no night train currently preferred/locked for this short edge.

## OPTIONAL WORLDS — DEFERRED
No optional-cluster ballot until all six fixed cores + real mandatory edges produce the fixed-core budget.
- Braj / Mathura–Vrindavan–Govardhan — NOT dropped; inclusion unresolved/deferred; fixed Vrindavan A anchors remain selected.
- Haridwar / Kankhal / Rishikesh.
- Prayagraj — especially relevant to Bodh inbound edge because it can insert directly before Bodh Gaya.

## HARD ROUTE / HUMAN GUARDS
- Ranchi + Kolkata/Hooghly/Serampore/Dakshineswar + Puri/Odisha skipped unless Mark reopens.
- exactly two intended true ashram sleeps: Haidakhan + Sri Ramanasramam if accepted/available.
- old V1/V2 route/date grids are provenance only.
- Kakrighat = A* / SKIP_FIRST.
- a question/hypothesis is never a Mark decision.
- only Mark changes A+/A/A*/B/C, personal hotel/base, subjective dwell/pace.
- action-first: if safe relevant work can be done now, do it; do not merely announce future research.
- map-integrity-first: before any user-facing India map, exact entity + verified coordinate/business ref/address + disambiguation + sanity check; unresolved = no pin.
- distance-first: before asking Mark to grade, show underlinge km/minuten and logical combinations; use conservative operational times.
- decision-support-first: show marginal burden, displacement, robustness and confidence separately from subjective content value.
- final-comfort-first-before-day-card: once route/calendar/day structure are stable, build actual-location-based food/coffee/comfort cards before calling final day cards complete.

## MEMORY / SUCCESSOR STATUS
Durable top-layer architecture now includes master boot + behavioral contract + Mark profile + naming/context protocol + **map/coordinate verification rule** + human-centered complex-trip planning standard + final comfort sweep rule + hard trip frame + current decisions master + append-only ledger + current state + recovery deltas + knowledge map.
CCI full-repository harvest is COMPLETE at checkpoint 19 and remains a semantic QA/recovery layer subject to current authority reconciliation.

## PR / WORKER RULE
- PR #23 is relay/provenance, not automatically current truth.
- Worker COMPLETE != central adoption.
- Check PR #23 at start of a major integration/build and immediately before a major central write.

## ACTIVE METHOD
`FIXED CORE CONTENT/CANON -> FULL RELEVANT SOURCE VISIBILITY -> EXECUTION GEOMETRY -> MARK PACE/DWELL -> DURATION_CLOSED x6 -> REAL INTER-CORE EDGES -> FIXED_CORE_34_DAY_BUDGET -> OPTIONAL WORLD SURVIVAL -> FINAL TOPOLOGY -> LIVE LOGISTICS -> EXACT CALENDAR -> FINAL COMFORT / FOOD / HUMAN-TEXTURE SWEEP -> FINAL DAY CARDS`.
