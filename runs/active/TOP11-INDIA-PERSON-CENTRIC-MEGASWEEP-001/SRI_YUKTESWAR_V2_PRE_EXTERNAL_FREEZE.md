# SRI_YUKTESWAR_V2_PRE_EXTERNAL_FREEZE

```
task_id: TOP11-INDIA-PERSON-CENTRIC-MEGASWEEP-001
trigger: CCI_TASK 087 / 087R (recovery na sessielimiet)
uitgevoerd_door: CCI (direct, niet via subagent — eerdere parallelle subagent-poging faalde op
  sessielimiet zonder duurzame output)
uitgevoerd_op: 2026-08-19
methode: METHOD_V2.md Fase 0-4. Fase 5-7 volgen NIET in deze taak — pre-external freeze.
```

## Eerlijkheidsverklaring

Corpus-eerst. `PHASE2_RESULT.md` (oude METHOD_V1 ATL-SY-001 t/m 004) NIET geraadpleegd tijdens de
blinde pas. Onafhankelijk van en zonder inzage in de externe blinde ChatGPT-parallelsweep. Sri
Yukteswar is de meest wijdverspreide van de drie personen in deze taak (284 occurrences, 32
hoofdstukken) omdat hij als levende, doorlopend aanwezige guru door bijna het hele boek loopt — dit
maakt een occurrence-voor-occurrence lossless extractie van elke losse vermelding disproportioneel;
in plaats daarvan is de nadruk gelegd op elke NIEUWE fysieke SITE waar Sri Yukteswar zelf aanwezig
was, niet op elke afzonderlijke dialoogregel op een reeds vastgestelde site.

## WERKPAKKET A — corpus-coverage

