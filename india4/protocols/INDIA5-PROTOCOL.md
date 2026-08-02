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

## Scope-afspraak (belangrijk, expliciet door Mark vastgesteld op 2026-08-02)

CC (de Home Assistant-sessie) heeft hier een ARCHITECTUUR/TOOLING-rol — kritiek leveren, scripts
zoals `next_candidate.py`/`validate_brons.py` bouwen/onderhouden — GEEN uitvoerende rol in de
daadwerkelijke kandidaat-sweeps zelf. Een aparte, aan deze repo toegewijde Claude Code-sessie
voert de sweeps zelf uit, om te voorkomen dat sweep-werk Mark's tokens in de HA-sessie verbruikt.

## Volgende stap

Protocol is akkoord. Eerste testsweep (20 Varanasi-kandidaten, volledig autonome doorloop)
uitvoeren volgens bovenstaande regels, resultaat vastleggen onder `runs/active/`.
