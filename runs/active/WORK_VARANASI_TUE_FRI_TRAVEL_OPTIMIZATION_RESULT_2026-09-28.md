# WORK_RESULT — Varanasi Tuesday/Friday travel-time optimization

Status: **COMPLETE**  
Input branch/head: `agent/india8-cluster-casting` @ `d5503bba4f12690b47cf68104898dc482549932b`  
Work branch: `worker/varanasi-tue-fri-travel-optimization-work`  
Scope: routing/timing analysis only; no grade, Wednesday, PDF or broader-calendar change.

## Independence statement

This pass was worked independently from CCI's chat-side proposal for this exact Tuesday/Friday question. I read the task, the explicitly required current-plan sections and governing files, but no `CCI_RESULT` or CCI chat proposal for this specific optimization before reaching the result below.

## Verdict

1. **Recommended Tuesday:** hotel/Assi → New Bhrigu Karyalaya (car) → Tulsi Ghat (car) → Shree Shree Ma Anandamayi Ashram (walk) → Dashashwamedh Ghat (pre-booked boat) → hotel. Given Mark's fixed order, this is the minimum-travel topology. Walking from Bhadaini to Dashashwamedh loses 20–30 minutes and adds fatigue; a car cannot follow the riverfront old-city geometry.
2. **Anandamayi conclusion:** three hours is not an arbitrary CCI compromise. Once a normal 20-minute food/toilet break, the fixed Tulsi stop, boat access and at least about one hour of pre-Aarti presence are counted, **3 hours is the robust protected dwell**. An early-running day can yield about 10–15 extra minutes, but the ashram cannot honestly remain open-ended on the same day as a fixed evening Aarti.
3. **Recommended Friday:** hotel → Duniya school visit → road to Maidagin/Bulanala + walk to Shri Tailanga Swami Math/Panchganga → walk south to Kedareshwar Temple/Kedar Ghat → hotel. This keeps the northern, time-sensitive Tailanga stop before Kedar and ends back toward the hotel.
4. **Day actually lightened:** Thursday. Removing the Panchganga/Tailanga northern extension lets the dawn boat go directly Assi→Manikarnika. Manikarnika can start about **2u40–2u55 earlier** (about 07:20–07:35 instead of 10:15), without shortening its protected 3+ hour/open-ended dwell. Kedar also stays off Tuesday, preserving the already-created roughly 30-minute marginal relief there.
5. **Does this beat CCI's current draft?** Not by a large geometric win: the best independent solve converges on the same core topology. It improves it by fixing the exact Friday order (Tailanga/Panchganga first, Kedar second), avoiding a second full boat-corridor duplication, exposing the real ashram cutoff, and showing the correct skip-time arithmetic. No genuinely faster arrangement exists under the locks.
6. **Honest Friday limit:** content reaches roughly 13:45–14:05 and hotel return roughly 14:05–14:35 **only if Mark accepts the 2.1–2.2 km / 35–45 min Panchganga→Kedar ghat walk**. Without that walk, without an independently confirmed point-to-point boat, and without ruled-out filler, there is no honest way to reach the “content until ~14:00” target.

## Data basis and calculation rules

- The travel ranges in the WORK task at `d5503bb` are treated as ground truth, exactly as instructed.
- `TOTALE TIJD VOOR DEZE LOCATIE` is predecessor→location travel + dwell + location→successor travel. Adjacent-card totals must not be summed because shared legs appear twice.
- `TIJD VRIJGEMAAKT ALS DEZE GESKIPT WORDT` subtracts the recalculated direct predecessor→successor leg.
- Where the task does not supply a direct skip comparator, the calculation is explicitly labelled as a corridor inference and remains `LIVE_RECHECK`.
- Exact January 2027 boat availability, Aarti start, Tailanga access hours and the private Duniya address remain `LIVE_RECHECK`. The route does not depend on an unverified afternoon reopening of Tailanga; it is scheduled before 13:00.

---

## DI 5 JAN — recommended full day

**VERTREK HOTEL: 08:15.** This is the necessary fixed-appointment exception to the normal 08:30 start. The 20–35 minute car leg plus early-arrival/check-in slack protects the 09:00 appointment.

