# INPUT COMPLETENESS GATE — CCI SELF-CHECK

Status: **v2 — CCI'S RESPONSE TO WORK'S INDEPENDENT AUDIT OF v1, PLUS THE ORIGINAL v1 SELF-CHECK BELOW**

Pinned to central HEAD `8e7419d6120556c8151f2654bce33bcac85ca678` (see `INPUT_CONTRACT.md` §2); packet version = the six files in this directory as committed on the 2026-09-10 repair pass (v2), superseding the audited v1 at commit `c0338559222959d4a2fe4ac67ef5f8bf877c6b58`.

---

## PART A — RESPONSE TO WORK'S FAIL_WITH_GAPS AUDIT (2026-09-10)

Independent auditor WORK reviewed v1 of this packet and returned `FAIL_WITH_GAPS` with six numbered "material gap" categories plus a row-count observation. Per this project's evidence-over-authority philosophy, every one of WORK's specific claims was independently re-verified against the actual cited source files before any repair was made — WORK's verdict was treated as a hypothesis list, not as ground truth. This section states CCI's finding for each item.

### Row-count observation ("67 vs 68")

**DISPUTED — not an actual defect.** WORK observed that 21 A+ + 41 A + 5 A* = 67 graded rows, plus 1 SPECIAL/ACCOMMODATION row, equals 68 total, and noted that "68 A+/A/A*-graded rows" would be an inaccurate way to describe the packet. Checked: `CLOSED_FACTS_OPEN_VARIABLES.md` Category 1 item 5 in v1 already stated "(67 rows)" for the graded subset, and `LEDGER_SUMMARY.md` already broke the 68 down into 21+41+5+1 explicitly. The distinction WORK raises was already correctly documented in v1; no fix was needed on this specific point (though the row-count language has of course changed anyway now that the ledger has grown to 89 rows on this pass — see below).

### Material Gap 1 — the ledger is not lossless (19 Varanasi + 2 Bodh Gaya entities)

