# INDIA COORDINATE INTEGRITY GATE

Status: **HARD / PROJECT-WIDE / GEOMETRY-DEPENDENT PLANNING GATE**
Effective: 2026-08-29
Owner rule: `governance/MAP_COORDINATE_VERIFICATION_RULE.md`

## PURPOSE
Coordinates/geometries are foundational planning data. A wrong physical location can corrupt:
- Mark's burden-sensitive A/B/C/A*/A+ judgment;
- `je bent er toch` combinations;
- sleep-base choice;
- road/walk burden;
- route order;
- transfer-day capture;
- occupied day/night count;
- final calendar.

Therefore an item may influence geography-dependent planning only after it passes:
`GEO_VERIFIED_FOR_DECISION = YES` at the fit-for-purpose scale defined in `MAP_COORDINATE_VERIFICATION_RULE.md`.

This gate does NOT reopen or delete Mark's subjective grades. It controls whether geography may be used to interpret/execute those grades.

## VERIFICATION OBJECTS
For every active planning item store/know as applicable:
- exact physical entity identity;
- physical type: POINT / SMALL_BUILDING / COMPOUND / LARGE_AREA / LINEAR_DISTRIBUTED;
- `ENTITY_LOCATION` evidence;
- `ROUTING_ACCESS_LOCATION` evidence only where site scale/access makes it materially necessary;
- same-name disambiguation;
- independent cross-check;
- geographic sanity check;
- `GEO_VERIFIED_FOR_DECISION = YES/NO`;
- planning scope for which that YES is valid.

## FIT-FOR-PURPOSE EXAMPLES
- A 100x100 m hotel whose correct building/property is secure can be GEO-verified for city/proximity planning without proving the exact front door. Doorway uncertainty of tens of metres is not a reason to call the whole hotel coordinate unverified.
- A 3x3 km park/reserve can have a perfectly verified site centroid but still fail routing geometry until the actual entrance/trailhead/parking point used by Mark is verified.
- A walled compound may be verified as an entity for cluster placement while requiring a separate public gate for exact door-to-door timing.

## CURRENT AUDIT STATUS — 2026-08-29

### BODH GAYA / GAYA CURRENT ACTIVE GEOMETRY
Status: **PARTIAL PASS / CORE DECISION GEOMETRY VERIFIED**.
Canonical registry:
`runs/active/INDIA10-CLUSTER-COVERAGE-REAUDIT-001/BODHGAYA_VERIFIED_MAP_COORDINATES_2026-08-29.md`

Passed for current decision-scale geometry:
- Mahabodhi Temple Complex + Bodhi Tree exact UNESCO property coordinate;
- Great Buddha Statue exact object;
- Sujata Stupa exact/cross-checked object;
- Dungeshwari / Mahakala Caves exact/cross-checked cave-temple object + official direction/distance sanity check;
- Rajgir Brahmakund exact official entity + exact Plus Code locator + locality sanity check;
- Vishwa Shanti Stupa exact/cross-checked hilltop object;
- Maya Heritage exact hotel/business/property identity/address is verified for sleep-base placement; do not demand irrelevant exact-door precision. A separate routing entrance is only needed later if pedestrian/vehicle approach side materially affects the day calculation.

Still to verify before geometry use if presented in a proximity/day card:
- any additional Bodh B/A* item not yet present in the verified registry must pass the same gate before its distance/route is used.

### VARANASI / SARNATH CURRENT GEOMETRY
Status: **RE-AUDIT REQUIRED BEFORE NEW GEOMETRY-DEPENDENT USE**.

Historical PR #23 explicitly reported a geo layer with only 5 CONFIRMED and 35 PROVISIONAL records, plus one item without a safe coordinate, one roughly 3 km source discrepancy, and the selected guesthouse without a verified Google Maps marker at that stage.

Consequence:
- Mark's existing grades, hotel lock and 8-night duration remain current unless a new material delta is proven;
- old provisional KML/pins may NOT be treated as automatically verified current geometry;
- before reusing pairwise distance, walking, `je bent er toch`, microcluster or exact day-routing claims, reverify the relevant retained points at fit-for-purpose scale;
- do not waste time demanding an exact hotel door if the correct small property/building can be independently located; do verify access separately if lanes/ghat access materially alter walking/vehicle timing.

### OTHER FIXED WORLDS
Current status at this gate's creation:
- KUMAON: **AUDIT REQUIRED BEFORE NEXT NEW/REUSED DECISION-RELEVANT GEOMETRY CLAIM** unless the exact involved points are already independently proven in a current verified registry/source.
- DELHI: **AUDIT REQUIRED BEFORE NEXT NEW/REUSED DECISION-RELEVANT GEOMETRY CLAIM**.
- AGRA / TAJ: **AUDIT REQUIRED BEFORE NEXT NEW/REUSED DECISION-RELEVANT GEOMETRY CLAIM**.
- TIRUVANNAMALAI / ARUNACHALA: **AUDIT REQUIRED BEFORE NEXT NEW/REUSED DECISION-RELEVANT GEOMETRY CLAIM**.

This is deliberately a gate, not a claim that those old locations are wrong. It means old coordinates are not grandfathered into decision evidence merely because they exist in Git history.

## PRIORITY ORDER FOR GEO RE-AUDIT
Do not verify every obscure historical C/provenance point first.

Verify in this order:
1. selected sleep bases/ashram bases;
2. A+ locations;
3. A locations;
4. B/A* items likely to affect proximity/bundling/corridor decisions;
5. transfer endpoints, stations, airports and route-critical entrances/trailheads;
6. only then lower-impact/provenance items when needed.

C items do not need geometry work unless Mark explicitly reopens them or their identity is needed for provenance QA.

## GEOMETRY QUARANTINE RULE
Until a point passes this gate:
- it may remain in content/history/grade canon;
- it may be described semantically;
- it may NOT be used to claim it is nearby/on-route/a detour/a natural bundle;
- it may NOT drive a new duration/night/base conclusion;
- it may NOT appear as authoritative decision pin on a map.

## CLOSED-DURATION SAFETY
A prior `DURATION_CLOSED` decision is not automatically reopened merely because some historical pins were provisional.

Before final topology/calendar use, reverify the geometry actually supporting that closed duration. If the audit finds no material change, retain the closed duration. If it finds a material burden delta, quantify the delta and present it as a genuine correction; only Mark changes subjective choices.

## SUCCESSOR REQUIREMENT
Every INDIA successor must understand:
- coordinate integrity is upstream of proximity and routing;
- verification is fit-for-purpose, not precision theatre;
- `ENTITY_LOCATION` and `ROUTING_ACCESS_LOCATION` are different concepts;
- no unsafe old coordinate is grandfathered into current planning;
- no harmless 30–100 m uncertainty inside a known small building/property should paralyse planning;
- large-area access can be decision-critical even when the area itself is perfectly identified.

END.