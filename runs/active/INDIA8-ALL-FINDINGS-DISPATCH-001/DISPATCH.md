# INDIA8 ALL-FINDINGS DISPATCH — 001

## DOEL
Zet de lossless all-findings closure parallel in uitvoering. Mark is eindredacteur; INDIA8/INDIA9 regisseert en integreert. Geen agent wacht op Mark voor onderzoekskeuzes binnen zijn scope.

## HARD
- Geen bestaande permanente IDs verwijderen, hernummeren of hergebruiken.
- Geen bestaande A/B/C of locks wijzigen.
- Geen nieuwe A/B/C namens Mark.
- Geen route/hotelbestemming definitief kiezen.
- Geen locatieclaim laten verdwijnen omdat identiteit/adres/toegang onzeker is.
- Elk bronrecord moet eindigen als fysieke entity-link, duplicate-link of expliciete unresolved record.
- R1/R2/R3/R4/R5 gebruiken volgens LOCATION_RESOLUTION_BEFORE_ABC.
- Voor R1/R2/R3 huidige bezoekbaarheid/access vastleggen.
- Oost blijft voor reis geparkeerd, maar DATA wordt volledig verwerkt.

## PARALLELLE WERKPAKKETTEN

### BLAUW — AOAY / YOGANANDA EXACT-LOCATION CLOSURE
Branch: agent/indiablauw-trip-ops-prep
Task: runs/active/INDIABLAUW-AOAY-YOGANANDA-LOCATION-CLOSURE-001/TASK.md
Focus: alle AOAY/Yogananda R4/R5 en micro-sites; historische identiteit, huidig adres, opvolger, access, hoofdstuk/scène. AOAY heeft hoogste inhoudelijke prioriteit.

### ROOD — CORE KRIYA LOCATION CLOSURE
Branch: agent/indiarood-core-kriya-sweep
Task: runs/active/INDIAROOD-CORE-KRIYA-LOCATION-CLOSURE-001/TASK.md
Focus: Babaji, Lahiri Mahasaya, Sri Yukteswar; alle unresolved/approximate/host-house/grot/kamer/ghat/PWD/postmortale scene records uit alle detectoren.

### GEEL — NKB / RAM DASS / RAMANA / RAMAKRISHNA CLOSURE
Branch: agent/indiageel-ramana-ramakrishna-sweep
Task: runs/active/INDIAGEEL-FOURPERSON-LOCATION-CLOSURE-001/TASK.md
Focus: alle samengestelde en detector-only claims naar losse fysieke entities; onbekende hotels/dharamshalas/kamers/devoteehuizen/grotten/micro-sites niet laten verdwijnen.

### WIT — ANANDAMAYI + HERITAGE-STAY CLOSURE
Branch: agent/indiawit-master-travel-readiness
Task: runs/active/INDIAWIT-ANANDAMAYI-HERITAGE-LOCATION-CLOSURE-001/TASK.md
Focus: Anandamayi source-first + 156-union + hostgraph naar entities; daarnaast heritage-stay/hotel/ashram-kamer claims voor alle personen exact oplossen voor zover mogelijk.

### ZILVER — ID / PROXIMITY / ENTITY BACKFILL
Branch: agent/indiazilver-cluster-completeness-audit
Task: runs/active/INDIAZILVER-ENTITY-ID-PROXIMITY-BACKFILL-001/TASK.md
Focus: bestaande permanente IDs/A-B-C als beschermde baseline; nieuwe entities voorbereiden voor nieuwe IDs; betrouwbare coördinaten; <=1 km/<=3 km proximity; same-site/duplicate candidate mapping. Geen IDs daadwerkelijk toekennen voordat centrale reconciliatie entity-identity heeft bevestigd.

### TURQUOISE — CENTRAL ENTITY / OVERLAP RECONCILIATION PREP
Branch: agent/indiaturquoise-allperson-overlap
Task: runs/active/INDIATURQUOISE-ENTITY-OVERLAP-RECONCILIATION-001/TASK.md
Focus: cross-person same-site overlap, aliases, successor-sites, micro-site-vs-complex relaties en duplicate candidates; geen source record verwijderen. Levert entity merge-map voor centrale master.

## CENTRALE VOLGORDE
1. Parallelle agents produceren lossless candidate/result tables.
2. INDIA8/INDIA9 integreert alle outputs in ALL_FINDINGS_LOCATION_MASTER.
3. Accounting moet sluiten: iedere sourceclaim = entity / duplicate-link / unresolved.
4. Daarna alleen resterende R4/R5 gericht opnieuw onderzoeken.
5. Daarna nieuwe fysieke entities permanent ID-traject.
6. Daarna pas per gekozen/te kiezen cluster Mark A/B/C.
7. Daarna route/nachten/transport/hotels.

## REISPRIORITEIT BIJ RESOLUTIE
P0 AOAY Yogananda persoonlijke scenes
P1 Kumaon / Varanasi / Bodh Gaya / Tiruvannamalai-Arunachala
P2 Vrindavan-Braj / Prayagraj-Allahabad casting
P3 Delhi korte start + individuele route-overrides
P4 Oost-data volledig bewaren/verwerken maar niet routepromoveren
