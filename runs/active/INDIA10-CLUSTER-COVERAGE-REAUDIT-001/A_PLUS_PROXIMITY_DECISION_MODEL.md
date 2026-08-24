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
Never display `Nirmal Dham` alone; use `Nirmal Dham (rustplaats/Mahasamadhi van Shri Mataji Nirmala Devi)`.
`kosten` / `gratis` are money-only terms; logistics use reistijd, extra reistijd, omweg, duur, loop-/rijtijd.

## TWO LEVELS
### A+ CLUSTER / FIXED TRAVEL WORLD
Current fixed core:
- Kumaon;
- Varanasi / Sarnath;
- Bodh Gaya / Gaya;
- Tiruvannamalai / Arunachala;
- Delhi, anchored by Nirmal Dham (rustplaats/Mahasamadhi van Shri Mataji Nirmala Devi);
- Agra / Taj Mahal.

### A+ LOCATION / EXPERIENCE
A place/experience intrinsically among the real reasons for the India journey, independent of convenience.

## PARENT-COMPLEX A+ INHERITANCE — HARD
Do not ask Mark to vote separately on every room/shrine/micro-site when a meaningful parent is already A+.
- SAME_PHYSICAL_SITE / SAME_COMPLEX / true PARENT_CHILD -> CHILD_A_PLUS.
- Rooms, shrines, courtyards, rocks, bridge spots and other on-compound details stay nested.
- A nearby distinct site may be auto-bundled if genuinely walkable/natural and not a material separate excursion.
- A material drive/hike/river crossing remains a separate candidate.

Controlling examples:
- Kainchi Dham (Neem Karoli Baba-ashramcomplex): on-compound NKB/Ram Dass microsites inherit A+.
- Mahabodhi Temple Complex (Boeddha-verlichtingscomplex): Bodhi Tree/internal enlightenment microsites inherit A+; Sujata/Dungeshwari remain physically separate.
- Arunachala/Ramana sacred world: direct Ramana ashram/hill/local-life core is one A+ parent world; remote excursions remain visible.

## A+ CORRIDOR CAPTURE — GLOBAL HARD
Nearest-A+ distance alone is not enough. First connect the fixed A+ anchors/bases into realistic mandatory transfer corridors. Then test every old A/B/C, regional and traveler/LP finding against those corridors.

Required corridor classes:
1. `ON_CORRIDOR` — naturally passed during a transfer that must happen anyway.
2. `SMALL_TRANSFER_DETOUR` — short taxi/road/walk deviation from a mandatory transfer.
3. `ALTERNATIVE_CORRIDOR_BUNDLE` — a somewhat longer transfer route captures several meaningful sites together without requiring a new sleep module.
4. `TRUE_SIDE_EXCURSION` — materially separate out-and-back / half-day / full-day beyond the mandatory transfer.
5. `OFF_CORRIDOR_DROP` — practically poor fit and insufficient intrinsic importance to justify reopening time/route.

For each candidate show:
- corridor `FROM A+ -> TO A+`;
- mandatory baseline transfer without candidate;
- extra road/walk time caused by candidate;
- visit time separately;
- taxi/driver capture practicality;
- other sites bundled into same deviation;
- whether it changes only a transfer day or creates a separate half/full day/night.

`DROPPED MODULE != DROPPED SITE`.
A place that once looked awkward may remain A because it becomes a very easy corridor catch. Conversely an old A may become C if it is a genuine side excursion and no longer deserves the time.

## CORRIDOR TRIAGE — HARD ORDER
To reduce Mark's decision burden, INDIA reviews candidates in this order:

### 1. HARD PRACTICAL CUTS FIRST
Identify candidates that are clearly `TRUE_SIDE_EXCURSION` or `OFF_CORRIDOR_DROP` and whose intrinsic importance does not approach A+.
Present these first with a hard recommendation to cut. Mark alone confirms C.

### 2. EASY CAPTURES SECOND
Identify `ON_CORRIDOR` and `SMALL_TRANSFER_DETOUR` sites that Mark already liked. These get strong retention advice because the incremental burden is low.

### 3. BUNDLED ALTERNATIVE CORRIDORS THIRD
Only then compare route variants that capture multiple worthwhile places together. Judge the whole bundle against the extra transfer time, never each site as if it created a separate day.

### 4. TRUE SUBJECTIVE TIES LAST
Only the remaining genuinely balanced cases go back to Mark for difficult choice.

## WORKING LOGISTICS BANDS — ADVISORY, NOT AUTOMATIC GRADES
These are planning bands, not replacement for judgement and not automatic A/B/C rules:
- about 0–15 min extra driving/walking: near-zero corridor friction;
- about 15–30 min extra: easy catch;
- about 30–90 min extra: plausible bundle / transfer-day enrichment;
- about 90–150 min extra: meaningful route conversion; retain only if several strong sites are captured or one site matters a lot;
- over about 150 min extra or a standalone half/full day: true excursion; default hard-cut recommendation unless intrinsic importance is near A+.
Mountain roads, access windows, ferries, traffic and winter conditions override these bands when needed.

## DECISION ORDER — HARD
1. Discovery complete enough: person/AOAY + regional + traveler/LP + world-magnet universes exist.
2. Fixed core cluster set locked for this costing phase.
3. FIRST A+ PASS: Mark confirms parent/anchor A+; INDIA applies parent inheritance.
4. OLD-A PROMOTION / CORRIDOR PASS: build A+ corridors first; then hard cuts -> easy catches -> bundled alternatives -> true ties.
5. Resolve physical identity/coordinate confidence for selected A+ parents/anchors and corridor-critical candidates.
6. Overlay every remaining old A/B/C, regional candidate and traveler/Lonely-Planet finding against BOTH nearest/relevant A+ AND the A+ transfer corridors.
7. Only then Mark re-rates ordinary A/B/C.
8. Build realistic complete-execution schedule for fixed cluster.
9. Derive true minimum duration/nights.
10. Repeat through fixed core clusters.
11. After fixed-core footprint, evaluate route-sensitive/reserve clusters.
12. Global route / quarter-hour itinerary last.

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
`KUMAON_A_PLUS_CORRIDOR_MATRIX.md` showed why this method matters:
- Kakrighat (Vivekananda-realisatieplek aan de Kosi) looked weak when judged as an isolated Almora-side point, but becomes a strong retained A as a small detour on Kainchi -> Kukuchina/Babaji transfer.
- Jageshwar, Ramakrishna Kutir, Chitai, Turiya Niwas and Bodh Ashram were explicitly changed by Mark to C once corridor/time reality was shown.
Latest decision source: `KUMAON_CORRIDOR_MARK_DECISION_2026-08-24.md`.

## PROVENANCE
Existing A/B/C and locks remain visible provenance. Mark may supersede them in this reevaluation; workers/INDIA may not silently alter grades.

## CURRENT CONSEQUENCE
Do not present child-site ballot lists. Do not present isolated distance lists. Do not make Mark reconstruct geography. Present corridor-aware decision cards, starting with hard practical cuts.