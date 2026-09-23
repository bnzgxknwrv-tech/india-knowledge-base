# TASK — TOP11-CORE-KRIYA-INDIAROOD-DELTA-RECONCILIATION-001

```
task_id: TOP11-CORE-KRIYA-INDIAROOD-DELTA-RECONCILIATION-001
cci_task: CCI_TASK 092
issued_by: INDIA8
issued_at: 2026-08-19
target_branch: claude/werk-je-nu-of-niet-oa10y7
state_on_issue: READY_FOR_CCI
pdf_status: VERBODEN
```

## 1. Doel

Sluit de nog open derde-detector-gate van CCI_TASK 088 door de drie reeds duurzaam gefreezede onafhankelijke IndiaROOD Core-Kriya-sweeps lossless te reconciliëren met de bestaande CCI_TASK 088-resultaten voor:

1. Mahavatar Babaji
2. Lahiri Mahasaya
3. Sri Yukteswar

Dit is GEEN nieuwe discovery-sweep. De drie IndiaROOD-freezes bestaan al en mogen niet opnieuw worden uitgevoerd.

## 2. Verplichte input — exacte freezes

Branch: `agent/indiarood-core-kriya-sweep`

- Babaji
  - commit: `f9e7e25bec3716687f5fd2562c119baf31ea22ef`
  - file: `runs/active/TOP11-INDIAROOD-BLIND-SWEEP-001/BABAJI_INDIAROOD_FREEZE.md`
- Lahiri Mahasaya
  - commit: `fc8418b8785cdd22edd389f0a461586ce239ff17`
  - file: `runs/active/TOP11-INDIAROOD-BLIND-SWEEP-001/LAHIRI_MAHASAYA_INDIAROOD_FREEZE.md`
- Sri Yukteswar
  - commit: `6f71180a1a4cf6666088ae450a6cedb13052552e`
  - file: `runs/active/TOP11-INDIAROOD-BLIND-SWEEP-001/SRI_YUKTESWAR_INDIAROOD_FREEZE.md`

Controleer vóór inhoudelijke vergelijking dat deze exacte commit/file-combinaties bestaan en leg de blob-SHA/integriteitscheck vast.

Gebruik daarnaast volledig de bestaande CCI_TASK 088-output:

- `runs/active/TOP11-CORE-KRIYA-RECONCILIATION-001/BABAJI_RECONCILIATION.md`
- `runs/active/TOP11-CORE-KRIYA-RECONCILIATION-001/LAHIRI_MAHASAYA_RECONCILIATION.md`
- `runs/active/TOP11-CORE-KRIYA-RECONCILIATION-001/SRI_YUKTESWAR_RECONCILIATION.md`
- `runs/active/TOP11-CORE-KRIYA-RECONCILIATION-001/RECONCILIATION_MATRIX.jsonl`
- `runs/active/TOP11-CORE-KRIYA-RECONCILIATION-001/RECONCILIATION_RESULT.md`

De interne pre-external freezes en externe ChatGPT-freezes die in 088 zijn gebruikt blijven onderdeel van de provenance; niet opnieuw vanaf nul onderzoeken.

## 3. Canonieke Babaji-regel — HARD

Lees vóór Babaji-reconciliatie:
`decisions/BABAJI_MYTHIC_FIGURE_EVIDENCE_RULE_2026-08-19.md`.

Voor ieder Babaji-record blijven de assen strikt gescheiden:
- `TRADITION_CLAIM_DOCUMENTED`
- `PHYSICAL_SITE_IDENTITY`
- `HISTORICALLY_VERIFIED_BABAJI_PRESENCE: NIET_VASTSTELBAAR`

Een IndiaROOD- of lineage-claim mag nooit worden opgewaardeerd tot historisch bewezen fysieke aanwezigheid van Babaji. Verschillende Babaji-identiteitstradities niet stil samenvoegen.

## 4. Reconciliatiemethode

Werk per persoon, met checkpointcommit na elke persoon.

Voor ieder IndiaROOD-record bepaal minimaal:
- `MATCH_EXISTING`
- `INDIAROOD_MORE_GRANULAR`
- `INDIAROOD_ONLY_CLAIM`
- `CONFLICT`
- `DUPLICATE_DIFFERENT_LABEL`
- `NEGATIVE/CONTEXT_ONLY`
- `UNRESOLVED`

En omgekeerd: controleer welke bestaande 088-records/claims door IndiaROOD NIET zijn gevonden. Het doel is bidirectioneel detectorgedrag vastleggen, niet alleen IndiaROOD importeren.

