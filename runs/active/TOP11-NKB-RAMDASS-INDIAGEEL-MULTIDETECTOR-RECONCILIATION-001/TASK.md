# CCI_TASK 095 — NKB + RAM DASS INDIA-GEEL MULTIDETECTOR RECONCILIATION

STATUS: READY_FOR_CCI
OWNER: CCI
WORKBRANCH: claude/werk-je-nu-of-niet-oa10y7

## Doel
Voer een lossless derde-detector-reconciliatie uit voor Neem Karoli Baba en Ram Dass, voortbouwend op CCI_TASK 091.

Per persoon vergelijk je drie lagen:
1. interne CCI/METHOD_V2 + CCI_TASK 091-reconciliatiebasis;
2. bevroren externe ChatGPT-parallel-sweep;
3. bevroren India-GEEL PRE-COMPARE freeze.

India-GEEL inputs:
- NKB: `runs/active/TOP11-INDIAGEEL-NKB-BLIND-SWEEP-001/NEEM_KAROLI_BABA_INDIAGEEL_FREEZE.md`, commit `4cd99f5e45266dd3de0ed487e8147fd93ca525d9` op `agent/indiageel-ramana-ramakrishna-sweep`.
- Ram Dass: `runs/active/TOP11-INDIAGEEL-RAMDASS-BLIND-SWEEP-001/RAM_DASS_INDIAGEEL_FREEZE.md`, commit `e1f2e4b8bb56296e20bc0d3f6a3d2fbe9b7589cb` op dezelfde branch.

## Verplicht
- Integriteitscheck van beide India-GEEL commits/blobs vóór inhoudelijk openen.
- Bidirectionele mapping: GEEL↔091 basis, plus detectie van GEEL-only, basis-only, granulaire matches en conflicten.
- Directe bronverificatie voor travel-relevante nieuwe locaties, same-site claims en echte conflicten waar praktisch mogelijk.
- Preserveer het bestaande NKB laatste-reis/doodsvolgordeconflict expliciet als het niet hard oplosbaar is.
- Geen unsupported claims overnemen.
- Werk per persoon met checkpoint-commit: eerst NKB, daarna Ram Dass, daarna finale status/resultaat.
- Maak expliciet welke gates na deze derde detector voldoende zijn voor TRAVEL-READINESS, ook wanneer `PERSON_SWEEP_SATURATED: NEE` blijft.
- Onderscheid academische onvolledigheid van travel-relevante blockers.

## Outputs
Onder deze taakmap minimaal:
- `NEEM_KAROLI_BABA_INDIAGEEL_RECONCILIATION.md`
- `RAM_DASS_INDIAGEEL_RECONCILIATION.md`
- `TRAVEL_READINESS_GATE.md`
- `RECONCILIATION_RESULT.md`
- bijgewerkte `STATUS.md`

## Grenzen
Geen regio-sweep, heatmap, A/B/C, route/nachten/hotels, IDs, PDF of merge. Geen nieuwe taak starten na resultaat.

## next_allowed_step
Na afronding: plaats `CCI_RESULT — CCI_TASK 095` op PR #23 en stop voor INDIA-QA.
