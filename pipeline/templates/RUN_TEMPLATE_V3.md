# Run template v3 — toekomstige plaats-sweeps

Gebruik dit uitsluitend voor nieuwe runs na INDIA2-validatie van pipeline 3.0.0.

## run.yaml kern

```yaml
run_id: <RUN_ID>
project: india
run_type: <CLUSTER_SWEEP|TARGETED_SUPPLEMENT>
scope_file: research/active/<RUN_ID>/scope.md
created_at: <ISO8601>
created_by: SUBREGIE_INDIA
immutable_after_first_claim: true
operating_mode: CONTROLLED_MANUAL_FAST
pins:
  entrypoint: pipeline/ENTRYPOINT.md
  methodology: knowledge/methodology/METHODOLOGY_V2.md
  evidence_protocol: pipeline/protocols/EVIDENCE_PROTOCOL.md
  quality_gate: pipeline/QUALITY_GATE.md
  execution_protocol: pipeline/protocols/EXECUTION_PROTOCOL.md
  context_protocol: pipeline/protocols/CONTEXT_PROTOCOL.md
  controller_transition_protocol: pipeline/protocols/CONTROLLER_TRANSITION_PROTOCOL.md
  self_routing_protocol: pipeline/protocols/SELF_ROUTING_PROTOCOL.md
  roles:
    BRONS: pipeline/roles/BRONS.md
    ZILVER: pipeline/roles/ZILVER.md
    GOUD: pipeline/roles/GOUD.md
versions:
  pipeline: 3.0.0
  methodology: 3.0.0
source_base_commit: <COMMIT_SHA>
```

## Verplichte scopevelden

Iedere nieuwe clusterscope bevat:

- centrale onderzoeksvraag;
- geografische begrenzing en uitsluitingsgrens;
- bestaande formele A/B/C-statussen uit projectrecords;
- bekende A-ankers;
- verplichte detectoren;
- lineage-, traditie-, Babaji- en AOAY-overlays;
- devotionele onderzoekslaag;
- deelname en buitenlandse-bezoekerslaag;
- actuele review- en belevingslaag;
- visueel dossier met tien functies;
- nabijheid, A-naar-rest-reistijden en loopclusters;
- vereiste artifacts;
- expliciete verboden;
- criteria voor clustercompleetheid.

## BRONS_CONTEXT vereisten

Naast de bestaande technische bestanden bevat de context:

- Methodology v3;
- Evidence Protocol v3;
- Quality Gate v3;
- relevante INDIA2-decisions;
- bestaande place/status-records;
- relevante predecessorrapporten;
- compact-report- en image-registertemplates;
- herkenningshaken of vaste kandidaatnummering waar beschikbaar.

## Fase-artifacts

Minimaal per metaal:

- `report/INDEX.md`;
- kandidaatrapportdelen;
- `claims.jsonl`;
- `sources/registry.jsonl`;
- `sources/rejected.jsonl`;
- `images.jsonl`;
- `experience_reviews.jsonl`;
- `proximity.jsonl` of expliciet `DEFERRED_TO_ROUTE_PHASE`;
- `audit.md`;
- `handoff.yaml`;
- `COMPLETED`.

GOUD levert daarnaast een compacte `decision_inputs.md` voor INDIA2 met per kandidaat de negen mensentaallagen uit Methodology v3, maar zonder adviserend A/B/C.

## Chatstart

Iedere metaalchat krijgt eerst de verplichte GitHub-preflight uit `pipeline/ENTRYPOINT.md`, gevolgd door:

`Open pipeline/ENTRYPOINT.md en voer uitsluitend de actie uit die in pipeline/NEXT_ACTION.yaml staat.`

## Chatuitvoer

Maximaal:

- cluster;
- fase;
- status;
- completioncommit;
- drie inhoudelijke gaten;
- één volgende startzin.

END_OF_ARTIFACT