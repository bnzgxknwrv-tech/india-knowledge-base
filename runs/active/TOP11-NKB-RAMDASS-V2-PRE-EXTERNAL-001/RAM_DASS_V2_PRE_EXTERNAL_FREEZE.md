# RAM_DASS_V2_PRE_EXTERNAL_FREEZE

```
task_id: TOP11-NKB-RAMDASS-V2-PRE-EXTERNAL-001
cci_task: CCI_TASK 089
uitgevoerd_door: CCI
uitgevoerd_op: 2026-08-19
methode: METHOD_V2.md Fase 0-4 + interne onafhankelijke controle. Fase 5-7 volgen NIET in deze taak.
blindheid: geen externe PRE-COMPARE-freeze, geen IndiaROOD-resultaat, geen PHASE2_RESULT.md/
  METHOD_V1-lijst geraadpleegd tijdens deze pas. Geen inzage in de zojuist geschreven Neem
  Karoli Baba-freeze van deze sessie is gebruikt om Ram Dass-locaties te zaaien (afzonderlijk
  onderzocht, conform TASK.md §5 "Gekoppeld netwerk").
```

## Eerlijkheidsverklaring

Deze freeze is nog dunner onderbouwd dan de Neem Karoli Baba-freeze van dit checkpoint. Ram Dass'
eigen kernteksten — *Be Here Now* (1971, zijn eigen verslag van de India-reis en eerste ontmoeting)
en *Sacred Wanderer: An American Devotee's Story* (memoire, 2010) — waren in deze sessie NIET als
doorzoekbare volledige tekst bereikbaar (niet gevonden als vrij toegankelijke webtekst binnen de
gebruikte zoekroutes). Deze freeze steunt op secundaire biografische overzichten (Britannica,
Wikipedia, journalistieke profielen) en twee gerichte devotee-/reisverslagen (ramdass.org,
ashramsofindia.com). Corpus-coverage-gate is daarom `NEE`, sterker nog dan bij Neem Karoli Baba.

## WERKPAKKET A — corpus-coverage

| bronfamilie | status | toelichting |
|---|---|---|
| *Be Here Now* (Ram Dass, 1971) | `BRON_GEBLOKKEERD` | Niet gevonden als vrij toegankelijke volledige tekst; alleen samenvattingen/Wikipedia-artikel over het boek geraadpleegd. |
| *Sacred Wanderer: An American Devotee's Story* (2010) | `BRON_GEBLOKKEERD` | Alleen een verkoopvermelding (eBay) gevonden, geen tekst. |
| ramdass.org (officiële stichting) | `PARTIAL` | Eén pagina ("The First Meeting with Maharajji") gaf HTTP 403 (geblokkeerd voor geautomatiseerde toegang); alleen via secundaire citaties elders bereikt. |
| ashramsofindia.com (devotee-reisverslag "Hotel Evelyn") | `FULL` (dit artikel) | Concreet, gedateerd verslag met plaatsnamen. |
| Wikipedia/Britannica/journalistieke profielen | `PARTIAL` | Gebruikt voor biografisch raamwerk, niet voor occurrence-niveau detail. |
| maharajji.love (devotee-verhalenarchief) | `NIET GERAADPLEEGD` | Zelfde hiaat als bij Neem Karoli Baba. |

## WERKPAKKET B — lossless atlas (Fase 1-2)

| # | plaats | staat/district | type | gebeurtenis/periode | PERSONALLY_PRESENT | PHYSICAL_IDENTITY | bron |
|---|---|---|---|---|---|---|---|
| 1 | Delhi | Delhi | aankomstpunt | Genoemd als binnenkomstpunt voor een reisgenoot (Frank en Jan) zomer 1970; Ram Dass' eigen exacte aankomstroute/-datum voor de allereerste 1967-reis niet apart gevonden | ONZEKER (voor Ram Dass zelf specifiek) | ALLEEN_PLAATS | ashramsofindia.com (indirect, via reisgenoten) |
| 2 | **Kainchi Dham** | Nainital-district, Uttarakhand | ashram | **Kernlocatie**: eerste ontmoeting met Neem Karoli Baba, 1967 — de beroemde "je moeder is overleden"-episode; kreeg hier de naam "Ram Dass"; onderging intensieve sadhana-training; keerde in het najaar van 1971 terug voor dagelijkse darshan-bezoeken gedurende zeven weken | JA | EXACT | meerdere onafhankelijke bronnen (Britannica, ramdass.org via secundaire citaten, savetemples.org) |
| 3 | **Hotel Evelyn, Nainital** (Mall Road) | Nainital, Uttarakhand | hotel/tijdelijke "mini-ashram" | Zomer 1970 en september-november 1971 (zeven weken) verbleven hier ca. twintig westerse devotees, inclusief Ram Dass' kring, terwijl dagelijks naar Kainchi werd gereisd voor darshan; eigendom van de familie Sah | JA | EXACT | ashramsofindia.com |
| 4 | Kausani | Uttarakhand (Kumaon-heuvels) | gehuurd huis/retraiteplek | Vipassana-meditatieretraite in een gehuurd huis met uitzicht op de Himalaya, vóór de terugkeer naar Kainchi in het najaar van 1971 toen bekend werd dat Maharajji daar weer verbleef | JA | DEELS (huis niet met naam/adres geïdentificeerd, plaats wel) | ashramsofindia.com; secundaire reisverslagen |
| 5 | India (algemeen, 2004-reis) | onbepaald | laatste India-bezoek | Laatste reis naar India in 2004; opgelopen ernstige infectie na terugkeer, waarna hij aankondigde niet meer te zullen reizen; exacte binnenlandse bestemming(en) van déze specifieke reis niet gevonden | ONZEKER (India-aanwezigheid wel, exacte plek niet) | ONBEKEND | journalistieke profielen (o.a. mauinews.com-cluster) |

