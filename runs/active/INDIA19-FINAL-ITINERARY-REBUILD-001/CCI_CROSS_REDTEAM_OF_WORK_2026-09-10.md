# CCI CROSS-RED-TEAM OF WORK'S INDEPENDENT SOLVE — INDIA19

Status: **COMPLETE**
Author: CCI, per PR #23 dispatch "CCI_TASK — INDIA19 TARGETED CROSS-RED-TEAM OF WORK SOLVE — NO NEW GLOBAL SOLVE"
Audit target (read-only, not modified): `runs/active/INDIA19-FINAL-ITINERARY-REBUILD-001/WORK_INDEPENDENT_ADVERSARIAL_33_NIGHT_SOLVE_2026-09-10.md`, commit `594b430f235ebf49dcfa3f4a142717961480c0c1`, branch `worker/india19-work-independent-stress-solve`.
Reference (read-only, not modified): CCI's own frozen solve, `CCI_INDEPENDENT_SOLVE.md`, commit `b52ea7157803e8b2061191061e65804e6b44e0c1`, branch `worker/india19-cci-independent-solve`.
This is a targeted comparative audit, not a new route solve. No grade, lock, duration, or FINAL OUT decision is touched. Neither frozen solve file was edited to produce this audit.

---

## 1. BODH GAYA 2n+TIRU5n (WORK) vs BODH GAYA 3n+TIRU4n (CCI) — applied tier-by-tier

Ruler used: `OBJECTIVE_AND_HUMANE_GATES.md` §1 (lexicographic tiers 1–9) and §3 item 1–2 (explicit `MARK_DECISION_REQUIRED` flags for this exact question). Ground evidence: `decisions/BODH3_TIRU4_WAKING_HOURS_STRESS_TEST_RESULT_2026-09-08.md`, read in full and cited by both solves.

**Tier 1 (hard scope/canon/date/33-night feasibility):** TIE. Bodh Gaya (2–3n) and Tiruvannamalai (4–5n) are both explicitly open sensitivity ranges, not locked durations (`CLOSED_FACTS_OPEN_VARIABLES.md` Category 3.3). Both WORK's Bodh2/Tiru5 and CCI's Bodh3/Tiru4 pass 33/33 with no duplicate/missing night (independently reverified below, §2).

**Tier 2 (AI155 protection):** TIE. Neither solve's Bodh/Tiru choice touches the AI155 margin; both preserve the Chennai-positioning buffer night.

**Tier 3 (every retained A+/A has a real time-block home):** TIE. WORK's own §5 table states plainly: "Bodh 2 ... all Bod obligations fit" and "Bodh 3 ... extra Bodh depth is real." Both variants place every Bodh Gaya and Tiruvannamalai A+/A/A* row on a named day (confirmed by ID-level cross-check, §3 below). Neither variant drops or hides a row at this tier — the difference is pacing (tier 5), not presence.

**Tier 4 (door-to-door/access feasibility):** TIE. No access/closure fact cited by either solve depends on the 2n/3n or 4n/5n choice.

**Tier 5 (humane sleep/recovery/quiet-time viability) — this is where the real trade-off lives:** The frozen stress test explicitly finds costs on **both** sides, not one dominating the other:
- Bodh Gaya 2n: the Sujata/Dungeshwari excursion runs "on a schedule, back by mid-afternoon to preserve some rest, not at a genuinely unhurried pace" — a real but moderate restfulness cost.
- Tiruvannamalai 4n (reached by taking the night from Tiru rather than elsewhere): the arrival day (Fri 15 Jan) collides with Sri Ramanasramam's Friday Sri Chakra Puja, "forcing a skip-it-or-exhaust-yourself choice," and the final day absorbs two content-blocks that the 5-night form kept separate.

The stress test's own author does not resolve this as a tier-5 win for either side — its closing "MARK GATE" states verbatim: **"Both are legitimate; this file exists so the choice is informed rather than assumed."** Applying the lexicographic rule myself against this same evidence, I reach the identical conclusion: neither Bodh2/Tiru5 nor Bodh3/Tiru4 dominates at tier 5 or any higher tier. **This is a genuine, evidence-confirmed Mark-only tie**, exactly as `OBJECTIVE_AND_HUMANE_GATES.md` §3 items 1–2 anticipated it would be if "genuinely marginal after the objective hierarchy."

**Tiers 6–9:** Not separating factors either; neither solve claims a lower-tier win as a tie-breaker, and none would be admissible over a tier-5 tie per the lexicographic rule.

