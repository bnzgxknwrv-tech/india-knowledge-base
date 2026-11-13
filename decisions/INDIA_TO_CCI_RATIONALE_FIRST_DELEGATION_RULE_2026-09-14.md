# INDIA → CCI RATIONALE-FIRST DELEGATION RULE

Date: 2026-09-14
Decision authority: Mark
Status: HARD / DURABLE WORKING RULE

## WHY THIS RULE EXISTS

CCI was deliberately trained to think independently, challenge weak instructions, protect repository quality, and push back when a new task appears to contradict prior architecture or consensus. That is a feature, not a defect.

A failure occurred when INDIA22 gave CCI increasingly specific technical instructions without first explaining enough of the causal history: what Mark had just experienced, why the previous design had failed in practice, which invariant Mark was trying to protect, and which parts of the technical solution were merely INDIA's proposal rather than Mark's own decision. CCI then reasonably interpreted the new instructions as an unexplained reversal of the earlier consolidation agreement and resisted.

Mark explicitly corrected this on 2026-09-14: when INDIA delegates to CCI, especially architecture/governance/successor work, INDIA must explain the reasoning and history, not merely issue commands.

## HARD RULE

Every substantive INDIA → CCI delegation must be **RATIONALE FIRST, TASK SECOND**.

Before the requested actions, INDIA must explain in ordinary language:

1. **What happened / what Mark ran into.**
   - The concrete failure, confusion, regression, or new observation that triggered the task.

2. **Why it matters to Mark / the project.**
   - What user-facing or successor-quality problem this creates.

3. **What was already agreed before.**
   - The relevant prior consensus/invariant that should be preserved unless explicitly reopened.

4. **What changed now and why.**
   - Distinguish new Mark truth from INDIA's own technical hypothesis or proposed implementation.

5. **What is hard vs. what is open.**
   - HARD: explicit Mark requirement/invariant.
   - OPEN: architecture, mechanism, file count, test count, implementation detail for INDIA + CCI to solve together.

6. **Why CCI's independent judgment is wanted.**
   - CCI is not a blind executor. Invite it to challenge the proposed implementation when a simpler or safer way satisfies the same hard invariant.

Only after that rationale should INDIA state the concrete requested actions, bindings, deliverables, and tests.

## FORBIDDEN FAILURE MODE

Do not send CCI a bare technical command that looks like an unexplained reversal of earlier consensus when the real driver is a new Mark-observed failure.

Do not present INDIA's own architecture choice as if Mark personally chose that implementation.

Do not suppress CCI's independent reasoning. Explain enough context that CCI can reason from the same problem statement.

## DEFAULT DELEGATION SHAPE

`INDIA<n> zegt:`

### WAAROM DEZE TAAK BESTAAT
<what Mark encountered, why prior design was insufficient, what changed>

### HARD MARK TRUTH / INVARIANTS
<what must be preserved>

### OPEN TECHNICAL SPACE
<what CCI + INDIA may design/challenge>

### OPDRACHT
<concrete task>

### EXPECTED RESULT / BINDING
<deliverables, commit/comment header, pins>

`/INDIA<n>`

## SUCCESSOR REQUIREMENT

This rule must be incorporated into the active Mark working model / successor delegation behavior. A fresh INDIA must know that CCI's pushback is often intentional independent checking; the correct response is to provide causal context and distinguish Mark truth from INDIA implementation, not to overpower CCI with more unexplained instructions.
