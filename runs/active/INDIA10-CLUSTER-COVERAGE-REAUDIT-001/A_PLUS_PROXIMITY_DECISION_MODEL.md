# INDIA10 A+ / PROXIMITY / CORRIDOR DECISION MODEL

status: ACTIVE_MARK_REEVALUATION_RULE
updated: 2026-08-24
central_branch: agent/india8-cluster-casting

## PURPOSE
Ordinary A/B/C cannot be judged responsibly before the intrinsically non-negotiable A+ anchors are identified and the practical geometry between those anchors is known.
Only Mark assigns A+, A, B or C. INDIA must do the geography, bundling, corridor and time reasoning first so Mark is never asked to infer where places lie.

## HARD USER-FACING FORMAT
Every non-obvious location is shown as:
`CLUSTER / PLAATS / PLEK (korte Nederlandse uitleg) — huidige status: A+ / A / B / C / OPEN`.
Never rely on Mark remembering an Indian/local name.
`kosten` / `gratis` are money-only terms; logistics use reistijd, extra reistijd, omweg, duur, loop-/rijtijd.

## GRADE SEMANTICS — ABSOLUTE HARD / MARK 2026-08-24
### A+
A+ means: **this is why Mark is making this India journey**. It is a core location/experience. There is zero substantive debate about whether to include it. The route must bend for it; extra driving, a dedicated excursion or an otherwise awkward routing does not by itself threaten A+.

### A
A means: **Mark very much wants to visit this as well**. Often he only learned about it through the project, but it is a real intended visit, not a spare-time option.
- Default = PLAN / RETAIN.
- An A may be brought back for discussion only when the actual geometry or the experience itself creates disproportionate burden: e.g. very large detour, major isolated side trip, unusually long visit requirement, extra night(s), or a material collision with stronger trip priorities.
- Distance/time is therefore a challenge trigger, NOT an automatic downgrade rule.
- INDIA must explicitly show `what we gain vs what extra burden this A causes` before recommending that an A be reconsidered.

### B
B means: **not a planned destination in normal execution**.
- Only consider it if Mark is already there, the site is an almost frictionless add-on, a schedule unexpectedly has spare time, or the route accidentally puts him next to it.
- A B must never independently steer a route, create a taxi outing, create a half-day, or cause an extra night.
- In practice many B sites will never be visited, and that is expected.

### C
C means: **NIET heen**.
- Do not plan it, route for it, optimize for it, or re-present it unless Mark explicitly reopens it.

### OPEN traveler/regional candidates
OPEN means Mark has not graded it yet.
- INDIA may recommend A/B/C, but must use the semantics above rather than treating `interesting` as A.
- A recommendation means `this is strong enough that Mark may genuinely want to plan it`.
- B means `worth knowing only as accidental/easy bycatch`.
- C means `do not spend trip time on it`.

## TWO LEVELS
### A+ CLUSTER / FIXED TRAVEL WORLD
Current fixed core:
- Kumaon;
- Varanasi / Sarnath;
- Bodh Gaya / Gaya;
- Tiruvannamalai / Arunachala;
- Delhi;
- Agra / Taj Mahal.

### A+ LOCATION / EXPERIENCE
A place/experience intrinsically among the real reasons for the India journey, independent of convenience.

## PARENT-COMPLEX A+ INHERITANCE — HARD
Do not ask Mark to vote separately on every room/shrine/micro-site when a meaningful parent is already A+.
- SAME_PHYSICAL_SITE / SAME_COMPLEX / true PARENT_CHILD -> CHILD_A_PLUS.
- Rooms, shrines, courtyards, rocks, bridge spots and other on-compound details stay nested.
- A nearby distinct site may be auto-bundled if genuinely walkable/natural and not a material separate excursion.
- A material drive/hike/river crossing remains a separate candidate.

## A+ CORRIDOR CAPTURE — GLOBAL HARD
Nearest-A+ distance alone is not enough. First connect the fixed A+ anchors/bases into realistic mandatory transfer corridors. Then test every old A/B/C, regional and traveler/LP finding against those corridors.

Required corridor classes:
1. `ON_CORRIDOR` — naturally passed during a transfer that must happen anyway.
2. `SMALL_TRANSFER_DETOUR` — short taxi/road/walk deviation from a mandatory transfer.
3. `ALTERNATIVE_CORRIDOR_BUNDLE` — a somewhat longer transfer route captures several meaningful sites together without requiring a new sleep module.
4. `TRUE_SIDE_EXCURSION` — materially separate out-and-back / half-day / full-day beyond the mandatory transfer.
5. `OFF_CORRIDOR_DROP` — practically poor fit for an OPEN/B-level candidate; never auto-apply this to A+ and do not silently apply it to an existing A.

