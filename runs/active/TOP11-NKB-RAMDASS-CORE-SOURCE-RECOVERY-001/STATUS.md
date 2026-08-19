# STATUS — TOP11-NKB-RAMDASS-CORE-SOURCE-RECOVERY-001

```
task_id: TOP11-NKB-RAMDASS-CORE-SOURCE-RECOVERY-001
cci_task: CCI_TASK 090
state: READY_FOR_CCI__TARGETED_CORE_SOURCE_RECOVERY
issued_at: 2026-08-19
issued_by: INDIA7
target_branch: claude/werk-je-nu-of-niet-oa10y7
task_file: runs/active/TOP11-NKB-RAMDASS-CORE-SOURCE-RECOVERY-001/TASK.md
status_file: runs/active/TOP11-NKB-RAMDASS-CORE-SOURCE-RECOVERY-001/STATUS.md
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

## next_allowed_step

CCI voert uitsluitend `TASK.md` uit, commit per persoon en stopt na de resultaatenvelop. Daarna
beslist INDIA tussen nog één gerichte corpuspass of externe lossless reconciliatie.
