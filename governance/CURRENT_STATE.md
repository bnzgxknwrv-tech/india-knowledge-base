# CURRENT STATE — INDIA

Last updated: 2026-08-26
Branch: `agent/india8-cluster-casting`
Purpose: compact durable boot state. Old calendar sketches are provenance only.

## BOOT
Read in this order:
1. `README.md`
2. `governance/INDIA_REGIE_CRITICAL_BOOT_AND_NO_DEFERRAL_2026-08-23.md`
3. `governance/INDIA_SUCCESSOR_BOOT_PROTOCOL.md`
4. `governance/INDIA11_RECOVERY_POSTMORTEM_AND_MUST_READ_2026-08-26.md`
5. THIS file
6. `runs/active/INDIAZILVER-ENTITY-ID-PROXIMITY-BACKFILL-001/PROTECTED_CANON_BASELINE.csv`
7. current-frontier files listed below
8. PR #23 at start of major integration and directly before central write; no continuous polling.

Worker `COMPLETE` is not automatically central truth. Verify integration/adoption. A stale tracker also does not prove a worker is unfinished: inspect actual branch/output when heads moved. Use CCI lightly. STOP OPTIMIZING and return to the trip.

## INDIA11 RECOVERY GUARD — HARD
INDIA11 was not actually up-to-speed on several older but material Mark decisions/flow/dwell/base facts despite current-state boot. Mark had to recover them manually. The mandatory postmortem above records the concrete errors and recovery triggers.

Hard consequence:
- CURRENT_STATE is a compact pointer, NOT proof that no older user-specific dwell/base/pace/flow decision exists.
- If Mark says `we already decided this`, `zoek terug`, `je mist te veel`, or the current plan contradicts remembered flow, stop new conclusions and search historical decisions/commits/handoffs/PR evidence until the gap is resolved.
- Never claim project-wide readiness merely because the light boot completed.

## HARD PRESENTATION / DECISION RULES
Before any location, cluster, HOTEL, sleeping base or route item shown to Mark: `AL BESLIST?`.
Never re-offer existing A/B/C/A+/lock as a new choice.
Only Mark assigns/changes subjective A+/A/A*/B/C or hotel choices.

User-facing places use:
`CLUSTER / PLAATS / PLEK (korte Nederlandse uitleg) — huidige status: A+ / A / A* / B / C / OPEN`.
Every true Mark choice batch is ONE contiguous numbered block so Mark can answer `1 A, 2 B, 3 C`.

Sleeping-base display must not mutate lodging type. For an ashram sleep, make explicit that it is an ashramovernachting even if a generic `HOTEL`/sleep-base prefix is used.

## GRADE / CLUSTER SEMANTICS — HARD
Canonical definition:
`runs/active/INDIA10-CLUSTER-COVERAGE-REAUDIT-001/A_PLUS_PROXIMITY_DECISION_MODEL.md` plus latest Mark correction in `A_PLUS_MARK_DECISION_LOG.md`.

- A+ = trip-defining; intrinsic reason the trip goes there.
- A = Mark genuinely wants to visit; retain inside a retained world, but A alone does NOT make an otherwise-optional whole cluster trip-defining.
- A* = formal A corridor/base bycatch, SKIP_FIRST; never sole route-driver.
- B = ACTIVE CONDITIONAL / on-site reserve. B remains visible in the actual travel plan but cannot independently force a major detour, extra night or route restructuring.
- C = definitive active-trip reject. Remove from active plan/day combinations unless Mark explicitly reopens it.
- OPEN = ungraded.

## SIX FIXED A+ CORE WORLDS — AL BESLIST
1. DELHI
2. KUMAON
3. AGRA / TAJ MAHAL
4. BODH GAYA / GAYA
5. VARANASI / SARNATH
6. TIRUVANNAMALAI / ARUNACHALA

Their inclusion is fixed. Their obvious-parent A+ pass is complete and the preserved old-A -> A+ promotion pass is closed.
Current A+ / Mark grade truth:
`runs/active/INDIA10-CLUSTER-COVERAGE-REAUDIT-001/A_PLUS_MARK_DECISION_LOG.md`.

Important locks:
- `KUMAON / DUNAGIRI / HOTEL Dunagiri Retreat (gekozen spirituele wandelbasis bij de Mahavatar Babaji-grot) — accommodatie-status: LOCKED_BY_MARK`.
- `VARANASI / ASSI GHAT / HOTEL Sahi River View Guesthouse (gekozen verblijf aan/naast Assi Ghat) — accommodatie-status: LOCKED_BY_MARK`.
- `KUMAON / DWARAHAT / Yogoda Satsanga Sakha Ashram — Dwarahat (YSS-ashram in de Mahavatar Babaji/Kriya-regio) — huidige status: A` krijgt een FULL DAY. Mark is Ananda, niet YSS/SRF; geen YSS overnight.

