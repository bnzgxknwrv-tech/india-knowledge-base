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

## DELTA — CCI_TASK 090 (2026-08-19, bronherstelpas)

Deze paragraaf is een toevoeging bovenop het bovenstaande, niet een overschrijving. Zie
`runs/active/TOP11-NKB-RAMDASS-CORE-SOURCE-RECOVERY-001/SOURCE_RECOVERY_RESULT.md` voor de volledige
bronroute-documentatie.

### Titelcorrectie — belangrijkste bevinding van deze pas

"Sacred Wanderer" (genoemd in TASK.md van CCI_TASK 089 als mogelijke kernbron) bleek bij nader
onderzoek **niet van Ram Dass** te zijn. *The Sacred Wanderer* is een boek van **Ravi Dass**, een
andere Neem-Karoli-Baba-devotee — een naamsverwisseling. De correcte kernbiografische bron is
**"Being Ram Dass"** (2021, Sounds True, met Rameshwar Das), zijn postume definitieve memoire. Dit
corrigeert de aanname in de Eerlijkheidsverklaring en Werkpakket A hierboven zonder die tekst stil
te overschrijven.

### WERKPAKKET A — herziene corpus-coverage

| bronfamilie | status (090) | toelichting |
|---|---|---|
| *Be Here Now* (Ram Dass, 1971) | `FULL` (was `BRON_GEBLOKKEERD`) | Volledige tekst gevonden en gedownload via archive.org/details/be-here-now-pdfdrive — een volledig open "Community Texts"-item, geen login/omzeiling nodig. 17.535 regels platte tekst, corpusbreed doorzocht op India-plaatstermen. |
| "Being Ram Dass" (2021, Rameshwar Das) — **vervangt de foutieve "Sacred Wanderer"-aanname** | `PARTIAL` | Eén legaal uitgeversfragment (Tricycle) hersteld; volledige tekst niet vrij toegankelijk (recente titel, nog onder copyright). |

### WERKPAKKET B — nieuwe lossless atlasrecords uit *Be Here Now* en "Being Ram Dass"

| # | plaats | staat/district | type | gebeurtenis/periode | PERSONALLY_PRESENT | PHYSICAL_IDENTITY | bron |
|---|---|---|---|---|---|---|---|
| 6 | Amarnath Cave | Kashmir | grot/pelgrimsoord | Te paard bezocht tijdens een pre-guru pelgrimstocht met een reisgenoot, vóór de ontmoeting met Neem Karoli Baba | JA | EXACT | *Be Here Now*, regel 770 |
| 7 | Benares (Varanasi), niet-gespecificeerde locatie | Uttar Pradesh | stad (algemeen) | Bezocht in dezelfde pre-guru reissequentie, vóór doorreis naar Nepal | JA | ALLEEN_PLAATS | *Be Here Now*, regel 770-771 |
| 8 | Sarnath | Uttar Pradesh (bij Varanasi) | Chinees-boeddhistisch klooster | Verblijf van "een paar weken", vóór de ontmoeting met Neem Karoli Baba | JA | EXACT | *Be Here Now*, regel 988 |
| 9 | Delhi — Connaught Place, American Express-kantoor, visumkantoor, ongenoemd vegetarisch restaurant, ongenoemd boeddhistisch klooster (één nacht) | Delhi | stad + meerdere sublocaties | 12 uur durende bustocht om zijn visum te regelen, ná de eerste ontmoeting met Maharaj-ji; loopt blootsvoets en zwijgend rond | JA | DEELS (Connaught Place EXACT als buurt; overige sublocaties ALLEEN_PLAATS, geen namen) | *Be Here Now*, regel 967-1001 |
| 10 | Onbenoemde tempel/veld, "3 mijl" per Land Rover van een beeldhouwersverblijf | Uttarakhand, voetheuvels Himalaya | tempel/veld | Eerste ontmoeting met Neem Karoli Baba, incl. "je-moeder-is-overleden"-episode; zeer waarschijnlijk dezelfde plek als bestaande record 2 (Kainchi Dham), maar bron gebruikt de naam "Kainchi" zelf niet | JA | ALLEEN_PLAATS (geen naamsanker in déze bron; naam wordt wel bevestigd door record 13 hieronder) | *Be Here Now*, regel 1093-1180, 1273 |
| 11 | Forestry camp (onbenoemd) | Uttarakhand (heuvelgebied) | verblijfplaats | Zie identieke NKB-freeze-record 20 (gedeelde sublocatie) | JA | ALLEEN_PLAATS | *Be Here Now*, regel 1440-1468 |
| 12 | Onbenoemde "estate" bij een niet-genoemde "town near-by" | Uttarakhand (heuvelgebied) | landgoed/verblijfplaats | Zie identieke NKB-freeze-record 21 (gedeelde sublocatie); ook plaats van de moeder-visioen-episode | JA | ALLEEN_PLAATS | *Be Here Now*, regel 990-1005 |
| 13 | K.K. (Krishna Kumar) Sah's familiehuis, nabij Nainital | Nainital-district, Uttarakhand | privéwoning | Ram Dass hier ontvangen en gevoed ("double roti") kort na de eerste ontmoeting; K.K. vertaalde het eerste gesprek met Maharaj-ji | JA | DEELS (huis zelf ongenoemd bij naam/adres, "nabij Nainital" wel expliciet) | *Be Here Now*, regel 17000-17022 (50-jarig-jubileum-nawoord, zelfde editie/tekstbestand) |
| 14 | Kainchi (naamsbevestiging, geen los occurrence-record) | Nainital-district, Uttarakhand | naambevestiging bij bestaande record 2 | Fotobijschrift: "Ram Dass and his teacher Maharaj-ji in Kainchi, India" — bevestigt de naam voor de in record 10 beschreven ontmoetingsscène via een onafhankelijke tweede bron | JA | EXACT (naambevestiging) | "Being Ram Dass" (2021), tricycle.org/article/being-ram-dass-excerpt/ (fotobijschrift) |

