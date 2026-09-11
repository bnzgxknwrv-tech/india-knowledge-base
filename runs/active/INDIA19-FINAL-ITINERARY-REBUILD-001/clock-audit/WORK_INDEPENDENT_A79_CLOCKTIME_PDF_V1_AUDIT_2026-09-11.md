# WORK_RESULT — INDIA19 A79 CLOCKTIME PDF V1 INDEPENDENT AUDIT

## Audit binding and method

- `AUDIT_PACKET_HEAD`: `be3221681e634bf3be2538793c29d7c7c1789b59`
- Frozen authoritative A-ledger: `a2b71b2563f446480b012f0b9176a87e96fcb003`
- Manifest: `INDIA19_Kloktijdplanning_A79_v1_AUDIT_MANIFEST.md`
- Declared PDF: `INDIA19_Kloktijdplanning_A79_v1.pdf`
- Declared PDF SHA-256: `0adec758ca70f596d81f3f2b38495f3a063aa6af61f1d8fb927b33cfb36e6c80`
- Scope: the manifest and all seven bound text mirrors at the pinned commit were read in full. The new CCI audit was not read.
- Binary limitation: the manifest deliberately does not persist the PDF binary in Git. Therefore this audit can verify the seven mirrors and their repeated PDF binding, but cannot independently recompute the PDF SHA-256 or visually inspect the PDF bytes. This is an audit limitation, not evidence of a content mismatch.

## Verdict

**PASS_WITH_CORRECTIONS**

**SAFE_FOR_MARK_TEMPO_DECISIONS = NO**

The packet passes the central completeness test: it contains exactly 79 ordinary A+/A records, numbered uniquely A001–A079, and every record is visible in the index, an individual detail card and the day-by-day clock plan. It preserves all seven A* records separately, preserves 33 nights and does not change grades or route canon.

It is not yet safe as the final surface for Mark's tempo decision because one scheduled access time is outside the frozen access window, several consecutive blocks do not contain their own stated movement time, one appointment-dependent A is shown as unconditional, and the plan does not expose sleep opportunity/cumulative burden across all 33 nights. These are local clock/presentation repairs; they do not justify a new global solve or a macro-route reopening.

## Required checks

| Required check | Result | Finding |
|---|---|---|
| 79/79 A+/A | PASS | Frozen ledger and packet both contain 79 ordinary records: 24 A+ and 55 A. No missing or extra source IDs. |
| Unique A001–A079 | PASS | 79 unique sequential IDs; no duplicate or missing number. |
| Individual visibility | PASS | Every A appears in the index, on an individual detail card and in a dated clock block. Parent/world records are explicitly nested rather than silently omitted. |
| Clocktimes | PASS_WITH_CORRECTIONS | All 79 have times, but A068 violates its access window and several adjacent blocks have no room for their stated transfer. A052's “open einde” is contradicted by a fixed end time. |
| Distance/travel time between consecutive A's | PASS_WITH_CORRECTIONS | Every transition has a stated geometry/burden treatment, but several nonzero movements are not represented in the clock arithmetic. A064→A065 is presented as known geometry although the frozen governance says the exact pins are not yet established. |
| Person/AOAY links | PASS_WITH_CORRECTIONS | Links are present for all records, but A061 is materially understated and A008, A010 and A065 are overstated as direct AOAY/site links. A036 and A016 require site-level versus person/memory wording. |
| Closures/access | PASS_WITH_CORRECTIONS | Sarnath Sunday logic and the explicit A039/A064 access gates pass. A038 lacks its mandatory appointment gate; A068 is scheduled before the frozen 08:30 opening. |
| Transfers and humane burden | MATERIAL DEFECT | Major transfers are visible, but sleep opportunity and cumulative fatigue are not recorded across all 33 nights. The final Jan 20 day remains conditional and flight safety correctly outranks A079. |
| 33-night logic / AI155 | PASS | 19 Dec 2026 through 20 Jan 2027 equals 33 nights; AI155 departs Delhi Thu 21 Jan 2027 at 12:20. |
| Quiet days | PASS | Haidakhan quiet days 27–28 Dec are preserved without logistics. |
| Sarnath | PASS | Sunday 10 Jan is used; Friday museum closure is avoided. |
| Kolkata | PASS_WITH_LRL | Tue 12 Jan is transfer-only; A061–A063 are on Wed 13 Jan. Exact YSS/program, museum/ferry and same-day access remain live rechecks. |
| A039 / A064 | PASS | Both are explicitly access-gated rather than guaranteed. A039 has a retry; A064 requires pre-arrival confirmation. |
| Seven A* records | PASS | All seven frozen A* IDs are separately visible and are not counted among the 79 ordinary A+/A records. Sattal/Rajgir promotion conditions are not silently activated. |
| B3/T4 tempo usefulness | NOT YET SAFE | The document is useful for orientation, but the defects below prevent using this exact v1 as the decisive true-tempo surface. |

## Defect register

### HARD — local repair required

1. **A068 / TIR-03 — Virupaksha Cave is scheduled before the frozen access window.**
   - Packet: Sat 16 Jan, 08:00–09:30.
   - Frozen operational sources repeatedly place current cave access at approximately 08:30–16:30 and use an 08:30 cave-block start.
   - The approach block is only 07:30–08:00 although the packet's own approach range is 30–50 minutes. A069 starts 09:45, only 15 minutes after A068, while the stated climb is 20–30 minutes.
   - **Repair:** start A068 no earlier than 08:30; move A069 to at least 10:00/10:15 and reflow descent/lunch locally.
   - **Macro effect:** none.

