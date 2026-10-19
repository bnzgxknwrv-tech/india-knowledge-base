# STATUS — AOAY-FULL-LOCATION-ATLAS-001

```
task_id: AOAY-FULL-LOCATION-ATLAS-001
state: SUBSTANTIELE_EERSTE_OOGST__NIET_SATURATED__WACHT_OP_INDIA
task_file: runs/active/AOAY-FULL-LOCATION-ATLAS-001/TASK.md
result_file: runs/active/AOAY-FULL-LOCATION-ATLAS-001/RESULT.md
raw_occurrences_file: runs/active/AOAY-FULL-LOCATION-ATLAS-001/RAW_OCCURRENCES.jsonl
place_atlas_file: runs/active/AOAY-FULL-LOCATION-ATLAS-001/PLACE_ATLAS.jsonl
coverage_matrix_file: runs/active/AOAY-FULL-LOCATION-ATLAS-001/COVERAGE_MATRIX.md
last_updated: 2026-08-16
last_updated_by: CCI (CCI_TASK 082, eerste sweep-ronde)
```

**blockers**: geen.

**Mark-opdracht**: volledige *Autobiography of a Yogi* als omgekeerde detector: boek → ALLE locatievermeldingen. Geen regiobegrenzing, geen relevantiefilter tijdens extractie.

**Samenvatting eerste ronde**: reproduceerbare 3-detector-pipeline gebouwd (structuuranalyse +
machine-assisted token-pass + known-entity gazetteer-pass) over de volledige Project Gutenberg
#7452-tekst (48 hoofdstukken, sha256 in `RESULT.md`). 1.359 occurrence-records, 123 genormaliseerde
plaatsen, waarvan 30 `AOAY_FOUND_BUT_MISSING_FROM_REPO` (sterkste nieuwe signaal: een compleet
nieuwe Kashmir-regiocluster, twee volledige hoofdstukken lang, tot nu toe afwezig uit elke
bestaande sweep). 19 plaatsen bevestigen bestaande Top-11-atlaspunten rechtstreeks vanuit AOAY's
eigen brontekst.

**Eerlijk: `AOAY_LOCATION_SWEEP_SATURATED: NEE`.** Circa 6.691 kandidaat-tokentypes (vnl.
persoonsnamen/aanspreektitels op basis van steekproef, niet individueel geverifieerd) blijven
`UNRESOLVED_BUT_RECORDED`. Geen enkele occurrence heeft nog een ingevulde
`event_verified_from_AOAY`/`physical_identity_verified`/`exact_sublocation_verified`-beoordeling.
Zie `RESULT.md` voor de volledige, eerlijke stand en concrete vervolgstappen.

**next_allowed_step**: STOP hier voor INDIA-QA/richting. Voorstel: (1) eigen Kashmir-
discoverytaak starten, (2) gerichte detector-1-verdieping op de hoofdstukken met de meeste
onopgeloste tokens, (3) occurrence-niveau verificatie voor de 30 nieuwe plaatsen eerst. Geen
automatische voortzetting zonder INDIA-akkoord over prioriteit.

Geen PDF. Geen route. Geen A/B/C namens Mark.