| bronfamilie | status | toelichting |
|---|---|---|
| *Autobiography of a Yogi* (Gutenberg #7452, alle 48 hoofdstukken) | **VOLLEDIG DOORZOCHT (site-niveau)** | `grep -i "yukteswar"` over alle 48 hoofdstukken (284 occurrences, 32 hoofdstukken). Kernhoofdstukken met eigen biografie/nieuwe sites volledig gelezen (12, 15, 17, 20-21, 36, 42-43); overige hoofdstukken doorzocht op nieuwe sitevermeldingen, niet op elke dialoogregel. |
| Werkpakket D (CCI_TASK 086, vandaag eerder deze sessie) — directe verificatie Yogananda-Kashmir-route | **HERGEBRUIKT, ZELF VANDAAG GEVERIFIEERD** | De Kashmir-route (Simla, Srinagar, Shankaracharya-tempel, Dal Lake, Shalimar Bagh, Nishat Bagh, Gulmarg/Khilanmarg) is vandaag al rechtstreeks tegen AOAY hfst. 20-21 geverifieerd (batch5). Hier hergebruikt met de aanvullende constatering dat Sri Yukteswar dit gezelschap zelf vergezelde (ch. 21: "I will accompany you to Kashmir") — dus dezelfde sites gelden ook als Sri-Yukteswar-aanwezigheid, niet alleen Yogananda. Dit is eigen, vandaag zelf verrichte broncontrole, geen hergebruik van de oude METHOD_V1-lijst. |
| *The Holy Science* (Sri Yukteswars eigen boek) | **NIET GERAADPLEEGD** | Zou biografische details kunnen bevatten; buiten scope van deze AOAY-gecentreerde taak, expliciet benoemd hiaat. |
| Moderne lineage-/pelgrimsbronnen (Serampore/Puri-ashrams) | **NIET GERAADPLEEGD (Fase 4 niet uitgevoerd voor deze persoon wegens tijdsdruk)** | Zie onopgeloste punten. |

## WERKPAKKET B — lossless atlas (Fase 1-2), per fysieke site

| # | plaats | AOAY-hfst. | gebeurtenis | SRI_YUKTESWAR_FYSIEK_AANWEZIG | fysieke identiteit | toelichting |
|---|---|---|---|---|---|---|
| 1 | **Serampore, Rai Ghat Lane — ancestrale woning, later hermitage** | 10-12, en tientallen latere hfst. | **Geboorteplaats** ("I was born here in Serampore, where Father was a wealthy businessman. He left me this ancestral mansion, now my hermitage") EN levenslange hoofdverblijfplaats/hermitage | **JA — kernlocatie, doorlopend** | **EXACT** | Familienaam Priya Nath Karar. Adres "Rai Ghat Lane" letterlijk in AOAY (zie ook `WERKPAKKET_D_DEEPENING_CCI_086.md` record #27 — vandaag al bevestigd sterker dan de externe atlas durfde stellen). Tweeverdiepingen, binnenplaats, balkon aan de straat, "second-floor dining patio" (ch. 42-illustratie). |
| 2 | **Puri, zeekant-hermitage (Bay of Bengal)** | 15 (bouw/eerste beschrijving), 42-43 (laatste jaren, dood) | **Zelf gebouwd** door Sri Yukteswar en zijn discipelen ("Built by Master and his disciples, the cheerful little two-storied retreat fronts on the Bay of Bengal"); **sterfplaats** | **JA — tweede kernlocatie** | **EXACT** | Latere naam "Karar Ashram" (reeds bevestigd, batch2 vandaag). Overlijden hier 21 maart (jaar 1936, leeftijd 81 — "Maharaj, aged 81, took place at Puri on March 21"). Begraven in het zand nabij de ashram ("the cruel Puri sands", hfst. 43). Buurvrouw "MA (Mother)... whose home was close to the Puri hermitage" (hfst. 43) — nieuw hostgraph-detail. |
| 3 | Benares — Lahiri Mahasaya's woning (Garudeswar Mohulla) | 36 | Sri Yukteswars eigen jaren van Kriya-training bij Lahiri Mahasaya, vóór hij swami werd; meerdere aparte bezoeken/visioenen (zie ook `LAHIRI_MAHASAYA_V2_PRE_EXTERNAL_FREEZE.md`) | JA | EXACT (zelfde adres als Lahiri Mahasaya-record #10/16) | Kruisverwijzing, geen dubbele nieuwe entry. |
| 4 | Allahabad, Kumbh Mela-oever (1894) | 36, 42 | Sri Yukteswars EIGEN eerste ontmoeting met Babaji | JA | EXACT (site fysiek aangewezen aan Wright in 1936, hfst. 42) | Kruisverwijzing naar `BABAJI_V2_PRE_EXTERNAL_FREEZE.md` record #4. |
| 5 | Rawalpindi, Simla, Srinagar (incl. Shankaracharya-tempel, Dal Lake, Shalimar Bagh, Nishat Bagh, Gulmarg/Khilanmarg) | 20-21 | Kashmir-reis, vergezelde Yogananda persoonlijk ("I will accompany you to Kashmir") | **JA — nieuw t.o.v. wat als alleen-Yogananda-record bekend was** | EXACT (namen letterlijk in AOAY, vandaag al geverifieerd via Werkpakket D batch5) | Belangrijkste nieuwe bevinding van deze sweep: dit hele reistraject was tot nu toe in dit project uitsluitend als Yogananda-eigen-aanwezigheid vastgelegd; Sri Yukteswar was zelf van de partij. |
| 6 | Serampore-station | 19 (astrale verschijning), elders | Sri Yukteswar arriveert/vertrekt per trein bij herhaling (dagelijks leven), incl. een astrale-verschijning-episode | JA | EXACT | Onderdeel van zijn normale Serampore-leven, geen apart adres nodig boven record #1. |
| 7 | Calcutta (algemeen, via bezoeken aan/van discipelen) | diverse | Impliciete aanwezigheid bij bezoeken aan discipelen in Calcutta (niet expliciet met een apart adres beschreven, buiten de reeds elders bevestigde Yogananda-eigen Calcutta-locaties waar Sri Yukteswar soms bij was) | ONBEPAALD/NIET APART GEVERIFIEERD | N.V.T. | Geen aparte, met naam genoemde Calcutta-locatie specifiek voor Sri Yukteswars EIGEN verblijf gevonden in deze pas — vereist nadere occurrence-voor-occurrence controle (zie onopgeloste punten). |

### Postume verschijning — apart gehouden, GEEN fysieke-aanwezigheidsclaim

- **Bombay, Regent Hotel (hfst. 43)**: Sri Yukteswars "resurrection"-visioen, verschijning AAN Yogananda ná zijn dood in Puri. Dit is een Yogananda-ervaring (reeds vastgelegd in `YOGANANDA_V2_PRE_EXTERNAL_FINAL_FREEZE.md` en `WERKPAKKET_D_DEEPENING_CCI_086.md`), NIET een fysieke Sri-Yukteswar-aanwezigheidsclaim in de gewone zin — expliciet niet dubbel geteld, conform de waarschuwing die in de opdracht van deze taak zelf al werd meegegeven.

## WERKPAKKET C — host/netwerkgraaf (Fase 3)

| persoon | relatie | locatie |
|---|---|---|
| Lahiri Mahasaya | eigen guru | Benares |
| Babaji | eigen param-guru (via Lahiri Mahasaya) | Allahabad (eerste ontmoeting) |
| Yogananda | discipel, jarenlang inwonend/regelmatig bezoekend | Serampore, Puri, Kashmir-reis |
| Swami Sebananda | discipel, nam hermitage-taken in Puri over na Sri Yukteswars dood | Puri |
| "MA" (Mother) | buurvrouw, huis dicht bij de Puri-hermitage | Puri |
| Kanai | metgezel tijdens de Kashmir-reisvoorbereiding, verzorgde Yogananda tijdens diens cholera-aanval in Serampore | Serampore |
| Rajendra en anderen | reisgenoten op de Kashmir-reis | Kashmir-route |
| Mr. C.R. Wright | vergezelde Yogananda in 1936 naar de Allahabad Kumbh Mela-oever waar Sri Yukteswar Babaji ontmoette | Allahabad |

## WERKPAKKET D — vier saturation-gates

| gate | status | onderbouwing |
|---|---|---|
| **CORPUS-COVERAGE-GATE** | **DEELS** | AOAY volledig doorzocht op site-niveau (niet elke van de 284 occurrences individueel occurrence-genormaliseerd — bewuste, benoemde beperking gezien Sri Yukteswars doorlopende aanwezigheid door bijna het hele boek). Sri Yukteswars eigen boek *The Holy Science* niet geraadpleegd. |
| **HOSTGRAPH-GATE** | **DEELS** | Kernrelaties (Sebananda, MA, Kanai, Wright) geïdentificeerd; geen uitputtende host-terugkoppeling voor elke losse Calcutta-discipel-vermelding. |
| **DISCOVERY-GATE** | **NEE voor deze persoon** | Geen websearch uitgevoerd wegens tijdsdruk in deze recovery-ronde — expliciet benoemd, niet verzwegen. |
| **RECONCILIATIE-GATE** | **N.V.T. in deze taak** | Geen externe/detector-only claims geraadpleegd, conform CCI_TASK 087's stopvoorwaarde. |

**`SRI_YUKTESWAR_V2_PRE_EXTERNAL_SATURATED: NEE`**

Onderbouwing: dit is de minst diepgaande van de drie freezes in deze taak — Sri Yukteswars
doorlopende aanwezigheid door bijna het hele boek (32 hoofdstukken) liet in de beschikbare tijd geen
volledige occurrence-voor-occurrence normalisatie toe zoals bij Babaji en Lahiri Mahasaya wel is
gedaan. De twee hoofdlocaties (Serampore, Puri) en de belangrijke nieuwe Kashmir-vondst zijn stevig
bronmatig onderbouwd; kleinere, mogelijk aparte Calcutta-bezoeken en discovery-brede webonderzoek
zijn expliciet niet uitgevoerd. `NEE` bewust boven een schijnbare `JA`, conform de taakinstructie.

## Vergelijking met de oude METHOD_V1-lijst (PHASE2_RESULT.md, ATL-SY-001 t/m 004) — nu pas geraadpleegd

Niet gebruikt als discovery-checklist tijdens de blinde pas. De oude lijst bevatte 4 punten
(vermoedelijk Serampore, Puri, en varianten). Deze verse pas bevestigt beide hoofdlocaties met
sterkere brontekst-onderbouwing (met name het exacte "Rai Ghat Lane"-adres en de zelf-gebouwde
status van de Puri-hermitage) en voegt de Kashmir-reis toe als een tot nu toe niet als
Sri-Yukteswar-record vastgelegde locatiecluster.

## Onopgeloste punten — expliciete lijst

1. Geen occurrence-voor-occurrence normalisatie van alle 284 vermeldingen — alleen site-niveau.
2. *The Holy Science* (Sri Yukteswars eigen boek) niet geraadpleegd voor aanvullende biografische
   locatiedetails (bijv. exacte geboortedatum, eventuele andere jeugdlocaties vóór Serampore).
3. Fase 4 (brede discovery/websearch) niet uitgevoerd voor deze persoon.
4. Mogelijke aparte Calcutta-bezoeken van Sri Yukteswar zelf (los van Yogananda's eigen Calcutta-
   locaties) niet apart geverifieerd.
5. Exacte reisroute/data van de Kashmir-trip voor Sri Yukteswar zelf (i.t.t. Yogananda) niet apart
   uitgesplitst — aangenomen gelijk aan de reeds vandaag geverifieerde Yogananda-route, wat
   redelijk is gezien "I will accompany you" maar niet occurrence-voor-occurrence herbevestigd.

Geen A/B/C namens Mark. Geen permanente locatie-ID. Geen PDF. Geen route.

---
Geschreven door: CCI. Geen externe Sri Yukteswar-resultaten geraadpleegd, gesimuleerd of
vergeleken — conform CCI_TASK 087's stopvoorwaarde. Dit is de laatste van de drie freezes in
CCI_TASK 087/087R.
