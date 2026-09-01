# INDIA CURRENT KNOWLEDGE MAP — WAT MOET JE LEZEN / WAT IS OUD

Status: **CURRENT LIVING SOURCE MAP — V8 / MANIFEST-DRIVEN + FRESH-SESSION-BOOT-PROOF + CCI-PARITY-SYNCHRONIZED**
Updated: 2026-09-01
Branch: `agent/india8-cluster-casting`
Canonical manifest: **`governance/BOOT_MANIFEST_V8.json`** — the single machine-readable authority for exactly which files/counts are mandatory. This map explains ROUTING and WHY; it does not define a competing mandatory set. If a count or file list below ever disagrees with the manifest, the manifest wins and this map must be corrected in the same change.
Boot owner: `governance/INDIA_MASTER_BOOT.md` V8
Decision-ledger migration: **DECISION_LEDGER_BACKFILL_COMPLETE**
CCI parity source: immutable completed harvest `b5349afe41f98eb4870728aaff2c633899afc1fa`
Detailed current predecessor handoff: `governance/INDIA14_TO_INDIA15_HANDOFF_2026-09-01.md`

Purpose: every successor must know which files are ALWAYS current, which are required only for one cluster/topic, which are frozen recovery evidence, which are SEARCH_ONLY provenance, which may NEVER independently control current truth, and whether the CURRENT session actually executed the boot.

## A. ALWAYS — EXACTLY FOLLOW MASTER BOOT V8 + BOOT_MANIFEST_V8.json

`governance/BOOT_MANIFEST_V8.json` is the sole machine-readable authority for the mandatory central/CCI/active-cluster file sets and their counts. `governance/INDIA_MASTER_BOOT.md` is the sole authority for the read ORDER, receipt mechanics and gate sequencing built on top of that manifest. The knowledge map MUST NOT maintain a shorter or differently-numbered competing boot list; the list below is a human-readable mirror of the manifest's `central_required` array and must stay identical to it.

