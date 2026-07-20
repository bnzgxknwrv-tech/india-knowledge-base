# BRONS-audit — VARANASI-COMPLETE-001

## Preflight en context

- GitHub-read en GitHub-write vóór inhoudelijk werk aantoonbaar getest.
- `NEXT_ACTION`, run, state, events en BRONS-context stemden overeen.
- State/eventcursor stonden synchroon op `READY_FOR_BRONS` / `EVT-0002`; geen actieve claim.
- Alle required files volledig gelezen; alle gepinde blob-SHA's en sentinels kwamen overeen.
- Alleen de twee expliciet getriggerde Kumaon-GOUD-bestanden zijn aanvullend gelezen.
- Geen forbidden file gebruikt of gewijzigd.
- De BRONS-workerclaim is vóór onderzoek als ACTIVE vastgelegd.

## Scope

- Volledige brede Varanasi/Kashi- en Sarnath-detectie uitgevoerd.
- Alle verplichte detectoren behandeld.
- Repositorybrede formele A/B-kaartinventaris uitgevoerd.
- `KUMAON-ROUTE-OPTIMIZATION-001` niet gelezen of gewijzigd.
- Geen oude BRONS-, ZILVER- of GOUD-output overschreven.
- Geen route, hotel, basis, statusbesluit, PARELS of pipelinewerk uitgevoerd.

## Registers

- kandidaten: 40 unieke IDs;
- claims: 57 unieke IDs;
- geaccepteerde bronnen: 22 unieke IDs;
- afgewezen bronnen: 6 unieke IDs;
- ieder claim-source-ID resolveert exact eenmaal;
- detectorchecks: 8;
- negatieve zoekrecords: 6;
- working-GEO-records: 40;
- image-records: 40 expliciete beeldtekortrecords;
- experience-records: 40 expliciete reviewtekortrecords;
- proximity-records: 15;
- master A/B-records: 30;
- KML-placemarks: 30.

## A/B-dekking

- 28 formele A exact behouden;
- 2 formele B exact behouden;
- voorbereide KML: 28 A + 2 B;
- C, stations, routes, bases en hotels: 0;
- dubbele niet-lege LOCATION_ID's: 0;
- ontbrekende coördinaten: 0;
- stille weglatingen: 0.

## GEO

Bestaande geldige Kumaon-GEO is hergebruikt. Voor andere formele locaties zijn herkenbare pins, terreincentra, adressen of lokale werkpunten gebruikt. Onzekerheid is zichtbaar en de exacte bezoekersingang is niet als vrijgavevoorwaarde gebruikt.

## Finale GitHub-readback

- alle rapportdelen, kandidaten, claims, accepted/rejected sources, detectoren, negatieve zoekresultaten, GEO, nabijheid, formele A/B-dekking, masterregister en handoff zijn opnieuw vanuit de bestaande werkbranch gelezen;
- alle tekstbestanden eindigen zichtbaar met `END_OF_ARTIFACT`;
- `images.jsonl` Git-blob-SHA `3300048f4ce95746637e4c9c501c501115a50ce2` is bytegelijk aan de lokaal gevalideerde 40-recordversie;
- `experience_reviews.jsonl` Git-blob-SHA `805c9152450809c50b3c468a5b8d595ef90a8ff0` is bytegelijk aan de lokaal gevalideerde 40-recordversie;
- `INDIA_ALL_FORMAL_A_B_WORKING_PREPARED.kml` Git-blob-SHA `510ccbcbc8665b12ba2edff807638558f41a677d` is bytegelijk aan de lokaal gevalideerde XML-versie;
- XML opent en sluit geldig; folders zijn exact `A_FORMEEL` en `B_FORMEEL`;
- placemarktelling is exact 28 A, 2 B en 30 totaal;
- de KML bevat geen C, routes, treinhaltes, bases, hotels of categorie-logo's.

## Kwaliteitsuitkomst

Technische integriteit vóór completion: PASS.
Inhoudelijke uitkomst: PARTIAL wegens open microtopografie/toegang, expliciet onvolledige beelden/reviews en tijdgevoelige praktische informatie.

END_OF_ARTIFACT
