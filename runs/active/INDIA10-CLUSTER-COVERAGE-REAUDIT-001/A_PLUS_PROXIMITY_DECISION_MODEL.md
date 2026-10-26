# INDIA — A+ / A / A* / B / C / PROXIMITY DECISION MODEL

status: ACTIVE_MARK_DECISION_RULE
updated: 2026-08-29
central_branch: agent/india8-cluster-casting

## PURPOSE
Define the current grade semantics and how selected/conditional content is used in corridor and day planning. Only Mark assigns or changes subjective A+, A, A*, B or C grades.

## HARD USER-FACING FORMAT
Every non-obvious location is shown as:
`CLUSTER / PLAATS / PLEK (korte Nederlandse uitleg) — huidige status: A+ / A / A* / B / C / OPEN`.
Never rely on Mark remembering an Indian/local name.
`kosten` / `gratis` are money-only terms; logistics use reistijd, extra reistijd, omweg, duur, loop-/rijtijd.

## PROXIMITY BEFORE GRADE — ABSOLUTE HARD / MARK 2026-08-29
Mark cannot reasonably grade unfamiliar Indian places without understanding how far they are from the places he already wants to visit.

Therefore BEFORE asking for A+/A/A*/B/C on any actionable place, INDIA must show a compact **decision geometry**:
- km + conservative time from the selected hotel/base when relevant;
- km + conservative time from the nearest retained A+/A host;
- km + conservative time from the natural previous/next stop in the proposed combination;
- walking distance/time where realistic;
- likely taxi/auto/private-car requirement;
- logical combinations: `if you choose X, Y is only ~N km / ~N min further, so it is cheap to combine`;
- full excursion burden when the place creates a half/full day;
- inbound/outbound corridor fit and net extra km/minutes when non-local.

Published/map minimum travel time is NOT copied blindly into planning. Use a conservative operational class: e.g. a map estimate of 11 minutes may be presented as ~15 minutes planning time. Add access/parking/walking/queue friction separately where material.

This is fundamental to subjective grading, not post-grade logistics. A place that sounds like B may become A when it is nearly free beside an A+; an attractive A may become A*/C in Mark's judgment when it requires a separate day. INDIA must expose that geometry before Mark is asked to decide.

## GRADE SEMANTICS — ABSOLUTE HARD / LATEST MARK

### A+
A+ = **trip-defining**.
- The place/world itself is a reason the trip routes there.
- A+ can carry a cluster and may justify major routing burden.
- Existing A+ is never reopened without a real material delta.

### A
A = **Mark definitely wants to visit this inside a retained world/cluster**.
- A is intrinsic selected content: Mark wants it for itself.
- A is planned/retained.
- An A alone does NOT make an otherwise optional whole cluster mandatory.
- If actual burden is unexpectedly disproportionate, INDIA must show the trade-off immediately; only Mark may downgrade/remove it.

### A*
A* = **host-dependent corridor/bycatch — SKIP_FIRST — NOT intrinsic A**.
- A* exists because an already-retained A+ or A route/day brings Mark there or makes it essentially natural to capture.
- It is NOT evidence that Mark independently wants to route for the place.
- It belongs in the real plan only where its A+/A host geometry remains genuinely natural.
- If the host A+/A disappears or geometry ceases to be easy, the A* loses its operational reason unless Mark explicitly upgrades it.
- It may be dropped at any moment for delay, fatigue, weather, access, crowding or simple lack of interest.
- It cannot independently force a detour, dedicated half/full day, new base, extra night or schedule sacrifice.
- If a day overruns, A* is the first selected content to drop before intrinsic A/A+.
- User-facing display should make host dependence obvious.

### B
B = **ACTIVE CONDITIONAL / RESERVE**.
- B MUST remain visible in the real itinerary/day plan as an on-site option.
- It may be done when time, weather, visibility, energy or unexpectedly short visits make it attractive.
- B does NOT independently justify a dedicated extra night, major detour or route restructuring.
- B can become much more attractive when the distance matrix shows it is nearly free beside a retained A+/A; only Mark changes its grade.

