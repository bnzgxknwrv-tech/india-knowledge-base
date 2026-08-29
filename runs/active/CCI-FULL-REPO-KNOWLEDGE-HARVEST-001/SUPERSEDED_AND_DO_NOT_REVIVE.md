# Superseded and Do Not Revive

> Provenance note. This file was produced by the repository-wide knowledge harvest
> `CCI-FULL-REPO-KNOWLEDGE-HARVEST-001` on worker branch `agent/cci-full-repo-knowledge-harvest`,
> frozen against central commit `a37423639f7dabb0dfd55c8656d4689bb8a25351`.
> It is **archaeology and reconciliation**, not new decision-making. No Mark A/B/C grade, hotel or
> sleepbase lock, route lock or dwell decision was created, changed or inferred here.
> Every statement below carries its exact source so a successor can re-verify it independently.
> Where a statement contradicts a newer explicit Mark decision, **the newer Mark decision wins**.

Things that look current but are not, things that were deliberately withdrawn, and factual claims
that were retracted after verification. A successor that skips this file will re-import errors
that this project has already paid to find.

The most dangerous single entry is `SUP-001`: the grade `A+` was **abolished by Mark and later
returned with a different meaning**. Any grade read from a pre-INDIA10 file is in a different
vocabulary from the current one.

---

## SUP-001

VOCABULARY TRAP — the A+ grade was ABOLISHED and later RETURNED WITH A DIFFERENT MEANING. On 2026-07-11 commit 20db360a first harmonised METHODOLOGY to A+/A/B/C/R; on the SAME DAY commit 0d118b1d records Mark's decision to SCRAP A+ and R entirely ('A+ overbodig' — Mark knows his own top places), leaving A/B/C/U where A = definitely visit, B = interesting, Mark decides later, C = seen and deliberately rejected (NOT 'probably not' — when in doubt it is B), U = unassessed WORK STATUS not a grade. A+ was then REINTRODUCED in the INDIA10 generation with the NEW meaning 'trip-defining / can carry a cluster', and A* was added later still. Any pre-INDIA10 'A+' must never be read with the current meaning, and any pre-INDIA10 file that lacks A+ is not evidence that a place was not top-tier.

- **Class:** `SUPERSEDED`  |  **Integration state:** `PROVENANCE_ONLY`
- **Source:** commits 20db360a and 0d118b1d (2026-07-11) message bodies vs current governance/INDIA_MASTER_BOOT.md §7
- **Note:** Largest vocabulary-drift trap in the repository; visible only through commit archaeology.

## SUP-002

Poort T (DELTA-ONLY re-assessment) was canonised and RETRACTED on the same day (2026-08-08). It was only ever a practical aid for the Bodh Gaya correction round, not a permanent rule — future sweeps must prevent late material corrections via the double sweep + reconciliation + integral pre-PDF QA (poort R). GOUD/USER/DELTA_REVIEW_2026-08-08.md therefore exists WITHOUT a canon basis and must not be used to re-canonise poort T. An INGETROKKEN_CANONPOGING note was deliberately left in ACTIVE_STATE.md for exactly this reason.

- **Class:** `SUPERSEDED`  |  **Integration state:** `PROVENANCE_ONLY`
- **Source:** commits 58c4f642 then 7587889e (2026-08-08)

## SUP-003

RETRACTED FACTUAL CLAIM: 'Ramakrishna visited Bodh Gaya and meditated before the Buddha image' is WRONG. Direct recheck of the cited source (sriramakrishna.in) shows the opposite — he deliberately REFUSED to visit Gaya in 1868. The correct Ramakrishna link is his father Kshudiram's naming Gadadhar/Vishnu vision during the 1835 Gaya pilgrimage, and it was moved from candidate 046 to 051.

- **Class:** `INVALID_DECISION_RECORD`  |  **Integration state:** `REJECTED_OR_SUPERSEDED`
- **Source:** commit 46fa5260 (2026-08-08)

## SUP-004

CORRECTED CLAIM: Ram Dass's S.N. Goenka Vipassana course is JANUARY 1971, not 'winter 1969-70'. The exact venue cannot be decided between 074 (Samanvaya Ashram) and 061 (Burmese Vihara) — two courses ran back to back and the available sources do not distinguish which one Ram Dass attended.

- **Class:** `CONFLICT_NEEDS_RECONCILIATION`  |  **Integration state:** `ADOPTED`
- **Source:** commit 46fa5260 (2026-08-08)

## SUP-005

CORRECTED GENEALOGY: a delivered PDF described Sri Yukteswar as 'the teacher of Yogananda's teacher', which actually describes LAHIRI MAHASAYA. The correct line is Babaji -> Lahiri Mahasaya -> Sri Yukteswar -> Yogananda; Sri Yukteswar was Yogananda's OWN DIRECT guru. The sannyas-initiation founder Swami Krishna Dayal Giri was added at the same time.

