# MASTER_INDIA_KML_LINKAGE — BRONS input

Issue-koppeling: `MASTER-INDIA-KML-001` (#17)

## Later op te nemen lagen

- A_FORMEEL: alle bestaande Kumaon-A-markers ongewijzigd.
- B_FORMEEL: bestaande B-marker ongewijzigd.
- C_FORMEEL: alle bestaande C-markers ongewijzigd.
- D_DOOR_MARK_TE_BEOORDELEN: bestaande onbeoordeelde markers; D is geen vierde klasse.
- CONTEXT_OF_AFGEVALLEN: bestaande contextmarker.
- ROUTE_VOLGORDE: volgorde uit `route_sequence.jsonl` en `kml_route_input.jsonl`.
- BASES_EN_OVERNACHTING: Bhowali 3, Almora/Kasar 5, Dwarahat 4, Haldwani 2.
- TREINTRAJECTEN: 12040 NDLS-KGM, 12092 HDW-HW, 18478 HW-MTJ.
- TREINSTATIONS_GRIJS: alle stop-instanties uit `train_stops.jsonl`, één grijze stijl en één treinlogo.
- VLIEGVELDEN_EN_VLUCHTEN: alleen vergelijking/fallback; geen aanbevolen vluchtlaag tenzij ZILVER/GOUD deze dragend houdt.

## Integriteitsregels

- Geen treinhalte krijgt een formele of adviserende A/B/C.
- Permanente LOCATION_ID's blijven behouden.
- Nieuwe externe stationpunten worden pas in finale KML gezet na WGS84-verificatie.
- De master-KML wordt in deze run niet rechtstreeks gewijzigd.
- Issue #17 wordt in deze fase niet gemuteerd.

END_OF_ARTIFACT
