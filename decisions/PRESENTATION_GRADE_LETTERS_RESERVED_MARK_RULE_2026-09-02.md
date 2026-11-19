# PRESENTATION RULE — GRADE LETTERS ARE RESERVED FOR MARK GRADES — 2026-09-02

Status: **LOCKED_BY_MARK / HARD USER-FACING PRESENTATION RULE**
Branch: `agent/india8-cluster-casting`

## MARK DECISION
Mark explicitly corrected INDIA15 after it labeled Delhi traveler corridors/options with letters `A`, `B`, `C`, `D`, etc.

Hard rule:
- `A+`, `A`, `A*`, `B`, `C` are reserved exclusively for Mark's subjective travel grades/status semantics.
- Never label corridors, bundles, scenarios, packages, choice groups, menu options, route alternatives or planning worlds with letter labels `A/B/C/D/E/...`.
- Use neutral descriptive headings.
- If selectable groups need compact identifiers, use ordinary numbers (`1`, `2`, `3`, ...) only.

## WHY
Using A/B/C-style option letters for anything other than grades creates immediate ambiguity about whether INDIA is assigning or changing a Mark grade. The grade vocabulary is already semantically loaded throughout the repository and must remain visually unambiguous.

## RELATED USER-FACING RULE
Whenever an existing grade is displayed during a new presentation, make clear from context whether it is an already-existing explicit Mark decision rather than a new INDIA recommendation. Never let a carried-forward `[B]` appear as though INDIA just assigned it.

## PRECEDENCE
This is newer explicit Mark truth and supersedes any older presentation artifact that used A/B/C/D/E option letters, including the first version of `runs/active/INDIA10-CLUSTER-COVERAGE-REAUDIT-001/DELHI_FINAL_DAY_LP_DECISION_SURFACE_2026-09-02.md` before commit `a0c74b4f008a0baa3ba125a7b10f2f4eab7830f9`.

END