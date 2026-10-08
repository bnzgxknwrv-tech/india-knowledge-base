# BABAJI_V2_PRE_EXTERNAL_FREEZE

```
task_id: TOP11-INDIA-PERSON-CENTRIC-MEGASWEEP-001
trigger: CCI_TASK 087 / 087R (recovery na sessielimiet)
uitgevoerd_door: CCI (direct, niet via subagent — eerdere parallelle subagent-poging faalde op
  sessielimiet zonder duurzame output; deze freeze is een verse, volledige METHOD_V2 Fase 0-4-pas)
uitgevoerd_op: 2026-08-18/19
methode: METHOD_V2.md Fase 0-4. Fase 5-7 (onafhankelijke tweede pas, externe multi-AI-union,
  reconciliatie) volgen NIET in deze taak — dit is een pre-external freeze, analoog aan
  YOGANANDA_V2_PRE_EXTERNAL_FINAL_FREEZE.md.
```

## Eerlijkheidsverklaring

Corpus-eerst, niet zoekmachine-eerst. `PHASE2_RESULT.md` (de oude METHOD_V1 ATL-MB-001 t/m 005)
is tijdens de blinde pas NIET geraadpleegd als discovery-checklist. Vergelijking daarmee volgt
hieronder apart, als eindnotitie, niet als sturing vooraf. Deze taak loopt bewust parallel aan en
onafhankelijk van de aparte externe blinde ChatGPT-parallelsweep (`TOP11-PARALLEL-CHATGPT-SWEEP-001`,
zie `handoffs/INDIA6_TO_INDIA7_LIVE_DELTA_2026-08-18_2359.md`) — er is geen inzage geweest in die
externe resultaten voor of tijdens deze freeze.

## Babaji-specifieke epistemische classificatie

Babaji is, in tegenstelling tot Yogananda/Sri Yukteswar/Lahiri Mahasaya, door zijn eigen traditie
bewust ahistorisch/legendarisch vormgegeven — geen geboorte-/sterftedatum, geen burgerlijke
administratie, geen onafhankelijk buiten de lineage documenteerbaar bestaan. Elke claim krijgt
daarom een expliciete tier:

**CANONIEKE OVERRIDE — MARK_DECISION 2026-08-19:** deze tiers meten uitsluitend de nabijheid en
kwaliteit van de **claimprovenance binnen een traditie**. Zij bewijzen niet dat Babaji historisch
bestond of lichamelijk op de genoemde plek aanwezig was. Zelfs tier A betekent:
`TRADITION_CLAIM_DOCUMENTED: JA`, nooit `HISTORICALLY_VERIFIED_BABAJI_PRESENCE: JA`.
Bij Babaji kan wel worden geverifieerd dat (a) een bron de claim werkelijk bevat, (b) de fysieke
site bestaat of identificeerbaar is en (c) een historisch beter documenteerbare getuige/volgeling
daar aanwezig was. Babaji's eigen aanwezigheid blijft `CLAIMED_BY_<TRADITION>` en
`HISTORICALLY_VERIFIED_BABAJI_PRESENCE: NIET_VASTSTELBAAR`. Zie
`decisions/BABAJI_MYTHIC_FIGURE_EVIDENCE_RULE_2026-08-19.md`.

- **A) DIRECTE/PRIMAIRE LINEAGE-CLAIM** — eerstehands of bijna-eerstehands verslag binnen de directe
  Kriya-lijn (Yogananda's eigen ooggetuigenverslag, of Lahiri Mahasaya's/Sri Yukteswars eigen
  getuigenis zoals rechtstreeks aan Yogananda doorverteld).
- **B) VROEGE SEMI-PRIMAIRE TRADITIE** — lineage-interne overlevering, één of meer schakels van een
  directe getuige verwijderd, maar binnen de gevestigde Kriya-transmissielijn.
