# INDIA11 — FIXED CORE TIME FOOTPRINT AUDIT — 2026-08-26

status: ACTIVE_FRONTIER_RESTORED__FIXED_CORE_FIRST
branch: agent/india8-cluster-casting

## MASTER META CONTROLLER
For the complete route-to-calendar sequence and definition-of-done gates, read first:
`runs/active/INDIA10-CLUSTER-COVERAGE-REAUDIT-001/TRIP_PLANNING_META_CONTROLLER_2026-08-26.md`.

This audit remains the fixed-core evidence/state layer; the meta controller is the higher-level process controller.

## PURPOSE
Restore the original controller logic after the 2026-08-25 travel-time correction caused the durable successor pointer to jump too early toward optional-cluster comparison.

Mark's current question is not yet which optional world to retain. First determine how much of the 34-day trip is consumed by the already-fixed A+ core worlds, including all selected A+/A/A* traveler/LP/Komoot content and honest door-to-door travel.

## CONTROLLING LOGIC RECOVERED
The active A+ model already requires this sequence:
`DISCOVERY -> A+ -> OLD-A PROMOTION -> A+-CENTRIC CORRIDOR/TIME -> ORDINARY A/A*/B/C -> COMPLETE-EXECUTION PLAN PER FIXED CLUSTER -> TRUE DURATION/MINIMUM NIGHTS -> REPEAT FOR ALL FIXED CORE -> ONLY THEN ROUTE-SENSITIVE/RESERVE CLUSTERS -> GLOBAL ROUTE`.

The later travel-time correction remains valid and adds the requirement that all inter-cluster and internal transfers consume honest door-to-door occupied time. It does NOT authorize skipping the fixed-core complete-execution/time-footprint gate.

## SIX FIXED A+ CORE WORLDS
1. DELHI
2. KUMAON
3. AGRA / TAJ MAHAL
4. BODH GAYA / GAYA
5. VARANASI / SARNATH
6. TIRUVANNAMALAI / ARUNACHALA

These six are already trip-defining. Their inclusion is not being reopened.

## GATE STATUS BY CORE WORLD

### KUMAON
- A+ parent/anchor pass: COMPLETE.
- preserved old-A -> A+ promotion pass: COMPLETE.
- corridor work: substantial and usable.
- Komoot/walk layer: substantial and usable.
- traveler/LP overlay: NOW CLOSED ENOUGH FOR EXECUTION after 2026-08-26 Mark decisions; see `KUMAON_FINAL_OPEN_SURVIVOR_MARK_DECISIONS_2026-08-26.md`.
- complete-execution schedule: ACTIVE DRAFT in `KUMAON_COMPLETE_EXECUTION_DRAFT_2026-08-26.md`.
- true duration/minimum nights: MARK PACE REVIEW REQUIRED.

Current working footprint through final Dunagiri night is 9 occupied days / 9 nights including the Delhi -> Haidakhan inbound day, with the eastbound Dunagiri exit kept visible as the next mandatory full-travel edge to charge exactly once later.

### VARANASI / SARNATH
- A+ parent/anchor pass: COMPLETE.
- preserved old-A promotion pass: COMPLETE.
- extensive protected A/B/C canon: COMPLETE.
- A+ corridor matrix: EXISTS.
- traveler/LP overlay: NOT FOUND AS CLOSED. Several exact duplicates already inherit A+ (e.g. Ganga Aarti, Ratneshwar child, Sarnath), but no final closure artifact for all genuinely new traveler rows was found.
- complete-execution schedule: NOT FOUND AS CLOSED CURRENT ARTIFACT.
- true duration/minimum nights: NOT FOUND AS CLOSED CURRENT ARTIFACT.

### BODH GAYA / GAYA
- A+ parent/anchor pass: COMPLETE.
- preserved old-A promotion pass: COMPLETE.
- protected A/B/C research/saturation: strong and accepted.
- A+ corridor matrix: EXISTS.
- traveler/LP overlay: NOT CLOSED. Dungeshwari duplicate inherits A+; Mahabodhi component inherits A+, while the separate international-monasteries traveler experience was explicitly left for later review.
- complete-execution schedule: NOT FOUND AS CLOSED CURRENT ARTIFACT.
- true duration/minimum nights: NOT FOUND AS CLOSED CURRENT ARTIFACT.

