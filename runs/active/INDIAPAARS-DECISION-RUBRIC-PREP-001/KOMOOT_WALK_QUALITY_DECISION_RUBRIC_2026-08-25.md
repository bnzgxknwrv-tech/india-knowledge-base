# INDIA PAARS — KOMOOT WALK QUALITY + DECISION RUBRIC

status: COMPLETE_RUBRIC
updated: 2026-08-25
branch: agent/indiapaars-decision-rubric-prep
owner: INDIA PAARS
scope: walk-quality comparison / decision support only

## 0. GOVERNANCE / NON-OVERRIDE

This rubric compares WALK VARIANTS and WALK MODES. It does **not** change any existing Mark grade, lock, A+/A/A*/B/C status, cluster decision or place inclusion.

Existing grades are metadata only. A place may remain A+/A/A* while a particular walking mode receives `DO_NOT_WALK`, `GUIDE_REQUIRED`, `DAYLIGHT_ONLY`, `SUPPRESS_VARIANT` or `HOLD_FOR_SAFETY_CLOSURE`.

Primary method input for this pass:
- `runs/active/INDIA10-CLUSTER-COVERAGE-REAUDIT-001/KOMOOT_WALK_DISCOVERY_LAYER_2026-08-25.md` from central branch `agent/india8-cluster-casting`.

Core principle: Komoot is discovery/route evidence, never legal or safety certification.

## 1. DECISION ORDER — GATES BEFORE SCORE

A candidate is evaluated in this order. A later high score can never undo an earlier veto.

### GATE 1 — IDENTITY / EXACT ROUTE
Required before final ranking:
- exact/best-searchable Komoot route or Highlight name;
- physical start and end point;
- route form: loop / out-and-back / point-to-point;
- distance and realistic walking time from that physical start;
- elevation gain/loss where available.

If the attraction is known but the exact Komoot line is not closed: `ROUTE_IDENTITY_UNCLOSED`. It may be screened for quality, but cannot be a final operational winner.

### GATE 2 — LEGALITY / SAFETY VETO
Safety is outside the compensating score.

Allowed operational modes:
- `SAFE_SOLO`
- `DAYLIGHT_ONLY`
- `PREFER_COMPANY`
- `GUIDE_RECOMMENDED`
- `GUIDE_REQUIRED`
- `DO_NOT_WALK`

Additional closure state:
- `HOLD_FOR_SAFETY_CLOSURE` = insufficient exact-route evidence; never silently convert to SAFE.

Hard outcomes:
- walking prohibited by competent authority -> `DO_NOT_WALK`;
- registered guide legally mandatory -> `GUIDE_REQUIRED`;
- temporary closure / material current access prohibition -> walking variant suppressed for affected period;
- exact trail crosses protected land where pedestrian legality is unverified -> `HOLD_FOR_SAFETY_CLOSURE`;
- material wildlife/exposure risk that makes dawn/dusk unsuitable -> at minimum `DAYLIGHT_ONLY`, stronger status if evidence warrants;
- winter ice/snow/landslide conditions that make the exact line unsuitable in Dec–Jan -> `WINTER_NOT_RECOMMENDED` or veto for this trip window.

The PLACE remains untouched. Only the WALK MODE is constrained.

### GATE 3 — ANTI-MEDIOCRITY FLOOR
A long walk does not earn value merely by being a walk.

Automatic `SUPPRESS_LONG_MEDIOCRITY` when all are true:
- realistic walking time is 3–5 h (or longer), and
- unique scenic/spiritual payoff < 4/5, and
- scenic-density score < 4/5, and
- no genuinely unique destination/content requires that duration.

A 3–5 h generic viewpoint or repetitive hill walk must **not** beat a 30–90 min route with genuinely exceptional water/forest/waterfall/cave/spiritual content.

For >5 h routes, require at least one of:
- world-class or near-world-class landscape payoff;
- uniquely meaningful spiritual/historical footpath where walking is part of the meaning;
- multiple exceptional sections with sustained scenic density;
- no materially shorter route reaches the same high-reward core.

### GATE 4 — SCENIC-DENSITY FLOOR
Estimate the fraction of walking time that is genuinely attractive rather than road shoulder, built-up approach, generic ascent, parking access or repetitive connector.

Scenic-density rating:
- 5 = >=80% high-quality / little dead walking;
- 4 = 60–79%;
- 3 = 40–59%;
- 2 = 20–39%;
- 1 = <20%;
- 0 = route is mostly transport disguised as walking.

If a route has >40% dull approach and the high-reward core can be entered later by road/drop-off, compare the shortened variant. Do not reward unnecessary walking.

### GATE 5 — DUPLICATION / DOMINANCE
When two walks deliver substantially the same payoff, retain the dominant variant.

Variant A dominates B when A is at least as strong on scenic payoff and safety, and materially better on one or more of:
- scenic density;
- time;
- elevation/technical burden;
- anchor/corridor friction;
- road exposure;
- winter fit;
- shortening potential.

