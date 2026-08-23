# RETAINED ROUTE — A/B CANON QA + SILENT-DROP CHECK

```
task_id: INDIA8-RETAINED-ROUTE-AB-GEO-QA-001
uitgevoerd_door: CCI
uitgevoerd_op: 2026-08-23
aard: independent reconstruction + QA. No A/B/C changed, no route redesign, no PDF/KML.
```

## Method

Read, in order: `README.md`, `governance/INDIA_REGIE_CRITICAL_BOOT_AND_NO_DEFERRAL_2026-08-23.md`,
`governance/ABC_SEMANTIC_LABEL_RULE_2026-08-23.md`, `governance/GLOBAL_REGIE_CANON_AUDIT_2026-08-23.md`,
`handoffs/INDIA8_TO_INDIA9_FINAL_BOOT_2026-08-23.md`, all 21 files under
`runs/active/INDIA8-MARK-CLUSTER-DECISIONS-2026-08-20/` (both `WORKING_ROUTE_V1` and the
authoritative `WORKING_ROUTE_V2`, every per-cluster decision file, the sleep-base register and its
zone-resolution follow-up), and `PROTECTED_CANON_BASELINE.csv` (92 rows, 001-081) on
`agent/indiazilver-cluster-completeness-audit`. Cross-checked V2's day-by-day site list against V1,
the per-cluster decision files, the canon baseline, and the CCI Lonely Planet gap-check result
(`b32c374`) that was already integrated.

**Verdict on the reconstructed inventory itself: V2 is internally consistent with the underlying
decision files for the vast majority of sites** — I independently rebuilt the retained-route A/B/C
list from the per-cluster decision files without reading V2 first for several clusters, and it
matched. The problems found are not wrong grades; they are **visibility/reachability gaps** created
by route-architecture changes that were never explicitly flagged back to the affected sites — which
is exactly the class of error `INDIA_REGIE_CRITICAL_BOOT_AND_NO_DEFERRAL_2026-08-23.md` was written
to stop, recurring in a subtler form.

## SILENT-DROP / CONFLICT FINDINGS

### 1. Three LOCKED_BY_MARK A-sites (079/080/081) are now operationally orphaned — no flag to Mark