| Time | Block | Real transfer data / note |
|---|---|---|
| 08:15–09:00 | Sahi River View/Assi → New Bhrigu Karyalaya | car/auto-rickshaw; ~3.2–4.0 km; 20–35 min, plus 10–25 min arrival/check-in buffer |
| 09:00–12:00 | New Bhrigu Karyalaya / Bhadury Sadan [A+] | protected 3-hour appointment window |
| 12:00–12:20 | Bhrigu → Tulsi Ghat | car; ~3.2–3.5 km; 15–20 min |
| 12:20–12:40 | Simple packed lunch/toilet break | no added attraction and no detour |
| 12:40–13:05 | Tulsi Ghat [A] | 25 min conscious place visit |
| 13:05–13:10 | Tulsi Ghat → Anandamayi Ashram | walk; ~0.2 km; 4–6 min |
| 13:10–16:10 | Shree Shree Ma Anandamayi Ashram, Bhadaini [A+] | protected 3 hours; if every earlier leg runs at its minimum, use at most 10–15 extra minutes |
| 16:10–16:20 | Walk/board pre-arranged boat | operational access buffer |
| 16:20–16:45 | Bhadaini → Dashashwamedh Ghat | boat; river leg ~2.2–2.4 km; 20–25 min |
| 16:45–19:00 | Dashashwamedh Ghat + Ganga Aarti [A+] | ~75 min place-presence before an indicative ~18:00 Aarti, then ceremony; exact January time `LIVE_RECHECK` |
| 19:00–20:00 | Dashashwamedh → hotel/Assi | crowd egress + walk-to-road + car; ~3.1 km river-axis / roughly 5–6 km road class; 45–60 min whole-human evening allowance |

Baseline hotel-to-hotel: **08:15–19:45/20:00 = about 11u30–11u45**. This is a heavy fixed-content day, not a light day.

### New Bhrigu Karyalaya / Bhadury Sadan — personal Bhrigu astrology reading in the living Bhadury family practice (Ramapura-Luxa) [A+]

**TIJD: 08:15–12:20, including approach and onward transfer.**

**WAT IS DIT IN GEWOON NEDERLANDS?** A one-to-one Bhrigu astrology reading in the family home/practice where the tradition and manuscript collection are still actively used.  
**WAAROM WIL JIJ, MARK, HIERHEEN?** This is one of Mark's own core motivations in Varanasi, connected to his interest in the Bhrigu tradition and the reported Bhadury–Lahiri Mahasaya link.  
**WIE WAS HIER / WAT GEBEURDE HIER?** The practice descends through Sudhir Ranjan Bhadury, Brahma Gopal Bhadury and the current generation; family sources report that Sudhir Ranjan met and studied with Lahiri Mahasaya.  
**WAT MOET JE HIER PRECIES ZOEKEN?** The actual consultation, translation/explanation and—if shown—the family manuscript collection.  
**HOE WIL JE HIER ZIJN?** A protected appointment, not a quick visit; three hours includes intake, reading, explanation and realistic overrun.  
**UNIEK HERKENNINGSPUNT:** A living private astrology practice rather than a temple or museum.

**TOTALE TIJD VOOR DEZE LOCATIE: 4u00–4u05.**  
**TIJD VRIJGEMAAKT ALS DEZE GESKIPT WORDT: 3u50–3u55, calculation only; it is fixed and not a skip candidate.**  
**BEREKENING:** hotel→Bhrigu scheduled approach 45 min (20–35 min ride + variable arrival buffer) + 3u dwell + Bhrigu→Tulsi 15–20 min − hotel→Tulsi direct ~10 min walk.

### Tulsi Ghat — Tulsidas' living/working/death ghat with the still-active akhada (south Varanasi) [A]

**TIJD: 12:40–13:10, including onward walk.**

**WAT IS DIT IN GEWOON NEDERLANDS?** The river ghat associated with Tulsidas' final years and death, with a centuries-old wrestling school still active on site.  
**WAAROM WIL JIJ, MARK, HIERHEEN?** Mark explicitly added it as a real stop, not merely a name passed during another walk.  
**WIE WAS HIER / WAT GEBEURDE HIER?** Tulsidas is traditionally associated with living, writing and dying here; the akhada continues the site's living cultural layer.  
**WAT MOET JE HIER PRECIES ZOEKEN?** The ghat, the Tulsidas-associated shrine/house layer and the akhada area.  
**HOE WIL JE HIER ZIJN?** A conscious 25-minute recognition stop, long enough to see the place without taking time from the protected ashram.  
**UNIEK HERKENNINGSPUNT:** The Tulsidas ghat and active earthen wrestling-school setting.

