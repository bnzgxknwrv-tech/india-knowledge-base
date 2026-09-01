# CURRENT STATE — INDIA

state_revision: 2026-09-02_DELHI_LP_TRIAGE_FRONTIER_CORRECTION
branch: `agent/india8-cluster-casting`
status: WAITING_MARK_DELHI_BROAD_LP_TRIAGE__OPTIONAL_WORLD_FRONTIER_RETRACTED
boot_authority: `governance/INDIA_MASTER_BOOT.md` + `governance/FRESH_SESSION_BOOT_GATE.md` + `governance/BOOT_MANIFEST_V8.json`
manifest_active_cluster: `DELHI_BROAD_LP_GENERAL_TRAVELER_TRIAGE`
detailed_handoff: `governance/INDIA14_TO_INDIA15_HANDOFF_2026-09-01.md`

## BOOT / SUCCESSOR ARCHITECTURE — CLOSED
Use the universal V8.2 protocol stored at `governance/INDIA14_START_AND_INDEPENDENT_CHECK.md`. Do not reopen boot architecture without a real failure.

Latest repository boot evidence before this correction:
- INDIA15 receipt `governance/boot_receipts/INDIA15__9WT6G2WTETWAC.json`: `boot_gate = PASS`;
- INDIA15 LIGHT-check artifact `governance/boot_checks/INDIA15_CHECK__9WT6G2WTETWAC.json`: `check_gate = PASS`, committed at `624cd60fdfefebd8e277fe9f3e33eb876be85a79`.

IMPORTANT RECONCILIATION: the LIGHT check and later crash-safe prose reflected the then-recorded frontier, but the underlying Delhi source files prove that the broad Delhi LP/general-traveler Layer-A triage was not actually complete. Newer direct source reconciliation therefore corrects that frontier without reopening boot architecture.

Any future fresh session must boot against the then-current HEAD and let V8.2 recompute CHECK eligibility from real blob SHAs. Never reuse a prior receipt/check as authorization for another fresh session and never infer LIGHT/FULL from a stale prose pointer.

## CORRECTION OF COMMIT `eab5aff` — HARD ANTI-REGRESSION
Commit `eab5affee9956b76c5be7d656bcdcb1957adcd79` (`INDIA15: crash-safe final checkpoint before context limit`) was **FACTUALLY WRONG ON ONE MATERIAL FRONTIER POINT**:
- it stated that the true LP/general-traveler layer for all six fixed worlds, including Delhi, was complete enough and that the next gate was `OPTIONAL_WORLD_SURVIVAL`;
- but the controlling Delhi reserve `runs/active/INDIA10-CLUSTER-COVERAGE-REAUDIT-001/DELHI_SPARE_DAY_LP_TOPX_LAYER_2026-08-31.md` is explicitly `PREPARED / ... / NO NEW GRADES` and contains many `[OPEN / NOT GRADED]` items that Mark has not triaged;
- `runs/active/INDIA10-CLUSTER-COVERAGE-REAUDIT-001/DELHI_TRAVELER_FOOD_CINEMA_FINAL_PASS_2026-09-01.md` explicitly says it **supplements** that broad controlling reserve and says `No item is graded here`.

Cause of the error: a **research-completeness supplement** was incorrectly treated as if it also completed **Mark-facing Layer-A triage / grading** of the controlling broad Delhi reserve.

HARD RULE FROM THIS CORRECTION:
`RESEARCH_COMPLETE_ENOUGH != LAYER_A_MARK_TRIAGE_COMPLETE`.
A later fine-detail or supplement file may not silently close OPEN/NOT_GRADED rows in its controlling source. Only explicit Mark triage/decision or an explicit authoritative supersession can do that.

## WHAT IS ACTUALLY COMPLETE
The following work remains valid and must not be discarded:
- the six fixed A+ worlds themselves are established;
- Kumaon traveler/LP integrity = PASS / strong;
- Varanasi/Sarnath traveler/LP integrity = PASS / strong;
- targeted traveler completeness repairs for Tiruvannamalai/Arunachala, Bodh Gaya/Gaya and Agra/Braj are complete enough as research;
- the Delhi broad traveler universe has been researched/prepared;
- the Delhi food/cinema/IMAX fine-detail supplement is complete enough as research;
- real fixed-core inter-core edge work and fixed-core budget work exist as planning artifacts;
- the optional-world comparison artifact exists as background research.

These later global artifacts are **NOT the current decision frontier** until Delhi's broad Layer-A OPEN rows are triaged and the canonical work order has been restored.

