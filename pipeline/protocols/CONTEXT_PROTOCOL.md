# Context Protocol v2.1

## Regel

Geen rol leest ooit "de repository". Iedere rol leest uitsluitend:
1. `pipeline/ENTRYPOINT.md`;
2. zijn gepinde rolcontract;
3. de gepinde methodologie en protocollen;
4. zijn fase-contextmanifest;
5. exact de bestanden die daarin staan.

## Contextmanifest

Per uitvoerbare rol bestaat `research/active/<run-id>/context/<ROLE>_CONTEXT.yaml` met minimaal:
- `run_id`;
- `role`;
- `source_commit`;
- `protocol_versions`;
- `required_files`;
- `optional_files`;
- `forbidden_files`;
- `priority_order`;
- `expected_hashes` waar beschikbaar;
- `maximum_context_budget`;
- `predecessor_manifest`;
- `output_path`.

## Levenscyclus

Bij runcreatie wordt uitsluitend `BRONS_CONTEXT.yaml` definitief gegenereerd.

`ZILVER_CONTEXT.yaml` bestaat pas nadat:
- BRONS volledig is gecommit;
- BRONS/manifest.yaml en COMPLETED zijn gevalideerd;
- de controller de definitieve BRONS-resultaatcommit heeft vastgesteld;
- alle vereiste BRONS-artifacts en beschikbare hashes zijn gepind.

`GOUD_CONTEXT.yaml` wordt op dezelfde wijze pas na een geldige ZILVER-uitkomst gegenereerd.

Een leeg, voorlopig, PENDING of vooraf gegokt contextmanifest is niet uitvoerbaar en mag niet als required file voor een rol worden gebruikt.

## Selectie

`required_files` bevat alleen wat noodzakelijk is voor de rol. Oude runs, niet-relevante clusters en volledige archieven zijn verboden tenzij expliciet genoemd.

BRONS krijgt scope, controlelijst, projectoverlays, bestaande statussen en relevante records.

ZILVER krijgt het volledige BRONS-outputmanifest en alle daarin verplichte rapport-, claim- en bronbestanden, gepind op de definitieve BRONS-resultaatcommit.

GOUD krijgt het volledige ZILVER-outputmanifest en alleen BRONS-bestanden die expliciet nodig zijn voor verliescontrole, gepind op de definitieve ZILVER-resultaatcommit.

De controller genereert deze manifesten volgens `pipeline/protocols/CONTROLLER_TRANSITION_PROTOCOL.md`.

## Budget en splitsing

- Geen primair bestand boven 1500 regels.
- Grote kandidatenkaarten worden in genummerde delen gesplitst.
- `report/INDEX.md` bepaalt de verplichte leesvolgorde.
- Een rol stopt wanneer een required file niet volledig gelezen kan worden.
- Optional files worden alleen geopend wanneer het manifest een concrete trigger noemt.

## Determinisme

Een AI mag geen extra repositoryzoektocht starten om "voor de zekerheid" meer interne bestanden te lezen. Extern webonderzoek binnen de rol blijft toegestaan. Ontbrekende interne context wordt een blokkade of expliciet context-gat; geen vrije gok.

END_OF_ARTIFACT