# CORRECTIERAPPORT -- volledig regionaal Varanasi-pakket (40 kandidaten)

run_id: VARANASI-GEO-DELIVERY-REPAIR-001
rapportdatum: 2026-08-02

## 1. Tooling-fix (voorafgaand aan deze GOUD-ronde)

Root cause: een eerdere BRONS-batchschrijver opende bestaande JSONL-batchbestanden in tekstmodus en
schreef er nieuwe regels overheen zonder te controleren of het bestand al op een newline eindigde.
Dit liet VNS-CAND-021 en VNS-CAND-022 samensmelten tot een ongeldige regel, en een eerste reparatie
herserialiseerde per ongeluk ALLE bestaande regels (cosmetische diff, spaties na ":"/",").

Oplossing: nieuw `scripts/append_batch_record.py` -- uitsluitend append of een gerichte toevoeging
(hoogstens een ontbrekende trailing newline), nooit een volledige herserialisatie van bestaande
regels. VNS-CAND-021 is teruggezet naar exact de originele bytes van voor de testsweep (inhoud
byte-voor-byte geverifieerd identiek). VNS-CAND-001 t/m 020 zijn niet aangeraakt.

## 2. ZILVER-Z01 (VNS-CAND-001-020, plus 021 als dekkingsfix)

- 18 kandidaten: PROVISIONAL (fysieke identiteit bevestigd via >=1 onafhankelijke bron, geen
  Google Maps-marker interactief te openen in deze sessie).
- 2 kandidaten (018, 019): CONFIRMED, ongewijzigd overgenomen (al EXACT_GOOGLE_MAPS_MARKER).
- Extra identiteitsbronnen (vooral officiele kashi.gov.in-listings) toegevoegd waar de dekking dun
  was (1 bron): VNS-CAND-002, 004, 006, 008, 010, 011, 012, 013, 014, 015, 016, 020.
- **Verworpen bevinding:** voor VNS-CAND-003 (Manikarnika Ghat) en VNS-CAND-009 (Dashashwamedh Ghat)
  gaf een Google Earth entity-API-zoekopdracht IDENTIEKE coordinaten voor twee verschillende, ~500-800
  m uit elkaar liggende ghats. Beoordeeld als onbetrouwbare generieke fallback (zoekterm "Ghat") en
  NIET gebruikt.
- **Dekkingsgat gedicht:** VNS-CAND-021 had een BRONS-record maar viel buiten zowel ZILVER-Z01
  (oorspronkelijk 001-020) als de testsweep (022-040). Alsnog gevalideerd volgens dezelfde regels;
  BRONS-record niet gewijzigd.
- Mark-besluiten exact behouden: VNS-CAND-001/002/003/007 = A, VNS-CAND-008 = B. Het expliciet
  afgewezen coordinaat [25.3045, 82.979369] gecontroleerd en niet hergebruikt.

## 3. Kritieke bevinding tijdens KML-opbouw: bijna-hergebruik van het afgewezen VNS-CAND-008-punt

Bij de eerste opzet van de regionale KML werd voor elke PROVISIONAL-kandidaat zonder eindcoordinaat
automatisch het oude vergelijkingspunt getoond. Voor VNS-CAND-008 is dat oude vergelijkingspunt
echter precies het door Mark afgewezen coordinaat -- de eerste KML-versie plaatste dit dus per ongeluk
alsnog op de kaart. **Gecorrigeerd voordat de KML werd opgeleverd:** VNS-CAND-008 krijgt in de
definitieve KML geen `<Point>`-geometrie; alleen een tekstuele vermelding met adres en een expliciete
toelichting dat er geen veilig coordinaat beschikbaar is. Geverifieerd met een geautomatiseerde check
dat het afgewezen coordinaat in geen enkele `<Point>` in het uiteindelijke bestand voorkomt.

## 4. Dedup: VNS-CAND-006 vs. Sarnath-deelsites (VNS-CAND-029-034)

Zie ook GEO_AUDIT.md en BESLISOVERZICHT.md. VNS-CAND-006 ("Sarnath sacred complex") is een
koepelkandidaat; de testsweep heeft daarbinnen 6 specifieke deelsites apart gecatalogiseerd. Dit is
als concrete, expliciete keuze aan Mark voorgelegd (BESLISOVERZICHT.md) -- er is GEEN A/B/C-besluit
hierover genomen namens Mark, en geen van beide kandidaattypen is gewijzigd of samengevoegd.

## 5. Openstaande bijzonderheden

- VNS-CAND-023 (Mrityunjay Mahadev Temple): een onafhankelijke (niet-Google) coordinaat wijkt ~3 km
  af van het oude vergelijkingspunt (uit de eerdere testsweep, ongewijzigd overgenomen).
- VNS-CAND-025 en VNS-CAND-028: physical_identity blijft PARTIAL (herdenkingszones zonder eenduidig
  hoofdgebouw, uit de eerdere testsweep, ongewijzigd overgenomen).
- VNS-CAND-008: geen enkel veilig coordinaat beschikbaar (zie punt 3) -- vraagt om een expliciete
  Mark-beslissing over vervolgstappen (nieuw onderzoek? voorlopig zonder kaartpositie laten?).

## 6. Wat NIET is gedaan (bewust buiten scope)

- Geen wijziging aan VNS-CAND-001 t/m 021 (bestaande geldige records, alleen gevalideerd/aangevuld
  met evidence, geen enkele bestaande waarde overschreven behalve het toevoegen van het nieuwe
  ZILVER-laag-record).
- Geen nieuwe A/B/C-keuze namens Mark voor welke kandidaat dan ook.
- Geen wijziging aan de centrale India-master-KML.
- Geen hergebruik van het expliciet afgewezen VNS-CAND-008-coordinaat, in geen enkel bestand.