Controlling artifacts:
- meta-controller/work order: `runs/active/INDIA10-CLUSTER-COVERAGE-REAUDIT-001/TRIP_PLANNING_META_CONTROLLER_2026-08-26.md`
- traveler integrity audit: `runs/active/INDIA10-CLUSTER-COVERAGE-REAUDIT-001/TRAVELER_LAYER_INTEGRITY_AUDIT_2026-08-31.md`
- traveler repairs: `runs/active/INDIA10-CLUSTER-COVERAGE-REAUDIT-001/TRAVELER_LAYER_TARGETED_REPAIRS_2026-09-01.md`
- Delhi broad controlling traveler reserve: `runs/active/INDIA10-CLUSTER-COVERAGE-REAUDIT-001/DELHI_SPARE_DAY_LP_TOPX_LAYER_2026-08-31.md`
- Delhi food/cinema supplement: `runs/active/INDIA10-CLUSTER-COVERAGE-REAUDIT-001/DELHI_TRAVELER_FOOD_CINEMA_FINAL_PASS_2026-09-01.md`
- Delhi live triage tracking: `runs/active/INDIA10-CLUSTER-COVERAGE-REAUDIT-001/DELHI_BROAD_LP_MARK_TRIAGE_2026-09-02.md`
- fixed edges + budget background artifact: `runs/active/INDIA10-CLUSTER-COVERAGE-REAUDIT-001/FIXED_CORE_REAL_INTERCORE_EDGES_AND_34_DAY_BUDGET_2026-09-01.md`
- optional-world comparison background artifact: `runs/active/INDIA10-CLUSTER-COVERAGE-REAUDIT-001/OPTIONAL_WORLD_SURVIVAL_DECISION_READY_2026-09-01.md`

STRUCTURAL NOTE (2026-09-02, CCI): every active cluster/reserve/traveler-layer file that carries a `Status:` line now also carries an explicit `Controlling: YES/NO` field, stating whether that file's own completeness gates its cluster's Layer-A pass — the exact distinction this correction is about (`RESEARCH_COMPLETE_ENOUGH != LAYER_A_MARK_TRIAGE_COMPLETE`). `DELHI_SPARE_DAY_LP_TOPX_LAYER_2026-08-31.md` and `DELHI_BROAD_LP_MARK_TRIAGE_2026-09-02.md` are both `Controlling: YES`; the food/cinema supplement is `Controlling: NO`. See `runs/active/INDIA10-CLUSTER-COVERAGE-REAUDIT-001/DELHI_FILE_INDEX.md` (and the equivalent `*_FILE_INDEX.md` for Agra, Bodh Gaya/Gaya, Tiruvannamalai, Varanasi, Kumaon) for a short per-cluster map of current vs superseded files. Full detail: PR #23 comment `CCI_RESULT — REPO STRUCTURAL HEALTH: CONTROLLING-FLAG + CLUSTER INDEX`. This is purely a structural/organizational addition — it changed no grade, hotel, route or duration and does not affect the content correction above.

## CANONICAL WORK ORDER — RESTORED
`FIXED CORE CONTENT/CANON -> FULL RELEVANT SOURCE VISIBILITY -> LAYER-A TRIAGE -> EXECUTION GEOMETRY -> MARK PACE/DWELL -> DURATION_CLOSED x6 -> REAL INTER-CORE EDGES -> FIXED_CORE_34_DAY_BUDGET -> OPTIONAL WORLD SURVIVAL -> FINAL TOPOLOGY -> LIVE LOGISTICS -> EXACT CALENDAR -> FINAL COMFORT SWEEP / DAY CARDS`.

The project may possess later-stage research artifacts created in advance, but they do not move the live frontier past an unresolved earlier gate.

## SIX FIXED A+ WORLDS — CURRENT STATUS
1. **Delhi** — inclusion fixed via Nirmal Dham [A+], but the **broad LP/general-traveler Layer-A reserve is NOT fully triaged by Mark**. Minimal fixed-core assumptions and existing B decisions remain historical/current decisions where explicitly locked, but they do not erase the remaining OPEN/NOT_GRADED traveler rows.
2. **Kumaon** — 9 occupied days / 9 nights through final Dunagiri night. Haidakhan Vishwa Mahadham/Ashram 3 nights / 2 full quiet days LOCKED_BY_MARK. Traveler layer PASS/strong.
3. **Agra / Taj Mahal** — Taj Mahal [A+] [UNESCO WH] only; one Agra hotel night LOCKED_BY_MARK. Targeted traveler completeness repair exists; rejected/dropped Agra sightseeing stays rejected unless Mark explicitly reopens it.
4. **Bodh Gaya / Gaya** — Maya Heritage LOCKED_BY_MARK; 2 hotel nights default under useful early inbound, 3 only late/disrupted/consciously deeper; max 3. Targeted traveler completeness repair exists.
5. **Varanasi / Sarnath** — 8 occupied days / 8 nights; Sahi River View Guesthouse, Assi Ghat LOCKED_BY_MARK. Traveler layer PASS/strong.
6. **Tiruvannamalai / Arunachala** — 5 nights LOCKED_BY_MARK. Targeted traveler completeness repair exists; old additional local LP layer remains DROPPED_BY_MARK.

