# INDIA26 — REPO AUDIT — 31 FINDINGS — 2026-10-05

Branch: `claude/werk-je-nu-of-niet-oa10y7`  
Status: COMPLETE AUDIT HANDOFF  
Authority: audit/research only; this file makes no new Mark decisions.  
Precedence: `DL-0002` — newest explicit Mark decision outranks later assistant summaries/plans.

## Totals
- Contradictions: 6
- Genuine open/follow-up items: 10
- Strong possible missed person-sites: 4
- Stale/real recheck flags: 11

## Top 3
1. Rebuild Fri 8 Jan Varanasi around booked train **13042 BSB 21:05 → HWH 11:30**.
2. Close **FOUT 30**: Varanasi nature/waterfall batch is still not Mark-graded.
3. Present the strongest newly surfaced **Vivekananda-in-Varanasi** candidates to Mark: Home of Service + Gopal Lal Villa/Sandhyabas.

# 1. CONTRADICTIONS

1. **HOOG — Varanasi→Kolkata plan vs booked 13042.**  
Files: `governance/CURRENT_TRUTH.md`, current Varanasi quarter-hour plan, `governance/DECISION_LEDGER.jsonl` `DL-0091`.  
Old skeleton/plan still contains Sat-9-Jan / 22324-era logic. Actual booked leg: **13042, BSB Fri 8 Jan 21:05 → HWH Sat 9 Jan 11:30, 1A**. Friday 8 Jan must be recalculated end-to-end.

2. **HOOG — Shyampukur Bati [A] vs [A*].**  
Files: `decisions/INDIA20_KOLKATA_VIVEKANANDA_PRIORITY_AND_CHENNAI_BYCATCH_MARK_DECISION_2026-09-13.md`, `decisions/INDIA20_DAY1_NEW_FRONTIER_LOCK_AND_KOLKATA_GRADE_SUPERSEDE_2026-09-13.md`, Kolkata quarter-hour plan, CURRENT_TRUTH.  
Two explicit 13-Sep decision records say **[A]**; one explicitly says prior A* wording is stale. No later explicit Mark regrade found. Strongest provenance = **A**.

3. **HOOG — Vivekanandar Illam / Ice House [A*] vs OPEN/UNGRADED.**  
13-Sep Mark decision explicitly says **A***, buffer-bycatch/no extra day or night. Later CURRENT_TRUTH/Chennai plan revert to OPEN. No later retraction found. Strongest provenance = **A*** unless Mark deliberately reopens.

4. **MIDDEL — Yogi Ramsuratkumar A+ but still listed “all ungraded”.**  
Tiru plan + CURRENT_TRUTH record Mark 5-Oct: **A+**, Sannidhi Street house + grave/ashram scheduled; Sudama dropped. OPEN DECISIONS item 14 is stale.

5. **MIDDEL — Friday Varanasi still called reserve/buffer although DL-0086 made it a real content day.**  
Valid pre-train-change content: Duniya Foundation → Tailanga/Panchganga → Kedar Ghat. Needs retiming for 13042.

6. **LAAG/MIDDEL — booking-phase status stale.**  
Older CURRENT_TRUTH text says other trains not booked / booking not started. Later CURRENT_TRUTH + `DL-0091`: **all six trains booked and paid**.

# 2. GENUINE OPEN / FORGOTTEN FOLLOW-UPS

7. **HOOG — FOUT 30 Varanasi nature/waterfall layer never closed.**  
Files: human handoff FOUT 30, `DL-0083`, CURRENT_TRUTH, `runs/active/INDIA24_FINAL_EXTRACTION_2026-09-28.md`.  
Second batch includes Rajdari & Devdari, Lakhaniya Dari, Chunadari, Aurwatand, akhara/kushti, Ganges dolphins, hot-air balloon etc. No ledger-backed Mark grades found. INDIA24’s “13 + 8 graded” is not supported for this second batch.

8. **HOOG — Sri Ramakrishna Math, Mylapore, Chennai ungraded.**  
Surfaced in Chennai quarter-hour plan and CURRENT_TRUTH open list. Strong Ramakrishna/Vivekananda institutional relevance. Needs Mark grade.

9. **HOOG/MIDDEL — Kolkata 6 nights is still not a Mark lock.**  
Decision files + CURRENT_TRUTH explicitly describe this as a mechanical calendar consequence after Varanasi cuts, not a final duration decision.

10. **MIDDEL — Tiruvannamalai three genuinely ungraded candidates remain.**  
Sri Seshadri Swamigal Ashram; Ayyankulam tank; Premalaya/Shanthimalai Handicrafts. Ramsuratkumar is no longer open.

11. **MIDDEL — Acharya Bhaban / J.C. Bose identity solved, grade still open.**  
AOAY crescograph scene resolved to Bose residence Acharya Bhaban, not later Bose Institute. No Mark grade found.

12. **MIDDEL — Shyampukur Bati and 50 Amherst Street lack final execution choice.**  
Shyampukur graded but unscheduled. 50 Amherst [A*] left unscheduled; no separate Mark decision found authorizing that omission as final.

