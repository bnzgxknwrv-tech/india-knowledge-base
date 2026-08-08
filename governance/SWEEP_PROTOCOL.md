# SWEEP_PROTOCOL_V1 — ACTIEF/CANONIEK

Status: **ACTIEF/CANONIEK** sinds `SWEEP_PROTOCOL_V1: GEACCEPTEERD` (protocolreview door de
huidige INDIA-regisseur, PR #23). Deze locatie (`governance/`) is de versie-onafhankelijke canon:
niet gebonden aan een specifieke regisseursessie (INDIA4, INDIA5, INDIA6, ... zijn vervangbare
regisseursessies, geen canonieke systeemversies — zie `governance/ACTIVE_STATE.md`).

Dit document VERVANGT `INDIA5_REGION_START_PROTOCOL.md`, `NOT_TO_BE_MISSED_FRAMEWORK.md` en
`INDIA5-PROTOCOL.md` niet — het voegt harde, controleerbare poorten toe op de plekken in de
bestaande negen-stappenflow (`INDIA5_REGION_START_PROTOCOL.md`) waar Bodh Gaya aantoonbaar
faalde. Waar mogelijk hergebruikt dit document bestaande, al goed ontworpen regels (met name de
Verzadigingsdrempel-sectie in `INDIA5-PROTOCOL.md`, regels 319-339) in plaats van ze te
herschrijven. Activatie/acceptatie van vervolgwijzigingen aan dit document gebeurt voortaan via
het rolgebaseerde token `CURRENT_INDIA_REGISSEUR: ACCEPTEERT` (of, historisch, het eerdere
`SWEEP_PROTOCOL_V1: GEACCEPTEERD`) — nooit via een sessienaam-specifieke formulering.

Machine-checkbare preflight: zie `governance/scripts/preflight_validator.py` en de toelichting in
Deel 4 hieronder.

---

## Deel 1 — Root-cause-analyse (Bodh Gaya)

### Foutenlijst met blokkeermoment en ontbrekende controle

| # | Fout | Waarom het protocol dit toeliet | Ideaal blokkeermoment | Ontbrekende controle |
|---|---|---|---|---|
| 1 | Vroege CORE_PASS/OPTIONAL_PASS/WATCHLIST-ronde filterde 9 locaties weg op verwachte A/B/C-kans | Geen expliciet verbod op "verwachte uitkomst" als (impliciete) uitsluitingsgrond; de vijf harde uitsluitingsgronden bestonden wel, maar niets checkte actief of een afwijzing er één van was | Bij elke afwijzing, vóór WATCHLIST-plaatsing | Een verplichte koppeling tussen elke afwijzing en één van de vijf harde gronden (zie Deel 2, E) |
| 2 | `SATURATION_REPORT.md` registreerde zelf `DET-BGY-P003: NOT_YET_SATURATED`, maar de run ging toch door naar nummering/BRONS/GOUD | De Verzadigingsdrempel-regel (INDIA5-PROTOCOL.md 319-339) bestond al, maar niets dwong een check van die regel af vóórdat de volgende stap begon | Vóór stap 4 (Kandidaatstatus) van de negen-stappenflow | Een harde sweep-closure-gate die alle detectorstatussen leest en blokkeert bij een niet-`SATURATED` status (zie Deel 2, C/J) |
| 3 | Hele categorieën (Sikhisme, Vuurpreek/post-verlichting, meerdere internationale kloosters, Gaya-stad-hindoeïsme) bleven onontdekt tot een expliciete, latere heropening | Geen vooraf vastgelegd, verplicht dekkingsplan per lens/categorie — detectoren ontstonden ad hoc tijdens discovery, niet uit een vaste checklist | Vóór Discovery start (PRE-BRONS) | Een verplichte, per-lens dekkingsmatrix met status NOT_STARTED/ACTIVE/SATURATED/EXPLICIET_ONBESCHIKBAAR (zie Deel 2, A/C) |
| 4 | Generieke kandidaten (069 Mongolian Temple, bijna ook 075 Jain Temple) kregen een permanent nummer op basis van "nog een land/traditie" i.p.v. een eigen verhaal | De MARK_WAARDIG-toets bestond, maar werd op het moment van nummeren niet expliciet langs de vraag "is dit alleen categorie-/landendekking?" gelegd | Op het moment van nummeren (stap 5) | Een verplichte, expliciete generiek-check als laatste stap vóór nummering (zie Deel 2, E) |
| 5 | Identiteitsvragen (063 vs. 068, Daijokyo vs. Indosan Nippon, Akshayavat vs. 051, Bakraur vs. Sujata) werden pas laat, na expliciete vraag, opgelost | Geen standaardregel die een identiteitscheck verplicht vóórdat twee gelijkende plekken allebei als losse, actieve kandidaten worden behandeld | Op het moment dat een nieuwe kandidaat qua naam/traditie/locatie op een bestaande lijkt | Een verplichte overlap-check bij nummering, met een blokkerende status bij onzekerheid (zie Deel 2, F) |
| 6 | Keuze-relevante toegankelijkheid (niet-hindoe-toegang bij 051, cursus-only bij 074, sublocatiestatus van 076) werd pas laat, soms pas na een correctieronde, onderzocht | Toegankelijkheid was geen verplicht veld vóór opname in het keuzerapport — het werd behandeld als "later, bij routeplanning" | Vóór een kandidaat in het keuzerapport komt (vóór stap 8 GOUD) | Een verplicht toegankelijkheidsveld per kandidaat, ingevuld vóór GOUD (zie Deel 2, H) |
| 7 | Zware historische claims (Vuurpreek/Gayasisa-identificatie) steunden aanvankelijk op Alamy-fotobijschriften en een fandom-wiki | Bronkwaliteitsregels bestonden (DET-BGY-P007), maar zonder differentiatie naar het GEWICHT van de claim — een lichte en een zware claim hadden dezelfde drempel | Op het moment dat de claim wordt geschreven, niet pas bij controle | Een claimgewicht-afhankelijke bronregel (zie Deel 2, G) |
| 8 | Voorspellende A/B/C-taal ("eerder B/C", "A alleen als...") sloop in "objectieve" kandidaatteksten | Geen expliciet stijl-/inhoudsverbod, alleen een algemene regel dat CCI geen A/B/C invult namens Mark — dat werd gelezen als "geen A/B/C aanvinken", niet als "geen A/B/C-taal gebruiken" | Bij het schrijven van elke kandidaattekst | Een expliciete, letterlijke verbodslijst + een geautomatiseerde grep-check vóór commit (zie Deel 2, L) |
| 9 | PDF werd twee keer gebouwd zonder ondubbelzinnige toestemming (eerst een kleine correctie, later een taak die alleen naar een bestandsnaam verwees) | De regel "vraag eerst" bestond, maar had geen machine-checkbaar token — een verwijzing naar een PDF-bestandsnaam in een opdracht werd verkeerd gelezen als impliciete toestemming | Vóór elke PDF-build-actie | Een verplicht, letterlijk `PDF_GO: JA`-veld, met `PDF_STATUS: VERBODEN` als default (inmiddels al ingevoerd, zie INDIA5-PROTOCOL.md) |
| 10 | INDIA6 moest zes tot acht keer handmatig gaten ontdekken (berichten 021, 024, 026, 028, 030) i.p.v. dat CCI's eigen `SATURATED=JA` betrouwbaar was | CCI's eigen saturatie-verklaring werd niet getoetst aan een controleerbare, itemized evidence-matrix — het was een vrije-tekst-conclusie | Direct na elke `SATURATED=JA`-claim, vóór acceptatie | Een verplichte evidence-matrix bij elke saturatieclaim + een aparte INDIA-acceptatiestap (zie Deel 2, J/K) |

### Top 5 root causes (samengevat voor het rapportageveld)

1. **Geen verplicht pre-sweep dekkingsplan** — categorieën/lenzen werden ad hoc ontdekt in plaats
   van vooraf vastgelegd, waardoor hele tradities (Sikhisme, post-verlichtingsmomenten) pas laat
   opdoken.
2. **Geen harde koppeling tussen detectorstatus en sweep-afsluiting** — een zelf-gerapporteerde
   `NOT_YET_SATURATED` blokkeerde de volgende stap niet automatisch.
3. **Geen generiek-check op het moment van nummeren** — categorie-/landendekking sloop toch door
   als reden voor een permanent nummer, ondanks een bestaande regel die dat verbiedt.
4. **Geen claimgewicht-afhankelijke bronregel** — lichte en zware claims kregen dezelfde
   bronkwaliteitsdrempel, waardoor een historisch kernfeit op een fotobijschrift kon rusten.
5. **CCI's eigen saturatieclaim was niet extern controleerbaar** — een vrije-tekst-conclusie in
   plaats van een itemized, door INDIA6 te auditen evidence-matrix, dwong INDIA6 tot herhaald
   handmatig speurwerk.

---

## Deel 2 — Sweep-protocol (poorten A-S)

Elke poort hieronder is een TOEVOEGING aan een bestaande stap uit
`INDIA5_REGION_START_PROTOCOL.md`. Waar een poort een bestaand mechanisme al dekt, wordt dat
expliciet vermeld in plaats van gedupliceerd.

**Letteringsnoot (na INDIA6 bericht 032/tweede, gedetailleerdere versie van dezelfde
systeemtaak):** INDIA6's eigen versie gebruikt een iets andere letter-indeling (o.a. losse
Coverage-Plan/Lead-Register-samenvoeging onder A, Discovery Feedback Loop als eigen letter D,
Content-QA en PDF-Gate als twee gescheiden letters M/N met elk een eigen token). Inhoudelijk zijn
beide versies gelijk; deze versie behoudt haar eigen A-P-indeling (die al gecommit was) en dekt
alle punten uit INDIA6's versie af — zie de mapping in de PR-reactie. Twee inhoudelijke deltas uit
INDIA6's versie zijn hieronder wél verwerkt: een zesde Lead Register-uitkomst `SUBLOCATION` (D) en
een apart `CONTENT_QA_ACCEPTED: JA`-token vóór `PDF_GO: JA` (M).

