# VARANASI_FINAL_STATUS — afsluiting sweep, MAINTENANCE_STATUS

Besluit: INDIA2, PR #23, 2026-08-03. Varanasi Discovery wordt hiermee afgesloten. De regio gaat
naar MAINTENANCE_STATUS: geen nieuwe locaties meer, tenzij Mark daar expliciet om vraagt of
concreet nieuw bewijs een echte NOT_TO_BE_MISSED-locatie aantoont.

## Definitieve scope

Varanasi stad + straal van circa 20 km rond het centrum (Dashashwamedh Ghat, ~25.31°N 83.01°E),
plus een signalerende blik tot circa 30-34 km (één gevonden Jain-kalyanaksite, Chandraprabhu/
Chandrawati, op ~34 km, expliciet buiten scope gehouden). Onderzoek uitgevoerd in twee fasen:
de oorspronkelijke GEO-doorloop (001-040, Mark-beoordeeld) en een latere discovery-/coverage-
audit (041-045, PROVISIONAL).

## Totaal aantal permanente kandidaten

**45** permanent genummerde kandidaten in `NUMBERING_REGISTRY.jsonl` (VNS-CAND-001 t/m 045).
Geen 046 of hoger — een eerder overwogen 046e kandidaat (Laat Bhairav) is nooit gecommit; die
taak is ingetrokken vóór afronding (zie git-historie PR #23, HOLD 2026-08-03).

## Aantal A/B/C

Van de 40 oorspronkelijke, door Mark beoordeelde kandidaten (001-040):
- **A: 32**
- **B: 5**
- **C: 3**

De 5 discovery-kandidaten (041-045) hebben GEEN A/B/C — status blijft `PROVISIONAL` /
`DOOR_MARK_TE_BEOORDELEN`, ongewijzigd, in afwachting van Marks eigen initiatief.

## Aantal WATCHLIST

Van de 5 discovery-kandidaten (041-045), na toetsing tegen het NOT_TO_BE_MISSED-framework
(`india5/reports/VARANASI_NOT_TO_BE_MISSED_041_045_REASSESSMENT.md` en de daaropvolgende
verdiepingscontrole `india5/reports/VARANASI_041_045_DEEPENING_CHECK.md`):
- **PASS (na verdieping): 2** — 041 Parshvanath Digambar Jain Temple, 045 Adi Keshava Ghat.
- **WATCHLIST: 2** — 042 Suparshvanath Jain Tirth, 044 Ramnagar Fort.
- **FAIL: 1** — 043 Shreyansanath Jain Tirth (Sarnath).

Dit zijn CCI-adviezen, geen A/B/C-besluiten. Conform het besluit van vandaag blijven alle vijf
records in `DISCOVERY_CANDIDATES.jsonl` ongewijzigd staan; er is geen automatische promotie naar
een Mark-keuzeronde.

## Open onzekerheden

- VNS-CAND-008: geen veilig/bevestigd coördinaat; het eerder afgewezen coördinaat
  [25.3045, 82.979369] is nergens als kaartgeometrie gebruikt.
- VNS-CAND-023: circa 3 km afwijking tussen twee bronnen, niet opgelost.
- 35 van de 40 GEO-bevestigde kandidaten (001-040) hebben nog geen bevestigde Google Maps-marker
  (`PROVISIONAL`, niet `CONFIRMED`).
- Het vastgelegde hotel (Sahi River View Guesthouse, `VNS-HOTEL-001`, `LOCKED_BY_MARK`) heeft
  geen geverifieerde Google Maps-marker — tekstueel adres, geen kaartpunt.
- 041-045: geen van de vijf heeft een bevestigde Google Maps-marker (`GOOGLE_MAPS_MARKER_NOT_CONFIRMED`
  voor alle vijf) — GEO-verificatie (BRONS) is voor deze vijf nooit uitgevoerd, expliciet buiten
  scope van de discovery-audit.
- 043 (FAIL-advies) blijft desondanks geregistreerd met permanent nummer — geen kandidaat wordt
  ooit stil verwijderd, alleen zijn NOT_TO_BE_MISSED-advies is negatief.
- Drie PRE-BRONS-detectoren uit de saturatie-episode (samadhi/mahasamadhi, levende ashram,
  sacrale geografie/yatra) zijn nooit canoniek vastgelegd of doorzocht — die episode is
  ingetrokken vóór afronding; er bestaat geen betrouwbare uitspraak over deze richtingen voor
  Varanasi.
- Geen lokale insider-/priesterbron is ooit geraadpleegd voor Varanasi — uitsluitend webbronnen,
  in alle onderzoeksrondes.

## Lessen voor de volgende regio

1. **Categorievolledigheid is geen geldig toevoegingscriterium.** De discovery-audits van
   041-045 zochten aanvankelijk naar "welke tradities ontbreken" — dat leverde kandidaten op die
   pas bij een tweede, striktere toets (NOT_TO_BE_MISSED) houdbaar bleken (of niet, zoals 043).
   Volgende regio's beginnen direct met de hoofdvraag, niet met een categorie-inventarisatie.
2. **Bronsterkte verandert een oordeel wezenlijk.** 041 en 045 gingen van WATCHLIST naar PASS
   zodra gerichte verificatie een primaire tekst (Vividha Tirtha Kalpa) en een historische
   inscriptie (Gahadavala-inscriptie) opleverde in plaats van uitsluitend reisblogs. Eerste-ronde
   bronnen zijn vaak onvoldoende; een gerichte verdiepingsronde op de sterkste kandidaten is de
   moeite waard vóórdat een definitief advies wordt gegeven.
3. **Nummering en kandidaatstatus moeten nooit vóór de inhoudelijke poort komen.** Dit was
   expliciet de fout bij 041-045 (eerst genummerd, pas achteraf getoetst) — nu structureel
   gecorrigeerd in `INDIA5_REGION_START_PROTOCOL.md`, stap 3 vóór stap 5.
4. **PR-comments zijn geen opslagmedium.** Lange inhoudelijke rapporten in PR-comments raken
   afgekapt bij het uitlezen. Volledige rapporten horen in bestanden; de PR-comment is
   uitsluitend een envelop (taak-id/commit/bestand/blob-SHA/status).
5. **Een taak kan en mag worden ingetrokken vóór uitvoering** (zoals SATURATION-004) zonder dat
   dit een fout is — het HOLD-mechanisme in `india5/TASK_PROTOCOL.md` bestaat precies hiervoor,
   en werkte hier zoals bedoeld: geen inhoudelijk spoor van de ingetrokken taak bleef achter op
   de branch.
6. **Een sweep mag op nul nieuwe kandidaten uitkomen** — dat is vanaf nu expliciet een geldig
   resultaat, niet een falen van de detectoren.

## Bevestiging: startprotocol voor volgende regio's

Elke volgende regiosweep start voortaan volgens de vaste negen stappen in
`india4/protocols/INDIA5_REGION_START_PROTOCOL.md` (PRE-BRONS → Discovery →
NOT_TO_BE_MISSED-poort → Kandidaatstatus → Permanente nummering → BRONS → ZILVER → GOUD →
TRAVEL), met de hoofdvraag uit `india4/protocols/NOT_TO_BE_MISSED_FRAMEWORK.md` boven elke
detector en boven categorievolledigheid. Dit is geen keuze meer per regio — het is de canonieke
startvolgorde voor alle toekomstige sweeps.

---
Geschreven door: CCI, op verzoek van INDIA2 (PR #23, afsluitopdracht).
Datum: 2026-08-03.
Status: Varanasi -> MAINTENANCE_STATUS. Geen PDF, geen KML, geen datasetwijziging, geen nieuwe
detectoren, geen nieuwe kandidaten door dit document.
