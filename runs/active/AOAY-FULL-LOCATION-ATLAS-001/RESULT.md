# RESULT — AOAY-FULL-LOCATION-ATLAS-001

```
task_id: AOAY-FULL-LOCATION-ATLAS-001
trigger: CCI_TASK 082 (INDIA, TASK.md commit d82315f4, STATUS.md commit 8a345e2a)
uitgevoerd_door: CCI
uitgevoerd_op: 2026-08-16
status: SUBSTANTIEEL_VOORTGANG — NIET SATURATED, zie eerlijke stand hieronder
```

## Bron

Project Gutenberg eBook #7452, "Autobiography of a Yogi" door Paramahansa Yogananda.
Plain-text UTF-8-editie, gedownload van `https://www.gutenberg.org/ebooks/7452.txt.utf-8`.

```
sha256: 1299580d5017a3b63194d739394ffec7a63145e6789c04cfc95be3241a0d7d79
bestandsgrootte: 983.099 bytes / 20.104 regels
Gutenberg release date: 1 februari 2005; laatst bijgewerkt: 28 augustus 2025
```

48 hoofdstukken (geen apart appendix/epiloog-hoofdstuk; voetnoten staan aan het einde van elk
hoofdstuk, geïntegreerd in de doorlopende tekst zoals de online-editie zelf aangeeft). Preface
(Evans-Wentz) en "List of Illustrations" zijn onderdeel van de gedownloade tekst maar zijn in deze
ronde niet apart als hoofdstuk doorzocht — zie beperkingen hieronder.

## Methode — drie onafhankelijke detectoren, zoals verplicht

1. **Hoofdstuk-voor-hoofdstuk structuuranalyse**: het boek is machinaal in 48 losse
   hoofdstukbestanden gesplitst op de canonieke `CHAPTER: N`-markers, met regelnummer-precisie.
2. **Detector 2 — machine-assisted place-token pass**: een reproduceerbaar Python-script
   (`detector2_tokens.py`) extraheert alle hoofdletter-woordreeksen (1-4 woorden) per hoofdstuk,
   plus alle `[Illustration: ...]`-captions (52 gevonden) en voetnootregels apart. Resultaat:
   7.095 distincte kandidaat-tokentypes over het hele boek.
3. **Detector 3 — known-entity reverse pass**: een gecureerde gazetteer van 123 bekende
   geografische termen (landen, staten, steden, rivieren, bergen, historische spellingsvarianten,
   reeds uit de Top-11-sweep bekende adressen) is met woordgrens-matching tegen elk hoofdstuk
   gelegd (`detector3_gazetteer.py`). Resultaat: 1.359 bevestigde occurrences over 123 unieke
   plaatsen.
4. **Menselijke steekproefcontrole (gedeeltelijk detector 1)**: de circa 600 meest frequente
   kandidaat-tokens uit detector 2 die NIET al in de gazetteer zaten, zijn handmatig doorgelopen
   op twee rondes. Dit leverde 30 nieuwe, echte plaatsen op (zie hieronder) die zijn toegevoegd aan
   de gazetteer en opnieuw doorgedraaid.

Alle scripts + tussenoutput (`detector2_output.json`, `detector3_output.json`) zijn reproduceerbaar
en blijven in de taak-scratchruimte bewaard; de repo bevat de bevroren eindresultaten
(`RAW_OCCURRENCES.jsonl`, `PLACE_ATLAS.jsonl`).

## Eerlijke stand — waarom dit NIET `SATURATED` is

`AOAY_LOCATION_SWEEP_SATURATED: NEE`, conform de taakregel dat dit alleen mag wanneer ALLE
onopgeloste tokens tot 0 zijn teruggebracht of expliciet `UNRESOLVED_BUT_RECORDED` zijn.

- Van de 7.095 detector-2-tokentypes zijn er nu 123 (met 1.359 occurrences) bevestigd als echte
  plaats, en zijn circa 600 hoogfrequente overige tokens handmatig gecontroleerd (voornamelijk
  persoonsnamen, aanspreektitels, schrifttitels, gewone woorden — geen gemiste plaatsen gevonden
  in deze steekproef buiten de 30 al toegevoegde).
- **Er blijven circa 6.691 tokentypes over de volle 48 hoofdstukken volledig ongeverifieerd** —
  overwegend lage-frequentie persoonsnamen op basis van het waargenomen patroon, maar dit is een
  aanname, geen individueel bewezen feit per token. Dit is expliciet `UNRESOLVED_BUT_RECORDED`,
  zie `COVERAGE_MATRIX.md` voor de exacte verdeling per hoofdstuk.
- De Preface (Evans-Wentz) en List of Illustrations zijn nog niet apart als eigen "hoofdstuk" door
  de detectoren gehaald.
- Geen enkele plek is beoordeeld op `event_verified_from_AOAY` / `physical_identity_verified` /
  `exact_sublocation_verified` op het niveau van individuele occurrences — dat vereist het
  daadwerkelijk lezen van de omliggende alinea per occurrence, wat bij 1.359 occurrences een
  aparte, grote vervolgstap is.

