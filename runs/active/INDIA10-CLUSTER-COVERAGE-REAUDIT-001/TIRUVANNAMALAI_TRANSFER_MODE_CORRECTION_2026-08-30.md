# TIRUVANNAMALAI / ARUNACHALA — TRANSFER MODE CORRECTION — 2026-08-30

Status: **CURRENT CORRECTION / RAIL-FIRST REEVALUATION REQUIRED / NO MARK ROUTE OR DURATION DECISION**
Branch: `agent/india8-cluster-casting`

## FAILURE FOUND
During a fresh-session Tiruvannamalai planning turn, INDIA recommended multi-hour private-car/taxi legs after flights without first applying the existing hard transport hierarchy.

This was an INDIA boot/execution failure, NOT missing repository memory. The rule already existed redundantly in mandatory current sources:
- `INDIA_MASTER_BOOT.md` human-planning checksum;
- `MARK_TRAVEL_PREFERENCES_CURRENT.md` transport section;
- `TRIP_FRAME_HARD.md` transport invariant;
- `CURRENT_DECISIONS_MASTER.md` hard trip frame;
- `DECISION_LEDGER.jsonl` `DL-0009`;
- CCI parity `MARK_CURRENT_CANON_MASTER.md` `MRK-028`.

## CONTROLLING TRANSPORT RULE
1. Train first when practical.
2. Overnight rail target 1A / First AC where appropriate; 2A only after Mark accepts fallback.
3. Flight only when it truly creates meaningful usable door-to-door time savings after airport friction.
4. Private car/taxi is preferred for mountains, short last-mile, or a genuine door-to-door win — not as an automatic multi-hour intercity default.
5. Long-distance/intercity bus is excluded as normal fallback.
6. Full human burden controls: checkout/loading/access/wait/security/baggage/delay/onward/check-in/rest/daylight/energy.
7. For Mark, calm and predictability matter: a train solution may be preferred even when approximately 1–2 hours slower than a long taxi/car solution, provided it is operationally sensible and bookable.

Item 7 does not create a new preference; it makes explicit the practical implication Mark stated while correcting INDIA, consistent with the already-existing train-first hierarchy.

## INVALIDATED WORKING HYPOTHESES
The following are no longer accepted as default planning assumptions:
- `Varanasi -> Bengaluru or Chennai by air -> 2.5–3.5 h private car -> Tiruvannamalai` as default inbound;
- `Tiruvannamalai -> 2.5–3 h private car -> Chennai Airport -> Delhi flight` as default outbound.

They remain transport alternatives to compare only if rail-heavy options are materially worse. They were never Mark decisions.

## REQUIRED REBUILD
Before the Tiruvannamalai duration surface is presented as final decision-ready support, INDIA must compare current service structure for:

### Edge A — Varanasi/Sarnath -> Tiruvannamalai/Arunachala
Goal: put the major ground distance on rail wherever practical. Test direct/near-direct long-distance rail, rail via useful junctions, flight + short rail, and flight + genuinely short last-mile. Avoid a multi-hour taxi merely because it is nominally fastest.

### Edge B — Tiruvannamalai/Arunachala -> Delhi/international-exit world
Goal: compare a rail-heavy exit from Tiruvannamalai itself or via a nearby major junction against Chennai-air routing. Long overnight/through rail may be attractive if it converts movement into rest without consuming an unreasonable extra trip day; otherwise use rail for the regional leg and flight for the long northbound leg if that yields the best human result.

## LIVE-FACT BOUNDARY
Exact Dec 2026 / Jan 2027 train numbers, running days, 1A availability and domestic flight schedules remain `LIVE_RECHECK_LATER` until exact dates/topology are ready. Current schedules may be used now to prove route feasibility and burden classes, not to lock tickets.

## DURATION EFFECT
No duration decision changes automatically from this correction. Current local interpretation remains:
- 4 nights = compressed if one whole Ramanasramam day is protected;
- 5 nights = first clean no-stacking local structure and current INDIA recommendation;
- 6 nights = deliberately extra depth/recovery.

The corrected inbound/outbound rail-heavy burden must be shown before Mark locks 4/5/6 nights.

END TRANSFER MODE CORRECTION
