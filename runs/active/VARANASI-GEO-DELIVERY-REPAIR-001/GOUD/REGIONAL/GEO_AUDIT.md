# GEO-AUDIT -- volledig regionaal Varanasi-pakket (40 kandidaten)

run_id: VARANASI-GEO-DELIVERY-REPAIR-001
scope: alle 40 Varanasi-kandidaten (VNS-CAND-001 t/m 040)
audit_datum: 2026-08-02
bronnen: BRONS-B01 t/m B04, ZILVER-Z01 (001-021), ZILVER-TESTSWEEP-022-040 (022-040)

## Dekking

Alle 40 kandidaten zijn aanwezig in de gevalideerde dataset (`DATASET_VARANASI_40.jsonl`), de KML en
de PDF. Geen kandidaat ontbreekt, geen dubbele candidate_id.

Tijdens het samenvoegen is een dekkingsgat ontdekt: VNS-CAND-021 had een BRONS-record maar viel
buiten zowel ZILVER-Z01 (001-020) als de INDIA5-testsweep (022-040). Dit is gedicht door VNS-CAND-021
alsnog via ZILVER te laten lopen (zie CORRECTIERAPPORT.md); het BRONS-record zelf is niet gewijzigd.

## Status- en coordinatenoverzicht (alle 40)