**TOTALE TIJD VOOR DEZE LOCATIE: 44–51 min.**  
**TIJD VRIJGEMAAKT ALS DEZE GESKIPT WORDT: about 19–36 min; corridor inference, not a reason to skip a fixed stop.**  
**BEREKENING:** Bhrigu→Tulsi 15–20 min + Tulsi 25 min + Tulsi→Ashram 4–6 min − Bhrigu→Ashram direct inferred ~15–25 min. The direct comparator needs local-driver confirmation because the task verifies Bhrigu→Tulsi, not the ashram drop point.

### Shree Shree Ma Anandamayi Ashram — Anandamayi Ma's own living worship complex (Bhadaini) [A+]

**TIJD: 13:10–16:20 scheduled, including boat-access buffer after the 3-hour dwell.**

**WAT IS DIT IN GEWOON NEDERLANDS?** Anandamayi Ma's active Varanasi ashram, with temple/yajna spaces and the Kanyapith layer; this is a worship place, not a photo stop.  
**WAAROM WIL JIJ, MARK, HIERHEEN?** Anandamayi Ma is one of Mark's Top-X people and this is her own Varanasi institution.  
**WIE WAS HIER / WAT GEBEURDE HIER?** Anandamayi Ma established the Bhadaini site from 1944 onward; it remains a living ashram. It is not the site of her 1935 AOAY meeting with Yogananda, which occurred in Calcutta.  
**WAT MOET JE HIER PRECIES ZOEKEN?** The Annapurna/Shiva temple, yajna hall, Ananda Jyoti Mandir and living ashram atmosphere.  
**HOE WIL JE HIER ZIJN?** Three protected hours for worship and unhurried presence. This remains spiritually open in quality, but not literally open-ended in clock time because the Aarti is fixed.  
**UNIEK HERKENNINGSPUNT:** A living Anandamayi Ma ashram immediately north of Tulsi Ghat.

**TOTALE TIJD VOOR DEZE LOCATIE: 3u34–3u41 at the 3-hour baseline; every extra ashram minute adds one minute.**  
**TIJD VRIJGEMAAKT ALS DEZE GESKIPT WORDT: about 2u59–3u11, calculation only; it is protected and not a skip candidate.**  
**BEREKENING:** Tulsi→Ashram 4–6 min + Ashram 3u + access/boarding 10 min + boat 20–25 min − a direct Tulsi→Dashashwamedh boat of approximately the same 30–35 min whole-human class. The direct comparator is a same-corridor inference and remains `LIVE_RECHECK`.

### Dashashwamedh Ghat + Ganga Aarti — AOAY Babaji/Mataji/Lahiri/Ram Gopal place and evening fire ceremony (central ghats) [A+]

**TIJD: 16:20–19:45/20:00, including arrival boat and hotel return.**

**WAT IS DIT IN GEWOON NEDERLANDS?** Varanasi's main ceremonial ghat and the site of the large synchronized evening fire ritual.  
**WAAROM WIL JIJ, MARK, HIERHEEN?** In AOAY chapter 33, this is the named ghat of the Babaji–Mataji–Lahiri Mahasaya scene witnessed by Ram Gopal; the Aarti is an additional experience, not the sole reason.  
**WIE WAS HIER / WAT GEBEURDE HIER?** Lahiri sent Ram Gopal here; Mataji appeared from the hidden-cave setting and called Babaji and Lahiri, after which Babaji made his physical-body promise.  
**WAT MOET JE HIER PRECIES ZOEKEN?** The ghat itself and its older upper steps; do not claim any marketed modern cave is the exact AOAY cave without separate proof.  
**HOE WIL JE HIER ZIJN?** Arrive before peak crowding, spend about 60–75 minutes in conscious place-presence, then experience the Aarti.  
**UNIEK HERKENNINGSPUNT:** The largest lamp ceremony on the riverfront, layered onto one of the itinerary's strongest AOAY place-links.

**TOTALE TIJD VOOR DEZE LOCATIE: 3u30–3u50.**  
**TIJD VRIJGEMAAKT ALS DEZE GESKIPT WORDT: about 3u15–3u40, calculation only; it is fixed and protected.**  
**BEREKENING:** Ashram→Dashashwamedh access + boat 30–35 min + Dashashwamedh/Aarti 2u15 + return 45–60 min − Ashram→hotel direct 10–15 min.

### Why the ashram cannot remain literally open-ended on Tuesday

The latest robust ashram exit is approximately **16:15**:

- 10 min to reach/board a pre-arranged boat;
- 20–25 min on the river;
- arrival about 16:45–16:50;
- roughly 70 minutes before an indicative 18:00 Aarti.

