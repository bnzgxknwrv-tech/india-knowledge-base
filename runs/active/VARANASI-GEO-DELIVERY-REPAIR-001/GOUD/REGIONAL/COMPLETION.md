run_id: VARANASI-GEO-DELIVERY-REPAIR-001
role: GOUD
scope: volledig regionaal Varanasi-pakket, alle 40 kandidaten (VNS-CAND-001 t/m 040)
status: KLAAR

## Eindproducten

- `GOUD/REGIONAL/DATASET_VARANASI_40.jsonl` -- de volledige gevalideerde dataset (40 records, incl.
  `display_id` = permanent nummer).
- `NUMBERING_REGISTRY.jsonl` -- het permanente, onwijzigbare nummer per kandidaat (Mark-besluit
  IMMUTABLE_LOCATION_NUMBERING, 2026-08-02).
- `GOUD/REGIONAL/USER/VARANASI_40_KANDIDATEN.kml` -- definitieve Varanasi-KML, alle 40 kandidaten,
  elke naam met nummerprefix, kleurcodering per Mark-keuze (groen=A, oranje=B, paars=C, wit=DOOR_
  MARK_TE_BEOORDELEN), vorm per status (ster=CONFIRMED, cirkel=PROVISIONAL), aparte lege AMBIGUOUS-
  laag, geen REJECTED-bestemmingen.
- `GOUD/REGIONAL/USER/VARANASI_40_KEUZE.pdf` -- oorspronkelijke technische keuze-PDF, ongewijzigd
  bewaard ter vergelijking.
- `GOUD/REGIONAL/USER/VARANASI_40_KEUZE_REISGIDS.pdf` -- het nieuwe, verplichte reisgidsformaat, elke
  kandidaattitel met nummerprefix, 42 pagina's.
- `GOUD/REGIONAL/GEO_AUDIT.md` -- volledige geo-audit, statusoverzicht, dedup-check, bijgewerkte
  Mark-keuze-verdeling.
- `GOUD/REGIONAL/CORRECTIERAPPORT.md` -- tooling-fix, ZILVER-bevindingen, gecorrigeerde KML-bug,
  Mark-besluitronde 2026-08-02.
- `GOUD/REGIONAL/BESLISOVERZICHT.md` -- compleet beslisoverzicht voor Mark, incl. de gevonden
  tegenstrijdigheid over de Sarnath-deelsites.
- `GOUD/REGIONAL/COMPLETION.md` -- dit bestand.

## Bestandscontroles

- `validate_brons.py`: OK, 40/40 BRONS-records.
- `validate_numbering.py`: OK, 40/40 permanente nummers gecontroleerd (registry, dataset, KML- en
  PDF-naamprefixes), geen dubbele of gewijzigde nummers.
- KML geparsed met `xml.etree.ElementTree`: 40/40 Placemarks, geen duplicaten, geen ontbrekende
  kandidaten, coordinatenvolgorde (lon,lat) correct, het expliciet afgewezen VNS-CAND-008-coordinaat
  komt in GEEN enkele `<Point>` voor (geverifieerd met een geautomatiseerde check).
- Reisgids-PDF teruggelezen met `pypdf`: 42 pagina's, alle 40 candidate_id's aanwezig, geen
  technische reason-tekst of herhaalde generieke zin overgenomen.
- Dataset gecontroleerd: 40 unieke candidate_id's, statusverdeling 5 CONFIRMED / 35 PROVISIONAL / 0
  AMBIGUOUS / 0 REJECTED, Mark-verdeling 25x A / 4x B / 2x C / 9x DOOR_MARK_TE_BEOORDELEN.

## Zekere locaties (5)

018, 019 (eerder bevestigd), 029, 031, 033 (bevestigd tijdens ZILVER van de testsweep) -- alle vijf
via een officiele Google-kaartbron. Status los van A/B/C: 018 en 029/031/033 zijn nu A, 019 is nog
open.

## Onzekere locaties (35)

Alle overige kandidaten: PROVISIONAL, fysieke identiteit bevestigd, Google Maps-marker (nog) niet
geverifieerd. Zie GEO_AUDIT.md voor de volledige tabel. Een A/B/C-besluit verandert nooit een
coordinaat of geo-status.

## Beschermde Mark-keuzes

25x A, 4x B, 2x C -- volledige lijst in GEO_AUDIT.md en RUN.yaml `protected_mark_decisions`. Het
expliciet afgewezen VNS-CAND-008-coordinaat [25.3045, 82.979369] is nergens gebruikt.

## Door Mark te beoordelen

9 kandidaten blijven open: 012, 019, 040, plus 029-034 (zie BESLISOVERZICHT.md punt 1 voor een
gevonden tegenstrijdigheid over de Sarnath-deelsites die expliciete bevestiging vraagt). Ook 008
(coordinaatprobleem) en 023 (3km-afwijking) hebben een openstaand technisch punt, los van hun reeds
vaste B-keuze.

## Niet uitgevoerd of verboden

- Centrale India-master-KML niet bijgewerkt.
- Geen nieuwe A/B/C-keuze namens Mark (alleen de gecommitte besluiten van Mark zelf verwerkt).
- 029-034 NIET stil op A gezet ondanks de losse tegenstrijdige zin in de opdracht (zie
  BESLISOVERZICHT.md punt 1).
- Geen bestaand geldig kandidaatrecord (VNS-CAND-001 t/m 021) inhoudelijk gewijzigd.
- Geen afgewezen coordinaat teruggeplaatst.
- Geen bestaand permanent nummer gewijzigd, hergebruikt of dubbel toegekend.

## Readback

KML geparsed en gecontroleerd (zie hierboven). PDF geopend en teruggelezen met pypdf (zie hierboven).
Beide controles uitgevoerd NA creatie, inclusief een gerichte her-controle nadat de VNS-CAND-008-bug
in de KML werd gevonden en gecorrigeerd.
