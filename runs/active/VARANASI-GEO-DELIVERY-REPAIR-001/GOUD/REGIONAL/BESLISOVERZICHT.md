# BESLISOVERZICHT VOOR MARK -- volledig regionaal Varanasi-pakket

run_id: VARANASI-GEO-DELIVERY-REPAIR-001
datum: 2026-08-02 (bijgewerkt na Marks definitieve keuzeronde, commit 58be47b)

Dit overzicht is bijgewerkt nadat Mark op 2026-08-02 zijn definitieve A/B/C-keuzeronde heeft
vastgelegd in `MARK_DECISIONS_2026-08-02.jsonl`. Van de 40 kandidaten zijn er nu 31 besloten
(25x A, 4x B, 2x C); 9 blijven open. Alle besluiten hieronder zijn 1-op-1 overgenomen uit dat
gecommitte bestand -- er is in deze ronde GEEN nieuwe A/B/C-keuze gemaakt namens Mark.

## 1. TEGENSTRIJDIGHEID GEVONDEN -- bevestiging gevraagd: Sarnath-deelsites (029-034)

Dit is het belangrijkste openstaande punt. De CCI-opdracht van 2026-08-02 bevat twee elkaar
tegensprekende instructies over dezelfde zes kandidaten:

- **Herhaald en gecommitteerd (3x expliciet in de opdracht, plus letterlijk in
  `MARK_DECISIONS_2026-08-02.jsonl`)**: "006 Sarnath sacred complex = A. Dit besluit maakt NIET
  automatisch de afzonderlijke kandidaten 029 t/m 034 tot A. Deze zes specifieke Sarnath-deelsites
  blijven DOOR_MARK_TE_BEOORDELEN totdat Mark ze afzonderlijk beslist." Ook letterlijk zo vastgelegd
  in het gecommitte besluitbestand zelf (cluster-decision SARNATH, note-veld).
- **Eén losse, niet-gecommitte zin aan het einde van dezelfde opdracht**: "Mark; nog open dtaat er
  maar de sites van cluster Sarnath mag je allemaal A maken."

Deze twee instructies spreken elkaar rechtstreeks tegen. Omdat de eerste versie herhaald,
expliciet uitgeschreven EN vastgelegd is in het gezaghebbende, gecommitte besluitbestand, en de
tweede een losse ongestructureerde zin met een typefout is, is in dit pakket gekozen om **029-034
NIET stil om te zetten naar A** en de expliciete, gecommitte instructie te volgen.

**Vraag aan Mark:** wilt u dat 029 (Dhamek Stupa), 030 (Mulagandha Kuti Vihara), 031 (Chaukhandi
Stupa), 032 (Sarnath Archaeological Museum), 033 (Deer Park/Isipatana) en 034 (Saranganath Temple)
inderdaad open blijven zoals nu verwerkt, of wilt u dat ze alsnog allemaal A worden? Eén duidelijk
"ja, allemaal A" of "nee, laat ze open" is voldoende om dit in de volgende ronde correct te
verwerken.

## 2. Resterende open kandidaten (9, exclusief de Sarnath-deelsites hierboven)

- 012 Harishchandra Ghat
- 019 Kedareshwar Temple and Kedar Ghat
- 040 Bharat Mata Temple

(029-034 zijn hierboven apart behandeld.)

## 3. VNS-CAND-008 heeft geen enkel veilig coordinaat

Het enige bekende vergelijkingspunt voor 008 (Yogoda Satsanga Dhyana Mandali) is het coordinaat dat
Mark eerder expliciet heeft afgewezen. Er is geen vervangend punt gevonden (geen interactieve Google
Maps-toegang beschikbaar in deze sessie). Mark-keuze B blijft ongewijzigd; dit gaat uitsluitend over
de ontbrekende kaartpositie.

**Vraag aan Mark:** wilt u dat een volgende sessie hier gericht opnieuw naar een geldig coordinaat
zoekt, of blijft 008 voorlopig zonder kaartpositie in de KML/PDF staan?

## 4. VNS-CAND-023 (keuze B): 3 km-afwijking

Mrityunjay Mahadev Temple: een onafhankelijke (niet-Google) bron geeft een coordinaat dat ca. 3 km
afwijkt van het oude vergelijkingspunt. Prioriteit voor handmatige verificatie zodra interactieve
Google Maps-toegang beschikbaar is. De B-keuze zelf staat niet ter discussie.

## 5. Nog geen bevestigde Google Maps-marker (35 van de 40)

Alleen 018, 019 (van vóór deze ronde), 029, 031 en 033 hebben een coordinaat uit een officiele
Google-kaartbron. Dit staat los van de A/B/C-status: een A-besluit verandert nooit een coordinaat of
de geo-onzekerheid. De overige kandidaten hebben een bevestigde fysieke identiteit maar geen
geverifieerde marker -- dit vraagt op termijn om een sessie met interactieve Google Maps-toegang.

## Definitief vastgelegd, ter bevestiging (geen open vraag)

- 25x A, 4x B, 2x C: zie `GEO_AUDIT.md` voor de volledige lijst met nummers, of de keuze-index in
  `USER/VARANASI_40_KEUZE_REISGIDS.pdf`.
- Immutable Location Numbering-regel: elk permanent nummer in `NUMBERING_REGISTRY.jsonl` is
  vastgelegd en wijzigt nooit.
- Het expliciet afgewezen coordinaat van 008 [25.3045, 82.979369] is nergens gebruikt.
- Centrale India-master-KML: niet aangepast.
