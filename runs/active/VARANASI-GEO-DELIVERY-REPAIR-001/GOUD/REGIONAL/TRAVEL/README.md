# Varanasi TRAVEL-module

run_id: VARANASI-GEO-DELIVERY-REPAIR-001
status: KLAAR. Op basis van de definitieve dataset (40/40 besloten), Marks A/B/C-keuzes en het
LOCKED_BY_MARK-hotelbesluit. Geen nieuw kandidaatonderzoek, geen A/B/C-wijziging.

## Bestanden

- `DAGROUTES.md` -- dagblokken A-D, en de combinaties voor 2, 3 en 4 dagen, vertrek/eind bij de
  hotelbasis.
- `AARTI_EN_BOOT.md` -- Ganga Aarti (Dashashwamedh, avond) en Subah-e-Banaras (Assi Ghat, ochtend)
  tijden, plus bootmomenten.
- `PRAKTISCHE_TIPS.md` -- weer/kleding, ghats/rivier, vervoer, geld, gezondheid, respect/gedrag.
- `RESTAURANTS.md` -- compacte selectie rond Assi Ghat/hotelbasis (informatief, geen GEO-
  kandidaatverificatie).

## Integratie

- **KML**: `USER/VARANASI_40_KANDIDATEN.kml` heeft een nieuwe folder "Travel -- dagroutes (Dagblok
  A-D)" met per dagblok een route-lijn (LineString) langs de bestaande kandidaatcoordinaten, in
  bezoekvolgorde. Geen nieuwe coordinaten toegevoegd; de hotelbasis heeft geen geverifieerde
  marker en staat daarom niet als lijnstartpunt.
- **PDF**: NIET bijgewerkt in deze ronde. Mark heeft expliciet gevraagd te stoppen met het
  (her)bouwen van de PDF -- die regel staat nu in `INDIA5-PROTOCOL.md` ("PDF is eenmalig — NIET
  automatisch herbouwen"). De CCI-travel-opdracht noemde PDF-integratie als punt 8; dat is
  hiermee in tegenspraak met de net daarvoor gegeven, zeer expliciete stop-instructie. Dit is
  bewust NIET stilzwijgend opgelost -- zie het bijbehorende eindrapport, waarin dit expliciet aan
  Mark wordt voorgelegd.
