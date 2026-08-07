# INDIA5-PROTOCOL (definitief, akkoord CC + ChatGPT, 2026-08-02)

Status: CONFIRMED — voorgesteld door CC (Home Assistant-sessie), akkoord door ChatGPT met één
verwerkt tegenpunt (autonome regio-doorloop, zie hieronder). Dit is het geldende protocol voor
elke sweep vanaf nu. Lees dit document eerst volledig voordat je verder werkt aan een sweep.

## Doel

Niet één regio (Varanasi) handmatig oplossen, maar een architectuur waarmee uiteindelijk
duizenden locaties verwerkt kunnen worden met zo min mogelijk handmatige tussenkomst van Mark.

## Waarom het oude INDIA4-protocol faalde

`india4/roles/BRONS.md` schreef letterlijk "Stop daarna" voor na elke kandidaat — dat forceerde
één chatronde per kandidaat, wat bij honderden/duizenden kandidaten onhoudbaar is. Root-cause
volledig gedocumenteerd in `runs/active/VARANASI-GEO-DELIVERY-REPAIR-001/ROOT_CAUSE.md`.

## Autonome regio-doorloop (ChatGPT's tegenpunt, verwerkt — dit is de kern van het protocol)

Mark start een regiosweep met ÉÉN opdracht. Daarna mag hij GEEN batchplanner of doorgeefluik
worden. De uitvoerende sessie doorloopt zelfstandig, zonder tussentijdse Mark-actie:

```
Mark start één regiosweep
        ↓
BRONS verwerkt automatisch alle batches van 15-25 (achter elkaar, zelfde sessie/keten)
        ↓
ZILVER valideert automatisch alle batches
        ↓
GOUD maakt één regionaal eindpakket
        ↓
Mark ontvangt PDF + KML + beslisoverzicht
```

Ontwerpdoel is dus NIET "precies 3 commits" — voor een regio met meerdere batches zijn meer dan
drie interne commits normaal en logisch. Het echte doel:
- **één gebruikershandeling bij de start**;
- **nul tussentijdse handelingen bij normale voortgang** — geen paden, statussen of
  onderzoeksinhoud die Mark moet overnemen of doorgeven tussen BRONS/ZILVER/GOUD;
- **één complete eindoplevering**;
- **alleen terug naar Mark bij een echte inhoudelijke beslissing of een niet-herstelbare
  blocker** (bijv. een structureel gat in de bronnen dat een beleidskeuze vereist).

## Rolverdeling

- **CONTROLLER**: bepaalt scope, kiest eindproducten, en orkestreert vervolgens de VOLLEDIGE
  regio-doorloop zelf (roept intern BRONS → ZILVER → GOUD aan, batch na batch) — verdwijnt niet
  na één batch, blijft de keten besturen tot de regio af is of een echte blocker optreedt. Leest
  bij elke (her)start uitsluitend `runs.jsonl` (append-only journaal) om te bepalen waar verder
  te gaan.
- **BRONS**: verwerkt batches van 15-25 kandidaten, ná elkaar, zonder op een nieuwe
  Mark-opdracht te wachten (niet "alle kandidaten in RAM" — dat bestaat niet voor een chat-agent,
  elke kandidaat kost context ongeacht wanneer je commit, vandaar de kleine vaste batchgrootte).
  Puur onderzoek → JSON. Eén lokaal checkpoint elke ~5 kandidaten (géén git-commit, puur
  crashbescherming). Eén git-commit per afgeronde batch.
- **ZILVER**: start automatisch zodra BRONS een batch heeft afgerond, leest alleen de JSON van
  die batch, valideert bronnen/Google Maps/consistentie. Her-zoekt UITSLUITEND als een
  kandidaat's status ≠ `CONFIRMED` (harde regel, geen open "tenzij nodig"-oordeel). Eén commit
  per batch.
- **GOUD**: start automatisch zodra de VOLLEDIGE regio door ZILVER is gevalideerd (niet na elke
  kleine batch), bouwt het regionale eindpakket (PDF/KML/kaart/print/A-B-C-overzicht). Eén
  afsluitende commit.

## Kernregels (vervangen het oorspronkelijke INDIA5-voorstel op deze punten)

