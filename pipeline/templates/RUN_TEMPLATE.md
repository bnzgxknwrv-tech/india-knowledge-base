# Run templates

Kopieer deze structuren naar `research/active/<run-id>/`. Vervang alle `<...>`-waarden vóór activatie.

## run.yaml

```yaml
run_id: <run-id>
project: india
scope_file: research/active/<run-id>/scope.md
created_at: <ISO-8601>
created_by: <controller>
immutable_after_first_claim: true
pins:
  entrypoint: pipeline/ENTRYPOINT.md
  methodology: knowledge/methodology/METHODOLOGY_V2.md
  overlays: knowledge/project/OVERLAYS_INDIA.md
  execution_protocol: pipeline/protocols/EXECUTION_PROTOCOL.md
  context_protocol: pipeline/protocols/CONTEXT_PROTOCOL.md
  controller_transition_protocol: pipeline/protocols/CONTROLLER_TRANSITION_PROTOCOL.md
  evidence_protocol: pipeline/protocols/EVIDENCE_PROTOCOL.md
  quality_gate: pipeline/QUALITY_GATE.md
  roles:
    BRONS: pipeline/roles/BRONS.md
    ZILVER: pipeline/roles/ZILVER.md
    GOUD: pipeline/roles/GOUD.md
versions:
  pipeline: 2.1.0
  methodology: 2.0.0
source_base_commit: <commit-sha>
```

## state.yaml

```yaml
run_id: <run-id>
state: READY_FOR_BRONS
active_role: null
claim: null
last_event_id: EVT-0001
last_validated_commit: <commit-sha>
blockers: []
```

## events.jsonl

```json
{"event_id":"EVT-0001","run_id":"<run-id>","event_type":"RUN_CREATED","at":"<ISO-8601>","actor":"<controller>","from_state":null,"to_state":"READY_FOR_BRONS","commit":"<commit-sha>","notes":"Alleen BRONS_CONTEXT.yaml is uitvoerbaar aangemaakt."}
```

## context/BRONS_CONTEXT.yaml bij runcreatie

```yaml
run_id: <run-id>
role: BRONS
source_commit: <commit-sha>
protocol_versions:
  pipeline: 2.1.0
  methodology: 2.0.0
required_files:
  - pipeline/ENTRYPOINT.md
  - pipeline/roles/BRONS.md
  - knowledge/methodology/METHODOLOGY_V2.md
  - knowledge/project/OVERLAYS_INDIA.md
  - pipeline/protocols/EXECUTION_PROTOCOL.md
  - pipeline/protocols/CONTEXT_PROTOCOL.md
  - pipeline/protocols/EVIDENCE_PROTOCOL.md
  - pipeline/QUALITY_GATE.md
  - research/active/<run-id>/run.yaml
  - research/active/<run-id>/state.yaml
  - research/active/<run-id>/scope.md
optional_files: []
forbidden_files:
  - research/completed/**
  - research/active/<run-id>/ZILVER/**
  - research/active/<run-id>/GOUD/**
priority_order: []
expected_hashes: {}
maximum_context_budget:
  files: 40
  lines_per_file: 1500
predecessor_manifest: null
output_path: research/active/<run-id>/BRONS/
```

Bij runcreatie worden `ZILVER_CONTEXT.yaml` en `GOUD_CONTEXT.yaml` niet aangemaakt.

## context/ZILVER_CONTEXT.yaml na BRONS_COMPLETE

De controller genereert dit bestand pas na validatie van BRONS:

```yaml
run_id: <run-id>
role: ZILVER
source_commit: <definitieve-brons-resultaatcommit>
protocol_versions:
  pipeline: 2.1.0
  methodology: 2.0.0
required_files:
  - pipeline/ENTRYPOINT.md
  - pipeline/roles/ZILVER.md
  - knowledge/methodology/METHODOLOGY_V2.md
  - knowledge/project/OVERLAYS_INDIA.md
  - pipeline/protocols/EXECUTION_PROTOCOL.md
  - pipeline/protocols/CONTEXT_PROTOCOL.md
  - pipeline/protocols/EVIDENCE_PROTOCOL.md
  - pipeline/QUALITY_GATE.md
  - research/active/<run-id>/run.yaml
  - research/active/<run-id>/state.yaml
  - research/active/<run-id>/scope.md
  - research/active/<run-id>/BRONS/manifest.yaml
  - <alle door BRONS/manifest.yaml verplichte BRONS-artifacts>
optional_files: []
forbidden_files:
  - research/completed/**
  - research/active/<run-id>/GOUD/**
priority_order: []
expected_hashes:
  <path>: <hash>
maximum_context_budget:
  files: 80
  lines_per_file: 1500
predecessor_manifest: research/active/<run-id>/BRONS/manifest.yaml
output_path: research/active/<run-id>/ZILVER/
```

## context/GOUD_CONTEXT.yaml na ZILVER_COMPLETE

De controller genereert dit bestand pas na validatie van ZILVER. Het is gepind op de definitieve ZILVER-resultaatcommit en bevat alle verplichte ZILVER-artifacts plus alleen expliciet benodigde BRONS-artifacts voor verliescontrole.

## Fase manifest.yaml

```yaml
run_id: <run-id>
role: <ROLE>
source_commit: <commit-sha>
result_status: <PASS|PARTIAL|BLOCKED>
protocol_versions:
  pipeline: 2.1.0
  methodology: 2.0.0
required_outputs:
  - report/INDEX.md
  - claims.jsonl
  - sources/registry.jsonl
  - sources/rejected.jsonl
  - audit.md
  - handoff.yaml
  - COMPLETED
artifacts: []
validation:
  all_required_exist: false
  all_sentinels_present: false
  references_valid: false
  reread_complete: false
```

## report/INDEX.md

```markdown
# <ROLE> report index

Lees in deze volgorde:
1. 01_scope_and_counts.md
2. 02_candidates_01.md
3. 03_outside_list_and_overlays.md
4. 04_uncertainties_and_duplicates.md
5. 05_ashrams_and_living_practice.md
6. 06_conclusion_and_gate.md

END_OF_ARTIFACT
```

## handoff.yaml

```yaml
run_id: <run-id>
completed_role: <ROLE>
result_status: <PASS|PARTIAL|BLOCKED>
output_manifest: research/active/<run-id>/<ROLE>/manifest.yaml
next_role: <ZILVER|GOUD|REGISSEUR>
next_expected_transition: <TRANSITION_TO_ZILVER|TRANSITION_TO_GOUD|NONE>
open_blockers: []
required_predecessor_files: []
```

De worker vult geen toekomstige `source_commit` in. De controller stelt die na de definitieve fasecommit vast.

## COMPLETED

```text
RUN_ID=<run-id>
ROLE=<ROLE>
STATUS=<PASS|PARTIAL|BLOCKED>
SOURCE_COMMIT=<sha-waarop-de-fase-begon>
OUTPUT_MANIFEST=<path>
VALIDATED=true
END_OF_ARTIFACT
```

END_OF_ARTIFACT