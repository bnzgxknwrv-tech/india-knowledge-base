# ITERATION 1 — FORENSIC AUDIT AND PRESERVATION MAP

## Scope and evidence base
INDIA3 audited the active pipeline entrypoint and routing, BRONS/ZILVER/GOUD contracts, execution and controller protocols, GEO rules, canonical decision index and representative Varanasi artifacts, including issue #22. The audit is targeted: it preserves active research outputs and avoids a blind repository rewrite.

## What INDIA1/INDIA2 did well
- GitHub is already the durable handoff layer: runs have immutable identity, state, append-only events, phase folders, manifests and pinned predecessor snapshots.
- Role separation is substantially present: BRONS discovers, ZILVER challenges, GOUD integrates, and the controller owns transitions.
- Existing contracts prohibit workers from inventing formal A/B/C decisions and protect phase ownership.
- Source-commit pinning, sentinels, claim locks and readback rules provide a strong basis for resumability.
- Varanasi retained all 40 candidates and surfaced uncertainty rather than deleting weak records.

## Principal failures and contradictions
1. Technical validation was repeatedly worded too broadly. KML parsing, marker count and valid coordinates were treated as if they established geographic correctness.
2. The old GEO taxonomy lacks explicit evidence for Google Maps place identity versus official map link, site centre, working point or approximate point.
3. GOUD's old contract says it does not make KML unless explicitly scoped and normally delivers a long Markdown report. Issue #22 makes a decision-ready PDF plus complete KML a canonical product requirement for candidate runs.
4. DECISION-0013 says INDIA2 creates KML and human products after GOUD; issue #22 and INDIA3 supersede that workflow operationally by making the complete user delivery part of GOUD completion. The historical decision remains preserved and is marked superseded only through an explicit new register entry, never silently overwritten.
5. Existing run policy allows advisory status for new candidates, while Mark's newer requirement prohibits BRONS/ZILVER/GOUD from assigning A/B/C. INDIA3 uses `DOOR_MARK_TE_BEOORDELEN` instead.
6. Existing prompts and post-phase handoffs are long. They duplicate repository policy in chat and increase copy/paste and context load.
7. Capability checks are implicit. A worker can discover late that visual Google Maps operation is impossible.
8. The active NEXT_ACTION points to a Varanasi GOUD phase whose final report already exists. Routing state can therefore become stale relative to repository HEAD.
9. The VNS-CAND-008 class of failure shows that a rejected coordinate can be reintroduced through source reuse unless user rejection is a first-class immutable constraint.

## Sources of slowness
- broad role instructions repeated in every activation;
- reading full predecessor reports instead of compact manifests and claim/source subsets;
- duplicate prose across report, handoff and chat;
- late tool-capability discovery;
- separation of technical GOUD completion from user-product rendering;
- repeated reconstruction of Mark decisions from narrative files.

## Canonical Mark decisions identified
- Only Mark assigns formal A/B/C.
- Existing Mark choices remain exact and cannot be overwritten by a worker.
- Unchosen candidates remain `DOOR_MARK_TE_BEOORDELEN`.
- Candidate/cluster GOUD delivery requires a readable decision product and complete map product where the run requires them.
- GEO uncertainty must remain visible; an explicitly rejected coordinate may not be restored.
- A clean chat must start from one short prompt and retrieve the remainder from GitHub.

## Preservation findings
- Preserve all historical research outputs, source registers, claim registers, decisions and run artifacts.
- Preserve the old pipeline as historical evidence, but remove its active status after activation.
- Do not delete unique protocols during migration. Archive replaced control documents with provenance.
- Existing active/finished runs remain readable under their pinned protocol versions.

## Protocol overlaps
- ENTRYPOINT, EXECUTION_PROTOCOL, ROLE_HANDOFF_PROTOCOL and CONTROLLER_TRANSITION_PROTOCOL repeat preflight, role switching and state rules.
- GOUD, MARK_FINAL_REPORT template and issue #22 overlap but conflict on the actual user deliverable.
- GEO_LOCATION_PROTOCOL and run-specific GEO policy use overlapping but insufficiently precise status labels.

## Role-boundary corrections for INDIA3
- Controller: state, transition, manifest, integrity and recovery only.
- BRONS: bounded discovery and evidence capture; no definitive validation or Mark choice.
- ZILVER: independent verification and correction; no Mark choice.
- GOUD: integrates validated content, protects decisions and produces both technical audit and required user products; no broad new sweep or Mark choice.

## Varanasi structural lessons
- `40 markers` proves coverage count only.
- `KML opens` proves syntax only.
- `coordinate copied from an official page` does not prove the point is the intended physical visitor location.
- A Google Maps URL is not evidence of visual inspection unless the tool actually opened and matched the place.
- A single disputed candidate is isolated as `NOT_ESTABLISHED`, `TOOL_LIMITED` or a specific request for a Mark-supplied link; it does not block the other candidates.
- User-rejected evidence has precedence over inherited coordinates until explicitly superseded by Mark.

## Iteration 1 quality gate
PASS.
- Canonical decisions identified: YES.
- Unique valid protocols preserved: YES.
- Lessons concrete and testable: YES.
- Inventory sufficient for safe parallel build: YES.
- Deletions performed: NO.

END_OF_ARTIFACT
