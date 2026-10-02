# CCI MASTER QA REPORT — ALL_FINDINGS_LOCATION_MASTER

```
task_id: CCI-MASTER-QA-ALL-FINDINGS-001
role: independent QA/reconciliation partner (not a new color/workstream)
uitgevoerd_door: CCI
uitgevoerd_op: 2026-08-20
central_branch_audited: agent/india8-cluster-casting
central_task: runs/active/INDIA8-ALL-FINDINGS-LOCATION-CLOSURE-001/CCI_MASTER_QA_TASK.md
method: cross-branch read-only inspection + commit-SHA/blob verification, no merge, no A/B/C, no route
```

## MASTER_QA_VERDICT: **PASS_WITH_FIXES**

The underlying discipline, entity modeling and per-family execution are rigorous and, everywhere
sampled, verifiably correct — no silent drops, no fabricated coordinates, no claimant-tradition
collapse, no micro-site absorption, no historic/successor conflation were found. However, the
literal deliverable named in the QA task — "the central-master construction" — **does not yet exist
as a single, queryable, row-level artifact**. What exists on `agent/india8-cluster-casting` is a
schema, a source ledger, a prioritized unresolved-queue seed, and six per-color feed summaries that
correctly cite real commits on six separate branches. The actual row-level
`ALL_FINDINGS_LOCATION_MASTER` (per the columns defined in
`ALL_FINDINGS_LOCATION_MASTER_SCHEMA.md`) has not been assembled yet — this is explicitly still the
"NEXT" step per `FINAL_FEED_MANIFEST.md` itself, not a hidden gap I am the first to notice. This is
the reason for `PASS_WITH_FIXES` rather than a clean `PASS`: the fixes are about *finishing
consolidation*, not about *correcting mistakes found in what exists*.

## 0. Method — what I actually verified, not just read

I did not just read the central branch's own summary claims at face value. For a representative
sample I:
- Verified via `list_commits`/`get_commit` (direct GitHub API, not an unauthenticated proxy) that
  cited commits are real, on the stated source branches, and touch the stated files with the stated
  line counts — sampled across BLAUW, TURQUOISE, ROOD, WIT, and ZILVER (5 of 6 families; GEEL's
  underlying commits were already independently verified by CCI in CCI_TASK 095 two turns ago in
  this same session).
- Fetched the ZILVER family's actual final CSV/markdown content directly from its home branch
  (`agent/indiazilver-cluster-completeness-audit`) — not just the central branch's secondhand
  summary — because the central directory's `FEED_INDIAZILVER_PARTIAL_...md` turned out to describe
  an **earlier, superseded** ZILVER state (different commit SHAs than `FINAL_FEED_MANIFEST.md`
  cites); the central branch itself does not contain the ZILVER task directory at all (it lives only
  on ZILVER's own branch, read cross-branch per the governance's explicit allowance).
- Independently reproduced the existing Varanasi A/B/C split (32×A / 5×B / 3×C for 001-040) by
  counting ZILVER's `PROTECTED_CANON_BASELINE.csv` row-by-row and comparing the total against
  `governance/ACTIVE_STATE.md`'s own stated split — **exact match**, a genuine independent check, not
  a re-read of the same claim.
- Cross-checked Bodh Gaya (046-078: `051=C`, `061=C`, `074=C` all "reconfirmed after delta") and
  Kumaon (079/080/081: all `A`, `LOCKED_BY_MARK`, "Do not infer GPS") against my own prior knowledge
  of `ACTIVE_STATE.md` — exact match on both.
- Read the raw `PROXIMITY_1KM_3KM_MATRIX.csv` line-by-line rather than trusting only the summary's
  "16 pairs / 7 tight / 0 guessed" claim — the raw file's own internal summary rows match the
  external claim exactly, and no row in between fabricates a distance for an `UNKNOWN` coordinate
  pair.

## 1. Checklist verdict, item by item (Mark's explicit "controleer vooral" list)

