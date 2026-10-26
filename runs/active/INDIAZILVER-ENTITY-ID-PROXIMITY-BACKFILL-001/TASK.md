# INDIAZILVER ENTITY / ID / PROXIMITY BACKFILL

## DOEL
Bescherm de bestaande locatiecanon en maak de nieuwe all-findings entities gereed voor later ID + A/B/C zonder vroegtijdig iets te nummeren.

## LEES EERST
- `runs/active/INDIAZILVER-ENTITY-ID-PROXIMITY-BACKFILL-001/CENTRAL_INPUT_MANIFEST.md`
- bestaande permanente locatie-ID/A/B/C canon en oude clusteroutputs
- eerdere INDIA ZILVER completeness/proximity audit
- `governance/LOCATION_RESOLUTION_BEFORE_ABC_2026-08-19.md`

## EXPLICIET TOEGESTANE CROSS-BRANCH INPUTS
Van branch `agent/india8-cluster-casting`:
- `runs/active/INDIA8-ALL-FINDINGS-LOCATION-CLOSURE-001/SOURCE_LEDGER.md`
- `runs/active/INDIA8-ALL-FINDINGS-LOCATION-CLOSURE-001/GLOBAL_UNRESOLVED_QUEUE_SEED.md`
- `runs/active/INDIA8-ALL-FINDINGS-LOCATION-CLOSURE-001/STATUS.md`

Dit is een STAGED task. Ontbreken van de latere all-findings entitymaster is GEEN reden om te stoppen. Werk nu alles af wat met bestaande canon + 31 bekende candidates betrouwbaar kan.

## UITVOEREN NU
1. Herstel/bouw de beschermde baseline: bestaande permanent IDs, naam, cluster, A/B/C, lock, coordinates uit alle reeds beschikbare oude cluster/registerbronnen. `UNKNOWN` waar geen betrouwbare coordinaten bestaan.
2. Geen nieuwe IDs toekennen; gebruik de eerdere 31-candidate `REOPEN_AND_ID_QUEUE.md` als initiële NEW_ID_REQUIRED seed. Voeg later nieuwe candidates append-only toe.
3. Verzamel betrouwbare coordinates voor bestaande + nu al voldoende geïdentificeerde candidate entities; geen raden.
4. Bereken `<=1 km` en `<=3 km` nabijheid waar beide kanten betrouwbaar zijn. Maak NU een gedeeltelijke matrix; wacht niet op alle parallelle agents.
5. Markeer same-site/possible-duplicate/parent-complex cases voor TURQUOISE/centrale reconciliatie.
6. Markeer bestaande B/C die door nieuwe nabijheid/overlap later `REVIEW_FOR_UPGRADE` verdienen, zonder keuze te wijzigen.
7. Geef expliciet `UNKNOWN` / `DEPENDENCY_ENTITY_CLOSURE` waar coordinates/identity onvoldoende zijn.
8. Maak alle zes outputs. Als alle huidige inputs zijn uitgeput maar parallelle entity-feeds nog ontbreken, zet STATUS op `PARTIAL_COMPLETE__WAITING_FOR_PARALLEL_ENTITY_FEEDS`, niet BLOCKED.

## OUTPUTS
- PROTECTED_CANON_BASELINE.csv
- NEW_ID_REQUIRED_QUEUE.csv
- PROXIMITY_1KM_3KM_MATRIX.csv
- DUPLICATE_PARENT_CANDIDATES.md
- ABC_REVIEW_AFTER_CLOSURE_QUEUE.md
- STATUS.md

## LATER ADDITIEF INNEMEN
Zodra beschikbaar: outputs van BLAUW AOAY/Yogananda, ROOD Core-Kriya, GEEL four-person closure, WIT Anandamayi/heritage, TURQUOISE entity overlap. Nooit huidige betrouwbare rijen weggooien; alleen verrijken/append.

## HARD
Geen oude IDs/A-B-C/locks wijzigen. Geen nieuwe ID definitief uitgeven. Geen coordinaten raden. Geen route. Geen silent drops. Commit alles op dezelfde branch.