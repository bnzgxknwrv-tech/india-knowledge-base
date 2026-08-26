# INDIA — A+ / A / A* / B / C / PROXIMITY DECISION MODEL

status: ACTIVE_MARK_DECISION_RULE
updated: 2026-08-26
central_branch: agent/india8-cluster-casting

## PURPOSE
Define the current grade semantics and how selected/conditional content is used in corridor and day planning. Only Mark assigns or changes subjective A+, A, A*, B or C grades.

## HARD USER-FACING FORMAT
Every non-obvious location is shown as:
`CLUSTER / PLAATS / PLEK (korte Nederlandse uitleg) — huidige status: A+ / A / A* / B / C / OPEN`.
Never rely on Mark remembering an Indian/local name.
`kosten` / `gratis` are money-only terms; logistics use reistijd, extra reistijd, omweg, duur, loop-/rijtijd.

## GRADE SEMANTICS — ABSOLUTE HARD / LATEST MARK 2026-08-26

### A+
A+ = **trip-defining**.
- The place/world itself is a reason the trip routes there.
- A+ can carry a cluster and may justify major routing burden.
- Existing A+ is never reopened without a real material delta.

### A
A = **Mark definitely wants to visit this inside a retained world/cluster**.
- A is planned/retained.
- An A alone does NOT make an otherwise optional whole cluster mandatory.
- If actual burden is unexpectedly disproportionate, INDIA may show the trade-off, but only Mark may downgrade/remove it.

### A*
A* = **formal A, corridor/bycatch subtype — SKIP_FIRST**.
- It belongs in the real plan where geographically/logistically natural.
- It cannot independently force a detour, dedicated half/full day, new base or extra night.
- If a day overruns, A* is normally the first selected content to drop before A/A+.

### B
B = **ACTIVE CONDITIONAL / RESERVE**.
- B MUST remain visible in the real itinerary/day plan as an on-site option.
- It may be done when time, weather, visibility, energy or unexpectedly short visits make it attractive.
- B does NOT independently justify a dedicated extra night, major detour or route restructuring.
- B is therefore NOT equivalent to 'absent from the plan'. It is visible but conditional.

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
3. A — place into a real day.
4. A* — give a real natural slot, marked SKIP_FIRST.
5. B — show as a conditional on-site/day option; never let it force major burden.
6. OPEN — resolve only genuine day-changing survivors.

## DECISION / PLANNING ORDER
`DISCOVERY -> A+ -> OLD-A PROMOTION -> A+-CENTRIC GEO/CORRIDOR -> A/A*/B/C -> COMPLETE FIXED-CLUSTER EXECUTION -> MARK PACE/DWELL -> DURATION_CLOSED -> REPEAT SIX -> FIXED_CORE_34_DAY_BUDGET -> OPTIONAL CLUSTER SURVIVAL -> FINAL TOPOLOGY -> EXACT CALENDAR`.

The active master controller is:
`TRIP_PLANNING_META_CONTROLLER_2026-08-26.md`.
If this file and an older route/corridor artifact conflict, this latest grade model + newest explicit Mark decision + active meta-controller control.

## PROVENANCE
Old grades/locks remain historical evidence. Only a newer explicit Mark decision supersedes them; workers/INDIA may not silently mutate grades.

END_OF_MODEL