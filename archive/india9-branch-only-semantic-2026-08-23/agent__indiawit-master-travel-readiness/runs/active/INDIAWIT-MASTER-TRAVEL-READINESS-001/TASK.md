# INDIA WIT — MASTER TRAVEL READINESS INTEGRATION

STATUS: READY
OWNER: INDIA WIT
MODE: CROSS-BRANCH INTEGRATOR
GOAL: combineer alle afgeronde parallelle werkstromen tot één actuele brug van onderzoek naar reisplanning, zonder zelf nieuwe persoonslocaties te onderzoeken en zonder A/B/C-keuzes namens Mark te maken.

## Bronnen die WIT WEL mag lezen
Lees de actuele outputbestanden van deze branches/taken:
- agent/indiaorange-travel-heatmap-prep
- agent/indiablauw-trip-ops-prep
- agent/indiapaars-decision-rubric-prep
- agent/indiaroze-route-builder-prep
- agent/indiaturquoise-allperson-overlap
- agent/indiageel-ramana-ramakrishna-sweep (alleen POST-FREEZE/targeted/overlap-output; blindheid is al afgesloten)
- claude/werk-je-nu-of-niet-oa10y7 voor CCI-resultaten t/m CCI_TASK 094; neem CCI_TASK 095 alleen mee indien CCI_RESULT 095 inmiddels duurzaam bestaat op het moment van uitvoering.
- relevante governance/decisions voor LOCKED_BY_MARK en harde projectgrenzen.

## Opdracht
Maak vijf outputs:
1. MASTER_TRAVEL_READINESS.md
   - per persoonslaag: voldoende voor travel-planning JA/NEE/DEELS; academische restgaten apart;
   - per cluster/regio: huidige minimum-confirmed overlap, evidence maturity, exact-site density, travel-readiness;
   - expliciet kritisch pad vanaf NU tot complete A-Z reis.

2. MASTER_HEATMAP_INPUT.md
   - één geconsolideerde, lossless input voor de echte landelijke heatmap;
   - markeer voorlopige tellingen als MIN_CONFIRMED;
   - scheid city overlap, region overlap en exact same-site overlap;
   - neem Arunachala/Tiruvannamalai LOCKED_BY_MARK A-anker en Kukuchina/Dunagiri hoofdreden apart op zonder ze te herwaarderen.

3. HIGH_IMPACT_GAPS.md
   - alleen gaten die redelijkerwijs een bestemmingskeuze, clusterprioriteit, aantal nachten, vervoer of boekingsrisico kunnen veranderen;
   - obscure academische microgaten die de reis niet beïnvloeden in aparte NON_BLOCKING-sectie;
   - maximaal 10 echte high-impact gaten, liefst minder.

4. MARK_DECISION_QUEUE_DRAFT.md
   - bundel toekomstige keuzes in zo weinig mogelijk beslismomenten;
   - nog GEEN keuze namens Mark;
   - ontwerp batches, bijvoorbeeld cluster-keuze, intensiteit per cluster, comfort/logistiek, zodat Mark niet tientallen losse A/B/C's hoeft te beantwoorden.

5. NEXT_EXECUTION_MAP.md
   - exacte paralleliseerbare stappen na deze taak;
   - wat kan al vóór CCI 095 klaar is;
   - wat wordt direct ontgrendeld na CCI 095;
   - wanneer regionale deep sweeps werkelijk nodig zijn versus wanneer we direct naar route kunnen.

## Harde grenzen
- Geen nieuw webonderzoek naar persoonslocaties.
- Geen nieuwe personen-sweeps.
- Geen A/B/C namens Mark.
- Geen hotels kiezen.
- Geen nachten of route definitief vastzetten.
- Geen PDF.
- Geen merge/PR.
- Geen permanente locatie-ID's.
- Onzekerheid niet verbergen; gebruik PROVISIONEEL/MIN_CONFIRMED waar nodig.

## Outputlocatie
Schrijf alle vijf bestanden onder:
runs/active/INDIAWIT-MASTER-TRAVEL-READINESS-001/

Werk STATUS.md bij naar COMPLETE en commit alles op agent/indiawit-master-travel-readiness.
