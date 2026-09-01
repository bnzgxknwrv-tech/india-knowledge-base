run_id: VARANASI-GEO-DELIVERY-REPAIR-001
role: GOUD
scope: volledig regionaal Varanasi-pakket, alle 40 kandidaten (VNS-CAND-001 t/m 040)
status: KLAAR -- inhoudelijke A/B/C-keuzeronde COMPLEET (32x A, 5x B, 3x C, 0x nog open)

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
- `ACCOMMODATION_REGISTER.jsonl` -- nieuw permanent accommodatieregister (los van de kandidaat-
  nummering 001-999), met het vastgelegde Varanasi-hotelbesluit (`VNS-HOTEL-001`, LOCKED_BY_MARK,
  commit cf2daf2).

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
  AMBIGUOUS / 0 REJECTED, Mark-verdeling 32x A / 5x B / 3x C / 0x DOOR_MARK_TE_BEOORDELEN.
- Volledige geautomatiseerde cross-check dataset/KML/PDF: alle 40 Mark-keuzes consistent op alle
  drie plekken (geen enkele mismatch).

## Zekere locaties (5)

018, 019, 029, 031, 033 -- alle vijf via een officiele Google-kaartbron. Status los van A/B/C: alle
vijf zijn inmiddels A.

## Onzekere locaties (35)

Alle overige kandidaten: PROVISIONAL, fysieke identiteit bevestigd, Google Maps-marker (nog) niet
geverifieerd. Zie GEO_AUDIT.md voor de volledige tabel. Een A/B/C-besluit verandert nooit een
coordinaat of geo-status.

## Beschermde Mark-keuzes

32x A, 5x B, 3x C -- volledige lijst in GEO_AUDIT.md en RUN.yaml `protected_mark_decisions`. Het
expliciet afgewezen VNS-CAND-008-coordinaat [25.3045, 82.979369] is nergens gebruikt.

## Door Mark te beoordelen

Geen A/B/C-vragen meer -- alle 40 kandidaten zijn besloten. Resterende punten zijn zuiver technisch
(geen A/B/C-vraag): 008 heeft geen veilig coordinaat, 023 heeft een 3km-afwijking tussen bronnen.
Zie BESLISOVERZICHT.md.

## Gekozen verblijf

Sahi River View Guesthouse (Assi Ghat) is vastgelegd als `LOCKED_BY_MARK` Varanasi-basis (commit
cf2daf2, `HOTEL_DECISION.md`). Verwerkt in `ACCOMMODATION_REGISTER.jsonl` (`VNS-HOTEL-001`), de
reisgids-PDF (hoofdstuk "Gekozen verblijf", direct na de keuze-index) en de KML (aparte folder
"Gekozen verblijf (LOCKED_BY_MARK)", geen A/B/C-ID). Geen geverifieerde Google Maps-marker gevonden
-- geen `<Point>`-geometrie toegevoegd, alleen tekstueel adres. Data is routeklaar (basis +
bereikbare A-clusters); nog geen volledige dagroute berekend (bewust buiten scope van deze ronde).

## Niet uitgevoerd of verboden

- Centrale India-master-KML niet bijgewerkt.
- Geen nieuwe A/B/C-keuze namens Mark (alleen de gecommitte/expliciet bevestigde besluiten van Mark
  zelf verwerkt, inclusief de expliciete bevestiging voor 029-034 in de afrondende ronde).
- Geen bestaand geldig kandidaatrecord (VNS-CAND-001 t/m 021) inhoudelijk gewijzigd.
- Geen afgewezen coordinaat teruggeplaatst.
- Geen bestaand permanent nummer gewijzigd, hergebruikt of dubbel toegekend.
- Geen volledige dagroute-/planningberekening uitgevoerd vanuit het hotel (alleen routeklaar gemaakt,
  zoals expliciet gevraagd).
- Geen coordinaat geraden voor het hotel bij gebrek aan een geverifieerde Google Maps-marker.

## Readback

KML geparsed en gecontroleerd (zie hierboven). PDF geopend en teruggelezen met pypdf (zie hierboven).
Beide controles uitgevoerd NA creatie, inclusief een gerichte her-controle nadat de VNS-CAND-008-bug
in de KML werd gevonden en gecorrigeerd.
