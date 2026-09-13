# CCI — LIVE LEDGER SYNC REPAIR (INDIA20 → INDIA21 HANDOFF)

Status: **CORRECTION RECORD, not a new Mark decision**
Date: 2026-09-13
Author: CCI, while writing `runs/active/INDIA20_FINAL_EXTRACTION_2026-09-13.md` for the INDIA21 boot handoff
Branch: `agent/india8-cluster-casting`

## What was found

While cross-checking INDIA20's final state for the successor extraction, CCI found that `governance/CURRENT_STATE.md`'s "HIGH-PRIORITY RECOVERED OPEN CANDIDATES" section, and six rows (`L101`-`L106`) of `runs/active/INDIA20-LIVE-LEDGER-V4-REPAIR-001/LIVE_DERIVED_PLACE_GRADE_LEDGER_2026-09-13.csv`, still showed `OPEN`/`MARK_TRIAGE_REQUIRED` for candidates that already had a locked Mark decision on record elsewhere in the repository:

| Candidate | CSV row | Was | Actual locked grade | Authority |
|---|---|---|---|---|
| Kasar Devi Cave / "Grot Vivekananda" | L101 | OPEN | A+ | `decisions/INDIA20_DEC23_24_KUMAON_VIVEKANANDA_TRANSIT_AND_BABAJI_DAY_MARK_DECISION_2026-09-13.md` sec.6 |
| Vivekananda Ancestral House/Birthplace | L102 | OPEN | A+ | `decisions/INDIA20_KOLKATA_VIVEKANANDA_PRIORITY_AND_CHENNAI_BYCATCH_MARK_DECISION_2026-09-13.md` sec.1.1 |
| Cossipore/Kashipur Udyanbati | L103 | OPEN | A+ | same file sec.1.2 |
| Balaram Mandir | L104 | OPEN | A+ | same file sec.1.3 |
| Shyampukur Bati | L105 | OPEN | A | same file sec.1.4 |
| Chennai Vivekananda House/Ice House | L106 | OPEN | A* (buffer-bycatch only) | same file sec.3 |

Two other candidates in the same "recovered" family (50 Amherst Street, Dihika) already had correct grades in the CSV (`L095`=A*, `L100`=A*) but `governance/CURRENT_STATE.md`'s prose still listed them under "must go to Mark" — also stale.

Root cause: each of these grades was recorded correctly inside a dated `decisions/*.md` file, but the mechanical sync step that writes decisions back into the live-derived CSV and into `CURRENT_STATE.md`'s summary prose did not run for these particular rows before INDIA20's context ran out. This is the same `GRADE_SCOPED_LEDGER_MISTAKEN_FOR_COMPLETE_MEMORY` failure class INDIA20 itself named in `CURRENT_STATE.md`, recurring inside the very tool built to fix it.

Two candidates remain genuinely open (no decision file exists for them): Lala Badri Shah House (`L107`) and J.C. Bose residence (`L108`, which additionally needs an existence/access verification pass before it can be presented to Mark at all).

## What was fixed

- `LIVE_DERIVED_PLACE_GRADE_LEDGER_2026-09-13.csv`: rows `L101`-`L106` updated to their correct `LIVE_GRADE`/`LIVE_EXECUTION_CLASS`/`NOTE`, each citing the exact decision file and section that locked it. Verified by content-level diff that no other row changed.
- `governance/CURRENT_STATE.md`: the "HIGH-PRIORITY RECOVERED OPEN CANDIDATES" section rewritten to state the resolved grades and cite this file; `state_revision`, `status`, and `latest_successor_handoff` fields updated; the classification-regression half of the v4 blocker marked cleared while the separate ledger-completeness blocker is left explicitly still open.
- `runs/active/INDIA20_FINAL_EXTRACTION_2026-09-13.md`: written to already reflect the corrected state, so INDIA21 never sees the stale version.

## Why this is a correction record, not a new Mark decision

No grade was changed by CCI's judgment. Every value written here already existed as an explicit Mark decision in a dated `decisions/*.md` file; this record only makes the mechanical ledger and status prose agree with what Mark already decided. Per `decisions/TRADITION_IS_EVIDENCE_PILGRIMAGE_NOT_COURTROOM_MARK_DECISION_2026-09-13.md` and the standing rule that only Mark changes A+/A/A*/B/C, CCI verified this distinction carefully before writing anything: this is bookkeeping repair, not a grade opinion.

## Successor rule

Do not re-ask Mark about any of the six resolved candidates above. When a status file and a decision file disagree, trust the more recent decision file (verify with `git log -S`/`git show`, as done here), fix the status file, and record the fix — do not present the disagreement to Mark as if it were his open question.

END CCI LIVE LEDGER SYNC REPAIR
