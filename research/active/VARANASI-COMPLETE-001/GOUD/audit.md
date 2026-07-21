# GOUD-audit — VARANASI-COMPLETE-001

## Preflight en context

- GitHub-read en admin-write bevestigd;
- `NEXT_ACTION.yaml` matchte exact run, GOUD, `READY_FOR_GOUD` en het gepinde contextmanifest;
- state en eventcursor waren synchroon op `EVT-0012` vóór claim;
- ZILVER-workerclaim en controllerclaim waren gesloten;
- alle 34 required files en 15 getriggerde optionals volledig gelezen;
- alle gepinde blob-SHA’s en tekstsentinels matchten;
- forbidden files gebruikt: 0;
- `research/active/KUMAON-ROUTE-OPTIMIZATION-001/**` gelezen of gewijzigd: 0;
- GOUD-claim vastgelegd in commit `484cb3dcac961e4963b04e3492952e1c440d5c5c`.

## Registers en bewijs

- kandidaten: 40 unieke IDs;
- claims: 57 unieke IDs;
- accepted bronnen: 25 unieke IDs;
- rejected bronnen: 7 unieke IDs;
- source-ID-overlap accepted/rejected: 0;
- ontbrekende claim-sourceverwijzingen: 0;
- detectorchecks: 8;
- negatieve searches: 6;
- praktische toegangsrecords: 40;
- beeldrecords: 40;
- reviewrecords: 40.

## GEO en verbindingen

- `geo_locations.jsonl`: 40 records met alle verplichte GEO-velden;
- `geo_connections.jsonl`: 15 records met alle verplichte verbindingsvelden;
- nieuwe permanente `place_id`: 0;
- nieuwe permanente `location_id`: 0;
- Lahartara en Bhaskarananda blijven `ESTIMATED`/`NOT_ESTABLISHED`;
- Lahiri Samadhi, Lahiri-huis en Trailanga Math blijven werkpunten zonder ingangprecisie;
- reistijdclaims: 0;
- routebesluiten: 0.

## Formele A/B en KML

- formele A: 28;
- formele B: 2;
- KML-placemarks: 30;
- KML-folders: 2;
- A-stijl: uitsluitend `A_GREEN`, `ff00aa00`;
- B-stijl: uitsluitend `B_ORANGE`, `ff00a5ff`;
- C, stations, routes, bases, hotels en categorie-logo’s: 0;
- dubbele niet-lege LOCATION_IDs: 0;
- ontbrekende coördinaten: 0.

## Canonieke integratie

- voorstel vooraf gecommit: `9e3b17026d472e0235bd892bcb5aa802820fe879`;
- registrywrite: `8f23111b8d9810e9673d7853619b21ce15f57a4c`;
- gewijzigde bestaande records: `IND-PLACE-000001`, `IND-PLACE-000002`;
- nieuwe records of IDs: 0;
- gewijzigde formele status: 0;
- gewijzigde decision-ID: 0;
- decisions-indexwrite: 0;
- registry JSONL opnieuw gelezen en geldig.

## Quality gate

Technische integriteit: `PASS`.
Inhoudelijke status: `PARTIAL`.

Hoogste niet-fatale gaten:

1. Lahartara en Bhaskarananda/Anand Bagh: exacte micro-identiteit, beheer, toegang en GEO niet vastgesteld.
2. Lahiri Samadhi/Satyalok, Lahiri-huis en Trailanga Math: directe beheer- en toegangsinformatie open.
3. Volledige tien-functionele beeldsets en systematische recente reviews ontbreken.
4. Opening, fotografie, buitenlandse toegang, festivals en drukte blijven tijdgevoelig.

## Scopeverboden

- formele/adviserende A/B/C toegekend of gewijzigd: `NEE`;
- nieuw decision-ID: `NEE`;
- nieuwe permanente ID: `NEE`;
- route, basis, station, hotel of eerste bezoek gekozen: `NEE`;
- pipeline of protocol gewijzigd: `NEE`;
- parked-run gelezen of gewijzigd: `NEE`.

END_OF_ARTIFACT