**Governance rule check — Sri Chakra Puja "not a Tiru5 veto":** `governance/CURRENT_STATE.md` states verbatim: "Sri Chakra Puja optional bonus, not a hard Mark-graded requirement and not a Tiru5 veto" — i.e., the puja must not be used to force Tiru5. WORK complies: its own day-15 note reads "A Friday Sri Chakra Puja is optional date-quality only and must be live-confirmed; it is not a route lock," and WORK's stated reason for preferring Tiru5 as its default is structural (avoiding module-stacking on 18 Jan), not the puja. **No violation found in WORK's framing.** CCI also complies (frames the puja collision as an accepted cost of its own recommendation, not as a forced exclusion). Neither solve violates this rule.

**The one asymmetry worth surfacing to Mark, not previously weighed by either solve:** The stress test file's own header quotes Mark directly — *"Ik vind Bodh Gaya te kort en Tiruvannamalai te lang"* ("I find Bodh Gaya too short and Tiruvannamalai too long"). This is the only actual Mark-sourced subjective signal anywhere in the reused evidence chain for this exact question, and it points toward **more** Bodh Gaya and **less** Tiruvannamalai — i.e., the Bodh3/Tiru4 direction. Neither WORK's nor CCI's solve quotes or explicitly weighs this line in its Bodh/Tiru section, but WORK's chosen "operational default" (Bodh2/Tiru5) sits in the opposite direction from it, while CCI's recommended default (Bodh3/Tiru4) aligns with it. This does not make WORK's solve invalid — the duration remains genuinely open and WORK correctly declines to lock it — but it is a material piece of context INDIA19/Mark should see before accepting WORK's "operational default" label at face value.

**Verdict:** TIED under the frozen objective/humane hierarchy — confirmed by independently reapplying the tiers, not merely by trusting either solve's self-report. Preserved as genuine `MARK_DECISION_REQUIRED`, correctly flagged as such by both WORK (§9 item 1) and CCI (§6 item 1). WORK's specific chosen default point, however, runs opposite to Mark's only directly-quoted preference in the record.

---

## 2. Calendar consistency — independent recomputation of WORK's dated form

All day-of-week claims in WORK's §3 table were independently recomputed (Python `datetime`, proleptic Gregorian) against the stated 2026/2027 dates:

| Claim in WORK | Recomputed | Match |
|---|---|---|
| 19 Dec 2026 = Sat | Saturday | YES |
| 24/25/26/27/28/29/30/31 Dec | Thu/Fri/Sat/Sun/Mon/Tue/Wed/Thu | YES (all 8) |
| 1 Jan 2027 = Fri | Friday | YES |
| 3 Jan = Sun | Sunday | YES |
| 8 Jan = Fri | Friday | YES |
| 10 Jan = Sun | Sunday | YES |
| 11 Jan = Mon | Monday | YES |
| 12 Jan (National Youth Day) | Tuesday (date-fixed, day-of-week irrelevant to the holiday) | YES |
| 14/15/17/19/20 Jan | Thu/Fri/Sun/Tue/Wed | YES (all 5) |
| 21 Jan (AI155) | Thursday | YES |

The full 33-slot table was independently walked date-by-date: 19 Dec 2026 through 20 Jan 2027 inclusive, every calendar date appearing **exactly once**, no gap, no duplicate. WORK's own arithmetic line (`1+3+3+3+1+1+1+2+8+3+5+1+1=33`) is correct and matches the table.

**Varanasi 8-night lock:** nights of 3–10 Jan inclusive = 8 nights. Correct, matches the lock.
**Haidakhan 2 protected quiet days:** 27 and 28 Dec, both marked "protected complete quiet/ashram day," zero transfer/checkout logistics on either. Correct.
**Nirmal Dham placement:** scheduled 20 Jan (final Delhi), explicitly absent from 19 Dec arrival day. Correct per `decisions/NIRMAL_DHAM_FINAL_DELHI_PLACEMENT_MARK_DECISION_2026-09-09.md`.
**No FINAL OUT world reopened:** confirmed by direct text search — zero mentions of Puri/Odisha, Serampore/Srirampur, Vrindavan/Braj/Mathura/Govardhan, Haridwar-Kankhal-Rishikesh, Prayagraj/Allahabad, Mysuru-Bengaluru, Ranchi, or Sri Aurobindo Ashram/Puducherry anywhere in WORK's file.
**AI155/AI156 envelope:** AI156 arrival ~10:15 on 19 Dec, AI155 departure ~12:20 on 21 Jan — exact match to the frozen envelope in `CLOSED_FACTS_OPEN_VARIABLES.md` Category 1.1.
**Bhrigu Karyalaya / Manikarnika separation rule:** WORK places Bhrigu on 6 Jan and Manikarnika on 8 Jan — different days, and WORK explicitly states "Bhrigu is never placed on Manikarnika day." Correct.
**No removed/downgraded B/C site smuggled back in as A-grade:** confirmed by direct text search — zero mentions of Bhaskarananda Samadhi/Anand Bagh, Tulsi Manas Temple, Mangala Gauri Temple, Nalanda Mahavihara, Patharkatti, Sher Shah Suri Tomb, or Baranagar Math anywhere in WORK's file.

