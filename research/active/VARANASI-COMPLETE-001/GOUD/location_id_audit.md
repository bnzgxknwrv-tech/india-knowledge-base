# LOCATION_ID-audit — VARANASI-COMPLETE-001

## Autoriteitsregel

`knowledge/places/NUMBERING_POLICY.md` bepaalt dat uitsluitend SUBREGIE INDIA nieuwe permanente `IND-PLACE-*`-IDs reserveert en uitgeeft. GOUD heeft daarom geen nieuw permanent place-ID of LOCATION_ID toegewezen.

## Varanasi-kandidaten

- kandidaten: 40;
- unieke `candidate_id`: 40/40;
- permanente `place_id` toegewezen door GOUD: 0;
- permanente `location_id` toegewezen door GOUD: 0;
- `geo_locations.jsonl` bevat voor ieder record de velden `location_id` en `place_id` met waarde `null`;
- iedere kandidaat blijft via zijn unieke `VNS-CAND-*`-ID en coördinaten traceerbaar totdat SUBREGIE INDIA een nummerblok reserveert.

## Repositorybrede A/B-masterkaart

- masterrecords: 30;
- unieke `registry_record_id`: 30;
- bestaande niet-lege LOCATION_IDs: 17;
- dubbele niet-lege LOCATION_IDs: 0;
- ontbrekende coördinaten: 0;
- bestaande Kumaon-LOCATION_IDs: exact behouden;
- records zonder LOCATION_ID: niet door GOUD aangevuld.

Bestaande LOCATION_IDs in de masterkaart:
`400, 401, 402, 403, 404, 405, 406, 407, 408, 409, 412, 413, 414, 420, 421, 423, 424`.

Alle 17 IDs zijn uniek en vallen binnen het reeds uitgegeven Kumaon-blok. Geen nummer is hergebruikt, gewijzigd of cross-block toegewezen.

## Canonieke registry

- bestaande place-IDs vóór en na integratie: `IND-PLACE-000001` t/m `IND-PLACE-000008`;
- nieuw place-ID: 0;
- gewijzigd place-ID: 0;
- twee bestaande records kregen uitsluitend WORKING_GEO en provenance;
- formele statussen en status-decision-ID bleven ongewijzigd.

## Uitkomst

`PASS` voor nummeringsintegriteit. Canonieke registratie van de overige Varanasi- en masterkaartrecords blijft een latere taak voor SUBREGIE INDIA.

END_OF_ARTIFACT