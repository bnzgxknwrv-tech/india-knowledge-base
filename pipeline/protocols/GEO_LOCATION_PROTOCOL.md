# GEO Location Protocol v1.0

## Doel

Zorgt dat rapporten, KML, Google My Maps en reisdocumenten naar dezelfde fysieke punten verwijzen.

## Identifiers

`IND-PLACE-*` is de interne database-ID. `LOCATION_ID` is de permanente reis- en kaart-ID. Beide blijven bestaan en worden nooit hergebruikt.

## Clusterblokken

- Delhi/aankomst: `100-199`.
- Braj: `200-299`.
- Volgende reisclusters krijgen opeenvolgende vrije blokken van 100 volgens de definitieve reisvolgorde.
- Een clusterblok overlapt nooit met een ander blok.
- Gaten zijn toegestaan.

## GEO-record

Iedere kandidaat krijgt in GOUD exact één record in `geo_locations.jsonl` met:

- `location_id`;
- `candidate_id` en waar beschikbaar `place_id`;
- `canonical_name`;
- `cluster`;
- `latitude_wgs84`;
- `longitude_wgs84`;
- `geo_point_type`: `VISITOR_ENTRANCE`, `EXACT_SITE`, `COMPLEX_CENTRE` of `ESTIMATED`;
- `geo_verification_status`: `VERIFIED_TWO_SOURCES`, `VERIFIED_ONE_AUTHORITATIVE_SOURCE`, `CONFLICTED` of `NOT_ESTABLISHED`;
- `geo_sources`;
- `google_maps_url`;
- `point_choice_reason`;
- `checked_at`;
- `recheck_before` waar relevant.

Geen coördinaat wordt afgeleid uit alleen een plaatsnaam of willekeurig complexmiddelpunt. Bij bezoekbare complexen heeft de logische bezoekersingang voorkeur.

## Verbindingen

`geo_connections.jsonl` bevat per gebruikte verbinding:

- `from_location_id`;
- `to_location_id`;
- `mode`;
- `estimated_time_min`;
- `distance_km` indien betrouwbaar;
- `source_or_method`;
- `checked_at`;
- `traffic_or_access_notes`;
- `status`.

Alle tijden worden berekend vanaf de geverifieerde punten. Een onbekende of volatiele waarde blijft open en wordt niet gegokt.

## C-locaties

C-locaties blijven in alle registers en GEO-datasets. Alleen routegebruik kan later worden uitgesloten.

## Rollen

GOUD verzamelt en valideert GEO-data maar maakt geen KML en kent geen A/B/C toe. INDIA2 maakt na technische vrijgave kaartlagen, KML en mensentaalproducten.

END_OF_ARTIFACT