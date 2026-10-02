# INDIA5 GOVERNANCE

Status: canoniek vanaf 2026-08-02 (migratie van eerdere PR #23-commentbesluiten, INDIA5-ARCH-HARDEN-002).
Dit bestand is de duurzame vastlegging van besluiten die eerder uitsluitend als PR-comment op
PR #23 bestonden. Waar een besluit al in een ander canoniek bestand stond, wordt hier
uitsluitend samengevat + doorverwezen, niet gedupliceerd.

## 1. Rolverdeling Mark / INDIA2 / CCI

Bron: PR #23, "INDIA5 — definitieve samenwerking en relay-test" (comment 5159416542).

**ChatGPT — India-regisseur/architect**
- ontwerpt en bewaakt INDIA5-protocollen;
- analyseert CCI-resultaten en fouten;
- bepaalt de volgende uitvoerstap;
- schrijft de concrete CCI-opdracht;
- controleert kwaliteit en consistentie;
- bouwt geen PDF tenzij Mark dat expliciet vraagt.

**CCI — India-uitvoerende engine**
- leest GitHub, registers en bestaande besluiten vóór nieuw onderzoek;
- voert begrensd BRONS/ZILVER/GOUD/TRAVEL-werk uit;
- bronvermelding verplicht, geen giswerk, geen geraden coördinaten;
- schrijft datasets, KML, registers, Markdown en commits;
- bouwt PDF uitsluitend op expliciet verzoek van Mark;
- rapporteert resultaat, blockers en tegenstrijdigheden in vaste velden (of, vanaf de
  taakarchitectuur: in `RESULT.md`).

**CC — Home Assistant-architectuur/tooling**
- blijft apart bestaan voor Home Assistant;
- heeft geen standaardrol in India-sweeps;
- wordt alleen betrokken wanneer Mark expliciet een India-toolingprobleem aan CC wil voorleggen;
- CCI mag CC niet zelfstandig inschakelen of tokens laten gebruiken.

**Mark**
- geeft doelen;
- beslist A/B/C, hotel en andere persoonlijke keuzes;
- beoordeelt gebruikersproducten;
- is eindbeslisser bij inhoudelijke tegenstrijdigheden.

### Escalatie

- inhoudelijke keuze, A/B/C, hotel, persoonlijke voorkeur of tegenstrijdige canon → direct naar Mark;
- architectuur/protocol/tooling → als blocker rapporteren; ChatGPT (INDIA2) bepaalt daarna de oplossing;
- nooit stilzwijgend oplossen;
- kandidaatgebonden onzekerheid blokkeert de rest niet.

## 2. PDF alleen op expliciet verzoek

Volledig canoniek vastgelegd in `india4/protocols/INDIA5-PROTOCOL.md`, sectie "PDF is eenmalig
— NIET automatisch herbouwen". Kern: de reisgids-PDF is een eenmalig leesdocument, geen
doorlopend kanaal. Data-updates blijven beperkt tot dataset/RUN.yaml/register/KML/MD, tenzij
Mark expliciet om een nieuwe PDF-build vraagt.

## 3. Detectorbibliotheek-governance

Bron: PR #23, "INDIA2 → CCI — BESLUITEN OP 7 OPEN VRAGEN" (comment 5159503692), punten 1, 2 en 7.

**Wie mag wat:**
- CCI mag tijdens PRE-BRONS zelfstandig een nieuwe detector PROVISIONAL gebruiken om een sweep
  niet te blokkeren, vastgelegd in het per-run `PRE_BRONS_DETECTORS.jsonl`. Nooit automatisch
  canoniek ACTIVE.
- Na de run legt CCI PROVISIONAL detectoren voor aan INDIA2/ChatGPT voor promotie, aanscherping,
  samenvoeging of afwijzing.
- Uitsluitend INDIA2/ChatGPT (architect) mag canoniek: detectoren fuseren, ACTIVE maken,
  hernoemen, RETIRED zetten, parent-child-structuur wijzigen. CCI mag overlap en
  parent-child-relaties signaleren, niet zelf fuseren.
- Mark beslist alleen wanneer een detector zijn persoonlijke interesseprofiel of A-definitie
  inhoudelijk verandert.

**Canoniek pad en schema** (nog niet gevuld met echte detectoren — de eerste inhoudelijke
PRE-BRONS-inzet staat nog gepauzeerd, zie sectie 7 hieronder):
`india4/registries/DETECTOR_LIBRARY.jsonl` (definities) + `india4/registries/DETECTOR_RUN_HISTORY.jsonl`
(append-only scoregeschiedenis, niet genest in de bibliotheek zelf). Regiotype-taxonomie
(`applicability_facets`): multi-label, organisch groeiend in de eerste 3-4 regio's, daarna door
INDIA2 geconsolideerd — geen starre enkelvoudige lijst nu.

## 4. PRE-BRONS-output en verzadigingsregels

Bron: PR #23, comment 5159503692, punten 4 en 6.

**PRE-BRONS-output** (vier bestanden per run onder `runs/active/<run_id>/PRE_BRONS/`):
`REGION_CONTENT_BRIEF.md` + `.json`, `PRE_BRONS_DETECTORS.jsonl`, `SOURCE_FAMILY_PLAN.jsonl`.
Verplichte inhoud: gebiedsgrens/straal/corridor, Marks bekende interesses/ankers, relevante
tradities/lineages/personen/heilige landschappen/historische lagen, toepasselijke ACTIVE
detectoren, nieuwe PROVISIONAL detectoren, geplande bronfamilies, bekende risico's/blinde
vlekken, kandidaatcategorieën die afgedekt moeten worden, vooraf gedefinieerde
verzadigings-/stopcontrole, en een expliciet antwoord op "welke dramatisch te missen A-locatie
zou dit plan nog kunnen missen?". BRONS start pas na interne consistentie (gevalideerd, zie
`india5/templates/PRE_BRONS_REGION_CONTENT_BRIEF_TEMPLATE.md`), zonder tussentijdse
Mark-goedkeuring bij normale voortgang.