### TIRUVANNAMALAI / ARUNACHALA
- A+ parent/anchor pass: COMPLETE; Ramana/Arunachala sacred world is protected A+ parent.
- preserved old-A promotion: no remaining separate old-A question.
- traveler duplicate inheritance: partial (Girivalam, Arunachaleswarar, Skandashram/Virupaksha trail inherit A+).
- traveler/LP overlay for all genuinely new rows: NOT FOUND AS CLOSED.
- complete-execution schedule: NOT FOUND AS CLOSED CURRENT ARTIFACT.
- true duration/minimum nights: NOT FOUND AS CLOSED CURRENT ARTIFACT.

### DELHI
- A+ anchor pass: COMPLETE; Nirmal Dham A+.
- old-A promotion: no remaining old-A item in that pass.
- regional/traveler discovery exists.
- traveler/LP overlay: NOT FOUND AS CLOSED CURRENT ARTIFACT.
- complete-execution schedule: NOT FOUND AS CLOSED CURRENT ARTIFACT.
- true duration/minimum nights: NOT FOUND AS CLOSED CURRENT ARTIFACT.

### AGRA / TAJ MAHAL
- A+ anchor pass: COMPLETE; Taj Mahal A+ with earliest-practical-opening preference.
- old-A promotion: no remaining preserved old-A item.
- regional/traveler discovery exists.
- traveler/LP overlay: NOT CLOSED. Taj sunrise inherits A+; Taj moonlight viewing is explicitly a distinct experience still left for later content/scheduling review, and other genuinely new Agra traveler rows do not have a found global closure artifact.
- complete-execution schedule: NOT FOUND AS CLOSED CURRENT ARTIFACT.
- true duration/minimum nights: NOT FOUND AS CLOSED CURRENT ARTIFACT.

## ROOT CAUSE OF FRONTIER DRIFT
On 2026-08-25 INDIA10 correctly discovered that earlier calendar sketches undercharged travel time. It then built a global transfer ledger and topology feasibility layer. This repair was valuable.

However the successor state subsequently moved the active question to optional-cluster pressure tests before the pre-existing fixed-core traveler/LP overlay and complete-execution/time-footprint sequence had been finished. That was a sequencing drift, not a reason to discard the transfer research.

## CORRECT ACTIVE FRONTIER
Do NOT compare Braj, Haridwar/Rishikesh or Prayagraj for trip inclusion yet.
Do NOT build exact calendar dates yet.

Execute in this order:
1. Finish KUMAON execution geometry + Mark pace judgment from the corrected current draft; then mark Kumaon duration closed.
2. Repeat traveler/LP/regional/Komoot closure + complete-execution/time-budget process for VARANASI/SARNATH, BODH GAYA/GAYA, TIRUVANNAMALAI/ARUNACHALA, DELHI and AGRA.
3. Combine the six internal durations with the mandatory inter-core door-to-door transfer blocks into one `FIXED_CORE_34_DAY_BUDGET`.
4. Only then calculate how many of the 34 trip days remain and compare route-sensitive/optional worlds by total marginal burden: extra transfer occupancy + extra base change + their own selected dwell/visit days.
5. After optional survival, freeze final topology, recheck actual-date services/access and only then build exact calendar dates.

## OPTIONAL WORLDS — DEFERRED, NOT FORGOTTEN
- BRAJ / MATHURA–VRINDAVAN–GOVARDHAN: inclusion unresolved; earlier false DROP has been invalidated. Its new reconciliation/prep files are preserved but NOT the active frontier.
- HARIDWAR / KANKHAL / RISHIKESH: inclusion unresolved; topology evidence preserved.
- PRAYAGRAJ: inclusion unresolved; topology/event evidence preserved.

They wait until the fixed-core 34-day footprint exists.

## DECISION ECONOMY
Do not restart generic discovery. The traveler union already has 150 canonical records and the regional sweeps are integrated.
For each fixed core:
- deduplicate against current canon;
- remove inherited C/non-action rows;
- preserve already-decided A+/A/A*/B;
- present Mark only genuinely unresolved survivors whose inclusion materially changes actual day usage;
- then immediately build the cluster execution/duration once selection is closed.

## CURRENT FIRST MARK-DEPENDENT GATE
KUMAON is no longer blocked by generic content discovery. It is at EXECUTION/Mark-pace stage. Close only operational geometry that can materially change the day bundles, show the corrected complete Kumaon structure, obtain Mark's dwell/pace judgment, then freeze Kumaon duration.

END_OF_ARTIFACT