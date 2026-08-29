# INDIA MAP / COORDINATE VERIFICATION RULE

Status: **HARD / UNIVERSAL / ALL INDIA GEOMETRY / ALL SUCCESSORS**
Effective: 2026-08-29
Hardened: 2026-08-29 — FIT-FOR-PURPOSE 100% GEO VERIFICATION
Trigger: Mark caught a materially wrong map pin for the Dungeshwari / Mahakala Caves, which made a distant Rajgir hot-spring cluster appear to lie on the route. This is a decision-corrupting failure class.

## CORE RULE — COORDINATES ARE FOUNDATIONAL PLANNING DATA
A location used in India planning may affect A/B/C/A*/A+ judgment, `je bent er toch` combinations, hotel choice, route order, day count, walking burden, transfers and night count. Therefore **geometry-dependent planning may not use a location until its physical position is GEO_VERIFIED_FOR_DECISION at the planning-relevant scale.**

A map shown to Mark is decision evidence. INDIA may NEVER render a decision-relevant map pin, route relationship, proximity claim or `je bent er toch` conclusion from an unverified/ambiguous geocoder result.

If the physical location is not sufficiently verified, the correct action is **NO PIN / NO GEOMETRY CONCLUSION**, not a guessed pin.

## WHAT “100% VERIFIED” MEANS — HARD MARK CLARIFICATION 2026-08-29
`100% GEO VERIFIED` does **NOT** mean fake centimetre/meter precision or knowing the exact front door of every building.

It means:
1. **ENTITY CERTAINTY = 100%:** the coordinate/footprint belongs to the exact intended physical place, not a same-name/different-place match;
2. **SCALE FIT = YES:** the positional uncertainty is small enough that it cannot materially change the planning decision being made;
3. **ACCESS FIT = YES WHEN NEEDED:** if the size/layout/access of the site can materially change route time, the actual usable entrance/trailhead/parking/jetty/gate must be separately verified for routing.

The operative flag is:
`GEO_VERIFIED_FOR_DECISION = YES`.

A point is not rejected merely because the exact doorway is unknown when the correct building/site is securely located and doorway uncertainty is irrelevant to the planning decision.

Conversely, a correct site centroid is NOT sufficient for routing to a large site if the usable access point could be kilometres away or on another side.

## ENTITY LOCATION VS ROUTING ACCESS — ALWAYS DISTINGUISH
Where useful store two different objects:
- `ENTITY_LOCATION` — where the physical place/site itself is;
- `ROUTING_ACCESS_LOCATION` — where Mark actually enters/parks/starts walking/boards/gets dropped off.

They may be identical for a small building. They may be very different for a large park, reserve, campus, mountain, riverfront or walled complex.

Do not turn an access-point uncertainty into a false claim that the whole building/site is geographically unverified. Do not turn a verified site centroid into a false claim that the route endpoint is known.

## FIT-FOR-PURPOSE VERIFICATION BY PHYSICAL TYPE

### A. POINT / SMALL OBJECT
Examples: statue, stupa, spring compound, individual cave entrance, small shrine.
Required for geometry use:
- exact intended object resolved;
- coordinate lies on/at the object/site;
- authoritative identity/location evidence where available;
- independent coordinate cross-check where practical;
- same-name trap excluded.

### B. SMALL BUILDING / HOTEL / SHOP / HOUSE
If the correct building/property is securely identified, a building footprint, rooftop point, verified business entity or verified address on that building is sufficient for cluster/proximity planning.

**Exact front door is NOT required** merely to call the hotel/building location verified when a 30–100 m entrance difference cannot alter the route decision.

Only verify a separate entrance if the approach side materially changes walking/driving access or the day plan.

### C. COMPOUND / TEMPLE / ASHRAM / CAMPUS
For city/cluster placement and gross proximity:
- correct compound footprint/location may be enough.

For door-to-door routing:
- verify the public gate/vehicle drop-off/visitor entrance separately **only if** the compound size, walls, one-way access or multiple roads can materially change travel/walk burden.

### D. LARGE PARK / FOREST / RESERVE / ARCHAEOLOGICAL FIELD / 3x3 KM-CLASS AREA
A centroid or generic park pin can identify the area but is **NOT automatically a routing endpoint**.

For route/day geometry verify the actual entrance, trailhead, parking, visitor centre, jetty or gate Mark will use. If several accesses are plausible, choose the operationally relevant one and document why.

### E. LINEAR / DISTRIBUTED FEATURE
Examples: long ghat frontage, pilgrimage circuit, ridge, trail, river walk.
Do not use an arbitrary midpoint for routing. Verify the start/end/access points that the proposed day actually uses, plus any critical interchange/junction where route geometry depends on it.

## DECISION-RELEVANT PRECISION — NO OVERPRECISION, NO UNDERPRECISION
Precision is **fit for purpose**.

A coordinate difference of tens of metres inside the same small hotel/building/compound is normally immaterial to A/B/C or day-count geometry.

A coordinate difference of kilometres, a same-name place in another locality, or the wrong side/access of a very large site is material and blocks geometry use.

Do not invent an arbitrary universal meter tolerance. Ask instead:
`COULD THE REMAINING POSITIONAL UNCERTAINTY CHANGE PROXIMITY CLASS, ROUTE, MODE, EXTRA TIME, DAY COUNT, NIGHT COUNT OR MARK'S BURDEN-SENSITIVE GRADE?`

- NO -> location may pass `GEO_VERIFIED_FOR_DECISION` for that planning purpose.
- YES -> verify the missing access/location detail before geometry use.