| candidate_id | naam | status | geo_status | eindcoordinaat | oud vergelijkingspunt |
|---|---|---|---|---|---|
| VNS-CAND-001 | Lahiri Mahasaya Samadhi / Satyalok | PROVISIONAL | GOOGLE_MAPS_MARKER_NOT_CONFIRMED | -- (geen) | 25.3028,83.0074 (WORKING_GOOGLE_MAPS_PIN) |
| VNS-CAND-002 | Lahiri Mahasaya original home | PROVISIONAL | GOOGLE_MAPS_MARKER_NOT_CONFIRMED | -- (geen) | 25.3018,83.0068 (WORKING_GOOGLE_MAPS_PIN) |
| VNS-CAND-003 | Manikarnika Ghat | PROVISIONAL | GOOGLE_MAPS_MARKER_NOT_CONFIRMED | -- (geen) | 25.3109,83.0142 (WORKING_GOOGLE_MAPS_PIN) |
| VNS-CAND-004 | Shri Tailanga Swami Math | PROVISIONAL | GOOGLE_MAPS_MARKER_NOT_CONFIRMED | -- (geen) | 25.3188,83.013 (WORKING_GOOGLE_MAPS_PIN) |
| VNS-CAND-005 | Shree Shree Ma Anandamayi Ashram, Bhadaini | PROVISIONAL | GOOGLE_MAPS_MARKER_NOT_CONFIRMED | -- (geen) | 25.2897,83.0068 (WORKING_GOOGLE_MAPS_PIN) |
| VNS-CAND-006 | Sarnath sacred complex | PROVISIONAL | GOOGLE_MAPS_MARKER_NOT_CONFIRMED | -- (geen) | 25.3811,83.0214 (WORKING_GOOGLE_MAPS_PIN) |
| VNS-CAND-007 | Shri Kashi Vishwanath Temple | PROVISIONAL | GOOGLE_MAPS_MARKER_NOT_CONFIRMED | -- (geen) | 25.3109,83.0107 (WORKING_GOOGLE_MAPS_PIN) |
| VNS-CAND-008 | Yogoda Satsanga Dhyana Mandali, Varanasi | PROVISIONAL | GOOGLE_MAPS_MARKER_NOT_CONFIRMED | -- (geen) | ~~25.3045,82.979369~~ AFGEWEZEN, niet gebruikt |
| VNS-CAND-009 | Dashashwamedh Ghat | PROVISIONAL | GOOGLE_MAPS_MARKER_NOT_CONFIRMED | -- (geen) | 25.3062,83.0104 (WORKING_GOOGLE_MAPS_PIN) |
| VNS-CAND-010 | Assi Ghat | PROVISIONAL | GOOGLE_MAPS_MARKER_NOT_CONFIRMED | -- (geen) | 25.2887,83.0061 (WORKING_GOOGLE_MAPS_PIN) |
| VNS-CAND-011 | Panchganga Ghat | PROVISIONAL | GOOGLE_MAPS_MARKER_NOT_CONFIRMED | -- (geen) | 25.3185,83.0128 (WORKING_GOOGLE_MAPS_PIN) |
| VNS-CAND-012 | Harishchandra Ghat | PROVISIONAL | GOOGLE_MAPS_MARKER_NOT_CONFIRMED | -- (geen) | 25.2994,83.009 (WORKING_GOOGLE_MAPS_PIN) |
| VNS-CAND-013 | Kaal Bhairav Temple | PROVISIONAL | GOOGLE_MAPS_MARKER_NOT_CONFIRMED | -- (geen) | 25.3223,83.009 (WORKING_GOOGLE_MAPS_PIN) |
| VNS-CAND-014 | Maa Annapurna Temple | PROVISIONAL | GOOGLE_MAPS_MARKER_NOT_CONFIRMED | -- (geen) | 25.3107,83.0103 (WORKING_GOOGLE_MAPS_PIN) |
| VNS-CAND-015 | Sankat Mochan Hanuman Temple | PROVISIONAL | GOOGLE_MAPS_MARKER_NOT_CONFIRMED | -- (geen) | 25.282,82.9992 (WORKING_GOOGLE_MAPS_PIN) |
| VNS-CAND-016 | Durga Temple and Durga Kund | PROVISIONAL | GOOGLE_MAPS_MARKER_NOT_CONFIRMED | -- (geen) | 25.288,82.9998 (WORKING_GOOGLE_MAPS_PIN) |
| VNS-CAND-017 | Vishalakshi Gauri Temple | PROVISIONAL | GOOGLE_MAPS_MARKER_NOT_CONFIRMED | -- (geen) | 25.3102,83.0119 (WORKING_GOOGLE_MAPS_PIN) |
| VNS-CAND-018 | Sankatha Devi Temple | CONFIRMED | EXACT_GOOGLE_MAPS_MARKER | 25.3126289,83.0154469 | 25.3156,83.014 (WORKING_GOOGLE_MAPS_PIN) |
| VNS-CAND-019 | Kedareshwar Temple and Kedar Ghat | CONFIRMED | EXACT_GOOGLE_MAPS_MARKER | 25.2995855,83.0060964 | 25.2967,83.0088 (WORKING_GOOGLE_MAPS_PIN) |
| VNS-CAND-020 | Lalita Ghat | PROVISIONAL | GOOGLE_MAPS_MARKER_NOT_CONFIRMED | -- (geen) | 25.3114,83.0131 (WORKING_GOOGLE_MAPS_PIN) |
| VNS-CAND-021 | Nepali Temple / Kathwala Temple | PROVISIONAL | GOOGLE_MAPS_MARKER_NOT_CONFIRMED | -- (geen) | 25.312,83.0132 (WORKING_GOOGLE_MAPS_PIN) |
| VNS-CAND-022 | Bindu Madhav Temple | PROVISIONAL | GOOGLE_MAPS_MARKER_NOT_CONFIRMED | -- (geen) | 25.3187,83.0125 (WORKING_GOOGLE_MAPS_PIN) |
| VNS-CAND-023 | Mrityunjay Mahadev Temple | PROVISIONAL | GOOGLE_MAPS_MARKER_NOT_CONFIRMED | -- (geen) | 25.3291,83.0056 (WORKING_GOOGLE_MAPS_PIN) |
| VNS-CAND-024 | Kabir Chaura Math | PROVISIONAL | GOOGLE_MAPS_MARKER_NOT_CONFIRMED | -- (geen) | 25.3233,82.9992 (WORKING_GOOGLE_MAPS_PIN) |
| VNS-CAND-025 | Lahartara Kabir birthplace memorial | PROVISIONAL | GOOGLE_MAPS_MARKER_NOT_CONFIRMED | -- (geen) | 25.304,82.966 (APPROXIMATE_LOCAL_POINT) |
| VNS-CAND-026 | Ramakrishna Mission Home of Service | PROVISIONAL | GOOGLE_MAPS_MARKER_NOT_CONFIRMED | -- (geen) | 25.309,82.9974 (WORKING_GOOGLE_MAPS_PIN) |
| VNS-CAND-027 | Baba Keenaram Sthal / Krim Kund | PROVISIONAL | GOOGLE_MAPS_MARKER_NOT_CONFIRMED | -- (geen) | 25.2928,83.001 (WORKING_GOOGLE_MAPS_PIN) |
| VNS-CAND-028 | Bhaskarananda Samadhi / Anand Bagh | PROVISIONAL | GOOGLE_MAPS_MARKER_NOT_CONFIRMED | -- (geen) | 25.2868,82.9968 (APPROXIMATE_LOCAL_POINT) |
| VNS-CAND-029 | Dhamek Stupa | CONFIRMED | VERIFIED_OFFICIAL_MAP_LINK | 25.380889,83.024276 | 25.3807,83.0245 (WORKING_GOOGLE_MAPS_PIN) |
| VNS-CAND-030 | Mulagandha Kuti Vihara | PROVISIONAL | GOOGLE_MAPS_MARKER_NOT_CONFIRMED | -- (geen) | 25.3819,83.0216 (WORKING_GOOGLE_MAPS_PIN) |
| VNS-CAND-031 | Chaukhandi Stupa | CONFIRMED | VERIFIED_OFFICIAL_MAP_LINK | 25.37402,83.023588 | 25.3756,83.022 (WORKING_GOOGLE_MAPS_PIN) |
| VNS-CAND-032 | Sarnath Archaeological Museum | PROVISIONAL | GOOGLE_MAPS_MARKER_NOT_CONFIRMED | -- (geen) | 25.3817,83.0205 (WORKING_GOOGLE_MAPS_PIN) |
| VNS-CAND-033 | Deer Park / Isipatana sacred landscape | CONFIRMED | VERIFIED_OFFICIAL_MAP_LINK | 25.3825,83.024445 | 25.3813,83.023 (WORKING_GOOGLE_MAPS_PIN) |
| VNS-CAND-034 | Saranganath Temple | PROVISIONAL | GOOGLE_MAPS_MARKER_NOT_CONFIRMED | -- (geen) | 25.3833,83.0225 (WORKING_GOOGLE_MAPS_PIN) |
| VNS-CAND-035 | Tulsi Manas Temple | PROVISIONAL | GOOGLE_MAPS_MARKER_NOT_CONFIRMED | -- (geen) | 25.2883,83.0003 (WORKING_GOOGLE_MAPS_PIN) |
| VNS-CAND-036 | Tulsi Ghat | PROVISIONAL | GOOGLE_MAPS_MARKER_NOT_CONFIRMED | -- (geen) | 25.2906,83.0068 (WORKING_GOOGLE_MAPS_PIN) |
| VNS-CAND-037 | Lolark Kund | PROVISIONAL | GOOGLE_MAPS_MARKER_NOT_CONFIRMED | -- (geen) | 25.2875,83.0038 (WORKING_GOOGLE_MAPS_PIN) |
| VNS-CAND-038 | Ratneshwar Mahadev Temple | PROVISIONAL | GOOGLE_MAPS_MARKER_NOT_CONFIRMED | -- (geen) | 25.3113,83.0145 (WORKING_GOOGLE_MAPS_PIN) |
| VNS-CAND-039 | Shitala Mata Temple, Dashashwamedh | PROVISIONAL | GOOGLE_MAPS_MARKER_NOT_CONFIRMED | -- (geen) | 25.3064,83.0105 (WORKING_GOOGLE_MAPS_PIN) |
| VNS-CAND-040 | Bharat Mata Temple | PROVISIONAL | GOOGLE_MAPS_MARKER_NOT_CONFIRMED | -- (geen) | 25.317,82.989 (WORKING_GOOGLE_MAPS_PIN) |