### Aanvullende negatieve bevindingen (aanvulling op de bestaande lijst hierboven)

- **Sewalti Hotel**: verblijfplaats tijdens het vijfdaagse seminar met Bhagwan Dass, direct na de
  Blue-Tibetan-ontmoeting in Kathmandu. Land/plaats niet ondubbelzinnig vastgesteld binnen de
  brontekst (context suggereert mogelijk nog Nepal) — **niet als India-record opgenomen**, geen gok.
- **Badrinath**: uitsluitend genoemd als achtergrond over K.K. Sah's vaders politiefunctie (opende/
  sloot de tempel jaarlijks) — geen Ram-Dass-aanwezigheidsrecord, uitgesloten als context-only.
- **Dalai Lama-bezoek**: genoemd zonder plaatsnaam — niet geregistreerd, geen Dharamsala-aanname.
- Zes maanden yoga-/meditatietraining in de "Himalaya foothills" vóór 1968 ("Being Ram Dass",
  Tricycle-fragment) is inhoudelijk consistent met de reeds bekende sadhana-periode bij record 2
  (Kainchi Dham) — behandeld als corroboratie van bestaande record 2, niet als nieuw record.

### WERKPAKKET D — herziene saturation-gates

| gate | status (090) | onderbouwing |
|---|---|---|
| **CORPUS-COVERAGE-GATE** | **DEELS** (was `NEE`) | *Be Here Now* — Ram Dass' belangrijkste eigen bron — is nu volledig doorzocht. "Being Ram Dass" (2021) is pas gedeeltelijk bereikt (één fragment). |
| **HOSTGRAPH-GATE** | **DEELS** | K.K. Sah (vertaler/gastheer) toegevoegd aan het netwerk; zie Werkpakket C-aanvulling hieronder. |
| **DISCOVERY-GATE** | **DEELS** | Volledige corpusdoorzoeking van *Be Here Now* uitgevoerd; "Being Ram Dass" nog niet volledig; maharajji.love nog steeds niet doorzocht. |
| **RECONCILIATIE-GATE** | **N.V.T. in deze taak** | Geen externe/IndiaROOD-claims geraadpleegd, conform de blindheidsgrens van CCI_TASK 090. |

**`RAM_DASS_V2_PRE_EXTERNAL_SATURATED: NEE`** — ongewijzigd. Onderbouwing: de recordcount groeide
van 5 naar 13 (plus één naamsbevestiging), maar drie locaties blijven onbenoemd in de brontekst
(records 10-12) en de tweede kernbiografie ("Being Ram Dass") is nog niet volledig doorzocht. Een
schijnbare `JA` op basis van een gedeeltelijk gedekt corpus zou de eerlijkheidsnorm van dit project
tegenspreken.

