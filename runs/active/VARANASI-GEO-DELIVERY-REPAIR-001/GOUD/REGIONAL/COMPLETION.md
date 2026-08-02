run_id: VARANASI-GEO-DELIVERY-REPAIR-001
role: GOUD
scope: volledig regionaal Varanasi-pakket, alle 40 kandidaten (VNS-CAND-001 t/m 040)
status: KLAAR

## Eindproducten

- `GOUD/REGIONAL/DATASET_VARANASI_40.jsonl` -- de volledige gevalideerde dataset (40 records).
- `GOUD/REGIONAL/USER/VARANASI_40_KANDIDATEN.kml` -- definitieve Varanasi-KML, alle 40 kandidaten,
  kleurcodering per Mark-keuze (groen=A, oranje=B, wit=DOOR_MARK_TE_BEOORDELEN), vorm per status
  (ster=CONFIRMED, cirkel=PROVISIONAL), aparte lege AMBIGUOUS-laag, geen REJECTED-bestemmingen.
- `GOUD/REGIONAL/USER/VARANASI_40_KEUZE.pdf` -- leesbare NL keuze-PDF, alle 40 kandidaten.
- `GOUD/REGIONAL/GEO_AUDIT.md` -- volledige geo-audit, statusoverzicht, dedup-check.
- `GOUD/REGIONAL/CORRECTIERAPPORT.md` -- tooling-fix, ZILVER-bevindingen, gecorrigeerde KML-bug.
- `GOUD/REGIONAL/BESLISOVERZICHT.md` -- compleet beslisoverzicht voor Mark.
- `GOUD/REGIONAL/COMPLETION.md` -- dit bestand.

## Bestandscontroles

- `validate_brons.py`: OK, 40/40 BRONS-records.
- KML geparsed met `xml.etree.ElementTree`: 40/40 Placemarks, geen duplicaten, geen ontbrekende
  kandidaten, coordinatenvolgorde (lon,lat) correct, het expliciet afgewezen VNS-CAND-008-coordinaat
  komt in GEEN enkele `<Point>` voor (geverifieerd met een geautomatiseerde check).
- PDF teruggelezen met `pypdf`: 11 pagina's, alle 40 candidate_id's aanwezig.
- Dataset gecontroleerd: 40 unieke candidate_id's, statusverdeling 5 CONFIRMED / 35 PROVISIONAL / 0
  AMBIGUOUS / 0 REJECTED, Mark-verdeling 4x A / 1x B / 35x DOOR_MARK_TE_BEOORDELEN.

## Zekere locaties (5)

VNS-CAND-018, 019 (eerder bevestigd), 029, 031, 033 (bevestigd tijdens ZILVER van de testsweep) --
alle vijf via een officiele Google-kaartbron.

## Onzekere locaties (35)

Alle overige kandidaten: PROVISIONAL, fysieke identiteit bevestigd, Google Maps-marker (nog) niet
geverifieerd. Zie GEO_AUDIT.md voor de volledige tabel.

## Beschermde Mark-keuzes

VNS-CAND-001/002/003/007 = A, VNS-CAND-008 = B. Alle vijf ongewijzigd. Het expliciet afgewezen
VNS-CAND-008-coordinaat [25.3045, 82.979369] is nergens gebruikt.

## Door Mark te beoordelen

Zie `BESLISOVERZICHT.md` voor het complete overzicht (A/B/C-keuzes, VNS-CAND-006-dedupvraag,
VNS-CAND-008-coordinaatprobleem, VNS-CAND-023-afwijking, 35 nog te bevestigen markers).

## Niet uitgevoerd of verboden

- Centrale India-master-KML niet bijgewerkt.
- Geen nieuwe A/B/C-keuze namens Mark.
- Geen bestaand geldig kandidaatrecord (VNS-CAND-001 t/m 021) inhoudelijk gewijzigd.
- Geen afgewezen coordinaat teruggeplaatst.

## Readback

KML geparsed en gecontroleerd (zie hierboven). PDF geopend en teruggelezen met pypdf (zie hierboven).
Beide controles uitgevoerd NA creatie, inclusief een gerichte her-controle nadat de VNS-CAND-008-bug
in de KML werd gevonden en gecorrigeerd.