1. **Batchgrootte klein en vast** (15-25 kandidaten per BRONS-run), nooit "alles ineens."
2. **Volgende kandidaat = diff van doellijst tegen output**, via de bestaande
   `runs/active/VARANASI-GEO-DELIVERY-REPAIR-001/scripts/next_candidate.py`-logica. NOOIT
   "laatste ID + 1" — dat breekt bij een overgeslagen of opnieuw-gedane kandidaat.
3. **Elke kandidaat krijgt een status-veld vanaf record 1**: `CONFIRMED` / `NEEDS_REVIEW` /
   `GEEN_BRON` / `AMBIGUE_PIN`. Geen eenduidige Google Maps-pin (0 of >1 kandidaten zonder
   onderscheidend signaal) = altijd `AMBIGUE_PIN`, nooit gokken/substitueren (zie
   `runs/active/VARANASI-GEO-DELIVERY-REPAIR-001/scripts/validate_brons.py` voor het bestaande
   verbod op nep-coördinaten).
4. **`runs.jsonl`** = de enige overblijvende "state": één regel per afgeronde batch (regio,
   batch-ID, kandidaat-range, commit-SHA, timestamp), uitsluitend door CONTROLLER geschreven.
   Geen los `progress.yaml`.
5. **GitHub bevat alleen input/output**, geen state/locks/controller-logica — die logica leeft in
   de uitvoerende agent-sessie zelf, niet in de repo.
6. **Google Maps = bron van waarheid** voor coördinaten (niet website → coördinaten → Maps).
7. **Losse dedup-stap** bij ZILVER of GOUD vóór het eindpakket (naam-gelijkenis + geo-nabijheid),
   belangrijk bij religieuze locaties met meerdere filialen/naamvarianten.

## Definitieve testdoelstelling

Eén startopdracht voor twintig Varanasi-kandidaten, waarna BRONS → ZILVER → GOUD zonder
tussenkomst van Mark doorloopt en eindigt met: één PDF, één KML, één gevalideerde dataset en één
korte eindmelding aan Mark. Geen tussentijdse handelingen van Mark tijdens de doorloop.

## Immutable Location Numbering (Mark-besluit 2026-08-02, commit 58be47b)

Elke kandidaat/fysieke locatie in ALLE India-regio's (niet alleen Varanasi) heeft een vast,
permanent nummer:
- het nummer staat altijd vóór de naam, bijvoorbeeld `007 Shri Kashi Vishwanath Temple`;
- eenmaal toegekend wijzigt het nummer NOOIT, wordt het NOOIT hergebruikt voor een andere locatie,
  en blijft het permanent aan diezelfde fysieke locatie gekoppeld;
- nieuwe locaties krijgen uitsluitend een nieuw vrij nummer, nooit een bestaand nummer;
- nummering loopt voorlopig door tot 999; een toekomstige nummerreeks per regio/cluster mag
  uitsluitend vooraf worden gereserveerd en mag bestaande nummers nooit veranderen.

Bron van waarheid: `runs/active/<run_id>/NUMBERING_REGISTRY.jsonl` (append-only, per regio). Elke
BRONS/ZILVER/GOUD-stap die een candidate_id aanmaakt, registreert het nummer hier vóór het elders
gebruikt wordt. `scripts/validate_numbering.py` (per run, naar analogie van `validate_brons.py`)
blokkeert wanneer:
- een bestaand nummer bij een andere locatie terechtkomt;
- een locatie een ander nummer krijgt dan voorheen;
- een nummer dubbel wordt gebruikt;
- een gegenereerde KML- of PDF-naam niet met het nummer begint.

Draai deze validator verplicht als onderdeel van elke GOUD-validatieronde, naast `validate_brons.py`.

## GOUD-PDF-format (verplicht vanaf 2026-08-02)

De GOUD-keuze-PDF is een REISGIDS voor Mark, geen GEO-validatierapport. Volledig
gespecificeerd in `india4/templates/GOUD_PDF_TEMPLATE.md` — verplichte leesstof voor elke
GOUD-rol. Kern:
- Per kandidaat eerst: waarom bezoeken, spirituele/historische betekenis, wat je ziet/ervaart, hoe
  bijzonder het is, verwachte bezoektijd, goed te combineren met (op werkelijke geografische
  nabijheid), praktische tips, reden om eventueel over te slaan, en een voorlopige keuzehulp
  (advies, geen formele A/B/C-wijziging). GEO-status/coördinaat/Mark-keuze komen pas daarna, in een
  klein technisch blok.
