# TASK — TOP11-RAMANA-RAMAKRISHNA-V2-PRE-EXTERNAL-001

```
task_id: TOP11-RAMANA-RAMAKRISHNA-V2-PRE-EXTERNAL-001
cci_task: CCI_TASK 093
issued_by: INDIA8
issued_at: 2026-08-19
state: READY_FOR_CCI
mode: METHOD_V2 PRE-EXTERNAL BLIND
```

## Doel
Maak vanaf nul twee landelijke corpus-first METHOD_V2 PRE-EXTERNAL freezes, in deze vaste volgorde:

1. Ramana Maharshi
2. Ramakrishna

Heel India; geen regionale beperking.

## HARD BLINDNESS
Totdat de freeze van de betreffende persoon duurzaam gecommit is, mag CCI GEEN inhoud lezen uit:
- `agent/chatgpt-top11-parallel-sweep`;
- `agent/indiageel-ramana-ramakrishna-sweep`;
- de India GEEL Ramana/Ramakrishna-freezes;
- oude METHOD_V1/PHASE2 kandidatenlijsten als discoverychecklist;
- externe unions/reconciliaties voor deze personen;
- regionale/clusterbestanden die locatie-antwoorden kunnen zaaien.

Blindheid per persoon apart bevestigen in de freeze.

## METHOD_V2 VERPLICHT
Per persoon:
1. corpus inventory;
2. lossless corpus occurrence extraction;
3. event/place normalization;
4. host/network graph;
5. brede web discovery na corpuspass;
6. spelling-/historische-naamvarianten en relevante meertalige routes;
7. directe bronverificatie waar praktisch mogelijk;
8. expliciete blockers + saturation attempts.

Zoek ook micro-sites: huizen, kamers, scholen, stations, hotels, ziekenhuizen, ghats, tempels, caves, tuinen, routes, hosthuizen, retreats en andere fysieke sublocaties.

Geen plaats afleiden uit context of een genoemde andere persoon. PERSONALLY_PRESENT expliciet scheiden van context-only.

## Output
Schrijf per persoon een eigen bestand onder deze taakmap:
- `RAMANA_MAHARSHI_V2_PRE_EXTERNAL_FREEZE.md`
- `RAMAKRISHNA_V2_PRE_EXTERNAL_FREEZE.md`

Minimaal opnemen:
- CORPORA_SEARCHED
- SOURCE_ACCESS_BLOCKERS
- HOSTGRAPH_SEARCHED
- DISCOVERY_SEARCH_FAMILIES
- NORMALIZED_RECORDCOUNT
- LOCATION_RECORDS
- CONFLICTS
- UNRESOLVED_LEADS
- gate-statussen
- PERSON_SWEEP_SATURATED: JA/NEE
- BLINDNESS_CONFIRMED

## Duurzaam checkpointen
Commit Ramana onmiddellijk zodra die freeze klaar is. Ga pas daarna naar Ramakrishna. Commit Ramakrishna afzonderlijk. Laat lang werk nooit ongecommit liggen.

## Na beide freezes
Stop. Open GEEN externe ChatGPT-freeze en GEEN India GEEL-freeze. Geen vergelijking/reconciliatie in deze taak.

Plaats `CCI_RESULT — CCI_TASK 093` op PR #23 met:
- beide commit-SHA's;
- recordcounts;
- blockers/gates;
- saturationstatus;
- bevestiging blindheid;
- next_allowed_step = INDIA-QA en daarna aparte multi-detector-reconciliatie.

## HARD HOLDS
Geen Core-Kriya-heronderzoek; geen NKB/Ram Dass; geen cluster/regio/heatmap; geen A/B/C; geen permanente IDs; geen PDF; geen route; geen merge.