### WERKPAKKET C — aanvulling host/netwerkgraaf

| persoon | relatie | locatie |
|---|---|---|
| K.K. (Krishna Kumar) Sah | vertaler bij eerste ontmoeting, gastheer | nabij Nainital |
| Bina (K.K.'s zus) | gastvrouw, bereidde maaltijden | K.K.'s familiehuis, nabij Nainital |
| Bhawani Das Sah (K.K.'s vader) | Circle Inspector of Police, Kumaon-heuveldistrict; contact met Maharaj-ji vóór K.K.'s geboorte | Kumaon-heuvels (Badrinath-toezicht als contextvermelding, geen eigen aanwezigheidsrecord) |
| Bhagwan Dass (reisgenoot) | introduceerde Ram Dass bij Maharaj-ji | Kathmandu (ontmoeting) → Amarnath/Benares (gedeelde reis) → eerste-ontmoetingsscène |

Checkpoint: Ram-Dass-source-recovery, CCI_TASK 090, checkpoint 2/2.

## DELTA — CCI_TASK 091 (2026-08-19, externe reconciliatie)

Volledige reconciliatie tegen de externe `agent/chatgpt-top11-parallel-sweep`-freeze (57 records):
zie `runs/active/TOP11-NKB-RAMDASS-EXTERNAL-RECONCILIATION-001/RAM_DASS_RECONCILIATION.md` en
`RECONCILIATION_MATRIX.jsonl`. Deze paragraaf registreert alleen de overgenomen toevoegingen/
correcties zonder de bovenstaande rows stil te overschrijven.

**Nieuwe sublocaties, Tier-1 bevestigd in de eigen reeds gedownloade *Be Here Now*-tekst**:
1. **"Health Department"-kantoor, Delhi** — woordelijk teruggevonden op regel 1373 van
   `be_here_now.txt`. Sublocatie van het bestaande Delhi-record.
2. **Rivier-badplaats bij Kainchi** — woordelijk teruggevonden op regel 1508: "I would get up
   early, take my bath in the river or out...". Nieuwe sublocatie bij record 2 (Kainchi Dham).
3. **Appelboomgaard-tussenstop** — extern splitst dit terecht als apart record vóór het Forestry
   camp (record 11/090); toegevoegd als sub-stap in dezelfde route.

**Overgenomen, niet volledig geverifieerd**:
4. **Kausani/Anasakti Ashram**: extern koppelt het gehuurde huis inferentieel aan Anasakti Ashram
   (Gandhi-verbonden) — overgenomen als aanvullende, niet volledig bewezen naamskoppeling naast het
   bestaande "gehuurd huis"-record.

**Expliciet NIET overgenomen (fout gevonden)**:
5. **Jagannath Puri-strandwandeling**: de externe freeze citeert Sara Davidson met de quote
   "walking on the beach in Jaganath Puri", maar deze quote staat **niet** in de twee door de
   externe freeze zelf aangehaalde SD-bronnen (saradavidson.com/ram-dass-does-a-saint-get-angry/
   en beezone.com/ramdass/ram_dass_history.html) — beide volledig gedownload en doorzocht op
   "Puri" en "beach", nul treffers. Geregistreerd als `FALSE_OR_UNSUPPORTED_EXTERNAL_CLAIM`,
   conform het Yogananda-precedent. Niet als locatie toegevoegd.

**Cross-persoon bevestigd**: Auroville-bezoek (december 1992) rechtstreeks bevestigd via de
officiële Auroville-pagina — dit is een geheel nieuwe, extern-only locatie voor Ram Dass buiten de
Kainchi/NKB-lijn, niet toegevoegd als los record binnen deze taak (behoort tot een bredere
levensfase-inventarisatie) maar wel als geverifieerd feit vastgelegd in de reconciliatiedoc.

**Herziene gates**: CORPUS-COVERAGE-GATE blijft **DEELS** (ongewijzigd t.o.v. 090). HOSTGRAPH-GATE
**DEELS** (Mr. Soni, Sathya Sai Baba-kring, Sri Aurobindo Ashram-gemeenschap als nieuwe leads).
`RAM_DASS_SATURATED: NEE` blijft de eerlijke uitkomst.

Checkpoint: Ram-Dass-externe-reconciliatie, CCI_TASK 091, checkpoint 2/2.