**One genuine finding — WORK is demonstrably *more* correct than CCI's own frozen solve on a real closure fact, not a defect in WORK:** The reused, previously-completed independent calendar audit (`runs/active/FINAL_BOOKABLE_CALENDAR_INDEPENDENT_CHECK_2026-09-07.md`, commit `2879705a83325734ba2f2f20ccad7ef857bf9267`, cited as reusable evidence in `CLOSED_FACTS_OPEN_VARIABLES.md` Category 2.4) states, sourced to the official ASI Sarnath Museum planning page: **"Keep Sarnath Museum off Fri 8 Jan: official museum rule is Friday closure."** WORK's calendar places the full Sarnath world (including the Archaeological Museum, `VNS-38`) on **Sunday 10 Jan**, explicitly noting "Sunday avoids the museum's Friday closure" (§4, 3–10 Jan section) — correct, and independently confirmed correct by me against the cited official-source audit. By contrast, CCI's own frozen solve places the same Sarnath world, including the same museum, on **Friday 8 Jan** (`CCI_INDEPENDENT_SOLVE.md` §3, night 21) — a real collision with the pre-existing, already-sourced closure fact, which CCI's own §7 only flags as an unresolved `LIVE_RECHECK_LATER` risk rather than actually avoiding it. This is not a defect in WORK; it is a point where WORK's dated form is more correct than CCI's own frozen artifact.

No hard date/closure/transfer defect was found in WORK's calendar.

---

## 3. 86-row disposition — semantic or substantive?

Both checksums were independently verified against the frozen `PHYSICAL_A_PLUS_A_COVERAGE_LEDGER.csv` (87 rows total; 86 graded A+/A/A* rows; `VNS-22` is the separate SPECIAL/ACCOMMODATION row, correctly excluded from the 86 by both solves).

**Completeness check:** every one of the 86 graded ledger IDs appears in WORK's §8 checksum exactly once across its SCHEDULED (68) + LEGITIMATELY_SHARED_WITH_PARENT (16) + BLOCKED_PENDING_MARK (2) buckets — no row omitted, no row double-counted, no non-existent row invented. WORK's claim "independently reconciled one-for-one against the frozen CSV" (§11) checks out exactly.

**Bucket-by-bucket diff against CCI's 46+40+0:** comparing every ID's bucket (SCHEDULED vs SHARED, ignoring the BLOCKED label for now) produces **26 differing rows**, of which:

- **24 rows** are pure SCHEDULED-vs-SHARED classification differences on items the ledger's own `PARENT_CHILD_RELATION`/`MAY_SHARE_VISIT_BLOCK` fields already describe as "Child of X," "Standalone but tied to X," or "route-side member of the X world" — e.g. `TIR-04`/`TIR-06`/`TIR-07` (ledger: "Child of TIR-01"), `VNS-32`/`VNS-34` (ledger: "Child/route-side member of the Manikarnika... world"), `AGR-02/03/04` and `TIR-09/10/11` (ledger: "Standalone FINAL-COMFORT-adjacent food item, zero independent day/night weight"). CCI folds these into SHARED; WORK gives each its own SCHEDULED bullet while still placing it inside the same day-block as its parent (WORK's own §8 preamble: "Each remains individually named on its day card" for the SHARED bucket, and the SCHEDULED entries for these items cite the same date as their parent, e.g. `VNS-32`/`VNS-34` both dated 8 Jan alongside `VNS-01`). Cross-checking every one of these 24 against WORK's day-by-day §3/§4 text confirms **no placement difference** — same day, same block, same parent context in both solves. `OBJECTIVE_AND_HUMANE_GATES.md` §1 tier 3 explicitly sanctions this ("a parent/child pair may legitimately share one block, but neither entity may disappear") without mandating a particular bucket label for it. **This is classification granularity, not a coverage difference.**
- **2 rows** — `KUM-13` (Sattal/Seven Lakes) and `BOD-06` (Rajgir Brahmakund) — are the genuine dispute, addressed below.