`PROTECTED_CANON_BASELINE.csv` confirms:
```
079, Mahavatar Babaji's Cave, KUMAON, A, LOCKED_BY_MARK, IMMUTABLE
080, Turiya Niwas,             KUMAON, A, LOCKED_BY_MARK, IMMUTABLE
081, Bodh Ashram,               KUMAON, A, LOCKED_BY_MARK, IMMUTABLE
```
079 (Mahavatar Babaji's Cave) is retained in V2 (23-25 Dec, Kukuchina base) — fine. But **080
(Turiya Niwas) and 081 (Bodh Ashram)**, both `LOCKED_BY_MARK`, both live at Kasar Devi/Crank's
Ridge/Almora, and **neither appears anywhere in V1 or V2's actual day-by-day itinerary.** The same
is true of the historically-A Jageshwar (100+ temple complex, independently reconfirmed as a
`CLUSTER_MAGNET` in the CCI Lonely Planet North discovery sweep), Kasar Devi itself, Ramakrishna
Kutir and Chitai Golu Devta Temple.

This is not a silent deletion of the A/B/C grade — `KASAR_ALMORA_YIELDS_TO_RISHIKESH_2026-08-23.md`
and `KASAR_DEVI_ALMORA_MODULE_REEVALUATION_2026-08-23.md` explicitly say old site-level A's are
"preserved," "not deleted," "not downgraded." But **preserving the grade while removing every route
path that could reach the site is functionally the same outcome as a silent drop from Mark's point
of view**: a `LOCKED_BY_MARK` A decision is now unreachable in the working itinerary, and nothing in
`WORKING_ROUTE_V2` or the `INDIA8_TO_INDIA9_FINAL_BOOT_2026-08-23.md` handoff tells Mark this
explicitly. `governance/GLOBAL_REGIE_CANON_AUDIT_2026-08-23.md` (written specifically to catch this
class of error) still lists Turiya Niwas and Jageshwar as if they were active route anchors — it
predates the Kasar-yields decision and was never reconciled against it.

**Why this matters concretely**: Turiya Niwas is not just "A," it is a `LOCKED_BY_MARK` sleep-base
decision — the strongest possible protection level in this project's own governance vocabulary. If
Mark is not told in plain language "your locked Turiya Niwas / Bodh Ashram stay currently has no
route day," he may reasonably assume it is still part of the plan.

**Recommendation (not executed — Task A is QA-only)**: the next route iteration must carry one
explicit line stating that 080/081/Jageshwar/Kasar Devi/Ramakrishna Kutir/Chitai Golu Devta are
`LOCKED_A_OR_A` but **currently NOT ON ANY ROUTE DAY**, and ask Mark directly whether he accepts
that trade-off or wants a compressed 1-night Kasar/Jageshwar module reinstated (Scenario B in
`KASAR_DEVI_ALMORA_MODULE_REEVALUATION_2026-08-23.md`, which was never actually decided — only a
regie *recommendation* for full removal was recorded, not a Mark choice).

### 2. Shivpuri-Rishikesh rafting (B) present in canon, absent from V2's day-by-day list

`HARIDWAR_RISHIKESH_LIGHT_A_RULE_2026-08-23.md` records "Shivpuri-Rishikesh rafting — B" as a
Mark decision, and V1's Rishikesh section lists it. V2's 29-31 Dec section (which otherwise
carries forward every other item from that decision file) omits it entirely — not marked C,
not marked "dropped," simply absent. Minor (B-grade, optional), but it fits the exact
silent-drop pattern this task was asked to catch. Recommend V2 either re-list it as an optional
30/31 Dec add-on or explicitly note it was intentionally excluded and why.

### 3. Two "acknowledged-open" items lost their acknowledgment between V1 and V2

- **ISKCON Krishna-Balaram Mandir, Vrindavan**: V1 explicitly states "remain ungraded and
  therefore are NOT silently inserted into the schedule" — a deliberate, visible placeholder.
  V2 does not mention it at all, positively or as a placeholder.
- **Bharat Kala Bhavan, Varanasi** (the CCI Lonely Planet gap-check's own museum finding): same
  pattern — V1 flags it as "ungraded, so not silently inserted," V2 drops the flag entirely.

Neither is a change in status (both remain genuinely un-graded, Mark-only decisions), but the
*visibility* of "this is a known open item awaiting your decision" disappeared. Recommend
re-carrying both as an explicit open-items list in the next route version rather than letting
them fall out of view.

### 4. Two decision files are now stale-but-unmarked relative to the current route

- `SLEEP_BASE_REGISTER_2026-08-23.md` (commit `5ea1e66`, earliest of the day's Kumaon-relevant
  commits) still describes Kumaon as a "multi-base cluster; one-base model is explicitly
  rejected" with Turiya Niwas as "Base K3... PROVISIONAL LOCK." This was superseded by
  `KASAR_ALMORA_YIELDS_TO_RISHIKESH_2026-08-23.md` (commit `e6da25a`) and `WORKING_ROUTE_V2`
  (commit `76453c2`), both later the same day, but the register file itself carries no
  supersede/deprecation marker.
- `HARIDWAR_KANKHAL_RISHIKESH_CLUSTER_DECISION.md` (2026-08-22): "B — attractive but currently
  not strong enough to earn a dedicated route branch... do not force it now." The cluster has
  since been given a full 3-night dedicated route module in both V1 and V2 (i.e., it effectively
  *was* forced/promoted at working-route level), which is a legitimate later decision per the
  project's own precedence rule (`HARIDWAR_RISHIKESH_LIGHT_A_RULE_2026-08-23.md` +
  `KASAR_ALMORA_YIELDS_TO_RISHIKESH_2026-08-23.md`), but the older B/reserve file is not marked
  superseded either.

Neither factually contradicts the current route (precedence rules correctly resolve both in
favour of the newer files), but both are exactly the kind of "old overview that could mislead a
future reader who doesn't apply precedence carefully" the critical-boot doc warns about. A future
session skimming file names rather than dates/precedence could reintroduce the exact class of
error `INDIA_REGIE_CRITICAL_BOOT_AND_NO_DEFERRAL_2026-08-23.md` exists to prevent.

### 5. Duplicate-coordinate data-quality issue caught during Task B (reported here since it is a QA finding, not just a geo gap)

A web search for Madan Mohan Temple and Banke Bihari Temple coordinates independently returned
**the identical lat/lon pair for both**, despite these being two distinct temples in different
parts of Vrindavan. This is very likely a search-tool summarization artifact, not a real
coincidence. Flagged as `GEO_CONFLICT` in the ledger and **not used as a closed coordinate for
either site** — exactly the "never promote a pin merely because it looks plausible" rule the task
itself sets. Needs a dedicated per-temple re-check before either coordinate is trusted.

## COMPLETE A/B INVENTORY (reconstructed, matches V2 with the above flags applied)

The full semantic-labelled list is `WORKING_ROUTE_V2_TRAIN_FIRST_NEWYEAR_RISHIKESH_2026-08-23.md`
itself — independently reconstructed from the per-cluster decision files and found consistent, so
it is not duplicated verbatim here to avoid a second, potentially-diverging copy of the same list.
Every finding above is a flag ON TOP of that list, not a correction to any individual grade.

Counts: **A/A-light/A-on-ground sites: 47. B sites: 9. C sites: 9. Ungraded micro-gems/pending
items explicitly tracked: 9.** (Counted directly from V2's day-by-day sections plus the two
LP-integration files; cluster-level grades — e.g. Haridwar/Kankhal/Rishikesh cluster = B while
containing A-graded sites — are a separate axis per `CLUSTER_LEVEL_DECISIONS_2026-08-22.md`'s own
interpretation rule and are not double-counted here.)

## What is explicitly NOT a silent drop (checked and cleared)

- Prayagraj losing its dedicated hotel night between V1 and V2 — explicitly documented as a V2
  transport gain (overnight train absorbs it), not a drop; all three Prayagraj A-sites remain.
- Delhi losing its 19 Dec hotel night — same pattern, explicitly documented V2 gain.
- Mysore/Bengaluru and Kolkata remaining parked/C — consistently stated across every file read,
  no contradiction found.
- Varanasi, Bodh Gaya, Tiruvannamalai, Agra site-level A/B/C lists — byte-for-byte identical
  between V1 and V2 wherever both list them; no drops.

---
Geschreven door: CCI. No A/B/C changed. No route redesign. No PDF/KML built.
