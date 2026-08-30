# INDIA CURRENT KNOWLEDGE MAP — WAT MOET JE LEZEN / WAT IS OUD

Status: **CURRENT LIVING SOURCE MAP — V8 / MANIFEST-DRIVEN + FRESH-SESSION-BOOT-PROOF + CCI-PARITY-SYNCHRONIZED**
Updated: 2026-08-30
Branch: `agent/india8-cluster-casting`
Canonical manifest: **`governance/BOOT_MANIFEST_V8.json`** — the single machine-readable authority for exactly which files/counts are mandatory. This map explains ROUTING and WHY; it does not define a competing mandatory set. If a count or file list below ever disagrees with the manifest, the manifest wins and this map must be corrected in the same change.
Boot owner: `governance/INDIA_MASTER_BOOT.md` V8
Decision-ledger migration: **DECISION_LEDGER_BACKFILL_COMPLETE**
CCI parity source: immutable completed harvest `b5349afe41f98eb4870728aaff2c633899afc1fa`

Purpose: every successor must know which files are ALWAYS current, which are required only for one cluster/topic, which are frozen recovery evidence, which are SEARCH_ONLY provenance, which may NEVER independently control current truth, and whether the CURRENT session actually executed the boot.

## A. ALWAYS — EXACTLY FOLLOW MASTER BOOT V8 + BOOT_MANIFEST_V8.json

`governance/BOOT_MANIFEST_V8.json` is the sole machine-readable authority for the mandatory central/CCI/active-cluster file sets and their counts. `governance/INDIA_MASTER_BOOT.md` is the sole authority for the read ORDER, receipt mechanics and gate sequencing built on top of that manifest. The knowledge map MUST NOT maintain a shorter or differently-numbered competing boot list; the list below is a human-readable mirror of the manifest's `central_required` array and must stay identical to it.