| item | verdict | evidence |
|---|---|---|
| nul silent drops | **PASS (per-family), OPEN (global)** | All 5 sampled families explicitly claim and substantiate `SILENT_DROPS=0` with traceable commit refs. No global accounting equation has been computed across all families combined yet — see P0-1. |
| iedere source claim krijgt een disposition | **PASS (per-family), OPEN (global)** | R1-R5/duplicate/negative dispositions consistently present everywhere sampled; global roll-up pending, same root cause as above. |
| micro-sites niet geabsorbeerd in parent-complex | **PASS** | TURQUOISE's explicit rule ("rooms, verandas, cremation spots, memorials... must NOT be silently deduplicated into the parent") is consistently applied — Kainchi, 4 Church Lane, Sri Ramanasramam, Dakshineswar, Cossipore, Karar Ashram, Fouzdar Kunj, Shyampukur all correctly keep children (`KEEP_CHILD`) distinct from parents in ZILVER's own proximity/ID matrix. |
| historical successor niet vals als hetzelfde gebouw behandeld | **PASS** | Regent Hotel 1936 vs. current same-name hotel is explicitly `SAME_NAME_NOT_PROVEN_SUCCESSOR`, kept **separate**, not merged. Same discipline applied to Ghurni original estate vs. Jaleshwar successor shrine, Serampore historic Priyadham terrain vs. current Smriti Mandir, Panthi's demolished plot vs. room, NKB Akbarpur birth site vs. the 2001 temple — all correctly `R2`/successor-flagged, not silently upgraded to `R1`. |
| Babaji claimant traditions gescheiden | **PASS** | Explicitly enforced with a dedicated "Babaji claimant-tradition ABC guard" section: Dunagiri/YSS Pandukholi cave, Haidakhan Vishwa Mahadham, Parangipettai Nagaraj Mandir, and the unnamed 1861 initiation cave are all kept as four separate claimant families, each with "never merge" language, and the dedup of the *current* YSS cave against permanent ID `079` is explicitly scoped to "current claimant site," not historical proof. |
| R4/R5 zichtbaar gehouden | **PASS (preservation), PARTIAL (visibility)** | Nothing is dropped — every unresolved item is preserved either individually (`GLOBAL_UNRESOLVED_QUEUE_SEED.md`) or by exact count + source-commit reference (e.g. ROOD's "54 R4 + 25 R5... source commit `cd817119` remains authoritative"). But the queue seed is explicitly labeled a prioritized **seed**, not the full expansion — Mark cannot yet see all ~79+ unresolved ROOD records, or the full GEEL R4/R5 set, in one place. See P1-1. |
| bestaande IDs 001-081/A-B-C/locks onaangetast | **PASS, independently reproduced** | See §0 — exact match on Varanasi 32/5/3 split, Bodh Gaya 046-078 statuses, Kumaon 079-081. No file anywhere in my sample renumbers, reuses, or silently changes an existing ID or A/B/C. |
| AOAY P0-scenes zichtbaar | **PASS** | BLAUW's feed explicitly closes several high-priority P0 AOAY scenes (Haridwar ch.4 split into station/detention-bungalow/not-reached-Rishikesh; Vrindavan ch.11 Madanamohana Temple; Regent Hotel Bombay third-floor scene). `GLOBAL_UNRESOLVED_QUEUE_SEED.md` Priority 1 keeps the rest explicitly visible, not hidden. |
| heritage rooms/stays niet verloren | **PASS** | Hotel Evelyn (hotel/cave-room/patio kept as 3 distinct rows), Jaipuria Bhawan, K.K. Sah house, 4 Church Lane (parent + room + hall + veranda + kitchen), Fouzdar Kunj (building + room + veranda) are all explicitly tracked at room level. WIT's Kankhal finding is a good positive example of correct nuance: the historic bedroom is flagged `HERITAGE_VISITABLE`, explicitly **not** accommodation, while the adjacent International Centre is separately flagged as currently offering accommodation — the two are not conflated. |
| proximity alleen waar ZILVER betrouwbare coordinate pairs heeft | **PASS, directly verified** | Read the raw `PROXIMITY_1KM_3KM_MATRIX.csv`, not just the summary: every `PARENT_CHILD`/`SUCCESSOR_SITE` relation with unknown coordinates correctly shows `coordinate_a/b_status: UNKNOWN` and `distance_km: UNKNOWN` — no fabricated number. Only rows where both endpoints carry a `TRUSTED_HERITAGE_COORD`/`CONFIRMED_MARKER`/`CONFIRMED_EXACT_ENTITY`/`WORKING_PIN_25_100M` status get an actual computed distance. Summary row states "0 guessed coordinates" and this is borne out by the raw data. |

## 2. Additional integration defects found (beyond the checklist)

1. **`FEED_INDIAZILVER_PARTIAL_GEEL_TURQUOISE_INTEGRATED.md` on the central branch is stale.** It
   cites ZILVER commits (`70b5fc0f...`, `92a96bf3...`, `1c218773...`, `befb91bd...`, `cfb7e480...`)
   that are an **earlier** ZILVER state than what `FINAL_FEED_MANIFEST.md` cites
   (`f491be93...`, `a0f199fb...`, `7ddcb764...`, `c64c6707...`, `118cacae...`). Both files coexist on
   the central branch; a reader who trusts the "PARTIAL" file's proximity conclusion ("no fabricated
   numeric claims were added") would miss that the final state does contain 16 real numeric pairs.
   Not a data error — a documentation-ordering trap.
2. **`MASTER_INGEST_STATE.md` is stale relative to `FINAL_FEED_MANIFEST.md`.** It still says
   `ZILVER: CURRENT INPUTS EXHAUSTED — awaiting only additive WIT+ROOD ingest`, while
   `FINAL_FEED_MANIFEST.md` (same branch, same directory) already shows all six families
   `COMPLETE`/`READY_FOR_CENTRAL_MASTER`. Low severity, but a future session bootstrapping from
   `MASTER_INGEST_STATE.md` alone would think ZILVER is still blocked.
3. **No `FEED_INDIAZILVER_FINAL_COMPLETE.md`** exists in the central directory, unlike WIT which
   correctly got a superseding `FEED_INDIAWIT_FINAL_COMPLETE.md` when its state changed. ZILVER's
   final state is only referenced secondhand inside `FINAL_FEED_MANIFEST.md`; I had to go to
   ZILVER's own branch directly to verify it. This is the same class of gap as #1/#2 — the central
   branch's own paper trail lags its actual state.
4. **Minor count discrepancy, not a defect**: ROOD's `CORE_KRIYA_SOURCE_RECORDS.jsonl` commit shows
   179 line additions, while the accounting text says "178 source records." Almost certainly a
   trailing-newline/header artifact, but worth a one-line confirmation before treating 178 as exact
   in the eventual global accounting equation.
5. **Anandamayi 108-vs-156 overlap status is honestly unresolved, not swept under the rug** —
   `SOURCE_LEDGER.md` itself says the 108 source-first additions "are NOT to be treated as already
   deduplicated against the external 156." This is correct caution, not a defect, but it means
   Anandamayi-heavy clusters (Vrindavan, Kankhal) cannot close their accounting equation until this
   specific dedup question is resolved — flagging it so it is not forgotten once the master build
   starts.

## 3. What I did NOT find (explicitly, since absence-of-evidence needs to be stated for a QA report)

- No instance of a source claim disappearing without a disposition.
- No instance of a physically distinct micro-site silently merged into its parent's row.
- No instance of a historic structure being treated as identical to a modern successor without an
  explicit R2/successor flag.
- No instance of two different Babaji claimant traditions being pooled or cross-inheriting
  evidence/tier.
- No instance of an existing permanent ID (001-081), A/B/C, or lock being changed, renumbered, or
  reused.
- No instance of a fabricated or guessed coordinate feeding a proximity claim.
- No new A/B/C decision made on Mark's behalf anywhere in the six families or the ZILVER staging
  queue — every review candidate is explicitly `MARK_REVIEW_REQUIRED` with a reason attached, not a
  pre-baked answer.

## 4. Required fixes, ordered

**P0 — must close before any cluster is presented for a new Mark A/B/C round (per the task's own
`MARK-READY GATE`):**
1. Actually assemble the row-level `ALL_FINDINGS_LOCATION_MASTER` (the schema's own column list) by
   pulling the real content from all six branches into one file/table — not just the six summary
   digests currently on the central branch. This is the literal object the QA task asked me to
   audit, and it does not exist yet.
2. Compute the one global accounting equation
   (`TOTAL_SOURCE_ROWS = PHYSICAL_ENTITY_LINKED + DUPLICATE + NEGATIVE/NONPRESENCE + UNRESOLVED`)
   across all families combined, not just per-family. Until this closes, "zero silent drops" is five
   separate honest claims, not one verified whole.

**P1 — should close soon, does not block currently staged parallel work:**
3. Expand `GLOBAL_UNRESOLVED_QUEUE_SEED.md` from a prioritized seed into the actual full R4/R5
   listing (or link every family's full closure doc directly from it) before Fase C ("onderzoek ALLE
   R4/R5-records gericht") can be marked complete for any cluster.
4. Refresh `MASTER_INGEST_STATE.md` to match `FINAL_FEED_MANIFEST.md`'s current state, and add a
   `FEED_INDIAZILVER_FINAL_COMPLETE.md` to the central directory mirroring what WIT already has, so
   the central branch's paper trail is self-consistent without needing a cross-branch fetch to
   verify.
5. Resolve or explicitly schedule resolution of the Anandamayi 108-vs-156 dedup question before the
   Vrindavan/Braj or Kankhal cluster slices are declared accounting-closed.

**P2 — low severity, track but do not block:**
6. Confirm the ROOD 178-vs-179 count discrepancy is a formatting artifact, not a missing/extra row.

## 5. NEXT_ALLOWED_STEP

CCI does not build the master itself (out of scope for this QA role) and does not start a new
person sweep, A/B/C decision, or route choice. INDIA8/INDIA9 should:
1. Execute P0-1/P0-2 (assemble the actual master + close the global accounting equation) before
   presenting Vrindavan/Braj or Prayagraj/Allahabad for a new Mark A/B/C round, per the task's own
   `MARK-READY GATE`.
2. Apply the P1 documentation fixes (§4) at the same time, since they are cheap and prevent a future
   session from bootstrapping off a stale file.
3. Once P0 closes, CCI is available for a second, short verification pass specifically on the
   assembled master's accounting equation and on the first cluster slice (Vrindavan/Braj) before it
   goes to Mark — a natural, low-cost second QA checkpoint given how much scattered cross-branch
   verification this round required.

CCI stops here and waits for INDIA8/INDIA9-QA. No merge, no A/B/C, no route, no PDF performed.

---
Geschreven door: CCI. Onafhankelijke QA-rol, geen nieuwe workstream.
