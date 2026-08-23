# INDIA10 A+ / PROXIMITY DECISION MODEL

status: ACTIVE_MARK_REEVALUATION_RULE
updated: 2026-08-23
central_branch: agent/india8-cluster-casting

## PURPOSE
Mark has clarified that ordinary A/B/C cannot be judged responsibly before the intrinsically non-negotiable or near-non-negotiable anchors are identified and the practical proximity of all other candidates to those anchors is known.

This file does not itself assign A+, A, B or C. Only Mark does that.

## A+ DEFINITION
A+ is a separate decision dimension from ordinary A/B/C.

A+ means: a place, experience or event that is intrinsically a major reason for Mark to want to visit that area / make this India journey, independent of convenience or nearby add-ons.

A+ may come from any discovery layer:
- AOAY / Top-11 / person sweep;
- regional/location sweep;
- Lonely-Planet/traveler/experience layer;
- world-magnet layer.

A+ DOES NOT mean the cluster is automatically included in the final trip. A cluster can contain one or more A+ items and still be dropped later because the complete cluster cannot be executed properly within the total trip.

## HARD TRAVEL QUALITY RULE
Mark prefers skipping an entire cluster rather than visiting a retained cluster hurriedly, incompletely, or by silently omitting important retained sites/experiences.

Therefore:
- no cluster survives merely because it has an A+;
- no cluster is compressed below a realistic complete-execution duration merely to force it into the route;
- final cluster survival is decided only after the cluster's complete realistic execution time is known.

## DECISION ORDER — HARD
1. Finish enough discovery to create the full candidate universe per cluster:
   - person/AOAY layer;
   - regional/location layer;
   - traveler/Lonely-Planet/experience layer;
   - adaptive world-magnet/out-of-radius layer;
   - visitability filter.
2. Mark identifies A+ items FIRST across all decision-relevant clusters.
3. For every other surfaced candidate, establish proximity/context relative to the nearest/relevant A+:
   - trustworthy coordinates / identity where possible;
   - straight-line distance as descriptive support only;
   - real walking/driving/boat travel time where meaningful;
   - incremental detour time from the likely A+ visit path / sleep base;
   - whether it naturally bundles with an A+ or requires a separate excursion;
   - isolation flag if far from all A+ and other retained items.
4. Only with that context does Mark re-rate ordinary A/B/C.
5. Build a realistic complete-execution schedule PER CLUSTER using all retained A/B and any required buffers/transfer reality. Do not yet force every cluster into one global trip.
6. Derive true minimum nights/time for each cluster.
7. Only then compare clusters against the total trip envelope and decide which clusters survive.
8. Build the global route / quarter-hour itinerary from surviving complete clusters.

## WHY ORDINARY A/B/C MUST WAIT FOR A+
A moderate candidate may rationally rise because it is essentially free to add to an A+ visit. Conversely, an old A may fall if it requires a large separate excursion and is not intrinsically strong enough to justify it.

Examples of the intended logic:
- pleasant waterfall 5 minutes from a heavy A+ -> may become A in context;
- same waterfall 90 minutes each way from all A+ -> may remain B/C;
- old A 100 km from every true A+ -> must be explicitly reconsidered rather than silently counted as cluster weight;
- world-class traveler experience can itself become A+ if Mark judges it a major trip reason.

## PROXIMITY METRIC — DO NOT USE KILOMETRES ALONE
The existing `PROXIMITY_1KM_3KM_MATRIX.csv` is useful foundation evidence, but the new decision model needs practical route cost.

Required context fields for Mark review where feasible:
- `nearest_A_plus`
- `distance_km`
- `travel_mode`
- `realistic_travel_time_one_way`
- `incremental_detour_time`
- `walkable_from_A_plus` YES/NO
- `same_compound_or_parent` YES/NO
- `natural_bundle` YES/MAYBE/NO
- `isolated_from_all_A_plus` YES/NO
- `coordinate_confidence`

Straight-line distance never substitutes for route reality in mountains, across rivers, restricted zones or poor-road areas.

## PROVENANCE
Existing A/B/C and locks remain preserved as old decisions and must be shown during re-rating. This authorized reevaluation round permits Mark to supersede them after the full discovery + A+ + proximity context is available. No worker or INDIA session may automatically alter them.

## RELATION TO KML/GEO WORK
Existing geo/proximity work is not discarded. Reuse and extend:
- `runs/active/INDIAZILVER-ENTITY-ID-PROXIMITY-BACKFILL-001/PROXIMITY_1KM_3KM_MATRIX.csv`
- protected trusted coordinates and coordinate-quality flags;
- prior KML/geo artifacts where provenance is sound.

New coordinate work should prioritize surfaced A+ candidates first, then candidates needed for contextual A/B/C review.

## CURRENT CONSEQUENCE
Do NOT ask Mark to do final ordinary A/B/C re-rating yet.
First complete the missing regional + multi-AI traveler discovery layers. Then present the union in manageable cluster slices for A+ selection. Only after A+ selection should proximity enrichment and final ordinary A/B/C review begin.
