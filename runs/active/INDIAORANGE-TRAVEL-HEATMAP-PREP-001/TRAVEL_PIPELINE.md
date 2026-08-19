# TRAVEL_PIPELINE — INDIA ORANJE

Doel: minimale, verliesloze keten van persoonsreconciliatie naar uitvoerbare reisplanning, zonder A/B/C vooraf in te vullen.

## Ketting

1. **Gereconcilieerde persoonsrecords**
   - Input: uitsluitend per persoon gereconcilieerde records met expliciete gate/status.
   - Open conflicten blijven gemarkeerd; detectorfreezes gaan niet rechtstreeks door.

2. **Landelijke heatmap**
   - Agregeer per `geo_key` volgens `HEATMAP_SCHEMA.md`.
   - Produceer counts, fysieke exactheid, conflictflags en locked-ankers.
   - `travel_significance = ONBESLIST`.

3. **Regionale verificatie**
   - Pas `CLUSTER_TRIGGER_RULES.md` toe.
   - Alleen regio's met `YES` krijgen gerichte verificatie/deep sweep.
   - `DEFER` zolang persoons-/governancegates open zijn.
   - Arunachala/Tiruvannamalai blijft locked; deze pipeline start daar geen inhoudelijke regio-sweep.
   - Vivekananda/Hariharananda: geen exhaustieve landelijke deep sweep; later alleen grootste/belangrijkste bekende locaties gericht verifiëren.

4. **Mark A/B/C-besluit**
   - Eerste expliciete reiswaarderingslaag.
   - Mark bepaalt A/B/C; systeem/agent vult dit niet afgeleid in.
   - Babaji-grot Kukuchina/Dunagiri blijft bestaande hoofdreden-governance; geen nieuwe waardering door INDIA ORANJE.

5. **Route en nachten**
   - Pas ná A/B/C.
   - Cluster A/B/C-locaties geografisch; bepaal volgorde en benodigde nachten.
   - Geen route-/nachtenbesluit vóór stap 4.

6. **Transportlaag**
   - Verifieer reistijden, trein/vlucht/auto-opties, overstappen en lokale bereikbaarheid voor de gekozen route.
   - Mag route/nachten terugkoppelen als logistiek onmogelijk of disproportioneel blijkt, maar verandert A/B/C niet zelfstandig.

7. **Verblijflaag**
   - Selecteer verblijf per gekozen nachtencluster op ligging, rust, bereikbaarheid en andere later vastgestelde voorkeuren.
   - Geen verblijfsonderzoek voor regio's die nog buiten de gekozen route vallen.

8. **Dagplanning**
   - Bouw per verblijfplaats concrete dagen met volgorde, openingstijden, reistijd, rustbuffers en fallback.
   - Laat onopgeloste locatieconflicten zichtbaar; geen schijnzekerheid.

## Paralleliseerbaarheid

- **Na persoonsreconciliatie:** heatmapaggregatie kan technisch per staat/regio parallel, zolang dezelfde schema- en deduplicatieregels gelden.
- **Regionale verificatie:** meerdere `YES`-regio's kunnen parallel worden geverifieerd; locked/deferred regio's niet.
- **Mark A/B/C:** centraal beslismoment; niet parallel door agents invullen.
- **Na A/B/C:** route-/nachtenmodellering en grove transporthaalbaarheid kunnen deels parallel, maar moeten vóór definitieve route worden samengevoegd.
- **Na routefreeze:** transportdetail en verblijfsverkenning kunnen per routecluster parallel.
- **Dagplanning:** kan per verblijfcluster parallel nadat transport en verblijf voldoende stabiel zijn.

## Hard gates

`PERSON_RECONCILIATION -> HEATMAP -> REGIONAL_VERIFICATION -> MARK_A_B_C -> ROUTE_NIGHTS -> TRANSPORT -> STAY -> DAYPLAN`

Geen latere stap mag een eerdere open gate stilzwijgend overslaan. Een downstream logistieke bevinding mag terugkoppelen naar een eerdere stap, maar nooit zelfstandig een Mark-besluit vervangen.