Starting the ashram around 13:10 therefore yields about **3u05**. Best-case earlier running can raise that to roughly **3u15–3u20**, but not to a genuine open end. A literal open end and the fixed evening ceremony are mutually incompatible on the same day. The honest plan is a protected three-hour minimum plus a small on-the-day margin, never a promise of unlimited dwell.

---

## VR 8 JAN — recommended full day

**VERTREK HOTEL: 08:30.** This preserves Mark's standard start and keeps the day substantial but manageable before the ~00:10 hotel departure for the overnight train.

| Time | Block | Real transfer data / note |
|---|---|---|
| 08:30–08:45 | Hotel/Assi → Stichting Duniya, Nagwa | car/auto-rickshaw; exact distance cannot be stated because the school address is intentionally non-public; current south-zone allowance ~15 min |
| 08:45–10:45 | Stichting Duniya school visit | 2-hour personally connected visit already on Friday |
| 10:45–11:25/11:35 | Nagwa → Maidagin/Bulanala vehicle edge → Panchganga | car ~25–35 min + final old-city walk ~10–15 min; use 40–50 min total because the exact school pin is private |
| 11:25/11:35–12:10/12:20 | Shri Tailanga Swami Math [A] | 45 min; deliberately first because the strongest current timetable closes at 13:00 |
| 12:10/12:20–12:40/12:50 | Panchganga Ghat [A] | 30 min; same microcluster, no separate transfer |
| 12:40/12:50–13:15/13:35 | Panchganga → Kedar Ghat | walk south; ~2.1–2.2 km; 35–45 min; no direct car route |
| 13:15/13:35–13:45/14:05 | Kedareshwar Temple + Kedar Ghat [A] | 30 min |
| 13:45/14:05–14:05/14:35 | Kedar → hotel/Assi | ghat walk or walk-to-road + auto; ~1.4–1.6 km walking / ~2–2.5 km mixed route; 20–30 min |

Content ends **13:45–14:05**; hotel return **14:05–14:35**. Lunch follows at/near the hotel. Even a 14:35 return leaves roughly **9u35** before the 00:10 station departure, so the train-night buffer remains generous.

### Stichting Duniya — small education project in Nagwa with Mark's personal connection (south Varanasi) [personal fixed content]

**TIJD: 08:30–11:25/11:35, including approach and onward transfer.**

**WAT IS DIT IN GEWOON NEDERLANDS?** A small school and vocational-training project serving children and families in Nagwa.  
**WAAROM WIL JIJ, MARK, HIERHEEN?** Mark has a direct personal connection through an acquaintance; this is not generic sightseeing.  
**WIE WAS HIER / WAT GEBEURDE HIER?** A local team runs the education and training work supported by the Dutch foundation.  
**WAT MOET JE HIER PRECIES ZOEKEN?** The agreed visit itself; exact address and access must be arranged privately rather than published.  
**HOE WIL JE HIER ZIJN?** A real two-hour visit, not a drive-by.  
**UNIEK HERKENNINGSPUNT:** A living community project in the same southern zone as the hotel.

**TOTALE TIJD VOOR DEZE LOCATIE: 2u55–3u05.**  
**TIJD VRIJGEMAAKT ALS DEZE GESKIPT WORDT: about 2u15, calculation only; it is already confirmed personal content.**  
**BEREKENING:** hotel→Duniya 15 min + Duniya 2u + Duniya→Tailanga/Panchganga 40–50 min − hotel→Tailanga/Panchganga direct 40–50 min.

### Shri Tailanga Swami Math — samadhi shrine linking Trailanga Swami with Lahiri Mahasaya and Ramakrishna (Panchganga) [A]

**TIJD: 10:45–12:10/12:20, including northern access.**

**WAT IS DIT IN GEWOON NEDERLANDS?** Trailanga Swami's samadhi/meditation shrine in the Panchganga microcluster.  
**WAAROM WIL JIJ, MARK, HIERHEEN?** It has the rare double lineage relevance of Lahiri Mahasaya and Sri Ramakrishna.  
**WIE WAS HIER / WAT GEBEURDE HIER?** AOAY identifies Trailanga as Lahiri Mahasaya's famous friend; Ramakrishna visited and honoured him during the 1868 Kashi pilgrimage.  
**WAT MOET JE HIER PRECIES ZOEKEN?** The underground meditation/samadhi room, the Shiva lingam and the Kali image associated with Trailanga.  
**HOE WIL JE HIER ZIJN?** A focused 45-minute visit before the currently supported 13:00 closing boundary.  
**UNIEK HERKENNINGSPUNT:** The Trailanga samadhi complex directly at Panchganga.

