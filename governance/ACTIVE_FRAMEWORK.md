# INDIA ACTIVE FRAMEWORK

Status: CURRENT AUTHORITY MAP
Effective: 2026-08-23

## Current architecture
The current INDIA project is governed by:
1. explicit current Mark decisions / `LOCKED_BY_MARK` and explicit supersedes;
2. `governance/INDIA_SUCCESSOR_BOOT_PROTOCOL.md` for successor boot mechanics;
3. `governance/PRECEDENCE_MAP.jsonl` for authority conflicts;
4. central protected canon and current decision/state files;
5. current task contracts/state explicitly marked live;
6. current handoff/session entrypoints.

## Provenance versus current authority
Older `pipeline/`, earlier `india4/india5` protocol generations, older handoffs, archived worker snapshots and side-branch outputs remain valuable provenance. They are NOT automatically current operational authority merely because they still exist.

A historical file can contain a valid method insight while its route/status/count snapshot is superseded. Use the authority scope in PRECEDENCE_MAP and integration registries rather than treating a whole old file as either wholly true or wholly useless.

## Central-integration rule
A worker branch saying `COMPLETE` means only that worker output is complete. It does not mean the output is centrally integrated, Mark-reviewed or travel-ready. See `governance/CENTRAL_INTEGRATION_REGISTRY.jsonl`.

## Protected canon
The completed ZILVER package is centrally available at:
`runs/active/INDIAZILVER-ENTITY-ID-PROXIMITY-BACKFILL-001/`

`PROTECTED_CANON_BASELINE.csv` is a hard protected input. Staging queues in the same task are NOT Mark decisions and do not assign final new IDs.

## Archived semantic knowledge
The INDIA9 repo-wide audit and the lossless 62-blob unique semantic pack are preserved under:
`archive/india9-knowledge-audit-2026-08-23/`

They are provenance/evidence for the certified baseline, not a second live state tree.

## Legacy ACTIVE_STATE
`governance/ACTIVE_STATE.md` is preserved because it contains historical canon and evidence. Its old session labels, task states and date snapshots are NOT automatically live. Where it conflicts with this framework, PRECEDENCE_MAP, newer explicit decisions, protected canon or current task state, the newer scoped authority wins.

## Current-state principle
Do not infer currentness from directory name, age or `COMPLETE` alone. Currentness is determined by explicit authority, supersede relation, integration state and task scope.

## Freshness principle
Historical research knowledge may remain semantically valid while operational facts expire. Visa/transport/opening-hours/bookability/weather/current-access information must be revalidated when due.

## No silent deletion
Old protected decisions/evidence are not deleted merely to simplify the repo. Deprecate/supersede visibly. Physical branch/file pruning requires a separate reference audit and Mark approval where protected provenance could be affected.
