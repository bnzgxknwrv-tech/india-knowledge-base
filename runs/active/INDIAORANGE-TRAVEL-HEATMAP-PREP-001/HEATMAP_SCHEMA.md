# HEATMAP_SCHEMA — INDIA ORANJE

Status: PROCESS-SCHEMA; geen persoonsresearch; `travel_significance` blijft ONBESLIST tot Mark A/B/C beslist.

## 1. Inputrecord
Elke rij representeert één gereconcilieerd persoons-locatierecord. Alleen records gebruiken die de persoonsreconciliatie hebben doorlopen; ongereconcilieerde detectoroutputs blijven buiten de heatmap.

```yaml
record_id: <duurzame of tijdelijke reconciliatie-id>
person: <canonieke Top-11 naam>
location_name: <gereconcilieerde locatienaam>
city: <stad/dorp of UNKNOWN>
region: <staat/regio of UNKNOWN>
country: India
geo_key: <stabiele city/region sleutel; geen nieuw onderzoek nodig>
evidence_level: <project-evidentietier zoals door bronreconciliatie vastgesteld>
physical_exactness: <EXACT_SITE | SITE_WITHIN_COMPLEX | CITY_ONLY | REGION_ONLY | UNKNOWN>
a_anchor_locked: <true|false>
lock_basis: <LOCKED_BY_MARK | NONE>
conflict_flag: <NONE | OPEN_SOURCE_CONFLICT | OPEN_LOCATION_CONFLICT | OPEN_IDENTITY_CONFLICT | OTHER>
reconciliation_state: <FINAL | PROVISIONAL | BLOCKED>
travel_significance: ONBESLIST
source_task: <reconciliatie-task-id>
source_checkpoint: <commit/SHA indien metadata beschikbaar>
```

## 2. Aggregatie per `geo_key`
Heatmapaggregatie gebeurt mechanisch, zonder reiswaardering.

```yaml
geo_key: <city/region sleutel>
city: <naam of MULTI/UNKNOWN>
region: <naam>
unique_person_count: <aantal unieke personen met minimaal 1 record>
location_count: <aantal unieke fysieke locaties na reconciliatie-deduplicatie>
exact_site_count: <aantal records/locaties met EXACT_SITE of SITE_WITHIN_COMPLEX>
a_anchor_locked_count: <aantal locked A-ankers>
persons: [<unieke canonieke namen>]
evidence_levels_present: [<tiers>]
conflict_flag: <true indien minimaal één onderliggend open conflict>
blocked_record_count: <aantal BLOCKED>
provisional_record_count: <aantal PROVISIONAL>
travel_significance: ONBESLIST
regional_deep_sweep_trigger: <YES | NO | DEFER volgens CLUSTER_TRIGGER_RULES.md>
```

## 3. Normalisatieregels
1. `unique_person_count` telt personen, niet vermeldingen.
2. `location_count` telt gereconcilieerde fysieke locaties; aliases/synoniemen tellen eenmaal wanneer reconciliatie ze reeds gelijkstelt.
3. Records mogen niet door INDIA ORANJE inhoudelijk worden samengevoegd wanneer reconciliatie dat nog niet heeft gedaan.
4. Een open conflict blijft zichtbaar en mag nooit door aggregatie verdwijnen.
5. `A-anker/locked` is governance, geen score. Arunachala/Tiruvannamalai blijft `LOCKED_BY_MARK`; dit schema start daar geen regio-sweep.
6. Babaji-grot Kukuchina/Dunagiri blijft als bestaande hoofdreden-governance behouden, maar krijgt hier geen nieuwe locatieanalyse.
7. Geen numerieke travel-score afleiden uit personen-, locatie- of evidentiecounts. Counts zijn detectoren, geen A/B/C.
8. `travel_significance` blijft letterlijk `ONBESLIST` totdat Mark de A/B/C-laag uitvoert.

## 4. Minimale validatie voor heatmap-ingest
Een record mag pas in de landelijke heatmap wanneer `person`, `geo_key`, `reconciliation_state`, `conflict_flag`, `physical_exactness` en `travel_significance: ONBESLIST` aanwezig zijn. Ontbrekende stad/regio mag `UNKNOWN` zijn; ontbrekende zekerheid mag niet worden ingevuld door nieuw persoonslocatieonderzoek.