**TOTALE TIJD VOOR DEZE LOCATIE: 1u25–1u40.**  
**TIJD VRIJGEMAAKT ALS DEZE GESKIPT WORDT: about 45 min.**  
**BEREKENING:** Duniya→Tailanga 40–50 min + Tailanga 45 min + internal walk to Panchganga 0–5 min − Duniya→Panchganga direct 40–50 min. Same-microcluster geometry means skipping the shrine saves almost only its dwell.

### Panchganga Ghat — five-river confluence tradition and Trailanga's riverfront setting (north Varanasi) [A]

**TIJD: 12:10/12:20–13:15/13:35, including the onward ghat walk.**

**WAT IS DIT IN GEWOON NEDERLANDS?** A historic ghat traditionally marking the confluence of five sacred rivers, with only the Ganges physically visible.  
**WAAROM WIL JIJ, MARK, HIERHEEN?** It is the riverfront context of the Tailanga visit and also carries its own Ramananda/Kabir and Guru Nanak layers.  
**WIE WAS HIER / WAT GEBEURDE HIER?** Trailanga is associated with sitting at these steps; Ramananda taught in this sacred geography and Guru Nanak is traditionally linked to the ghat.  
**WAT MOET JE HIER PRECIES ZOEKEN?** The steps beside the math and the traditional confluence point.  
**HOE WIL JE HIER ZIJN?** Thirty minutes of place-presence before beginning the southbound walk.  
**UNIEK HERKENNINGSPUNT:** The far-northern five-river ghat, immediately beside the Trailanga complex.

**TOTALE TIJD VOOR DEZE LOCATIE: 1u05–1u20.**  
**TIJD VRIJGEMAAKT ALS DEZE GESKIPT WORDT: about 30 min.**  
**BEREKENING:** Tailanga→Panchganga 0–5 min + Panchganga 30 min + Panchganga→Kedar 35–45 min − Tailanga→Kedar direct 35–45 min. It lies on the only practical exit line toward Kedar.

### Kedareshwar Temple + Kedar Ghat — red-and-white Shiva temple and Ramakrishna pilgrimage base (mid-south ghats) [A]

**TIJD: 12:40/12:50–14:05/14:35, including approach and hotel return.**

**WAT IS DIT IN GEWOON NEDERLANDS?** A visually distinctive red-and-white Shiva temple directly on its own ghat.  
**WAAROM WIL JIJ, MARK, HIERHEEN?** It has a direct Sri Ramakrishna link rather than being generic temple fill.  
**WIE WAS HIER / WAT GEBEURDE HIER?** Ramakrishna's 1868 Kashi party used houses near Kedar Ghat; the tradition records ecstatic/samadhi experience at Kedareshwar during that stay.  
**WAT MOET JE HIER PRECIES ZOEKEN?** The striped facade, the natural linga and the ghat setting that anchored the pilgrimage stay.  
**HOE WIL JE HIER ZIJN?** A conscious 30-minute visit at the end of the southbound walk.  
**UNIEK HERKENNINGSPUNT:** The red-and-white striped riverfront temple.

**TOTALE TIJD VOOR DEZE LOCATIE: 1u25–1u45.**  
**TIJD VRIJGEMAAKT ALS DEZE GESKIPT WORDT: about 35–65 min.**  
**BEREKENING:** Panchganga→Kedar 35–45 min + Kedar 30 min + Kedar→hotel 20–30 min − Panchganga→hotel direct 40–50 min.

---

## Thursday before/after and exact relief

No Thursday location loses dwell; only the northern detour moves.

| Milestone | Full northern Thursday | Recommended shortened Thursday | Difference |
|---|---:|---:|---:|
| Leave hotel | 06:15 | 06:15 | none |
| Boat | Assi→Panchganga, 90 min | Assi→near Manikarnika, 35–50 min | 40–55 min saved |
| Land/access after boat | ~15 min | near-zero separate northern access | ~15 min saved |
| Tailanga + Panchganga dwell | 45 + 30 min | moved to Friday | 75 min released |
| Walk to Ratneshwar/Manikarnika | ~30 min | direct landing/short approach | ~30 min saved |
| Ratneshwar Mahadev [A+] | 15 min | same 15 min | unchanged |
| Manikarnika Ghat [A+] starts | 10:15 | about 07:20–07:35 | **2u40–2u55 earlier** |
| Manikarnika protected dwell | 3+ hours/open end | 3+ hours/open end | unchanged |

