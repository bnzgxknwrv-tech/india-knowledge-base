# SWEEP_PROTOCOL_V1 — VOORSTEL (nog niet actief)

Status: **VOORSTEL**, geschreven door CCI op verzoek van INDIA6 (bericht 031, PR #23,
2026-08-06). Wordt pas canoniek/bindend na expliciete acceptatie door INDIA6 (of Mark) — zie
sectie "Activatie" onderaan. Overschrijft geen bestaande canon stilzwijgend: totdat geaccepteerd
blijven `INDIA5_REGION_START_PROTOCOL.md`, `NOT_TO_BE_MISSED_FRAMEWORK.md` en
`INDIA5-PROTOCOL.md` (inclusief de bestaande "Verzadigingsdrempel"-sectie) ongewijzigd van kracht.

Dit voorstel VERVANGT die documenten niet — het voegt harde, controleerbare poorten toe op de
plekken in de bestaande negen-stappenflow (`INDIA5_REGION_START_PROTOCOL.md`) waar Bodh Gaya
aantoonbaar faalde. Waar mogelijk hergebruikt dit voorstel bestaande, al goed ontworpen regels
(met name de Verzadigingsdrempel-sectie in `INDIA5-PROTOCOL.md`, regels 319-339) in plaats van ze
te herschrijven.

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

## Deel 2 — Nieuw sweep-protocol (poorten A-P)

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

Vast, verplicht controlelijstje — elke regel-start doorloopt dit EERST, vóór de eerste detector
wordt geschreven:

| Lens | Verplicht overwogen? |
|---|---|
| AOAY/Kriya/Yogananda/Sri Yukteswar/Giri-lijn | ☐ |
| Boeddha-biografie: geboorte/verlichting/vóór-verlichting/NA-verlichting (leermomenten)/overlijden | ☐ |
| Levende praktijk: kloosters, tempels, ashrams, meditatiecentra, retraiteplekken | ☐ |
| Alle relevante internationale tradities/kloosters (niet vooraf beperkt tot een sublijst) | ☐ |
| Directe stad/regio-omgeving (niet alleen het hoofdcomplex) | ☐ |
| Andere religieuze tradities: hindoeïsme, jaïnisme, soefisme/islam, sikhisme, christendom | ☐ |
| Historische/archeologische plekken en fysiek unieke heilige objecten | ☐ |
| Spirituele extremen buiten Marks bekende voorkeuren | ☐ |
| Officiële/institutionele bronnen geraadpleegd | ☐ |
| Lokale/insider-bronnen geraadpleegd indien beschikbaar | ☐ |
| Geografische zones (0-20 km kernstraal, 20-30 km signalering, >30 km alleen uitzonderlijk) | ☐ |

Regel: een lens mag pas als "gedekt" gelden met status `SATURATED` of
`EXPLICIET_ONBESCHIKBAAR` — nooit stilzwijgend overgeslagen. Dit lijstje wordt het skelet van de
Coverage Matrix (poort C).

### B. Discovery (bevestiging van bestaande regel, geen wijziging)