### MATERIAL — local clock/canon presentation repair

2. **A021→A022 has no room for its stated uphill transfer.**
   - A021 ends 12:15 and A022 starts 12:15; the packet states 0.3–0.8 km and 15–30 minutes uphill.
   - If the climb is included in A022's 45-minute block, actual on-site dwell is only 15–30 minutes and must be said explicitly. Otherwise the clock is impossible.
   - **Repair:** expose the climb within the block or shift A022; keep `SCHEDULED IF SAFE` explicit.

3. **Whole-human burden is not complete enough for a tempo decision.**
   - There is no explicit sleep-opportunity/wind-down ledger for all 33 nights.
   - The schedule contains approximately six sub-05:30 disruptions, including rail arrivals/wakes: 20 Dec (~05:05), 5 Jan (05:10), 6 Jan (05:15), 7 Jan (05:10), 17 Jan (03:45) and 20 Jan (03:15).
   - Five consecutive loaded days appear on 13–17 Jan (`FULL`, `NORMAL/FULL`, `HIGH FRICTION`, `FULL`, `FULL/PHYSICAL`). Jan 9 is overloaded and Jan 10 full, with recovery only on Jan 11.
   - Jan 20 runs roughly 03:15–22:00 and combines flight, A077, A078 and conditional A079. At the upper end of the A077→A078 road estimate, its 120-minute gap leaves only about 20 minutes for lunch.
   - **Repair:** add per-night sleep opportunity, early-wake count and cumulative-load warnings; retain the existing safety precedence and conditional A079.

4. **A038 / VNS-02 — Bhrigu Karyalaya is shown without its mandatory appointment gate.**
   - Packet: Wed 7 Jan, 10:00–11:30, presented as a scheduled visit.
   - Frozen sources require advance confirmation of a genuine Bhrigu/Bhadury-family reading and insertion of the confirmed appointment as a mandatory block.
   - **Repair:** label `ACCESS/APPOINTMENT GATE`; do not present the 10:00 block as unconditional.

5. **A052 / VNS-42 — Manikarnika open-end canon conflicts with the clock.**
   - The text says “open einde/geen strak vertrekdoel,” while the block ends exactly at 18:30 and the return is fixed at 18:30–19:30.
   - **Repair:** show `15:15–open end` plus a flexible return/wind-down band.

6. **A064→A065 exact geometry is asserted before the two pins are frozen.**
   - Packet: 0.5–1 km / 5–15 minutes between 4 Garpar Road and the current YSS Garpar centre.
   - Frozen governance distinguishes the historical house and the current centre and forbids a pin/geometry conclusion until both exact access points are verified.
   - **Repair:** mark distance/time `LRL / exact pins unverified` and retain A064's pre-arrival access gate.

7. **Person/AOAY taxonomy needs targeted correction.**
   - **A061 / Dakshineswar Kali Temple:** the packet understates it as indirect/no Yogananda biographical site. The frozen AOAY atlas classifies Dakshineswar as `TIER_AOAY_EXACT_SITE`, with repeated Yogananda pilgrimages/sacred experience, in addition to its Ramakrishna link.
   - **A010 / YSS Dwarahat Ashram:** a modern YSS institution in the Babaji/Kriya region, not a direct AOAY physical-event site for all four named Kriya figures.
   - **A008 / Babaji Smriti Bhavan:** modern memorial/commemorative link; A009, the cave, is the direct AOAY site.
   - **A065 / current YSS Garpar centre:** current adjacent/successor institution; not proof of the exact historical room/site. A064 is the direct historical house.
   - **A036 / Anandamayi Ma Ashram, Bhadaini:** direct person/AOAY memory through Yogananda's meeting and writing, but not a demonstrated site-specific AOAY event at Bhadaini.
   - **A016 / Taj Mahal:** retain the supported Yogananda historical-photo/memory cue without implying an uncited AOAY textual episode.
   - **Repair:** correct link labels only; do not change grades or remove any A.

### MINOR — clock notation cleanup

8. **Several adjacent A blocks have zero clock gap despite a nonzero stated movement.**
   - A011→A012: 5–15 min.
   - A029→A030: 2–5 min.
   - A045→A046: 2–5 min.
   - A046→A047: 5 min.
   - A048→A049: 2–5 min.
   - A051→A052: 5 min.
   - A053→A054: 10 min.
   - **Repair:** explicitly nest movement in one block or shift the next start. This is not a reason to delete or downgrade any A.

## Confirmed non-defects and LRL items

- A032, A053 and A066 are parent/world experiences with nested child locations. Their structure does not mechanically double-count visits, but the nesting must remain explicit.
- A062's direct AOAY/Yogoda link and A064's direct historical-house link are supported.
- Ramana Maharshi and Haidakhan Babaji/Mahavatar Babaji identity distinctions are preserved.
- Exact-date rail and flight inventories remain `LIVE_RECHECK_LATER`, including 12039, Gatimaan, 12988, 20887, VNS–CCU, CCU–MAA and MAA–DEL.
- Kolkata operational LRL remains: exact YSS visitor/program hours, Belur Math museum sessions/ferry and current access.
- A065 January programme/access remains LRL.
- A079 remains conditional; final-flight safety correctly has priority.

## Repair boundary

All identified defects are local to clock arithmetic, access qualifiers, AOAY wording or burden display. The audit does **not** authorize a new global route solve, changed grades, removed A+/A locations, changed nights, changed hotels, or a macro-route reopening.

After the local corrections are made, rerun the same mechanical 79/79, transition-arithmetic and burden checks and independently hash/render the actual PDF artifact if its bytes are made available.
