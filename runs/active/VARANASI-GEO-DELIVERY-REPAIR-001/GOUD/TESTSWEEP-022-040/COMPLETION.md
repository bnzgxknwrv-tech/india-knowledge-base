run_id: VARANASI-GEO-DELIVERY-REPAIR-001
role: GOUD
scope: INDIA5-PROTOCOL eerste testsweep, VNS-CAND-022 t/m VNS-CAND-040 (19 kandidaten)
status: KLAAR

## Eindproducten

- `GOUD/TESTSWEEP-022-040/USER/VARANASI_TESTSWEEP_022-040.kml` -- 19 placemarks, 3 bevestigd (groen),
  16 onbevestigd (geel, oud vergelijkingspunt zichtbaar gemarkeerd als niet-definitief).
- `GOUD/TESTSWEEP-022-040/USER/VARANASI_TESTSWEEP_022-040_KEUZE.pdf` -- 6 pagina's, alle 19 kandidaten,
  beschermde besluiten en openstaande vragen voor Mark.
- `GOUD/TESTSWEEP-022-040/GEO_AUDIT.md` -- volledige geo-audit per kandidaat + dedup-check.
- `GOUD/TESTSWEEP-022-040/CORRECTIERAPPORT.md` -- scope-afwijking, ZILVER-correcties, onzekerheden.
- `GOUD/TESTSWEEP-022-040/COMPLETION.md` -- dit bestand.

## Bestandscontroles

- KML geparsed met `xml.etree.ElementTree`: geldig XML, 19/19 Placemarks, coordinatenvolgorde
  (lon,lat) correct, alle 19 candidate_id's exact eenmaal aanwezig.
- PDF teruggelezen met `pypdf`: 6 pagina's, alle 19 candidate_id's aangetroffen in de geextraheerde
  tekst, inhoud leesbaar en overeenkomstig de brondata.
- `python3 scripts/validate_brons.py`: OK, 40/40 BRONS-records gecontroleerd (alle 40 Varanasi-
  kandidaten, inclusief de 19 nieuwe), geen fouten.
- `python3 scripts/next_candidate.py`: bevestigt 0 resterende kandidaten in het volledige
  candidates.jsonl-bereik (40/40 BRONS-verwerkt).

## Zekere locaties (3)

VNS-CAND-029 Dhamek Stupa, VNS-CAND-031 Chaukhandi Stupa, VNS-CAND-033 Deer Park/Isipatana --
VERIFIED_OFFICIAL_MAP_LINK via een officiele Google Earth entity-API-link met ingesloten coordinaat
en feature-ID.

## Onzekere locaties (16)

VNS-CAND-022, 023, 024, 025, 026, 027, 028, 030, 032, 034, 035, 036, 037, 038, 039, 040 --
GOOGLE_MAPS_MARKER_NOT_CONFIRMED. Fysieke identiteit in alle gevallen bevestigd via minstens twee
onafhankelijke bronnen; geen interactieve Google Maps-marker beschikbaar in deze sessie. Zie
CORRECTIERAPPORT.md voor bijzondere aandachtspunten (met name VNS-CAND-023).

## Beschermde Mark-keuzes

VNS-CAND-001, 002, 003, 007 (keuze A) en VNS-CAND-008 (keuze B, met expliciet afgewezen coordinaat
[25.3045, 82.979369]) zijn niet aangeraakt en niet gewijzigd. Deze testsweep heeft geen A/B/C-keuze
toegekend aan VNS-CAND-022 t/m 040 -- dat blijft aan Mark.

## Door Mark te beoordelen

- A/B/C-keuze voor alle 19 testsweep-kandidaten (geen enkele heeft nu een Mark-besluit).
- VNS-CAND-023: 3 km-afwijking tussen een onafhankelijke coordinaat en het oude vergelijkingspunt.
- Mogelijke relatie tussen VNS-CAND-006 ("Sarnath sacred complex", buiten scope) en de zes nieuwe
  Sarnath-deelsites (029-034).
- De 16 GOOGLE_MAPS_MARKER_NOT_CONFIRMED-kandidaten: baat bij een toekomstige sessie met interactieve
  Google Maps-toegang om alsnog een exacte marker vast te stellen.

## Niet uitgevoerd of verboden

- Geen centrale India-master-KML bijgewerkt (verboden, RUN.yaml `forbidden_outputs`).
- Geen ZILVER-Z01 (VNS-CAND-001 t/m 020) uitgevoerd -- buiten deze testsweep-scope.
- Geen volledig regionaal GOUD-eindpakket voor alle 40 kandidaten gemaakt -- buiten deze
  testsweep-scope (alleen de 19 nieuwe testkandidaten zijn geintegreerd).
- Geen bestaand geldig kandidaatrecord (VNS-CAND-001 t/m 021) gewijzigd.
- Geen schatting, terreinmiddelpunt, oud KML-punt of website-coordinaat gebruikt als vervangend
  eindpunt voor een onbevestigde kandidaat.

## Readback

KML: geparsed en gecontroleerd (zie hierboven). PDF: geopend en teruggelezen met pypdf (zie
hierboven). Beide bestandscontroles zijn uitgevoerd NA creatie, zoals PRACTICAL_DELIVERY.md vereist.
