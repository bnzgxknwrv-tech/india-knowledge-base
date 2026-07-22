# CLAIM STATUS PROTOCOL

Allowed statuses:
- `USER_DECISION`: explicit active Mark decision.
- `IMPLEMENTED`: confirmed present in an artifact or system; not proof of substantive truth.
- `VERIFIED_PRIMARY`: claim directly supported by an appropriate primary/official source.
- `VERIFIED_SECONDARY`: claim supported by suitable independent secondary evidence.
- `ASSISTANT_PROPOSAL`: non-user proposal awaiting acceptance.
- `REJECTED`: explicitly rejected evidence, claim or proposal; reason required.
- `NOT_FOUND`: targeted search found no supporting evidence; search scope required.
- `NOT_ESTABLISHED`: available evidence is insufficient for the claim.
- `TOOL_LIMITED`: required check cannot be completed with available tools.
- `SUPERSEDED`: replaced by a named later record.

Every claim stores claim ID, subject, exact statement, status, source IDs, checked_by_role, checked_at, method and residual uncertainty. `IMPLEMENTED` never substitutes for `VERIFIED_*`.

END_OF_ARTIFACT