- **Class:** `INVALID_DECISION_RECORD`  |  **Integration state:** `REJECTED_OR_SUPERSEDED`
- **Source:** commit e1c23178 (2026-08-05)

## SUP-006

CORRECTED ATLAS DATA: 'Dwarka' in the AOAY atlas (5 occurrences) was actually 'Dwarka Prasad', a PERSON's name, not the pilgrimage town — a name collision. 'Belur' had been assumed to be Belur Math (Bengal, Vivekananda) but close reading of chapter 41 shows it is the unrelated Belur temple in KARNATAKA. Both corrected in place, not silently dropped.

- **Class:** `INVALID_DECISION_RECORD`  |  **Integration state:** `REJECTED_OR_SUPERSEDED`
- **Source:** commits cd0ff2b1 (2026-08-17), 1b389a1e (2026-08-16)

## SUP-007

CORRECTED SELF-ERROR: an internal freeze recorded 21 March 1936 as Sri Yukteswar's death date from AOAY ch. 42, but that passage describes the death BHANDARA (memorial ceremony tied to the spring equinox), not the mahasamadhi. Correct sequence: mahasamadhi 9 March 1936, burial 10 March, bhandara 21 March — triple cross-validated.

- **Class:** `INVALID_DECISION_RECORD`  |  **Integration state:** `REJECTED_OR_SUPERSEDED`
- **Source:** commits 59463c13 (2026-08-19), 2889174e (2026-08-19)

## SUP-008

CORRECTED BABAJI LOCALISATION: the Babaji / Mataji / Lahiri appearance was wrongly localised at Ram Gopal's cave (Ranbajpur/Tarakeswar) instead of the actual AOAY location DASHASHWAMEDH GHAT, VARANASI. An external date claim '25 July 1920' for the Babaji-Gurpar-Road meeting does NOT appear in AOAY ch. 37.

- **Class:** `INVALID_DECISION_RECORD`  |  **Integration state:** `REJECTED_OR_SUPERSEDED`
- **Source:** commit 0bfeb45b (2026-08-19)

## SUP-009

