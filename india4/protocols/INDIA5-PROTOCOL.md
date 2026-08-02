# INDIA5-PROTOCOL (voorstel, wacht op akkoord ChatGPT)

Status: DRAFT — voorgesteld door CC (Home Assistant-sessie) op 2026-08-02, na kritiek op het
oorspronkelijke INDIA5-voorstel van ChatGPT. Nog geen bevestigd akkoord ontvangen. Lees dit
document eerst volledig voordat je verder werkt aan een sweep.

## Doel

Niet één regio (Varanasi) handmatig oplossen, maar een architectuur waarmee uiteindelijk
duizenden locaties verwerkt kunnen worden met zo min mogelijk handmatige tussenkomst van Mark.

## Waarom het oude INDIA4-protocol faalde

`india4/roles/BRONS.md` schreef letterlijk "Stop daarna" voor na elke kandidaat — dat forceerde
één chatronde per kandidaat, wat bij honderden/duizenden kandidaten onhoudbaar is. Root-cause
volledig gedocumenteerd in `runs/active/VARANASI-GEO-DELIVERY-REPAIR-001/ROOT_CAUSE.md`.

## Rolverdeling

- **CONTROLLER**: bepaalt scope, kiest eindproducten, start een batch. Leest bij elke start
  uitsluitend `runs.jsonl` (append-only journaal) om te bepalen waar verder te gaan.
- **BRONS**: verwerkt precies ÉÉN batch van 15-25 kandidaten (niet "alle kandidaten in RAM" —
  dat bestaat niet voor een chat-agent, elke kandidaat kost context ongeacht wanneer je commit).
  Puur onderzoek → JSON. Eén lokaal checkpoint elke ~5 kandidaten (géén git-commit, puur
  crashbescherming). Eén git-commit aan het eind van de batch.
- **ZILVER**: leest alleen de JSON van die batch, valideert bronnen/Google Maps/consistentie.
  Her-zoekt UITSLUITEND als een kandidaat's status ≠ `CONFIRMED` (harde regel, geen open
  "tenzij nodig"-oordeel). Eén commit.
- **GOUD**: bouwt eindproducten (PDF/KML/kaart/print/A-B-C-overzicht) — alleen op expliciet
  verzoek of bij afronding van een hele regio, NIET automatisch na elke kleine batch. Eén commit.

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

## Eerste testdoel

Eén complete sweep op een klein deel van Varanasi (~20 kandidaten), volledig volgens dit
protocol: exact 3 commits (BRONS/ZILVER/GOUD), één leesbaar eindrapport. Geen 20 losse
handelingen van Mark.

## Scope-afspraak (belangrijk, expliciet door Mark vastgesteld op 2026-08-02)

CC (de Home Assistant-sessie) heeft hier een ARCHITECTUUR/TOOLING-rol — kritiek leveren, scripts
zoals `next_candidate.py`/`validate_brons.py` bouwen/onderhouden — GEEN uitvoerende rol in de
daadwerkelijke kandidaat-sweeps zelf. Een aparte, aan deze repo toegewijde Claude Code-sessie
voert de sweeps zelf uit, om te voorkomen dat sweep-werk Mark's tokens in de HA-sessie verbruikt.

## Volgende stap

Wacht op ChatGPT's akkoord (of tegenpunt) op dit protocol, vastgelegd in de HA-sessie chat. Zodra
bevestigd: eerste testsweep volgens bovenstaande regels uitvoeren, resultaat hier vastleggen onder
`runs/active/`.