Kumaon direction remains:
`HAIDAKHAN VISHWA MAHADHAM -> NAINITAL -> KAINCHI -> DWARAHAT -> DUNAGIRI/KUKUCHINA`.
Eastern Kumaon exit is FULL TRAVEL DAY class and must be counted exactly once in the global budget/adjacent edge.

## RECOVERED CONTROLLER FLOW — HARD
The original active decision model requires:
`DISCOVERY -> A+ -> OLD-A PROMOTION -> A+-CENTRIC CORRIDOR/TIME -> ORDINARY A/A*/B/C -> COMPLETE-EXECUTION PLAN PER FIXED CLUSTER -> TRUE DURATION/MINIMUM NIGHTS -> REPEAT ALL SIX -> INTER-CORE TRANSFERS -> FIXED-CORE 34-DAY BUDGET -> ONLY THEN OPTIONAL/ROUTE-SENSITIVE CLUSTERS -> GLOBAL ROUTE`.

The 2026-08-25 route-planning correction remains valid but does NOT supersede this fixed-core time-footprint gate. It adds honest door-to-door transfer accounting.

Therefore the current job is:
**determine how much of Mark's 34-day trip is consumed by the six fixed A+ worlds, their selected A/A*/B/traveler/LP/Komoot content, and mandatory inter-core travel.**

Canonical audit:
`runs/active/INDIA10-CLUSTER-COVERAGE-REAUDIT-001/FIXED_CORE_TIME_FOOTPRINT_AUDIT_2026-08-26.md`.

## FIXED-CORE DAY-ACCOUNTING RULE — HARD / MARK 2026-08-26
For cluster footprint budgeting, do NOT count only nights/on-site days and defer a known inbound journey as `later global`.

Use explicit edge charging:
- inbound occupied transfer from the known current predecessor is included in the cluster footprint being costed;
- internal base changes are included on their real occupied day;
- outbound edge remains visible and is assigned exactly once to the next cluster/global bridge so it cannot disappear or double-count.

For the current FIXED-CORE-ONLY Kumaon baseline, the current topology predecessor is **DELHI**. Haridwar/Rishikesh is optional/deferred and must not silently replace Delhi as predecessor. If that optional cluster later survives, calculate the delta/scenario then.

Current official/topology working relation for the exact true Haidakhan Vishwa Mahadham:
- Delhi -> Haidakhan Vishwa Mahadham: about **337 km / 8–9 h raw road journey** according to Haidakhandi Samaj; treat as a FULL OCCUPIED TRAVEL DAY once departure/loading/food/winter buffer/arrival are included.
- Older generic-Haidakhan shortcuts are not calendar-safe.

## KUMAON — CURRENT SELECTION CLOSED ENOUGH FOR EXECUTION / PACE REVIEW
Day-expanding OPEN survivor decisions are now closed in:
`runs/active/INDIA10-CLUSTER-COVERAGE-REAUDIT-001/KUMAON_FINAL_OPEN_SURVIVOR_MARK_DECISIONS_2026-08-26.md`.

Latest important Mark outcomes:
- Naina Peak / China Peak short forest walk — B; decide on site depending spare time/weather/visibility.
- Corbett/Dhikala — C.
- Pangot/Kilbury — C.
- Mukteshwar + Chauli ki Jali — C.
- Sattal–Chanfi specialist extra birding/hides — C; Sattal / Seven Lakes itself remains A*.
- Chhoti Haldwani heritage trail — C.
- Uttarayani Mela Bageshwar — C.
- Patal Bhuvaneshwar — C.

C items above are OUT of active planning. Do not re-present.

### HAIDAKHAN RECOVERED DWELL / SLEEP TRUTH
Historical DECISION-0001/handoff recovery established:
- sleep is **inside Haidakhan Vishwa Mahadham / Haidakhan Ashram itself**; no separate hotel property is implied;
- duration remains technically OPEN, but the preserved planner working hypothesis is **3 nights / 2 complete quiet days** because 2 nights provide only one full day;
- this 3-night value is NOT yet a final Mark duration lock, but it is the correct baseline and must not be silently compressed again.

### KUMAON ACTIVE EXECUTION DRAFT
Current draft:
`runs/active/INDIA10-CLUSTER-COVERAGE-REAUDIT-001/KUMAON_COMPLETE_EXECUTION_DRAFT_2026-08-26.md`.

Working sleep baseline:
- Haidakhan Vishwa Mahadham / Ashram: 3 nights / 2 full quiet days — working hypothesis.
- Nainital: 3 nights.
- HOTEL Dunagiri Retreat: 3 nights.
- Total: 9 Kumaon nights.

