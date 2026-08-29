# INDIA MAP / COORDINATE VERIFICATION RULE

Status: **HARD / UNIVERSAL / ALL INDIA MAPS / ALL SUCCESSORS**
Effective: 2026-08-29
Trigger: Mark caught a materially wrong map pin for the Dungeshwari / Mahakala Caves, which made a distant Rajgir hot-spring cluster appear to lie on the route. This is a decision-corrupting failure class.

## CORE RULE
A map shown to Mark is decision evidence. Therefore INDIA may NEVER render a decision-relevant map pin, route relationship, proximity claim or `je bent er toch` conclusion from an unverified/ambiguous geocoder result.

If a coordinate is not sufficiently verified, the correct action is **NO PIN**, not a guessed pin.

## REQUIRED VERIFICATION BEFORE ANY USER-FACING MAP
For every point that will appear on the map:
1. resolve the exact physical entity, not merely a similar place name;
2. check an authoritative/first-party source for identity/location where available (government, UNESCO, ASI, official hotel/business address, etc.);
3. obtain exact coordinates from a reliable map/geodata source, business entity ref, verified plus code, official GIS, or equivalent;
4. cross-check against a second independent source where practical;
5. disambiguate same-name places explicitly;
6. run a geographic sanity check against known nearby anchors and expected direction/distance;
7. only then render the pin.

A name-only geocoder call is NOT verification.

## SOURCE-CONFLICT RULE
If two credible coordinate sources materially disagree:
- do not average them;
- do not pick whichever gives the nicer route;
- classify `MAP_COORDINATE_UNRESOLVED`;
- research until the exact physical entity is resolved;
- if still unresolved, omit the pin and tell Mark exactly why.

This preserves the earlier Varanasi precedent from PR #23: uncertain hotel/location geometry must remain without `<Point>` rather than receive a guessed point.

## ROUTE / PROXIMITY RULE
Correct pins alone are not enough for route advice.

Before saying `langs de route`, `5 min verder`, `je bent er toch`, `omweg` or similar:
- verify both route endpoints;
- use actual road/walk route evidence for movement claims, not straight-line visual inference;
- compare baseline route vs route via candidate when the claim can change Mark's grade or day count;
- use conservative operational time, not optimistic map minimum;
- sanity-check that the route direction is geographically plausible.

A map pin may support orientation; it may not substitute for routing evidence.

## MAP RENDERING PREFERENCE
For decision-relevant maps prefer, in order:
1. verified structured business/place ref when it is the exact entity;
2. exact verified latitude/longitude;
3. sufficiently precise verified address when coordinates are not manually supplied.

Never invent a precise street address.

## USER-FACING CONFIDENCE
When a map materially supports a decision, INDIA should be able to state the pin basis compactly:
- `OFFICIAL + COORDINATE CROSS-CHECKED`, or
- `VERIFIED BUSINESS ENTITY`, or
- `PROVISIONAL — NOT USED FOR ROUTE DECISION`.

No map carrying an unresolved decision-critical pin may be presented as authoritative.

## PRE-SEND MAP VETO
Before every user-facing India map ask:
- Is every pin the exact intended physical place?
- Is every decision-relevant coordinate verified, not guessed by geocoder?
- Did I check for same-name traps?
- Do distances/directions pass a sanity test?
- If I make a route/proximity statement, do I have actual movement evidence rather than visual map inference?
- Would a wrong pin plausibly change Mark's A/B/C/A*/A+ judgment, night count or route?

Any NO = do not render the map yet.

## FAILURE RECOVERY
If Mark spots a map inconsistency:
1. stop all map-derived conclusions immediately;
2. reverify every pin in that presented map, not only the pin Mark noticed;
3. invalidate route/proximity conclusions derived from the bad map until recalculated;
4. create/update a verified coordinate registry for the active cluster when repeated map use is expected;
5. record the failure and strengthened rule in living governance so later INDIA versions do not repeat it.

## ABSOLUTE SUCCESS CRITERION
For India planning, it is better to show **no map** than a plausible-looking wrong map.