Ongewijzigd t.o.v. `NOT_TO_BE_MISSED_FRAMEWORK.md`: geen kandidaatquotum, geen filtering op
verwachte A/B/C, elke MARK_WAARDIGE fysieke plek wordt getoond. Toegevoegd: een detector die nog
nieuwe leads oplevert kan per definitie nooit `SATURATED` zijn (zelfde regel als de bestaande
Verzadigingsdrempel, hier expliciet herbevestigd omdat fout #2 dit negeerde).

### C. Coverage Matrix (nieuw, machine-leesbaar bestand per run)

Eén JSONL-bestand per run: `runs/active/<RUN_ID>/PRE_BRONS/COVERAGE_MATRIX.jsonl`. Eén regel per
lens uit poort A, plus elke detector die eruit ontstaat:

```json
{"lens_of_detector_id": "...", "status": "NOT_STARTED|ACTIVE|SATURATED|EXPLICIET_ONBESCHIKBAAR", "reden": "...", "laatst_bijgewerkt": "YYYY-MM-DD"}
```

Harde regel: een sweep mag pas naar stap 4 (Kandidaatstatus) van de negen-stappenflow zolang GEEN
regel `NOT_STARTED` of `ACTIVE` heeft. Dit is de directe fix voor fout #2 en #3.

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
| **Generiek-check**: is het onderscheid UITSLUITEND "vertegenwoordigt land/traditie X"? Zo ja → `EXCLUDED_HARD_REASON`, geen nummer | ja (nieuw, fixt fout #4) |
| Geen bevestigd duplicaat/sublocatie van een bestaande kandidaat (zie poort F) | ja |
| Redelijkerwijs A, B of C mogelijk na eerlijke uitleg | ja |

Landendekking/categorievolledigheid is nooit op zichzelf voldoende — dit stond al in
`NOT_TO_BE_MISSED_FRAMEWORK.md`, hier herbevestigd met een verplichte, expliciete checkstap i.p.v.
een achteraf-principe.

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

### M. Content-QA vóór PDF (bevestiging/formalisering van de reeds bestaande PDF-poort)

Ongewijzigd t.o.v. de al ingevoerde regel in `INDIA5-PROTOCOL.md`: CCI levert tekst/data, INDIA
controleert de volledige inhoud, correcties gaan eerst in brondata/rapport. Aangescherpt (INDIA6
bericht 032/tweede versie): dit levert een apart, expliciet, letterlijk token op —
`CONTENT_QA_ACCEPTED: JA` — LOS van `PDF_GO: JA`. Zonder dit token blijft de sweep in
`AWAITING_CONTENT_QA`; pas daarna kan een apart, eveneens letterlijk `PDF_GO: JA` een PDF-build
openen. Deze twee tokens zijn nooit hetzelfde besluit: content-goedkeuring zegt niets over
toestemming om daadwerkelijk te bouwen (fixt fout #9, scherper dan de eerdere versie van dit
voorstel).

### N. PDF (ongewijzigd)

Eén definitieve keuze-PDF per sweep-fase, uitsluitend ná content-QA. De PDF is een presentatie van
al goedgekeurde inhoud, nooit zelf een onderzoeksstap of correctiekanaal.

### O. Vervangbaarheid/handoff (nieuw format, zie ook Deel 2 van dit voorstel-pakket:
`india5/ACTIVE_STATE.md`)

Elke actieve run houdt een `STATUS.md` (of vergelijkbaar) bij met minimaal: huidige fase (van de
negen stappen), laatste permanente nummers, harde Mark-besluiten, open blockers, protocolversie
(dit document + eventuele opvolgers), toegestane volgende stap, en relevante foutlessen
(verwijzing naar Deel 3, het foutklassenregister). Een nieuwe regisseursessie moet dit ene
bestand kunnen lezen en zonder chatgeschiedenis verder kunnen.

### P. Zelflerende foutklassen (nieuw register)

Zie `india4/protocols/FOUTKLASSEN_REGISTER.md` (nieuw, apart bestand — zie Deel 3 hieronder). Bij
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

Deze regel is geen aparte controlestap maar een werkinstructie voor hoe alle poorten A-P worden
uitgevoerd — vandaar geen eigen JSONL-bestand of token.

---

## Deel 3 — Foutklassenregister (nieuw, apart bestand aangemaakt)

Zie `india4/protocols/FOUTKLASSEN_REGISTER.md`. Bevat de tien fouten uit Deel 1 als herbruikbare,
genummerde klassen (FK-001 t/m FK-010), zodat een toekomstige, nieuwe fout eerst tegen dit
register gelegd kan worden ("is dit een bekende klasse, of nieuw?") in plaats van dat elke fout
een losse, steeds langere ad-hoc regel wordt.

---

## Wat dit voorstel NIET doet

- Geen nieuwe regionale sweep gestart.
- Geen PDF gebouwd.
- Geen A/B/C ingevuld namens Mark.
- Geen route/pacing/accommodatie.
- Geen bestaande canon (INDIA5-PROTOCOL.md, INDIA5_REGION_START_PROTOCOL.md,
  NOT_TO_BE_MISSED_FRAMEWORK.md) stilzwijgend overschreven of automatisch actief verklaard.

## Openstaande ontwerpbeslissingen voor INDIA6

1. **Twee protocol-lineages ontdekt**: naast `india4/protocols/INDIA5-PROTOCOL.md` (het document
   dat feitelijk deze hele sessie is gebruikt) bestaat een parallelle, eerder opgezette
   architectuur onder `india5/` (`GOVERNANCE.md`, `TASK_PROTOCOL.md`, `india5/tasks/` met
   `TASK.yaml`/`STATUS.yaml`, `india5/schemas/`). Die tweede architectuur lijkt na de eerste
   Varanasi-coverage-taken (`INDIA5-VNS-DISCOVERY-COVERAGE-003`, nog altijd "active" staande
   `INDIA5-VNS-DISCOVERY-SATURATION-004`) niet meer gebruikt te zijn voor Bodh Gaya — de run
   gebruikte in plaats daarvan de PR-comment-envelop + `runs/active/`-structuur. INDIA6 moet
   beslissen: (a) de `india5/tasks/`-architectuur alsnog gebruiken/reactiveren, (b) haar bewust
   als gearchiveerd/legacy markeren, of (c) de nieuwe Coverage Matrix/Lead Register (Deel 2, C/D)
   daarin integreren i.p.v. als losse bestanden onder `runs/active/`. Dit voorstel kiest voorlopig
   optie (c)-light: nieuwe bestanden onder `runs/active/<RUN_ID>/PRE_BRONS/`, niet onder
   `india5/tasks/`, puur omdat dat de locatie is die deze hele sessie daadwerkelijk werd gebruikt
   — maar dit is expliciet een keuze die INDIA6 kan overrulen.
2. **Machine-validatie vs. handmatige discipline**: dit voorstel beschrijft de Coverage
   Matrix/Lead Register/evidence-matrix als bestandsformaten en checklists, niet als afgedwongen
   door een script. INDIA6 kan beslissen of een v2 een Python-validator verdient (zoals
   `validate_global_numbering.py` al bestaat voor nummering) die deze bestanden automatisch
   controleert vóór een `SATURATED=JA`-claim wordt geaccepteerd.
3. **Reikwijdte van de adversarial pass (poort I)**: dit voorstel laat in het midden hoeveel
   nieuwe zoekrichtingen/brontypen "genoeg anders" zijn om als een geldige adversarial pass te
   tellen. INDIA6 kan hier een concreet minimum aan willen verbinden (vergelijkbaar met de
   bestaande Verzadigingsdrempel: "minimaal twee wezenlijk verschillende benaderingen").

## Activatie

Dit document is **VOORSTEL** totdat INDIA6 (of Mark) expliciet schrijft: `SWEEP_PROTOCOL_V1:
GEACCEPTEERD`. Tot die tijd blijft de bestaande canon (negen-stappenflow, Verzadigingsdrempel,
NOT_TO_BE_MISSED-framework) ongewijzigd van kracht; dit voorstel is uitsluitend leesvoer en nog
niet bindend voor lopende of toekomstige sweeps.

---
Geschreven door: CCI, op verzoek van INDIA6 (PR #23, bericht 031). Geen PDF, geen nieuwe
regionale sweep, geen A/B/C, geen route/pacing. `PDF_STATUS: VERBODEN` gerespecteerd.