### A. Pre-sweep dekkingsplan (nieuw, vóór PRE-BRONS-detectoren worden geschreven)

**Reisdoel-prioriteitscorrectie (INDIA6 bericht 044, 2026-08-08) — GEEN gelijkwaardige lijst.**
De lenzen hieronder vallen in twee, uitdrukkelijk NIET gelijkwaardige lagen:

- **Laag 1 — MISSIEKRITISCH (AOAY + Top-X)**: onderworpen aan een 100%-sweepverplichting, zie
  hieronder. Dit is Marks eigenlijke reisdoel.
- **Laag 2 — BONUSMATERIAAL (alle overige lenzen)**: pas relevant NADAT laag 1 aantoonbaar is
  afgezocht. Mag de zoekinspanning voor laag 1 nooit verdringen. Zie ook poort C/J: laag-2-
  kandidaten mogen een `SATURATED=JA`-claim pas mee ondersteunen als de laag-1-detectoren
  zelf `SATURATED` of `EXPLICIET_ONBESCHIKBAAR` zijn.

**Bestaande regel die hiermee botste (herkend bij deze correctie)**: de dekkingsmatrix hieronder
behandelde voorheen alle elf lenzen als gelijkwaardige checkboxvakjes met dezelfde statusregel —
zonder enige prioriteitsvolgorde tussen bijvoorbeeld de AOAY-lens en "spirituele extremen buiten
Marks bekende voorkeuren". Hersteld door de laag 1/laag 2-scheiding hieronder en de bijbehorende
volgordedwang in poort C/J.

**Laag 1A — AOAY, 100% sweepverplichting.** Zoek systematisch naar ELKE verifieerbare fysieke
plek uit, of rechtstreeks verbonden met, *Autobiography of a Yogi* — ook een klein huis, kamer,
schuur, boom, straat, station, eenvoudige tempel, grot, ashram, verblijfplaats, ontmoetingsplek,
initiatieplek, meditatieplek of gebeurtenislocatie. Objectieve beroemdheid of bezoekersaantal is
hierbij IRRELEVANT — zie ook poort E.1.

**Laag 1B — Top-X, 100% prioriteitssweep.** Voor iedere Top-X-persoon systematisch alle
betekenisvolle fysieke verbindingen zoeken: geboorte, jeugd, verblijf, meditatie, initiatie,
leraar/leerling-ontmoeting, ashram, samadhi, onderricht, lineage-gebeurtenis, relieken,
belangrijke reis/gebeurtenis.

**Definitieve Top-11 (canoncorrectie INDIA6 bericht 046, 2026-08-08 — vervangt elke eerdere,
bredere Top-X-omschrijving)**:

1. Paramahansa Yogananda
2. Mahavatar Babaji
3. Lahiri Mahasaya
4. Sri Yukteswar
5. Ram Dass
6. Neem Karoli Baba
7. Anandamayi Ma
8. Ramakrishna
9. Ramana Maharshi
10. Hariharananda
11. Vivekananda

Apart van deze lijst, met een expliciet gewenste Mahasamadhi-locatie in Delhi: **Shri Mataji
Nirmala Devi** — buiten de Top-11, maar wel met een eigen, met naam benoemde missiekritische
locatiewens.

**Boeddha en Krishna staan NIET in de Top-11** (bericht 046, expliciete correctie op een eerdere,
te brede lezing): beiden zijn zo groot/alomtegenwoordig/religieus breed vertegenwoordigd dat een
lage Top-X-drempel enorme kandidaat-inflatie zou veroorzaken (een gewone boeddhistische of
Krishna-tempel zou anders automatisch een missiekritische link krijgen). Boeddha- en
Krishna-gerelateerde kandidaten vallen daarom voortaan volledig onder **laag 3** (zie hieronder)
— alleen behouden als de fysieke plek ZELF de hoge, zelfstandige-zwaarte-drempel haalt (zoals
Mahabodhi Temple/Bodh Gaya dat overduidelijk doet), NOOIT alleen omdat Boeddha/Krishna er wordt
vereerd.

Voorbeeld van exact gewenste informatie voor een échte Top-11-verbinding: Sri Yukteswar trad in
Bodh Gaya in de swami/sannyas-orde (zie 046). Zo'n verbinding moet door de sweep
worden gevonden, ook wanneer de precieze fysieke sublocatie niet meer vaststelbaar is — scheid
dan expliciet: gebeurtenis = verifieerbaar (JA/NEE), exacte fysieke plek = wel/niet verifieerbaar
(los van elkaar vastgelegd, nooit stilzwijgend samengevoegd tot één "onbevestigd").

| Lens | Laag | Verplicht overwogen? |
|---|---|---|
| AOAY/Kriya/Yogananda/Sri Yukteswar/Giri-lijn (100% sweepverplichting, zie Laag 1A) | 1 (missiekritisch) | ☐ |
| Top-11 (Yogananda, Babaji, Lahiri Mahasaya, Sri Yukteswar, Ram Dass, Neem Karoli Baba, Anandamayi Ma, Ramakrishna, Ramana Maharshi, Hariharananda, Vivekananda) + Shri Mataji Nirmala Devi apart: elk een eigen detector (100% sweepverplichting, zie Laag 1B; Boeddha/Krishna vallen NIET hieronder, zie laag 2/E.1) | 1 (missiekritisch) | ☐ |
| Boeddha-biografie: geboorte/verlichting/vóór-verlichting/NA-verlichting (leermomenten)/overlijden | 2 (bonus) | ☐ |
| Levende praktijk: kloosters, tempels, ashrams, meditatiecentra, retraiteplekken | 2 (bonus) | ☐ |
| Alle relevante internationale tradities/kloosters (niet vooraf beperkt tot een sublijst) | 2 (bonus) | ☐ |
| Directe stad/regio-omgeving (niet alleen het hoofdcomplex) | 2 (bonus) | ☐ |
| Religie-onafhankelijke bedevaarts-/heiligdomzoeking (zie E.1) — directe zoektermen: bedevaart, pelgrimsstromen, heiligdommen, beroemde relieken/beelden/graven/grotten/heilige plaatsen; hindoeïsme/jaïnisme/soefisme-islam/sikhisme/christendom e.a. zijn hier ALLEEN aanvullende zoektermen, nooit de begrenzing | 2 (bonus) | ☐ |
| Historische/archeologische plekken en fysiek unieke heilige objecten | 2 (bonus) | ☐ |
| Spirituele extremen buiten Marks bekende voorkeuren | 2 (bonus) | ☐ |
| Officiële/institutionele bronnen geraadpleegd | 2 (bonus) | ☐ |
| Lokale/insider-bronnen geraadpleegd indien beschikbaar | 2 (bonus) | ☐ |
| Geografische zones (0-20 km kernstraal, 20-30 km signalering, >30 km alleen uitzonderlijk) | 2 (bonus) | ☐ |