13. **MIDDEL — Varanasi A-items without explicit slots.**  
The Ram Bhandar [A] and Winter Malaiyo/Makhan Malai [A] were graded via `DL-0082` but still need actual placement.

14. **MIDDEL — Kolkata sleepbase/access unresolved.**  
No final hotel/sleepbase; YSS Dakshineswar guesthouse response/length issue open; 4 Garpar Road advance access/contact still open.

15. **MIDDEL — Kumaon real-world gates remain.**  
Evam Choskhorling permission/access and local December ridge-walk guide/safety confirmation require real-world contact.

16. **LAAG — Delhi Jama Masjid + Jyotish/astrologer remain ungraded.**

# 3. STRONG POSSIBLE MISSED PERSON-SITES

Strict filter applied: meaningful link to Mark’s core persons, plausible corridor proximity, and no clear named candidate/grade found in checked canon/active layers. Deep-repo false positives were excluded.

17. **HOOG/MIDDEL — Gopal Lal Villa / Sandhyabas, Varanasi.**  
Official Ramakrishna Mission Varanasi material documents Vivekananda’s 1902 stay of roughly three weeks. No clear named candidate/grade found in CURRENT_TRUTH, ledger, current Varanasi plan or all-findings master. Current physical access still needs verification.

18. **HOOG/MIDDEL — Ramakrishna Mission Home of Service, Varanasi.**  
Official institutional history documents Vivekananda’s 1902 visit, his naming of the service association as “Ramakrishna Home of Service”, and his support appeal. Strong living Vivekananda site; not found as named candidate/grade in checked central layers.

19. **MIDDEL — Vivekananda Rest House, Almora.**  
Official Ramakrishna Kutir Almora material marks the 1890 exhaustion/fakir-help episode and memorial, ~1 km from Ramakrishna Kutir. Not found as a distinct Mark-facing candidate/grade.

20. **MIDDEL — Thompson House, Almora.**  
Official Ramakrishna Kutir page says Vivekananda and fellow disciples stayed there, ~0.5 km from Ramakrishna Kutir. Not found as distinct candidate/grade in checked central layers.

Not counted as clean miss: Ramakrishna Advaita Ashrama, Varanasi — strong institutional link to Vivekananda’s instruction, but weaker personal-presence evidence than findings 17–18.

# 4. STALE / REAL RECHECK FLAGS

21. **HOOG — Visa heading stale.**  
CURRENT_TRUTH top heading says category not confirmed, while later text says J/JTV route is resolved and form submitted. Still-open subissues: self-employed documentation acceptance + VFS Amsterdam vs The Hague.

22. **HOOG — Varanasi→Kolkata “not verified / arrival pending” stale.**  
13042 is booked BSB 21:05 → HWH 11:30. Propagate Howrah throughout downstream Kolkata logistics.

23. **MIDDEL — Bodh plan 20887 LIVE_RECHECK stale.**  
`DL-0089/0090/0091`: existence/timing/day verified, chosen over car, booked GAYA 09:55 → BSB 13:00 EC.

24. **MIDDEL — Tiru plan 22604 LIVE_RECHECK stale.**  
Verified/booked Tuesday TNM 12:00 → PER 15:40/15:45, 2A. Does **not** stop at Chennai Central.

25. **LAAG — old 22324 LIVE_RECHECK survives only in explicitly superseded archive text.**

26. **HOOG — Vrindavan Anandamayi Ashram midday access genuinely unresolved.**  
30 Dec depends on ~11:00–14:45 block. Official hours absent; secondary sources conflict. Direct confirmation required. If midday access fails, real replan needed.

27. **MIDDEL — Haidakhan→Kathgodam exact km genuinely open, but allowance robust.**  
Operationally use ~30–45 km / 1.5–2h normal, 2–2.5h protected. Local winter-road confirmation remains more important.

28. **MIDDEL/LAAG — Taj exact sunrise opening genuinely needs later recheck.**  
Agra→Gaya train is booked; only exact Taj opening is date-sensitive.

29. **MIDDEL — Garpar programme/access genuinely open.**  
YSS Dhyana Kendra January programme + 4 Garpar Road advance access/contact.

30. **MIDDEL — Pavalakunru opening time genuinely uncertain.**  
Sources conflict between late-afternoon and recent morning priest access; conservative late-afternoon assumption remains appropriate pending local confirmation.

31. **MIDDEL — PNR/berth assignment genuinely needs later recheck.**  
All six trains are booked. Some FTQ bookings before normal ARP still lack final coach/berth assignment. Never regress this to “not booked”.

# Anti-regression for successor AIs

- Six train legs = booked.
- 13042 replaces 22324.
- Fri 8 Jan Varanasi must be rebuilt.
- Ramsuratkumar = A+ and scheduled.
- Shyampukur strongest provenance = A unless a later explicit Mark decision is produced.
- Vivekanandar Illam has explicit A* provenance.
- FOUT 30 second batch is not ledger-closed.
- Category-3 sites are candidates for Mark, never auto-grade.
- Distinguish access uncertainty from subjective grade/relevance.
