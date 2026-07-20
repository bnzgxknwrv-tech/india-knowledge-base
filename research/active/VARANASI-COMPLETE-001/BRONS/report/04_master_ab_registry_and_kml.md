# 04 — Repositorybreed A/B-register en voorbereide KML

## Dekking

Het gedeelde `MASTER_A_B_GEO_REGISTRY.jsonl` bevat exact 30 actieve records:

- 28 formele A;
- 2 formele B;
- 0 formele C;
- 0 stations, routes, bases of hotels.

De telling komt exact overeen met `LOCKED_A.md` en `LOCKED_B.md`.

## LOCATION_ID en GEO

Alle bestaande Kumaon-LOCATION_ID's zijn exact behouden. Formele locaties waarvoor in de gepinde bronnen geen permanent LOCATION_ID beschikbaar is, hebben `location_id: null`; zij zijn via een unieke `registry_record_id` en fysieke naam afzonderlijk identificeerbaar. Er is geen tijdelijk nummer als permanent gepresenteerd.

Iedere kaartlocatie heeft een coördinaat en zichtbare GEO-status. Bestaande Kumaon-GEO is rechtstreeks hergebruikt. Elders is een herkenbare pin, terreincentrum, adrespunt of verantwoord lokaal werkpunt gebruikt. De precieze deur of ingang is geen BRONS-vrijgavevoorwaarde.

## KML

`INDIA_ALL_FORMAL_A_B_WORKING_PREPARED.kml` is deterministisch uit het masterregister opgebouwd en bevat exact twee hoofdlagen:

- `A_FORMEEL`: 28 groene uniforme pins;
- `B_FORMEEL`: 2 oranje uniforme pins.

De markernaam bevat waar nodig een korte Nederlandse functie. De KML bevat geen C's, stations, routes, bases, hotels of categorie-logo's.

## Integriteitscontrole

- formele A-bron = actieve A-registerrecords = A-placemarks: 28;
- formele B-bron = actieve B-registerrecords = B-placemarks: 2;
- dubbele niet-lege LOCATION_ID's: 0;
- dubbele registry-record-ID's: 0;
- ontbrekende coördinaten: 0;
- stille weglatingen: 0.

END_OF_ARTIFACT
