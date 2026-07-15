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
context_profile: BRONS_MIN
pins:
  entrypoint: pipeline/ENTRYPOINT.md
  methodology: knowledge/methodology/METHODOLOGY_V2.md
  evidence_protocol: pipeline/protocols/EVIDENCE_PROTOCOL.md
  quality_gate: pipeline/QUALITY_GATE.md
  execution_protocol: pipeline/protocols/EXECUTION_PROTOCOL.md
  long_running_execution_protocol: pipeline/protocols/LONG_RUNNING_EXECUTION_PROTOCOL.md
  context_protocol: pipeline/protocols/CONTEXT_PROTOCOL.md
  controller_transition_protocol: pipeline/protocols/CONTROLLER_TRANSITION_PROTOCOL.md
  self_routing_protocol: pipeline/protocols/SELF_ROUTING_PROTOCOL.md
  context_profiles: pipeline/CONTEXT_PROFILES.yaml
  handoff_layer_template: pipeline/templates/HANDOFF_LAYER_STATUS_TEMPLATE.yaml
  place_registry: knowledge/places/registry.jsonl
  place_numbering_policy: knowledge/places/NUMBERING_POLICY.md
  decisions_index: decisions/INDEX.yaml
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

## Rolgebonden context

Gebruik verplicht `pipeline/CONTEXT_PROFILES.yaml`:

- BRONS: `BRONS_MIN`;
- ZILVER: `ZILVER_MIN`;
- GOUD: `GOUD_MIN`.

Ieder required bestand in een contextmanifest vermeldt:

- `path`;
- `reason`;
- `task`;
- `expected_git_blob_sha`.

Iedere metaalcontext bevat tevens `pipeline/protocols/LONG_RUNNING_EXECUTION_PROTOCOL.md`. Bij omvangrijke runs werkt de rol in afsluitbare blokken en schrijft zij vóór sessie-uitputting een `CHECKPOINT.yaml` met dezelfde actieve claim. Een hervattende chat maakt geen nieuwe claim en herhaalt geen afgerond onderzoek.

Volledige oudere rapporten worden alleen toegevoegd bij een concrete loss-control-, conflict- of clustercontinuïteitstrigger.

## BRONS_CONTEXT vereisten

Naast de technische bestanden bevat BRONS alleen:

- scope en bekende ankers/statussen;
- Methodology v3;
- Evidence Protocol v3;
- Quality Gate v3;
- relevante decisions;
- canonical place registry en nummeringsbeleid;
- compacte predecessorcontext die duplicaten voorkomt;
- required outputtemplates.

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
- `handoff.yaml` met laagstatussen `ACCEPTED`, `CORRECTED`, `OPEN` of `NOT_APPLICABLE`;
- `COMPLETED`.

De opvolger heropent altijd `OPEN`, alle dragende claims en `CORRECTED` met hoog risico. Een `ACCEPTED` niet-dragende review- of beeldlaag wordt alleen met een gemotiveerde steekproef heropend.

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