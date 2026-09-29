# INDIA10 — OOSTENRIJK METHOD TRANSFER TO INDIA

status: ACTIVE_METHOD_ENRICHMENT
updated: 2026-08-25
source_repo: bnzgxknwrv-tech/oostenrijk-knowledge-base
branch: agent/india8-cluster-casting

## PURPOSE
Transfer only general planning/research lessons proven useful in Mark's 2026 Austria trip into India planning. Do not import Austria-specific destinations, vehicle/camping rules or stale live facts.

## 1. WALK QUALITY = SCENIC DENSITY, NOT JUST DESTINATION
Strong rule from Austria experience: the walk itself should be beautiful/interesting for a substantial part of the route. A mediocre approach to one decent viewpoint does not become a top walk merely because the endpoint is famous.
Positive reference pattern: forest + visible natural water along much of the route + rewarding water/landscape destination.
Negative reference pattern: long/medium walk whose route is mostly ordinary and only final viewpoint is mildly attractive.
India application:
- add `scenic_density` to every serious walk candidate: HIGH / MEDIUM / LOW;
- describe what proportion/type of the actual route delivers the main experience;
- long walk with LOW/MEDIUM scenic density is normally B/C unless spiritual/historical meaning independently makes the walking itself essential;
- prioritize compact 30–90 min or 1–3 h routes when experiential density is high.

## 2. WATER-FIRST HIGH-REWARD PATTERN
Stable preference learned from actual visits: particularly strong match = forest + running water/streams/cascades + lake/pool/river/waterfall destination. A compact water place with ~30–90 min pleasant walking and simple nearby tea/food/rest stop can score extremely high without being a major destination.
India application:
- Komoot discovery should explicitly search not only `lake`/`waterfall`, but route segments where water is present THROUGHOUT much of the walk;
- search `river trail`, `stream`, `cascade`, `forest lake`, `kund`, `tal`, `jheel`, `waterfall`, `ghat walk`, local-language equivalents;
- score `water_presence`: CONTINUOUS / REPEATED / DESTINATION_ONLY / NONE;
- do not underrate compact high-density water walks merely because they are short.

## 3. COMPLETE CHAIN VERIFICATION
Austria day protocol proved that isolated correct facts do not prove an executable outing. Verify the complete chain:
BASE/ANCHOR -> ROAD -> DROP/PARK -> PHYSICAL WALK START -> WALK -> END -> FOOD/REST/RETURN -> DRIVER/PICKUP -> NEXT ANCHOR.
India application:
- every selected walk gets exact physical trailhead/start, not just attraction coordinates;
- distinguish road distance from anchor to trailhead from walking distance;
- verify point-to-point pickup where used;
- record driver wait/relay logic where relevant;
- identify last access/gate/entry time, not only nominal closing time;
- include practical fallback if a forest gate/path/boat/temple access fails.

## 4. KOMOOT + HUMAN EVIDENCE WEIGHTING
Austria review protocol: community routes/reviews measure subjective reality better than official marketing, but ratings alone are weak.
India application:
- Komoot is primary route/community signal where coverage exists; cross-check with official route/forest/temple/park access + Outdooractive/AllTrails/Google Maps/local blogs/forums/Reddit where useful;
- `5.0 from 4 users` is weak compared with broad consistent evidence;
- evaluate number of users, photos, comments/tips, recency, second-source confirmation and whether route photos actually show the promised experience;
- evidence classes for route quality: STRONG_PATTERN / MODERATE_PATTERN / WEAK_SIGNAL / CONTRADICTED / NO_EVIDENCE;
- absence of wildlife/safety complaints is NOT proof of safety.

## 5. DISCOVERY -> SHORTLIST -> DEEP CLOSURE
Do not spend deep-research time equally on every walk.
India pipeline:
A. DISCOVERY: cheap reject of ordinary/repetitive routes.
B. SHORTLIST: compare scenic density, route burden, winter fit, safety, community evidence, spiritual content.
C. DEEP CLOSURE: only finalists get exact route, legal access, start point, timing, wildlife, driver/pickup, daylight and fallback closure.
Research depth rises with damage/irreversibility: isolated tiger/elephant forest or long detour = DEEP; urban lake loop = lighter closure.

## 6. LIGHT / SHADOW IS PART OF QUALITY
Austria mistake at a mountain lake showed that daylight does not mean the subject itself receives useful direct light. This matters for color/wow.
India application:
- for blue/green lakes, waterfalls in deep valleys, mountain panoramas, photogenic ghats/buildings, canyon/forest water and dawn/sunset views, add `LIGHT_AT_PLANNED_TIME = GOOD / PARTIAL / RISK / BAD / UNKNOWN`;
- distinguish sunrise/sunset from actual subject illumination/terrain shadow;
- a route marketed as `sunrise` or `evening` is not automatically optimal;
- if timing changes materially, re-open light analysis;
- for sacred walks, spiritual timing may legitimately outweigh scenic-light optimum, but state that tradeoff.

