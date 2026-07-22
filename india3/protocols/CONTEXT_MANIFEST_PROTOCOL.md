# CONTEXT MANIFEST PROTOCOL

An executable context manifest contains:
- schema version, run ID, role and expected state;
- source commit and predecessor completion commit where applicable;
- role contract path;
- every file the worker must apply in `required_files` with its current Git blob SHA;
- allowed and forbidden repository paths;
- allowed public-research scope;
- output paths;
- required capability checks;
- quality gates and stop conditions.

## Immutable pin rules
Every required file must exist, be readable and have a current Git blob SHA. Placeholders, empty hashes, commit SHAs used as blob SHAs and stale file hashes are forbidden. A manifest containing `TODO`, `UNKNOWN`, `PLACEHOLDER`, `TO_BE_REPLACED` or a null required-file SHA is not executable and may not be activated.

## No circular dependency
A worker context must not hash-pin `pipeline/NEXT_ACTION.yaml` or another mutable activation file whose final contents are written after the manifest. The valid order is:
1. prepare all run and input files;
2. write the final context manifest;
3. read back and validate the manifest blob SHA and all required-file blob SHAs;
4. write `pipeline/NEXT_ACTION.yaml` last, including `context_manifest` and `context_manifest_sha`.

The activation write may not require or predict its own future commit SHA.

## Exhaustive context
Normal-context workers may read only the role contract, pinned manifest and listed required files. Therefore every protocol, decision register, candidate source and capability document that the worker must apply must be listed and hash-pinned. Workers may not broaden repository scope.

Only the controller creates or repairs worker contexts. Missing, truncated or hash-mismatched required files stop worker execution and return control to the controller.

END_OF_ARTIFACT