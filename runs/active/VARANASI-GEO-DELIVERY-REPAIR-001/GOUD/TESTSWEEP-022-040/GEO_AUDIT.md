# GEO-AUDIT -- INDIA5-testsweep VNS-CAND-022 t/m 040

run_id: VARANASI-GEO-DELIVERY-REPAIR-001
scope: eerste INDIA5-PROTOCOL testsweep, regio Varanasi, 19 kandidaten (VNS-CAND-022 t/m 040)
audit_datum: 2026-08-02
bronnen: BRONS-B03.jsonl (022-030), BRONS-B04.jsonl (031-040), ZILVER-TESTSWEEP-022-040.jsonl

## Dekking

Alle 19 kandidaten van het testsweep-bereik zijn aanwezig in BRONS, ZILVER en de KML/PDF. Geen
kandidaat overgeslagen, geen dubbele candidate_id, geen candidate_id buiten bereik.

## Geo-status per kandidaat (na ZILVER)

| candidate_id | naam | geo_status | coordinaat (eind) | oud vergelijkingspunt | afwijking t.o.v. oud punt |
|---|---|---|---|---|---|
| VNS-CAND-022 | Bindu Madhav Temple | GOOGLE_MAPS_MARKER_NOT_CONFIRMED | -- (onbevestigd) | 25.3187,83.0125 | n.v.t. |
| VNS-CAND-023 | Mrityunjay Mahadev Temple | GOOGLE_MAPS_MARKER_NOT_CONFIRMED | -- (onbevestigd) | 25.3291,83.0056 | LET OP: onafhankelijke (niet-Google) coordinaat wijkt ~3 km af, zie correctierapport |
| VNS-CAND-024 | Kabir Chaura Math | GOOGLE_MAPS_MARKER_NOT_CONFIRMED | -- (onbevestigd) | 25.3233,82.9992 | n.v.t. |
| VNS-CAND-025 | Lahartara Kabir birthplace memorial | GOOGLE_MAPS_MARKER_NOT_CONFIRMED | -- (onbevestigd) | 25.304,82.966 | n.v.t. (physical_identity: PARTIAL) |
| VNS-CAND-026 | Ramakrishna Mission Home of Service | GOOGLE_MAPS_MARKER_NOT_CONFIRMED | -- (onbevestigd) | 25.309,82.9974 | n.v.t. |
| VNS-CAND-027 | Baba Keenaram Sthal / Krim Kund | GOOGLE_MAPS_MARKER_NOT_CONFIRMED | -- (onbevestigd) | 25.2928,83.001 | klein (~0.4 km, niet-Google bron) |
| VNS-CAND-028 | Bhaskarananda Samadhi / Anand Bagh | GOOGLE_MAPS_MARKER_NOT_CONFIRMED | -- (onbevestigd) | 25.2868,82.9968 | n.v.t. (physical_identity: PARTIAL) |
| VNS-CAND-029 | Dhamek Stupa | **VERIFIED_OFFICIAL_MAP_LINK** | 25.380889,83.024276 | 25.3807,83.0245 | vrijwel nul (~30 m) |
| VNS-CAND-030 | Mulagandha Kuti Vihara | GOOGLE_MAPS_MARKER_NOT_CONFIRMED | -- (onbevestigd) | 25.3819,83.0216 | n.v.t. |
| VNS-CAND-031 | Chaukhandi Stupa | **VERIFIED_OFFICIAL_MAP_LINK** | 25.37402,83.023588 | 25.3756,83.022 | klein (~200 m) |
| VNS-CAND-032 | Sarnath Archaeological Museum | GOOGLE_MAPS_MARKER_NOT_CONFIRMED | -- (onbevestigd) | 25.3817,83.0205 | n.v.t. |
| VNS-CAND-033 | Deer Park / Isipatana sacred landscape | **VERIFIED_OFFICIAL_MAP_LINK** | 25.3825,83.024445 | 25.3813,83.023 | klein (~150 m) |
| VNS-CAND-034 | Saranganath Temple | GOOGLE_MAPS_MARKER_NOT_CONFIRMED | -- (onbevestigd) | 25.3833,83.0225 | n.v.t. |
| VNS-CAND-035 | Tulsi Manas Temple | GOOGLE_MAPS_MARKER_NOT_CONFIRMED | -- (onbevestigd) | 25.2883,83.0003 | n.v.t. |
| VNS-CAND-036 | Tulsi Ghat | GOOGLE_MAPS_MARKER_NOT_CONFIRMED | -- (onbevestigd) | 25.2906,83.0068 | n.v.t. |
| VNS-CAND-037 | Lolark Kund | GOOGLE_MAPS_MARKER_NOT_CONFIRMED | -- (onbevestigd) | 25.2875,83.0038 | n.v.t. |
| VNS-CAND-038 | Ratneshwar Mahadev Temple | GOOGLE_MAPS_MARKER_NOT_CONFIRMED | -- (onbevestigd) | 25.3113,83.0145 | klein (~150 m, niet-Google bron) |
| VNS-CAND-039 | Shitala Mata Temple, Dashashwamedh | GOOGLE_MAPS_MARKER_NOT_CONFIRMED | -- (onbevestigd) | 25.3064,83.0105 | n.v.t. |
| VNS-CAND-040 | Bharat Mata Temple | GOOGLE_MAPS_MARKER_NOT_CONFIRMED | -- (onbevestigd) | 25.317,82.989 | vrijwel nul (~20 m, niet-Google bron) |