Dit is dus een **stevige, reproduceerbare eerste-fase-oogst met echte, geverifieerde nieuwe
vondsten** — geen doe-alsof-volledige sweep. Zie STATUS.md voor het concrete vervolgvoorstel.

## Statistieken

- totaal occurrence-records: **1.359** (1.300 hoofdtekst, 39 voetnoot, 20 caption)
- totaal unieke genormaliseerde plaatsen: **123**
- in India: 82 · buiten India: 35 · onzeker/grensgeval (historisch Brits-Indië, nu ander land): 6
- tier-verdeling: `TIER_AOAY_MENTION_ONLY` 71 · `TIER_AOAY_EVENT_PLACE` 23 ·
  `TIER_AOAY_EXACT_SITE` 21 · `TIER_AOAY_TRANSIT` 7 · `TIER_AOAY_MYTHIC_OR_NONPHYSICAL` 1
  (Badrinarayan, expliciet als legendarisch gelabeld, niet als aards reisdoel)

## Fase C — vergelijking met bestaande repo (Top-11-atlas + regio-sweeps)

**30 plaatsen zijn `AOAY_FOUND_BUT_MISSING_FROM_REPO`** (nog niet als kandidaat elders vastgelegd):

- **Sterkste nieuw signaal: Kashmir-cluster.** Twee volledige hoofdstukken (20 "We Do Not Visit
  Kashmir", 21 "We Visit Kashmir") + Srinagar, Gulmarg — een compleet nieuwe regio die in geen
  enkele bestaande regio-sweep of Top-11-atlas voorkomt. `AOAY_NEW_REGION_SIGNAL`.
- **Calcutta-institutiecluster**: Gurpar Road (vult het adres-gat uit Yogananda's Top-11-entry
  ATL-PY-003 exact in), Kalighat Temple, Bhowanipur, Scottish Church College, Calcutta University
  — vijf nieuwe, concrete Calcutta-plekken naast de al bekende Belur/Dakshineswar/Cossipore-cluster.
- **Santiniketan** (Tagore's school, hfst. 29) — nieuw, geen bestaande Tagore-link in de repo.
- **Rishikesh, Hardwar, Dehra Dun** — nieuw t.o.v. bestaande regio-sweeps.
- **Madras, Hyderabad, Bangalore, Kolar, Nasik, Ahmedabad, Poona** — losse Zuid-/West-Indiase
  transitpunten, elk te dun voor een eigen cluster, wel individueel vastgelegd.
- Overige (Kedarnath, Amarnath, Nanda Devi, Burdwan, Kidderpore, Ranbajpur, Bishnupur, Ichapur,
  Purulia, Dwarka, Yogoda Math) zijn losse, lager-geprioriteerde `TIER_AOAY_MENTION_ONLY`-punten.

**`AOAY_FOUND_AND_ALREADY_KNOWN`** (bevestigt bestaande Top-11-atlas rechtstreeks vanuit AOAY's
eigen brontekst — sterke onafhankelijke bronbevestiging): Serampore, Ranchi, Puri (Karar Ashram),
Dakshineswar, Danapur, Ranikhet, Ghurni, Gorakhpur, Bareilly, Allahabad, Belur, Almora, Naini Tal,
Wardha, Mysore, Dihika, Nadia, Abu/Mount Abu, Rajputana.

**`AOAY_PERSON_LINK_UPGRADE`**: Almora bevestigt onafhankelijk het `REGION_MISS`-signaal dat al in
de Vivekananda-sweep (`ATL-VK-009`) was vastgelegd — nu tweemaal onafhankelijk gevonden (Top-11-
sweep buiten het boek om, én rechtstreeks in AOAY's eigen tekst).

**Geen `EDITION_DELTA`**: er is in deze ronde geen tweede editie vergeleken.

**Geen `MARK_DECISION_CONFLICT`**: geen van de nieuwe vondsten raakt een bestaand A/B/C-besluit.

## Voorstel voor vervolg

1. **Kashmir-cluster** verdient een eigen gerichte reconciliatie-/discovery-taak (analoog aan
   Kumaon) — dit is het sterkste onbenutte signaal uit heel deze sweep.
2. Voor de resterende ~6.700 onopgeloste tokens: geen blinde verdere brute-force, maar gerichte
   detector-1-hoofdstuklezing voor de hoofdstukken met de hoogste `unresolved_tokens`-telling
   (12, 41, 42, 44, 48 — zie `COVERAGE_MATRIX.md`), waar de kans op gemiste plaatsen het grootst is.
3. Voor de 1.359 bevestigde occurrences: een tweede pass om per occurrence
   `event_verified_from_AOAY`/`physical_identity_verified`/`exact_sublocation_verified` in te
   vullen, te beginnen bij de 30 nieuwe plaatsen.

Geen PDF. Geen route. Geen A/B/C namens Mark.

---
Geschreven door: CCI. `PDF_STATUS: VERBODEN` gerespecteerd.