Keep a second variant only if it creates a genuinely different experience (e.g. forest immersion versus exposed panorama; sunrise option versus midday; spiritual approach versus vehicle arrival).

## 2. 100-POINT QUALITY SCORE — ONLY AFTER GATES

Unknown fields are `UNK`, never zero. A candidate with material `UNK` fields gets a provisional score/rank only and cannot displace a fully closed candidate on false precision.

### A. SCENIC / CONTENT VALUE — 45 points

#### A1. Unique scenic payoff — 18
0 generic; 1 ordinary; 2 pleasant; 3 clearly good; 4 exceptional/strong trip memory; 5 destination-defining or rare.

Evidence question: what exactly is the payoff — blue/green water, forest lake, waterfall/cascade, gorge/river, cave/rock landscape, summit/ridge view, sacred footpath, unusually beautiful forest — and could a comparable experience be obtained more easily elsewhere on this trip?

#### A2. Scenic density — 15
Use Gate 4 scale. High payoff at one point cannot conceal a long dull approach.

#### A3. Content richness — 8
Rate the meaningful combination of `water`, `forest`, `waterfall`, `river/gorge`, `cave/rock`, `viewpoint/ridge`, `spiritual`.
- 5 = several strong elements or one extraordinarily strong element;
- 3 = one clear strong element;
- 1 = generic scenery only.
Do not count weak tags merely to inflate variety.

#### A4. Walking-specific meaning — 4
5 = the act of walking materially adds meaning (historic/spiritual footpath, immersion, point-to-point narrative);
3 = walking substantially improves the experience over vehicle arrival;
0 = the same payoff is essentially obtained from the road/parking point.

### B. REWARD EFFICIENCY / ROUTE FRICTION — 26 points

#### B1. Reward per walking time — 10
5 = <=90 min and exceptional/high-density payoff, or longer only because exceptional content is sustained;
4 = <=2 h with strong payoff;
3 = 2–3 h with strong payoff;
2 = 3–5 h for merely good payoff;
1 = long/effortful for limited payoff;
0 = poor conversion of time to experience.

This field enforces the anti-mediocrity preference; it is not a blanket preference for short walks.

#### B2. Elevation / technical burden — 4
5 = easy/moderate burden relative to payoff;
3 = meaningful climb/terrain but justified;
1 = high burden for modest gain;
0 = technical/physical burden disproportionate to experience.
A hard route can still score well if payoff is exceptional; difficulty itself is never rewarded.

#### B3. Friction from selected A+/A/A* anchor or mandatory corridor — 8
Measure from the relevant selected anchor/corridor, not hotel folklore.
5 = effectively on-foot/from-anchor or negligible detour;
4 = <=15 min incremental road detour;
3 = 16–30 min;
2 = 31–60 min;
1 = >60 min or awkward transport dependency;
0 = requires route sacrifice/extra day without exceptional justification.

Where possible record both:
- road time anchor -> physical walk start;
- incremental detour versus mandatory transfer corridor.

#### B4. High-reward shortening potential — 4
5 = long route can cleanly become a short high-reward core without losing the principal experience;
3 = partial shortening possible;
0 = no useful shortening or shortening destroys the experience.

Shortening is a positive capability, not an instruction to mutilate genuinely coherent routes.

### C. DEC–JAN / DAYPART FIT — 12 points

#### C1. Winter fit — 6
5 = normally strong Dec–Jan fit with no material seasonal degradation/access issue known;
3 = workable but needs weather/local check;
1 = frequent winter limitation or meaningful ice/snow/access risk;
0 = unsuitable/closed for target period.

#### C2. Morning/evening value — 3
5 = particularly good and safely usable at the relevant daypart;
3 = ordinary daylight use;
0 = daypart adds little or safety makes the intended timing inappropriate.
Never award sunrise/sunset value where wildlife/legal evidence argues against dawn/dusk.

#### C3. Crowd / road exposure — 3
5 = mostly trail/nature, low traffic conflict and crowd burden;
3 = mixed;
1 = material road shoulder/traffic/crowd dilution;
0 = route experience dominated by road/crowd exposure.

### D. SAFETY OPERABILITY AFTER PASSING VETO — 7 points
This does **not** cancel Gate 2.

5 = exact route legal, straightforward retreat/access, safety evidence supports intended mode;
4 = manageable with daylight/local check;
3 = company/guide prudent but operationally easy;
1 = substantial remoteness/wildlife/terrain friction even with mitigation;
0 = do not operationally recommend.

Required annotations remain separate: wildlife, protected-area status, guide rule, daylight window, signal/remoteness, terrain, winter risk, driver-wait requirement.

### E. PORTFOLIO NOVELTY / DUPLICATION — 10 points
5 = adds a genuinely new trip experience;
4 = similar category but clearly distinctive;
3 = moderate overlap;
1 = largely repeats a stronger planned walk;
0 = redundant variant with no meaningful advantage.