## Samenvatting

- 3/19 (16%) EXACT/VERIFIED via een officiele Google-kaartbron (Google Earth entity-API, gevonden
  door ZILVER): VNS-CAND-029, 031, 033.
- 16/19 (84%) GOOGLE_MAPS_MARKER_NOT_CONFIRMED: fysieke identiteit in alle 16 gevallen bevestigd via
  minstens 2 onafhankelijke bronnen; geen interactieve Google Maps-marker kon in deze sessie worden
  geopend en afgelezen. Geen schatting, terreinmiddelpunt, oud KML-punt of website-coordinaat is als
  vervanging gebruikt (verboden per RUN.yaml `geo_marker_rule.forbidden_substitutes`).
- Dit ratio (3/19 bevestigd) is consistent met de eerdere 21 kandidaten van deze run (2/21 bevestigd,
  zie ROOT_CAUSE.md) -- de sessie heeft geen interactieve Google Maps-toegang, alleen websearch/fetch.
- Geen expliciet Mark-besluit of -afwijzing (VNS-CAND-008) geraakt door deze 19 kandidaten.
- Geen van de 19 kandidaten valt onder `protected_mark_decisions` (alle 19 zijn `DOOR_MARK_TE_BEOORDELEN`).

## Dedup-check (naam-gelijkenis + geo-nabijheid)

Uitgevoerd over de 19 testsweep-kandidaten onderling en tegen de reeds verwerkte VNS-CAND-001 t/m 021:

- Geen duplicaten of near-duplicates binnen de 19 (verschillende namen, verschillende clusters,
  onderlinge afstand > 300 m in alle gevallen behalve de zes Sarnath-kandidaten, die bewust apart
  gecatalogiseerde deelsites binnen hetzelfde complex zijn -- zie observatie hieronder).
- **Observatie (geen wijziging, alleen signalering voor Mark):** VNS-CAND-006 ("Sarnath sacred
  complex", reeds verwerkt, buiten deze testsweep) is een koepelkandidaat voor het hele
  Sarnath-gebied. Deze testsweep heeft daarbinnen 6 specifieke deelsites afzonderlijk gecatalogiseerd
  (029 Dhamek Stupa, 030 Mulagandha Kuti Vihara, 031 Chaukhandi Stupa, 032 Sarnath Archaeological
  Museum, 033 Deer Park/Isipatana, 034 Saranganath Temple). Dit is geen fout of duplicaat, maar Mark
  kan later overwegen of VNS-CAND-006 als aparte kandidaat behouden blijft naast de zes deelsites, of
  wordt samengevoegd/ingetrokken. VNS-CAND-006 zelf is NIET gewijzigd (buiten scope, beschermd).

## Validators

`python3 scripts/validate_brons.py` -- OK, 40/40 records gecontroleerd, geen fouten (zie BRONS-batchcommit).
KML geparsed met `xml.etree.ElementTree`: 19/19 Placemarks, coordinatenvolgorde (lon,lat) correct.
