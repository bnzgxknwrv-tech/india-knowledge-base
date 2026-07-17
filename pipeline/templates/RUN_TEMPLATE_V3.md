# Run template v3.1 — toekomstige plaats-sweeps

Gebruik dit uitsluitend voor nieuwe runs nadat de handoff-smoketest is geslaagd en de implementatie is gemerged. Oude, reeds gepinde of geclaimde runs blijven hun oude protocolversie volgen.

## run.yaml kern

```yaml
run_id: <RUN_ID>
project: india
run_type: <CLUSTER_SWEEP|TARGETED_SUPPLEMENT>
scope_file: research/active/<RUN_ID>/scope.md
created_at: <ISO8601>
created_by: INDIA2
immutable_after_first_claim: true
operating_mode: CONTROLLED_MANUAL_INLINE_HANDOFF
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
  role_handoff_protocol: pipeline/protocols/ROLE_HANDOFF_PROTOCOL.md
  context_profiles: pipeline/CONTEXT_PROFILES.yaml
  next_action_template: pipeline/templates/NEXT_ACTION_V3_TEMPLATE.yaml
  next_role_handoff_template: pipeline/templates/NEXT_ROLE_HANDOFF_TEMPLATE.md
  mark_final_report_template: pipeline/templates/MARK_FINAL_REPORT_TEMPLATE.md
  handoff_layer_template: pipeline/templates/HANDOFF_LAYER_STATUS_TEMPLATE.yaml
  place_registry: knowledge/places/registry.jsonl
  place_numbering_policy: knowledge/places/NUMBERING_POLICY.md
  decisions_index: decisions/INDEX.yaml
  roles:
    BRONS: pipeline/roles/BRONS.md
    ZILVER: pipeline/roles/ZILVER.md
    GOUD: pipeline/roles/GOUD.md
versions:
  pipeline: 3.1.0
  methodology: 3.0.0
source_base_commit: <COMMIT_SHA>
post_completion_policy:
  BRONS:
    mode: INLINE_POST_PHASE_CONTROLLER
    target_role: ZILVER
    target_ready_state: READY_FOR_ZILVER
  ZILVER:
    mode: INLINE_POST_PHASE_CONTROLLER
    target_role: GOUD
    target_ready_state: READY_FOR_GOUD
  GOUD:
    mode: MARK_FINAL_REPORT
    completion_destination: VOOR_MARK
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

Iedere nieuwe metaalcontext bevat ook:

- `pipeline/protocols/LONG_RUNNING_EXECUTION_PROTOCOL.md`;
- `pipeline/protocols/ROLE_HANDOFF_PROTOCOL.md`;
- voor BRONS en ZILVER: `pipeline/templates/NEXT_ROLE_HANDOFF_TEMPLATE.md`;
- voor GOUD: `pipeline/templates/MARK_FINAL_REPORT_TEMPLATE.md`.

Bij omvangrijke runs schrijft de rol vóór sessie-uitputting `CHECKPOINT.yaml` onder dezelfde actieve workerclaim. Een hervattende chat maakt geen nieuwe workerclaim en herhaalt geen afgerond onderzoek.

Volledige oudere rapporten worden alleen toegevoegd bij een concrete loss-control-, conflict- of clustercontinuïteitstrigger.

## BRONS_CONTEXT vereisten

Naast technische bestanden bevat BRONS alleen:

- scope en bekende ankers/statussen;
- gepinde methodologie en evidence-protocol;
- quality gate;
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

GOUD levert daarnaast alle run-specifieke finale artifacts en verplicht `MARK_FINAL_REPORT.md`.

## NEXT_ACTION per fase

Maak `pipeline/NEXT_ACTION.yaml` voor nieuwe runs volgens `pipeline/templates/NEXT_ACTION_V3_TEMPLATE.yaml`.

BRONS en ZILVER gebruiken:

```yaml
post_completion:
  mode: INLINE_POST_PHASE_CONTROLLER
  transition_protocol: pipeline/protocols/CONTROLLER_TRANSITION_PROTOCOL.md
  role_handoff_protocol: pipeline/protocols/ROLE_HANDOFF_PROTOCOL.md
  target_role: <ZILVER|GOUD>
  target_ready_state: <READY_FOR_ZILVER|READY_FOR_GOUD>
  emit_next_role_handoff: true
  report_template: NOT_APPLICABLE
  completion_destination: VOOR_VOLGEND_METAAL
```

GOUD gebruikt:

```yaml
post_completion:
  mode: MARK_FINAL_REPORT
  transition_protocol: NOT_APPLICABLE
  role_handoff_protocol: pipeline/protocols/ROLE_HANDOFF_PROTOCOL.md
  target_role: MARK
  target_ready_state: NOT_APPLICABLE
  emit_next_role_handoff: false
  report_template: pipeline/templates/MARK_FINAL_REPORT_TEMPLATE.md
  completion_destination: VOOR_MARK
```

## Chatstart

INDIA2 levert één volledige BRONS-startopdracht. Daarna gebruikt iedere volgende chat het geldige, door de inline controller geleverde handoffblok.

De volgende rol leest inhoudelijke predecessoroutput uitsluitend uit het gepinde GitHub-contextmanifest.

## Chatuitvoer

BRONS en ZILVER leveren compact:

- cluster;
- fase;
- status;
- fasecompletioncommit;
- transitioncommit of blocker;
- maximaal drie inhoudelijke gaten;
- `NEXT_ROLE_READY`;
- de volledige plakbare opvolgeropdracht wanneer READY.

GOUD levert niet alleen een completionnote maar het volledige gecommitte rapport rechtstreeks aan Mark, gevolgd door het zelfrouterende slotblok.

END_OF_ARTIFACT