Fresh-session rule before content:
- every new INDIA session starts `UNBOOTED`, regardless of predecessor/chat/model summary;
- `governance/FRESH_SESSION_BOOT_GATE.md` is an explicit mandatory read, not a pointer-only file;
- after all reads, the CURRENT session must write a NEW append-only receipt under `governance/boot_receipts/INDIA<N>__<NONCE>.json` (per `governance/BOOT_MANIFEST_V8.json`'s `receipt_directory`/`receipt_mode`) showing `boot_gate: PASS`, and pass `governance/scripts/validate_successor_boot.py --require-session-receipt <path> --expected-session <N> --expected-nonce <NONCE>`; `governance/BOOT_SESSION_RECEIPT.md` may still be refreshed as a human pointer but is never itself sufficient proof;
- even a mechanical receipt PASS is not content authorization until an independent CHECK session passes (`governance/INDIA14_START_AND_INDEPENDENT_CHECK.md`);
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
- this `governance/INDIA_CURRENT_KNOWLEDGE_MAP.md`.

Central mandatory full-read count = `15/15`.

Then the mandatory CCI successor-parity layer at immutable completed commit `b5349afe41f98eb4870728aaff2c633899afc1fa` on `agent/cci-full-repo-knowledge-harvest`:
1. `runs/active/CCI-FULL-REPO-KNOWLEDGE-HARVEST-001/SUCCESSOR_START_HERE.md`
2. `runs/active/CCI-FULL-REPO-KNOWLEDGE-HARVEST-001/SUPERSEDED_AND_DO_NOT_REVIVE.md`
3. `runs/active/CCI-FULL-REPO-KNOWLEDGE-HARVEST-001/MARK_CURRENT_CANON_MASTER.md`
4. `runs/active/CCI-FULL-REPO-KNOWLEDGE-HARVEST-001/PROJECT_PHILOSOPHY_AND_SELECTION_MODEL.md`
5. `runs/active/CCI-FULL-REPO-KNOWLEDGE-HARVEST-001/OPEN_MARK_DECISIONS_ONLY.md`
6. `runs/active/CCI-FULL-REPO-KNOWLEDGE-HARVEST-001/CURRENT_TRAVEL_EXECUTION_CANON.md`

CCI is frozen recovery/reconciliation evidence, not a time machine. Newer explicit Mark decisions and newer current central artifacts win. In particular, old CCI frontier text and old route hypotheses must be reconciled, never copied blindly.

The append-only receipt at `governance/boot_receipts/INDIA<N>__<NONCE>.json` is the mandatory fresh-session OUTPUT, not a shortcut input. It records exact BOOT_HEAD, per-file blob evidence and byte-level read coverage, 15/15 + 6/6 full reads, no unfinished truncation, no summary substitution, active-cluster gate, proof-of-read quotes and control-veto checksum. Being append-only, prior sessions' receipts are never overwritten. `governance/BOOT_SESSION_RECEIPT.md` may be refreshed as a convenience pointer to the latest one but carries no independent authority.

Reference only when needed: CCI `KNOWLEDGE_ATOMS.jsonl`, `COVERAGE_MANIFEST.csv`, `HARVEST_REPORT.md`, `work/NEW_KNOWLEDGE_CANDIDATES.md`.

## B. CURRENT GLOBAL CHECKSUM

Fixed A+ worlds:
1. DELHI
2. KUMAON
3. AGRA / TAJ MAHAL
4. BODH GAYA / GAYA
5. VARANASI / SARNATH
6. TIRUVANNAMALAI / ARUNACHALA

Duration status:
- KUMAON: DURATION_CLOSED — 9 occupied days / 9 nights through final Dunagiri night; Delhi -> Haidakhan inbound occupied day included; eastern exit separate full-travel adjacent edge charged once later.
- VARANASI / SARNATH: DURATION_CLOSED — 8 occupied days / 8 nights through final Varanasi night; Bodh Gaya/Gaya -> Varanasi arrival/wind-down + 7 local days included.
- BODH GAYA / GAYA: content + execution + duration RULE closed; default 2 hotel nights if early inbound, 3 only for late/disrupted inbound or conscious extra sacred-core time, max 3; Maya Heritage LOCKED_BY_MARK.
- TIRUVANNAMALAI / ARUNACHALA: local duration surface exists and no duration is locked; 5 nights remains the current clean local recommendation, but **the current operational frontier is rail-first re-evaluation of the inbound/outbound inter-core edges before the duration surface is decision-ready again**. Previous flight + multi-hour-car defaults are not controlling.
- DELHI: prepared, not duration-closed.
- AGRA / TAJ: prepared, not duration-closed.

Current fixed-A+-only route skeleton:
`DELHI -> KUMAON -> AGRA/TAJ -> BODH GAYA/GAYA -> VARANASI/SARNATH -> TIRUVANNAMALAI/ARUNACHALA -> DELHI/INTERNATIONAL EXIT`.

Deferred optional worlds:
- Braj / Mathura–Vrindavan–Govardhan;
- Haridwar / Kankhal / Rishikesh;
- Prayagraj.

Hard route guard:
- Ranchi + Kolkata/Hooghly/Serampore/Dakshineswar + Puri/Odisha route family explicitly skipped for this trip unless Mark explicitly reopens.

## C. CCI PARITY FILTER — CURRENT / RECHECK / SUPERSEDED

When CCI and central differ, classify before use:

### Still-valid and successor-relevant
- item-level grade protection is much larger than the short master summaries; use `A_PLUS_MARK_DECISION_LOG.md` when exact active-cluster item truth matters;
- full human transfer accounting from `GLOBAL_TRANSFER_LEDGER_2026-08-25.md` remains controlling when edges are built;
- four Kumaon execution edges/operations remain P0_TO_RECLOSE where explicitly marked; never resurrect the invalid old shortcut;
- optional-world geometry remains: Braj low insertion tax near Delhi/Agra; Prayagraj corridor-compatible but not route-required because direct Agra->Gaya overnight exists; Haridwar/Kankhal/Rishikesh is materially heavier and, if retained, belongs before Kumaon;
- Varanasi delivered legacy KML contains weak/unconfirmed pins; recovered better working points exist but must pass the current `MAP_COORDINATE_VERIFICATION_RULE.md` before decision use;
- VNS-CAND-001 Lahiri Mahasaya Samadhi/Satyalok identity split remains an INDIA data-repair issue, not a Mark choice;
- NKB Vrindavan coordinates remain conflicted in old registries; no route pin until reverified;
- Varanasi emotional sequencing preference remains valid: connect early with Lahiri/Kriya + Assi/Ganges; Manikarnika can deliberately come later for acclimatization;
- Sarnath UNESCO precision remains valid: the inscribed serial property comprises Chaukhandi Stupa + Archaeological Remains; museum and modern Mulagandha Kuti Vihara are visit content, not UNESCO components;
- Haridwar Ardh Kumbh/Makar Sankranti signal around 14 Jan 2027 and YSS Dwarahat Christmas Long Meditation signal around 20 Dec 2026 are `LIVE_RECHECK_LATER` opportunities, not route locks;
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
- exact map identity/coordinates require current verification;
- fresh-session context/summary is not a boot; a current session receipt is required before substantive work.

### Superseded by newer central truth
- CCI's frozen Bodh Gaya OPEN frontier is closed; never re-present that six-item ballot.
- CCI's old Bodh Gaya sleep statement that Maya Heritage was not locked is superseded: Maya Heritage is now LOCKED_BY_MARK.
- CCI's frozen `VNS -> Chennai primary / Bengaluru fallback` south-gateway hypothesis and the later central `Bengaluru inbound + private car` working hypothesis are BOTH non-controlling after the 2026-08-30 boot-execution repair. The next operational task is rail-first re-evaluation under the hard transport hierarchy. Exact train/flight services remain LIVE_RECHECK_LATER until they affect the real edge decision.
- any CCI statement that only reflected frozen central commit `a374236...` loses to a later explicit central decision/artifact.

## D. CONDITIONAL ANTI-FORGET REGISTERS

Mandatory when their detail can affect `AL BESLIST?`:
- `runs/active/INDIAZILVER-ENTITY-ID-PROXIMITY-BACKFILL-001/PROTECTED_CANON_BASELINE.csv` — permanent IDs + protected older decisions; old grade never beats later explicit Mark decision.
- `runs/active/INDIA10-CLUSTER-COVERAGE-REAUDIT-001/A_PLUS_MARK_DECISION_LOG.md` — later item-level grade/A+ truth; especially important because the short boot summary cannot list all ~60+ graded items.
- `runs/active/INDIA10-CLUSTER-COVERAGE-REAUDIT-001/CURRENT_OLD_A_PROMOTION_MASTER.md` — promotion/regrade provenance; later decision log wins where different.
- durable `decisions/*.md` originals — targeted provenance where master/ledger points.
- `runs/active/INDIA10-CLUSTER-COVERAGE-REAUDIT-001/TRIP_PLANNING_META_CONTROLLER_2026-08-26.md` — method provenance/controller detail.

If current master + active cluster package do not resolve an entity confidently, consult these before asking Mark to reconstruct anything.

## E. REQUIRED_BEFORE_TOUCHING_BODH_GAYA
Read current closure first, then older prep only for detail:
1. `decisions/BODHGAYA_CLUSTER_CLOSURE_MARK_DECISION_2026-08-29.md`
2. `runs/active/INDIA10-CLUSTER-COVERAGE-REAUDIT-001/BODHGAYA_PREP_PACKET_2026-08-27.md`
3. `runs/active/INDIA10-CLUSTER-COVERAGE-REAUDIT-001/BODHGAYA_INDIA12_BOUNDED_CURRENT_CHECK_2026-08-27.md`
4. `runs/active/INDIA10-CLUSTER-COVERAGE-REAUDIT-001/BODHGAYA_STRICT_LP_LAYER_GATE_2026-08-27.md`
5. `runs/active/INDIA10-CLUSTER-COVERAGE-REAUDIT-001/INDIA12_RECOVERY_CANON_RECONCILIATION_2026-08-28.md`

Hard current checksum: Mahabodhi/Bodhi Tree A+ [UNESCO WH]; Sujata Stupa A+; Dungeshwari/Mahakala Caves A+; Great Buddha A; Barabar/Nagarjuni C / DO NOT RE-PRESENT; Maya Heritage LOCKED_BY_MARK; former six-item open batch CLOSED.

## F. REQUIRED_BEFORE_TOUCHING_KUMAON
Read:
1. `runs/active/INDIA10-CLUSTER-COVERAGE-REAUDIT-001/KUMAON_DURATION_MARK_DECISION_2026-08-27.md`
2. `runs/active/INDIA10-CLUSTER-COVERAGE-REAUDIT-001/KUMAON_COMPLETE_EXECUTION_DRAFT_2026-08-26.md`
3. `runs/active/INDIA10-CLUSTER-COVERAGE-REAUDIT-001/BABAJI_DUNAGIRI_RETREAT_LOCKED_ACCOMMODATION_2026-08-25.md`
4. `runs/active/INDIA10-CLUSTER-COVERAGE-REAUDIT-001/A_PLUS_MARK_DECISION_LOG.md` for exact item grades.
5. `runs/active/INDIA10-CLUSTER-COVERAGE-REAUDIT-001/GLOBAL_TRANSFER_LEDGER_2026-08-25.md` before detailed day bundles/edges.

Hard current: 9/9 closed; Haidakhan 3 nights/2 quiet days; Hotel Evelyn A+; Kainchi Dham A+; Mahavatar Babaji Cave A+; YSS Dwarahat A full day/no overnight; Kakrighat A*/SKIP_FIRST; Dunagiri Retreat primary/Joshi fallback. CCI also protects less-visible item grades such as Naini Lake loop A+, historic Haidakhan cave A+, Bhumiadhar A, Hanuman Garhi/Maharajji-kuti A, Dunagiri Temple A, Babaji Smriti Bhavan A and Dhokaney Waterfall A.

## G. REQUIRED_BEFORE_TOUCHING_VARANASI / SARNATH
Read:
1. `runs/active/INDIA10-CLUSTER-COVERAGE-REAUDIT-001/VARANASI_DURATION_MARK_DECISION_2026-08-27.md`
2. `runs/active/INDIA10-CLUSTER-COVERAGE-REAUDIT-001/BHRIGU_BHADURY_A_PLUS_OPERATIONAL_CLOSURE_2026-08-27.md`
3. `runs/active/INDIA10-CLUSTER-COVERAGE-REAUDIT-001/A_PLUS_MARK_DECISION_LOG.md` for exact current A+/A/A*/B/C spine.
4. `runs/active/INDIA10-CLUSTER-COVERAGE-REAUDIT-001/SARNATH_VISIT_GUIDANCE_AND_UNESCO_LABEL_2026-08-27.md` before Sarnath day cards/UNESCO claims.
5. `runs/active/INDIA10-CLUSTER-COVERAGE-REAUDIT-001/VARANASI_HISTORICAL_PACE_PREFERENCE_RECOVERY_2026-08-27.md` before final sequencing.
6. `runs/active/VARANASI-GEO-DELIVERY-REPAIR-001/NUMBERING_REGISTRY.jsonl` when immutable 001–040 identity matters.

Geo warning: old delivered KML pins are not automatically safe. Before final maps/day-routing, reconcile CCI EXE-009..011 against the current map-verification gate. VNS-CAND-001 identity split is INDIA work; do not ask Mark to choose a coordinate.

## H. REQUIRED_BEFORE_TOUCHING_TIRUVANNAMALAI / ARUNACHALA
Read:
1. `runs/active/INDIA10-CLUSTER-COVERAGE-REAUDIT-001/TIRUVANNAMALAI_PREP_PACKET_2026-08-27.md`
2. `runs/active/INDIA10-CLUSTER-COVERAGE-REAUDIT-001/TIRUVANNAMALAI_DURATION_DECISION_SURFACE_2026-08-29.md` — current local duration surface.
3. `runs/active/INDIA10-CLUSTER-COVERAGE-REAUDIT-001/TIRUVANNAMALAI_4_NIGHT_TRIAL_EXECUTION_PRESENTATION_2026-08-30.md` — 4-night trial evidence, not a Mark lock.
4. `runs/active/INDIA10-CLUSTER-COVERAGE-REAUDIT-001/TIRUVANNAMALAI_SRI_RAMANASRAMAM_STAY_MODEL_2026-08-30.md` — current ashram stay/free-time model.
5. `runs/active/INDIA10-CLUSTER-COVERAGE-REAUDIT-001/TIRUVANNAMALAI_TRANSFER_MODE_CORRECTION_2026-08-30.md` — boot-failure transfer correction; rail-first re-evaluation required.
6. `governance/COORDINATE_INTEGRITY_GATE.md` — current duration-scale geo status.
7. `decisions/ARUNACHALA_TIRUVANNAMALAI_A_ANCHOR_2026-08-18.md` when parent/child provenance or Sri Aurobindo preference detail matters.
8. conditional A+ register when exact historical grade provenance is needed.

Hard recognition: Arunachala/Ramana world A+ parent; protected A children Sri Ramanasramam, Virupaksha Cave, Skandashram, Arunachaleswarar/Annamalaiyar Temple, Gurumurtam, Pavalakunru, full 14 km Giripradakshina/Girivalam; Sri Ramanasramam desired true ashram sleep #2 if accepted/available.

Current status: no duration locked. Five nights is still the clean local-content recommendation, but do NOT present the final 4/5/6 duration choice until the inbound/outbound edges are rebuilt rail-first and whole-human burden is compared against any flight alternative.

Do NOT fold Gingee/Mamallapuram/Puducherry/Sri Aurobindo into the fixed-A+-only duration arithmetic now. Preserve Mark's real Sri Aurobindo interest for the later southern optional/gateway review.

## I. REQUIRED_BEFORE_TOUCHING_DELHI
Read:
1. `runs/active/INDIA10-CLUSTER-COVERAGE-REAUDIT-001/DELHI_PREP_PACKET_2026-08-27.md`
2. current master/profile; conditional A+ register if exact grade provenance matters.

Hard: Nirmal Dham A+; bounded/quiet Delhi, no forced generic Old Delhi; Delhi Bhrigu only backup if Varanasi Bhrigu fails; duration open.

## J. REQUIRED_BEFORE_TOUCHING_AGRA / TAJ
Read:
1. `runs/active/INDIA10-CLUSTER-COVERAGE-REAUDIT-001/AGRA_PREP_PACKET_2026-08-27.md`
2. current master/profile; conditional A+ register if exact grade provenance matters.

Hard: Taj Mahal [UNESCO WH] A+; sunrise/earliest practical opening; old 1-night Taj-only baseline nonbinding; prepared open layer must be shown before duration closure; hotel still open.

## K. OPTIONAL WORLDS — LOAD ONLY AFTER FIXED-CORE BUDGET

### Braj / Mathura–Vrindavan–Govardhan
Not dropped, not mandatory, not A+ by inference. Load current/protected decisions + regional/traveler packets. Mandatory Neem Karoli Baba anti-forget: `decisions/NEEM_KAROLI_VRINDAVAN_RED_HOUSE_ROUTE_RULE_2026-08-29.md`. NKB Vrindavan Ashram + Mahasamadhi Mandir remains site-level A. Old coordinate registries conflict; reverify before map use.

### Haridwar / Kankhal / Rishikesh
Load current site decisions + regional freeze + traveler layer + CCI `OPN-012`/`EXE-044` context. Parmarth Niketan is experience only unless Mark explicitly chooses a sleep base. Anandamayi Ma Samadhi at Kankhal is an important existing A and a major content casualty if this optional world is dropped; show that trade-off explicitly. Recheck the 14 Jan 2027 Ardh Kumbh/Makar Sankranti signal live when this ballot is actually reached.

### Prayagraj
Load current decisions + regional/traveler layer. Direct Agra->Gaya overnight means Prayagraj is not route-required. Mandatory Neem Karoli Baba anti-forget: `decisions/NEEM_KAROLI_VRINDAVAN_RED_HOUSE_ROUTE_RULE_2026-08-29.md`. Red House / 4 Church Lane remains B / only if Prayagraj already happens / access confirmed / zero independent route weight.

## L. ROUTE / TRANSFER — CONDITIONAL
Use when route/global-edge work is active:
- `runs/active/INDIA10-CLUSTER-COVERAGE-REAUDIT-001/ROUTE_PLANNING_SYSTEM_CORRECTION_2026-08-25.md`
- `runs/active/INDIA10-CLUSTER-COVERAGE-REAUDIT-001/GLOBAL_TRANSFER_LEDGER_2026-08-25.md`
- `runs/active/INDIA10-CLUSTER-COVERAGE-REAUDIT-001/CLUSTER_TOPOLOGY_FEASIBILITY_2026-08-25.md`
- `runs/active/INDIA10-CLUSTER-COVERAGE-REAUDIT-001/CLUSTER_TOPOLOGY_QUANTIFIED_DELTA_2026-08-26.md`
- current fixed-A+-only route artifact(s) dated 2026-08-29 or later;
- for current south-edge work: `TIRUVANNAMALAI_TRANSFER_MODE_CORRECTION_2026-08-30.md` and the hard `train first` transport hierarchy.

Old exact V1/V2 calendars are provenance only. Full human transfer burden controls; raw vehicle time never equals occupied travel time. For the current Tiruvannamalai edges, rail must be tested first before flight+road can be recommended as a meaningful door-to-door win.

## M. BOOKING / LIVE LOGISTICS — CONDITIONAL
`runs/active/INDIA10-BOOKING-SEQUENCE-CLOSURE-001/BOOKING_ACTION_BOARD.md` = SEARCH_ONLY provenance/live-source lead. Old V2 dates/base choices are not current route truth.

Recheck at the proper stage: visa; Haidakhan acceptance; Dunagiri Retreat availability/winter operation; Hotel Evelyn; Sahi River View balcony; Sri Ramanasramam application/acceptance; Bhrigu provider process; trains/flights/opening/access; winter fog.

Durable booking wording guard from CCI: never ask a property to reserve “the Ram Dass room”; exact room is not proven.

## N. PERSON / EVIDENCE — CONDITIONAL
Apply as needed:
- `decisions/BABAJI_MYTHIC_FIGURE_EVIDENCE_RULE_2026-08-19.md`;
- `decisions/TOP11_SWEEP_DEPTH_BY_PERSON_2026-08-18.md`;
- `decisions/REVERSE_DISCOVERY_REOPEN_RULE_2026-08-19.md`;
- `governance/ANANDAMAYI_YOGANANDA_PHOTO_OVERRIDE_2026-08-20.md`;
- `decisions/NEEM_KAROLI_VRINDAVAN_RED_HOUSE_ROUTE_RULE_2026-08-29.md`.

Hard recovered personal guard: a physically resolved India location where Anandamayi Ma and Paramahansa Yogananda are documented together in a photograph must be surfaced as `MUST_VISIT_WITHIN_INCLUDED_CLUSTER` if that cluster is included; it does not by itself force an excluded macro-region.

Top-11 research-depth guard: full deep sweep specifically for Yogananda, Lahiri Mahasaya, Sri Yukteswar, Neem Karoli Baba, Ram Dass, Ramana Maharshi and Ramakrishna; Mahavatar Babaji was bundled with Lahiri/Sri Yukteswar; Anandamayi Ma already had broad treatment. Ramakrishna is personally underrepresented in Mark's view and a substantial route-logical Ramakrishna place is desired, without a hard detour obligation.

## O. SEARCH_ONLY / PROVENANCE
Never independently current unless explicitly re-adopted/reconciled:
- `governance/ACTIVE_STATE.md`;
- all `handoffs/*`;
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
7. keep `SUCCESSOR_SAFE_STATE.md` current and atomically aligned with CURRENT_STATE when both change;
8. every fresh successor writes a new `governance/boot_receipts/INDIA<N>__<NONCE>.json` (and may refresh `BOOT_SESSION_RECEIPT.md` as a pointer) only after complete 15/15 central + 6/6 CCI reads and before content;
9. before reply test: `IF THIS CHAT DIES NOW, CAN INDIA(N+1) RECOVER THIS FROM MASTER BOOT + THIS MAP WITHOUT MARK?`

**MAP-SYNC GUARD:** after every change to `INDIA_MASTER_BOOT.md` that adds/removes/changes a mandatory read, update section A of this map in the same execution cycle. After every frontier closure or material operational-frontier change, update section B and the relevant cluster section in the same execution cycle. A stale map is a successor-memory failure, not harmless documentation drift.

END CURRENT KNOWLEDGE MAP
