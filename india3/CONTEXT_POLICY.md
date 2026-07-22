# CONTEXT POLICY

Normal execution reads only:
1. `pipeline/ENTRYPOINT.md`;
2. `pipeline/ACTIVE_SYSTEM.yaml`;
3. `pipeline/NEXT_ACTION.yaml`;
4. the active role contract;
5. the pinned context manifest;
6. files explicitly listed in `required_files`.

A context manifest must declare allowed and forbidden paths, expected state, source commit, required hashes where available, output paths and stop conditions. Broad repository sweeps are prohibited during normal role execution. Historical research is referenced by path and source ID, not recopied into every handoff.

A controller may inspect predecessor manifests, state, events and required artifacts solely to validate and prepare the next context. A migration or repair run may use a wider explicitly declared scope.

END_OF_ARTIFACT