Fresh-session rule before content:
- every new INDIA session starts `UNBOOTED`, regardless of predecessor/chat/model summary;
- `governance/FRESH_SESSION_BOOT_GATE.md` is an explicit mandatory read, not a pointer-only file;
- after all reads, the CURRENT session must write a NEW append-only receipt under `governance/boot_receipts/INDIA<N>__<NONCE>.json` (per `governance/BOOT_MANIFEST_V8.json`'s `receipt_directory`/`receipt_mode`) showing `boot_gate: PASS`, and pass the current canonical boot validator;
- `governance/BOOT_SESSION_RECEIPT.md` may still be refreshed as a human pointer but is never itself sufficient proof;
- even a mechanical receipt PASS is not content authorization until the independent CHECK/final authorization passes under the current streamlined protocol;
- partial/truncated/summary-only reads do not count.

Current master boot V8 requires the central durable core including:
- `governance/FRESH_SESSION_BOOT_GATE.md`;
- `governance/INDIA_MASTER_BOOT.md`;
- `governance/INDIA_BEHAVIORAL_EXECUTION_CONTRACT.md`;
- `governance/MARK_TRAVEL_PREFERENCES_CURRENT.md`;
- `governance/MARK_LOCATION_NAMING_CONTEXT_PROTOCOL.md`;
- `governance/MAP_COORDINATE_VERIFICATION_RULE.md`;
- `governance/INDIA_HUMAN_CENTERED_COMPLEX_TRIP_PLANNING_STANDARD.md`;
- `governance/FINAL_COMFORT_SWEEP_RULE_2026-08-23.md`;
- `governance/TRIP_FRAME_HARD.md`;
- `governance/CURRENT_DECISIONS_MASTER.md`;
- `governance/DECISION_LEDGER.jsonl`;
- `governance/CURRENT_STATE.md`;
- `governance/SUCCESSOR_SAFE_STATE.md` — crash-recovery checkpoint; read even if `CURRENT_STATE.md` seems complete, reconcile immediately if they disagree;
- `governance/INDIA_RECOVERY_DELTAS_CURRENT.md`;
- this `governance/INDIA_CURRENT_KNOWLEDGE_MAP.md`;
- `governance/INDIA14_START_AND_INDEPENDENT_CHECK.md` — canonical START/CHECK protocol, generalized for later INDIA versions despite historical filename.

Central mandatory full-read count = `16/16` unless the machine-readable manifest itself changes.

Then the mandatory CCI successor-parity layer at immutable completed commit `b5349afe41f98eb4870728aaff2c633899afc1fa` on `agent/cci-full-repo-knowledge-harvest`:
1. `runs/active/CCI-FULL-REPO-KNOWLEDGE-HARVEST-001/SUCCESSOR_START_HERE.md`
2. `runs/active/CCI-FULL-REPO-KNOWLEDGE-HARVEST-001/SUPERSEDED_AND_DO_NOT_REVIVE.md`
3. `runs/active/CCI-FULL-REPO-KNOWLEDGE-HARVEST-001/MARK_CURRENT_CANON_MASTER.md`
4. `runs/active/CCI-FULL-REPO-KNOWLEDGE-HARVEST-001/PROJECT_PHILOSOPHY_AND_SELECTION_MODEL.md`
5. `runs/active/CCI-FULL-REPO-KNOWLEDGE-HARVEST-001/OPEN_MARK_DECISIONS_ONLY.md`
6. `runs/active/CCI-FULL-REPO-KNOWLEDGE-HARVEST-001/CURRENT_TRAVEL_EXECUTION_CANON.md`

CCI is frozen recovery/reconciliation evidence, not a time machine. Newer explicit Mark decisions and newer current central artifacts win. Old CCI frontier text and old route hypotheses must be reconciled, never copied blindly.

The append-only receipt at `governance/boot_receipts/INDIA<N>__<NONCE>.json` is the mandatory fresh-session OUTPUT, not a shortcut input. It records exact BOOT_HEAD and machine-checkable read evidence. Being append-only, prior sessions' receipts are never overwritten.

Reference only when needed: CCI `KNOWLEDGE_ATOMS.jsonl`, `COVERAGE_MANIFEST.csv`, `HARVEST_REPORT.md`, `work/NEW_KNOWLEDGE_CANDIDATES.md`.

## B. CURRENT GLOBAL CHECKSUM

Fixed A+ worlds:
1. DELHI
2. KUMAON
3. AGRA / TAJ MAHAL
4. BODH GAYA / GAYA
5. VARANASI / SARNATH
6. TIRUVANNAMALAI / ARUNACHALA

**All six fixed A+ local footprints/durations are now closed at the currently required planning precision.**

Current closed footprint summary:
- DELHI: DURATION_CLOSED / minimal fixed-core model LOCKED_BY_MARK — Nirmal Dham [A+] fixed content driver; one first Delhi hotel night + one final international-flight buffer night; zero guaranteed generic sightseeing days.
- KUMAON: DURATION_CLOSED — 9 occupied days / 9 nights through final Dunagiri night; Delhi -> Haidakhan inbound occupied day included; eastern exit separate adjacent edge charged once later.
- AGRA / TAJ: DURATION_CLOSED — Taj Mahal [A+] [UNESCO WH] only; one Agra hotel night LOCKED_BY_MARK; second night logistics fallback only.
- BODH GAYA / GAYA: content + execution + duration rule closed; default 2 hotel nights under useful early inbound, 3 only for late/disrupted inbound or conscious extra sacred-core time, max 3; Maya Heritage LOCKED_BY_MARK.
- VARANASI / SARNATH: DURATION_CLOSED — 8 occupied days / 8 nights; Sahi River View Guesthouse LOCKED_BY_MARK.
- TIRUVANNAMALAI / ARUNACHALA: DURATION_CLOSED — **5 nights LOCKED_BY_MARK**; low tempo + standalone full Sri Ramanasramam immersion day.

The real fixed-core inter-core edge pass and 34-day budget are complete:
`runs/active/INDIA10-CLUSTER-COVERAGE-REAUDIT-001/FIXED_CORE_REAL_INTERCORE_EDGES_AND_34_DAY_BUDGET_2026-09-01.md`.

Current fixed-core night accounting:
- 28 committed India-night slots;
- 5 genuinely unallocated optional-world nights;
- do not precharge authorized contingencies before they actually occur.

The true LP/general-traveler integrity audit, targeted repairs and Delhi food/cinema/IMAX final pass are also complete enough for this stage. Do not restart them as unfinished work.

**CURRENT MARK-ONLY FRONTIER = OPTIONAL WORLD SURVIVAL.**
Decision-ready artifact:
`runs/active/INDIA10-CLUSTER-COVERAGE-REAUDIT-001/OPTIONAL_WORLD_SURVIVAL_DECISION_READY_2026-09-01.md`.

Current optional-world packages:
- A — INDIA recommendation: Braj 1 + Puducherry/Mamallapuram South 3 + 1 flex.
- B — Haridwar 2 + Braj 1 + South 2.
- C — Haridwar 2 + South 3; no Braj.
- D — Braj 2 + South 3; no slack.
- E — Haridwar 2 + Braj 1 + 2 flex; no South.
- custom combination allowed.

Do not ask another planning question first. After Mark chooses, record choice + WHY, freeze FINAL TOPOLOGY, then continue automatically to live logistics/calendar.

Hard route guard:
- Ranchi + Kolkata/Hooghly/Serampore/Dakshineswar + Puri/Odisha route family explicitly skipped for this trip unless Mark explicitly reopens.

## C. CCI PARITY FILTER — CURRENT / RECHECK / SUPERSEDED

When CCI and central differ, classify before use.

### Still-valid and successor-relevant
- item-level grade protection is much larger than short master summaries; use `A_PLUS_MARK_DECISION_LOG.md` when exact active-cluster item truth matters;
- human transfer-accounting principles from `GLOBAL_TRANSFER_LEDGER_2026-08-25.md` remain useful, but the current fixed-core edge result is now the 2026-09-01 fixed-edge artifact;
- Varanasi delivered legacy KML contains weak/unconfirmed pins; recovered better working points exist but must pass the current fit-for-purpose map-verification gate before final use;
- VNS-CAND-001 Lahiri Mahasaya Samadhi/Satyalok identity split remains an INDIA data-repair issue, not a Mark choice;
- Varanasi emotional sequencing preference remains valid: connect early with Lahiri/Kriya + Assi/Ganges; Manikarnika can deliberately come later for acclimatization;
- Sarnath UNESCO precision remains valid: exact inscribed components matter;
- event/service signals frozen in older CCI remain `LIVE_RECHECK_LATER`, not route locks;
- Mark's Ramakrishna concern, Sri Aurobindo/Puducherry interest, Anandamayi Ma x Yogananda joint-photo override, copy-paste/iPhone rule and explicit-next-action rule remain successor-relevant unless a newer explicit Mark statement supersedes them.

### Already centrally adopted / do not duplicate as new discovery
- GitHub is external memory and INDIA must be replaceable;
- Mark is not the courier;
- spiritually open + evidence-critical;
- Ramakrishna is personally important;
- Sri Aurobindo is a real but non-mandatory interest;
- strong nature/water/walking preference;
- historic pastry/sweets/coffee/human-texture sensitivity;
- final comfort sweep mandatory;
- reverse discovery may add findings without silently changing old grades;
- exact map identity/coordinates require fit-for-purpose current verification;
- fresh-session context/summary is not a boot.

### Superseded by newer central truth
- CCI's frozen Bodh Gaya OPEN frontier is closed; never re-present that ballot.
- CCI's old Maya Heritage non-lock is superseded: Maya Heritage is LOCKED_BY_MARK.
- CCI's frozen `VNS -> Chennai primary / Bengaluru fallback` and later `Bengaluru inbound + long private car` defaults are non-controlling.
- Any older instruction saying Tiruvannamalai 4/5/6 nights, Agra duration or Delhi duration are still open is superseded. All six fixed footprints are closed.
- Any older instruction saying fixed-core edge/budget work is still the active frontier is superseded. That work is complete; optional-world survival is current.
- any frozen CCI statement contradicted by a later explicit central Mark decision loses.

## D. CONDITIONAL ANTI-FORGET REGISTERS

Mandatory when their detail can affect `AL BESLIST?`:
- `runs/active/INDIAZILVER-ENTITY-ID-PROXIMITY-BACKFILL-001/PROTECTED_CANON_BASELINE.csv` — permanent IDs + protected older decisions; old grade never beats later explicit Mark decision.
- `runs/active/INDIA10-CLUSTER-COVERAGE-REAUDIT-001/A_PLUS_MARK_DECISION_LOG.md` — later item-level grade/A+ truth.
- `runs/active/INDIA10-CLUSTER-COVERAGE-REAUDIT-001/CURRENT_OLD_A_PROMOTION_MASTER.md` — promotion/regrade provenance; later decision log wins where different.
- durable `decisions/*.md` originals — targeted provenance where master/ledger points.
- `runs/active/INDIA10-CLUSTER-COVERAGE-REAUDIT-001/TRIP_PLANNING_META_CONTROLLER_2026-08-26.md` — method provenance/controller detail.

If current master + active cluster package do not resolve an entity confidently, consult these before asking Mark to reconstruct anything.

## E. REQUIRED_BEFORE_TOUCHING_BODH_GAYA
File map/orientation (which of the 13 active Bodh Gaya files is current vs superseded): `runs/active/INDIA10-CLUSTER-COVERAGE-REAUDIT-001/BODHGAYA_GAYA_FILE_INDEX.md`.
Read current closure first, then older prep only for detail:
1. `decisions/BODHGAYA_CLUSTER_CLOSURE_MARK_DECISION_2026-08-29.md`
2. `runs/active/INDIA10-CLUSTER-COVERAGE-REAUDIT-001/BODHGAYA_PREP_PACKET_2026-08-27.md`
3. `runs/active/INDIA10-CLUSTER-COVERAGE-REAUDIT-001/BODHGAYA_INDIA12_BOUNDED_CURRENT_CHECK_2026-08-27.md`
4. `runs/active/INDIA10-CLUSTER-COVERAGE-REAUDIT-001/BODHGAYA_STRICT_LP_LAYER_GATE_2026-08-27.md`
5. `runs/active/INDIA10-CLUSTER-COVERAGE-REAUDIT-001/INDIA12_RECOVERY_CANON_RECONCILIATION_2026-08-28.md`

Hard current checksum: Mahabodhi/Bodhi Tree A+ [UNESCO WH]; Sujata Stupa A+; Dungeshwari/Mahakala Caves A+; Great Buddha A; Barabar/Nagarjuni C / DO NOT RE-PRESENT; Maya Heritage LOCKED_BY_MARK; former six-item open batch CLOSED.

OPEN QUESTION (flagged, not resolved, 2026-09-02 structural pass): whether file #4's own remaining rows (Sher Shah Suri's Tomb, Patharkatti, Tutla Bhawani) still need Mark triage the way Delhi's did, or are genuinely covered by later work, was found genuinely ambiguous from the files alone and was deliberately left unmarked pending a real Mark/INDIA check — do not assume either answer without checking directly, given the Delhi precedent for this exact category of mistake.

## F. REQUIRED_BEFORE_TOUCHING_KUMAON
File map/orientation (which of the 13 active Kumaon files is current vs superseded): `runs/active/INDIA10-CLUSTER-COVERAGE-REAUDIT-001/KUMAON_FILE_INDEX.md`.
Read:
1. `runs/active/INDIA10-CLUSTER-COVERAGE-REAUDIT-001/KUMAON_DURATION_MARK_DECISION_2026-08-27.md`
2. `runs/active/INDIA10-CLUSTER-COVERAGE-REAUDIT-001/KUMAON_COMPLETE_EXECUTION_DRAFT_2026-08-26.md`
3. `runs/active/INDIA10-CLUSTER-COVERAGE-REAUDIT-001/BABAJI_DUNAGIRI_RETREAT_LOCKED_ACCOMMODATION_2026-08-25.md`
4. `runs/active/INDIA10-CLUSTER-COVERAGE-REAUDIT-001/A_PLUS_MARK_DECISION_LOG.md` for exact item grades.
5. `runs/active/INDIA10-CLUSTER-COVERAGE-REAUDIT-001/GLOBAL_TRANSFER_LEDGER_2026-08-25.md` before detailed day bundles/edges.

Hard current: 9/9 closed; Haidakhan 3 nights/2 quiet days; Hotel Evelyn A+; Kainchi Dham A+; Mahavatar Babaji Cave A+; YSS Dwarahat A full day/no overnight; Kakrighat A*/SKIP_FIRST; Dunagiri Retreat primary/Joshi fallback. CCI also protects less-visible item grades.

## G. REQUIRED_BEFORE_TOUCHING_VARANASI / SARNATH
File map/orientation (which of the 15 active Varanasi files is current vs superseded): `runs/active/INDIA10-CLUSTER-COVERAGE-REAUDIT-001/VARANASI_FILE_INDEX.md`.
Read:
1. `runs/active/INDIA10-CLUSTER-COVERAGE-REAUDIT-001/VARANASI_DURATION_MARK_DECISION_2026-08-27.md`
2. `runs/active/INDIA10-CLUSTER-COVERAGE-REAUDIT-001/BHRIGU_BHADURY_A_PLUS_OPERATIONAL_CLOSURE_2026-08-27.md`
3. `runs/active/INDIA10-CLUSTER-COVERAGE-REAUDIT-001/A_PLUS_MARK_DECISION_LOG.md` for exact current A+/A/A*/B/C spine.
4. `runs/active/INDIA10-CLUSTER-COVERAGE-REAUDIT-001/SARNATH_VISIT_GUIDANCE_AND_UNESCO_LABEL_2026-08-27.md` before Sarnath day cards/UNESCO claims.
5. `runs/active/INDIA10-CLUSTER-COVERAGE-REAUDIT-001/VARANASI_HISTORICAL_PACE_PREFERENCE_RECOVERY_2026-08-27.md` before final sequencing.
6. `runs/active/VARANASI-GEO-DELIVERY-REPAIR-001/NUMBERING_REGISTRY.jsonl` when immutable 001–040 identity matters.

Geo warning: old delivered KML pins are not automatically safe. Before final maps/day-routing, reverify the retained points fit-for-purpose; do not demand irrelevant front-door precision.

## H. REQUIRED_BEFORE_TOUCHING_TIRUVANNAMALAI / ARUNACHALA
File map/orientation (which of the 14 active Tiruvannamalai files is current vs superseded — the LP ballot in items below was later dropped, see index): `runs/active/INDIA10-CLUSTER-COVERAGE-REAUDIT-001/TIRUVANNAMALAI_FILE_INDEX.md`.
Read current locks first:
1. `decisions/TIRUVANNAMALAI_5_NIGHTS_MARK_DECISION_2026-08-31.md` — **5 nights LOCKED_BY_MARK**.
2. `runs/active/INDIA10-CLUSTER-COVERAGE-REAUDIT-001/TIRUVANNAMALAI_MARK_DECISION_HUMAN_DAYPLAN_2026-08-31.md` — current human/geographic dayplan surface.
3. `decisions/TIRUVANNAMALAI_LONELY_PLANET_LAYER_DROPPED_BY_MARK_2026-08-31.md` — complete extra local LP layer dropped; do not re-present.
4. `decisions/TIRUVANNAMALAI_INBOUND_COMFORT_PREFERENCE_MARK_DECISION_2026-08-31.md` — Chennai arrival: rail preferred over long taxi when roughly <=1.5 h slower; 3–4 h taxi disliked for modest saving.
5. `runs/active/INDIA10-CLUSTER-COVERAGE-REAUDIT-001/TIRUVANNAMALAI_DAYPLAN_PRESENTATION_AUDIT_2026-08-31.md` — presentation anti-regression.
6. `runs/active/INDIA10-CLUSTER-COVERAGE-REAUDIT-001/TIRUVANNAMALAI_SRI_RAMANASRAMAM_STAY_MODEL_2026-08-30.md` — ashram stay/free-time detail.
7. `governance/COORDINATE_INTEGRITY_GATE.md` plus `governance/MAP_COORDINATE_VERIFICATION_RULE.md` — fit-for-purpose, no precision theatre.
8. `runs/active/INDIA10-CLUSTER-COVERAGE-REAUDIT-001/KOMOOT_WALK_DISCOVERY_LAYER_2026-08-25.md` when walking/navigation detail is touched.
9. `runs/active/INDIA10-CLUSTER-COVERAGE-REAUDIT-001/TIRUVANNAMALAI_MANGO_TREE_CAVE_CONTEXT_2026-08-31.md` when cave-route detail is touched.

Hard recognition: **Tiruvannamalai / Arunachala — Ramana Maharshi sacred mountain/ashram world [A+ parent]**. Protected A children: Sri Ramanasramam; Virupaksha Cave; Skandashram; Arunachaleswarar/Annamalaiyar Temple; Gurumurtam; Pavalakunru/Pavazhakundru; full 14 km Giripradakshina/Girivalam. B reserves: Mango Tree Cave only if natural on hill route; Pachaiamman Temple only if naturally easy. Sri Ramanasramam is desired true ashram sleep #2 if accepted/available.

**Full additional local LP layer is DROPPED_BY_MARK.** Do not show Gingee, Tirumalai Jain, Parvathamalai, Mamandur, Jawadhu, Jambai etc. as current Tiruvannamalai choices.

Current lock = **5 nights**: arrival night + four local days, preserving a standalone full Ramanasramam immersion day. There is no remaining 4/5/6 Mark ballot.

Human precision guard: ordinary times quarter-/half-hour blocks; no pseudo-exact local arrivals; no wake-up/get-out-of-bed micromanagement; small same-entity pin/door differences that cannot affect mode/burden/day count do not block planning.

## I. REQUIRED_BEFORE_TOUCHING_DELHI
File map/orientation (which of the 7 active Delhi files is current fixed-core vs the controlling reserve vs historical): `runs/active/INDIA10-CLUSTER-COVERAGE-REAUDIT-001/DELHI_FILE_INDEX.md`.
**The broad Delhi LP/general-traveler reserve is NOT fully Mark-triaged — see `governance/CURRENT_STATE.md`'s 2026-09-02 correction before treating Delhi as complete.**
Read:
1. `decisions/DELHI_MINIMAL_FIXED_CORE_MARK_DECISION_2026-08-31.md`.
2. `decisions/DELHI_RESERVE_B_GRADES_MARK_DECISION_2026-08-31.md`.
3. `runs/active/INDIA10-CLUSTER-COVERAGE-REAUDIT-001/DELHI_SPARE_DAY_LP_TOPX_LAYER_2026-08-31.md` — the broad controlling Delhi traveler reserve (`Controlling: YES`); still has genuinely un-triaged `[OPEN / NOT GRADED]` rows.
4. `runs/active/INDIA10-CLUSTER-COVERAGE-REAUDIT-001/DELHI_TRAVELER_FOOD_CINEMA_FINAL_PASS_2026-09-01.md` for food/cinema fine detail (`Controlling: NO` — a supplement; grades nothing, does not close #3's gate).
5. `runs/active/INDIA10-CLUSTER-COVERAGE-REAUDIT-001/DELHI_BROAD_LP_MARK_TRIAGE_2026-09-02.md` — live tracking of Mark's triage of #3 (`Controlling: YES`).
6. older `DELHI_PREP_PACKET_2026-08-27.md` only when deeper background is needed.

Hard current:
- Nirmal Dham [A+] is the sole fixed Delhi content driver.
- minimal fixed-core model is DURATION_CLOSED: one first Delhi hotel night + one final airport/international buffer night; no guaranteed generic sightseeing day.
- active B reserves in both Delhi windows: PVR Priya IMAX [B], Hauz Khas Village [B], Humayun's Tomb [B] [UNESCO WH], Sunder Nursery [B].
- PVR Priya = current large-modern-IMAX enthusiast pick; exact film/showtime/subtitle/screen LIVE_RECHECK_LATER at day-card stage.
- Delite Cinema remains OPEN as a historic/cultural Hindi-film alternative; do not auto-grade it.
- bounded/quiet Delhi; no forced generic Old Delhi.

## J. REQUIRED_BEFORE_TOUCHING_AGRA / TAJ
File map/orientation (which of the 6 active Agra files is current fixed-core vs reserve vs historical): `runs/active/INDIA10-CLUSTER-COVERAGE-REAUDIT-001/AGRA_FILE_INDEX.md`.
Read newest Mark locks first:
1. `decisions/AGRA_TAJ_ONLY_FIXED_CORE_MARK_DECISION_2026-08-31.md`
2. `decisions/AGRA_TAJ_1_NIGHT_MARK_DECISION_2026-08-31.md`
3. `runs/active/INDIA10-CLUSTER-COVERAGE-REAUDIT-001/AGRA_TAJ_ONLY_ADVANCE_DECISION_READY_PREP_2026-08-31.md`
4. `runs/active/INDIA10-CLUSTER-COVERAGE-REAUDIT-001/AGRA_TAJ_MAHAL_YOGANANDA_ONSITE_MEMORY_CUE_2026-08-31.md`
5. older `AGRA_PREP_PACKET_2026-08-27.md` only as background/provenance, NOT as a reason to reopen extra Agra attractions.

Hard current: **Taj Mahal [A+] [UNESCO WH] ONLY for the fixed Agra world — LOCKED_BY_MARK**. **One Agra hotel night LOCKED_BY_MARK.** Earliest practical Taj morning; same-evening onward toward Gaya is preferred when the actual-date rail product is sane. Fatehpur Sikri, Keoladeo, Chambal, Agra Fort, Baby Taj, Mehtab etc. do NOT receive extra day/night weight unless Mark explicitly reopens them. Yogananda-at-Taj photo memory cue from Ananda video ~04:44 must surface on-site.

## K. OPTIONAL WORLDS — CURRENT MARK-ONLY FRONTIER
Controlling decision-ready comparison:
`runs/active/INDIA10-CLUSTER-COVERAGE-REAUDIT-001/OPTIONAL_WORLD_SURVIVAL_DECISION_READY_2026-09-01.md`.

### Braj / Mathura–Vrindavan–Govardhan
Not dropped, not mandatory, not A+ by inference. Protected existing A sites include:
- Neeb/Neem Karoli Baba Ashram + Mahasamadhi Mandir [A];
- Katyayani Peeth / Keshav Ashram [A].
Lean survival footprint = 1 night; unusually strong payoff/friction beside Agra. Load `decisions/NEEM_KAROLI_VRINDAVAN_RED_HOUSE_ROUTE_RULE_2026-08-29.md` and current optional-world artifact before advice.

### Haridwar / Kankhal / Rishikesh
Inclusion unresolved. Protected existing A = Shree Shree Ma Anandamayee Ashram + Samadhi Mandir, Kankhal [A]. Best insertion before Kumaon; 2 nights recommended if surviving. Do not use stale Kumbh/Ardh-Kumbh claims as route drivers.

### Prayagraj
Current survival recommendation = NO. Red House / 4 Church Lane remains B / only if Prayagraj already happens / access confirmed / zero independent route weight. Do not destroy the efficient Agra->overnight train->Gaya edge merely to capture this B.

### Puducherry + Mamallapuram southern gateway
Positive / inclusion unresolved; no grade inferred. Current meaningful components include Sri Aurobindo Ashram, Puducherry White Town and Group of Monuments at Mahabalipuram/Mamallapuram [UNESCO WH]. Geometry naturally turns the Tiruvannamalai exit toward Chennai into content. Preferred uncompressed survival = 3 nights; compressed = 2.

### Ramakrishna
Durable wish remains for one substantial genuine route-logical historical Ramakrishna place, but no current optional corridor produces a place that should independently consume the five-night envelope. Do not misrepresent a modern mission branch as a Ramakrishna life-site.

Current packages: A Braj1+South3+1flex (INDIA recommendation); B Haridwar2+Braj1+South2; C Haridwar2+South3; D Braj2+South3; E Haridwar2+Braj1+2flex; custom allowed.

## L. ROUTE / TRANSFER — FIXED CORE COMPLETE; FINAL TOPOLOGY WAITS ON OPTIONAL CHOICE
Current controlling fixed-core edge/budget artifact:
- `runs/active/INDIA10-CLUSTER-COVERAGE-REAUDIT-001/FIXED_CORE_REAL_INTERCORE_EDGES_AND_34_DAY_BUDGET_2026-09-01.md`.

Useful background principles when live-routing later:
- `runs/active/INDIA10-CLUSTER-COVERAGE-REAUDIT-001/ROUTE_PLANNING_SYSTEM_CORRECTION_2026-08-25.md`
- `runs/active/INDIA10-CLUSTER-COVERAGE-REAUDIT-001/GLOBAL_TRANSFER_LEDGER_2026-08-25.md`
- `runs/active/INDIA10-CLUSTER-COVERAGE-REAUDIT-001/CLUSTER_TOPOLOGY_FEASIBILITY_2026-08-25.md`
- `runs/active/INDIA10-CLUSTER-COVERAGE-REAUDIT-001/CLUSTER_TOPOLOGY_QUANTIFIED_DELTA_2026-08-26.md`
- `TIRUVANNAMALAI_TRANSFER_MODE_CORRECTION_2026-08-30.md` as transport-hierarchy evidence, filtered through newer current truth.

Current fixed-edge checksum:
1. Delhi -> Haidakhan is inside Kumaon K0; do not double-count.
2. final Dunagiri -> Agra is a separate full positioning day; direct private car current humane baseline.
3. Agra -> Gaya strongest current baseline = 12988 overnight, current daily/1A planning evidence; LIVE_RECHECK_LATER.
4. Gaya -> Varanasi current strongest baseline = 20887 ~3h05; absorbed into Varanasi V0; exact Jan operation LIVE_RECHECK_LATER.
5. Varanasi -> Tiruvannamalai = flight VNS->MAA + rail-first MAA/Tambaram->Tiruvannamalai under Mark's comfort rule; inside T0.
6. Tiruvannamalai -> Delhi is only a direct comparator, not topology-locked because the southern optional world may intervene.

Old exact V1/V2 calendars are provenance only. Train-first remains a hard transport principle. Do not freeze the final topology until Mark resolves optional-world survival.

## M. BOOKING / LIVE LOGISTICS — CONDITIONAL
`runs/active/INDIA10-BOOKING-SEQUENCE-CLOSURE-001/BOOKING_ACTION_BOARD.md` = SEARCH_ONLY provenance/live-source lead. Old V2 dates/base choices are not current route truth.

Live logistics/calendaring starts only after optional-world survival and FINAL TOPOLOGY are closed.

Recheck at the proper stage: visa; Haidakhan acceptance; Dunagiri Retreat availability/winter operation; Hotel Evelyn; Sahi River View balcony; Sri Ramanasramam application/acceptance; Bhrigu provider process; trains/flights/opening/access; winter fog; Delhi cinema film/showtime/subtitle/screen; actual January train operating days/inventory.

Durable booking wording guard from CCI: never ask a property to reserve “the Ram Dass room”; exact room is not proven.

## N. PERSON / EVIDENCE — CONDITIONAL
Apply as needed:
- `decisions/BABAJI_MYTHIC_FIGURE_EVIDENCE_RULE_2026-08-19.md`;
- `decisions/TOP11_SWEEP_DEPTH_BY_PERSON_2026-08-18.md`;
- `decisions/REVERSE_DISCOVERY_REOPEN_RULE_2026-08-19.md`;
- `governance/ANANDAMAYI_YOGANANDA_PHOTO_OVERRIDE_2026-08-20.md`;
- `decisions/NEEM_KAROLI_VRINDAVAN_RED_HOUSE_ROUTE_RULE_2026-08-29.md`.

Hard recovered personal guard: a physically resolved India location where Anandamayi Ma and Paramahansa Yogananda are documented together in a photograph must be surfaced as `MUST_VISIT_WITHIN_INCLUDED_CLUSTER` if that cluster is included; it does not by itself force an excluded macro-region.

Top-11 research-depth guard remains: deep evidence follows personal relevance; Ramakrishna is personally underrepresented in Mark's view and substantial route-logical Ramakrishna places deserve attention later without forcing detours.

## O. SEARCH_ONLY / PROVENANCE
Never independently current unless explicitly re-adopted/reconciled:
- `governance/ACTIVE_STATE.md`;
- old `handoffs/*`;
- INDIA6/7/8/9/10/11/12 successor snapshots/hot handoffs;
- old route V1/V2/exact calendars;
- old route/topology checkpoints;
- old A+ review indices/checklists;
- old Komoot WAITING trackers;
- worker TASK/STATUS/COMPLETE files;
- PRE_BRONS/watchlists/candidate lists;
- old PDFs;
- PR #23 comments before current adoption/reconciliation;
- branch-only worker output before central-effect review;
- CCI frozen frontier statements that have newer central replacements.

Exception: `governance/INDIA14_TO_INDIA15_HANDOFF_2026-09-01.md` is a current predecessor handoff pointer only because `CURRENT_STATE.md`/`SUCCESSOR_SAFE_STATE.md` explicitly route to it; it never outranks controlling current authority.

## P. NEVER_AS_CURRENT
Never independently mutate current planning from:
- old handoff claiming CURRENT/FINAL/MUST_READ;
- old exact calendar;
- worker COMPLETE marker;
- raw candidate list;
- old booking-board date/base;
- protected-baseline grade against a later Mark decision;
- unreconciled PR comment;
- frozen CCI statement contradicted by later central truth;
- predecessor/model/context summary used as a substitute for this session's boot.

## Q. INTEGRATION STATE VOCABULARY
Use one of: RECEIVED_UNREVIEWED / REVIEWED_NOT_ADOPTED / PARTIALLY_ADOPTED / ADOPTED / PROVENANCE_ONLY / REJECTED_OR_SUPERSEDED.

## R. UPDATE DISCIPLINE — CONTINUOUS SUCCESSOR PARITY
After every material event, not only Mark decisions:
1. put detailed new fact/research/geometry in the exact current artifact;
2. update `CURRENT_STATE.md` when frontier/completed work/next action materially changes;
3. for a Mark decision update ledger + current master + exact decision artifact in the same cycle, preserving WHY;
4. update profile for durable Mark preference/WHY;
5. update recovery deltas for reusable failure traps;
6. update THIS map whenever a successor must know a new source path or a current source is superseded;
7. keep `SUCCESSOR_SAFE_STATE.md` aligned when its crash checkpoint materially changes;
8. every fresh successor executes the current manifest/receipt/CHECK mechanics rather than relying on old session state;
9. after authorization, explicitly compare `CURRENT_STATE.md`, `SUCCESSOR_SAFE_STATE.md`, this map section B and `CURRENT_DECISIONS_MASTER.md`; any material frontier mismatch is a blocking repository-memory defect to repair before content;
10. reconstruct interruptions: completed side work is history, the still-open controlling frontier is the only first action unless Mark explicitly changes it;
11. before reply test: `IF THIS CHAT DIES NOW, CAN INDIA(N+1) RECOVER THIS FROM MASTER BOOT + THIS MAP WITHOUT MARK?`

**MAP-SYNC GUARD:** after every change to `INDIA_MASTER_BOOT.md` that adds/removes/changes a mandatory read, update section A of this map in the same execution cycle. After every frontier closure or material operational-frontier change, update section B and the relevant cluster section in the same execution cycle. A stale map is a successor-memory failure, not harmless documentation drift.

END CURRENT KNOWLEDGE MAP
