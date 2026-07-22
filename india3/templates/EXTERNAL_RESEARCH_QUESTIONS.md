# EXTERNAL RESEARCH QUESTION TEMPLATES

Use one section as the full external task contract. Fill all placeholders; do not append contradictory instructions.

## BRONS BROAD SWEEP
Role: broad physical-place detector.
Goal: find all relevant physical places within `<scope>`.
Include: `<inclusion rules>`.
Exclude: persons/books without a physical place, routes/hotels unless explicitly scoped, automatic A/B/C.
Sources: public primary, institutional, academic and suitable current practical sources.
Known established facts: `<facts with IDs>`.
Open questions: `<gaps>`.
Capability check: classify direct access versus public search before work.
Output: candidate records, source records, atomic claims, negative findings and uncertainty.
Stop: central scope unavailable, required source inaccessible with no permitted fallback, or unsafe identity conflict.

## ZILVER VERIFICATION
Role: independent verifier.
Goal: test every material predecessor claim and source ID.
Do not repeat the broad sweep. Retain valid unique content; trace corrections, rejections and unresolved claims.
Output: verification action per claim, stronger sources where needed, physical identity and visitability separated, GEO status limited by actual tools.

## ZILVER TARGETED SUPPLEMENT
Role: focused gap researcher.
Goal: resolve only `<listed gaps>`.
Exclude: all already verified claims and candidates outside scope.
Output: new source IDs, exact claim changes and residual uncertainty.

## GOUD INTEGRATION
Role: final integrator and product builder.
Goal: integrate validated ZILVER output and active Mark decisions.
Exclude: broad new discovery and new A/B/C choices.
Output: technical audit, required user products and delivery manifest.

## GEO RECOVERY
Role: candidate-level GEO verifier.
Goal: establish the best defensible point for `<candidate IDs>`.
Mandatory: capability classification; check name, place type, locality/address, nearby anchors and explicit rejected points.
Statuses: only those allowed by GEO_PROTOCOL.
Output: one GEO audit record per candidate. Do not call syntax or coordinate parsing geographic verification.

## VISITABILITY CHECK
Role: current-access verifier.
Goal: separately establish present public access, entry conditions, opening patterns, contact and time sensitivity.
Output: `VERIFIED_PRIMARY`, `VERIFIED_SECONDARY`, `NOT_ESTABLISHED` or `TOOL_LIMITED` with date and source IDs.

## SOURCE-ID AUDIT
Role: referential-integrity auditor.
Goal: confirm every material claim references existing unique sources that support the exact domain.
Output: missing, duplicate, mismatched and valid IDs; no substantive rewriting.

## PHYSICAL IDENTITY CHECK
Role: identity verifier.
Goal: establish whether the named candidate corresponds to one physical site rather than a person, tradition, wrong branch, hotel, shop or same-name place.
Output: identity facts, aliases, locality, anchors, conflicts and exact uncertainty.

All templates require maximum safe autonomous completion, exact uncertainty wording and candidate-level isolation of blockers.

END_OF_ARTIFACT
