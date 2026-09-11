# A79 PROVENANCE GAPS — PART 2 (A041–A079)

Status: honest, unresolved gaps/contradictions found while restoring person-provenance for A041–A079. Nothing here has been papered over, guessed at, or silently resolved. No grade has been changed.

---

## GAP 1 — A059 [VNS-23] Shreyansanath Jain Tirth: an unresolved FAIL-vs-A contradiction

This project's own quality-control process (`india5/reports/VARANASI_NOT_TO_BE_MISSED_041_045_REASSESSMENT.md`, dated 2026-08-03) explicitly re-tested this candidate against the canonical `NOT_TO_BE_MISSED_FRAMEWORK` and concluded:

> "**Uitkomst: FAIL** ... De enige onderscheidende claim in het brondocument is fysieke nabijheid tot het bestaande Sarnath-cluster — een zuiver route-argument, expliciet uitgesloten als zelfstandige grond ... Bronsterkte: ZWAK — uitsluitend twee reisbronnen ... dit is de kandidaat uit deze vijf die waarschijnlijk nooit kandidaatstatus had moeten krijgen."

Yet `runs/active/INDIA10-CLUSTER-COVERAGE-REAUDIT-001/CURRENT_OLD_A_PROMOTION_MASTER.md` (2026-08-24) lists it under "VARANASI / SARNATH — RESOLVED" as a plain `A`, with no citation of new evidence and no acknowledgment of the FAIL finding one file over. `PROTECTED_CANON_BASELINE.csv` (id 043) shows it moved from `PROVISIONAL_NO_ABC` to the current frozen `A` without a visible reconciliation step in between.