For each candidate show:
- corridor `FROM A+ -> TO A+`;
- mandatory baseline transfer without candidate;
- extra road/walk time caused by candidate;
- visit time separately;
- taxi/driver capture practicality;
- other sites bundled into same deviation;
- whether it changes only a transfer day or creates a separate half/full day/night.

`DROPPED MODULE != DROPPED SITE`.
A wanted A can survive a dropped module when a corridor makes it easy to capture. Kakrighat is the proof case.

## GRADE-SENSITIVE CORRIDOR TRIAGE — HARD ORDER
### 1. Existing C rows
Remove from active planning immediately.

### 2. Existing A+ rows
Protect absolutely. Solve the route around them.

### 3. Existing A rows
Assume retain. First identify easy captures and sensible bundles. Only surface an A for reconsideration when its real burden is clearly disproportionate. Never downgrade an A merely because another candidate is closer.

### 4. Existing B rows
Do not route for them. Attach only to already-planned days when friction is near zero and spare time exists.

### 5. OPEN regional/traveler/LP rows
First hard-cut obvious off-corridor/huge-time findings, then easy captures, then bundles, then genuine content choices. Mark grades only the survivors where a real choice remains.

## WORKING LOGISTICS BANDS — ADVISORY ONLY
These bands describe friction; they are NOT automatic grades and NEVER override A+:
- about 0–15 min extra driving/walking: near-zero corridor friction;
- about 15–30 min extra: easy catch;
- about 30–90 min extra: plausible transfer enrichment;
- about 90–150 min extra: meaningful route conversion;
- over about 150 min extra or a standalone half/full day: substantial excursion and a legitimate **discussion trigger for an existing A**, or strong C/B pressure for an OPEN candidate, depending on intrinsic value.
Extra nights, restrictive opening windows, long treks, permits, seasonal closure, and exhaustion may be more important than raw driving minutes.
Mountain roads, access windows, ferries, traffic and winter conditions override these bands when needed.

## DECISION ORDER — HARD
1. Discovery complete enough: person/AOAY + regional + traveler/LP + world-magnet universes exist.
2. Fixed core cluster set locked for this costing phase.
3. FIRST A+ PASS: Mark confirms parent/anchor A+; INDIA applies parent inheritance.
4. OLD-A PROMOTION / CORRIDOR PASS: build A+ corridors first; protect A+, assume A retain unless burden is disproportionate, keep B incidental, remove C.
5. Resolve physical identity/coordinate confidence for selected A+ parents/anchors and corridor-critical candidates.
6. Overlay every regional candidate and traveler/Lonely-Planet finding against BOTH nearest/relevant A+ AND the A+ transfer corridors.
7. Exact duplicates inherit latest Mark grade and are not re-ballotted.
8. For genuinely new OPEN rows: hard cuts -> easy captures -> bundled alternatives -> true ties.
9. Build realistic complete-execution schedule for fixed cluster.
10. Derive true minimum duration/nights.
11. Repeat through fixed core clusters.
12. After fixed-core footprint, evaluate route-sensitive/reserve clusters.
13. Global route / quarter-hour itinerary last.

## REQUIRED METRICS
Where feasible:
- nearest_A_plus
- distance_km
- travel_mode
- realistic_travel_time_one_way
- incremental_detour_time
- walkable_from_A_plus
- same_compound_or_parent
- natural_bundle
- isolated_from_all_A_plus
- coordinate_confidence
- corridor_from_A_plus
- corridor_to_A_plus
- corridor_class
- base_transfer_time
- added_transfer_time
- visit_time
- taxi_capture_practical
- additional_half_day_required
- additional_full_day_required
- additional_night_required

Straight-line distance never substitutes for route reality in mountains, across rivers, restricted zones or poor-road areas.

## CURRENT KUMAON PROOF OF METHOD
- KUMAON / KAKRIGHAT / Kakrighat (Kosi-rivierplek waar Vivekananda in 1890 een belangrijke realisatie had) looked awkward as an isolated Almora-side point, but became a retained A because it is a small transfer catch on the Kainchi -> Kukuchina/Babaji corridor.
- Other former Kumaon A rows were explicitly changed by Mark to C after their corridor/time reality was shown. That was a Mark decision, not an automatic distance threshold.

## PROVENANCE
Existing A/B/C and locks remain visible provenance. Mark may supersede them; workers/INDIA may not silently alter grades.

## CURRENT CONSEQUENCE
Do not present child-site ballot lists. Do not present isolated distance lists. Do not make Mark reconstruct geography. Present corridor-aware decision cards, while respecting the very different planning force of A+, A, B and C.