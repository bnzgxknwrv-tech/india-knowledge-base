---
id: DECISION-0013
subject: "Permanente LOCATION_ID's en geverifieerde GEO-data"
decided_by: "Mark"
decided_at: "2026-07-15"
outcome: "Iedere locatie krijgt een permanente reisgerichte LOCATION_ID en GOUD levert geverifieerde WGS84-kaartdata en daarop gebaseerde verbindingen"
applies_to: "Alle India-clusters, GOUD-datasets, KML/My Maps, rapporten, kaarten en reisdocumenten"
---

# DECISION 0013: LOCATION_ID en GEO-data

## 1. Twee permanente sleutels

`IND-PLACE-*` blijft de interne wereldwijd unieke database-ID. Daarnaast krijgt iedere opgenomen fysieke locatie één permanente reisgerichte `LOCATION_ID` voor rapporten, kaarten, KML en reisdocumenten.

## 2. Clusterblokken

Ieder reiscluster krijgt één niet-overlappend blok van 100 nummers. De blokken volgen de uiteindelijke reisvolgorde.

- `100-199`: Delhi/aankomst;
- `200-299`: Braj — Vrindavan, Mathura, Govardhan, Gokul/Mahavan, Barsana en Nandgaon;
- volgende clusters krijgen achtereenvolgens `300-399`, `400-499` enzovoort;
- binnen een blok zijn gaten toegestaan;
- nummers worden nooit hergebruikt, gewijzigd of naar een ander cluster verplaatst;
- later gevonden locaties krijgen een vrij nummer in het bestaande clusterblok.

`LOCATION_ID` wordt als decimale tekenreeks opgeslagen met minimaal drie cijfers, bijvoorbeeld `200`, `207`, `1000`.

## 3. Verplichte GEO-velden

GOUD levert per kandidaat:

- `LOCATION_ID`;
- `LATITUDE_WGS84`;
- `LONGITUDE_WGS84`;
- `GEO_POINT_TYPE`: `VISITOR_ENTRANCE`, `EXACT_SITE`, `COMPLEX_CENTRE` of `ESTIMATED`;
- `GEO_VERIFICATION_STATUS`;
- `GEO_SOURCES`;
- `GOOGLE_MAPS_URL`;
- motivatie wanneer meerdere kaartpunten mogelijk zijn.

Bij een bezoekbaar complex heeft de logische bezoekersingang voorkeur. GOUD controleert dat het punt niet naar een gelijknamige plaats, administratief centrum, willekeurig complexmiddelpunt, verkeerde ingang, hotel, winkel of kantoor verwijst.

Waar mogelijk worden twee onafhankelijke bronnen gebruikt. Onvoldoende verificatie blijft zichtbaar; er wordt geen willekeurig punt ingevuld.

## 4. Verbindingen

Iedere vermelde verbinding bevat vertrek-LOCATION_ID, aankomst-LOCATION_ID, vervoerswijze, geschatte tijd, bron of berekeningsmethode en controledatum wanneer tijdsgevoelig. Reistijden en looptijden worden gebaseerd op de vastgelegde geverifieerde GEO-punten.

## 5. C-locaties

C-locaties blijven volledig in kandidatenregister, GEO-dataset, rapport en kaartdata staan. C betekent voor de huidige reis niet bezoeken, niet verwijderen of vergeten.

## 6. Rollen

GOUD maakt geen kaart en kent geen formele of adviserende A/B/C toe. GOUD levert een betrouwbare `geo_locations.jsonl` en `geo_connections.jsonl`. INDIA2 kan daarna zonder nieuw locatieonderzoek KML, kaartlagen en compacte beslisproducten maken.

END_OF_ARTIFACT