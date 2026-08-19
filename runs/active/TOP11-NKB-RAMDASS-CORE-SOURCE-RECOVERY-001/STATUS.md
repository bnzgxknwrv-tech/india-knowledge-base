# STATUS — TOP11-NKB-RAMDASS-CORE-SOURCE-RECOVERY-001

```
task_id: TOP11-NKB-RAMDASS-CORE-SOURCE-RECOVERY-001
cci_task: CCI_TASK 090
state: AFGEROND__WACHT_OP_INDIA_QA
issued_at: 2026-08-19
issued_by: INDIA7
completed_at: 2026-08-19
completed_by: CCI
target_branch: claude/werk-je-nu-of-niet-oa10y7
task_file: runs/active/TOP11-NKB-RAMDASS-CORE-SOURCE-RECOVERY-001/TASK.md
status_file: runs/active/TOP11-NKB-RAMDASS-CORE-SOURCE-RECOVERY-001/STATUS.md
result_file: runs/active/TOP11-NKB-RAMDASS-CORE-SOURCE-RECOVERY-001/SOURCE_RECOVERY_RESULT.md
checkpoint_commits: 76020b9 (NKB source-recovery), 0f7a099 (Ram Dass source-recovery)
```

## Aanleiding

CCI_TASK 089 leverde verse blinde freezes op, maar de belangrijkste corpusbronnen waren niet
doorzoekbaar: *Miracle of Love*, *By His Grace*, *Be Here Now* en de bedoelde
*Sacred Wanderer*/Ram-Dass-kernbiografie. Daardoor bleef `CORPUS_COVERAGE_GATE: NEE` voor beide
personen en telde Ram Dass slechts vijf records.

## Scope

Gerichte legale bronherstelpoging plus lossless extractie uit ieder toegankelijk deel. Geen brede
discovery en geen externe vergelijking.

## Blindheid

Externe NKB/Ram-Dass-freezes en IndiaROOD blijven gesloten.

## Resultaat

- *Miracle of Love* en *By His Grace*: beide `BRON_GEBLOKKEERD` na hernieuwde legale routepogingen.
- *Be Here Now*: `FULL` hersteld (volledig open archive.org "Community Texts"-item) en corpusbreed
  doorzocht — 8 nieuwe locatie-occurrences (2 gedeeld met Neem Karoli Baba, 8 voor Ram Dass zelf).
- Titelcorrectie: "Sacred Wanderer" (Ravi Dass) was een verwisseling; correcte bron is
  "Being Ram Dass" (2021) — één fragment (Tricycle) hersteld, `PARTIAL`.
- Neem Karoli Baba: 19 → 21 records; `NEEM_KAROLI_BABA_V2_PRE_EXTERNAL_SATURATED: NEE` (ongewijzigd).
- Ram Dass: 5 → 13 records + 1 naamsbevestiging; CORPUS-COVERAGE-GATE NEE → DEELS;
  `RAM_DASS_V2_PRE_EXTERNAL_SATURATED: NEE` (ongewijzigd — eerlijke uitkomst, corpus nog niet
  uitputtend).

## next_allowed_step

CCI heeft `TASK.md` uitgevoerd, per persoon gecheckpoint (76020b9, 0f7a099), en stopt na de
resultaatenvelop op PR #23. INDIA beslist tussen (a) nog één gerichte corpuspass — met name
"Being Ram Dass" (2021) volledig bereiken en/of maharajji.love doorzoeken — of (b) externe lossless
reconciliatie starten met de bestaande `agent/chatgpt-top11-parallel-sweep`-freezes, analoog aan
CCI_TASK 088. Ramana Maharshi/Ramakrishna blijven niet gestart.
