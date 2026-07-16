# 02 — Stations, cities and route zones

## Vertrek

- Mathura Junction (LOCATION_ID 300, hoofdstation, toegang voor Vrindavan): meest robuuste algemene spoorpoort.
- Mathura Cantt (LOCATION_ID 301, kleiner station, Ramnagar-treinlead): uitsluitend gebruiken na controle van trein 15055 of opvolger.
- Het lokale station Vrindavan is geen betrouwbare doorgaande vertrekbasis voor deze corridor.

## Directe corridor

- Gajraula (LOCATION_ID 304, weg-/spoorknooppunt): geen zware spirituele kandidaat gevonden.
- Moradabad Junction (LOCATION_ID 305, spoorwegknooppunt, Kumaon-overstap): sterk vervoersknooppunt; geen zware kandidaat.
- Rampur Junction (LOCATION_ID 306, aftakking richting Kumaon): vervoersrelevant; geen zware kandidaat.
- Rudrapur City (LOCATION_ID 307, station en vlakteknooppunt): praktisch tussenpunt; geen zware kandidaat.
- Lal Kuan Junction (LOCATION_ID 308, station, Kumaon-vertakking): mogelijke aankomst/overstap; geen zware kandidaat.
- Haldwani (LOCATION_ID 309, stad, poort naar Kumaon): logische wegpoort; geen nieuwe zware kandidaat.
- Kathgodam (LOCATION_ID 310, eindstation, poort naar de heuvels): logische spoorpoort; geen nieuwe zware kandidaat.

## Kasganj/Bareilly-vergelijking

- Kasganj Junction (LOCATION_ID 311, spoor-/wegknooppunt): vergelijking voor NH530B en beperkt rail.
- Soron Shukar Kshetra (LOCATION_ID 312, regionale Varaha/Ganga-pelgrimsplek): contextlocatie; zware poort niet gehaald.
- Bareilly Junction (LOCATION_ID 313, spoorwegknooppunt): bruikbaar overstappunt.
- Dargah-e-Ala Hazrat (LOCATION_ID 315, soefi-schrijn, Ahmad Raza Khan/Barelvi): transnationaal belangrijk binnen de Barelvi-traditie; als `EXCEPTION_B_CANDIDATE` bewaard, niet als routebepalende zware A.
- Ramnagar (LOCATION_ID 314, station, westelijke Kumaon): bruikbaar voor westelijke aankomst maar niet universeel voor Marks Kumaon-A's.

## Delhi-vergelijking

- New Delhi Railway Station (LOCATION_ID 302, station, Shatabdi): sterke treinverbinding maar grote terugrit.
- YSS Noida Ashram (LOCATION_ID 303, Yogananda-ashram, Kriya/YSS): directe persoonlijke lijn technisch bevestigd, maar modern filiaal en route-omweg; geen reden om deze corridor te onderbreken.

## Buiten de corridor

Anandamayi Ma Samadhi in Kankhal (samadhi, Anandamayi Ma) haalt inhoudelijk de directe-persoonlijke-lijnpoort. De plek ligt echter ver buiten de snelste route. Zij krijgt geen verzonnen LOCATION_ID; `BLOCK_RESERVATION_REQUIRED` is geregistreerd.

Per routezone zijn de negatieve zoekresultaten en overnachtingsredenen machineleesbaar vastgelegd in `route_zones.jsonl` en `negative_searches.jsonl`.

END_OF_ARTIFACT