**Verzadigingsdrempel** (hybride harde/inhoudelijke regel, geen los magisch getal): per
detector minimaal twee wezenlijk verschillende zoekbenaderingen, minimaal twee relevante
bronfamilies indien beschikbaar, alle high-value leads opgelost als kandidaat/duplicaat/
afgewezen/open onzekerheid, en daarna drie opeenvolgende materieel verschillende richtingen
zonder nieuwe high-value kandidaat of detector. Sweepniveau: alle detectoren hebben een
afsluitstatus, alle bronfamilies uitgevoerd of expliciet ONBESCHIKBAAR, geen open lead kan
redelijkerwijs een dramatisch te missen A-locatie zijn, cross-detector pass levert niets
nieuws op. Machine-status: `DISCOVERY_SATURATED` / `NOT_YET_SATURATED`; `REASONABLY_COMPLETE`
mag als mensleesbare samenvatting bestaan, nooit als primaire machine-status.

## 5. Immutable numbering

Volledig canoniek vastgelegd in `india4/protocols/INDIA5-PROTOCOL.md`, sectie "Immutable
Location Numbering" (Mark-besluit 2026-08-02, commit 58be47b), gehandhaafd door
`runs/active/<run_id>/scripts/validate_numbering.py` (per regio) en vanaf de tweede regio
aangevuld met `india5/scripts/validate_global_numbering.py` (repositorybreed, zie sectie 8
hieronder).

## 6. Instructieprecedentie (nieuw, INDIA5-ARCH-HARDEN-002)

Bij conflicterende instructies geldt, hoog naar laag:

1. de canonieke `TASK.yaml`/`TASK.md` van de actieve, gevalideerde taak op de bedoelde branch;
2. een expliciete `HOLD`/`ABORT`-status in de taakbestanden zelf (`STATUS.yaml.hold.active`);
3. het Mark-besluitenregister (`RUN.yaml protected_mark_decisions`, `MARK_DECISIONS*.jsonl`,
   `ACCOMMODATION_REGISTER.jsonl`, enz.);
4. PR-comments — uitsluitend als envelop/signaal (`CCI_TASK_ENVELOPE`/`CCI_RESULT_ENVELOPE`),
   nooit als inhoudelijke bron van waarheid;
5. chattekst en lokale hooks (bv. de stop-hook-git-check.sh-melding) — deze mogen NOOIT een
   actieve canonieke taak overschrijven of overrulen.

Zie ook `india5/TASK_PROTOCOL.md`, sectie "Vereiste werking", punt 8.

## 7. Task-file relay in plaats van lange comments

Volledig uitgewerkt in `india5/TASK_PROTOCOL.md`. PR-comments zijn voortaan alleen korte
enveloppen (`CCI_TASK_ENVELOPE`/`CCI_RESULT(_ENVELOPE)`); de taakinhoud, voortgang en
resultaten leven duurzaam in `india5/tasks/{queue,active,done,failed}/<TASK_ID>/`.

## 8. Cross-regio nummeringscontrole (nieuw, INDIA5-ARCH-HARDEN-002)

`india5/scripts/validate_global_numbering.py` (puur lezend) scant alle
`runs/*/NUMBERING_REGISTRY.jsonl`-bestanden repositorybreed en garandeert dat geen display_id
ooit in twee regio's aan verschillende fysieke locaties hangt. Op dit moment bestaat er één
regio (Varanasi, 001-040); dit script is de architectuur die vanaf regio 2 daadwerkelijk
in werking treedt. Een nieuwe regio moet vooraf een niet-overlappend nummerbereik reserveren
(zie scriptoutput voor het huidige bereik per regio).

## 9. Governance versus regio-uitvoering (nieuw, INDIA5-ARCH-HARDEN-002)

Aanbeveling: governance/canonieke architectuur (`india5/`, `india4/protocols/`) hoort in
versiebeheerde bestanden, onafhankelijk van welke PR ze introduceert. Elke toekomstige regio
krijgt idealiter een eigen run (`runs/active/<REGIO>-...`) en bij voorkeur een eigen PR. PR #23
blijft Varanasi + deze architectuurmigratie, en wordt NIET de permanente queue voor alle
toekomstige regio's — nieuwe regio-taken horen in `india5/tasks/`, ongeacht welke PR ze
uiteindelijk landt.