**What CCI did:** left the grade untouched (A, per the frozen ledger — not CCI's call to change), and reported this exactly as found. **What is still open:** whether Mark ever saw and consciously overruled the FAIL finding, or whether the FAIL finding was simply lost/overlooked when the site was carried into the final ledger. A successor with write access to grading (not this task) should ask Mark directly whether he wants Jain heritage represented here, now that the weak-sourcing concern is visible again.

---

## GAP 2 — A048/A049 [VNS-34 / VNS-35] Lalita Ghat vs. Nepali/Kathwala Temple: possible physical duplication

The ledger and clock-audit treat `Lalita Ghat` (A048) and `Nepali / Kathwala Temple` (A049) as two separate physical entities, five minutes apart. External sources on Lalita Ghat's Nepali pagoda temple are not unanimous on whether this is one architectural complex described twice under two names, or genuinely two distinct structures. CCI did not find a repo source or an authoritative external source that definitively settles this within the task budget.

**What CCI did:** kept both as separate rows (per the frozen ledger — no grade/count change), and flagged the possible overlap explicitly in both entries rather than silently merging or silently ignoring it. **What is still open:** ground-truth confirmation (a map check or an on-the-ground note) of whether these are one stop or two.

---

## GAP 3 — A045/A046/A052 [VNS-25 / VNS-29 / VNS-01] Exact location of the Ramakrishna–Trailanga Swami meeting

Three independent detectors (internal, external-ChatGPT, IndiaGEEL — see `runs/active/TOP11-RAMANA-RAMAKRISHNA-MULTIDETECTOR-RECONCILIATION-001/RAMAKRISHNA_MULTIDETECTOR_RECONCILIATION.md`, record 17) confirm that Ramakrishna met and paid homage to Trailanga Swami during his 1868 Kasi pilgrimage. The internal freeze places this "bij Manikarnika" (near Manikarnika Ghat); external sources found by CCI in this task (ramdass.org, shreemaa.org) place Trailanga Swami's decades-long residence and samadhi specifically at Panchganga Ghat, a short distance from Manikarnika. These are not necessarily contradictory (Panchganga and Manikarnika are adjacent ghats in the same northern ghat arc), but CCI could not find a single source pinning the meeting to one exact ghat versus the other.

**What CCI did:** used `PROBABLY` rather than `YES` for the Panchganga/Manikarnika placement specifically, while keeping `YES` for the fact of the meeting itself (which is drieweg-confirmed). **What is still open:** a source that names the precise ghat of the historical meeting itself, if one exists.

---

## GAP 4 — A062 [KOL-02] Yogoda Satsanga Math, Dakshineswar: no confirmed personal presence by Yogananda

The current ledger/PDF calls this a "Direct Yogananda/Kriya anchor," implying a strong personal-presence link comparable to Dakshineswar Kali Temple (A061) or 4 Garpar Road (A064). External research in this task found that the Dakshineswar Math was established as YSS headquarters in **1939** — three years after Yogananda's final departure from India in 1936 (he never returned; he died in the US in 1952). No source, in the repo or externally, was found confirming that Yogananda personally visited, resided at, or was otherwise physically present at this specific compound.

**What CCI did:** marked `PERSON_WAS_PHYSICALLY_HERE: UNKNOWN` and classified the link type as `PERSON_FOUNDED_SITE` (as founder of the organization, in the institutional/spiritual sense) and `LINEAGE_INSTITUTION`, explicitly distinct from `EXACT_RESIDENCE`. **What is still open:** whether any YSS-internal or biographical source (not found within this task's budget/access) documents an actual visit by Yogananda to this exact site before 1936, e.g. during a preparatory/land-donation phase.

---

## GAP 5 — A065 [KOL-05] YSS Dhyana Kendra, Garpar: address continuity across 17/1 P.B. Lane → 37A Raja Dinendra Street

The YSS institutional history (`dakshineswar.yssashram.org/article/view/282`, fetched externally in this task) states the very first premises for Yogananda's boyhood meditation group were made available at "17/1, P.B. Lane" (procured 1911), while the centre's current official address is "37A, Raja Dinendra Street, Garpar." CCI could not confirm within this task's budget whether these are the same plot under an old/renamed street numbering, or whether the meditation society physically relocated at some point between 1911 and the 1951/1957 rebuild.

**What CCI did:** kept the strong personal-founding claim (Yogananda personally meditated here as a boy from ~1911) because both addresses are consistently described as the same continuous institution/lineage in the source, but flagged the specific address-continuity question as unresolved rather than asserting the two addresses are provably the identical physical plot. **What is still open:** a property-record or older YSS source that explicitly bridges the two addresses.

---

## GAP 6 — A070 [TIR-06] Gurumurtam: disputed year (1897 vs. 1898)

This is a pre-existing, explicitly acknowledged three-way conflict already on record in `runs/active/TOP11-RAMANA-RAMAKRISHNA-MULTIDETECTOR-RECONCILIATION-001/RAMANA_MAHARSHI_MULTIDETECTOR_RECONCILIATION.md`: "extern/IndiaGEEL geven zelf al aan dat afgeleide tijdlijnen wisselen tussen feb. 1897 en 1898." All three detectors (internal, external-ChatGPT, IndiaGEEL) acknowledge the conflict; none resolves it. CCI did not attempt new resolution in this task (out of scope — this is a pre-existing, already-flagged research conflict, not a new provenance gap CCI introduced), and simply carried the acknowledged uncertainty forward.

**What is still open:** the same as before this task — a primary/authoritative source that fixes Ramana's Gurumurtam period to one specific year.

---

## GAP 7 — Scope clarification (not a contradiction, but worth recording explicitly)

The dispatch's own calibration text asked whether "4 Garpar Road is clearly identified as Yogananda's actual birth house (EXACT_BIRTH_SITE)." Research in this task shows this framing itself was incorrect: Yogananda was born in Gorakhpur (5 January 1893), not Kolkata. 4 Garpar Road is his boyhood/family home from childhood onward, not his birthplace. This is recorded here explicitly (and corrected in the main PART2 files) so that a future PDF-builder does not inherit the dispatch's implicit assumption and mislabel the site as a birth site. No trip location was added or removed as a result — Gorakhpur is not, and is not being proposed to become, part of this itinerary.

---

## Summary of what was NOT found to be a gap

For the many ordinary south-Varanasi/ghat/temple microcluster items in this range (A042, A043, A048, A049, A050 and the historical-building-identity note on A047) CCI found **no** Mark priority-person connection in the repo or via external research, and did **not** invent one. Per the governing rule's own instruction ("If the original reason cannot be recovered, label that as a data/provenance gap. Do NOT silently replace it with a generic tourist description"), these are reported honestly as genuine, intrinsically-valuable Hindu devotional/architectural sites without a Tier-1 person link — this is a finding, not a failure of this task.