Do not penalize repeated walking itself. Penalize repeated EXPERIENCE content.

## 3. SCORE INTERPRETATION

After gates:
- 85–100: `KEEP_STRONG`
- 75–84: `KEEP`
- 65–74: `KEEP_ONLY_IF_LOW_FRICTION_OR_DISTINCT`
- 55–64: `BORDERLINE_SUPPRESS`
- <55: `SUPPRESS_VARIANT`

These are walk-quality outcomes, **not Mark grades**.

A candidate can score 90 and still be `GUIDE_REQUIRED`; a place can be A+ while its walk variant scores 55; a place can remain selected while pedestrian access is `DO_NOT_WALK`.

## 4. LONG-WALK OVERRIDE TEST

Before allowing any 3 h+ route into a top shortlist, answer YES to at least two of the following, including Q1 or Q2:
1. Is the principal payoff >=4/5 unique scenic value?
2. Is scenic density >=4/5?
3. Is walking itself spiritually/historically meaningful >=4/5?
4. Does the route contain multiple distinct exceptional sections rather than one endpoint?
5. Is there no <=2 h variant preserving >=80% of the best experience?

If not: `SUPPRESS_LONG_MEDIOCRITY`.

## 5. SHORT-HIGH-REWARD ADVANTAGE TEST

A <=90 min walk receives explicit comparison priority when it has:
- scenic payoff >=4/5;
- scenic density >=4/5;
- manageable anchor/corridor friction;
- no safety/legal veto.

Such a route should normally outrank a 3–5 h route with merely good scenery even if the longer route has more total kilometres, more elevation or a higher Komoot community count.

Komoot popularity is a signal only. It is never a substitute for scenic quality, legality, safety or portfolio fit.

## 6. WALK-INSTEAD-OF-DRIVE / POINT-TO-POINT TEST

For any connector between two already selected places, compare:
- vehicle-only time;
- walk distance/time from drop-off A to pickup B;
- scenic-density of the connector;
- whether the walk eliminates rather than adds road kilometres;
- luggage/driver logistics;
- daylight and safety;
- whether the point-to-point line is legal throughout.

A connector is preferred only when walking itself adds memorable content. Do not turn a practical transfer into a long mediocre roadside walk merely to increase walking volume.

## 7. MORNING / EVENING TEST

Morning/evening candidates must have a daypart-specific reason:
- better light/reflection/view;
- quieter atmosphere;
- meaningful ritual/spiritual timing;
- temperature advantage;
- frictionless use directly before departure/after arrival.

Safety has precedence. A beautiful dawn idea in a wildlife-risk zone can become `DAYLIGHT_ONLY` or be rejected for that daypart.

## 8. REQUIRED COMPARISON ROW FOR EACH CANDIDATE

Use this lossless schema:

`candidate | existing_mark_status | komoot_name | physical_start | physical_end | km | realistic_time | elevation | form | scenic_payoff_0_5 | scenic_density_0_5 | content_tags | walking_specific_meaning_0_5 | reward_efficiency_0_5 | technical_burden_0_5 | anchor_or_corridor | anchor_to_start_road_time | incremental_detour | shortening_0_5 | winter_0_5 | daypart_0_5 | crowd_road_0_5 | safety_mode | legal_status | wildlife | guide_rule | remoteness_signal | terrain_risk | duplication_0_5 | weighted_score | gate_result | quality_outcome | confidence`

Never replace `UNK` with an invented estimate.

## 9. TIE-BREAK ORDER

If two candidates remain within 3 weighted points, decide in this order:
1. no safety/legal qualifier over qualified mode;
2. higher unique scenic payoff;
3. higher scenic density;
4. lower total visit burden;
5. lower incremental route friction;
6. stronger Dec–Jan fit;
7. more novel portfolio content;
8. better clean shortening option;
9. stronger Komoot community/photos/tips signal.

Community signal is deliberately last among substantive tie-breakers.

## 10. WHAT MUST NEVER HAPPEN

- No Mark grade changes from this rubric.
- No automatic promotion because Komoot calls a route popular/top-rated.
- No assumption that a Komoot line is legal or safe.
- No long route winning through distance/elevation prestige.
- No hidden penalty for short walks.
- No hidden reward for difficulty.
- No counting a dull approach as scenic content.
- No treating `UNK` safety as safe.
- No keeping several near-identical route variants merely to make a longer shortlist.
- No forcing a second waterfall/lake/viewpoint when it duplicates a clearly stronger planned experience without a low-friction or genuinely distinctive reason.

## 11. DECISION OUTPUT PHILOSOPHY

The desired result is a small set of dominant walks:
- exceptional scenic/spiritual payoff;
- high beautiful-minute density;
- efficient integration with selected anchors/corridors;
- winter-operable in Dec–Jan;
- explicit safe/legal walking mode;
- low duplication;
- shortened to the high-reward core when that improves the experience.

The rubric is intentionally hostile to mediocrity. Fewer closed winners are preferable to a long catalogue of merely pleasant walks.
