# ITERATION 2 TEST REPORT

## Method
Architecture contracts and templates were tested as deterministic scenario walkthroughs against the new role, context, decision, GEO and delivery gates.

1. New BRONS chat without prior knowledge — PASS. ENTRYPOINT + NEXT_ACTION + BRONS context provides bounded scope, role and outputs.
2. New ZILVER chat reading only pinned context — PASS. Required predecessor files and allowed paths are explicit; broad repository sweep is forbidden.
3. New GOUD chat producing a Mark choice product — PASS. GOUD context and delivery protocol require PDF/KML and active decision preservation.
4. Failure between ZILVER and GOUD — PASS. Status records last valid commit, first incomplete step and exact resume prompt; controller recreates only GOUD context after predecessor validation.
5. Missing source ID — PASS. Source protocol and transition gate block the material claim package; no silent repair.
6. State desynchronization — PASS. Run and quality protocols require state/events/claim agreement and stop transition.
7. Existing valid Mark decision — PASS. Append-only register loads before integration; worker cannot overwrite it and absence does not imply a new status.
8. GEO task without visual Google Maps access — PASS. Capability is `EXECUTABLE_PUBLIC_SEARCH` or `TOOL_LIMITED`; direct visual verification status is prohibited.
9. VNS-CAND-008 failure class — PASS. An explicit Mark rejection is durable; the rejected coordinate cannot return. Candidate 008 becomes `NOT_ESTABLISHED`, `TOOL_LIMITED` or `REQUIRES_MARK_LINK`; the other 39 remain executable.
10. Technically complete GOUD without practical Mark file — PASS. Quality gate returns BLOCKED because required PDF/KML are absent or not validated.

## Additional checks
- Claim status vocabulary separates IMPLEMENTED from VERIFIED.
- KML parsing/count checks are explicitly non-geographic.
- Candidate-level blockers are isolated.
- External prompt templates define role, scope, exclusions, sources, output, uncertainty, stop conditions and capability checks.
- No role may assign Mark A/B/C.

## Critical test result
ALL_CRITICAL_TESTS_PASS: YES

END_OF_ARTIFACT