FALSE_OR_UNSUPPORTED_EXTERNAL_CLAIM register: (a) the 'walking on the beach in Jaganath Puri' quote attributed to Sara Davidson does not appear in either cited source (both fully downloaded and searched) — not adopted; (b) an external freeze claimed 'no evidence' for Lahiri's presence at the Allahabad Kumbh Mela, but AOAY ch. 33 confirms it unambiguously (washing an ascetic's feet); (c) an external atlas contained a hallucinated Jagannath-temple quotation (record #42); (d) the Krishnamurti-meeting site for Anandamayi Ma is Kitty Shiva Rao's Delhi garden, NOT the Rajghat/Krishnamurti Foundation campus; (e) a 'Mandi' claim was sourced only to 'AI2's own methodology section', a union-compilation artifact.

- **Class:** `REJECTED_BY_MARK`  |  **Integration state:** `REJECTED_OR_SUPERSEDED`
- **Source:** commits 20c281ce, 05cc7daa (2026-08-19), b42b069a (2026-08-19), 9e471179 (2026-08-16)
- **Note:** Rejected on evidence, not by Mark personally; kept here so no successor re-imports them.

## SUP-010

CORRECTED ATTRIBUTION: 'Sacred Wanderer' is RAVI DASS's book, not Ram Dass's. The correct core Ram Dass biography is 'Being Ram Dass' (2021). Also: a 1997 Vrindavan mention turned out to concern a DIFFERENT devotee who heard news there about Ram Dass's stroke, not Ram Dass's own presence. The Haidakhan ashram's own 'Ram Dass' is a NAME COLLISION and a non-identity.

- **Class:** `INVALID_DECISION_RECORD`  |  **Integration state:** `REJECTED_OR_SUPERSEDED`
- **Source:** commits 0f7a0993 (2026-08-19), f3a5e5da (2026-08-19), 119f80e9 (2026-08-16)

## SUP-011

EXCLUDED-BUT-NUMBERED Bodh Gaya candidates (numbers permanently reserved, never reused): 069 Mongolian Temple, 075 Jain Temple Gaya, and after the retroactive E.1 test 053 Root Institute, 054 Wat Thai, 055 Royal Bhutan Monastery, 056 Tibetan Temple, 057 Vietnamese Temple, 059 Metta Buddharam/Silver Temple, 064 Chinese Temple, 065 Bangladesh Buddhist Monastery, 066 Cambodian Monastery, 067 Korean Temple — all EXCLUDED_HARD_REASON because their only remaining distinction was country/tradition REPRESENTATION or pure architecture.

- **Class:** `SUPERSEDED`  |  **Integration state:** `PROVENANCE_ONLY`
- **Source:** commits 557cfd28, 54b8ba9d, 9cab2431 (2026-08-05..08)

## SUP-012

CORRECTED ABSOLUTE CLAIMS: 'the only Thai temple in India' (054 Wat Thai) is FALSE — at least two other Thai temples confirmed in Delhi (Wat Thai Temple Sant Nagar; Bhogal Buddha Vihar). 054 'first foreign monastery' corrected to 'first MODERN foreign monastery' (an older Sri Lankan Sangharam exists). 055 'exists nowhere outside the Himalaya' corrected to the actual source wording (a superlative, not an absolute). 056 canonical_name corrected from the unconfirmed 'Namgyal Monastery' (with a Dalai Lama claim) to the officially confirmed 'Tibetan Temple', with Namgyal/Karma Temple recorded as UNCONFIRMED aliases — the NUMBER 056 itself stayed immutable and got an append-only CANONICAL_NAME_CORRECTION record.

- **Class:** `INVALID_DECISION_RECORD`  |  **Integration state:** `REJECTED_OR_SUPERSEDED`
- **Source:** commits e52b7a9c (2026-08-07), ad641131 (2026-08-05)

## SUP-013

DO NOT REVIVE: BOOKING_CONTACT_PACK.md (deleted). It contained copy-ready booking messages with exact dates (Haidakhan 20-23 Dec 2026; Joshi Guest House 23-26 Dec; Hotel Evelyn 26-29 Dec; Sahi River View 5-11 Jan 2027; Sri Ramanasramam 14-19 Jan 2027). It was DELIBERATELY REVERTED as premature, together with its status and state updates, and the whole booking sequence was demoted to a future planning artifact. Its dates are old-V2 dates and its Kumaon base is the superseded Joshi Guest House. Only the wording guard ('do not ask to reserve the Ram Dass room') should carry forward.

- **Class:** `REJECTED_BY_MARK`  |  **Integration state:** `REJECTED_OR_SUPERSEDED`
- **Source:** commits 7fddaf9e -> b3a66b26 -> 341ecab2 -> ba82d753 -> 5bd2e865 (all 2026-08-23)

## SUP-014

DEPRECATED ARCHITECTURE: the india5/tasks/ file-based task architecture (TASK.yaml/STATUS.yaml with sha256 hashes, ACLs, completion markers) was explicitly considered and judged TOO HEAVY. It was deliberately NOT reactivated and remains deprecated in favour of the lighter runs/active/<TASK_ID>/TASK.md + STATUS.md + RESULT.md relay (poort O.1). Do not resurrect it.

- **Class:** `SUPERSEDED`  |  **Integration state:** `PROVENANCE_ONLY`
- **Source:** commits 71d2e7b7 (2026-08-09), 17b92442 (2026-08-08)

## SUP-015

SUPERSEDED GENERATIONS whose files remain readable but must never independently control current truth: the india1/india2 Dutch governance generation (AI_RULES, OPERATING_MODEL, LOCKED_A/B/C, CLUSTER_LOCATIONS 1-46, CLUSTER_ANCHORS, PRIORITY_GROUPS, METHODOLOGY, LESSONS, CHAT_DISTILLATION, PLACE/PERSON/SOURCE-0001 records); the whole INDIA3 pipeline generation (ARCHITECTURE, OPERATING_PRINCIPLES, CONTEXT_POLICY, MEMORY_POLICY, FAILURE_RECOVERY, CAPABILITY_CHECK, USER_COMMUNICATION, START_PROMPTS, 13 protocols, 4 role contracts, 17 templates) — now DELETED from every tip; the INDIA4/INDIA5 PRE-BRONS/detector architecture; and all BRONS/ZILVER/GOUD region-run outputs.

- **Class:** `HISTORICAL_PROVENANCE_ONLY`  |  **Integration state:** `PROVENANCE_ONLY`
- **Source:** recovered deleted india3/** (55 files); central india4/, india5/ trees

## SUP-016

SUPERSEDED SLEEP/ROUTE MODULES: the Kasar Devi / Almora / Turiya Niwas sleep module is NOT part of the current trip; the old Joshi Guest House primary lock is superseded by Dunagiri Retreat (Joshi retained only as fallback); the old YSS half-day file was superseded by a dedicated full-day rest-first plan and YSS overnight is BANNED; the old Agra Taj-only one-night baseline is historical only; old Mysore/Bengaluru optional-route sets are not current competitors merely because historical files mention them.

- **Class:** `SUPERSEDED`  |  **Integration state:** `PROVENANCE_ONLY`
- **Source:** a37423639f7dabb0dfd55c8656d4689bb8a25351:governance/INDIA_RECOVERY_DELTAS_CURRENT.md R08/R16; CURRENT_DECISIONS_MASTER.md §12; commits "INDIA10: supersede obsolete YSS half-day file", "INDIA10: canonize full-day YSS Dwarahat plan and ban YSS overnight"

## SUP-017

Tutla Bhawani waterfall is WINTER-MISMATCH PROVENANCE — it is NOT a Mark C and is not actionable in the current Dec/Jan window absent materially better winter evidence. Do not present it as an open item and do not record it as a rejection.

- **Class:** `HISTORICAL_PROVENANCE_ONLY`  |  **Integration state:** `PROVENANCE_ONLY`
- **Source:** a37423639f7dabb0dfd55c8656d4689bb8a25351:governance/CURRENT_STATE.md; CURRENT_DECISIONS_MASTER.md §8

## SUP-018

Impossible-window discoveries remain provenance and must NOT become actionable ballot items.

- **Class:** `CURRENT_CANON`  |  **Integration state:** `ADOPTED`
- **Source:** a37423639f7dabb0dfd55c8656d4689bb8a25351:governance/CURRENT_DECISIONS_MASTER.md §13

## SUP-019

PROTECTED_CANON_BASELINE.csv is NOT sufficient current grade truth. It is the permanent-ID / protected-older-decision anti-forget layer, but can contain older statuses not reflecting later explicit Mark decisions (proof patterns: Varanasi 041-045 provisional in the baseline while later Mark decisions exist; later A+ promotions outranking old A/B/C). It is now a CONDITIONAL, not every-boot, read. It exists ONLY on branch agent/indiazilver-cluster-completeness-audit and its central counterpart lives under runs/active/INDIAZILVER-ENTITY-ID-PROXIMITY-BACKFILL-001/.

- **Class:** `CURRENT_CANON`  |  **Integration state:** `ADOPTED`
- **Source:** a37423639f7dabb0dfd55c8656d4689bb8a25351:governance/INDIA_RECOVERY_DELTAS_CURRENT.md R11; commit c59dc33c (2026-08-23) headline finding

## SUP-020

All 68 branch-only blobs that share a path with the central tree were diffed against frozen central: EVERY ONE is an OLDER version and central is the newer/richer side in all 68. Four plausible loss candidates were additionally git-grep-verified present in central (Bodh Gaya per-number A/B/C, Varanasi VNS-CAND 001-040 grades, Kumaon legacy locks, Mark's 'die grot is bijna reden 1' quote). NO same-path knowledge loss exists. Do not spend successor effort re-checking this.

- **Class:** `HISTORICAL_PROVENANCE_ONLY`  |  **Integration state:** `ADOPTED`
- **Source:** this harvest, diff chunks DF_001-DF_018

## SUP-021

DO NOT re-derive from the conditional registers without checking their date. Two conditional registers disagree with each other and with the current layer: CURRENT_OLD_A_PROMOTION_MASTER.md is dated 2026-08-24 and closed; A_PLUS_MARK_DECISION_LOG.md is dated 2026-08-27 and is the later authority; PROTECTED_CANON_BASELINE.csv is older still. Known concrete divergence: Kakrighat is A in the 2026-08-24 promotion master and A* in the 2026-08-27 decision log. Always take the latest dated register, and above all the latest explicit Mark decision.

- **Class:** `CONFLICT_NEEDS_RECONCILIATION`  |  **Integration state:** `ADOPTED`
- **Source:** a37423639f7dabb0dfd55c8656d4689bb8a25351:runs/active/INDIA10-CLUSTER-COVERAGE-REAUDIT-001/A_PLUS_MARK_DECISION_LOG.md vs a37423639f7dabb0dfd55c8656d4689bb8a25351:runs/active/INDIA10-CLUSTER-COVERAGE-REAUDIT-001/CURRENT_OLD_A_PROMOTION_MASTER.md
- **Note:** PARITY REPAIR (iteration 1). This item-level Mark grade is NOT present in any of the eight always-read central boot files; it lives only in a register the current boot demotes to a CONDITIONAL read. A successor booting the central layer alone would not see it.

---

### How to use this file

Before adopting anything from an older generation, search this file for the place name, the claim,
or the artifact name. If it appears here, do not adopt it without reading the `Source` line and
confirming that no *later* explicit Mark decision has changed the situation again.

A retraction recorded here is **evidence-based**, not a Mark rejection, unless the class is
`REJECTED_BY_MARK`. Evidence-based retractions can in principle be reversed by better evidence;
a Mark rejection can only be reversed by Mark.
