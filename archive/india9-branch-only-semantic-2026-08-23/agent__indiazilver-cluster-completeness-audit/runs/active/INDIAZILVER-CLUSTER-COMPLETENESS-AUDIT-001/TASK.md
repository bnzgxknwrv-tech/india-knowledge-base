# INDIA ZILVER — CLUSTER COMPLETENESS / REVERSE-RECALL AUDIT

STATUS: READY
OWNER: INDIA ZILVER
MODE: CROSS-LAYER AUDIT
GOAL: aantonen welke eerder afgeronde locatieclusters door persoonsgerichte sweeps onvolledig bleken en voorkomen dat Mark tijdens de reis op korte afstand van een relevante plek komt zonder dat die ooit aan hem is voorgelegd.

## Kernhypothese
Eerdere locatiegerichte sweeps waren niet volledig genoeg als enige detector. Persoonsgerichte sweeps hebben aantoonbaar nieuwe locaties gevonden. Daarom moet elk reisrelevant cluster vóór route-lock drie detectierichtingen doorstaan:
1. LOCATION_TO_PERSON / klassieke locatiesweep;
2. PERSON_TO_LOCATION / persoonsgerichte reverse discovery;
3. LOCAL_PROXIMITY_BACKFILL / lokale nabijheidsaudit rond bestaande en nieuw gevonden kandidaten.

## Opdracht
Maak repo-breed, op basis van reeds beschikbare resultaten en zonder bestaande keuzes te verwijderen:

1. `CLUSTER_RECALL_AUDIT.md`
   - inventariseer alle eerder als afgerond/bevroren/ABC-complete beschouwde clusters;
   - leg per cluster vast welke nieuwe persoonslocaties later alsnog verschenen;
   - markeer `REOPEN_REQUIRED: JA/NEE`;
   - onderscheid exact nieuwe fysieke kandidaat, alleen stad/regio, conflict/lead.

2. `MISSED_NEARBY_RISK.md`
   - identificeer nieuwe fysieke kandidaten die op korte praktische afstand liggen van bestaande A/B/C-locaties of gekozen verblijf/basis;
   - gebruik alleen betrouwbare bestaande coördinaten/afstanden; niet raden;
   - bands: <=250 m, 250-500 m, 0.5-1 km, 1-3 km, 3-10 km, >10 km/unknown;
   - extra vlag voor same-site of zelfde complex.

3. `REOPEN_AND_ID_QUEUE.md`
   - lijst alle nieuwe fysieke kandidaten die een nieuw permanent ID nodig hebben in hun bestaande cluster/regionale nummeringsreeks;
   - geen bestaand ID wijzigen/hergebruiken;
   - nog geen definitief nummer claimen als registercontext ontbreekt, maar exact aangeven waar append moet gebeuren.

4. `ABC_REVIEW_QUEUE.md`
   - elke nieuwe fysieke kandidaat krijgt `MARK_REVIEW_REQUIRED`;
   - bestaande B/C met sterke nabijheid/synergie tot nieuwe A-waardige of multi-person plek krijgt `REVIEW_FOR_UPGRADE`;
   - bestaande A/B/C nooit automatisch veranderen.

5. `COMPLETENESS_GATE.md`
   - definieer en pas per cluster toe:
     `LOCATION_SWEEP_DONE`, `PERSON_REVERSE_DONE`, `LOCAL_PROXIMITY_DONE`, `NEW_IDS_ASSIGNED`, `NEW_ABC_REVIEWED`, `TRAVEL_COMPLETENESS_GATE`;
   - `TRAVEL_COMPLETENESS_GATE: JA` alleen als geen bekende nieuwe persoonslocaties zonder review overblijven en een proximity-backfill is gedaan.

6. `TOP_REOPEN_PRIORITIES.md`
   - rangschik clusters op kans dat heropening de reis echt verandert: veel nieuwe locaties, multi-person overlaps, historisch verblijf/hotel, veel <=3km nabijheid, bestaande reisbasis/lock, hoge logistieke synergie.

## Toegestane bronnen
Lees bestaande clusteratlassen, A/B/C-besluiten, numbering registries, persoonsfreezes/reconciliaties, overlap/heatmap-resultaten en governance. Geen nieuwe landelijke persoonsmegasweep. Web alleen indien strikt nodig om een travel-relevante nabijheidsclaim of actuele fysieke identiteit van een reeds bekende kandidaat te verifiëren; geen brede discovery.

## Speciale aandacht
- Varanasi en andere reeds A/B/C-afgeronde clusters expliciet auditen.
- Historisch betekenisvolle hotels/verblijven waar een Top-persoon werkelijk verbleef apart markeren als `HERITAGE_STAY_CANDIDATE`.
- Exacte gedeelde sites van meerdere personen apart markeren als `MULTI_PERSON_SAME_SITE`.
- Een locatie die 100 m van een bestaande routebasis ligt mag niet verdwijnen in een generieke stadsoverlap.

## Grenzen
Geen locaties verwijderen. Geen A/B/C namens Mark. Geen route/nachten/hotelkeuze namens Mark. Geen merge/PDF. Alle uitkomsten zijn additief.

## Einde
Commit alle zes outputs en STATUS.md op dezelfde branch. Rapporteer hoeveel clusters moeten heropenen, hoeveel nieuwe fysieke kandidaten een ID + A/B/C nodig hebben, en hoeveel <=1 km / <=3 km van reeds gekozen of beoordeelde locaties liggen.
