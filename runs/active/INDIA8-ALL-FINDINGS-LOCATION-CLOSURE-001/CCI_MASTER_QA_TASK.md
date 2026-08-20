# CCI MASTER QA TASK — ALL FINDINGS LOCATION MASTER

## ROLE
CCI is an independent QA/reconciliation partner, NOT a new color/workstream. INDIA8/9 remains central integrator and Mark remains final A/B/C editor.

## REPOSITORY
`bnzgxknwrv-tech/india-knowledge-base`

## PRIMARY CENTRAL BRANCH
Read central integration state from `agent/india8-cluster-casting`.
Do not merge or modify protected A/B/C/IDs/locks.

## REQUIRED FIRST READ
1. `governance/INDIA_REGIE_DOORGANGSPROTOCOL_2026-08-20.md`
2. `governance/LOCATION_RESOLUTION_BEFORE_ABC_2026-08-19.md`
3. `runs/active/INDIA8-ALL-FINDINGS-LOCATION-CLOSURE-001/MASTER_SCHEMA.md`
4. `runs/active/INDIA8-ALL-FINDINGS-LOCATION-CLOSURE-001/MASTER_INGEST_STATE.md`
5. `runs/active/INDIA8-ALL-FINDINGS-LOCATION-CLOSURE-001/FINAL_FEED_MANIFEST.md`

## OBJECTIVE
Independently QA the central-master construction. The goal is NOT new broad discovery. The goal is to catch integration mistakes before Mark sees A/B/C-ready cluster lists.

Audit specifically:
- source-record accounting closes with zero silent drops;
- no physical micro-site was collapsed into a parent complex;
- no historic structure was silently equated with a modern successor;
- same-site overlap is physical, not city-name-only;
- Babaji claimant traditions remain separated;
- R4/R5 records remain visible and excluded from A/B/C until sufficiently resolved;
- existing permanent IDs 001-081 and all old A/B/C/locks remain unchanged;
- newly resolved R1-R3 entities that need a new permanent ID are staged exactly once;
- aliases/duplicates preserve all source links;
- AOAY/Yogananda P0 scenes remain visible even when micro-location is approximate;
- heritage stays and preserved rooms are not lost in generic site rows;
- ZILVER proximity claims are only used when both coordinates passed its reliability gate;
- East findings remain preserved even though East is currently route-deprioritized.

## INPUT FEEDS TO EXPECT
- BLAUW AOAY/Yogananda complete feed
- TURQUOISE entity/same-site/parent-child/successor reconciliation
- GEEL four-person closure
- WIT Anandamayi/heritage closure
- ROOD Core-Kriya closure
- ZILVER final proximity/new-ID staging

## OUTPUT
Write a durable QA report under a new CCI task path on your normal CCI/Claude working branch, or post result to the existing CCI reporting channel/PR #23 if that is current CCI governance.
The report must include:
1. `MASTER_QA_VERDICT`: PASS / PASS_WITH_FIXES / FAIL
2. exact accounting or integration defects with source refs
3. any duplicate/silent-drop/parent-child/successor errors
4. any A/B/C-readiness errors
5. required fixes ordered P0/P1/P2
6. `NEXT_ALLOWED_STEP`

Do not start a new person sweep. Do not make route choices. Do not assign A/B/C.
