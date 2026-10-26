# TASK — AOAY-FULL-LOCATION-ATLAS-001

```
task_id: AOAY-FULL-LOCATION-ATLAS-001
issued_by: INDIA
issued_at: 2026-08-16
mode: INVERSE_BOOK_CENTRIC_MEGASWEEP
scope: volledige Autobiography of a Yogi, hoofdstuk-voor-hoofdstuk
priority: MISSIEKRITISCH
```

## Mark-besluit
Mark wil het volledige *Autobiography of a Yogi* als het "andersommetje":

**boek → ALLE locaties die erin staan**

Niet alleen regio's waar al een reis-sweep bestaat en niet alleen beroemde of keuze-waarschijnlijke plekken.

## Hoofddoel
Bouw een reproduceerbare, volledige AOAY-locatie-atlas uit de canonieke volledige brontekst. Iedere locatievermelding wordt eerst rauw geregistreerd en pas daarna gededupliceerd/geclassificeerd.

De atlas moet later als orthogonale detectorlaag tegen elke regio-sweep en tegen de Top-11-persoon-atlas worden gekruist.

## Canonieke brontekst
Gebruik voor de primaire reproduceerbare extractie de volledige publieke Project Gutenberg-uitgave van *Autobiography of a Yogi* (1946-tekst), inclusief:
- alle hoofdstukken;
- voorwoord/inleidende tekst voor zover onderdeel van het boek;
- voetnoten;
- fotobijschriften/captions;
- appendices/nawoord indien aanwezig in de gebruikte tekst.

Leg exact vast welke Gutenberg-versie/URL/hash of gedownloade tekstversie is gebruikt.

Als een latere/andere editie aantoonbaar locatie-inhoud toevoegt of wijzigt: NIET stil mengen. Noteer als `EDITION_DELTA` voor een aparte latere vergelijking.

## Harde recall-regel — ALLES eerst opnemen
Registreer ELKE plaatsreferentie die fysiek/geografisch bedoeld kan zijn, ook wanneer deze voor Marks reis onbelangrijk lijkt.

Minimaal:
- land, staat/provincie, district, stad, dorp, gehucht;
- buurt, straat, adres, huis, kamer, landgoed;
- school, universiteit, ziekenhuis, hotel, station, kantoor, club, zaal;
- ashram, math, tempel, kerk, moskee, gurdwara, klooster, shrine;
- grot, berg, heuvel, rivier, meer, kust, bos, tuin, boom/veld indien locatie-relevant;
- geboorte-, woon-, verblijf-, bezoek-, meditatie-, initiatie-, ontmoeting-, les-, lezing-, samadhi-, crematie- of gebeurtenisplek;
- transitlocaties als station/treinhalte/routeplaats wanneer letterlijk genoemd;
- historische namen/spellingvarianten;
- plaatsen buiten India;
- brede geografische referenties als Himalaya/Bengalen wanneer letterlijk gebruikt;
- fysiek bedoelde maar niet exact identificeerbare plekken.

GEEN selectie op beroemdheid, huidige bezoekbaarheid, verwachte A/B/C of afstand.

## Ook opnemen, maar apart labelen
- mythische/devotionele/niet-aardse plaatsreferenties;
- allegorische of mogelijk niet-fysieke locatievermeldingen;
- onduidelijke toponiemen;
- alleen in een citaat/voetnoot/caption genoemde locaties.

Deze krijgen bijvoorbeeld `location_nature: MYTHIC_OR_NONPHYSICAL` of `UNCERTAIN`, maar worden niet weggegooid. Doel is dat "alle locaties die erin staan" controleerbaar waar is.

## Twee niveaus verplicht

### 1. RAW OCCURRENCE LOG — verliesloos
Iedere afzonderlijke vermelding in de tekst krijgt een occurrence-record, ook als dezelfde plek 30 keer voorkomt.

Minimaal per occurrence:
- occurrence_id;
- hoofdstuk/sectie;
- tekstanker of korte contextparafrase;
- ruwe plaatsnaam exact zoals in de bron;
- rol in passage;
- bronsoort: hoofdtekst / voetnoot / caption / appendix;
- actor(en) indien duidelijk;
- fysiek/geografisch bedoeld: JA/NEE/ONZEKER.

### 2. NORMALIZED PLACE ATLAS
Pas NA de raw log aliases/dubbele vermeldingen samenbrengen tot één fysieke plaatsidentiteit.

Minimaal per normalized place:
- atlas_id tijdelijk;
- canonical_name;
- aliases/historische spellingen;
- current_name indien anders;
- land/staat/district/stad;
- place_type;
- in_india: JA/NEE/ONZEKER;
- AOAY occurrence_ids;
- chapters;
- persons/events verbonden in AOAY;
- `event_verified_from_AOAY`;
- `physical_identity_verified`;
- `exact_sublocation_verified`;
- huidige mapping/status indien bekend;
- match met bestaande repo-ID indien later gevonden;
- claimgrenzen/onzekerheden.

