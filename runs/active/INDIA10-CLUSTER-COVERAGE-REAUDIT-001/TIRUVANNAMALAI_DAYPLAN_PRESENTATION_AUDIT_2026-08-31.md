# TIRUVANNAMALAI / ARUNACHALA — DAYPLAN PRESENTATION AUDIT — 2026-08-31

Status: **CURRENT CORRECTION / EXISTING DAYPLAN NOT MARK-READY / REBUILD REQUIRED**
Branch: `agent/india8-cluster-casting`

## WHY THIS EXISTS
INDIA14 presented `TIRUVANNAMALAI_FIXED_A_NUMBERED_DAYPLAN_2026-08-31.md` as decision-ready while it did not satisfy all hard user-facing geography/presentation requirements.

Mark correctly identified that a human-readable day cannot merely say `06:15 temple` or `09:05 next site`. Mark must be able to follow the day from bed to bed without knowing Indian geography.

## CONFIRMED FAILURES
1. Existing naming/recognition rules were broadly followed, but movement context was incomplete.
2. The existing hard `MARK_LOCATION_NAMING_CONTEXT_PROTOCOL.md` already required distance from the real base, realistic one-way time/mode and companion-stop geometry whenever a place is actionable. INDIA14 did not consistently expose that in the dayplan.
3. The human-centered standard already required proximity matrices, temporal fit, energy, robustness and enough geometry that Mark need not reconstruct the map. The answer did not satisfy that human-service bar.
4. A map/geo view was already required when spatial relation is the issue and the interface supports it. INDIA14 omitted the verified-location map.
5. `COORDINATE_INTEGRITY_GATE.md` says Tiruvannamalai is PASS for duration-scale geometry but NOT blanket-final-routing/KML-ready. In particular:
   - Gurumurtam exact pairwise road km/min still require final-routing verification;
   - Pavalakunru/Pavazhakundru exact approach/stair/vehicle endpoint still requires final-routing verification;
   - Virupaksha Cave final KML point must be rechecked because older/public coordinate renderings conflict;
   - Giripradakshina/Girivalam exact chosen start/end access was intentionally deferred.
   Therefore INDIA14 must NOT manufacture exact stop-to-stop numbers merely to make the dayplan look complete.
6. Varanasi/Sarnath is explicitly `RE-AUDIT REQUIRED BEFORE NEW GEOMETRY-DEPENDENT USE`; therefore the recently quoted precise-ish Sahi River View Guesthouse -> Varanasi Airport distance/time must not be treated as decision-grade until that exact transfer geometry is reverified.
7. Sri Ramanasramam guest accommodation may be allocated in an ashram-run facility outside the main compound within walking distance. Until acceptance/allocation is known, `actual sleep base` is not a single exact door. Local planning must state the assumed anchor and range rather than pretending room-door precision.

## NEW HARD FORMAT ADDED
`governance/MARK_LOCATION_NAMING_CONTEXT_PROTOCOL.md` now contains a universal `CLOCK-LEVEL DAYPLAN FORMAT` requiring, for every movement:
- origin;
- destination;
- route km;
- mode;
- conservative travel time;
- departure time;
- arrival time;
- dwell + WHY;
- next movement;
- first-stop distance from actual sleep base;
- later-stop distance from immediately previous stop;
- end-of-day return;
- walking-vs-motorized comparison where plausible;
- hike start/end/access;
- total walking, total motorized/rail burden, energy load and robustness.

## MAP RULE FOR THE REBUILD
The corrected Mark-facing Tiruvannamalai dayplan must include a map when the interface supports it.
Only locations that are currently `GEO_VERIFIED_FOR_DECISION = YES` at the relevant scale may be shown as authoritative pins.
Where a final pin/access point remains unresolved, either reverify it first or label/omit it rather than showing false precision.
The map supplements, never replaces, written km/min/mode context.

## REBUILD ORDER
Before the next Mark-facing dayplan:
1. reverify the exact local routing/access points needed for the selected A day modules;
2. reverify the previous-cluster sleep-base -> airport geometry if the arrival day is shown with decision-grade km/min;
3. choose/declare the planning sleep-base anchor for nights where the exact ashram guest building is unknown;
4. build pairwise practical route km/min for every day in chronological order;
5. include a verified-location map;
6. then re-present the numbered dayplan and only after that ask Mark for the duration decision.

## CONTENT STATUS
This audit does NOT change Mark's content decisions:
- Arunachala/Ramana sacred world remains A+ parent;
- the seven protected A children remain A;
- Mango Tree Cave and Pachaiamman Temple remain conditional B;
- the full added Lonely Planet layer remains dropped by Mark;
- no C or new OPEN attraction is inserted.

END