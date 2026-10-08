# KUMAON — DEEP RESEARCH / SWEEP-B STATE

```
region_task: KUMAON-V2-RESWEEP-001
updated: 2026-08-14
state: CCI_SWEEP_A_KLAAR__INDIA_SWEEP_B_FROZEN__READY_FOR_RECONCILIATION
```

## Huidige status

`runs/active/KUMAON-V2-RESWEEP-001/STATUS.md` meldt:

- `state: SWEEP_A_KLAAR_WACHT_OP_INDIA_SWEEP_B`
- CCI Sweep A is uitgevoerd.
- CCI heeft Mark’s voorkeur voor `KUM-SWEEP-A-001` vastgelegd: Mahavatar Babaji-grot = A zodra de fysieke identiteit na reconciliatie vaststaat.

INDIA heeft Sweep B al parallel en blind uitgevoerd vóór inzage in CCI `RESULT.md` of legacy Kumaon-kandidaten.

## Frozen INDIA Sweep B

- Branch: `india/kumaon-v2-sweep-b-001`
- Bestand: `runs/active/KUMAON-V2-RESWEEP-001/INDIA_SWEEP_B.md`
- Freeze-commit: `41bd4a7caebe83e44b9ee2470ecf1212d5111d9e`
- Status: `SWEEP_B_FROZEN_BLIND`

Deze Sweep B mag nu wél gebruikt worden voor reconciliatie, omdat CCI Sweep A inmiddels volgens `STATUS.md` klaar is.

## Diepgaand-onderzoek-app

De deep-research app is gestart als extra kwaliteitscontrole/audit voor Kumaon, niet als vervanging van CCI Sweep A of INDIA Sweep B.

Behandeling:

- Gebruik deep-research-output uitsluitend als extra bron-/gatendetector.
- Laat deep-research geen Mark-besluiten overschrijven.
- Laat deep-research geen CCI/INDIA-sweep vervangen.
- Nieuwe claims uit deep-research moeten dezelfde bronverificatie doorlopen als andere keuze-relevante claims.

## Mark-besluit Babaji-grot

Zie apart bestand:

`research/deep-research/MAHAVATAR-BABAJI-CAVE-A.md`

Kern: Mahavatar Babaji-grot = A voor Mark zodra de fysieke identiteit is gereconcilieerd. Niet opnieuw aan Mark vragen tenzij er een echte fysieke identiteitsbotsing is.

## Reconciliatie-volgorde nu

1. CCI opent zijn eigen `RESULT.md` van Sweep A.
2. CCI opent `INDIA_SWEEP_B.md` van branch `india/kumaon-v2-sweep-b-001` op commit `41bd4a7caebe83e44b9ee2470ecf1212d5111d9e`.
3. CCI vergelijkt A vs B.
4. Pas daarna opent CCI legacy `KUMAON-COMPLETE-001` / oude Kumaon-data als benchmark.
5. CCI maakt de verplichte tabellen:
   - `NIEUW_INTERSECT_OUD`
   - `NIEUW_MIN_OUD`
   - `OUD_MIN_NIEUW`
   - `BRON_CONFLICTEN`
   - `MARK_BESLUIT_CONFLICTEN`
6. CCI verifieert de Babaji-grot-identiteit en koppelt Mark’s A aan de correcte permanente fysieke locatie.
7. Geen PDF, geen routeplanning, geen andere A/B/C-voorspellingen.

## Volgende output die verwacht wordt

CCI levert een reconciliatie-resultaat met:

- commit;
- gereconcilieerde kandidaatset;
- welke tijdelijke IDs bij elkaar horen;
- legacy match/mismatch;
- fysieke Babaji-grot mapping;
- welke plekken keuze-ready zijn;
- welke echte conflicten eventueel nog Mark nodig hebben.
