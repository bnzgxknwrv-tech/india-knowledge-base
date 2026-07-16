# 05 — WORKING_GEO and map readiness

## LOCATION_ID-integriteit

- Braj 200–228 is ongewijzigd.
- Corridorlocaties 300–315 zijn sequentieel en uitsluitend binnen blok 300–399 uitgegeven.
- Kumaon-seeds 400–426 zijn ongewijzigd.
- Geen ID is hergebruikt of over een blokgrens geschreven.
- Anandamayi Ma Samadhi in Kankhal en alle formele A-locaties buiten toegewezen blokken staan als `BLOCK_RESERVATION_REQUIRED`.

## GEO-status

Veertig records hebben een gelabeld `WORKING`-punt voor globale route- en kaartanalyse:
- zestien corridor/stations/contextrecords;
- de twee formele Vrindavan-A's;
- de formele Kumaon A/B/C-records die voor de corridorbeslissing relevant zijn;
- Radha Raman Temple als bestaande formele B.

De punten zijn gebouw-, terrein-, station- of landschapscentra met een zichtbare nauwkeurigheidsklasse. Zij zijn geen claim dat de bezoekersingang exact is vastgesteld. Alle punten moeten vóór praktisch routegebruik worden hercontroleerd.

## Centrale kaartbron

`central_map_source.jsonl` bevat:
- alle 28 formele A-locaties;
- beide formele B-locaties;
- alle vier formele C-locaties;
- corridorstations en routecontext;
- de Kankhal-gate-pass met ontbrekende blokreservering.

Formele locaties buiten Braj en Kumaon blijven zichtbaar zonder tijdelijk permanent nummer.

## KML

`corridor_working.kml` is technisch valide XML en bevat uitsluitend records met een toegewezen LOCATION_ID en een bruikbaar WORKING-punt. De KML is voorlopig:
- groen: formele A;
- oranje: formele B-laag;
- rood: formele C/context;
- blauw: corridor en stations.

GEO-status staat afzonderlijk in iedere markerbeschrijving. De KML is geen definitieve volledige projectkaart zolang blokken voor Bodh Gaya, Varanasi, Agra en Haridwar/Kankhal ontbreken.

END_OF_ARTIFACT