Regel: een lens mag pas als "gedekt" gelden met status `SATURATED` of
`EXPLICIET_ONBESCHIKBAAR` — nooit stilzwijgend overgeslagen. Dit lijstje wordt het skelet van de
Coverage Matrix (poort C). De religie-lens hierboven is expliciet GEEN vaste religielijst om af
te vinken (zie E.1) — de zoekvraag is "welke fysieke plekken hebben hier uitzonderlijke
religieuze/spirituele/pelgrimszwaarte?", niet "welke bekende religies zijn hier aanwezig?".

**Voorbeeld van de bedoelde prioriteit (INDIA6 bericht 044)**: een obscure schuur waar Yogananda
aantoonbaar mediteerde staat qua keuzeprioriteit BOVEN een enorm bedevaartsoord met miljoenen
bezoekers — dat is geen inconsistentie, maar precies Marks persoonlijke reisdoel. Dit bepaalt
NIET wat wordt getoond (poort B/E blijven quotumvrij en filteren niet op verwachte A/B/C) — het
bepaalt uitsluitend de verplichte zoekvolgorde/-diepte en de saturatie-afhankelijkheid (poort
C/J).

### B. Discovery (bevestiging van bestaande regel, geen wijziging)

Ongewijzigd t.o.v. `NOT_TO_BE_MISSED_FRAMEWORK.md`: geen kandidaatquotum, geen filtering op
verwachte A/B/C, elke MARK_WAARDIGE fysieke plek wordt getoond. Toegevoegd: een detector die nog
nieuwe leads oplevert kan per definitie nooit `SATURATED` zijn (zelfde regel als de bestaande
Verzadigingsdrempel, hier expliciet herbevestigd omdat fout #2 dit negeerde).

### C. Coverage Matrix (nieuw, machine-leesbaar bestand per run)

Eén JSONL-bestand per run: `runs/active/<RUN_ID>/PRE_BRONS/COVERAGE_MATRIX.jsonl`. Eén regel per
lens uit poort A, plus elke detector die eruit ontstaat:

```json
{"lens_of_detector_id": "...", "status": "NOT_STARTED|ACTIVE|SATURATED|EXPLICIET_ONBESCHIKBAAR", "reden": "...", "laatst_bijgewerkt": "YYYY-MM-DD", "laag": "1_MISSIEKRITISCH|2_BONUS"}
```

Harde regel: een sweep mag pas naar stap 4 (Kandidaatstatus) van de negen-stappenflow zolang GEEN
regel `NOT_STARTED` of `ACTIVE` heeft. Dit is de directe fix voor fout #2 en #3.

**Volgordedwang laag 1 vóór laag 2 (INDIA6 bericht 044, 2026-08-08)**: de AOAY-regel en ELKE
Top-X-persoon-regel (`laag: "1_MISSIEKRITISCH"`) moeten `SATURATED` of `EXPLICIET_ONBESCHIKBAAR`
zijn vóórdat laag-2-regels (algemene bedevaartsplekken/tradities) mogen meetellen als steun voor
een `SATURATED=JA`-claim op sweepniveau (zie poort J). Een sweep mag laag-2-onderzoek best parallel
verrichten, maar de saturatieclaim zelf blijft geblokkeerd zolang een laag-1-regel nog
`NOT_STARTED`/`ACTIVE` is.

### D. Lead Register (nieuw, machine-leesbaar bestand per run)

Eén JSONL-bestand: `runs/active/<RUN_ID>/PRE_BRONS/LEAD_REGISTER.jsonl`. Elke concrete lead
(genoemd door Mark, gevonden tijdens discovery, of door de adversarial pass in poort I) krijgt
één regel met verplichte einduitkomst:

```json
{"lead": "...", "outcome": "MARK_WAARDIG|HARD_EXCLUDED|DUPLICATE|SUBLOCATION|OUT_OF_SCOPE_HIGH_VALUE|EXPLICIET_ONBESCHIKBAAR", "candidate_id_if_any": "...", "reden": "..."}
```

Toegevoegd (bijgewerkt na INDIA6 bericht 032/tweede versie): `SUBLOCATION` als eigen uitkomst,
los van `DUPLICATE` — een lead kan een feitelijk andere, bestaande plek zijn zonder een duplicaat
te zijn (precies het 076 Akshayavat-geval: geen dubbele plek, wel binnen dezelfde
tempelbinnenplaats als 051, dus geen zelfstandige kandidaat maar ook geen "duplicaat").

Harde regel: geen lead mag zonder eindstatus blijven staan bij sweep-afsluiting (fixt fout #10 —
"vergeten open leads" worden zichtbaar in plaats van pas later herontdekt).

### E. MARK_WAARDIG-gate (aanscherping van bestaand mechanisme)

Vóór een permanent nummer wordt toegekend, verplicht "ja" op ALLE onderstaande punten (niet
alleen impliciet aannemen):

| Check | Verplicht |
|---|---|
| Concrete, aanwijsbare fysieke plek (geen diffuus gebied) | ja |
| Eigen verhaal/ervaring, los van de categorie waartoe het behoort | ja |
| **Generiek-check**: is het onderscheid UITSLUITEND "vertegenwoordigt land/traditie X"? Zo ja → `EXCLUDED_HARD_REASON`, geen nummer, TENZIJ E.1 hieronder een AOAY- of Top-X-override geeft | ja (fixt fout #4) |
| Geen bevestigd duplicaat/sublocatie van een bestaande kandidaat (zie poort F) | ja |
| Redelijkerwijs A, B of C mogelijk na eerlijke uitleg | ja |

Landendekking/categorievolledigheid is nooit op zichzelf voldoende — dit stond al in
`NOT_TO_BE_MISSED_FRAMEWORK.md`, hier herbevestigd met een verplichte, expliciete checkstap i.p.v.
een achteraf-principe.

#### E.1 Prioriteitslagen / beslisvolgorde (canoncorrectie, INDIA6 berichten 036 + 044, 2026-08-08)

De generiek-check hierboven is niet absoluut — er zijn drie lagen, elk met een eigen drempel.
**Dit is uitdrukkelijk GEEN gelijkwaardige drielaagse lijst (bericht 044-verscherping)**: laag 1
en 2 (AOAY, Top-X) zijn Marks eigenlijke, missiekritische reisdoel; laag 3 is bonusmateriaal, pas
relevant nadat laag 1/2 aantoonbaar zijn afgezocht (zie poort A/C/J voor de bijbehorende
sweepverplichting en volgordedwang). Voor iedere lead, in deze volgorde:

1. **AOAY = ABSOLUTE OVERRIDE, MISSIEKRITISCH.** Een verifieerbare fysieke plek die expliciet
   voorkomt in *Autobiography of a Yogi*, rechtstreeks gekoppeld is aan een daarin beschreven
   gebeurtenis, of aantoonbaar de fysieke plek is waar zo'n gebeurtenis plaatsvond → MOET getoond
   worden, ook als de plek objectief klein, lokaal, architectonisch onbelangrijk, geen grote
   bedevaartsplaats of verder niet onderscheidend is. AOAY overrulet de generiek-/zwaartefilter
   volledig. Enige eis: fysieke identiteit verifieerbaar (welke plek dat werkelijk is).
2. **TOP X = MAXIMALE PERSOONLIJKE ZWAARTE, MISSIEKRITISCH.** Zonder AOAY-link: breed zoeken naar
   betekenisvolle fysieke plekken rond geboorte, jeugd, verblijf, meditatie, initiatie,
   leraar/leerling-ontmoeting, ashram, samadhi, onderricht, lineage-gebeurtenis, relieken,
   belangrijke reis/gebeurtenis van de **definitieve Top-11** (zie poort A: Yogananda, Babaji,
   Lahiri Mahasaya, Sri Yukteswar, Ram Dass, Neem Karoli Baba, Anandamayi Ma, Ramakrishna, Ramana
   Maharshi, Hariharananda, Vivekananda — plus Shri Mataji Nirmala Devi apart, met haar eigen
   Mahasamadhi-locatiewens). **Boeddha en Krishna staan NIET in deze lijst** (bericht 046) — hun
   kandidaten vallen onder laag 3. Lage drempel voor tonen binnen de Top-11 — niet beperken tot
   beroemde of drukbezochte plekken. **Gebeurtenis vs. exacte plek, apart vastleggen
   (bericht 044)**: als een betekenisvolle verbinding wél verifieerbaar is maar de precieze
   fysieke sublocatie niet meer vaststelbaar is (bijvoorbeeld: Sri Yukteswar trad in Bodh Gaya in
   de sannyas-orde, exacte plek binnen Bodh Gaya onbekend — zie 046), wordt dit ALTIJD getoond met
   twee losse velden: `gebeurtenis_geverifieerd: JA/NEE` en `exacte_locatie_geverifieerd:
   JA/NEE/ONBEKEND` — nooit stilzwijgend samengevoegd tot één "onbevestigd" dat de gebeurtenis
   zelf verdoezelt.
3. **ALLES BUITEN AOAY/TOP X = RELIGIE-ONAFHANKELIJKE BEDEVAARTSZOEKING, HOGE DREMPEL** (verscherpt,
   INDIA6 bericht 040/tweede versie, 2026-08-08 — vervangt de eerdere, voor misverstand vatbare
   formulering "religieuze zwaargewichten"). De zoekvraag is NIET "welke belangrijke religies zijn
   hier aanwezig?" maar UITSLUITEND: **"welke fysieke plekken in deze sweepregio hebben
   uitzonderlijke religieuze/spirituele/pelgrimszwaarte?"** Concreet:
   - Een grote wereldreligie geeft op zichzelf GEEN recht op opname.
   - Een zeer kleine, obscure of lokaal onbekende religie/traditie MOET wél ontdekt worden zodra
     zij hier een extreem belangrijke bedevaartsplek heeft — een obscure traditie met één plaats
     waar enorme aantallen mensen naartoe pelgrimeren moet juist boven komen.
   - Religiecategorieën (hindoeïsme, jaïnisme, islam, sikhisme, christendom, ...) zijn hoogstens
     aanvullende zoektermen, nooit de begrenzing van de zoekruimte.
   - Discovery moet daarom ook rechtstreeks zoeken op bedevaart, heiligdommen, pelgrimsstromen,
     beroemde relieken/beelden/graven/grotten/heilige plaatsen en vergelijkbare zwaartesignalen,
     zonder vooraf bekende religielijst als filter.
   - Sterke signalen (illustratief, geen religielijst): zeer grote jaarlijkse pelgrimsstromen,
     nationaal/internationaal beroemde bedevaartsstatus, een uitzonderlijk vereerd
     beeld/relict/graf/grot/heiligdom, een belangrijke heilige persoon, een zeer oude levende
     traditie, uitzonderlijke religieuze/historische zwaarte, of een plek waarheen ook mensen
     buiten de eigen traditie bewust reizen.
   - **Boeddha- en Krishna-kandidaten vallen hier expliciet onder** (bericht 046): een kleine
     boeddhistische tempel of gewone Krishna-tempel wordt NIET opgenomen alleen omdat Boeddha/
     Krishna er wordt vereerd; een plek als Mahabodhi Temple/Bodh Gaya blijft vanzelfsprekend
     kandidaat omdat de fysieke plek zelf uitzonderlijke internationale bedevaarts-/spirituele
     zwaarte heeft; een uitzonderlijk groot Krishna-bedevaartsoord blijft eveneens kandidaat als
     de plek zelf de hoge drempel haalt.
   - Een gewone tempel/heiligdom van eender welke traditie, puur aanwezig voor categoriedekking,
     is NIET MARK_WAARDIG; een heiligdom van eender welke traditie (groot of obscuur) mét
     aantoonbaar zware, zelfstandige bedevaartsbetekenis WEL.

**Geen "religies afvinken"**: religieuze/traditie-coverage (poort A, de lenzenlijst) is
uitsluitend aanvullende zoekterminologie om mogelijke zwaargewichten niet te missen — nooit
zelfstandig bewijs voor kandidaatstatus, en nooit een begrenzing van waar discovery mag zoeken.
Coverage mag discovery openen; kandidaatstatus vereist altijd óf een AOAY/Top-X-override, óf
aantoonbare zelfstandige, religie-onafhankelijke bedevaarts-/pelgrimszwaarte onder laag 3.

Praktisch: iedere lead doorloopt A→B→C. A: AOAY-link? Ja → tonen (mits fysieke identiteit
verifieerbaar). Nee → B: Top-X-link? Ja → brede toets, lage drempel. Nee → C: algemene
religieuze/spirituele plek? Alleen tonen als aantoonbaar zwaargewicht/bedevaartsplek/
uitzonderlijke fysieke of historische betekenis, zoals hierboven omschreven.

### F. Identiteit/duplicaten (nieuw, verplichte stap vóór nummering)

Bij elke nieuwe kandidaat: een korte overlap-scan tegen bestaande kandidaten met dezelfde
traditie, vergelijkbare naam, of dezelfde/aangrenzende locatie. Uitkomst verplicht één van:
`CONFIRMED_DIFFERENT` (met bronverwijzing), `CONFIRMED_DUPLICATE` (geen tweede nummer),
`UNRESOLVED_BLOCKER` (nummering wacht tot opgelost). Nooit stilzwijgend allebei nummeren zonder
check — dit is precies wat bij 063/068 wél goed ging (apart gecheckt) maar bij het eerste
Akshayavat-nummer (076) niet vooraf gebeurde.

### G. Claimkwaliteit naar claimgewicht (nieuw)

| Claimtype (voorbeelden) | Minimale bronstandaard |
|---|---|
| Exacte historische gebeurtenislocatie | Primaire tekst of erkend academisch naslagwerk; een toeristische foto-caption of wiki zonder bronvermelding is NOOIT voldoende als enige bron |
| "Eerste/enige/grootste" | Minimaal twee onafhankelijke bronnen, of expliciet als onbevestigd/mogelijk overdreven gemarkeerd |
| Toegang voor buitenlander/niet-aanhanger | Specifiek voor DIE plek geverifieerd — nooit afgeleid van een vergelijkbare, andere plek (zie 073-les: niet van Puri afleiden) |
| Evenementdatum | Meest recente bevestigde editie vermelden; toekomstige datum nooit zelf schatten — `ONBEKEND` indien niet gepubliceerd |
| Verblijf/deelnamemogelijkheid zonder volledig programma | Expliciet navragen/verifiëren wat een niet-deelnemer kan doen — nooit aannemen dat het hetzelfde is als een vergelijkbare kandidaat |
| Lineage-/persoonsconnectie (bv. Sri Yukteswar, Guru-bezoeken) | Bron benoemen als primair/institutioneel vs. gemeenschapshistoriografie vs. reisblog — expliciet het niveau vermelden, nooit gelijkstellen |

Regel: "onzeker" wordt altijd expliciet als onzeker geschreven — nooit stilzwijgend opgevuld met
de meest waarschijnlijke aanname.

### H. Toegankelijkheid vóór keuzerapport (nieuw, verplicht veld)

Elke kandidaat krijgt, vóór opname in het keuzerapport, een ingevuld veld: "wat kan Mark als
gewone buitenlandse bezoeker daadwerkelijk zien/doen?" — inclusief expliciete vermelding als dit
niet geverifieerd is. Dit mag nooit voor het eerst tijdens routeplanning aan het licht komen als
het de A/B/C-keuze had kunnen beïnvloeden (fixt fout #6).

### I. Adversarial missed-place pass (nieuw, verplichte stap na reguliere discovery)

Ná de reguliere discovery-ronde, vóór de sweep als gesloten wordt beschouwd, één verplichte,
apart gelogde ronde met de vraag: "Welke MARK_WAARDIGE plek zou Mark later terecht boos maken dat
we hem nooit hebben laten zien?" — met ANDERE zoekrichtingen/brontypen dan de eerste pass
(bijvoorbeeld: officiële lijsten/tourism-overzichten cross-checken tegen wat al genummerd is,
zoals in de Bodh Gaya-sweep uiteindelijk wél gebeurde met de internationale-kloosterlijst). Elke
nieuwe vondst heropent automatisch de bijbehorende detector/lens in de Coverage Matrix (status
terug naar `ACTIVE`).

### J. Saturation-gate (aanscherping, met controleerbare evidence-matrix)

`SATURATED=JA` mag CCI alleen claimen met een bijgevoegde, ingevulde evidence-matrix:

```text
[ ] Coverage Matrix: alle regels SATURATED of EXPLICIET_ONBESCHIKBAAR (geen NOT_STARTED/ACTIVE)
[ ] Laag 1 (AOAY + elke Top-X-persoon) apart bevestigd SATURATED/EXPLICIET_ONBESCHIKBAAR vóórdat
    laag-2-bevindingen (algemene bedevaartsplekken) meetellen als saturatiebewijs (INDIA6 bericht 044)
[ ] Lead Register: geen regel zonder eindstatus
[ ] Ontbrekende-categoriecheck: uitgevoerd, resultaat vermeld (ook als "niets nieuws")
[ ] Identiteit/duplicaatvragen die kandidaten beinvloeden: opgelost of expliciet UNRESOLVED_BLOCKER
[ ] Keuze-relevante toegangsblockers: geen open exemplaren
[ ] Adversarial pass (poort I): uitgevoerd, resultaat vermeld
```

Geen vrije-tekst-conclusie zonder deze matrix. Dit is de directe fix voor fout #10.

### K. Onafhankelijke INDIA-controle (bevestiging van reeds gegroeide praktijk, nu geformaliseerd)

Na een CCI-`SATURATED=JA` met evidence-matrix: INDIA (huidige regisseur) controleert de matrix
zelf, niet alleen de conclusie. Pas na een expliciet `INDIA_ACCEPTED_SATURATION: JA` (analoog aan
`PDF_GO: JA`) opent de keuzerapportfase. Zonder dat token blijft de sweep in
`AWAITING_INDIA_REVIEW`.

### L. Keuzerapport — verbod op voorspelde A/B/C (nieuw, met concrete verboden lijst)

Verboden formuleringen (letterlijk, niet uitputtend): "eerder B/C", "A alleen als...", "B goed
voorstelbaar", "waarschijnlijk C/B/A", "A minder waarschijnlijk", "A niet uitgesloten", "degelijke
C-optie". Toegestaan: feiten + een feitelijke "reden om eventueel over te slaan" zonder
lettercode-voorspelling. Aanbevolen praktische check vóór commit: een eenvoudige grep op deze
zinsneden over het GOUD-bestand (geen aparte validator-script verplicht in v1, wel aanbevolen voor
v2 — zie Deel 3).

#### L.1 GEO-combinatiesymmetrie (canoncorrectie, INDIA6 bericht 051, 2026-08-08)

"Goed te combineren met" betekent UITSLUITEND: de locaties liggen geografisch/praktisch zo dicht
bij elkaar dat ze in hetzelfde bezoek, wandeling, korte rit of dagdeel te combineren zijn. Het is
NOOIT: inhoudelijke verwantschap, zelfde religie/thema, "zou leuk samen zijn", of
routeplannings-voorkeur — thematische verwantschap mag nooit als GEO-combinatie gepresenteerd
worden.

**Verplichte symmetrie**: als kandidaat A vermeldt dat hij goed te combineren is met B, dan MOET
B's eigen tekst ook A vermelden. Vormen A, B en C samen één logisch cluster, dan noemt elk van de
drie de andere twee — nooit een eenrichtingsrelatie of een gedeeltelijk genoemd cluster. Altijd
`nummer + naam`, nooit een kaal nummer.

**Bij onvoldoende betrouwbare locatiegegevens**: niet raden. Schrijf letterlijk
`combineerbaarheid niet betrouwbaar vast te stellen na GEO-controle — [reden]` in plaats van een
aangenomen combinatie of een stille leegte.

**Permanente PDF-gate-uitbreiding**: een keuze-PDF faalt de gate (poort M/N) als: combineer-
relaties asymmetrisch zijn; een kandidaat slechts een deel van een aantoonbaar cluster noemt;
thematische verwantschap als GEO-combinatie gepresenteerd wordt; of combineerbaarheid nog niet
onderzocht is (dat laatste moet expliciet gemeld worden, niet stilzwijgend blijven staan als
"nog niet onderzocht").

### M. Content-QA vóór PDF — verplichte PRE_PDF_CONTENT-stap (aangescherpt, INDIA6 bericht 055, 2026-08-08)

**Vervangt/specificeert het eerdere `CONTENT_QA_ACCEPTED`-token** — hetzelfde principe (CCI levert
tekst/data, INDIA controleert de volledige inhoud, correcties gaan eerst in brondata/rapport),
maar nu met een verplichte, concrete tussenstap zodat INDIA altijd het EINDPRODUCT als geheel
controleert, niet alleen losse bronrapporten:

1. CCI rondt research/data af.
2. CCI bouwt de VOLLEDIGE beoogde PDF-inhoud als één human-readable Markdown-bestand
   (`PRE_PDF_CONTENT.md` in `GOUD/USER/` van de run), exact in de uiteindelijke volgorde en met
   dezelfde koppen/tabellen/kandidaatteksten die later in de PDF verschijnen.
3. CCI committeert dit bestand. **Nog GEEN PDF-build.**
4. INDIA leest het volledige `PRE_PDF_CONTENT.md` als eindproduct.
5. Correcties gaan terug naar CCI en worden in hetzelfde bestand verwerkt (niet in een los kanaal).
6. INDIA voert een laatste integrale controle uit op het gecorrigeerde bestand.
7. Alleen bij expliciet, letterlijk `PRE_PDF_CONTENT_APPROVED: JA` ÉN een apart, letterlijk
   `PDF_GO: JA` mag CCI renderen. Dit vervangt het oude losse `CONTENT_QA_ACCEPTED: JA`-token voor
   PDF-doeleinden — gebruik voortaan uitsluitend `PRE_PDF_CONTENT_APPROVED: JA` als het
   content-goedkeuringstoken vóór een PDF-build, om verwarring tussen een oud en nieuw token te
   voorkomen.
8. De uiteindelijke PDF mag inhoudelijk niet afwijken van het goedgekeurde `PRE_PDF_CONTENT.md`,
   behalve automatische paginering/typografie. De renderer herschrijft nooit zelfstandig inhoud.
9. Na build: CCI controleert uitsluitend visueel op lay-out (zoals al gangbare praktijk); inhoud
   wordt niet opnieuw autonoom herschreven.

Een PDF die INDIA niet integraal als volledige eindtekst heeft gelezen en goedgekeurd, mag nooit
aan Mark als keuze-PDF gepresenteerd worden.

### N. PDF — vorm/leesbaarheid en verplichte kandidaatblok-inhoud (aangescherpt, INDIA6 berichten 055/056/057, 2026-08-08)

Eén definitieve keuze-PDF per sweep-fase, uitsluitend ná de PRE_PDF_CONTENT-stap (poort M). De PDF
is een presentatie van al goedgekeurde inhoud, nooit zelf een onderzoeksstap of correctiekanaal.

**Voorkeursvolgorde van het document:**
1. Regio + Marks persoonlijke missie daar in het kort + AOAY-treffers + Top-11-treffers + overige
   zwaargewichten als bonus.
2. Compacte beslismatrix: nr + naam | Jouw link | GEO/cluster | bezoektijd | toegang | kernreden |
   A/B/C-vak (of, na een keuzeronde, de vastgelegde A/B/C).
3. Eenvoudige geografische clusterkaart, uitsluitend indien voldoende betrouwbare GEO-data
   beschikbaar is; onzekere GEO apart gemarkeerd, niet geraden.
4. Compacte kandidaatkaarten, bij voorkeur niet over een pagina-einde gesplitst.
5. Laatste pagina: compact A/B/C-invuloverzicht (of, na een keuzeronde, een overzicht van de
   vastgelegde besluiten).

**Verplichte velden per kandidaatkaart (minimaal):**
1. `JOUW LINK` — AOAY (exacte passage/gebeurtenis) OF Top-11 (naam + exacte link) OF
   `GEEN AOAY/TOP-11-LINK — zelfstandig pelgrims-/spiritueel zwaargewicht`. Nooit generiek "Kriya-/
   boeddhistische focus" schrijven — Boeddha is geen Top-11-naam.
2. `OBJECTIEVE SPIRITUELE/PELGRIMS-ZWAARTE` — zie poort L.2 hieronder.
3. `MAGNETISME TER PLEKKE` — zie poort L.2.
4. `WAAROM DIT VOOR MARK KAN TELLEN` — vertaling naar zijn reisdoel, zonder A/B/C te voorspellen.
5. `WAT ER CONCREET TE ERVAREN IS`.
6. `PRAKTISCH/GEO` — combineerbaarheid uitsluitend volgens poort L.1.
7. `BEZOEKTIJD` — realistische bandbreedte; een transparante INDIA/CCI-planningsschatting is
   toegestaan zonder officiële bron, mits expliciet zo gelabeld ("inschatting op basis van
   omvang/type bezoek") — geen schijnprecisie. Dit is geen routeplanning/ervaringstijd voor het
   hele cluster.
8. `REISPERIODE-RELEVANTIE` — Marks daadwerkelijke reisperiode is **18 december 2026 t/m 21
   januari 2027** (vastgelegd in `governance/ACTIVE_STATE.md`). Keuze-relevante festivals/
   evenementen/toegang worden hiertegen gecontroleerd, niet tegen een oud/generiek festivaljaar:
   `evenement tijdens reisperiode: JA/NEE/ONBEKEND NA ONDERZOEK`.
9. `AFWEGING` — het echte beslispunt, geen verborgen A/B/C-advies.
10. `ECHTE ONZEKERHEID` — alleen onzekerheid die overblijft NA onderzoek, met een concrete
    categorie: `RELEVANTIE-TWIJFEL`, `BRON-TWIJFEL`, `TOEGANG-TWIJFEL`, `DATUM-TWIJFEL`,
    `GEO-TWIJFEL`, of een andere concrete categorie (meerdere toegestaan). Nooit een kaal
    "TWIJFELGEVAL" zonder aard van de twijfel.

**Verboden placeholders voor keuze-relevante velden**: `NOG NIET ONDERZOCHT`, `TODO`, `TBD` of
gelijkwaardig. Als iets na echt gericht onderzoek onbekend blijft: `ONBEKEND NA ONDERZOEK` + korte
reden. Dit geldt minimaal voor: persoonlijke betekenis/link, spirituele/pelgrims-zwaarte, concrete
ervaring, bezoekbaarheid/toegang, GEO-identiteit, combineerbaarheid, bezoektijd voor zover redelijk
afleidbaar, keuze-relevante datum-/festivalinformatie.

**Na een Mark-keuze**: oude AI-classificaties (`CORE_PASS`, `OPTIONAL_PASS`, "niet kernwaardig",
e.d.) worden niet meer zichtbaar getoond in de gebruikers-PDF zodra Mark A/B/C heeft gekozen — dan
gewoon `MARK: A/B/C`. Oude AI-classificaties zijn niet gebruikersrelevant na Marks besluit.

Kale nummers zijn verboden — altijd `nummer + naam`. Vermijd meta-/protocoltekst in de
gebruikers-PDF en onnodige herhaling tussen "waarom", "betekenis", "ervaring" en "afweging".

#### L.2 Zwaarte voor Mark — verplicht blok (INDIA6 bericht 056, 2026-08-08)

Elke kandidaat krijgt, naast `JOUW LINK` (zie poort N), een `ZWAARTE VOOR MARK`-blok:

- **Objectieve pelgrims-/heiligdomzwaarte**: een klasse, geen kunstmatig puntensysteem:
  `WERELD-/PAN-INDIA HEAVYWEIGHT`, `NATIONAAL/ZEER ZWAAR`, `REGIONAAL ZWAAR`, `LOKAAL/BEPERKT`, of
  `GEEN ECHTE PELGRIMSMAGNEET — vooral historisch/institutioneel/architectonisch/studiecentrum`.
  Onderbouw concreet met wat beschikbaar is: aantoonbare bezoekers-/pelgrimsstroom (alleen cijfers
  bij betrouwbare bron), status binnen een canonieke groep (bv. één van een beperkt aantal
  Shakti Peethas), uniek reliek/lichaamsdeel/voetafdruk/graf/grot/boom/gebeurtenis, centrale
  rituele functie, nationale/internationale faam binnen de traditie, ouderdom/continuïteit van
  levende bedevaart, omvang van jaarlijkse festivals, levende devotie versus alleen historisch
  belang.
- **Magnetisme ter plekke**: feitelijk, observeerbaar (voortdurend veel pelgrims/offers/puja/zang;
  vooral druk tijdens één festival, daarbuiten rustig; actief klooster zonder pelgrimsmagneet;
  monument/museum met weinig levende praktijk; `ONBEKEND` indien niet betrouwbaar onderzocht) —
  geen zweverige "energie"-claims.
- **Relatieve context** (optioneel, alleen indien onderbouwd): één korte, feitelijke vergelijking
  met een andere kandidaat uit dezelfde regio — nooit een ranking om de ranking.
- **Voor Mark in één zin**: concrete persoonlijke vertaling, geen verborgen A/B/C-advies.

Regel: populariteit alleen is GEEN spirituele zwaarte; "vertegenwoordigt religie X" is NOOIT een
zwaarteargument (zie ook FK-011/E.1). Een kleine AOAY/Top-11-plek blijft voor Mark belangrijker dan
een objectief enorme bedevaartsplek zonder AOAY/Top-11-link.

#### L.3 Feitelijke claimdiscipline in gebruikerstekst (INDIA6 bericht 057, 2026-08-08)

Vóór elke PRE_PDF_CONTENT-vrijgave controleert CCI nogmaals alle keuze-relevante absolute claims:
"exacte plek", "eerste", "oudste", "grootste", "enige", directe causaliteitsclaims, en een
gebeurtenis-op-exact-deze-fysieke-plek-claim. Bij twijfel: genuanceerd formuleren, nooit
stilzwijgend een stad/regio-gebeurtenis versmallen tot een specifiek tempelcomplex, en
toegangsbeleid nooit afleiden uit de afwezigheid van een gemeld verbod (bestaande regel, poort G,
hier herbevestigd). Bekende Bodh Gaya-precedenten: Sri Yukteswars sannyas-gebeurtenis in Bodh Gaya
≠ bewezen exacte locatie Mahabodhi Temple Complex (zie poort E.1, gebeurtenis vs. exacte plek);
Sujata Stupa niet zonder sterk bewijs als "exacte plek van aanbieding" presenteren; Great Buddha
Statue niet onnodig absoluut als "grootste van India" formuleren; Mahabodhi Society niet absoluut
"oudste bestaande kloostergebouw" zonder sterke onderbouwing.

### O. Vervangbaarheid/handoff (nieuw format, zie ook Deel 2 van dit voorstel-pakket:
`governance/ACTIVE_STATE.md`)

Elke actieve run houdt een `STATUS.md` (of vergelijkbaar) bij met minimaal: huidige fase (van de
negen stappen), laatste permanente nummers, harde Mark-besluiten, open blockers, protocolversie
(dit document + eventuele opvolgers), toegestane volgende stap, en relevante foutlessen
(verwijzing naar Deel 3, het foutklassenregister). Een nieuwe regisseursessie moet dit ene
bestand kunnen lezen en zonder chatgeschiedenis verder kunnen.

### P. Zelflerende foutklassen (nieuw register)

Zie `governance/SWEEP_ERROR_CLASSES.md` (nieuw, apart bestand — zie Deel 3 hieronder). Bij
elke nieuwe, generaliseerbare fout: classificeren, een preventieve poort toevoegen aan dit
document (niet een losse ad-hoc regel ernaast), en één keer centraal documenteren.

### Q. Token-/efficiencyregel (nieuw, toegevoegd na INDIA6 bericht 032/tweede versie)

Dit protocol moet first-time-right verbeteren zonder een bureaucratisch monster te worden.

| Gebruik wél | Vermijd |
|---|---|
| Matrices/JSONL-regels i.p.v. lange vrije tekst | Herhaalde brede repo-scans wanneer gerichte bestanden volstaan |
| Korte, vaste statusvelden (bv. `SATURATED`/`ACTIVE`) | PDF-herbouw zonder nieuw `PDF_GO: JA` |
| Validatorscripts waar mogelijk (zie ook Deel 3, ontwerpvraag 2) | Heronderzoek van al gesloten/bevestigde feiten |
| Vaste stopcriteria (Verzadigingsdrempel, evidence-matrix) | Lange narratieve statusrapporten waar een tabel volstaat |
| Gerichte bronqueries per openstaande lens/lead | Volledige nieuwe sweep om één deelvraag te beantwoorden |

Deze regel is geen aparte controlestap maar een werkinstructie voor hoe alle poorten A-R worden
uitgevoerd — vandaar geen eigen JSONL-bestand of token.

### R. Dubbele onafhankelijke sweep + reconciliatie (nieuw, INDIA6 bericht 059, 2026-08-08 —
foutprecedent: Bodh Gaya)

**Waarom deze poort bestaat**: de Bodh Gaya-run toonde aan dat één CCI-sweep niet betrouwbaar
genoeg is voor Marks missiekritische laag (AOAY + Top-11). Pas nadat INDIA6 onafhankelijk dezelfde
regio onderzocht (bericht 058, "ONAFHANKELIJKE CROSS-CHECK"), kwamen meerdere gemiste/foutieve
links boven water: Ram Dass bij 061 versus 074 (datum + gebouw), Anandamayi Ma bij 051, Vivekananda
bij 046 (verdieping), een echte Ramakrishna-fout bij 046 (ingetrokken, correcte link verplaatst
naar 051), en Neem Karoli Baba's devotee-context bij 046 (correct geclassificeerd als geen directe
fysieke link). Dit lost tevens openstaande ontwerpvraag 3 (hieronder, "reikwijdte van de
adversarial pass") op door een harde ondergrens te zetten: één interne CCI-pass (poort I) is NOOIT
voldoende voor de missiekritische laag — er moet een echt onafhankelijke tweede sweep zijn.

**Twee onafhankelijke sweeps, verplicht vóór een regio als inhoudelijk compleet geldt**:
- **Sweep A = CCI primaire sweep**: normale discovery volgens dit protocol (AOAY volledig, elk
  Top-11-lid individueel, daarna laag-3 zwaargewichten), stopt alleen op geldige
  saturatieregels (poort J).
  - **Sweep B = onafhankelijke INDIA-tegensweep**: uitgevoerd door de actuele INDIA-regisseur,
  of — als Mark dat expliciet kiest — door een aparte, onafhankelijke onderzoekschat. Krijgt
  dezelfde regio en dezelfde Mark-kernprioriteiten, maar NIET vooraf CCI's kandidatenlijst of
  conclusies. Doel is zelfstandig ontdekken, niet kandidaat-voor-kandidaat CCI verifiëren:
  andere queryformuleringen, bronfamilies, biografische ingangen, historische spellingen.
  Rapporteert ook negatieve resultaten per AOAY/Top-11-persoon. Mag NIET vervangen worden door
  INDIA die achteraf alleen CCI's lijst naleest — dat veroorzaakt anchoring.

**Wat dubbel moet, wat niet**: verplicht dubbel — volledige AOAY-regioverbindingen, elk Top-11-lid
apart, fysieke gebeurtenissen/locaties (ook obscure huizen/kamers/tempeltjes/grotten/stations/
bomen/ashrams), gebeurtenis en exacte fysieke locatie apart geverifieerd; laag-3-zwaargewichten
(religie-onafhankelijk, geen religies afvinken, focus op zelfstandige zwaarte/magnetisme). NIET
verplicht dubbel tot detailniveau: GEO-coördinaten, openingstijden, PDF-layout, bronformattering,
technische validators — die blijven CCI-uitvoer/QA.

**Blinde volgorde (anchoring-preventie)**: (1) CCI rondt Sweep A af en bevriest de uitkomst; (2)
INDIA voert Sweep B uit zonder eerst Sweep A's kandidaten/conclusies als zoekbasis te gebruiken;
(3) pas daarna worden A en B naast elkaar gelegd; (4) elk verschil krijgt één van: `CCI_MISSED`,
`INDIA_MISSED`, `SAME_FINDING`, `SOURCE_CONFLICT`, `DIFFERENT_PHYSICAL_IDENTIFICATION`,
`NOT_RELEVANT_AFTER_RECONCILIATION`; (5) alleen de gereconcilieerde uitkomst mag door naar
keuzerapport-gereedheid.

**Reconciliatiegate (verplicht vóór keuzerapport/PDF)**:

```text
DOUBLE_SWEEP_COMPLETED: JA
INDEPENDENT_SWEEP_PERFORMED: JA
RECONCILIATION_COMPLETED: JA
MISSION_CRITICAL_DIFFERENCES_RESOLVED: JA
```

Een regio geldt NIET als inhoudelijk sweep-compleet/keuzerijp zolang een missiekritisch verschil
openstaat. Geen consensus-door-meerderheid, geen automatisch-CCI-gelijk-geven: bij verschil worden
bronnen opnieuw getoetst; als het verschil niet betrouwbaar oplosbaar is, gaat het zichtbaar naar
Mark (als `MARK_DECISION_CONFLICT` of vergelijkbaar).

**Rol van Mark**: Mark hoeft geen twee rapporten te lezen — INDIA en CCI lossen de verschillen
onderling op (via GitHub/PR, zie poort S, `HUMAN_TOUCHPOINTS_MINIMIZED`) en Mark krijgt pas
daarna één geconsolideerde, menselijke keuzebasis. Alleen echte onoplosbare inhoudelijke
conflicten of persoonlijke classificatiekeuzes gaan naar Mark.

**Efficiency**: dubbel DENKEN/ZOEKEN, niet dubbel PRODUCEREN — Sweep B focust op onafhankelijke
discovery/inhoud, geen tweede datasetsuite/PDF/KML; één compact onafhankelijk sweep-rapport
volstaat; reconciliatie in één bestand vastgelegd; alleen nieuwe/differente leads worden daarna
door CCI volledig technisch uitgewerkt (zie ook poort Q).

**Bodh Gaya blijft het geldige precedent** voor waarom deze poort bestaat, óók na de huidige
reconciliatieronde (bericht 058) — deze poort geldt voortaan voor toekomstige regio's, niet
retroactief als blokkade voor het al lopende Bodh Gaya-werk.

### S. HUMAN_TOUCHPOINTS_MINIMIZED — GitHub als communicatiebrug (nieuw, INDIA6 bericht 060,
2026-08-08)

**Principe**: Mark is geen menselijke message-bus tussen INDIA en CCI. GitHub/PR is de
gezamenlijke communicatie- en state-laag tussen INDIA en CCI; Mark komt alleen in beeld voor
beslissingen die uitsluitend hij kan nemen.

**Belangrijke grens (geen fictieve automatisering)**: INDIA kan technisch niet autonoom/achter-
grond blijven draaien of door CCI worden aangeroepen. Deze poort claimt dus GEEN automatische
INDIA-activering. Wat wél geldt: zodra Mark (of een geplande/getriggerde sessie) terugkeert in de
INDIA-chat, of zodra CCI een nieuwe PR-comment van INDIA leest, moet de betreffende kant
zelfstandig GitHub uitlezen — zien wat de andere kant inmiddels heeft gedaan/gecommit/gerapporteerd
— en de eerstvolgende eigen controle/actie uitvoeren zonder Mark opnieuw als koerier te gebruiken.

**Gewenste normale flow** (per sweep): (1) Mark geeft één opdracht: sweep regio X. (2) CCI voert
Sweep A uit en schrijft resultaten/state in GitHub. (3) INDIA leest die resultaten rechtstreeks uit
GitHub en voert onafhankelijk Sweep B uit (poort R). (4) INDIA zet verschillen/gaten rechtstreeks
op GitHub. (5) CCI onderzoekt/reconcileert die verschillen en commit de uitkomst. (6) INDIA leest
de volledige gereconcilieerde PRE_PDF_CONTENT rechtstreeks uit GitHub en reviewt integraal. (7)
Correcties tussen INDIA↔CCI lopen rechtstreeks via GitHub, zonder dat Mark teksten hoeft te
kopiëren. (8) Pas als beide inhoudelijk akkoord zijn, krijgt Mark één goede keuze-PDF. (9) Mark
geeft alleen A/B/C en eventuele persoonlijke inhoudelijke correcties. (10) CCI legt besluiten vast;
vervolgcluster/pacing kan daarna volgens canon.

**Mark hoeft normaal NIET**: CCI-uitvoer naar INDIA te kopiëren als die al op GitHub staat;
INDIA-instructies naar CCI te kopiëren als INDIA ze rechtstreeks op de PR kan plaatsen;
tussenreviews te lezen; technische commits/statusvelden te beoordelen; meerdere concept-PDF's te
beoordelen.

**Mark moet wel**: de initiële reis-/sweepvraag geven; persoonlijke voorkeuren/nieuwe
canonbesluiten geven; de uiteindelijke A/B/C-keuzes maken; alleen bij echte inhoudelijke ambiguïteit
die niet door bronnen/protocol oplosbaar is (bijv. een niet-oplosbare `MARK_DECISION_CONFLICT`)
beslissen.

**Geen aparte bureaucratische subarchitectuur**: dit vereenvoudigt de bestaande flow, het voegt er
geen nieuwe laag aan toe — poort K (Onafhankelijke INDIA-controle) en poort O
(Vervangbaarheid/handoff) blijven ongewijzigd van kracht, deze poort maakt alleen expliciet dat
GitHub/PR het kanaal is en dat Mark niet de verplichte tussenpersoon is.

---

## Deel 3 — Foutklassenregister (apart bestand)

Zie `governance/SWEEP_ERROR_CLASSES.md`. Bevat de tien fouten uit Deel 1 als herbruikbare,
genummerde klassen (FK-001 t/m FK-010), plus later toegevoegde klassen uit canoncorrecties
(FK-011 t/m FK-012 en verder), zodat een toekomstige, nieuwe fout eerst tegen dit register gelegd
kan worden ("is dit een bekende klasse, of nieuw?") in plaats van dat elke fout een losse, steeds
langere ad-hoc regel wordt.

---

## Deel 4 — Machine-checkbare preflight

`governance/scripts/preflight_validator.py` controleert, voor een gegeven run-directory, de
structurele (niet-inhoudelijke) voorwaarden vóór fase-overgangen:

- **Vóór keuzerapportfase**: Coverage Matrix bevat geen `NOT_STARTED`/`ACTIVE`-regel; Lead
  Register: elke lead heeft een geldige eindstatus; geen open `UNRESOLVED_BLOCKER` in de
  identiteit/duplicatencheck; geen open keuze-relevante toegankelijkheidsblocker; permanente
  nummering uniek/valide (hergebruikt `validate_global_numbering.py`); actieve kandidaten hebben
  geen status `HARD_EXCLUDED`/`SUBLOCATION`/`DUPLICATE`; saturation-evidence-bestand aanwezig;
  `INDIA_ACCEPTED_SATURATION: JA` aanwezig.
- **Vóór PDF**: `PRE_PDF_CONTENT_APPROVED: JA` aanwezig (vervangt `CONTENT_QA_ACCEPTED: JA` voor
  PDF-doeleinden, zie poort M); `PDF_GO: JA` aanwezig.
- **Vóór keuzerapport-gereedheid van een missiekritische regio (poort R, nieuw 2026-08-08, nog NIET
  in `preflight_validator.py` geïmplementeerd — hier expliciet als open punt genoteerd, niet
  verhuld)**: `DOUBLE_SWEEP_COMPLETED: JA`, `INDEPENDENT_SWEEP_PERFORMED: JA`,
  `RECONCILIATION_COMPLETED: JA`, `MISSION_CRITICAL_DIFFERENCES_RESOLVED: JA`. Vooralsnog
  handmatig door INDIA/CCI gecontroleerd,
  zoals ook `INDIA_ACCEPTED_SATURATION` aanvankelijk handmatig was vóórdat het een script-check
  werd — een validator-uitbreiding is mogelijke v2-toekomstige stap (zie Openstaande
  ontwerpbeslissingen, punt 2).

**Grens van de validator (expliciet, niet verhuld)**: de validator controleert uitsluitend
structurele/machinaal-checkbare voorwaarden (bestaat het veld, is de status geldig, is er geen
lege/tegenstrijdige waarde). Hij kan NIET beoordelen of een saturatieclaim inhoudelijk klopt, of
een bron sterk genoeg is voor een claim, of een generiek-check correct is uitgevoerd — dat blijft
mensen-/CCI-/INDIA-oordeel. De validator doet dus nooit alsof hij inhoudelijke kwaliteit
garandeert; hij garandeert alleen dat de vereiste structuur/velden aanwezig en intern consistent
zijn vóór een fase-overgang wordt toegestaan.

---

## Wat dit protocol NIET doet

- Geen nieuwe regionale sweep gestart.
- Geen PDF gebouwd.
- Geen A/B/C ingevuld namens Mark.
- Geen route/pacing/accommodatie.
- Geen bestaande canon (INDIA5-PROTOCOL.md, INDIA5_REGION_START_PROTOCOL.md,
  NOT_TO_BE_MISSED_FRAMEWORK.md) stilzwijgend overschreven — dit document VOEGT TOE, het vervangt
  niet.

## Openstaande ontwerpbeslissingen (rolgebaseerd — voor de huidige INDIA-regisseur)

1. **Twee protocol-lineages**: naast `india4/protocols/INDIA5-PROTOCOL.md` (het document dat
   feitelijk deze hele sessie is gebruikt) bestaat een parallelle, eerder opgezette architectuur
   onder `india5/` (`GOVERNANCE.md`, `TASK_PROTOCOL.md`, `india5/tasks/` met
   `TASK.yaml`/`STATUS.yaml`, `india5/schemas/`). Die tweede architectuur lijkt na de eerste
   Varanasi-coverage-taken (`INDIA5-VNS-DISCOVERY-COVERAGE-003`, nog altijd "active" staande
   `INDIA5-VNS-DISCOVERY-SATURATION-004`) niet meer gebruikt te zijn voor Bodh Gaya — de run
   gebruikte in plaats daarvan de PR-comment-envelop + `runs/active/`-structuur. Nog niet
   opgelost: reactiveren, bewust archiveren, of samenvoegen met Coverage Matrix/Lead Register.
   Dit document kiest voorlopig: nieuwe bestanden onder `runs/active/<RUN_ID>/PRE_BRONS/`, niet
   onder `india5/tasks/` — overrulebaar door de huidige regisseur.
2. **Machine-validatie**: gedeeltelijk opgelost door `governance/scripts/preflight_validator.py`
   (Deel 4) — dekt de structurele checks. Nog open: of ook Coverage Matrix/Lead Register-inhoud
   zelf (niet alleen status-volledigheid) verder geautomatiseerd moet worden.
3. **Reikwijdte van de adversarial pass (poort I)**: GEDEELTELIJK OPGELOST (2026-08-08, poort R) —
   voor de missiekritische laag (AOAY + Top-11) is nu een harde ondergrens gezet: één interne CCI-
   pass is nooit voldoende, er is een echt onafhankelijke tweede sweep (Sweep B, door INDIA of een
   aparte onderzoekschat) plus reconciliatiegate verplicht. Nog open: of dezelfde harde eis ook
   voor de bonusmateriaal-laag (laag 3, overige zwaargewichten) geldt, of dat daar de bestaande,
   lichtere adversarial-pass-taal (poort I, "minimaal twee wezenlijk verschillende benaderingen")
   blijft volstaan — nog niet formeel bevestigd.

## Activatie

Status: **ACTIEF/CANONIEK**, geaccepteerd via protocolreview (PR #23) door de huidige
INDIA-regisseur. Toekomstige, verdere wijzigingen aan dit document worden pas bindend na een
expliciet `CURRENT_INDIA_REGISSEUR: ACCEPTEERT`-token (rolgebaseerd, niet aan een sessienaam
gebonden) in een PR-reactie. De bestaande canon (negen-stappenflow, Verzadigingsdrempel,
NOT_TO_BE_MISSED-framework) blijft daarnaast onverkort van kracht; dit document is een aanvulling,
geen vervanging.

---
Geschreven door: CCI, geactiveerd na protocolreview door de huidige INDIA-regisseur (PR #23).
Geen PDF, geen nieuwe regionale sweep, geen A/B/C, geen route/pacing. `PDF_STATUS: VERBODEN`
gerespecteerd tijdens het schrijven van dit document.
