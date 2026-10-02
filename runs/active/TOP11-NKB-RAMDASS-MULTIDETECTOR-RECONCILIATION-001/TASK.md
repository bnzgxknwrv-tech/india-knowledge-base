# CCI_TASK 095 — NKB + RAM DASS MULTIDETECTOR RECONCILIATION

STATUS: QUEUED_AFTER_094
OWNER: CCI
WORKBRANCH: claude/werk-je-nu-of-niet-oa10y7

## Voorwaarde
NIET starten zolang CCI_TASK 094 nog niet volledig is afgerond en `CCI_RESULT — CCI_TASK 094` nog niet op PR #23 staat.

## Doel
Na 094: voeg India-GEEL als derde onafhankelijke detector toe aan de bestaande CCI_TASK 091-reconciliatie voor Neem Karoli Baba en Ram Dass.

Gebruik:
- bestaande interne METHOD_V2 + ChatGPT externe reconciliatie uit CCI_TASK 091;
- India-GEEL NKB freeze SHA `4cd99f5e45266dd3de0ed487e8147fd93ca525d9`;
- India-GEEL Ram Dass freeze SHA `e1f2e4b8bb56296e20bc0d3f6a3d2fbe9b7589cb`.

Integriteitscheck beide GEEL-freezes vóór inhoudelijke vergelijking. Voer volledige bidirectionele lossless delta/reconciliatie uit, met directe bronverificatie voor betekenisvolle nieuwe delta's/conflicten. Houd exacte fysieke overlap en alleen-stad overlap apart. Update per persoon CORPUS/HOSTGRAPH/DISCOVERY/RECONCILIATION/EXTERNAL_MODEL_DIVERSITY gates en benoem travel-relevante unresolved gaps afzonderlijk van academische micro-gaps.

Geen Ramana/Ramakrishna, geen nieuwe persoonsweep, geen regio-/clusteronderzoek, geen A/B/C, route, nachten, IDs, PDF, merge of PR.

Checkpoint NKB, daarna Ram Dass. Plaats na afronding `CCI_RESULT — CCI_TASK 095` op PR #23 en stop voor INDIA-QA.