- Kandidaten worden gegroepeerd per geografisch bezoekcluster (wijk/ghat-route), niet op
  candidate_id-volgorde. Een keuze-index vooraan bevat candidate_id, naam, cluster, Mark-keuze,
  keuzehulp in één zin en het paginanummer.
- Ontbrekende keuze-informatie wordt expliciet als "NOG NIET ONDERZOCHT" vermeld — nooit ingevuld
  met een aanname.
- **Gevolg voor BRONS**: BRONS verzamelt vanaf de eerste kandidaat van elke nieuwe sweep ook de
  reisgidsvelden (korte omschrijving, betekenis, wat te zien, uniekheid, bezoektijd, praktische
  info indien bronnen dat toelaten) — niet alleen GEO-verificatievelden. Zie
  `india4/templates/GOUD_PDF_TEMPLATE.md` voor de exacte veldenlijst. Dit voorkomt dat GOUD
  achteraf reisgidsinhoud moet reconstrueren, zoals bij de Varanasi-regio nodig was.
- De oude GEO-rapport-stijl PDF blijft geldig als GOUD ook een technische bijlage oplevert
  (GEO_AUDIT.md/CORRECTIERAPPORT.md/BESLISOVERZICHT.md), maar is niet langer het hoofddocument dat
  aan Mark wordt overhandigd.

### PDF is eenmalig — NIET automatisch herbouwen (Mark-besluit 2026-08-02)

De reisgids-PDF is een eenmalig leesdocument voor Mark, geen doorlopend bijgewerkt kanaal. Mark
leest 'm één keer en gooit 'm daarna weg — het is geen opslagformaat. Daarom:

- Elke wijziging in dataset/RUN.yaml/register (nieuwe Mark-keuze, hotelbesluit, nummering, enz.)
  wordt bijgewerkt in de brondata (JSONL/RUN.yaml/register) en in de KML. De PDF wordt
  **NIET automatisch herbouwd** bij elke ronde — dat kost onnodig tokens voor een document dat na
  lezen toch wordt weggegooid.
- Een nieuwe PDF-build gebeurt alleen als Mark dat expliciet vraagt (bv. "bouw de PDF opnieuw",
  "ik wil een nieuwe leesversie").
  Data-updates zonder die expliciete vraag blijven beperkt tot dataset/RUN.yaml/register/KML/MD.
- De brondata (dataset/RUN.yaml/register) is te allen tijde de bron van waarheid, ook als de PDF
  achterloopt of niet meer bestaat.

