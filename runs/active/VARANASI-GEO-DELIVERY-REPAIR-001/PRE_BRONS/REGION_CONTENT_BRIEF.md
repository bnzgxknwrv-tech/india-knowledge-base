# PRE-BRONS Region Content Brief — Varanasi (discovery/coverage-audit)

run_id: VARANASI-GEO-DELIVERY-REPAIR-001
taak: INDIA5-VNS-DISCOVERY-COVERAGE-003
geschreven_op: 2026-08-03
geschreven_door: CCI

## Gebiedsgrens

Varanasi stad + straal van circa 20 km rond het centrum (Dashashwamedh Ghat, ~25.31°N 83.01°E).
Eén expliciet gevonden Jain-kalyanaksite (Chandraprabhu, Chandrawati/Chandrapuri) ligt op
circa 34 km en valt daarmee BUITEN deze straal — bewust niet als kandidaat opgenomen, zie
`DISCOVERY_CANDIDATES.jsonl` en RESULT.md voor de motivatie.

## Marks bekende interesses en ankers

- Kriya Yoga-lijn (Lahiri Mahasaya): al vertegenwoordigd via VNS-CAND-001/002, beschermd A
  sinds de vroegste vastgelegde instructie (`india4/prompts/BRONS-B01.md`).
- Boeddhistisch erfgoed Sarnath: volledig vertegenwoordigd (006, 029-034), allemaal A.
- Hoofd-ghats/tempels van de oude stad: uitgebreid vertegenwoordigd.
- Persoonlijke, niet-institutionele aanbevelingen tellen zwaar mee (precedent: hotelbesluit via
  Debby).

## Relevante tradities, lineages, personen, heilige landschappen en historische lagen

- Hindoeïsme (Shaivisme rond Kashi Vishwanath, Vishnuïsme, Shaktisme) — al breed vertegenwoordigd.
- Kriya Yoga/Lahiri Mahasaya-lijn — al vertegenwoordigd (001/002); onderzocht op uitbreiding
  (zie detector LINEAGE_TEXT_DETECTOR hieronder), geen nieuwe in-regio kandidaat gevonden buiten
  de al bestaande twee.
- Boeddhisme (Sarnath) — al volledig vertegenwoordigd.
- Kabir-traditie — al vertegenwoordigd (024/025).
- Aghor/Ramakrishna — al vertegenwoordigd (026/027/008).
- **Jainisme — NIET vertegenwoordigd vóór deze audit (0 van 40 kandidaten).** Varanasi/Kashi is
  de heilige geboorte-/kalyanaka-plaats van vier Jain-Tirthankara's (Parshvanath, Suparshvanath,
  Chandraprabhu, Shreyansanath) — een volledige, aantoonbaar aparte religieuze traditie die
  volledig ontbrak. Zie detector JAIN_HERITAGE_DETECTOR.
- **Koninklijke/wereldlijke geschiedenislaag — NIET vertegenwoordigd vóór deze audit.** De
  Kashi Naresh (koning van Benares)-lijn en het Ramnagar Fort ontbraken volledig; de bestaande
  40 zijn vrijwel uitsluitend religieus/spiritueel.
- **Islamitisch/soefi-erfgoed — NIET vertegenwoordigd, NIET als kandidaat toegevoegd.** Bewust
  gesignaleerd als hiaat, maar NIET zelfstandig ingevuld met een specifieke kandidaat vanwege de
  gevoeligheid rond sommige locaties in dit thema in Varanasi (zie RESULT.md, expliciet
  voorgelegd aan Mark/INDIA2 in plaats van zelf een keuze te maken).

## Toegepaste detectoren

Bibliotheek was leeg (geen ACTIVE detectoren) — alle vier hieronder zijn nieuw geïntroduceerd
als PROVISIONAL (zie `PRE_BRONS_DETECTORS.jsonl`):
- `DET-P001` LINEAGE_TEXT_DETECTOR
- `DET-P002` JAIN_HERITAGE_DETECTOR
- `DET-P003` ASI_ROYAL_HERITAGE_DETECTOR
- `DET-P004` GHAT_COMPLETENESS_DETECTOR

## Geplande bronfamilies

Zie `SOURCE_FAMILY_PLAN.jsonl`. Gebruikt: officiële kashi.gov.in-listings, Wikipedia, Jain-
religieuze naslagbronnen (jainsite.com, jaintreasures.org.uk, jainsamaj.org), reisbronnen ter
kruiscontrole (meerdere onafhankelijke sites per claim).

## Bekende risico's/blinde vlekken

- Deze audit is één onderzoeksronde, geen meervoudige-sessie-verzadiging — zie saturatiestatus
  in RESULT.md (NOT_YET_SATURATED, niet REASONABLY_COMPLETE).
- Geen lokale insider-/priesterbronnen geraadpleegd (alleen webbronnen) — de "inzichtersles" uit
  het eerdere filosofie-overleg is dus nog niet toegepast.
- Islamitisch/soefi-erfgoed is een bekend, onopgelost hiaat (zie hierboven).
- Geen GEO-marker-verificatie op Google Maps-niveau uitgevoerd voor de nieuwe kandidaten (dat is
  BRONS' taak, niet PRE-BRONS'; deze audit levert PROVISIONAL kandidaten met identiteits-
  bewijs, geen bevestigd coördinaat).

## Verwachte kandidaatcategorieën die dit plan afdekt

Lineage-uitbreiding (getoetst, niets nieuws), Jain-erfgoed (3 nieuwe), koninklijke/wereldlijke
geschiedenis (1 nieuwe), ghat-volledigheid (1 nieuwe).

## Verzadigings- en stopcriteria (vooraf)

Per detector: minimaal 2 zoekbenaderingen, stoppen bij 3 opeenvolgende richtingen zonder nieuwe
high-value lead. Sweepniveau: DISCOVERY_SATURATED pas bij afsluitstatus voor alle toegepaste
detectoren EN geen enkele resterende open lead die redelijkerwijs een dramatisch te missen
A-locatie kan zijn.

## Dramatic miss check

**Vraag: welke dramatisch te missen A-locatie zou dit plan nog kunnen missen?**

Antwoord: het Islamitisch/soefi-erfgoed van Varanasi (een stad met een aanzienlijke moslimgemeenschap
en historische soefi-tradities) is met deze audit NOG NIET onderzocht op kandidaten — dat is het
grootste resterende, expliciet erkende gat. Daarnaast is er geen insider-/priesterbron geraadpleegd,
wat volgens het eerdere filosofie-overleg juist de belangrijkste bron is voor werkelijk verborgen
parels; deze audit steunt uitsluitend op webbronnen. Beide punten worden expliciet, niet
stilzwijgend, als openstaand gemeld in RESULT.md.