Current fixed-core day footprint must be expressed INCLUDING inbound from Delhi:
- **K0: DELHI -> HAIDAKHAN VISHWA MAHADHAM = full occupied travel day; night H1.**
- K1–K2: two full Haidakhan days; nights H2–H3.
- K3: Haidakhan -> Nainital with Sattal A* if practical; night N1.
- K4: Nainital local A+/A day; night N2.
- K5: Bhumiadhar + Kainchi A+ day; night N3.
- K6: Nainital -> Dhokaney A -> Kakrighat A* if practical -> Dwarahat/Dunagiri; night D1.
- K7: Mahavatar Babaji/Dunagiri pilgrimage day; night D2.
- K8: YSS Dwarahat FULL DAY; night D3.

Thus the current working Kumaon footprint through its final Dunagiri night is **9 occupied days / 9 nights**, not `8 internal days plus a travel day later`.

The eastern Dunagiri exit remains a mandatory FULL TRAVEL DAY edge and must be charged once when the next fixed-core connection is built. Do not omit it from the six-core 34-day total.

Kumaon true duration is still MARK_PACE_REVIEW_REQUIRED because only Mark can decide whether 3 Haidakhan nights / 2 complete days feels right.

## OTHER FIVE FIXED WORLDS
VARANASI/SARNATH, BODH GAYA/GAYA, TIRUVANNAMALAI/ARUNACHALA, DELHI and AGRA have fixed A+ and substantial prior canon/research, but no found current artifact closes every genuinely new traveler/LP row followed by a complete-execution plan and true duration/minimum-night result.

Therefore no honest fixed-core total day count exists yet.

## CURRENT FRONTIER — FIXED CORE FIRST
Do NOT assign exact calendar dates.
Do NOT compare Braj, Haridwar/Rishikesh or Prayagraj for inclusion yet.

Execute:
1. Finish Kumaon pace/duration review from the corrected 9-day/9-night working footprint including Delhi inbound.
2. Repeat selection closure + complete-execution/time budget for VARANASI/SARNATH, BODH GAYA/GAYA, TIRUVANNAMALAI/ARUNACHALA, DELHI and AGRA.
3. Combine those six footprints with every mandatory inter-core door-to-door edge exactly once into a `FIXED_CORE_34_DAY_BUDGET`.
4. Only after the remaining-day count is known compare optional clusters by marginal total burden: extra transfer occupancy + base change + selected dwell/visit time.

## ROUTE/TIME METHOD — STILL HARD
Old exact-date/day sketches are NON-AUTHORITATIVE because transfer time was not consistently charged.
Door-to-door includes packing/check-out/loading + access + station/airport buffer + transport + delay/fog/winter buffer + baggage/exit + next HOTEL transfer/check-in + food/rest + daylight/energy loss.

Useful transfer/topology evidence is preserved in:
- `ROUTE_PLANNING_SYSTEM_CORRECTION_2026-08-25.md`
- `GLOBAL_TRANSFER_LEDGER_2026-08-25.md`
- `CLUSTER_TOPOLOGY_FEASIBILITY_2026-08-25.md`
- North/East/South topology files.
Use it when building fixed-core execution and later optional marginal burden. Do not let topology substitute for unfinished content/time budgeting.

## OPTIONAL WORLDS — DEFERRED
- BRAJ / MATHURA–VRINDAVAN–GOVARDHAN: unresolved. Earlier false DROP was invalidated; Braj reconciliation/prep remains useful but is NOT current frontier.
- HARIDWAR / KANKHAL / RISHIKESH: unresolved; topology/event research preserved. Do not silently insert it before Kumaon while fixed-core footprint is being costed.
- PRAYAGRAJ: unresolved; topology/event research preserved.

No further optional-cluster ballot until fixed-core footprint is known.

## LATER P0 OPERATIONAL CLOSURES
- exact winter door-to-door handling for DELHI -> true Haidakhan Vishwa Mahadham; official base relation is already 337 km / 8–9h raw and sufficient to classify full travel day, but exact trip-day service/driver detail comes later;
- true Haidakhan Vishwa Mahadham -> Nainital road geometry: older shortcuts are source-conflicted and must be reclosed before exact timetable/day sequencing;
- HOTEL Dunagiri Retreat <-> YSS Dwarahat winter commute;
- Babaji cave hotel-walk track/safety;
- actual-date Dec 2026/Jan 2027 train/flight operations.
Close these when they materially affect the active fixed-core execution calculation or booking.

## REPLACEABILITY
If INDIA11 disappears, INDIA12 must read the mandatory INDIA11 recovery postmortem before this file. It resumes from the corrected Kumaon 9-day/9-night working footprint INCLUDING Delhi inbound, obtains only Mark's pace judgment on the Haidakhan 3-night hypothesis, then continues the other five fixed A+ worlds. It must NOT jump to Braj/Rishikesh/Prayagraj before the six-core 34-day footprint exists.