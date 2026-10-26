# INDIA19 A79 V2 RECONCILIATION — 2026-09-11

Status: **ADOPTED LOCAL REPAIR / SAFE FOR MARK TEMPO REVIEW**

## Exact binding

- v1 audit packet head: `be3221681e634bf3be2538793c29d7c7c1789b59`
- frozen authoritative A-ledger: `a2b71b2563f446480b012f0b9176a87e96fcb003`
- CCI task: PR #23 comment `5631614635`
- CCI result: PR #23 comment `5631777382`, `PASS_WITH_CORRECTIONS`, worker commit `0f2129b`
- WORK task: PR #23 comment `5631617560`
- WORK result: PR #23 comment `5632780362`, `PASS_WITH_CORRECTIONS`, frozen audit commit `7ec6e382efec4ff3f4081ef344defd7031ebf155`
- v2 rendered PDF filename: `INDIA19_Kloktijdplanning_A79_v2.pdf`
- v2 PDF SHA-256: `6f3eeb2296cdb5f6ac68c757f2a4c15480830cae77a1795818ced0dfa0ed57c8`
- v2 DOCX SHA-256: `a8154a5fce608f604928248d1ce8ec579994e6d52ab05dac1f8df874a484c3de`

The PDF/DOCX bytes are conversation artifacts, not claimed to be persisted as binary GitHub repository files. The repository records the authoritative correction set and hashes; this avoids the v1 chain-of-custody overclaim noted by CCI.

## Reconciliation verdict

Both independent audits agree on the important points:

- ordinary A+/A population is complete: **79/79**;
- numbering is complete and unique: **A001–A079**;
- all 79 are individually visible; no parent/world hiding was found;
- the seven A* rows remain separate and conditional, not falsely counted as ordinary A+/A;
- exactly 33 physical India nights remain intact;
- Sarnath Sunday repair is correct;
- Kolkata 12 Jan transfer-only repair is correct;
- Haidakhan protected quiet days remain intact;
- no audit defect requires a new global route solve, grade change, A removal, duration reopening or FINAL OUT reopening.

## Adopted v2 local repairs

### Clock arithmetic / access

1. `A012 KUM-02` Historic Haidakhan cave: `17:00–17:45`, leaving explicit transition after A011.
2. `A022 BOD-05` Pragbodhi/Dungeshwari ridge: `12:45–13:30`, with the 15–30 minute uphill movement from A021 explicitly outside the site dwell.
3. `A030 VNS-06` Banarasi paan: `13:20–13:40`, preserving a real movement gap from A029.
4. Varanasi 9 Jan microsequence reflowed so nonzero movements are represented: A046 `09:20–09:50`, A047 `09:55–10:25`, A048 `11:25–11:55`, A049 `12:00–12:30`, A052 starts `15:20`.
5. `A052 VNS-01` Manikarnika restored to true open-end semantics: `15:20–open end`, with flexible return band rather than a contradictory hard 18:30 end.
6. `A053 VNS-04` Sarnath parent/world orientation shortened to `08:20–08:30`; `08:30–08:40` is explicit movement to A054.
7. `A068 TIR-03` Virupaksha Cave moved to `08:30–09:45`, not before the frozen access window; A069 becomes `10:15–11:15` and the descent/lunch blocks are reflowed locally.
8. `A038 VNS-02` Bhrigu Karyalaya now carries an explicit `ACCESS/APPOINTMENT GATE`; the shown 10:00 slot applies only if a genuine appointment is confirmed.
9. `A064 -> A065` Garpar geometry is now `LRL / exact pins-access points unverified`; no precise walk-distance claim is made until both access points are frozen.

### AOAY/person taxonomy

10. `A061 KOL-01` Dakshineswar is corrected to direct Yogananda/AOAY site-memory as well as the Ramakrishna anchor.
11. `A010 KUM-10` YSS Dwarahat is described as a modern YSS/Yogananda institution in the Kriya/Babaji landscape, not as separate proven physical AOAY events for all four Kriya figures.
12. `A008 KUM-12` Babaji Smriti Bhavan is described as a modern memorial/commemorative link; A009 cave remains the direct physical anchor.
13. `A065 KOL-05` current Garpar YSS centre is treated as a living successor institution, not proof of the exact historical room/site; A064 remains the direct historic-house anchor.
14. `A036 VNS-26` Anandamayi Ma Bhadaini is a direct person/AOAY memory through Yogananda’s meeting/writing, without claiming that the specific meeting occurred at this Bhadaini site.
15. `A016 AGR-01` Taj Mahal retains the supported Yogananda historical photo/memory cue without implying an uncited AOAY textual episode.

### Whole-human burden / festival disclosure

16. v2 adds a **33-night sleep/recovery ledger** with a conservative sleep-opportunity band for every night.
17. Explicit aggregate burden metrics added:
   - 6 sub-05:30 disruptions;
   - 0 planned arrivals after 22:00, with ~22:00 boundary cases noted;
   - 2 fragmented train nights;
   - 5 consecutive loaded days on 13–17 Jan;
   - 9 Jan remains `OVERLOADED`;
   - 20 Jan remains `OVERLOADED / FLIGHT-SAFETY FIRST`.
18. 15 Jan CCU→MAA→Tiruvannamalai now explicitly discloses **Makar Sankranti/Pongal crowd/traffic/accommodation pressure**. This is treated as a material live-recheck/early-booking risk, not as proof that the route is impossible. The Friday Sri Chakra Puja remains optional and is not forced after the transfer day.

## Mechanical v2 QA

INDIA19 reran mechanical checks after the repairs:

- `A_COUNT = 79`
- `A_UNIQUE = 79`
- `A001_A079_CONTIGUOUS = PASS`
- `SLEEP_LEDGER_33_NIGHTS = PASS`
- corrected A-times are present in both index and day tables;
- A038 gate present;
- A052 open-end present;
- A064/A065 exact geometry downgraded to LRL;
- Pongal disclosure present;
- corrected AOAY taxonomy present;
- PDF rendered to 28 pages and every page visually inspected; no clipping/overlap/broken-table defect found.

## Current decision meaning

`INDIA19_Kloktijdplanning_A79_v2` is now the **current Mark-facing true-tempo surface**.

It is intentionally not made prettier by deleting A-locations. Mark can now judge the real pace with all ordinary A+/A present and communicate using unique numbers A001–A079. Any later A→B change remains a Mark decision, not an optimizer shortcut.

The macro topology remains:

`Kumaon-first -> 12039 daytime north exit + Delhi transit bed -> Agra/Taj -> 12988 -> Bodh Gaya -> Varanasi/Sarnath -> Kolkata/Dakshineswar -> Tiruvannamalai -> Chennai airport night -> final Delhi -> AI155`

Primary tempo version remains **Bodh Gaya 3 nights / Tiruvannamalai 4 nights**. This does not erase the prior finding that 2/5 is a valid subjective alternative; v2 is the audited 3/4 surface for Mark’s actual pace review.
