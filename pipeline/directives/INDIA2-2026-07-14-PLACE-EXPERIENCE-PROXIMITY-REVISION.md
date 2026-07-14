# INDIA2 -> SUBREGIE INDIA — plaatsbeleving, reviewanalyse en nabijheidsmatrix

## Status

`QUEUED_AFTER_DECISION_0005_IMPLEMENTATION`

## Gezaghebbend besluit

Lees en implementeer na afronding van de actieve devotionele methodologiecorrectie:

`decisions/DECISION-0006-place-experience-proximity-and-base-selection.md`

## Doel

Voeg een afzonderlijke ervarings- en ruimtelijke laag toe zonder de inhoudelijke spirituele beoordeling te vermengen met praktische nabijheid.

## Minimaal aanpassen

- methodologie en quality gate;
- BRONS-, ZILVER- en GOUD-rollen waar belevingsonderzoek of broncontrole nodig is;
- Marks rapporttemplate;
- route-/clusterfase;
- een schema voor reviewmomentopnamen;
- een schema voor volledige onderlinge afstands- en reistijdmatrices;
- een transparant model voor intrinsiek advies versus routeadvies;
- versie- en changelogbestanden.

## Review- en sfeeronderzoek

Per kandidaat waar mogelijk verzamelen:

- Google Maps-rating, reviewaantal en peildatum;
- Tripadvisor-rating, reviewaantal en peildatum;
- recente reviewthema's over schoonheid, sfeer, rust, chaos, netheid, commercie, devotie, gastvrijheid en toegankelijkheid;
- actuele bezoekersfoto's;
- verschillen tussen devotees en algemene toeristen;
- verschillen naar dagdeel en festivalperiode.

Gebruik reviewplatforms uitsluitend voor ervarings- en praktijkclaims, niet voor historische of spirituele gebeurtenisclaims.

## Nabijheid

Maak na kandidatenonderzoek een matrix met voor ieder locatiepaar:

- wegafstand;
- realistische reistijd;
- looptijd wanneer relevant;
- routebeperkingen;
- peildatum en bron.

Voeg na Marks selectie een basisgebiedanalyse toe. Kies eerst het beste gebied op gewogen bereikbaarheid van A/B/C-plekken en pas daarna concrete hotels.

## Regressieset

Gebruik de acht kandidaten uit de Vrindavan-runs. Lever minimaal:

- plaatsbelevingsprofiel per kandidaat;
- reviewmomentopname waar beschikbaar;
- onderlinge reistijdmatrix;
- intrinsiek advies en routeadvies;
- vergelijking van mogelijke basisgebieden;
- voorbeeld waarin een intrinsieke C door één minuut extra lopen `ROUTE A` wordt zonder de intrinsieke beoordeling te vervalsen.

## Afhankelijkheid

Wijzig `pipeline/NEXT_ACTION.yaml` nu niet. De actieve opdracht voor DECISION-0005 blijft leidend. Activeer deze directive pas nadat SUBREGIE INDIA de devotionele methodologiecorrectie heeft afgerond en naar INDIA2 heeft teruggerouteerd.

END_OF_ARTIFACT