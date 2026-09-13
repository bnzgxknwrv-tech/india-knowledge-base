# INDIA20 FINAL EXTRACTION — 2026-09-13

Status: **BINDING SUCCESSOR HANDOFF**
Branch: `agent/india8-cluster-casting`
Final HEAD covered by this extraction: `d6c5834` (India20: correct recovered-day logic and shift north chain earlier)
Author: INDIA20 (context exhausted); extraction written and verified by CCI on Mark's explicit instruction, since INDIA20 itself could no longer produce it.

This file exists because INDIA20's own context filled before it could write its own extraction. Per `governance/MARK_TO_INDIA_SUCCESSOR_HUMAN_HANDOFF.md` FOUT 20 (material knowledge must not remain chat-only) and the standing rule that a successor boot must never lose real progress, CCI reconstructed this extraction directly from the git history and the current governance files rather than from memory, then cross-checked it against `governance/CURRENT_STATE.md` for completeness before committing.

## 0. Hash semantics / exact central state

- Branch: `agent/india8-cluster-casting`.
- INDIA20 boot receipt: `governance/boot_receipts/INDIA20__I0L47E3996OB.json`, commit `9efff9f5065d20efd47c42f34fec1821b51d9206`, `BOOT_HEAD = 06a8dc145cb3ab1d73dabc5b85624719442be62c` (INDIA19's final extraction commit).
- Independent FULL CHECK: `governance/boot_checks/INDIA20_CHECK__I0L47E3996OB.json`, commit `d07ab68ebad4f0d8479f0c34745c8e744384bf2c`, `CHECK_NONCE = Y3PXK7QVT2NR`, `check_gate: PASS`, all 13 mandatory `check_required_challenge_topics` answered and independently verified by CCI. `CONTENT_AUTHORIZATION: GRANTED` — independently re-confirmed by CCI later the same day by re-running `governance/scripts/final_authorization.py` against the exact R→K chain (`K^ == R`, `diff(R,K)` == check file only).
- From authorization through this extraction, INDIA20 made **57 commits** (`9efff9f..d6c5834`), touching 38 distinct files, +4206/-342 lines. Full list is in git log; the substantive ones are grouped by topic below.
- The frozen A79 input-freeze ledger (`runs/active/INDIA19-FINAL-ITINERARY-REBUILD-001/PHYSICAL_A_PLUS_A_COVERAGE_LEDGER.csv`, frozen at `a2b71b2563f446480b012f0b9176a87e96fcb003`) was **not** mutated by INDIA20 itself. The only post-freeze commits touching that file are CCI's own three Mark-decision commits (`9a36376`, `0659f26`, `58609b8`). INDIA20 correctly built a **separate** live-derived ledger instead (see section 2).

### Source hierarchy / successor method

Unchanged from INDIA19: newer explicit Mark decision > CCI harvest > active-cluster research > stale central docs. Tradition-is-evidence (`decisions/TRADITION_IS_EVIDENCE_PILGRIMAGE_NOT_COURTROOM_MARK_DECISION_2026-09-13.md`) is now hard governance, not a one-off correction — do not reintroduce "PLAUSIBLE not CONFIRMED" hedging language anywhere.

### Successor boot/read order — before any new India content work

1. This file, in full.
2. `governance/CURRENT_STATE.md` (INDIA20 left this extremely current and detailed — read it in full, it is the single best map of exactly where things stand).
3. `runs/active/INDIA20-LIVE-LEDGER-V4-REPAIR-001/*` (the live-derived ledger family, see section 2).
4. `research/ACTIVE_WORLD_CLASSIFICATION_REGRESSION_AUDIT_2026-09-13.md` and `research/LIVE_LEDGER_COMPLETENESS_AUDIT_2026-09-13.md` (both still open, both block v4).
5. `governance/DECISION_LEDGER.jsonl` from `DL-0057` onward (everything before was already in INDIA19's extraction).

# 1. Hard trip truth (unchanged)

- AI156 AMS→DEL 18 Dec 2026 ~20:35, arrive 19 Dec ~10:15.
- AI155 DEL→AMS 21 Jan 2027 ~12:20.
- Exactly 33 physical India nights, 19 Dec through 20 Jan.
- Exactly one final Delhi hotel night immediately before AI155: 20 Jan.
- Flight safety outranks Nirmal Dham and all final-day extras.
- No booking/contact made anywhere yet, **except**: Day 1 hotel is now locked (see section 6).

# 2. Live-derived ledger family — the new v4 working layer

INDIA20's first substantive post-authorization act was to stop treating the frozen A79 ledger as something to keep editing, and instead build a **separate live layer** that derives from it without mutating it:

- `runs/active/INDIA20-LIVE-LEDGER-V4-REPAIR-001/LIVE_DERIVED_PLACE_GRADE_LEDGER_2026-09-13.csv` — the current live truth for grades/status. Continuously updated across the session as Mark made new decisions (Serampore, Kasar Devi, Kolkata batch, Chennai, Day-1 hotel, Dec 20-24 clock corrections). **This is the file to read for "what grade is X right now," not the frozen ledger.**
- `runs/active/INDIA20-LIVE-LEDGER-V4-REPAIR-001/MARK_FACING_LIVE_A_PLUS_A_CARDS_V4_SOURCE_2026-09-13.md` — the v4 Mark-facing card source (535 lines). Not yet the final PDF; the source material the eventual v4 PDF must be built from.
- `runs/active/INDIA20-LIVE-LEDGER-V4-REPAIR-001/LIVE_CLOCK_PLAN_V4_REPAIR_2026-09-13.md` — the repaired day-by-day clock plan.
- `runs/active/INDIA20-LIVE-LEDGER-V4-REPAIR-001/MARK_DECISION_SURFACE_BODH3_TIRU4_VS_BODH2_TIRU5_2026-09-13.md` — the first genuine Mark-only duration decision (see section 8). **Not yet presented to Mark** — deliberately deferred, see section 4.

Stable historic A-numbers (A001-A079) are decoupled from live grades: the A-number identifies the place, the live ledger carries the current grade. Do not assume the A79 clock-time PDF's original grade is still current — always check the live ledger.

# 3. Everything Mark actually decided since INDIA19's extraction (chronological, all already committed)

This is the complete list of binding Mark decisions INDIA20 recorded. Do not re-ask Mark about any of these; do not re-open them without new information.

**Grade changes (already reflected in the live ledger and, where they touch the frozen A-number, in the frozen ledger too):**
- A003 (Hanuman Garhi + Maharajji-kuti) → A+.
- A037 (Subah-e-Banaras) → conditional A* (zero-cost only).
- A006 (Dhokaney Waterfall) → conditional A*; A035 (Lolark Kund) → conditional A*.
- A023/A044/A047/A050/A059/A060 → B (removed from the frozen A-scoped ledger).
- A043 (Kedareshwar) stays A — explicitly excluded from the above downgrade batch after re-verification found a genuine Sri Ramakrishna connection.
- A067 (The Dreaming Tree) → A*; A068 (Virupaksha Cave) → A+.
- A078 (Lotus Temple) → A*; A079 (PVR Priya IMAX) → A*.
- Kakrighat → renamed/fixed to its canonical name **Swami Vivekananda Jnana Vriksha / Knowledge Tree** and promoted to **A+** (microcosm–macrocosm realization site).
- Kasar Devi Cave ("Grot Vivekananda") → **A+**; the "Grot Vivekananda" naming must always be retained on every Mark-facing occurrence.
- Chennai Vivekananda House/Ice House → **A***, buffer-bycatch only (existing waiting window, never a dedicated stop, never weakens the MAA→DEL safety margin).

**Serampore/Srirampur (reopened, was stale FINAL OUT):**
- SER-01 Sri Yukteswar main hermitage/Smriti Mandir = **A+**, 2h onsite incl. real meditation/quiet time if access permits.
- SER-02 Rai Ghat sacred banyan (Babaji–Sri Yukteswar 1894 site) = **A+**.
- SER-03 Anandaloka/YSS Serampore Retreat = **A+ if the exact preserved Yogananda room is enterable for meditation, otherwise A***.
- SER-04 Serampore College = **C**. SER-05 former Panthi boarding-house plot = **C** (structure demolished).
- Serampore does not create a separate sleep-world; it must be absorbed into the existing 3-night Kolkata/Dakshineswar block.

**Kolkata numbered follow-up batch (superseded once by newer INDIA20 research per Mark's own "newer wins" rule — use these final values, not any earlier tentative ones):**
1. Vivekananda Ancestral House/Birthplace = **A+**.
2. Cossipore/Kashipur Udyanbati = **A+**.
3. Balaram Mandir = **A+**.
4. Shyampukur Bati = **A**.
- Tulsi Bose Shrine (distinct from 4 Garpar and YSS Garpar) = **A+**.
- 50 Amherst Street = **B** (Mark's own rule: not currently proven as a formal shrine/open-to-devotees site).
- Nagendra Math/Bhaduri Mahasaya house = **A+** (official YSS: converted Math, open to devotees).
- Pandavkholi/Pandukholi (above Babaji Cave) = **A**, access/winter-safety gated.
- Kalighat Kali Temple (exact AOAY childhood event site) = **A+**.
- Dihika (original 1917 Yogananda school, birthplace of YSS) = **A***, kept alive as an optional meaningful world even though the current Varanasi→Kolkata train geometry makes it expensive; execute only if a genuinely available day/corridor makes the burden acceptable. (`decisions/INDIA20_KAKRIGHAT_AMHERST_DIHIKA_RICH_LOCATION_CARD_MARK_DECISIONS_2026-09-13.md` sec.3 explicitly supersedes an earlier same-day "C under current route burden" framing — the A* is Mark's actual last word.)
- 50 Amherst Street = **A*** — Mark wants to go if practical even for exterior-only access. (Same decision file sec.2 explicitly supersedes an earlier same-day "B, not proven as formal shrine" framing.)
- Kasar Devi Cave, canonical name **"Grot Vivekananda"** = **A+** (`decisions/INDIA20_DEC23_24_KUMAON_VIVEKANANDA_TRANSIT_AND_BABAJI_DAY_MARK_DECISION_2026-09-13.md` sec.6: "any older wording treating Kasar Devi Cave as OPEN grade is stale").

**Day-block / schedule decisions:**
- Every future day plan now starts the operational clock at **VERTREK HOTEL** — private morning routine, wake, breakfast are removed from the clock entirely.
- **Day 1 hotel is LOCKED: Hotel New Frontier**, 19 Dec 2026. Required execution before travel: prebook airport pickup via hotel/formal driver with meet-and-greet/name board; get driver name + mobile/WhatsApp in advance; get the hotel's 24h fallback number; confirm exact meeting point, delay/waiting policy, and price/payment before departure. Still open before booking: guaranteed daytime/early room access, request a quiet room, save contacts offline, re-verify train 15013 still boards at DLI, optionally daylight-walk hotel→DLI once.
- 19 Dec: arrival → hotel walkable to Old Delhi/Delhi Junction (DLI) for the current 15013 boarding plan; live-recheck station/timetable at booking time.
- 20 Dec: Naini Lake + Hanuman Garhi/Maharajji-kuti moved onto this day; Hotel Evelyn needs no separate sightseeing block.
- 21 Dec: a complete day was recovered by the correction in commit `d6c5834`; currently left unallocated.
- 22 Dec: Kainchi Dham at 08:00, depart 13:00 toward Bhumiadhar, rest of day free; default transport = one prebooked driver.
- 23 Dec: one prebooked private driver for the full Nainital→Vivekananda-detours→Dunagiri/Kukuchina transfer with luggage/waiting; protect the two Vivekananda anchors (Kakrighat A+, Kasar Devi A+ if executable on the transfer); Dhokaney (A*) yields if it adds >20 min net driving and can never displace the Vivekananda anchors.
- 24 Dec (Mark's own stated intent, not yet a locked clock): 08:30 VERTREK HOTEL → 09:15 A007 Dunagiri Bell Temple → 10:30 depart toward A008/trail → climb 11:15–12:15 toward A009 → long A009 Mahavatar Babaji Cave + Pandavkholi ridge presence through the afternoon if feasible. Mark wants ~17:00 cave/ridge presence; sunset is ~17:15–17:25. **This exact turnaround time cannot be locked yet** — winter trail condition, guide availability and return geometry must be checked first. This is the single open safety-gated item in the north schedule.
- Governing rule for all of the above and future PDFs: `governance/MARK_DAY_BLOCK_ONLY_PDF_RULE_2026-09-13.md` — the v4 PDF must be **day-block only**: every day self-contained with all travel/content/WHY/access/timing information inline, no substantive front/back appendices. **Do not generate the PDF yet.**

**Other governance additions:**
- `governance/PERMANENT_PLACE_NUMBER_RULE_2026-09-13.md` (also `4d4ad6f`): place numbers (A001-A079 etc.) are now permanent identifiers across all Mark-facing outputs, decoupled from grade.
- `governance/MARK_FACING_PLACE_CARD_TRAVEL_VALUE_RULE_2026-09-13.md`: the hard time-accounting formula for what a place actually costs/saves — `TOTAL TIME = A→B travel + B dwell + B→C travel`; `TIME FREED IF SKIPPED = (A→B + dwell B + B→C) − recalculated direct A→C`. Never substitute dwell time for skip-saving; never blindly sum card times when adjacent cards share a travel leg.
- A008 Babaji Smriti Bhavan's description was repaired from generic "memorial" wording to its real meaning: the meditation hall/shrine just below Babaji Cave, inside the 1861 Babaji–Lahiri-Mahasaya initiation world. Grade unchanged (A); meaning was the defect.

# 4. Why v4 (the next PDF) is still BLOCKED — read this before doing anything else

Two separate problems were gating v4 as of INDIA20's last commit (`d6c5834`). **CCI resolved the first one while writing this extraction; the second remains open:**

1. **Classification regression — RESOLVED 2026-09-13 by CCI.** The six high-priority candidates INDIA20 had flagged as "found but not yet graded" (Tulsi Bose Shrine, 50 Amherst Street, Nagendra Math, Pandavkholi, Kalighat Kali Temple, Dihika) **already had locked Mark decisions on record** — the live ledger CSV had simply never been synced to reflect them (a `GRADE_SCOPED_LEDGER_MISTAKEN_FOR_COMPLETE_MEMORY`-class bug, applied to itself). Same defect also affected Kasar Devi Cave and the four-site Kolkata Vivekananda/Ramakrishna batch (Vivekananda Ancestral House, Cossipore, Balaram Mandir, Shyampukur Bati) and the Chennai Vivekananda House. CCI wrote all correct grades back into `LIVE_DERIVED_PLACE_GRADE_LEDGER_2026-09-13.csv` (rows `L101`-`L106`) and corrected `governance/CURRENT_STATE.md`'s stale framing. **Do not re-present any of these to Mark; see section 3 for final values.** Two items in this family remain genuinely open with no Mark decision yet: Lala Badri Shah House (`L107`) and J.C. Bose residence (`L108`, needs existence/access verification before it can even be presented).
2. **Ledger completeness — STILL OPEN.** (`research/LIVE_LEDGER_COMPLETENESS_AUDIT_2026-09-13.md`): the live derived ledger is still not a mechanically complete memory of every B/C/OPEN decision ever made — it currently only reliably tracks A+/A/A* rows plus whatever B/C rows happened to get carried over. Confirmed still-missing examples: Delhi B reserves (Qutb Minar, Hauz Khas Village, Humayun's Tomb, Sunder Nursery, Garden of Five Senses, Lodhi Garden, Red Fort), Delhi OPEN items (Jama Masjid/astrology-interest), Tiruvannamalai B reserves (Mango Tree Cave, Pachaiamman Temple), and other historic C/reject items. This is a memory-model defect (a place must be distinguishably `B/C/OPEN`, never silently `never existed`), **not** permission to schedule any of these — just a completeness gap that must close before v4 can be trusted as authoritative.

`LIVE_LEDGER_MECHANICALLY_COMPLETE = NO` remains true. **Do not generate v4 yet.** The classification-regression blocker on the Bodh/Tiru duration ballot is cleared, but `CURRENT_STATE.md`'s full "V4 GATE" checklist has several other conditions (Serampore/Kolkata exact marginal-time fields, mechanical 33-night/stable-ID/tone verification) beyond just these two audits — read that section before assuming v4 is close.

# 5. Mark-only decisions still open (do not decide these yourself)

1. **Lala Badri Shah House and J.C. Bose residence** — the only two genuinely still-ungraded candidates from the classification-regression batch (see section 4.1). J.C. Bose needs an existence/access verification pass before it can even be presented; Lala Badri Shah House can be presented to Mark now, one item at a time, the same way A003/A037/A006 were done.
2. **Bodh Gaya 3n+Tiruvannamalai 4n vs Bodh Gaya 2n+Tiruvannamalai 5n** — fully prepared in `MARK_DECISION_SURFACE_BODH3_TIRU4_VS_BODH2_TIRU5_2026-09-13.md`, CCI and WORK already independently stress-tested both allocations and found no objective winner. **Deliberately not yet asked** — the classification-regression blocker on this is now cleared (section 4.1), but it is still deferred behind ledger completeness (section 4.2) and the rest of `CURRENT_STATE.md`'s V4 GATE checklist. Once those clear, this is the very next question for Mark.
3. **A069/A070/A071 (Skandashram/Gurumurtam/Pavalakunru) possible sacrifice for more Serampore time** — Mark is *considering* this, has **not** decided. Current analysis: dropping all three frees ~3h30-4h30 (not a clean day), A070 then A071 are the easier cuts, A069 is the hardest to cut (natural continuation of A068, Ramana's mother Alagammal's final period/death site, bridges the mountain phase to Ramanasramam).
4. **SER-03 Anandaloka's exact grade (A+ vs A*)** depends on a pre-arrival access check: can the exact preserved Yogananda meditation room actually be entered and used for meditation. Not resolvable until closer to booking.

# 6. High-priority recovered candidates — resolved by CCI, do not re-litigate

This section originally flagged a real internal inconsistency between `CURRENT_STATE.md` (framing these as still-OPEN) and later commits that showed durable grades for several of them. **CCI traced every one of them to its authoritative decision file and confirmed the grades were genuinely locked by Mark; the live ledger CSV had just never been synced.** CCI fixed the CSV (`L101`-`L106`) and `CURRENT_STATE.md`'s stale section. See section 3 for the final values and section 4.1 for the fix itself. Only `L107` (Lala Badri Shah House) and `L108` (J.C. Bose residence) remain genuinely open — do not re-ask Mark about anything else in this family.

# 7. CCI/WORK status — already complete, do not redo

Unchanged from INDIA19's extraction — still true:
- Frozen A79 coverage gate: complete.
- CCI/WORK macro solves + mutual red-team: complete.
- 79/79 person-provenance/relevance work (both re-verification passes): complete.
- Haidakhan local-Kailash research: complete, Mark graded A.
- Gyan Yatra/Buddha Marg existence research: complete.
- Seven Pragbodhi stupa research: complete.
- Sujata offering-vs-stupa research: complete (now two separate entities, A+ and A).
- Global topology solve: complete for the current macro; `GLOBAL_REOPTIMIZATION_REQUIRED = NO` — a global re-solve is not warranted by anything found this session.

`NO_REDO != DO_NOT_READ`: reopen raw outputs where needed to recover per-place meaning or find classification omissions — this is exactly how INDIA20 found Serampore, Kakrighat's naming, and A008's meaning defect.

# 8. What INDIA20 was doing when context filled

INDIA20 was mid-repair on the Kolkata numbered-candidate grade bookkeeping when context ran out, leaving `CURRENT_STATE.md` and the live ledger CSV out of sync with the actual locked Mark decisions (see sections 4.1 and 6 — CCI found and fixed this while writing this extraction). INDIA20's last commit (`d6c5834`) corrected a recovered-day/north-chain scheduling logic error and is internally consistent at the file level.

# 9. Successor's first real work

In order:
1. Read this file and `CURRENT_STATE.md` in full.
2. Present Lala Badri Shah House to Mark (one item, same pattern as A003/A037); run an existence/access verification pass on J.C. Bose residence before presenting it.
3. Continue the `LIVE_LEDGER_COMPLETENESS_AUDIT` — close the gap between "A+/A/A* scoped" and "mechanically complete B/C/OPEN memory." This is now the only classification-side blocker left on v4.
4. Once ledger completeness and the rest of `CURRENT_STATE.md`'s V4 GATE checklist are actually closed (not just progressed), present the Bodh Gaya 3n+4n vs 2n+5n choice to Mark using the already-prepared `MARK_DECISION_SURFACE` file — do not build a new one.
5. Resolve the Dec 24 Babaji Cave/Pandavkholi winter turnaround safety gate before it becomes execution-critical.
6. Only after all Mark-only choices are resolved: generate v4 as a day-block-only PDF per `governance/MARK_DAY_BLOCK_ONLY_PDF_RULE_2026-09-13.md`.
7. **Process note for whichever session reads this next:** when a governance/status file (`CURRENT_STATE.md`, a live ledger, a knowledge map) and a dated decision file disagree, do not average them or present both as open — trace the actual commit history (`git log -S`, `git show`) to find which one is genuinely newer and cite it, the way section 4.1 of this file did. A stale status file is a bug to fix, not a second opinion to weigh.

# 10. ABSOLUTE NO-REDO WARNING

Do not re-run: the A79 person-provenance restoration, the CCI/WORK macro solves, the Haidakhan/Gyan-Yatra/Sujata/seven-stupa research, or a global topology re-solve. All of these are complete and their outputs are cited throughout `CURRENT_STATE.md` and this file. Re-doing any of them wastes a successor's entire context on work that is already done and would not surface anything new — the actual remaining work is narrow and is listed in section 9.

# 11. Extraction validation

This extraction was built directly from `git log`, `governance/CURRENT_STATE.md` (read in full), `governance/DECISION_LEDGER.jsonl` (tail from `DL-0057`), and the INDIA20 boot/check artifacts — not from unverified memory. CCI cross-checked every commit hash and file path cited above against the actual repository before committing this file. One internal inconsistency was found during that check (section 6/8: `CURRENT_STATE.md` framed six-plus candidates as still-OPEN while later decision files showed them already locked by Mark). CCI resolved it by tracing each candidate through `git log -S`/`git show` to its authoritative, most-recent decision file rather than leaving it as an open question for the successor or for Mark — the live ledger CSV and `CURRENT_STATE.md` were both corrected accordingly (section 4.1). This extraction was reviewed by CCI three times before commit: once for completeness against the full commit list, once for internal consistency after the sync-repair fix was applied, and once for a final read-through against `CURRENT_STATE.md` as committed.

END INDIA20 FINAL EXTRACTION
