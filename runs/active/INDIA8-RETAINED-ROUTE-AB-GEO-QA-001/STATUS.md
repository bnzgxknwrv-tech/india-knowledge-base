# STATUS

state: CCI_RESULT_CONSUMED__PARTIAL_ACCEPT__CANON_RECONCILED
branch: agent/india8-cluster-casting
updated_by: INDIA9
updated_at: 2026-08-23

Task: `runs/active/INDIA8-RETAINED-ROUTE-AB-GEO-QA-001/TASK.md`

## WORKER RESULT CONSUMED

Worker branch: `agent/cci-retained-route-ab-geo-qa`
Worker commit: `3f2280ef45fb088efa00c634563902346f161dcb`
Outputs read:
- `RETAINED_ROUTE_AB_CANON_QA.md`
- `RETAINED_ROUTE_AB_GEO_LEDGER.csv`
- `OPERATIONAL_BLOCKERS.md`

## CENTRAL DISPOSITION

PARTIAL ACCEPTANCE.

Accepted:
- blocker collection;
- explicit unresolved geo states;
- silent-drop warnings as QA signals;
- useful location-by-location closure evidence where source/status semantics are correct.

Not accepted as exact map canon:
- `EXACT_GOOGLE_MAPS_MARKER` rows backed only by Wikipedia/derived coordinates rather than an actually opened, identity-matched Google Maps or approved official place record;
- the Madan Mohan / Banke Bihari coordinate collision as two exact closures;
- Varanasi completeness claims based only on the V2 prose shortlist instead of protected immutable VNS decisions;
- recommendation to ask Mark again about sacrificing Kasar/Almora A-sites, because Mark already made the route-yield decision.

## CENTRAL RECONCILIATION

Canonical correction written:
- `governance/INDIA9_CANON_RECONCILIATION_2026-08-23.md`

Sleep-base register reconciled:
- `runs/active/INDIA8-MARK-CLUSTER-DECISIONS-2026-08-20/SLEEP_BASE_REGISTER_2026-08-23.md`

Protected facts include:
- Kasar/Almora A/locks preserved but intentionally off current V2 route;
- Rishikesh retained in V2 but no Parmarth/ashram sleep;
- exactly two desired ashram stays: Haidakhan + Sri Ramanasramam;
- Varanasi protected original 001–040 = 32A / 5B / 3C plus later explicit 041–045 decisions;
- Sahi River View Guesthouse remains `LOCKED_BY_MARK`;
- Bodh Gaya historical locks preserved while later 2026-08-23 trip-selection supersedes older route use where inconsistent.

## GEO DISPOSITION

No guessed coordinates are promoted. Any visit point that still lacks source-compliant exact map closure remains explicitly in one of the allowed unresolved states (`ADDRESS_CONFIRMED_MARKER_NOT_CLOSED`, `ZONE_ONLY`, `GEO_CONFLICT`, `NONPUBLIC_OR_NOT_FOR_VISIT`) until stronger evidence exists.

The worker task is no longer `READY_FOR_CCI`; its result has been consumed and reconciled centrally.
