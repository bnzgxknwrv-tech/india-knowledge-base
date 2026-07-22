# CONTEXT MANIFEST PROTOCOL

An executable context manifest contains:
- schema version, run ID, role and expected state;
- source commit and predecessor completion commit;
- role contract path;
- `required_files` with path and hash when available;
- `allowed_repository_paths` and `forbidden_repository_paths`;
- allowed public-research scope;
- output paths;
- required capability checks;
- quality gates and stop conditions.

Workers may not broaden repository scope. Missing, truncated or hash-mismatched required files stop execution. Only the controller creates successor manifests after validating predecessor completion.

END_OF_ARTIFACT