## Statusverdeling

- CONFIRMED: 5 (VNS-CAND-018, 019, 029, 031, 033)
- PROVISIONAL: 35
- AMBIGUOUS: 0
- REJECTED: 0

## Mark-keuze-verdeling -- COMPLEET (alle 40 besloten)

Afgerond 2026-08-02: eerste ronde in `MARK_DECISIONS_2026-08-02.jsonl` (commit 58be47b), laatste
negen kandidaten (012, 019, 029-034, 040) besloten in dezelfde CCI-sessie. Geen kandidaat is nog
DOOR_MARK_TE_BEOORDELEN. Zie `NUMBERING_REGISTRY.jsonl` voor het permanente nummer per kandidaat.

- A: 32 (001, 002, 003, 004, 005, 006, 007, 009, 010, 011, 014, 015, 016, 017, 018, 019, 020, 021,
  022, 024, 028, 029, 030, 031, 032, 033, 034, 035, 036, 037, 038, 039)
- B: 5 (008, 012, 013, 023, 025)
- C: 3 (026, 027, 040)
- DOOR_MARK_TE_BEOORDELEN: 0

**006 = A en 029-034 = A**: dit zijn twee aparte, expliciete Mark-besluiten (niet automatisch uit
elkaar afgeleid). Zie CORRECTIERAPPORT.md voor de eerder gevonden tegenstrijdigheid over de
Sarnath-deelsites en hoe die door Mark expliciet is bevestigd/opgelost.