**HARDE HERBEVESTIGING (Mark-besluit 2026-08-05, na een schending van deze regel)**: CCI heeft
deze regel zelf overtreden door na een kleine tekstcorrectie (één foutieve zin) zonder te vragen
een volledige nieuwe PDF te bouwen en te versturen. Vanaf nu geldt zonder uitzondering: CCI mag
NOOIT uit eigen beweging een PDF bouwen of herbouwen, ook niet voor een correctie, ook niet als
de fout klein lijkt. Altijd eerst expliciet vragen ("wil je dat ik de PDF opnieuw bouw met deze
correctie, of volstaat de correctie in de brondata?") en pas bouwen na Marks eigen "ja". Een
tekstfout in een reeds geleverde PDF wordt gemeld en in de brondata gecorrigeerd; de PDF zelf
wordt pas herbouwd na expliciete toestemming.

**TWEEDE HERBEVESTIGING — expliciete PDF-poort (INDIA6-besluit, bericht 022, 2026-08-06, na een
tweede schending)**: ondanks de regel hierboven werd een PDF opnieuw gebouwd op basis van een
opdracht die zelf niet het expliciete woord "PDF_GO: JA" bevatte (alleen "herbouw daarna: [pdf]"
in een correctietaak) — dat bleek onvoldoende expliciet en kostte onnodige tokens. Vanaf nu geldt
een vaste, ondubbelzinnige poort, voor alle regio's:

1. **Discovery/onderzoek** — alleen onderzoek + brondata, geen PDF.
2. **Correctie** — alleen inhoud/data corrigeren, geen PDF.
3. **INDIA6-eindcontrole** — India6 controleert de volledige keuze-inhoud (alle kandidaten,
   hoofdclaims, absolute claims, toegankelijkheid, seizoenen, gebeurtenissen, onzekerheden).
4. Bij fouten: CCI corrigeert uitsluitend inhoud/data, daarna opnieuw controle door India6.
5. Een PDF-build mag UITSLUITEND plaatsvinden in een aparte opdracht die letterlijk het veld
   `PDF_GO: JA` bevat. Zonder dat exacte veld is een PDF-build VERBODEN — ook als de opdracht wel
   naar een PDF-bestandsnaam verwijst, ook als een sweep of correctieronde "klaar" is. "Sweep
   klaar" betekent dus NIET automatisch "PDF bouwen".

Elke nieuwe CCI-opdracht bevat vanaf nu expliciet een van de twee velden `PDF_STATUS: VERBODEN`
of `PDF_GO: JA`. Ontbreekt dat veld, dan geldt VERBODEN als impliciete default — CCI mag het
ontbreken van dit veld nooit als toestemming lezen.

## Accommodatiebesluiten (Mark-besluit 2026-08-02, commit cf2daf2)

Hotels, guesthouses, bases en andere verblijfskeuzes zijn GEEN kandidaten (geen A/B/C-locatie-ID uit
de Immutable Location Numbering) en moeten toch altijd expliciet en duurzaam worden gelogd — nooit
alleen in de chat. Bron/aanleiding: `runs/active/<RUN_ID>/GOUD/REGIONAL/HOTEL_DECISION.md` (Varanasi:
`ACCOMMODATION_REGISTER.jsonl`, accommodatie-ID `VNS-HOTEL-001`).

Elke regio krijgt een eigen `ACCOMMODATION_REGISTER.jsonl` naast het kandidaat-dataset. Elk record
heeft minimaal: `accommodation_id` (aparte reeks, bv. `<REGIOCODE>-HOTEL-NNN`), region, run_id,
accommodation_name, city/area, status (`SUGGESTED` | `SHORTLISTED` | `LOCKED_BY_MARK` |
`REJECTED_BY_MARK`), source_type, source_person_or_source_id, letterlijke gebruikerswoorden of
compacte besluitmotivatie, kamerwens, genoemde contactpersoon, boekingsnotities, datum, en
supersedes/superseded_by.

Harde regels, geldig voor elke toekomstige sweep:

1. Vóór nieuw hotelonderzoek altijd eerst bestaande accommodatiebesluiten lezen (register + eerdere
   HOTEL_DECISION-bestanden in de run).
2. `LOCKED_BY_MARK` is canoniek en mag nooit stilzwijgend worden vervangen of opnieuw vergeleken —
   alleen een nieuw, expliciet besluit van Mark mag dat wijzigen.
3. Persoonlijke aanbevelingen van bekenden (naam van de bron, kamerwens, genoemde contactpersoon,
   letterlijke kernnotitie) worden woordelijk bewaard, niet samengevat of weggelaten.
4. GOUD neemt het gekozen verblijf standaard op in de reisgids-PDF (eigen hoofdstuk "Gekozen
   verblijf", direct na de keuze-index), de KML (aparte folder, GEEN A/B/C-ID) en de route-
   /planninginput (lijst logisch bereikbare A-kandidaten = "routeklaar"; een volledige
   dagroute-/planningberekening is een aparte, pas op expliciet verzoek uit te voeren stap).
5. Als er geen accommodatiebesluit bestaat, meldt GOUD dat expliciet ("NOG NIET ONDERZOCHT") — nooit
   aannemen dat er nog niets gekozen is zonder eerst het register en de commit-historie te
   controleren.
6. Een chatvermelding of instructie die een concrete accommodatiekeuze of een sterke persoonlijke
   aanbeveling bevat, wordt zo snel mogelijk duurzaam naar het register/GitHub overgebracht in
   plaats van alleen in het gesprek te blijven staan.
7. Voor de kaartgeometrie van een accommodatie gelden dezelfde regels als voor kandidaten: alleen een
   `<Point>` toevoegen bij een geverifieerde Google Maps-marker; zonder voldoende markerbewijs wordt
   de accommodatie tekstueel opgenomen (adres, geen geraden coördinaat).

## PRE-BRONS en de detectorbibliotheek (INDIA2-architectuurbesluit, 2026-08-02, PR #23)

Fundamentele correctie op het oorspronkelijke BRONS-ontwerp: een sweep is geen locatie-
afwerklijst, maar een inhoudelijk detectieproces. BRONS was nooit bedoeld om een vooraf gegeven
lijst kandidaten af te werken — BRONS moet bewijzen dat de inhoudelijke werkelijkheid van een
gebied voldoende is afgedekt. Het aantal kandidaten is een UITKOMST van het onderzoek, nooit een
vooraf ingestelde invoer (geen minimum, geen maximum, niet kunstmatig aanvullen, niet vroeg
stoppen omdat er "genoeg" lijkt te zijn).

### Nieuwe volgorde

```
PRE-BRONS → detectoren → kandidaten → betekenis → onderscheid → Mark-relevantie
    → cluster/koepeltoets → GEO (BRONS) → ZILVER → GOUD → Mark-keuze
```

BRONS start dus niet meer met een gegeven naamlijst, maar met een intern consistente
regio-inhoudsbrief van PRE-BRONS (zie `india4/roles/PRE-BRONS.md`).

### PRE-BRONS

Vaste stap vóór elke BRONS-batch: bepaalt gebied, straal of functionele corridor, Marks bekende
interesses/A-criteria/ankers, relevante tradities/lineages/personen/heilige landschappen/
historische lagen, en welke detectoren van toepassing zijn. Levert vier bestanden onder
`runs/active/<run_id>/PRE_BRONS/`: `REGION_CONTENT_BRIEF.md` + `.json`,
`PRE_BRONS_DETECTORS.jsonl`, `SOURCE_FAMILY_PLAN.jsonl`. Structuur en verplichte velden:
`india4/templates/PRE_BRONS_REGION_CONTENT_BRIEF_TEMPLATE.md`. Validatie vóór BRONS mag starten:
`india4/scripts/validate_pre_brons_brief.py`. Bevat verplicht een expliciet antwoord op: "welke
dramatisch te missen A-locatie zou dit plan nog kunnen missen?" — nooit leeg of "geen" zonder
toelichting.

### Detectorbibliotheek

Een detector is een herbruikbare zoekrichting (traditie, lineage, bronfamilie, landschapstype,
enz.), cumulatief opgebouwd over regio's heen — bv. AOAY ontdekt tijdens Varanasi, mogelijk
Advaita-ashrams tijdens Kumaon, vroege boeddhistische kloosters tijdens Bodh Gaya. Elke sweep
levert daarom niet alleen kandidaten, maar ook een antwoord op: "hebben we een nieuwe detector
ontdekt?"

Canonieke bestanden:
- `india4/registries/DETECTOR_LIBRARY.jsonl` — één record per detector: `detector_id`
  (immutable), `name`, `definition`, `purpose`, `trigger_conditions`, `exclusion_conditions`,
  `required_source_families`, `applicability_facets`, `discovered_in_run`, `status`
  (PROVISIONAL/ACTIVE/RETIRED), `parent_detector_id`, `aliases`, `created_at`, `approved_by`.
- `india4/registries/DETECTOR_RUN_HISTORY.jsonl` — append-only scoregeschiedenis per
  (detector_id, run_id): toegepaste zoekrichtingen, nieuwe kandidaten, high-value leads (die de
  WHY_THIS_ONE/WHY_NOT_THE_OTHERS-toets overleefden), false positives, evaluatie. NIET genest in
  de bibliotheek zelf.

Validatie: `india4/scripts/validate_detector_library.py`.

**Wie mag wat:**
- CCI mag tijdens PRE-BRONS zelfstandig een nieuwe detector PROVISIONAL gebruiken om de sweep
  niet te blokkeren, vastgelegd in het per-run `PRE_BRONS_DETECTORS.jsonl`. Nooit automatisch
  canoniek ACTIVE.
- Na de run legt CCI PROVISIONAL detectoren voor aan INDIA2/ChatGPT voor promotie, aanscherping,
  samenvoeging of afwijzing.
- Uitsluitend INDIA2/ChatGPT (architect) mag canoniek: detectoren fuseren, ACTIVE maken,
  hernoemen, RETIRED zetten, parent-child-structuur wijzigen. CCI mag overlap en
  parent-child-relaties signaleren, niet zelf fuseren.
- Mark beslist alleen wanneer een detector zijn persoonlijke interesseprofiel of A-definitie
  inhoudelijk verandert.

**Scoring**: gemeten per gebiedstype/thema (zie `applicability_facets`), niet als één platte
globale ranglijst — een detector die sterk scoort in het ene soort gebied hoeft dat niet te zijn
in een fundamenteel ander soort gebied. Waardemaat is niet "aantal gevonden kandidaten" maar
"aantal kandidaten dat de differentiatietoets (WHY_THIS_ONE/WHY_NOT_THE_OTHERS) overleeft".

### Regiotype-taxonomie (applicability_facets)

Nog geen starre enkelvoudige lijst — te vroeg en te grof. Voorlopig multi-label, organisch
groeiend in de eerste 3-4 regio's, daarna door INDIA2 geconsolideerd tot een gecontroleerde
taxonomie:
- `settlement`: pelgrimsstad / kloosterstad / metropool / dorp / landschap
- `tradition`: hindoe / boeddhistisch / jain / sikh / islamitisch / christelijk / gemengd
- `sacred_form`: tempelnetwerk / ghatlandschap / samadhi-cluster / kloosterlandschap /
  yatra-corridor
- `temporal_layer`: oud / middeleeuws / koloniaal / modern
- `practice_state`: levend / gemengd / monumentaal
- `visitor_context`: lineage-specifiek / algemeen spiritueel / historisch / architectonisch

Geen vrije tekst zonder facetnaam.

### Verplichte kandidaatvelden vóór GEO-verificatie

Elke kandidaat krijgt, vóór GEO-verificatie: `why_this_one`, `why_not_the_others`,
`meaning_evidence`, `living_or_monumental`, `mark_relevance_link`. Zie
`india4/templates/BATCH_OUTPUT.md`. Dit voorkomt kandidaat-inflatie (honderden generieke
tempels) en de "beroemd-maar-leeg"-valkuil (plekken die historisch beroemd zijn maar
tegenwoordig nauwelijks nog levende betekenis hebben).

### Verzadigingsdrempel

Hybride harde/inhoudelijke regel — geen enkel magisch getal beslist alleen.

Per detector:
- minimaal twee wezenlijk verschillende zoekbenaderingen;
- minimaal twee relevante bronfamilies indien beschikbaar;
- alle gevonden high-value leads zijn opgelost als kandidaat, duplicaat, afgewezen of open
  onzekerheid;
- daarna leveren drie opeenvolgende materieel verschillende query-/bronrichtingen geen nieuwe
  high-value kandidaat of nieuwe detector meer op (alleen nog duplicaten, lage-waarde generieke
  locaties of reeds bekende context).

Op sweepniveau:
- alle detectoren hebben een afsluitstatus;
- alle bronfamilies zijn uitgevoerd of expliciet ONBESCHIKBAAR;
- geen open lead kan redelijkerwijs een dramatisch te missen A-locatie zijn;
- een cross-detector pass levert geen nieuwe high-value lead meer op.

Machine-status: `DISCOVERY_SATURATED` / `NOT_YET_SATURATED`. `REASONABLY_COMPLETE` is toegestaan
als mensleesbare samenvatting, nooit als primaire machine-status.

### Retroactiviteit

Deze correctie geldt ook voor de reeds afgeronde Varanasi-regio, maar begrensd: een
`VARANASI_DISCOVERY_COVERAGE_AUDIT` (niet een volledige herstart van de 40 GEO-records). Doel:
controleren of de bestaande 40-kandidatenlijst detector- en brondekking mist, actief zoeken naar
niet-ontdekte high-value kandidaten, en de bestaande 40 toetsen op `why_this_one`/
`why_not_the_others`/levend-vs-monumentaal/beroemd-maar-leeg. Geen A/B/C-wijziging zonder Mark,
niets stil verwijderen — uitsluitend missing leads, zwakke kandidaten, detectorgaten en
dekkingsstatus als output. Deze audit wordt apart en expliciet door Mark opgestart, niet
automatisch als onderdeel van een tooling-update.

## Scope-afspraak (belangrijk, expliciet door Mark vastgesteld op 2026-08-02)

CC (de Home Assistant-sessie) heeft hier een ARCHITECTUUR/TOOLING-rol — kritiek leveren, scripts
zoals `next_candidate.py`/`validate_brons.py` bouwen/onderhouden — GEEN uitvoerende rol in de
daadwerkelijke kandidaat-sweeps zelf. Een aparte, aan deze repo toegewijde Claude Code-sessie
voert de sweeps zelf uit, om te voorkomen dat sweep-werk Mark's tokens in de HA-sessie verbruikt.

## Volgende stap

Protocol is akkoord. Eerste testsweep (20 Varanasi-kandidaten, volledig autonome doorloop)
uitvoeren volgens bovenstaande regels, resultaat vastleggen onder `runs/active/`.
