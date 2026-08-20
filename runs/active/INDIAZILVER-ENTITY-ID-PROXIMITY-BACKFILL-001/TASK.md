# INDIAZILVER ENTITY / ID / PROXIMITY BACKFILL

## DOEL
Bescherm de bestaande locatiecanon en maak de nieuwe all-findings entities gereed voor later ID + A/B/C zonder vroegtijdig iets te nummeren.

## LEES
- bestaande permanente locatie-ID/A/B/C canon en oude clusteroutputs
- eerdere INDIA ZILVER completeness/proximity audit
- runs/active/INDIA8-ALL-FINDINGS-LOCATION-CLOSURE-001/SOURCE_LEDGER.md indien branch beschikbaar; anders de gereconcilieerde person/cluster outputs die in de eerdere audit waren toegestaan
- governance/LOCATION_RESOLUTION_BEFORE_ABC_2026-08-19.md

## UITVOEREN
1. Maak beschermde baseline: bestaande permanent IDs, naam, cluster, A/B/C, lock, coordinates.
2. Geen nieuwe IDs toekennen; maak NEW_ID_REQUIRED candidates zodra fysieke identiteit voldoende is.
3. Verzamel betrouwbare coordinates voor bestaande + nieuwe candidate entities; geen raden.
4. Bereken <=1 km en <=3 km nabijheid waar beide kanten betrouwbaar zijn.
5. Markeer same-site/possible-duplicate/parent-complex cases voor TURQUOISE/centrale reconciliatie.
6. Markeer bestaande B/C die door nieuwe nabijheid/overlap later REVIEW_FOR_UPGRADE verdienen, zonder keuze te wijzigen.
7. Geef expliciet UNKNOWN waar coordinates/identity onvoldoende zijn; maak resolution dependency.

## OUTPUTS
- PROTECTED_CANON_BASELINE.csv
- NEW_ID_REQUIRED_QUEUE.csv
- PROXIMITY_1KM_3KM_MATRIX.csv
- DUPLICATE_PARENT_CANDIDATES.md
- ABC_REVIEW_AFTER_CLOSURE_QUEUE.md
- STATUS.md

## HARD
Geen oude IDs/A-B-C wijzigen. Geen nieuwe ID definitief uitgeven. Geen route. Commit alles op dezelfde branch.