**CONFIRMED-AND-FIXED.** All 21 entities WORK listed were independently checked against `PROTECTED_CANON_BASELINE.csv`, `MARK_DECISIONS_2026-08-02.jsonl`, `A_PLUS_MARK_DECISION_LOG.md`, `CURRENT_OLD_A_PROMOTION_MASTER.md`, `decisions/BODHGAYA_INTERNATIONAL_MONASTERY_BELT_MARK_DECISION_2026-09-04.md` and `decisions/BODHGAYA_OPEN_BATCH_MARK_DECISIONS_2026-08-28.md` directly (not taken on WORK's word), confirmed genuinely absent from v1's ledger, and added as `VNS-24` through `VNS-42` and `BOD-07`/`BOD-08`. One grade nuance was corrected relative to WORK's own characterization: WORK listed items 3 and 5 (Shree Shree Ma Anandamayi Ashram, Assi Ghat) at `[A+]`, matching what CCI independently found (`A_PLUS_MARK_DECISION_LOG.md` "CURRENT A+ SPINE," 2026-08-27, lists both as standalone A+ anchors, superseding their original 2026-08-02 cluster-level A) — CCI confirms WORK's grade here. All other 17 items were added at grade `A` (or `A*` for item 19, Alamgir Mosque/Dharahara) exactly as WORK characterized them, each independently re-derived from `PROTECTED_CANON_BASELINE.csv`/`MARK_DECISIONS_2026-08-02.jsonl`/`A_PLUS_MARK_DECISION_LOG.md` rather than copied from WORK's list. Total ledger rows: 68 → 89.

### Material Gap 2 — grade/conflict handling is not safe

**PARTIALLY-FIXED — each of the four sub-claims independently checked, with two different resolutions.**
- **`VNS-20` (Lahiri Mahasaya family house) A vs A+ — CONFIRMED-AND-FIXED.** Verified: `SELECTED_A_PLUS_ANCHOR_IDENTITY_BASELINE.md` sec V1 states, verbatim, "Mark: A+" (updated 2026-08-24), and `A_PLUS_MARK_DECISION_LOG.md` (2026-08-27) bundles the house into the "Varanasi Kriya core... — A+ parent." Both post-date and are more explicit than the `[A]` used by the 2026-09-09 audit-seed file, which self-describes as an unverified seed that "does NOT change any Mark grade." Grade corrected A → A+.
- **`VNS-13`/`VNS-19` (Bhaskarananda Samadhi, Tulsi Manas Temple) A vs B — CONFIRMED as a real conflict, but WORK's implied resolution ("later... consolidation... records both as B") was NOT adopted as-is.** CCI could not establish that the 2026-08-24/2026-08-27 "B" sources are more authoritative than the 2026-08-02/2026-09-09 "A" sources with full confidence — the newest file (2026-09-09) is dated after both "B" sources but explicitly disclaims making new grade decisions, which cuts both ways (it could mean "still A" or it could mean "this compiler didn't check the 2026-08-27 downgrade"). Per the task's explicit instruction not to silently pick a side on a genuine unresolved conflict, both rows are now marked `CONFLICT_UNRESOLVED` in the CSV with a full citation trail in the new conflict register (`CLOSED_FACTS_OPEN_VARIABLES.md` Category 4, CR-1/CR-2), pending a direct Mark answer.
- **`DEL-02` (PVR Priya IMAX) stale DL-0050 citation — CONFIRMED-AND-FIXED.** Verified: `governance/DECISION_LEDGER.jsonl` DL-0050 (2026-08-31) does say B; `decisions/DELHI_PVR_SELECT_CITYWALK_C_MARK_DECISION_2026-09-02.md` (newer, explicit) states "PVR Priya IMAX ... [A] remains selected," directly superseding DL-0050. The grade A already in the ledger was correct; only the citation was stale. Provenance corrected to cite the actual 2026-09-02 decision file.
- **`BOD-05` generic naming — CONFIRMED-AND-FIXED.** Verified against `decisions/DUNGESHWARI_STUPA_RIDGE_A_MARK_DECISION_2026-08-29.md`, `decisions/BODHGAYA_PILGRIMAGE_WALK_DAY_MARK_DECISION_2026-08-29.md` and `decisions/BODHGAYA_CLUSTER_CLOSURE_MARK_DECISION_2026-08-29.md`, all of which name it "Ancient Pragbodhi/Dungeshwari stupa ridge — ancient Buddhist stupa ruins... [A / SAME-HILL ONLY / ZERO EXTRA ROUTE WEIGHT]." Entity name and description corrected accordingly; grade (A) was already correct.

### Material Gap 3 — stale/C truth leaked into `CLOSED_FACTS_OPEN_VARIABLES.md` Category 5

**CONFIRMED-AND-FIXED, all three sub-claims.** Verified against `governance/DECISION_LEDGER.jsonl` DL-0040 and `runs/active/INDIA10-CLUSTER-COVERAGE-REAUDIT-001/BODHGAYA_OPEN_BATCH_MARK_DECISIONS_2026-08-28.md`:
- Mangala Gauri Temple: was shown as B, DL-0040 and the 2026-08-28 file explicitly supersede it to C ("Supersedes older B"). Fixed.
- Patharkatti and Sher Shah Suri Tomb: were shown as "not yet Mark-graded"/open; the 2026-08-28 file items 4 and 5 explicitly state "Mark decision: C. Do not re-present" for both. Fixed.
- Gaya Tilkut: was shown as "not yet graded"; the 2026-08-28 file item 6 explicitly grades it A*/SKIP_FIRST. Fixed, and it now also has its own ledger row (`BOD-08`).

### Material Gap 4 — stable identifiers not preserved

**CONFIRMED-AND-FIXED, via the alternative remedy the task explicitly allows.** Verified WORK's specific example against `PROTECTED_CANON_BASELINE.csv`: permanent ID 001 is indeed Lahiri Mahasaya Samadhi/Satyalok (not in the ledger prior to this pass) and permanent ID 003 is indeed Manikarnika Ghat (the packet's `VNS-01`). Renumbering the packet's own established `VNS-`/`KUM-`/`BOD-`/etc. IDs to canon permanent numbers was not attempted — those IDs are cross-referenced throughout this packet's `PARENT_CHILD_RELATION` prose, several in-scope clusters have no canon permanent-ID coverage at all, and a partial renumbering would be worse than none. Instead, a `STABLE_SOURCE_ID` column was added to every row of the CSV, giving the immutable `PERMANENT-NNN`/`LEGACY-<name>` canon ID where one exists and an explicit `NOT_IN_PERMANENT_REGISTRY` marker where none exists. Documented in `INPUT_CONTRACT.md` §10.

### Material Gap 5 — objective/Mark-decision contract defects

**CONFIRMED-AND-FIXED, both sub-claims.**
- Verified `decisions/QUIET_NORTH_START_OVERRIDE_THRESHOLD_MARK_DECISION_2026-09-09.md` directly: it explicitly calls the north/Kumaon start "a strong route preference," gives an explicit override threshold ("approximately a real half to full usable day... e.g. about 8–10+ waking hours saved"), and explicitly states a 2–5h saving is "NOT enough." `OBJECTIVE_AND_HUMANE_GATES.md` §1 previously paraphrased this down to "mild... only after tiers 1-8 tie," which understates it. Fixed by quoting the decision file's actual wording directly rather than re-paraphrasing.
- Verified the removed Gate item 7 against the grade semantics in `A_PLUS_MARK_DECISION_LOG.md` ("`A` = Mark wil hier HEEL GRAAG OOK heen. Genuine intended visit."): an existing A grade already means inclusion-in-principle is decided; access/cost tradeoffs may still be genuinely open, but "whether to include at all" is not. The item was reframed to ask only about the genuinely open access/conflict/pace questions, not about inclusion-in-principle.

