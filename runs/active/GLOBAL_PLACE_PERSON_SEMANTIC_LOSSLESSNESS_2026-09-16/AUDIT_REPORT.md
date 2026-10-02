# GLOBAL PLACE↔PERSON SEMANTIC LOSSLESSNESS AUDIT — KAKRIGHAT INCIDENT

Run: 2026-09-16. Task source: PR #23 comment 5692870622. Branch: agent/india8-cluster-casting.
Companion files in this directory: `KAKRIGHAT_INCIDENT_POSTMORTEM.md`, `PLACE_PERSON_EDGE_LEDGER.jsonl`,
`DEFECT_REGISTER.jsonl`, `ROUTE_IMPACT.md`, `EXTERNAL_REDISCOVERY_REPORT.md`, plus the new
`governance/scripts/validate_place_person_edges.py` prototype validator.

No Mark grade, CURRENT_TRUTH content, or route decision was changed by this audit. This file only
reports findings and impact.

## 1. KAKRIGHAT CONTROL TEST: PASS

The task's mandatory positive control was to independently rediscover — without being told the
specific file — that Kakrighat carries more than its presented Vivekananda/Jnana-Vriksha layer.
Method: `grep -rli "kakrighat"` across the full repository, then targeted reads of every hit.
Result: found `runs/active/TOP11-NKB-RAMDASS-V2-PRE-EXTERNAL-001/NEEM_KAROLI_BABA_V2_PRE_EXTERNAL_FREEZE.md`
row 7, which documents a pre-existing, EXACT-confidence Neem Karoli Baba / Maharajji edge at
Kakrighat (Hanuman idol installation, shared holy place; also secondary Sombari Baba / Panjabi Baba
mentions), sourced to nkbmeditation.org. This edge is absent from `governance/CURRENT_TRUTH.md`
and from all Mark-facing route presentation, even though `governance/CURRENT_TRUTH.md` still
correctly carries the Vivekananda layer. **Control test: PASS** — the method finds the planted
failure unaided.

## 2. PLACES AND PERSONS AUDITED

- **Places carrying at least one ledger row**: Kakrighat; Dashashwamedh Ghat, Varanasi;
  Vivekanandar Illam / Ice House, Chennai; Mahabodhi Temple, Bodh Gaya; Rana Mahal district,
  Varanasi. (5 places with new/confirmed findings; two additional major anchors — Manikarnika Ghat
  and Kainchi Dham — were spot-checked and found clean, see §5.)
- **Persons audited across those places**: Swami Vivekananda, Neem Karoli Baba/Maharajji, Sombari
  Baba, Panjabi Baba, Mahavatar Babaji, Lahiri Mahasaya, Sri Yukteswar.
- **Source material used**: `governance/CURRENT_TRUTH.md` (full read, current canon);
  `research/INDIA20_ROUTEWIDE_KAKRIGHAT_TYPE_DETOUR_AND_MISSED_MAJOR_SITE_AUDIT_2026-09-13.md` (full
  read, prior place-centric audit); `runs/active/TOP11-NKB-RAMDASS-V2-PRE-EXTERNAL-001/`,
  `runs/active/TOP11-CORE-KRIYA-RECONCILIATION-001/`, and
  `runs/active/TOP11-RAMANA-RAMAKRISHNA-MULTIDETECTOR-RECONCILIATION-001/` (person-centric TOP-11
  reconciliation matrices, 156 combined JSONL entries cross-checked against current trip place
  names).

## 3. REPO-WIDE RESULT: THE SAME PATTERN RECURS

Cross-checking the two most authoritative TOP-11 reconciliation matrices against every current trip
place name surfaced 21 hits; most were already reflected in canon (e.g. Kolkata's Vivekananda
Birthplace/Cossipore/Balaram Mandir/Shyampukur Bati cluster, confirmed present in
`CURRENT_TRUTH.md` lines 107-114 from a prior audit). Two were not, and match the Kakrighat pattern
exactly — well-evidenced, previously-known edges that never crossed from person-centric research
into the place-centric canon:

- **Dashashwamedh Ghat, Varanasi** — Mahavatar Babaji / Mataji / Lahiri Mahasaya vision site
  (Autobiography of a Yogi ch. 33). Absent from CURRENT_TRUTH's Varanasi section entirely, despite
  Varanasi being an already-locked 8-night cluster.
- **Vivekanandar Illam / Ice House, Chennai** — Vivekananda's actual 6-14 Feb 1897 residence, with a
  still-existing, still-visitable meditation room. Already identified in the repo's own
  2026-09-13 place-centric audit (section D) but never migrated into CURRENT_TRUTH's Chennai
  section, which currently has zero site-level content beyond "buffer before flight."

Two lower-confidence leads were also found and are explicitly **not** presented as established
edges:

- **Mahabodhi Temple, Bodh Gaya** — an external research pass raised an unconfirmed claim that Sri
  Yukteswar took monastic vows there in 1906; not confirmed in AOAY text, no usable locator given.
  Flagged `UNVERIFIED`, not pursued further externally (see EXTERNAL_REDISCOVERY_REPORT.md) to
  avoid manufacturing false confidence around an already-blocked source.
- **Rana Mahal district, Varanasi** — Sri Yukteswar's mother's house per direct AOAY text (ch. 10,
  ch. 12); exact building and current access status unestablished. Held as a low-priority open
  lead, not ready for Mark presentation.

## 4. SEPARATELY VISITABLE SUB-PLACES HIDDEN UNDER A PARENT

Checked specifically for sub-places a single parent-place row might be masking. The clearest case
found is Dashashwamedh Ghat itself relative to Varanasi's ghats generally: it is not currently
named as its own stop at all, so nothing is "hidden under" it — the defect here is *absence*, not
masking. No case was found of an existing CURRENT_TRUTH row silently bundling two genuinely separate
visitable addresses under one name. This check was not exhaustive across all ~30+ current places
(see §6 coverage limits).

## 5. PASS 2 — CONTROLLED EXTERNAL REDISCOVERY (run only after Pass 1 frozen)

Full detail in `EXTERNAL_REDISCOVERY_REPORT.md`. Summary of what changed after fresh, live
verification:

- **Dashashwamedh Ghat / Babaji cave temple**: independently re-confirmed live via WebSearch across
  three independent sources (a first-person visitor account, an independent Kriya Yoga pilgrimage
  site listing, and Wikipedia's Lahiri Mahasaya article) — a cave temple dedicated to Babaji exists
  at the site today, "a perfect place to sit in meditation," next to Lahiri Mahasaya's preserved
  home in nearby Bengali Tola. This is a currently visitable, currently meditatable site, not just a
  historical citation.
- **Vivekanandar Illam closure day — resolved**: third-party aggregators disagreed (Monday vs.
  Wednesday). Fetched the museum's own official site (vivekanandahouse.org) directly: it states
  "Closed on Mondays," hours 10:00-12:30 and 15:00-19:15 (19:30 Sundays). Treated as authoritative.
  19 Jan 2027 is a Tuesday, so this does not conflict with the currently open Chennai day.
- **Mahabodhi/Sri Yukteswar 1906 vows**: deliberately not pursued further; the claim has no locator
  to chase, and further generic search would risk manufacturing false confidence around an
  already-flagged unverifiable claim. Left open.
- **Spot-checks on two major, already-locked anchors** (Manikarnika Ghat, Kainchi Dham): both clean,
  no additional canonical-person edge found beyond what's already documented.

## 6. RESIDUAL COVERAGE LIMITS (stated plainly, not hidden)

- The most authoritative/final TOP-11 reconciliation files were checked; not every one of the ~13
  TOP-11 sweep directories' full internal draft/intermediate file sets was individually read.
- No full external cross-product of every canonical person against every currently-scheduled place
  (~300+ combinations) was attempted — judged infeasible to do to a genuinely verified standard in
  one pass; a superficial attempt would have produced false-confidence noise, which is worse than an
  honestly bounded pass.
- Kolkata's ~80 minor Ramakrishna devotee-house records in the reconciliation matrix were
  deliberately not individually pursued — almost all are minor/private addresses, low expected
  yield relative to the two substantive findings this pass did produce.
- Everything reported here is either EXACT/independently re-verified (D1-D3) or explicitly marked
  unverified/open-lead (D4, D5) — nothing is asserted above the confidence the evidence supports.

## 7. WHICH EXISTING MARK DECISIONS MAY NEED RE-OPENING

- **None of Mark's existing grade or route decisions need re-opening because they were made on
  incomplete meaning.** Kakrighat (D1) is already A+ (the ceiling) and already locked into the
  23 Dec route per `decisions/INDIA22_GROT_VIVEKANANDA_23_DEC_MARK_DECISION_2026-09-14.md`; the
  missing NKB layer changes the *description* Mark should see, not the grade or the schedule.
- **D2 (Dashashwamedh Ghat) and D3 (Vivekanandar Illam) are not re-opens of past decisions** — Mark
  never saw either candidate, so there is no prior decision to revisit. Both need a normal,
  first-time decision-ready card presented to Mark, per standard place-card rules. See
  `ROUTE_IMPACT.md` for per-defect detail.
- D4 and D5 require no Mark action at this time (unverified / access-unknown respectively).

## 8. ROOT CAUSE

Two research modes have operated in this repository without ever cross-referencing each other:

1. **Person-centric sweeps** (the TOP-11 files): start from a saint/teacher and enumerate every
   place connected to them, with rich source provenance, but write their output into
   `runs/active/TOP-11-*` files that are never diffed against the place-centric trip canon.
2. **Place-centric audits** (like the 2026-09-13 Kakrighat-type audit): start from the current route
   and check for missed content, but check each place's most *prominent* association only, since
   that is what "the place" is filed under — a place already graded for one person's sake reads as
   "handled" and does not get systematically re-checked against every other person-centric sweep
   that also touched it.

Confirmed by inspecting every existing validator in `governance/scripts/`: all of them check that a
PLACE row exists, has a grade, and is uniquely numbered (`validate_successor_boot.py`,
`validate_independent_check.py`, and the various numbering/count checks). **None of them check that
a PERSON↔PLACE edge, once discovered in either research mode, survives into
`governance/CURRENT_TRUTH.md` and route presentation.** A place can look "complete" by every
existing check while silently having lost half its meaning, exactly as Kakrighat did.

## 9. PREVENTION MECHANISM

Prototype built and tested this session: `governance/scripts/validate_place_person_edges.py`.

- Reads a normalized `PLACE_PERSON_EDGE_LEDGER.jsonl` (schema demonstrated in this audit's own
  ledger file) plus `governance/CURRENT_TRUTH.md`.
- For every ledger row marked `repo_known_before_audit: true` and not flagged as an open lead, does
  a case-insensitive co-occurrence check (400-character context window) for the place name (or any
  alias) and the person name in CURRENT_TRUTH.
- Fails (exit 1) exactly when a ledger row claims `current_canon_present: true` but the edge is not
  actually found — i.e. a regression, not a new-discovery tool.
- Verified in this session: correctly reports `OK` for Kakrighat+Vivekananda (present), and
  correctly reports `CONFIRMED GAP (expected)` for Kakrighat+NKB, Dashashwamedh Ghat+Babaji,
  Dashashwamedh Ghat+Lahiri Mahasaya, and Vivekanandar Illam+Vivekananda (all currently missing,
  matching the ledger) — no unhandled exceptions, no false positives.

**Recommendation for how this should be used going forward**: every time a person-centric TOP-11
sweep or a place-centric audit discovers a PERSON↔PLACE edge, it should be appended as a row to a
single running ledger (this task's ledger is the first instance; it should be merged into one
project-wide ledger rather than left as a one-off). The validator should then be run as part of any
future "coverage complete" or "boot" claim, the same way existing validators are already run — this
turns "we checked" into something falsifiable rather than a prose assertion. This is a regression
guard only: it cannot invent edges research never found, so Pass-2-style external rediscovery
remains a separate, periodic activity.

## 10. CURRENT_TRUTH / GRADE / ROUTE CHANGES MADE BY THIS AUDIT

None. Per the task's explicit instruction, this audit changed no Mark grades, no
`governance/CURRENT_TRUTH.md` content, and no route decisions. All findings are reported for Mark's
own triage.

END AUDIT_REPORT