### C
C = **definitive dropout for the active trip**.
- Remove from active itinerary, route, day bundles and future choice batches.
- Do not research/re-present it unless Mark explicitly reopens it.

### OPEN
OPEN = genuinely ungraded.
- Present only if it can materially affect actual day use or cluster survival.
- Exact duplicates inherit the newest Mark grade and are not re-ballotted.

## CLUSTER FORCE
- A+ can make a world trip-defining.
- A/A*/B inside an optional world do not automatically make that world mandatory.
- Multiple A rows do not automatically equal A+.
- A* cannot contribute independent cluster-force because it is host-dependent by definition.
- Optional worlds compete later on content value versus total marginal time burden after the six fixed A+ worlds are duration-closed.

## CURRENT FIXED A+ WORLDS
1. DELHI
2. KUMAON
3. AGRA / TAJ MAHAL
4. BODH GAYA / GAYA
5. VARANASI / SARNATH
6. TIRUVANNAMALAI / ARUNACHALA

Their inclusion is closed.

## PARENT-COMPLEX A+ INHERITANCE
Do not ask Mark to vote separately on every room/shrine/micro-site when a meaningful parent is already A+.
- SAME_PHYSICAL_SITE / SAME_COMPLEX / true PARENT_CHILD -> CHILD_A_PLUS where appropriate.
- Same-site micro-content stays nested.
- A materially separate drive/hike/river crossing remains separate content.

## CORRIDOR CLASSES
For selected/open content use:
1. `ON_CORRIDOR`
2. `SMALL_TRANSFER_DETOUR`
3. `ALTERNATIVE_CORRIDOR_BUNDLE`
4. `TRUE_SIDE_EXCURSION`
5. `OFF_CORRIDOR`

For each meaningful candidate/selected item distinguish:
- baseline transfer;
- added road/walk time;
- visit time;
- whether it creates a separate half/full day/night;
- whether it can be bundled with other selected content.

Straight-line distance never substitutes for route reality in mountains, across rivers, restricted zones or poor roads.

## GRADE-SENSITIVE EXECUTION ORDER
1. C — remove from active planning.
2. A+ — protect; route around it.
3. A — place into a real day, but surface disproportionate burden if discovered.
4. A* — place only as a host-dependent natural bycatch; explicitly SKIP_FIRST.
5. B — show as a conditional on-site/day option; never let it force major burden.
6. OPEN — resolve only genuine day-changing survivors after decision geometry is shown.

## DECISION / PLANNING ORDER
`DISCOVERY -> A+ -> OLD-A PROMOTION -> A+-CENTRIC GEO/CORRIDOR -> PROXIMITY MATRIX -> A/A*/B/C -> COMPLETE FIXED-CLUSTER EXECUTION -> MARK PACE/DWELL -> DURATION_CLOSED -> REPEAT SIX -> FIXED_CORE_34_DAY_BUDGET -> OPTIONAL CLUSTER SURVIVAL -> FINAL TOPOLOGY -> EXACT CALENDAR`.

The active master controller is:
`TRIP_PLANNING_META_CONTROLLER_2026-08-26.md`.
If this file and an older route/corridor artifact conflict, this latest grade model + newest explicit Mark decision + active meta-controller control.

## PROVENANCE
Old grades/locks remain historical evidence. Only a newer explicit Mark decision supersedes them; workers/INDIA may not silently mutate grades.

Latest proximity clarification provenance:
- Mark 2026-08-29: underlinge afstanden are an essential precondition for meaningful grading; logical combinations must be actively proposed; conservative travel times must be used.
- Bodh Gaya correction 2026-08-29: Brahmakund was not wanted as a dedicated Rajgir day; only if naturally on-route/nearby. This exposed the failure of grading/presentation without full burden.

END_OF_MODEL