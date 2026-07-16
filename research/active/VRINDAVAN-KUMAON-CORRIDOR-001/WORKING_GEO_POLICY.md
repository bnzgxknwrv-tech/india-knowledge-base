# WORKING_GEO policy — VRINDAVAN-KUMAON-CORRIDOR-001

## Doel

Deze run maakt een praktisch kaart- en routebesluit mogelijk zonder bruikbare locaties leeg te laten omdat een exacte bezoekersingang nog niet dubbel is geverifieerd.

Dit document is een run-specifieke aanvulling op `pipeline/protocols/GEO_LOCATION_PROTOCOL.md` en `DECISION-0013`. Voor definitieve precisie blijft VERIFIED beter; voor de werkkaart is correct gelabeld WORKING voldoende.

## Toegestane GEO-statussen

- `VERIFIED`: kaartpunt rechtstreeks en betrouwbaar bevestigd als bedoelde fysieke locatie of logische bezoekersingang.
- `WORKING`: redelijk kaartpunt voor de bedoelde locatie, geschikt voor globale route- en kaartanalyse, maar exacte ingang of grens niet definitief bevestigd.
- `CONFLICTED`: twee of meer materieel verschillende fysieke identiteiten of punten zijn nog niet opgelost.
- `NOT_ESTABLISHED`: geen redelijk punt of adres gevonden; alleen toegestaan na aantoonbare zoekcontrole.

## Toegestane POINT_TYPE

- `VISITOR_ENTRANCE`;
- `EXACT_SITE`;
- `BUILDING_CENTRE`;
- `COMPLEX_CENTRE`;
- `SITE_CENTRE`;
- `STATION_POINT`;
- `CITY_TRANSPORT_NODE`;
- `ROUTE_REPRESENTATIVE_POINT`;
- `LANDSCAPE_REPRESENTATIVE_POINT`;
- `ADDRESS_CENTROID`;
- `ESTIMATED`.

## Toegestane kaartbasis

- Google Maps;
- OpenStreetMap;
- officiële instelling of overheid met kaart/adres;
- spoorweg- of stationsbron;
- straatadres dat via een tweede kaartbron naar hetzelfde terrein leidt;
- herkenbaar gebouw-, terrein- of landschapsmiddelpunt.

## Nauwkeurigheidsklassen

- `0_25_M`: exacte ingang of duidelijk fysiek object;
- `25_50_M`: gebouw of kleine site;
- `50_150_M`: terrein of complex;
- `150_500_M`: representatief centrum van groot terrein, route- of landschapsobject;
- `OVER_500_M`: alleen met expliciete motivatie; standaard niet kaartklaar.

## Verplichte velden per punt

- `location_id`;
- `candidate_id` of route/station-ID;
- `canonical_name`;
- `cluster`;
- `formal_status` of research label;
- `latitude_wgs84`;
- `longitude_wgs84`;
- `geo_status`;
- `point_type`;
- `estimated_accuracy`;
- `map_source` en URL;
- `point_choice_reason`;
- `checked_at`;
- `recheck_before` waar tijdsgevoelig.

## Harde controles

Een punt faalt wanneer het verwijst naar:

- een gelijknamige andere stad of plaats;
- een hotel, winkel, kantoor of reisbureau met dezelfde naam;
- een administratief centrum in plaats van de spirituele plek;
- een verkeerd station;
- een willekeurig stadscentrum terwijl een herkenbaar site- of adrespunt beschikbaar is.

Een WORKING-punt mag circa 50–500 meter afwijken wanneer het object daardoor nog ondubbelzinnig herkenbaar blijft. Coördinaten worden niet leeg gelaten wanneer een redelijk punt of adres beschikbaar is.

## Reistijden

Globale corridor-, auto-, trein- en aansluitingslogica mag op WORKING-punten worden gebaseerd. Vermeld altijd bron/methode, datum, vervoer en onzekerheidsklasse. Geen schijnprecisie: gebruik tijdsklassen of bandbreedtes wanneer verkeer, dienstregeling of exacte ingang onzeker is.

## KML

- Iedere marker toont `WORKING` of `VERIFIED` zichtbaar.
- `CONFLICTED` en `NOT_ESTABLISHED` komen niet als betrouwbaar punt in KML maar blijven in de bron- en auditbestanden.
- KML-kleur toont status A/B/C-laag; GEO-status blijft een afzonderlijk veld.
- Geen formele status afleiden uit marker- of laagkleur.

END_OF_ARTIFACT