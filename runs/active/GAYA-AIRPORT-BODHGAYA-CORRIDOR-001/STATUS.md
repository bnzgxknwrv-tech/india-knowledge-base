# STATUS — GAYA-AIRPORT-BODHGAYA-CORRIDOR-001

```
task_id: GAYA-AIRPORT-BODHGAYA-CORRIDOR-001
state: TASK_VASTGELEGD -- SWEEP A NOG NIET UITGEVOERD
task_file: runs/active/GAYA-AIRPORT-BODHGAYA-CORRIDOR-001/TASK.md
status_file: runs/active/GAYA-AIRPORT-BODHGAYA-CORRIDOR-001/STATUS.md
result_file: runs/active/GAYA-AIRPORT-BODHGAYA-CORRIDOR-001/RESULT.md (nog niet aangemaakt --
  ontstaat zodra Sweep A wordt uitgevoerd)
last_updated: 2026-08-08
last_updated_by: CCI (RELAY-MIGRATION-001)
```

**blockers**: geen.

**next_allowed_step**: CCI voert Sweep A uit volgens `TASK.md` (AOAY-corridorsweep, elk
Top-11-lid apart, laag-3-heavyweights, poort G.1-bronverificatie) en legt het resultaat vast in
een nieuw `RESULT.md` volgens de verplichte outputvelden in `TASK.md`. Daarna: STOP, geen
PRE_PDF_CONTENT, geen PDF, geen A/B/C. Pas daarna voert INDIA onafhankelijk Sweep B uit.

**Korte startzin voor CCI** (kopieerbaar, om Sweep A alsnog te starten):
`Voer Sweep A uit voor GAYA-AIRPORT-BODHGAYA-CORRIDOR-001 volgens runs/active/GAYA-AIRPORT-BODHGAYA-CORRIDOR-001/TASK.md.`

**Korte startzin voor INDIA** (kopieerbaar, ná Sweep A, om Sweep B te starten):
`Lees runs/active/GAYA-AIRPORT-BODHGAYA-CORRIDOR-001/RESULT.md (Sweep A) en voer onafhankelijk
Sweep B uit volgens TASK.md, zonder CCI's kandidatenlijst als zoekbasis.`

---
Dit bestand is de kortste, altijd-actuele bron van waarheid voor deze taak (poort O.1) — een
nieuwe sessie hoeft alleen dit bestand + `TASK.md` te lezen, niet de volledige PR #23-geschiedenis.
