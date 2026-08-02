# BESLISOVERZICHT VOOR MARK -- volledig regionaal Varanasi-pakket

run_id: VARANASI-GEO-DELIVERY-REPAIR-001
datum: 2026-08-02 (afgerond -- alle 40 kandidaten hebben een definitieve Mark-keuze)

De inhoudelijke A/B/C-keuzeronde voor Varanasi is COMPLEET. Alle 40 kandidaten hebben een
definitieve keuze: 32x A, 5x B, 3x C. Er staat geen enkele kandidaat meer als
DOOR_MARK_TE_BEOORDELEN. Alle besluiten zijn 1-op-1 overgenomen uit Marks eigen berichten/commits
-- er is op geen enkel moment een A/B/C-keuze gemaakt namens Mark.

## Definitieve verdeling

- **A (32)**: 001, 002, 003, 004, 005, 006, 007, 009, 010, 011, 014, 015, 016, 017, 018, 019, 020,
  021, 022, 024, 028, 029, 030, 031, 032, 033, 034, 035, 036, 037, 038, 039
- **B (5)**: 008, 012, 013, 023, 025
- **C (3)**: 026, 027, 040

## Sarnath (006, 029-034) -- tegenstrijdigheid gevonden EN opgelost

Eerder signaleerde dit pakket een tegenstrijdigheid: de opdracht zei zowel herhaald/expliciet/
gecommitteerd dat de zes Sarnath-deelsites (029-034) apart open moesten blijven na het 006=A-
besluit, als (in één losse zin) dat ze allemaal A gemaakt mochten worden. Die tegenstrijdigheid is
NIET stilzwijgend opgelost, maar expliciet aan Mark voorgelegd. Mark heeft daarna expliciet
bevestigd: 029, 030, 031, 032, 033 en 034 worden allemaal A. Dit is verwerkt als een apart,
zelfstandig bevestigd besluit -- niet als automatische afleiding uit 006=A.

## Resterende technische punten (geen A/B/C-vragen meer)

- **008 Yogoda Satsanga (B)**: geen enkel veilig coordinaat beschikbaar -- het enige bekende punt is
  het door Mark expliciet afgewezen coordinaat. Wilt u dat een volgende sessie hier gericht opnieuw
  naar een geldig coordinaat zoekt (interactieve Google Maps-toegang nodig), of blijft 008 voorlopig
  zonder kaartpositie?
- **023 Mrityunjay Mahadev (B)**: een onafhankelijke bron wijkt ca. 3 km af van het oude
  vergelijkingspunt. Prioriteit voor handmatige verificatie zodra interactieve Google Maps-toegang
  beschikbaar is.
- **35 van de 40 kandidaten** hebben nog geen bevestigde Google Maps-marker (alleen 018, 019, 029,
  031, 033 wel). Dit staat volledig los van de nu complete A/B/C-keuze -- een A/B/C-besluit
  verandert nooit een coordinaat of geo-status. Dit vraagt op termijn een sessie met interactieve
  Google Maps-toegang, buiten wat deze sessie kan uitvoeren.

## Gekozen verblijf -- Sahi River View Guesthouse (LOCKED_BY_MARK)

Mark heeft (commit `cf2daf27299cf4153921ed1fdc64a876b9b2661f`, `HOTEL_DECISION.md`) de Varanasi-basis
vastgelegd: **Sahi River View Guesthouse**, Assi Ghat. Dit is GEEN openstaande vraag -- status
`LOCKED_BY_MARK`, niet te vervangen zonder een expliciet nieuw besluit van Mark. Vastgelegd in het
nieuwe `ACCOMMODATION_REGISTER.jsonl` (accommodatie-ID `VNS-HOTEL-001`, apart van de kandidaat-
nummering 001-040) en verwerkt in de reisgids-PDF ("Gekozen verblijf"-hoofdstuk) en de KML (aparte
folder "Gekozen verblijf (LOCKED_BY_MARK)"). Verplichte notities: balcony room aanvragen, groeten aan
Jitendre van Debby. Geen geverifieerde Google Maps-marker gevonden -- alleen tekstueel adres
opgenomen, geen coordinaat geraden (adres: B1/158 A2, Assi Ghat Rd, Varanasi, Uttar Pradesh 221005).
Data is routeklaar (basis + logisch bereikbare A-clusters gelijst); er is nog GEEN volledige
dagroute-/planningberekening uitgevoerd -- dat is een aparte, nog niet uitgevoerde stap.

## Definitief vastgelegd

- Alle 40 Mark-keuzes: zie hierboven, of de keuze-index in `USER/VARANASI_40_KEUZE_REISGIDS.pdf`.
- Immutable Location Numbering-regel: elk permanent nummer in `NUMBERING_REGISTRY.jsonl` is
  vastgelegd en wijzigt nooit.
- Het expliciet afgewezen coordinaat van 008 [25.3045, 82.979369] is nergens gebruikt.
- Accommodatiebesluit Varanasi: Sahi River View Guesthouse, `LOCKED_BY_MARK` (zie hierboven).
- Centrale India-master-KML: niet aangepast.

## Volgende stap

De inhoudelijke keuzeronde is klaar. Openstaand zijn uitsluitend technische geo-verificatiepunten
(hierboven) -- geen daarvan vereist een nieuwe A/B/C-beslissing. Deze PR (#23) staat klaar voor uw
beoordeling en, zodra u akkoord bent, voor merge.