- **C) LATER TRADITIONEEL/INSTITUTIONEEL** — latere institutionele associatie, herdenkingssite,
  ashram/schrijn gebouwd ter ere van een traditie, zonder directe-getuige-keten.
- **D) SYMBOLISCH/GEEN FYSIEK BEWIJS** — puur symbolische/devotionele associatie, geen claim van een
  daadwerkelijk documenteerbare fysieke ontmoeting op die plek.

## WERKPAKKET A — corpus-coverage

| bronfamilie | status | toelichting |
|---|---|---|
| *Autobiography of a Yogi* (Gutenberg #7452, alle 48 hoofdstukken) | **VOLLEDIG DOORZOCHT** | `grep -i "babaji"` over alle 48 hoofdstukken uitgevoerd (132 occurrences, 14 hoofdstukken); alle occurrence-clusters met omringende context gelezen (hfst. 13, 26, 27, 31, 32, 33, 34, 35, 36, 37, 39, 42, 43, 48). |
| YSS/SRF-lineage-publicaties buiten AOAY (o.a. Daya Mata's *Only Love*, "A Blessing from Mahavatar Babaji") | **BRON_GEBLOKKEERD/NIET GERAADPLEEGD** | Genoemd door externe bronnen als aanvullend lineage-materiaal over Babaji; niet lokaal beschikbaar, niet doorzocht in deze ronde. Expliciet benoemd hiaat, niet verzwegen. |
| YSS-ashram-index (yssofindia.org) | **DOORZOCHT (gericht, Fase 4)** | Bevestigt een modern YSS-ashram/pelgrimssite bij Dwarahat (zie hieronder), als institutionele/moderne laag boven de AOAY-tekst. |
| Algemene webbronnen over "Mahavatar Babaji Cave" | **DOORZOCHT (gericht, Fase 4)** | Eén gerichte WebSearch, ter identificatie van de moderne naam/locatie van de in AOAY beschreven grotten — niet als vervanging van de primaire brontekst, alleen als institutionele identificatielaag. |

## WERKPAKKET B — lossless atlas (Fase 1-2), alle occurrence-clusters

| # | plaats/site | AOAY-hoofdstuk(en) | gebeurtenis | tier | BABAJI_AANWEZIGHEIDSCLAIM__BRONSTATUS | toelichting |
|---|---|---|---|---|---|---|
| 1 | Drongiri Mountain-grot, bij Ranikhet (Himalaya, Almora-district) | 33, 34 (+ 32 zijdelings) | Babaji's eerste ontmoeting met Lahiri Mahasaya (1861); tempel-/paleismaterialisatie en Kriya-initiatie | **A** | CLAIM_DOCUMENTED (voor Lahiri Mahasaya's aanwezigheid; Babaji's "aanwezigheid" is per definitie van de traditie doorlopend hier) | Lahiri Mahasaya's eigen verslag, via Kebalananda én Sri Yukteswar (beiden rechtstreeks van Lahiri Mahasaya gehoord) aan Yogananda doorgegeven. Illustratie in AOAY zelf toont een foto van de grot, bezocht door Lahiri Mahasaya's kleinzoon. |
| 2 | Algemeen "de noordelijke Himalaya-toppen nabij Badrinarayan" | 33 | Babaji's blijvende, algemene verblijfsregio | **A** (voor het bestaan van de claim zelf, maar regio-niveau, geen exacte site) | ONBEPAALD/REGIONAAL | Geen specifieke site; AOAY zelf noemt dit uitdrukkelijk vaag ("moves with his group from place to place"). |
| 3 | Moradabad — huis van een Bengaalse familie | 34 | Babaji materialiseert zich op Lahiri Mahasaya's aanroep, ten overstaan van zes vrienden | **A** | CLAIM_DOCUMENTED | Lahiri Mahasaya's eigen verslag; exact huisadres niet gegeven, alleen de plaatsnaam Moradabad. |
| 4 | Allahabad, Kumbh Mela-oever (1894) | 36, 42 (retrospectief gelokaliseerd) | Sri Yukteswars eigen eerste ontmoeting met Babaji | **A** | CLAIM_DOCUMENTED | Sri Yukteswars eigen, rechtstreeks aan Yogananda verteld verslag. Exacte oeverplek in 1936 fysiek aangewezen door Yogananda aan C.R. Wright (hfst. 42) — "the site on the river bank which Yoganandaji pointed out to me as the meeting place of Babaji and Sri Yukteswarji". |
| 5 | Allahabad, Kumbh Mela (ander jaar/gelegenheid) | 34 | Lahiri Mahasaya's eigen ontmoeting met Babaji (wast voeten van een asceet) | **A** | CLAIM_DOCUMENTED | Lahiri Mahasaya's eigen verslag. Geen jaartal expliciet gegeven voor déze specifieke episode (apart van de 1861-eerste-ontmoeting). |
| 6 | Serampore — banyanboom bij de rivieroever (nabij Sri Yukteswars hermitage) | 36 | Babaji verschijnt aan Sri Yukteswar na voltooiing van diens geschriften | **A** | CLAIM_DOCUMENTED | Sri Yukteswars eigen verslag. |
| 7 | Benares — woning/parlour van Lahiri Mahasaya | 36 | Babaji verschijnt bij de deur, zichtbaar gemaakt voor Sri Yukteswar door Lahiri Mahasaya's aanraking | **A** | CLAIM_DOCUMENTED | Sri Yukteswars eigen verslag, gebeurtenis in Lahiri Mahasaya's eigen huis in Benares. |
| 8 | Barackpur (nabij Calcutta) — kamer | 31 | Babaji betreedt stilletjes de kamer waar Lahiri Mahasaya en Shankari Mai Jiew zitten | **B** | CLAIM_DOCUMENTED (voor deze getuige) | Verteld door Shankari Mai Jiew (Trailanga Swami's enige bekende levende discipel), niet rechtstreeks aan Yogananda maar als overlevering in AOAY opgenomen ("She has related that..."). |
| 9 | **Calcutta, 4 Gurpar Road — Yogananda's eigen ouderlijk huis, vestibule** | **37** | **Yogananda rapporteert dat Babaji persoonlijk aan hem verschijnt, kort vóór diens vertrek naar Amerika (1920)** | **A — sterkste claim in het hele corpus** | **CLAIM_DOCUMENTED** | Yogananda's eigen, expliciet nooit eerder aan iemand verteld ooggetuigenverslag ("Until now, I have never recounted to anyone this story of my meeting with Babaji"). Dit is de enige claim in AOAY waarbij de auteur zelf, in eigen persoon, met Babaji spreekt — sterker claimant-provenanceniveau dan alle andere records, die allemaal via Lahiri Mahasaya of Sri Yukteswar aan Yogananda zijn doorverteld. |
| 10 | Badrinarayan-omgeving, grot (exacte locatie niet gespecificeerd, "near Badrinarayan") | 42 | Babaji verschijnt aan Keshabananda in een grot (ca. 1935), met een boodschap voor Yogananda | **A** (voor Keshabananda's eigen getuigenis, rechtstreeks aan Yogananda verteld) | CLAIM_DOCUMENTED (voor Keshabananda) | Expliciet GEEN Yogananda-Babaji-ontmoeting — Sri Yukteswar had al aangegeven dat Babaji niet op de Kumbh Mela 1936 zou verschijnen, en dit wordt in de tekst zelf bevestigd. |
| 11 | Ranbajpur/Tarakeswar — Ram Gopal Muzumdars grot | 33 | Visioen van Babaji + Mataji + Lahiri Mahasaya, verteld aan Yogananda tijdens diens eigen bezoek aan Ram Gopal | **A** (Ram Gopals eigen verslag, rechtstreeks aan Yogananda) | CLAIM_DOCUMENTED (voor Ram Gopal, Lahiri Mahasaya en Mataji als getuigen) | Zelfde hoofdstuk als de reeds bevestigde Yogananda-eigen-bezoeklocatie (#34 in de eerdere Yogananda-atlas). |
| 12 | "Mataji's grot" (ongespecificeerde locatie, niet ver van Ram Gopals grot) | 33 | Babaji's vermeende zuster Mataji ontvangt Babaji en Lahiri Mahasaya in haar eigen grot | **B/C** | ONBEPAALD | Geen plaatsnaam of regio gegeven buiten "niet ver van Ram Gopal"; te vaag voor een eigen atlas-entry met fysieke identiteit. |
| 13 | Badrinarayan (algemeen) | 27 | Pranabananda zou na reïncarnatie "naar Badrinarayan zijn gegaan en zich bij de groep heiligen rond Babaji hebben gevoegd" | **D** | SYMBOLISCH | Reïncarnatieclaim, geen fysieke ontmoeting die te dateren/lokaliseren is; puur devotioneel/traditioneel. |
| 14 | **Modern/institutioneel: "Mahavatar Babaji Cave", Kukuchina, Dunagiri-berg, bij Dwarahat (ca. 25 km van Dwarahat)** | *(niet in AOAY zelf — Fase 4-vondst)* | Moderne pelgrims-/institutionele identificatie van record #1 (Drongiri-grot) als exacte hedendaagse locatie, incl. eigen YSS-ashram ter plaatse | **C** | N.V.T. (institutionele laag, geen aparte fysieke-aanwezigheidsclaim) | AOAY zelf noemt geen dorpsnaam "Kukuchina" of bergnaam "Dunagiri" — dit is een latere, buiten de primaire tekst liggende identificatie die record #1 concretiseert tot een bezoekbare hedendaagse site. Niet verward met een eigen, aparte gebeurtenis. |

## WERKPAKKET C — host/netwerkgraaf (Fase 3)

| gastheer/getuige | relatie tot Babaji-occurrence | locatie |
|---|---|---|
| Lahiri Mahasaya | centrale getuige/discipel voor records #1, #3, #5, #7-9 (indirect) | Ranikhet, Moradabad, Allahabad, Benares |
| Sri Yukteswar | centrale getuige voor records #4, #6, #7 | Allahabad, Serampore, Benares |
| Swami Kebalananda (Yogananda's Sanskrit-leraar) | tussenpersoon die record #1/#3 aan Yogananda doorvertelde, zelf ook tijd met Babaji doorgebracht "in de Himalaya" (geen exacte site) | Himalaya (onbepaald) |
| Shankari Mai Jiew (Trailanga Swami's discipel) | getuige voor record #8 | Barackpur |
| Keshabananda | getuige voor record #10 | Badrinarayan-omgeving |
| Ram Gopal Muzumdar ("de slapeloze heilige") | getuige voor record #11 | Ranbajpur/Tarakeswar |
| Ananda Mohan Lahiri (kleinzoon van Lahiri Mahasaya) | bezoeker van de Drongiri-grot (fotobijschrift, geen eigen verhaal) | Drongiri Mountain |

Geen van deze gastheren/getuigen leidt naar een nieuwe, in de tabel hierboven nog niet genoteerde
fysieke site — de host-as bevestigt vooral de reeds gevonden locaties.

## WERKPAKKET D — vier saturation-gates

| gate | status | onderbouwing |
|---|---|---|
| **CORPUS-COVERAGE-GATE** | **DEELS** | AOAY volledig doorzocht (132/132 occurrences, alle 14 hoofdstukken met context gelezen). Aanvullende lineage-publicaties (Daya Mata e.a.) buiten AOAY zijn `BRON_GEBLOKKEERD/NIET GERAADPLEEGD` — concreet benoemd, niet verzwegen. |
| **HOSTGRAPH-GATE** | **JA voor de gevonden getuigen** | Alle in AOAY genoemde getuigen/gastheren voor Babaji-occurrences zijn geïdentificeerd en teruggekoppeld aan hun eigen bekende locatie; geen aanwijzing voor gemiste hostrelaties binnen het doorzochte corpus. |
| **DISCOVERY-GATE** | **DEELS** | Eén gerichte WebSearch uitgevoerd (moderne identificatie van de Drongiri-grot als "Mahavatar Babaji Cave, Kukuchina, Dunagiri"); geen bredere discovery-ronde naar bijv. Zuid-Indiase Babaji-tradities of andere lineage-vertakkingen (buiten AOAY-scope, mogelijk bestaand maar niet onderzocht). |
| **RECONCILIATIE-GATE** | **N.V.T. in deze taak** | Fase 7 vereist externe/detector-only claims om te reconciliëren; die bestaan nog niet voor deze blinde pre-external freeze (conform CCI_TASK 087's expliciete instructie: geen externe input vóór deze freeze, inclusief de aparte externe ChatGPT-parallelsweep). |

**`BABAJI_V2_PRE_EXTERNAL_SATURATED: NEE`**

Onderbouwing: twee bronfamilies (aanvullende YSS/SRF-lineage-publicaties, bredere niet-AOAY
Babaji-tradities) blijven onderzocht noch uitgesloten — een eerlijk benoemd hiaat. Daarnaast blijven
drie occurrences (#2, #12, #13) op regio-/symbolisch niveau zonder exacte fysieke identiteit, wat
inherent is aan Babaji's ahistorische status maar niettemin een expliciete beperking is, geen
verzwegen gok.

## Vergelijking met de oude METHOD_V1-lijst (PHASE2_RESULT.md, ATL-MB-001 t/m 005) — pas nú geraadpleegd

Niet als discovery-checklist gebruikt tijdens de blinde pas hierboven; alleen nu ter vergelijking.
De oude lijst bevatte 5 punten voor Babaji (Fase 2, METHOD_V1). Deze verse METHOD_V2-pas identificeert
14 afzonderlijke occurrence-clusters — een aanzienlijke verdieping, met name de nieuwe/explicietere
vondsten van record #4 (Allahabad-oeverplek exact aangewezen aan Wright), #6 (Serampore-banyanboom),
#7 (Benares-parlour), #8 (Barackpur) en vooral **#9 (Yogananda's eigen persoonlijke ontmoeting op
4 Gurpar Road)** — dit laatste record ontbrak in de oude lijst en is binnen AOAY de sterkste rechtstreeks door de
auteur vertelde Babaji-claim. Het is geen onafhankelijk historisch bewijs voor Babaji's bestaan of
fysieke aanwezigheid.

## Onopgeloste punten — expliciete lijst

1. Aanvullende YSS/SRF-lineage-publicaties (Daya Mata's *Only Love* e.a.) niet geraadpleegd.
2. Bredere Babaji-tradities buiten de Kriya-lijn (bijv. andere sadhu-overleveringen) niet onderzocht
   — buiten scope van deze AOAY-gecentreerde taak.
3. Records #2, #12, #13 blijven op regio-/symbolisch niveau, geen exacte fysieke site vast te stellen
   binnen AOAY zelf.
4. Kebalananda's eigen tijd "in de Himalaya" met Babaji (hfst. 33) heeft geen exacte locatie.

Geen A/B/C namens Mark. Geen permanente locatie-ID. Geen PDF. Geen route.

---
Geschreven door: CCI. Geen externe Babaji-resultaten geraadpleegd, gesimuleerd of vergeleken —
conform CCI_TASK 087's stopvoorwaarde en de parallelle externe-blindheidsvereiste uit
`handoffs/INDIA6_TO_INDIA7_LIVE_DELTA_2026-08-18_2359.md`.
