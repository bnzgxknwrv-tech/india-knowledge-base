# SUBREGIE INDIA — technische eindvalidatie

run_id: VRINDAVAN-KUMAON-CORRIDOR-001
validated_role: GOUD
validated_status: PARTIAL
worker_completioncommit: bc851c237e6470235e840a445bada4df119c81c3
original_artifact_commit: c06a8de2c0c8f11c2b61066a537c54638870097d
repair_commit: 264bba42b299110689c3b877ce3dbae2cdcf0e6b
validated_commit: 264bba42b299110689c3b877ce3dbae2cdcf0e6b
technical_integrity: PASS
validated_at: 2026-07-18T22:44:00+02:00
schema_version: 2

## Reparatiecontrole

- `ZS-022` is exact en ongewijzigd overgenomen uit `ZILVER/sources/registry.jsonl` naar `GOUD/sources/registry.jsonl`.
- De technische reparatie wijzigde uitsluitend het GOUD-bronregister en de drie daardoor geraakte accepted-source-tellingen in manifest, audit en `COMPLETED`.
- Het accepted-source-totaal is na reparatie overal 25.
- Geen onderzoeksinhoud, claim, detectoruitkomst, status, GEO-punt, LOCATION_ID, routebesluit of KML is gewijzigd.

## Complete schema-v2-validatie

- GitHub-read en GitHub-write zijn bevestigd.
- De run staat op `GOUD_PARTIAL`; actieve rol en claim zijn leeg.
- `state.yaml` en `events.jsonl` waren vóór deze eindsynchronisatie gelijk op `EVT-0013`.
- Alle schema-v2-contextbestanden en alle 24 gepinde ZILVER-artifacts zijn volledig gelezen; alle verwachte blob-SHA's kwamen overeen.
- Alle verplichte GOUD-outputbestanden bestaan en bevatten de vereiste eindsentinel.
- Tellingen sluiten: 8 claims, 25 accepted sources, 7 rejected sources, 5 corridors, 6 transportopties, 10 routezones, 4 heavy-A-records, 12 detectorchecks, 10 negatieve zoekrecords, 40 WORKING_GEO-records, 16 corridor-LOCATION_ID-toewijzingen, 4 block requests, 51 centrale kaartrecords en 4 geo-verbindingen.
- Alle 25 accepted en 7 rejected source-ID's zijn uniek. Iedere source-ID-verwijzing resolveert exact één keer; `ZDC-003` resolveert nu geldig naar `ZS-022` en `ZR-005`.
- Alle LOCATION_ID's zijn uniek en blokzuiver: Braj 200–299, corridor 300–399 en Kumaon 400–499. Er is niets hernummerd, hergebruikt of cross-block toegewezen.
- Alle 40 WORKING_GEO-punten zijn behouden. Een exacte bezoekersingang is volgens de gepinde runpolicy geen vrijgavevoorwaarde.
- De formele dekking blijft exact 28 A, 2 B en 4 C. Geen formele of adviserende A/B/C is toegevoegd of gewijzigd.
- De ZILVER-predecessor-KML heeft ongewijzigd blob-SHA `b83fae2a47835c9b0506f26014c4e44aeab33631`, bevat 40 placemarks en sluit geldig als KML/XML.
- Manifest, handoff, `COMPLETED`, decision, state en eventhistorie stemmen inhoudelijk overeen op status `PARTIAL` en corridorresultaat `DOORREIZEN_NAAR_KUMAON`.
- Er is geen andere technische afwijking vastgesteld.

## Bevestigingen

- `DOORREIZEN_NAAR_KUMAON` blijft geldig.
- Een exacte bezoekersingang is geen vrijgavevoorwaarde.
- Geen inline-handoffmigratie is uitgevoerd.
- Geen nieuwe A/B/C, PARELS, interne Kumaon-planning of complete-project-KML is gemaakt.
- Geen nieuw onderzoek, nieuwe sweep, GOUD-heruitvoering of pipelineprotocolwijziging is uitgevoerd.

## Eindbesluit

De technische integriteit is `PASS`. De inhoudelijke dossierstatus blijft terecht `PARTIAL` door uitsluitend de bestaande tijdgevoelige en projectbrede open controles. Het gevalideerde pakket mag uitsluitend naar INDIA2.

## Routering

Volgende bestemming: INDIA2.
Regisseurspakket: `research/active/VRINDAVAN-KUMAON-CORRIDOR-001/transitions/INDIA2_REGISSEUR_PACKAGE.md`.

END_OF_ARTIFACT