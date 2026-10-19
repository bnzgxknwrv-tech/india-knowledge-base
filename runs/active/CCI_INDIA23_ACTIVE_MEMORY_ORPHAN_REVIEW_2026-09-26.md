# CCI — INDIA23 ACTIVE-MEMORY ORPHAN REVIEW + MINIMAL SUCCESSOR PATCH

Task: PR #23 comment `5846889930`.
Input parity artifact: `runs/active/INDIA23_ACTIVE_MEMORY_PARITY_2026-09-26.md` (commit `58a1117`).
Central branch at review time: `agent/india8-cluster-casting`.
No central-required file is changed by this task (review-only, per instruction).

## 1. VERDICTS ON THE THREE FLAGGED FILES

CCI independently opened and read all three files in full (not just INDIA23's summary) plus the current `BOOT_MANIFEST_V8.json` `central_required` list (16 files) to check what is and isn't already lossless there.

### 1.1 `governance/PERMANENT_PLACE_NUMBER_RULE_2026-09-13.md`
**Verdict: REAL_ORPHAN.**
Confirmed: this file's rule (one permanent `A###` id per place, never renumbered, must appear on every occurrence) does not exist anywhere in the current 16-file central-required set. `HOW_TO_WORK_WITH_MARK.md` §5 (recognition-rich naming) and §12 (day-block contents) are the closest neighbors, but neither mentions a permanent numeric ID at all. INDIA23's verdict is correct.

### 1.2 `governance/CCI_GITHUB_WAKE_RELAY.md`
**Verdict: PARTIAL_GAP.**
The broad principle "Mark is not the courier between INDIA and CCI" is already present (`CCI_COLLABORATION_PROTOCOL.md` roles section, itself also not central-required — see 1.3). What's missing from the mandatory layer specifically is the *mechanical* fact: a single top-level PR #23 `CCI_TASK` comment is itself a proven wake trigger, and posting a duplicate task because no result is visible yet risks duplicate work. `HOW_TO_WORK_WITH_MARK.md` §18 (RELAY/AUTHORSHIP) covers relay *format* (`INDIA<n> zegt:` / `/INDIA<n>`) but not this operational fact. INDIA23's verdict is correct.

### 1.3 `governance/CCI_COLLABORATION_PROTOCOL.md`
**Verdict: PARTIAL_GAP.**
Confirmed not in central_required. The rationale-first delegation rule (`decisions/INDIA_TO_CCI_RATIONALE_FIRST_DELEGATION_RULE_2026-09-14.md`, already central-required since this session's own orphan-scan) captures *how a task should be framed*, but not the underlying *role definition* — that CCI is "a second pair of eyes and worker, not a compliance department," may challenge INDIA, and that direct central writes by CCI are exceptional, not default. INDIA23's verdict is correct.

## 2. MINIMAL SUCCESSOR-ROUTING PATCH (DESIGNED, NOT APPLIED)

Per instruction, no central-required file is touched in this task. This is the exact patch text to apply at the next safe governance batch moment (e.g. as part of the INDIA23→INDIA24 transition, alongside whatever else needs a fresh boot anyway) — chosen to be **lossless integration into existing central owners**, not new files, to avoid boot-bloat:

### Patch A — `governance/HOW_TO_WORK_WITH_MARK.md` §12 (DAY PLANS / PDF)
Insert one bullet into the existing per-place list (after the "recognition-rich name + grade/status" bullet):
```
- permanent `A###` identifier, never renumbered across days/PDFs/order changes (`governance/PERMANENT_PLACE_NUMBER_RULE_2026-09-13.md`), shown on every occurrence;
```

### Patch B — `governance/HOW_TO_WORK_WITH_MARK.md` §18 (RELAY / AUTHORSHIP)
Append after the existing relay-format text:
```
A single top-level `CCI_TASK` posted as a PR #23 comment is itself the wake trigger — Mark does not need to manually start Claude Code, and INDIA must not post a duplicate task merely because a result is not yet visible (`governance/CCI_GITHUB_WAKE_RELAY.md`).

CCI is a second pair of eyes and bounded researcher/reviewer, not a compliance department: it may challenge INDIA's approach, and its default working pattern is `INDIA task -> CCI worker/review -> INDIA judgment -> central update when useful`. Direct central writes by CCI are exceptional, not the default (`governance/CCI_COLLABORATION_PROTOCOL.md`).
```

### Disposition of the three source files
Mark the three files with a one-line banner once the patch above lands: `Core integrated into governance/HOW_TO_WORK_WITH_MARK.md §12/§18 on <date>; this file remains as detail/provenance, not a separate required boot read.` This prevents a future orphan-scan from re-flagging them as leaks while preserving their fuller text as backup detail.

### Does this force a new FULL re-pin?
**Yes, but only for the *next* boot, not retroactively for INDIA23's current session.** Editing `HOW_TO_WORK_WITH_MARK.md` (a `central_required` file) changes its blob SHA, which changes the `central_required` blob-map used by `find_prior_full_check_match()` in `validate_independent_check.py`. That means:
- INDIA23's own already-granted `CONTENT_AUTHORIZATION: GRANTED` (this session, `boot_head_final=324456e`) is unaffected — authorization is evaluated once per session at its own pinned snapshot, not continuously re-validated against a moving HEAD.
- The *next* fresh session (INDIA24) will see a changed `central_required` blob-map, so no prior FULL check will match it — INDIA24 will correctly be forced into a fresh FULL check (never LIGHT) the first time it boots after this patch lands. That is the intended, correct behavior, not a bug to route around.
- This is exactly why the task instruction says apply the patch "at the next safe governance batch moment / session transition" rather than mid-session: doing it now would not break INDIA23's current authorization, but it would be an unnecessary central write in the middle of an unrelated review task, and `BOOT_MANIFEST_V8.json`'s own central_required note pattern (see the `_central_required_note` field) expects each such change to be deliberate and dated, not incidental.

## 3. `governance/CURRENT_FRONTIER.md` STALENESS — VERIFIED AND EXACT MINIMAL SYNC

CCI independently re-read the full current file (last updated 2026-09-14) against `governance/CURRENT_TRUTH.md` (23 Sep) and the relevant decision files. Confirmed stale, itemized exactly:

1. **"LIVE WORK IN PROGRESS — DO NOT DUPLICATE" section (Kumaon 20-23 Dec sleep-base note)** — resolved. The hotel-base fix this note asks for was already done (commit `f84bcd5`, "Fix 23-25 Dec hotel base: adiMOUNT (not Dunagiri/Kukuchina)"). This entire section should be deleted.
2. **Open-decisions item 3, "Turiya Niwas ... still pending"** — stale. Decided 2026-09-21 (A\* → B, removed from active planning; `decisions/INDIA22_TURIYA_NIWAS_DOWNGRADE_MARK_DECISION_2026-09-21.md`). Remove from the open list.
3. **Open-decisions item 6, "Lala Badri Shah House ... not yet presented to Mark for a grade"** — stale. Declined 2026-09-21 (`decisions/INDIA22_LALA_BADRI_SHAH_HOUSE_DECLINED_MARK_DECISION_2026-09-21.md`). Remove from the open list.
4. **Closed-items example line: "Jageshwar (out), Dhokaney (out)"** — Dhokaney is wrong. `CURRENT_TRUTH.md` shows "RESTORED BY MARK 2026-09-16 — Dhokaney Waterfall = A\*, optional zero-time reserve." Change to "Jageshwar (out), Dhokaney (restored A\*, optional reserve)".
5. **Missing entirely: the current immediate frontier.** The file's "REAL OPEN DECISIONS" list is trip-wide and does not mention that 28-31 Dec is now a definitively locked corridor (`decisions/INDIA22_HAIDAKHAN_GHAZIABAD_GREATER_NOIDA_VRINDAVAN_AGRA_DEFINITIVE_LOCK_2026-09-23.md`) or that the immediate next task is the post-Taj 31-Dec Agra→Gaya/Bodh Gaya transport solve. Add one line under "CURRENT PROJECT PHASE" naming this as the active frontier, pointing to `governance/CURRENT_TRUTH.md` for the exact chain.
6. Bump "Last updated" to the date this sync actually lands.

Items NOT stale (verified still genuinely open, keep as-is): Bodh Gaya 2-vs-3 / Tiruvannamalai 5-vs-4 trade-off; Evam Choskhorling visit permission; the December Crank's Ridge walk guide confirmation; J.C. Bose site identity; Jama Masjid + astrologer/Jyotish; booking/contact not started.

This file is also `central_required` and the sole `active_cluster_required` entry, so the same "apply at next safe batch moment, not mid-task" logic in §2 applies — not touched in this review.

## 4. NO CENTRAL WRITE IN THIS TASK

Confirmed: this artifact is the only file this task creates, under `runs/active/`, not `governance/` or any `central_required`/`active_cluster_required` path. INDIA23's current `CONTENT_AUTHORIZATION: GRANTED` is untouched by this task.

CCI_RESULT to follow on PR #23 with this artifact's path and a compact summary.