Voor iedere betekenisvolle IndiaROOD-only, 088-only of conflictclaim:
1. verifieer rechtstreeks tegen de aangehaalde primaire/semi-primaire/lineage-bron waar praktisch mogelijk;
2. label bronstatus (`VERIFIED_TRUE`, `VERIFIED_FALSE`, `PARTIALLY_TRUE`, `UNRESOLVED`, `BRON_GEBLOKKEERD`);
3. corrigeer bestaande 088-output alleen met expliciete delta/provenance — geen stille overschrijving;
4. registreer hallucinaties, naamcollisies, overmerges en locatie-identiteitsfouten expliciet.

## 5. Verplichte output

Maak:
- `runs/active/TOP11-CORE-KRIYA-INDIAROOD-DELTA-RECONCILIATION-001/BABAJI_INDIAROOD_DELTA.md`
- `runs/active/TOP11-CORE-KRIYA-INDIAROOD-DELTA-RECONCILIATION-001/LAHIRI_MAHASAYA_INDIAROOD_DELTA.md`
- `runs/active/TOP11-CORE-KRIYA-INDIAROOD-DELTA-RECONCILIATION-001/SRI_YUKTESWAR_INDIAROOD_DELTA.md`
- `runs/active/TOP11-CORE-KRIYA-INDIAROOD-DELTA-RECONCILIATION-001/INDIAROOD_DELTA_MATRIX.jsonl`
- `runs/active/TOP11-CORE-KRIYA-INDIAROOD-DELTA-RECONCILIATION-001/RECONCILIATION_RESULT.md`
- `runs/active/TOP11-CORE-KRIYA-INDIAROOD-DELTA-RECONCILIATION-001/STATUS.md`

Werk daarnaast de relevante status/governance duurzaam bij, minimaal:
- `runs/active/TOP11-CORE-KRIYA-RECONCILIATION-001/STATUS.md`
- `runs/active/TOP11-INDIA-PERSON-CENTRIC-MEGASWEEP-001/STATUS.md`
- `governance/INDIA_SESSION_START.md`

## 6. Verplichte eindbeoordeling per persoon

Rapporteer:
- aantal bestaande 088-records/claims;
- aantal IndiaROOD-records;
- matches;
- IndiaROOD-only;
- 088-only;
- more-granular;
- conflicten;
- rechtstreeks bevestigde correcties;
- afgewezen claims/hallucinaties;
- resterende bronblokkades;
- actuele METHOD_V2-gates;
- of `RECONCILIATION_GATE` nu van `PROVISIONEEL` naar `JA/DEELS/NEE` kan;
- eerlijke saturationstatus.

`SATURATED: JA` alleen wanneer alle vereiste gates aantoonbaar dicht zijn. Geen cosmetische JA.

## 7. Checkpoints

1. Babaji volledig afmaken + commit.
2. Lahiri Mahasaya volledig afmaken + commit.
3. Sri Yukteswar volledig afmaken + commit.
4. Finale matrix/status/governance commit indien nodig.

Bij contextverlies hervat vanaf het laatste duurzame checkpoint.

## 8. NKB/Ram Dass

CCI_TASK 091 is door INDIA8 inhoudelijk geaccepteerd als voldoende om door te gaan. Het open NKB-conflict over de exacte laatste-reisvolgorde/Mathura-tussenstop blijft geregistreerd maar blokkeert deze taak niet. Niet opnieuw onderzoeken binnen 092.

## 9. Harde grenzen

- Geen nieuwe IndiaROOD-sweep.
- Geen nieuwe externe ChatGPT-sweep.
- Geen Ramana Maharshi/Ramakrishna in deze taak.
- Geen AOAY-brede vervolgsweep.
- Geen cluster/regio/heatmap.
- Geen A/B/C namens Mark.
- Geen permanente IDs.
- Geen PDF.
- Geen route/nachten/vervoer.
- Geen merge van externe branches of PR #24.

## 10. Stopvoorwaarde

Stop zodra alle drie IndiaROOD-freezes volledig bidirectioneel tegen CCI_TASK 088 zijn gereconcilieerd, betekenisvolle verschillen bronmatig zijn beoordeeld en de gates per persoon opnieuw zijn vastgesteld.

Plaats daarna één PR #23-envelop met kop:
`CCI_RESULT — CCI_TASK 092`

Vermeld checkpointcommits, recorddelta's, correcties/hallucinaties, gate-uitkomst, resterende blockers en exact `next_allowed_step`.