## REQUIRED VERIFICATION BEFORE ANY USER-FACING MAP OR GEOMETRY-DERIVED CHOICE
For every point that will influence the decision:
1. resolve the exact physical entity, not merely a similar place name;
2. classify the physical type above and required precision;
3. check an authoritative/first-party source for identity/location where available (government, UNESCO, ASI, official hotel/business address, etc.);
4. obtain coordinate/footprint from a reliable map/geodata source, business entity ref, verified plus code, official GIS, or equivalent;
5. cross-check against a second independent source where practical;
6. disambiguate same-name places explicitly;
7. run a geographic sanity check against known nearby anchors and expected direction/distance;
8. determine whether `ENTITY_LOCATION` alone is sufficient or whether a separate `ROUTING_ACCESS_LOCATION` is required;
9. set `GEO_VERIFIED_FOR_DECISION = YES` only when the remaining uncertainty cannot materially corrupt the decision;
10. only then calculate proximity, combination, route burden or render the point as decision evidence.

A name-only geocoder call is NOT verification.

## SOURCE-CONFLICT RULE
If two credible coordinate sources materially disagree:
- first determine whether they are simply different valid points on the same sufficiently small physical property;
- if yes and the difference cannot affect the current planning purpose, document it as immaterial rather than falsely blocking the location;
- if they may represent different entities, distant parts of a large site, or different access points, do not average them;
- do not pick whichever gives the nicer route;
- classify `MAP_COORDINATE_UNRESOLVED` or `ROUTING_ACCESS_UNRESOLVED` as appropriate;
- research until the exact physical entity/access is resolved;
- if still unresolved, omit that geometry from decision use and tell Mark exactly why.

This preserves the earlier Varanasi precedent from PR #23: genuinely unsafe geometry remains without a point rather than receiving a guessed point — while avoiding the opposite error of demanding irrelevant doorway-level precision for a known small building.

## ROUTE / PROXIMITY RULE
Correct entity locations alone are not enough for route advice.

Before saying `langs de route`, `5 min verder`, `je bent er toch`, `omweg` or similar:
- verify both relevant entity locations;
- verify routing access point(s) when site scale/access matters;
- use actual road/walk route evidence for movement claims, not straight-line visual inference;
- compare baseline route vs route via candidate when the claim can change Mark's grade or day count;
- use conservative operational time, not optimistic map minimum;
- sanity-check that the route direction is geographically plausible.

A map pin may support orientation; it may not substitute for routing evidence.

## PROJECT-WIDE GEOMETRY GATE
Existing A+/A/A*/B/C decisions are NOT automatically invalidated by old coordinate uncertainty; those remain Mark decisions.

But any **new or reused geography-dependent conclusion** — including proximity, bundle, A* host-fit, `je bent er toch`, hotel geometry, route order, transfer capture, driving/walking time or duration rationale — must pass this rule first.

Old `PROVISIONAL` coordinates may remain provenance but may not silently become current decision geometry.

If a previously closed duration materially relied on unsafe coordinates, re-audit the affected geometry before reusing that duration in final route/calendar work. Do not silently mutate the duration; surface only a material delta if verification changes the burden.

## MAP RENDERING PREFERENCE
For decision-relevant maps prefer, in order:
1. verified structured business/place ref when it is the exact entity;
2. exact verified latitude/longitude or footprint point appropriate to physical type;
3. sufficiently precise verified address when coordinates are not manually supplied.

Never invent a precise street address.

## USER-FACING CONFIDENCE
When a map materially supports a decision, INDIA should be able to state the basis compactly:
- `GEO VERIFIED FOR DECISION — OFFICIAL + COORDINATE CROSS-CHECKED`;
- `GEO VERIFIED FOR DECISION — VERIFIED BUILDING/BUSINESS ENTITY`;
- `ENTITY VERIFIED / ROUTING ACCESS VERIFIED` when those are separate;
- or `PROVISIONAL — NOT USED FOR GEOMETRY DECISION`.

No unresolved decision-critical geometry may be presented as authoritative.

## PRE-SEND / PRE-CALCULATION GEO VETO
Before every user-facing India map **and before every proximity/route calculation that can affect a choice**, ask:
- Is every location the exact intended physical entity?
- Is its verification precision fit for the physical size/type and current planning decision?
- Am I accidentally demanding irrelevant exact-door precision for a known small property?
- Am I accidentally using a centroid for a large site where the real entrance matters?
- Did I check for same-name traps?
- Do distances/directions pass a sanity test?
- If I make a route/proximity statement, do I have actual movement evidence rather than visual map inference?
- Would any remaining positional/access uncertainty plausibly change Mark's grade, combination, route, day count or night count?

Any unsafe YES/NO outcome = do not use that geometry yet.

## FAILURE RECOVERY
If Mark spots a map/coordinate inconsistency:
1. stop all dependent geography conclusions immediately;
2. reverify every decision-relevant point in that presented geometry, not only the point Mark noticed;
3. invalidate route/proximity conclusions derived from the bad geometry until recalculated;
4. create/update a verified coordinate registry for the active cluster when repeated map use is expected;
5. inspect whether the same failure class exists elsewhere in current planning artifacts;
6. record the failure and strengthened rule in living governance so later INDIA versions do not repeat it.

## ABSOLUTE SUCCESS CRITERION
For India planning, it is better to show **no map / no proximity conclusion** than a plausible-looking wrong one.

But it is also wrong to paralyse planning by demanding irrelevant precision. The target is:

**100% correct physical entity + planning-relevant positional certainty + verified access only where access matters.**
