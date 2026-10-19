# ZILVER_REPORT — Bodh Gaya (046-049)

run_id: BODHGAYA-DISCOVERY-001
geschreven_op: 2026-08-03
geschreven_door: CCI

ZILVER-controle voor uitsluitend de vier genummerde kandidaten (046-049). Geen nummers gewijzigd,
geen A/B/C, geen KML/PDF/reisplanning.

## Methode voor GEO-verificatie

Naast de reguliere brontoetsing is gezocht naar rechtstreekse Google Maps/Earth-entiteitsdata
(via `google.com/earth/rpc/entity`-links die soms rechtstreeks in zoekresultaten verschijnen,
inclusief Google Feature ID en, waar aanwezig, Google Plus Code) — een gestructureerde, door
Google zelf teruggegeven respons, niet een tekstsamenvatting van een derde partij. Dit is een
sterker bewijsniveau dan de eerdere "referentiecoördinaten van meerdere aggregatoren" en is voor
twee van de vier kandidaten gevonden.

## Per kandidaat

### 046 — Mahabodhi Temple Complex

`geo_status`: **CONFIRMED** (was `GOOGLE_MAPS_MARKER_NOT_CONFIRMED`). Rechtstreekse Google Earth-
entiteit, naam-gematcht op "Mahabodhi Temple", coördinaat 24.6959222°N, 84.9914193°E. Identiteit,
betekenis en bezoekbaarheid ongewijzigd bevestigd.

### 047 — Sujata Stupa, Bakraur

`geo_status`: **CONFIRMED** (was `GOOGLE_MAPS_MARKER_NOT_CONFIRMED`, expliciete conflictzaak).
Rechtstreekse Google Earth-entiteit, naam-gematcht op "The Sujata Stupa" (niet slechts het dorp
Bakraur), coördinaat 24.6979887°N, 85.0033228°E, met een Google Plus Code (M2X3+58W) als extra
bevestiging. **047_CONFLICTUITKOMST: OPGELOST** — de eerder gevonden tweede coördinatenset
(24.69791/85.00332) bleek er het dichtst bij te liggen; de andere twee sets zijn vervangen.

### 048 — Dungeshwari Cave Temples (Mahakala Caves)

`geo_status`: **ONGEWIJZIGD**, blijft `GOOGLE_MAPS_MARKER_NOT_CONFIRMED`. Twee aanvullende,
wezenlijk verschillende zoekpogingen deze ronde (directe Google-entiteitszoekactie, gerichte
coördinaat-zoekactie) leverden geen resultaat op. Identiteit blijft eenduidig bevestigd via twee
overheidsbronnen. Geen schatting overgenomen.

### 049 — Great Buddha Statue

`geo_status`: **ONGEWIJZIGD**, blijft `GOOGLE_MAPS_MARKER_NOT_CONFIRMED`. Geen Google-entiteit
gevonden; het Wikipedia-infobox-coördinaat blijft uitsluitend referentiemateriaal.

**Inhoudelijke correctie gevonden**: de hoogte van het beeld bleek inconsistent tussen bronnen
(18,5 m infobox / 20 m hoofdtekst voor het beeld zelf / 24 m totale constructie inclusief
voetstuk en lotus — eerder in het kandidaatrecord onnauwkeurig samengevat als "25 meter"). Dit is
gecorrigeerd in `DISCOVERY_CANDIDATES.jsonl` met vermelding van de brondiscrepantie.

**Hercontrole OPTIONAL_PASS-status (specifiek gevraagd)**: bevestigd. De kernfeiten die de
OPTIONAL_PASS-classificatie dragen — eerste/grootste in India gebouwde Boeddhabeeld op het moment
van bouw, consecratie door de 14e Dalai Lama in 1989 — staan los van de exacte hoogtediscussie en
blijven overeind. Geen aanleiding gevonden om de tier te wijzigen (niet naar CORE_PASS, niet naar
WATCHLIST).

## Samenvatting

| # | Kandidaat | geo_status voor | geo_status na | Wijziging |
|---|---|---|---|---|
| 046 | Mahabodhi Temple Complex | NOT_CONFIRMED | **CONFIRMED** | rechtstreekse Google-entiteit |
| 047 | Sujata Stupa | NOT_CONFIRMED (conflict) | **CONFIRMED** | conflict opgelost, rechtstreekse Google-entiteit |
| 048 | Dungeshwari Cave Temples | NOT_CONFIRMED | NOT_CONFIRMED | geen wijziging, geen schatting |
| 049 | Great Buddha Statue | NOT_CONFIRMED | NOT_CONFIRMED | geen wijziging; hoogtecijfer gecorrigeerd, OPTIONAL_PASS herbevestigd |

Geen nummer gewijzigd. Geen A/B/C toegekend. Geen KML, PDF of reisplanning uitgevoerd.

---
Geschreven door: CCI, op verzoek van INDIA2/CHATGPT (PR #23, bericht 002).