**Sattal / Rajgir Brahmakund — the actual rule text, read from source, not from either solve's paraphrase:**

`PHYSICAL_A_PLUS_A_COVERAGE_LEDGER.csv`, verbatim:
- `KUM-13`: `PARENT_CHILD_RELATION` = "SKIP_FIRST corridor-bycatch, not a dedicated excursion; only if true-road geometry/daylight/energy allow"; `MAY_SHARE_VISIT_BLOCK` = "Conditional — only as an add-on to the Haidakhan->Nainital transfer day, otherwise SKIP_FIRST"; `COVERAGE_STATUS` = `SPECIAL_STATUS`; `FINAL_CALENDAR_DISPOSITION` = blank (not pre-decided by the ledger itself).
- `BOD-06`: `PARENT_CHILD_RELATION` = "ONLY_IF_NATURAL_CORRIDOR_BYCATCH / SKIP_FIRST — explicitly not a dedicated A excursion"; `MAY_SHARE_VISIT_BLOCK` = "No — current expected Bodh corridor does not naturally pass Rajgir, so no Rajgir day is currently allocated"; `COVERAGE_STATUS` = `SPECIAL_STATUS`; `FINAL_CALENDAR_DISPOSITION` = blank.

Both rows carry a pre-existing Mark rule whose **default outcome is already SKIP** unless a natural corridor happens to exist; neither ledger row pre-assigns a `FINAL_CALENDAR_DISPOSITION`, leaving the bucket-word itself as a solver convention, not a locked field. Neither solve's topology contains the corridor the rule requires (Sattal needs a Haidakhan→Nainital edge, which does not exist in either solve's Nainital-first order; Rajgir needs the Bodh Gaya corridor to pass through Rajgir, which it does not in either solve). **Consistency check:** both solves correctly distinguish this from `BOD-08` (Gaya Tilkut), a third A*/SKIP_FIRST row where the corridor *does* exist (both solves' Gaya-station arrival genuinely passes through Gaya) — both solves correctly activate `BOD-08` while correctly not activating Sattal/Rajgir. This confirms the SKIP_FIRST/corridor-bycatch rule is being applied correctly and consistently by both solves, not asymmetrically.

Given the identical substantive resolution, the only remaining question is which label is truer to the rule: CCI's "SCHEDULED (not activated this trip)" — a self-admittedly stretched use of "SCHEDULED" for an item that appears nowhere in CCI's own day-by-day calendar — or WORK's "BLOCKED_PENDING_MARK" — which slightly overstates urgency (nothing is actually blocking completion of the itinerary; the pre-existing rule already resolves the default to skip, so Mark does not need to act to "unblock" anything, only to affirmatively override it if he wants a deliberate detour). Both labels are imperfect fits for a genuinely third state ("resolved-to-skip-by-a-pre-existing-Mark-rule, re-openable only by Mark's future initiative") that the ledger's own two-bucket vocabulary (SCHEDULED/SHARED) was never designed to hold. **Neither label is wrong enough to constitute a defect**, and — importantly — **both solves list the identical live possibility in their own `MARK_DECISION_REQUIRED` sections** (CCI §6 item 6; WORK §9 item 4): if Mark wants either site added as a deliberate extra excursion, he must explicitly override the SKIP_FIRST condition himself. The two artifacts reach the same operational answer through different bucket names.

**Verdict: SEMANTIC, not substantive.** No physical A+/A/A* row is scheduled by one solve and lost/hidden/dropped by the other. Every one of the 86 rows has an identical physical fate (visited-with-a-named-block, or correctly-skipped-by-a-pre-existing-rule-and-flagged-for-Mark) in both solves; the 68+16+2 vs 46+40+0 difference is entirely attributable to (a) a finer-vs-coarser convention for naming genuinely-bundled child/incidental items, and (b) a bucket-vocabulary choice for the two SPECIAL_STATUS rows, neither of which changes what actually happens on the ground.

---

## 4. Macro convergence — shared spine

Confirmed point-by-point between WORK's §1/§3 and CCI's §1/§3:

- **Kumaon-first:** both — `AI156 → rail → Nainital → Dunagiri/Kukuchina → Haidakhan`.
- **12039 daytime north exit + Delhi transit bed:** both independently converge on 29 Dec 12039 Kathgodam→New Delhi (~15:15–20:55) plus a normal Delhi hotel bed, explicitly rejecting the 15014 overnight/04:10 default and retaining it only as a same-evening fallback. WORK frames this as its "principal falsification finding" (§2); it is worth noting this exact reconfiguration was already present in the underlying `decisions/BODH3_TIRU4_WAKING_HOURS_STRESS_TEST_RESULT_2026-09-08.md` §3 ("29 Dec: ... board 12039 at 15:15 ... Delhi transit hotel, normal night's sleep"), which both solves cite as reused evidence — so this is a point of genuine convergence, not a novel divergence, though WORK's framing slightly overstates its own originality on this specific point. Not a defect; both solves agree on the substance.
- **Agra/Taj:** both — 12050 Gatimaan NZM→Agra Cantt, Taj-only protected dawn visit, depart-ASAP rule honored, evening 12988 sleeper to Gaya.
- **12988 direct (no Prayagraj insertion):** both cite and reuse the same `KEEP_12988_DIRECT` verdict verbatim, no re-litigation.
- **Eastward sequence:** both — Bodh Gaya → Varanasi/Sarnath → Kolkata/Dakshineswar → Tiruvannamalai/Arunachala → Chennai → final Delhi.
- **Chennai airport night:** both place a Chennai overnight on 19 Jan ahead of the final MAA→DEL flight; WORK is more explicit ("Chennai airport-side hotel") while CCI's text implies the same function without naming the hotel's exact positioning — a specificity difference, not a disagreement.
- **Final Delhi exactly 1 night, 20 Jan:** both — `DEL-01` Nirmal Dham (priority), `DEL-03` Lotus Temple, `DEL-02` PVR Priya IMAX (conditional).

**No silent divergence found.** Both solves' own texts openly admit the one place they differ (Bodh/Tiru duration) and are consistent about everything else in the shared spine.

---

## TOP-LINE VERDICT

```
PASS_WORK
BODH_TIRU_VERDICT: Genuine tie at every objective-hierarchy tier through tier 5 (humane/recovery), confirmed by independently reapplying OBJECTIVE_AND_HUMANE_GATES.md tier-by-tier against the shared frozen stress-test evidence, not by trusting either solve's self-report. Correctly preserved as MARK_DECISION_REQUIRED by both WORK and CCI. Neither solve violates the "Sri Chakra Puja is not a Tiru5 veto" rule. One asymmetry worth flagging to Mark: his own directly-quoted preference in the record ("Bodh Gaya too short, Tiruvannamalai too long") leans toward CCI's Bodh3/Tiru4 default, opposite WORK's chosen Bodh2/Tiru5 default — neither solve surfaces or weighs this quote, and WORK's "operational default" label should not be read as objectively favored on that basis.
DISPOSITION_DIFFERENCE: SEMANTIC. All 86 A+/A/A* rows independently confirmed present exactly once in both solves' checksums with identical physical placement/date; the 68+16+2 vs 46+40+0 split is bucket-naming granularity (24 rows: SCHEDULED-vs-SHARED convention for already-bundled child/incidental items per the ledger's own PARENT_CHILD_RELATION field) plus a bucket-vocabulary choice for 2 rows (KUM-13 Sattal, BOD-06 Rajgir Brahmakund: WORK's "BLOCKED_PENDING_MARK" vs CCI's "SCHEDULED (not activated)") where both solves reach the identical substantive resolution — skip by the pre-existing SKIP_FIRST/corridor-bycatch rule (no corridor exists for either in either topology, unlike BOD-08 Gaya Tilkut where a real corridor exists and both solves correctly activate it), flagged identically as a live Mark-optional override in both solves' own MARK_DECISION_REQUIRED sections.
MARK_DECISION_REQUIRED_REMAINS: Yes. (1) Bodh Gaya 2n/3n + Tiruvannamalai 5n/4n, a genuine tie per this audit's own tier-by-tier reapplication — Mark's own quoted preference is the one piece of real signal available and favors 3n/4n. (2) Whether to attempt the Friday Sri Chakra Puja tired-on-arrival if Tiru4 is chosen (contingent on item 1). (3) Final global macro-order acceptance — both solves ratify KEEP INCUMBENT from reused evidence but explicitly leave the final lock to Mark per that evidence's own closing line. (4) Whether Mark wants to override the SKIP_FIRST rule for Sattal and/or Rajgir Brahmakund as a deliberate extra excursion (default in both solves: no action needed, both are correctly skipped).
```

---

## WHAT THIS AUDIT DID NOT DO

- Did not create a new route solve or edit either frozen solve file.
- Did not change any grade, lock, or duration in the frozen ledger.
- Did not book anything or produce a PDF.
- Did not reopen the global macro-topology question independently — reused WORK's and CCI's shared reuse of the existing `KEEP INCUMBENT` verdict.

END CCI CROSS-RED-TEAM OF WORK