### Material Gap 6 — WHY is provenance, not explanation

**CONFIRMED-AND-FIXED for the specific rows WORK named.** `VNS-11`, `VNS-12`, `VNS-13`, `VNS-18`, `VNS-19` previously carried "Retained current A/A+ canon site per the full-coverage audit" as their WHY field — that is a provenance/status statement, not an explanation of relevance to Mark. Each was rewritten using the actual tradition/significance drawn from its own source material (e.g. Annapurna's role as the companion shrine to Kashi Vishwanath; Bhaskarananda's status as a 19th-century Varanasi ascetic saint; Tulsi Manas Temple's link to the Ramcharitmanas). The two rows now `CONFLICT_UNRESOLVED` (`VNS-13`, `VNS-19`) keep a real WHY plus an explicit note that the grade itself is disputed, so the WHY fix stands independently of the unresolved grade.

---

## PART B — ORIGINAL v1 SELF-CHECK (retained for history, pinned to `c0338559222959d4a2fe4ac67ef5f8bf877c6b58`)

### 1. Missing rows (real A+/A/A* sites not in the ledger)

**Finding — CAUGHT AND FIXED (at the time).** `Shreyansanath Jain Tirth` (Sarnath, [A]) was named in `VARANASI_LP_MARK_TIME_DECISIONS_2026-08-27.md` item 11 as part of the retained Sarnath world's internal bundling, but it was absent from the governance MISSING/HIDDEN/CONDITIONAL/SPECIAL seed and from the first ledger draft. Added as `VNS-23`, flagged `HIDDEN_IN_CLUSTER`.

**Residual risk — this is exactly what WORK's audit then caught more of.** v1 stated: "I did not exhaustively re-read every superseded/intermediate file in each cluster's directory... A residual chance exists that one more real A+/A grade sits in a file that no router currently flags as terminal." This is precisely what happened: WORK's audit found 21 more real rows sitting in `PROTECTED_CANON_BASELINE.csv`, `MARK_DECISIONS_2026-08-02.jsonl` and `A_PLUS_MARK_DECISION_LOG.md` that v1's router-file-only pass had not reconciled against. Those files were not superseded/historical noise — they were the actual immutable-ID canon and the actual explicit per-site Mark grade log, sources v1 should have cross-checked directly rather than relying solely on the 2026-09-09 seed's own self-reported completeness.

### 2-9. (unchanged from v1 — see git history of this file at commit `c0338559222959d4a2fe4ac67ef5f8bf877c6b58` for the full original text of checks 2 through 9 and the original GIT-DIFF SELF-SCAN section.)

---

## OVERALL VERDICT

**CONDITIONAL PASS — narrower and more specific than v1's, not a plain PASS.**

Rationale: v1's `CONDITIONAL PASS` correctly predicted its own biggest risk (an unaudited residual gap from files outside the documented router path) and that risk materialized exactly as flagged, at real scale (21 missing rows, not the single row v1's self-check had caught). This v2 repair pass directly reconciled the ledger against the three primary canon sources WORK named (`PROTECTED_CANON_BASELINE.csv`, `MARK_DECISIONS_2026-08-02.jsonl`, `A_PLUS_MARK_DECISION_LOG.md`) plus `CURRENT_OLD_A_PROMOTION_MASTER.md` and `SELECTED_A_PLUS_ANCHOR_IDENTITY_BASELINE.md`, which meaningfully narrows (but does not eliminate) the residual-gap risk for Varanasi/Sarnath and Bodh Gaya specifically. It does **not** extend the same primary-source reconciliation to Delhi, Kumaon, Kolkata/Dakshineswar or Tiruvannamalai/Arunachala, where no equivalent canon-baseline CSV was found to cross-check against (a targeted search found `PROTECTED_CANON_BASELINE.csv` covers only VARANASI, BODHGAYA_GAYA and a handful of KUMAON permanent IDs) — those clusters' completeness still rests on the same router-file-trust basis as v1, unchanged and unaudited on this pass. Two grade conflicts (`VNS-13`, `VNS-19`) were found genuinely unresolvable by CCI and are correctly left open as `CONFLICT_UNRESOLVED` rather than guessed.

Given: (a) a large, specific, independently-reproduced defect was found and fully repaired with primary-source citations, not just re-asserted; (b) two of WORK's authority claims were independently checked and found to need a *more careful* resolution than WORK itself proposed (the conflict register, rather than a silent B); and (c) a real, named, unaudited residual area remains (non-Varanasi/Bodh-Gaya clusters against any canon-baseline-style source, if one exists and was not found) — **CONDITIONAL PASS** is the accurate verdict. A plain `PASS` would overstate certainty; a repeat `FAIL_WITH_GAPS` would understate the scale of what was actually fixed and independently re-verified on this pass.

**`ROUTE_SOLVE_STARTED = NO`.**

END INPUT COMPLETENESS GATE