## Kritieke bevinding: VNS-CAND-008 heeft geen enkel veilig kaartpunt

Het enige bekende vergelijkingscoordinaat voor VNS-CAND-008 (Yogoda Satsanga Dhyana Mandali) is het
coordinaat dat Mark expliciet heeft afgewezen (`25.3045, 82.979369`, regel
`MUST_NOT_BE_REUSED_AS_FINAL_POINT` in RUN.yaml). Er is geen vervangend coordinaat gevonden. Daarom
heeft deze kandidaat in de KML bewust GEEN geometrie (geen `<Point>`) -- alleen een tekstuele
vermelding met adres en toelichting. Dit voorkomt dat het afgewezen punt ooit stilzwijgend op de kaart
verschijnt. Zie CORRECTIERAPPORT.md en het open-vraag-veld in de PDF.

## Verworpen bevindingen (Google Earth entity-links die NIET zijn overgenomen)

Tijdens ZILVER-Z01 werden voor VNS-CAND-003 (Manikarnika Ghat) en VNS-CAND-009 (Dashashwamedh Ghat)
Google Earth entity-API-links gevonden met IDENTIEKE coordinaten (25.303617, 83.014099) ondanks dat
het twee verschillende, ~500-800 m uit elkaar liggende ghats zijn. Dit wijst op een generieke
rivieroever-fallback van de API bij het zoekwoord "Ghat", niet op een specifieke plaatsmarker. Beide
zijn expliciet VERWORPEN en niet gebruikt als eindcoordinaat -- beide kandidaten blijven PROVISIONAL
met het oude vergelijkingspunt, duidelijk gemarkeerd als onbevestigd.

## Bevestigde kandidaten (5) -- herkomst

| candidate_id | herkomst |
|---|---|
| VNS-CAND-018 | Publieke Google Maps place-URL met ingesloten marker-coordinaat (bevestigd voor de eerdere testsweep-run, ongewijzigd) |
| VNS-CAND-019 | Idem |
| VNS-CAND-029 | Google Earth entity-API-link (google.com/earth/rpc/entity), specifiek zoekwoord "Dhamekh", coordinaat vrijwel identiek aan oud vergelijkingspunt |
| VNS-CAND-031 | Google Earth entity-API-link, zoekwoord "Chaukhandi" |
| VNS-CAND-033 | Google Earth entity-API-link, zoekwoord "deer" (Sarnath Deer Park) |

## Dedup-check (naam-gelijkenis + geo-nabijheid), regionaal

Uitgevoerd over alle 40 kandidaten. Geen exacte duplicaten of naamcollisies gevonden. Eén
begripsmatige overlap gesignaleerd (geen wijziging, concrete vraag aan Mark, zie
CORRECTIERAPPORT.md en BESLISOVERZICHT.md):

- VNS-CAND-006 ("Sarnath sacred complex", koepelkandidaat) vs. VNS-CAND-029/030/031/032/033/034
  (specifieke Sarnath-deelsites, uit de testsweep).

## Validators

- `python3 scripts/validate_brons.py` -- OK, 40/40 BRONS-records, geen fouten.
- KML geparsed met `xml.etree.ElementTree`: 40/40 Placemarks (39 met geometrie, VNS-CAND-008 bewust
  zonder geometrie), geen duplicaten, geen ontbrekende kandidaten, het afgewezen coordinaat
  [25.3045, 82.979369] komt in GEEN enkele `<Point>` voor.
- PDF teruggelezen met `pypdf`: 11 pagina's, alle 40 candidate_id's aanwezig.
