# TASK — TOP11-RAMANA-RAMAKRISHNA-MULTIDETECTOR-RECONCILIATION-001

```
task_id: TOP11-RAMANA-RAMAKRISHNA-MULTIDETECTOR-RECONCILIATION-001
cci_task: CCI_TASK 094
owner: CCI
issued_by: INDIA8
issued_at: 2026-08-19
state: READY_FOR_CCI
```

## Doel
Sluit de landelijke deep-person detectorreconciliatie voor:
1. Ramana Maharshi
2. Ramakrishna

Voer per persoon een volledige lossless driewegsreconciliatie uit tussen:
A. de zojuist in CCI_TASK 093 bevroren interne METHOD_V2 PRE-EXTERNAL freeze;
B. de reeds vóór vergelijking bevroren externe ChatGPT-freeze op `agent/chatgpt-top11-parallel-sweep`;
C. de onafhankelijke India-GEEL PRE-COMPARE freeze op `agent/indiageel-ramana-ramakrishna-sweep`.

## Bevroren input
Interne CCI 093:
- Ramana checkpoint `6e3f939`, 23 records.
- Ramakrishna checkpoint `12e99c1`, 19 records.

Externe ChatGPT branch:
- `runs/active/TOP11-PARALLEL-CHATGPT-SWEEP-001/RAMANA_MAHARSHI_PRE_COMPARE_FREEZE.md` — eerder gerapporteerd 103 records.
- `runs/active/TOP11-PARALLEL-CHATGPT-SWEEP-001/RAMAKRISHNA_PRE_COMPARE_FREEZE.md` — eerder gerapporteerd 175 records.
Controleer vóór inhoudelijke vergelijking de actuele blob/commit-identiteit en leg die vast.

India GEEL branch `agent/indiageel-ramana-ramakrishna-sweep`:
- `runs/active/TOP11-INDIAGEEL-BLIND-SWEEP-001/RAMANA_MAHARSHI_INDIAGEEL_FREEZE.md`, freeze-commit `0da6c2d0c54d6caf181e8e6fadcf6df863121e2d`, 51 records.
- `runs/active/TOP11-INDIAGEEL-BLIND-SWEEP-001/RAMAKRISHNA_INDIAGEEL_FREEZE.md`, freeze-commit `693ddc00660e88030d52564362f3eb2a8af3d9cd`, 55 records.

## Methode
Per persoon:
1. integriteitscheck van alle drie freezes;
2. normaliseer identiteit zonder lossless detail te verliezen;
3. label iedere claim minimaal als MATCH / INTERNAL_ONLY / CHATGPT_ONLY / INDIAGEEL_ONLY / GRANULARITY / CONFLICT / FALSE_OR_UNSUPPORTED / SOURCE_BLOCKED;
4. verifieer betekenisvolle delta's, conflicten en verrassende micro-sites rechtstreeks tegen primaire/semi-primaire bronnen waar praktisch mogelijk;
5. neem geen locatie over enkel omdat twee AI-detectoren hetzelfde zeggen;
6. behoud onzekerheid en historische-vs-huidige fysieke identiteit expliciet;
7. update gates: CORPUS_COVERAGE, HOSTGRAPH, DISCOVERY, RECONCILIATION, EXTERNAL_MODEL_DIVERSITY;
8. geef eerlijk SATURATED JA/NEE en vermeld exact wat nog ontbreekt.

Checkpoint eerst Ramana duurzaam, daarna Ramakrishna duurzaam.

## Specifieke controles
Ramana: besteed extra aandacht aan de 1896 Madurai→Tiruvannamalai reis, Tiruvannamalai/Arunachala micro-sites, vroege caves/temple sub-sites, familie/schoolhuizen en claims van reizen buiten Arunachala na 1896.

Ramakrishna: besteed extra aandacht aan Kamarpukur/Jayrambati micro-sites, de grote 1868-pelgrimage, Navadvip/Kalna, Panihati, Kolkata privé-hosthuizen en property-identiteit, Dakshineswar sub-sites, Shyampukur/Cossipore en postume instellingen die niet als persoonlijke aanwezigheid mogen worden meegeteld.

## Output
Maak minimaal:
- `RAMANA_MAHARSHI_MULTIDETECTOR_RECONCILIATION.md`
- `RAMAKRISHNA_MULTIDETECTOR_RECONCILIATION.md`
- `RECONCILIATION_MATRIX.jsonl`
- `RECONCILIATION_RESULT.md`
- update `STATUS.md`

Rapporteer per persoon recorddelta's, nieuwe bewezen locaties, afgewezen claims, conflicten, granulariteitswinsten, gate-status en resterende blockers.

## Grenzen
Geen NKB/Ram Dass in deze taak. Geen regio-/clustersweep, geen heatmap, geen A/B/C namens Mark, geen permanente IDs, geen PDF, geen route/nachten/hotels. Externe branches alleen lezen; niet wijzigen/mergen. PR #24 niet aanpassen.

## next_allowed_step
Na afronding `CCI_RESULT — CCI_TASK 094` op PR #23 en STOP voor INDIA-QA. INDIA8 bepaalt daarna direct of de landelijke deep-personlaag voldoende gesloten is voor een voorlopige landelijke clusterheatmap, dan wel of eerst de inmiddels beschikbare India-GEEL NKB/Ram-Dass-delta moet worden gereconcilieerd.