## Classificatie — geen filtering
Classificeer pas na opname:

- `TIER_AOAY_EXACT_SITE` — concreet gebouw/terrein/grot/etc. identificeerbaar.
- `TIER_AOAY_EVENT_PLACE` — gebeurtenisplaats bewezen, exacte sublocatie onbekend.
- `TIER_AOAY_MENTION_ONLY` — genoemd als geografische/contextuele plek zonder relevante gebeurtenis.
- `TIER_AOAY_TRANSIT` — transit/pass-through.
- `TIER_AOAY_MYTHIC_OR_NONPHYSICAL` — niet als aardse reislocatie behandelen.

Alle tiers blijven in de atlas.

## Extractiemethode — minimaal drie onafhankelijke detectoren
Een simpele naamzoeklijst is onvoldoende. Gebruik minimaal:

1. **Hoofdstuk-voor-hoofdstuk menselijke/contextuele extractie** van de volledige brontekst.
2. **Machine-assisted place-token pass**: alle vermoedelijke toponiemen/hoofletters/geo-termen laten uitwerpen en tegen de raw log vergelijken.
3. **Known-entity reverse pass**: index/zoekvarianten voor landen, steden, dorpen, bergen, rivieren, stations, ashrams, gebouwen, historische spellingsvarianten en captions/voetnoten.

Elke detector levert een gap-list op. Een vermelding mag pas als false positive worden afgewezen met korte reden.

## Verplichte coverage-matrix
Maak voor ieder hoofdstuk/onderdeel een rij met:
- tekst volledig doorlopen: JA/NEE;
- voetnoten doorlopen: JA/NEE/NVT;
- captions doorlopen: JA/NEE/NVT;
- detector-2 vergeleken: JA/NEE;
- detector-3 vergeleken: JA/NEE;
- unresolved place tokens: aantal;
- status: NOT_STARTED / ACTIVE / SATURATED.

`AOAY_LOCATION_SWEEP_SATURATED: JA` mag alleen als ALLE delen SATURATED zijn en unresolved tokens 0 of expliciet als `UNRESOLVED_BUT_RECORDED` zijn vastgelegd.

## Belangrijk onderscheid
AOAY noemt een plek ≠ Yogananda was daar persoonlijk.

Per plaats apart vastleggen:
- `mentioned_in_AOAY`;
- `yogananda_personally_present` JA/NEE/ONZEKER;
- andere actor(en) die er volgens AOAY waren;
- gebeurtenis;
- exacte huidige locatie.

Nooit één uit de ander afleiden.

## Fasevolgorde

### Fase A — blind boekextract
Gebruik GEEN bestaande India-kandidaten of oude AOAY-audits als checklist tijdens de primaire extractie. Alleen de volledige AOAY-brontekst stuurt discovery.

### Fase B — freeze
Bevries RAW_OCCURRENCES + NORMALIZED_ATLAS + COVERAGE_MATRIX.

### Fase C — repo cross-check
Pas daarna vergelijken met:
- huidige 001+ location registry;
- Varanasi/Bodh Gaya/Kumaon en latere regio-runs;
- oude AOAY-audits;
- Top11 persoon-atlas.

Rapporteer minimaal:
- `AOAY_FOUND_AND_ALREADY_KNOWN`;
- `AOAY_FOUND_BUT_MISSING_FROM_REPO`;
- `REPO_AOAY_CLAIM_NOT_REFINDABLE_IN_BOOK`;
- `AOAY_PERSON_LINK_UPGRADE`;
- `AOAY_NEW_REGION_SIGNAL`;
- `EDITION_DELTA` indien van toepassing.

## Nummering / keuzes
- Tijdens extractie alleen tijdelijke `AOAY-ATL-*` IDs.
- Geen permanente reislocatie-ID vóór identity-check/reconciliatie.
- Geen A/B/C voorspellen namens Mark.
- Bestaande Mark-keuzes beschermd.
- Nieuwe AOAY-hoofdinformatie bij bestaande B/C => `MARK_DECISION_CONFLICT` indien keuze-relevant.

## Outputbestanden
Minimaal:
- `RAW_OCCURRENCES.jsonl`
- `PLACE_ATLAS.jsonl`
- `COVERAGE_MATRIX.md`
- `RESULT.md`
- `STATUS.md`

Resultaat moet ook compacte statistieken bevatten:
- totaal occurrence-records;
- totaal unieke normalized places;
- India vs buiten India;
- exact site vs event place vs mention-only vs transit vs mythic/nonphysical;
- nieuw t.o.v. repo;
- unresolved identities.

## Stopregel
CCI voert de volledige AOAY-extractie autonoom uit tot `AOAY_LOCATION_SWEEP_SATURATED: JA` of een echte blocker. Niet na een pilot stoppen. Geen PDF. Geen routeplanning.
