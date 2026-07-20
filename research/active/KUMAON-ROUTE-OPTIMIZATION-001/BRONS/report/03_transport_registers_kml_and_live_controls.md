# 03 — Transportregisters, KML en live controles

## Aanbevolen treinen

- 12040 NDLS–KGM op 20 december 2026.
- 12092 HDW–HW op 3 januari 2027.
- 18478 HW–MTJ op 6 januari 2027.

Voor elk segment zijn beginstation, alle tussenstops, eindstation, stationcode, volgorde, huidige tijden, stopduur en Marks instap/uitstap vastgelegd in `train_stops.jsonl`.

## Kaartcontract

`kml_route_input.jsonl` levert technische input voor:

- ROUTE_VOLGORDE;
- BASES_EN_OVERNACHTING;
- TREINTRAJECTEN;
- TREINSTATIONS_GRIJS.

Iedere treinhalte gebruikt dezelfde grijze markerstijl en één herkenbaar treinlogo. Een halte is alleen transport- en detectorinput. Zij wordt nooit automatisch kandidaat, A, B of C.

De permanente Kumaon-LOCATION_ID's blijven ongewijzigd. Voor stations buiten de bestaande 308–310-reeks zijn coördinaten nog niet betrouwbaar gepind; dat is een blokkerende controle vóór de finale KML.

## Tijdgevoelige onderdelen

Dienstregelingen, fares, beschikbaarheid, platformen, vliegvoorwaarden, bagageregels, winterwegen, taxi's, parking, trails en toegang zijn geen blijvende feiten. `live_recheck_register.jsonl` bevat tien concrete controles met datum en blokkeringsstatus.

## Fares en kosten

Alle bedragen zijn snapshots, niet boekprijzen. De trein blijft in de huidige vergelijking duidelijk goedkoper dan de vlucht wanneer 23 kg ruimbagage wordt meegerekend. ZILVER moet de totale rekensom opnieuw opbouwen uit actuele, onafhankelijke bronnen.

END_OF_ARTIFACT
