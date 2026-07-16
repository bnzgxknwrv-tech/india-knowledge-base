---
id: DECISION-0014
subject: "Vrindavan-Kumaon-corridor, zeer strenge A-poort, WORKING_GEO en centrale KML"
decided_by: "Mark"
decided_at: "2026-07-16"
outcome: "Onderzoek de snelste corridor naar Kumaon; onderbreek alleen voor vervoer of een werkelijk zware A; gebruik bruikbare gelabelde werkpunten en lever centrale kaartdata/KML"
applies_to: "VRINDAVAN-KUMAON-CORRIDOR-001 en de daaropvolgende kaart- en regisseursverwerking"
clarifies:
  - "DECISION-0003"
  - "DECISION-0005"
  - "DECISION-0009"
  - "DECISION-0013"
---

# DECISION 0014: corridor, zware A, WORKING_GEO en KML

## 1. Hoofdvraag

De route van Marks formele A-locaties in Vrindavan naar zijn formele A-locaties in Kumaon wordt primair op snelheid, logica en betrouwbaarheid onderzocht. Een tussenstop of overnachting is alleen gerechtvaardigd wanneer vervoer dit praktisch noodzakelijk maakt of wanneer een werkelijk zware, routebepalende A wordt gevonden.

Wanneer geen zware A wordt gevonden, luidt het eindadvies: `DOORREIZEN NAAR KUMAON`.

## 2. Zeer strenge A-poort

Een locatie mag alleen als mogelijke zware A naar INDIA2 worden doorgestuurd wanneer zij minimaal één poort haalt:

1. `DIRECTE_PERSOONLIJKE_LIJN`: concrete fysieke relatie met Marks lijn, TOP_X of AOAY, zoals samadhi, ashram, feitelijke verblijfplaats, onderwijsplek, directe instelling, lineageplek of concrete belangrijke gebeurtenis.
2. `INDIA_ESSENTIAL`: nationaal of wereldwijd kernheiligdom waarvoor mensen speciaal grote afstanden reizen en waarvan overslaan waarschijnlijk een werkelijke gemiste kans is.

Gewone lokale tempels, algemene stadsinteresse en regionale religieuze plekken rechtvaardigen geen tussenstop of overnachting.

## 3. Krishna-regel

Maak verplicht onderscheid tussen:

- Krishna als leraar van de Bhagavad Gita;
- Krishna/Babaji binnen de Kriya-lineage;
- een nationaal of wereldwijd canoniek Krishna-heiligdom;
- algemene Krishna-tempels;
- regionale Braj-lila-, kund-, sarovar- en verhaalplaatsen.

Alleen de eerste twee categorieën of een uitzonderlijk sterke derde categorie kunnen zelfstandig een zware A zijn.

## 4. A-gestuurde reislogica

`EEN A MAAKT EEN CLUSTER. EEN CLUSTER MAAKT NOOIT AUTOMATISCH NIEUWE A'S.`

Onderzoek standaard rond bestaande formele A's, langs de werkelijke corridor, rond grote stations en overstapsteden en globaal binnen circa 20 kilometer of ongeveer 30 minuten extra reistijd. Buiten deze zone wordt alleen een zelfstandig zeer zware A onderzocht. Nabijheid versterkt relevantie maar maakt nooit zelfstandig een A.

## 5. WORKING_GEO voor deze run

DECISION-0013 blijft gelden voor permanente LOCATION_ID's en uiteindelijke verificatie. Voor deze run is daarnaast `WORKING_GEO` toegestaan wanneer de bedoelde fysieke locatie redelijk betrouwbaar herkenbaar blijft.

Toegestaan:

- bestaand Google Maps- of OpenStreetMap-punt;
- straatadres;
- gebouw- of terreinmiddelpunt;
- stationspunt;
- representatief centrum van een route- of landschapsobject.

Een geschatte afwijking van circa 50–500 meter is acceptabel wanneer naam, bron, puntsoort en nauwkeurigheid zichtbaar zijn. Een punt wordt gelabeld `WORKING` of `VERIFIED`; een gelijknamig hotel, winkel, kantoor of verkeerde plaats is nooit acceptabel.

## 6. Centrale kaartlaag

De keten levert een centrale praktische KML of het volledige, zonder nieuw inhoudelijk onderzoek omzetbare bronbestand met minimaal:

- `A_FORMEEL` — groen;
- `B_ADVIES` — oranje en niet formeel;
- `C_CONTEXT` — rood;
- `CORRIDOR_EN_STATIONS` — routes, stations, overstappunten en relevante steden.

Iedere marker bevat LOCATION_ID, naam, cluster, formeel/adviserend karakter, herkenningshaak, GEO-status en routerelevantie. Formele A-locaties uit de volledige repository blijven in de kaartbron zichtbaar. Een ontbrekend blok of ID wordt technisch opgelost zonder een tijdelijk nummer als permanent te presenteren.

## 7. Rollen

BRONS inventariseert breed, onderzoekt routeopties en levert WORKING_GEO en kaartbron. ZILVER verwijdert opgeblazen lokale kandidaten en controleert route- en A-poortclaims. GOUD controleert inhoud, praktische logica en geografie, maar blokkeert een bruikbare werkkaart niet uitsluitend omdat een exacte bezoekersingang nog niet is bevestigd.

BRONS, ZILVER en GOUD kennen geen formele A/B/C toe. INDIA2 mag adviserend A/B/C geven. Alleen Mark beslist formeel.

END_OF_ARTIFACT