## DELHI BROAD LP / GENERAL-TRAVELER LAYER — CURRENT LIVE FRONTIER
Controlling file:
`runs/active/INDIA10-CLUSTER-COVERAGE-REAUDIT-001/DELHI_SPARE_DAY_LP_TOPX_LAYER_2026-08-31.md`

Its status is `PREPARED / ON-SITE OPTIONAL / ZERO GUARANTEED DAY-NIGHT WEIGHT / NO NEW GRADES`.
It contains many `[OPEN / NOT GRADED]` rows, including major general-traveler categories such as Red Fort, Qutb Minar, Lodhi Colony/Lodhi Garden, Sunder Nursery, Hauz Khas Village, Lotus Temple, Jantar Mantar, museum layer, markets, unusual attractions and others.

Supplement:
`runs/active/INDIA10-CLUSTER-COVERAGE-REAUDIT-001/DELHI_TRAVELER_FOOD_CINEMA_FINAL_PASS_2026-09-01.md`

That file explicitly supplements the controlling broad reserve and explicitly says `No item is graded here`. Its food/cinema rows therefore remain inputs to the Delhi triage rather than proof that Delhi triage is complete.

Existing explicit Mark grades/locks must be preserved during triage. Do not re-present already decided items as fresh choices. Only the still-OPEN rows require Mark judgment.

## OPTIONAL WORLD SURVIVAL — RETRACTED AS CURRENT FRONTIER
`runs/active/INDIA10-CLUSTER-COVERAGE-REAUDIT-001/OPTIONAL_WORLD_SURVIVAL_DECISION_READY_2026-09-01.md` remains useful background research, but **A/B/C/D/E are withdrawn as the current action**.

Do not ask Mark to allocate the optional-world envelope until the earlier Delhi broad LP/general-traveler Layer-A triage is actually closed and any consequent Delhi execution/pace implications are reconciled.

The existence of a current 28-night fixed-core budget / 5-night optional envelope is therefore a provisional later-stage accounting result, not the current decision gate.

## HUMAN PLANNING RULES — HARD
- recognition-rich full names + visible grades on every graded visit occurrence;
- maps whenever spatial relationships materially help;
- from -> to -> km -> human travel range -> mode -> rounded timing -> dwell;
- ordinary planning in 15/30-minute blocks; exact minutes only where externally fixed;
- no wake-up/get-out-of-bed/personal-routine micromanagement unless explicitly requested;
- fit-for-purpose GEO, no precision theatre;
- Mark decides subjective value/dwell/duration after objective execution surface is visible;
- side questions never cancel authorized underlying work; resume automatically;
- after each materially completed reconciliation/correction/decision, checkpoint it durably before moving on.

## EXACT FIRST SUBSTANTIVE ACTION — HARD
After any required boot/authorization for a future fresh controller, and after checking that no newer central authority supersedes this state:

**De eerste inhoudelijke actie is: presenteer de nog OPEN/NOT_GRADED items uit de brede controlerende Delhi LP/general-traveler reserve aan Mark voor triage, zonder reeds besliste Delhi-items opnieuw open te breken, omdat `runs/active/INDIA10-CLUSTER-COVERAGE-REAUDIT-001/DELHI_SPARE_DAY_LP_TOPX_LAYER_2026-08-31.md` die brede reserve controleert en nog ongegradeerde items bevat.**

`OWNER = MARK_TRIAGE_WITH_INDIA_DECISION_SUPPORT`.

WAITING_FOR_MARK:
Delhi broad LP/general-traveler OPEN-item triage. Not optional-world package selection.

## AFTER DELHI TRIAGE
Automatically:
1. record each material Mark grade/drop/keep decision + WHY durably;
2. reconcile Delhi Layer A against the controlling broad reserve + food/cinema supplement;
3. determine whether Delhi execution geometry or pace/dwell changes;
4. only when the earlier gates are genuinely closed, resume the canonical work order;
5. revalidate later fixed-core budget / optional-world artifacts against any changed Delhi truth before using them as decision surfaces.

## SUCCESSOR REPLACEABILITY RULE
Every material research result, Mark decision, WHY, supersession, next action and decision-relevant uncertainty must be durable and GitHub-routable before substantive reply.
Crash test: `IF THIS CHAT DIES NOW, CAN INDIA(N+1) CONTINUE FROM GITHUB WITHOUT MARK REPEATING OR RECONSTRUCTING ANYTHING?`

END CURRENT STATE