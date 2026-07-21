# Formele A/B-dekking — VARANASI-COMPLETE-001 ZILVER

## Telling en kleurcontrole

- formele A in `LOCKED_A.md`: 28;
- actieve A-records in `shared/MASTER_A_B_GEO_REGISTRY.jsonl`: 28;
- A-placemarks in voorbereide KML: 28;
- formele B in `LOCKED_B.md`: 2;
- actieve B-records in masterregister: 2;
- B-placemarks in voorbereide KML: 2;
- totaal placemarks: 30.

## Stijlen

- `A_FORMEEL` gebruikt uitsluitend `#A_GREEN`, KML-kleur `ff00aa00` en de groene Google-pushpin;
- `B_FORMEEL` gebruikt uitsluitend `#B_ORANGE`, KML-kleur `ff00a5ff` en de oranje Google-pushpin;
- geen C-folder, station, route, basis, hotel of categorie-icoon aanwezig.

## Referentiële integriteit

- unieke `registry_record_id`: 30;
- dubbele niet-lege LOCATION_ID's: 0;
- ontbrekende coördinaten: 0;
- stille weglatingen: 0;
- bestaande Kumaon-LOCATION_ID's ongewijzigd;
- formele statuswijzigingen door ZILVER: 0.

## GEO-controle

De 30-puntenkaart is technisch en semantisch bruikbaar als repositorybrede formele A/B-werkkaart. De zeven Varanasi-A-punten zijn onafhankelijk heropend. Mahabodhi/Bodhiboom en Katyayani Peeth zijn aanvullend tegen institutionele/UNESCO-bronnen gecontroleerd. De resterende reeds gevalideerde Kumaon-, Braj- en Agra-punten zijn niet hernummerd of inhoudelijk herbeoordeeld. Werkpunten blijven zichtbaar als `WORKING_*` of `APPROXIMATE_*`; er is geen ingangsprecisie geclaimd.

Resultaat: `PASS`.

END_OF_ARTIFACT