This is genuine relief: Thursday's core sacred block gets a much earlier start and a correspondingly earlier possible hotel return. The improvement is larger than the 75 minutes of moved dwell because the direct boat also removes the extra northern sailing, landing and southbound backtrack.

## Variants rejected

### Friday Kedar first, Panchganga second

Nominal movement is similar, but it is worse operationally: the 35–45 minute northbound walk pushes the 45-minute Tailanga visit toward or beyond the currently supported 13:00 closing time, and the final Panchganga→hotel return is 40–50 minutes. North-first is safer and naturally ends toward the hotel.

### Friday full boat to Panchganga

It is nominally about 10 minutes faster than road+old-city walk, but it repeats most of Thursday's dawn river corridor and makes Friday depend on another boat. The land approach is the better base plan. A boat is a same-day fallback only if locally confirmed and materially easier because of fatigue or access conditions.

### Keep Tailanga/Panchganga on Thursday; Friday only Duniya + Kedar

This is calmer but fails Mark's target: fixed content ends around 11:45 and hotel return around 12:15. It leaves Friday visibly underfilled while Thursday remains 2u40–2u55 heavier before Manikarnika.

### Use more Tuesday content on Friday

Not available. Bhrigu→Tulsi→Anandamayi→Dashashwamedh is locked in that exact Tuesday order. Moving any of it would violate the task rather than optimize it.

### Fill Friday without the Panchganga→Kedar walk

No honest in-scope solution was found. The ruled-out A* layer and excluded temples cannot be used; a car cannot connect the two ghat points directly; and a point-to-point boat time has not been independently verified for this exact leg. Therefore the 35–45 minute walk is the disclosed cost of hitting the ~14:00 target.

## Booking/live-recheck list

1. Confirm Bhrigu's exact 09:00 appointment, language/translation needs and three-hour envelope.
2. Pre-arrange the Tuesday Bhadaini→Dashashwamedh boat with an exact ashram-side pickup point and a 16:20 target departure.
3. Recheck the 5 Jan 2027 Aarti start; protect at least 60 minutes of place-presence before it.
4. Confirm privately the Duniya address/appointment and recalculate the first Friday road leg without publishing the children's location.
5. Confirm Tailanga opening hours directly; base plan assumes the restrictive currently supported 05:30–13:00 window and does not rely on an afternoon reopening.
6. Ask a local driver/guide whether the Panchganga→Kedar 35–45 minute ghat walk is unobstructed and humane that week; if not, verify a pre-arranged point-to-point boat before changing the base plan.
7. Retain the ~00:10 Friday-night hotel departure for Varanasi Junction unless the railway schedule changes.

## Evidence used

- `runs/active/VARANASI_TUE_FRI_TRAVEL_OPTIMIZATION_WORK_TASK_2026-09-28.md` — fixed points and the 2026-09-28 ground-truth travel ranges.
- `governance/CURRENT_TRUTH.md` — trip/hotel/train frame, with the newer task and DL-0084/DL-0085 controlling where they supersede its stale Friday wording.
- `runs/active/CCI_VARANASI_QUARTERHOUR_PLAN_WITH_LINEAGE_LINKS_2026-09-26.md` — allowed current-plan Tuesday/Thursday/Friday place meaning, dwell and current clock context.
- `governance/MARK_FACING_PLACE_CARD_TRAVEL_VALUE_RULE_2026-09-13.md` and `governance/MARK_FACING_LOCATION_CARD_TEMPLATE.md` — mandatory card and net-skip accounting.
- `governance/DECISION_LEDGER.jsonl`, DL-0080 through DL-0085 — latest Varanasi decision history.
- Tailanga public timetable underlying the current repo reconciliation: `https://yappe.in/uttar-pradesh/varanasi/shri-trilinga-swami-math/415850` (05:30–13:00, last-updated claim 24 Jan 2024); direct local confirmation still required.

## Final recommendation to Mark/CCI

Adopt the Tuesday and Friday clocks above. Do not claim Tuesday's ashram is open-ended: call it **protected 3 hours, with at most 10–15 minutes on-the-day extension before the latest safe boat departure**. Move the Trailanga/Panchganga cluster from Thursday to Friday, visit it before Kedar, and disclose the long ghat walk rather than hiding it. This is the best travel-time combination available under the fixed content; the absence of a dramatic route improvement is a genuine geographic conclusion, not a failure to optimize.