## 7. MORNING / EVENING MICRO-WALK SLOT
Austria preference + India project direction: short high-value walks can efficiently use morning/arrival-evening slots and should not automatically consume a core daytime block.
India application:
- every walk candidate gets `best_slot`: EARLY_MORNING / MORNING / MIDDAY / LATE_AFTERNOON / EVENING / FLEX;
- separately record safety-permitted slots: wildlife/legal/road-access may rule out dawn/dusk even when visually attractive;
- prefer morning for quiet water, towns/ghats before crowd, high/open terrain before afternoon weather where relevant;
- evening only when solo safety/legal/wildlife/light supports it.

## 8. THREE-VARIANT INTERNAL DESIGN
For meaningful walking decisions, internally compare at least:
1. shortest high-reward version;
2. best full scenic/spiritual version;
3. point-to-point/bundle version replacing driving where possible.
Then choose only the strongest variant(s). Do not show route clutter to Mark.

## 9. ATTACK THE WINNER / FAILURE MODES
Before locking a walk, actively test at least:
- legal/access failure;
- wildlife/solo-safety failure;
- wrong start/parking/drop point;
- winter/path-condition failure;
- route quality inflation (photos only show endpoint, route itself dull);
- light/shadow failure where scenic payoff depends on light;
- driver/pickup or return-chain failure for point-to-point.
If a failure remains material, mark closure debt rather than pretending certainty.

## 10. USER-FACING PRESENTATION TRANSFER
Mark needs burden first, then sales pitch.
For every walk decision card show early:
- full site/status name;
- FROM relevant A+/A/A* anchor: road km + realistic one-way road time to physical trailhead;
- walk: km + realistic time FROM physical start;
- elevation/difficulty;
- total incremental burden vs mandatory route;
- safety class;
- best slot + light status where relevant;
- exact/best-searchable Komoot name;
THEN explain why beautiful/meaningful.

## 11. PERSONAL TASTE REFERENCES TRANSFERRED AS SEARCH HEURISTICS
Use as heuristics, not as India grade decisions:
- strong positive: forest + visible water throughout + beautiful water destination;
- strong positive: compact natural water + short pleasant loop + simple nearby rest/tea/food;
- strong positive: route itself repeatedly rewarding, not merely endpoint;
- negative: generic gondola/viewpoint-style equivalent where destination/route feels empty or merely panoramic;
- negative: long walk with mediocre route for one ordinary payoff;
- variation matters: avoid stacking highly similar walks/ghats/caves/nature experiences back-to-back when schedule can alternate experience types.

## 12. FRESHNESS / PROCESS STATES
Transfer Austria source discipline:
- LIVE facts must be checked again on use;
- CHECK_ON_USE facts rechecked before execution;
- STABLE applies to enduring preference/method lessons;
- missing evidence states: NIET_GECONTROLEERD / NIET_GEVONDEN / BRON_GEBLOKKEERD, separate from substantive UNCERTAIN.
This makes unfinished work replaceable instead of opaque.

## IMMEDIATE INDIA CHANGES
1. Extend Komoot finalist schema with: scenic_density, water_presence, evidence_class, best_slot, safety-permitted slots, light_at_planned_time, full-chain closure, failure_modes.
2. Re-evaluate A+ walk gaps using high-density-water and spiritual-walk heuristics before generic viewpoint hikes.
3. For Nainital/Sattal/Khurpatal/Dhokaney specifically, compare route photos/community evidence for how much of the WALK itself contains water/forest, not only endpoint beauty.
4. For Varanasi ghat spine, score experiential density + dawn/evening crowd/light/safety rather than treating all riverfront kilometers as equal.
5. For Arunachala, preserve spiritual meaning as a separate dimension from scenic density; legal lower paths can outrank prettier illegal/restricted summit variants.
6. For Bodh Gaya, test whether Mahabodhi->Sujata or local river/field walking actually provides meaningful route experience or is mostly ordinary road/urban walking before promoting a connection.

## PROVENANCE
Derived from stable method/taste lessons in Austria repository:
- PREFERENCES.md
- DAY_PLANNING_PROTOCOL.md
- REVIEW_RESEARCH_PROTOCOL.md
- RESEARCH_SOURCE_INDEX.md
- TASTE_REFERENCES.md
- VISITED_AND_DECIDED.md
No Austria-specific live route/price/opening fact is imported into India canon.