## Negatieve bevindingen / expliciet NIET opgenomen

- **Vrindavan Ashram, 1997**: een zoekresultaat noemt dat "de auteur" (een andere devotee, niet Ram
  Dass zelf) in 1997 in de Neem Karoli Baba-ashram in Vrindavan was en daar hoorde dat Ram Dass een
  beroerte had gehad. Dit is NIET een Ram-Dass-aanwezigheidsrecord — het is een derde persoon op een
  andere plek die nieuws over Ram Dass ontving. Expliciet uitgesloten conform de scheidingsregel in
  TASK.md §5 ("plaatsen die alleen in door hem vertelde... verhalen voorkomen" c.q. hier zelfs
  andersom: een verhaal ÓVER hem, niet van hem, elders verteld).
- **Kathmandu, Nepal**: waar Ram Dass Bhagavan Das ontmoette vóór hun gezamenlijke terugkeer naar
  India — bewaard als route-context, niet als India-atlasrecord (buiten scope conform TASK.md §5
  "buitenlandse plekken... niet als India-atlasrecord").

## WERKPAKKET C — host/netwerkgraaf (Fase 3)

| persoon | relatie | locatie |
|---|---|---|
| Neem Karoli Baba (Maharajji) | guru | Kainchi Dham |
| Bhagavan Das (Kermit Michael Riggs) | reisgenoot, introduceerde hem bij Maharajji | Nepal (ontmoeting) → Kainchi (introductie) |
| Frank en Jan (reisgenoten) | onderdeel van de Hotel Evelyn-groep, 1970 | Delhi (aankomst), Nainital |
| Familie Sah | eigenaar Hotel Evelyn | Nainital |

## WERKPAKKET D — vier saturation-gates

| gate | status | onderbouwing |
|---|---|---|
| **CORPUS-COVERAGE-GATE** | **NEE** | Beide kernteksten (*Be Here Now*, *Sacred Wanderer*) ontoegankelijk; zelfs de officiële ramdass.org-pagina over de eerste ontmoeting gaf een toegangsfout. Dit is de zwakste van alle tot nu toe uitgevoerde pre-external freezes in dit project. |
| **HOSTGRAPH-GATE** | **DEELS** | De weinige gevonden hostrelaties zijn teruggekoppeld; geenszins uitputtend. |
| **DISCOVERY-GATE** | **DEELS** | Meerdere gerichte zoekrondes (eerste ontmoeting, Be Here Now-locaties, latere reizen/beroerte/2004, sadhana-retraiteplekken); maharajji.love niet doorzocht. |
| **RECONCILIATIE-GATE** | **N.V.T. in deze taak** | Geen externe/IndiaROOD-claims geraadpleegd. |

**`RAM_DASS_V2_PRE_EXTERNAL_SATURATED: NEE`**

Onderbouwing: met slechts vijf atlasrecords (waarvan één ONBEPAALD qua locatie en één ONZEKER qua
persoonlijke aanwezigheid) is dit aantoonbaar geen uitputtende landelijke sweep. De twee
belangrijkste eigen bronnen van Ram Dass zelf ontbreken volledig. `NEE` is hier de enige eerlijke
uitkomst — een schijnbare `JA` op basis van vijf secundair-bronnige records zou de taakinstructie
(eerlijke motivatie, geen schijnzekerheid) direct tegenspreken.

## Onopgeloste punten — expliciete lijst

1. *Be Here Now* — volledige tekst niet gevonden/toegankelijk; grootste hiaat.
2. *Sacred Wanderer* (2010-memoire) — niet toegankelijk.
3. ramdass.org — herhaalde pagina's gaven toegangsfouten (403); alleen via secundaire citaten
   bereikt.
4. maharajji.love — niet doorzocht.
5. Latere levensfase (jaren '80-'90, vóór de 1997-beroerte): geen enkele aparte India-reis met
   locatie gevonden in deze ronde — waarschijnlijk bestaat die informatie wel, maar niet binnen de
   gebruikte zoekroutes gevonden.
6. 2004-reis: bevestigd dat hij naar India ging, geen enkele binnenlandse locatie gevonden.
7. Exacte aankomstroute/-datum van Ram Dass' eigen allereerste 1967-reis (i.t.t. de 1970-reisgenoten
   Frank/Jan) niet apart bevestigd.

Geen A/B/C namens Mark. Geen permanente locatie-ID. Geen PDF. Geen route. Geen externe freeze of
IndiaROOD-resultaat geraadpleegd tijdens deze pas.

---
Geschreven door: CCI. Checkpoint 2/2 (laatste persoon) van CCI_TASK 089.
