# INDIA8 -> INDIA9 — QUARTER-HOUR ITINERARY / GEO QA DELTA — 2026-08-23

Status: CURRENT LATEST DELTA. Read immediately after `handoffs/INDIA8_TO_INDIA9_FINAL_BOOT_2026-08-23.md` and before doing further itinerary work.

This file preserves the last INDIA8 working session so India9 can continue without asking Mark to reconstruct it.

## 1. NEW EXPLICIT MARK LODGING RULE — SUPERSEDES RISHIKESH ASHRAM SLEEP IDEA

Mark explicitly decided:
- only **two ashram stays** are wanted on this trip:
  1. **Haidakhan Ashram**;
  2. **Sri Ramanasramam / Ramana Maharshi ashram** in Tiruvannamalai.
- all other nights should use **non-ashram accommodation** (hotel/guesthouse).

Operational consequences:
- Haidakhan ashram sleep remains desired.
- Sri Ramanasramam stay remains desired; if actual ashram lodging is unavailable, use the existing Ramana Nagar / Chengam Road fallback zone, but the preference is the ashram itself.
- **Rishikesh must NOT use Parmarth Niketan as the sleep base.** Parmarth may remain a New-Year / Ganga / retreat experience only. Select a hotel on foot or a short tuk-tuk/taxi ride from the relevant Rishikesh/Parmarth zone.
- Existing non-ashram locks remain: Joshi Guest House / Kukuchina; Hotel Evelyn / Nainital; Sahi River View Guesthouse / Varanasi; later specific hotels still to be chosen in Vrindavan, Bodh Gaya, Agra, Rishikesh and Delhi where not locked.

## 2. NEW OUTPUT MARK WANTS NEXT — NOT ANOTHER ROUGH ROUTE

Mark accepts the current rough V2 as a useful starting plan. The next required product is a **full day-by-day operational itinerary with quarter-hour timing** so feasibility errors become visible.

For EVERY calendar day:
- show clock times in ~15-minute increments where useful;
- show wake/start early and aim for early bed;
- show every transfer and **travel time between consecutive stops**;
- show realistic station/airport/parking/walking/entry buffers where material;
- reserve **1 hour every evening for dinner**;
- **do NOT schedule a separate lunch block** — lunch/snacks happen en route and should not consume a formal itinerary slot unless a specific future logistics reason makes it unavoidable;
- use actual sleep base / hotel door as origin and destination, never an arbitrary city-centre point when a base is already known;
- treat overnight trains as sleep/travel nights, not automatically as a lost sightseeing day;
- use the schedule diagnostically: if a day only works under perfect conditions, label it overloaded rather than making the arithmetic fit.

## 3. LOCATION DESCRIPTIONS MUST BE LONGER FOR THIS REVIEW ROUND

For every A and B location in the day plan, give enough plain-language context for Mark to judge whether the grade still feels right:
- what the place physically is;
- why it matters to the relevant person/story/tradition;
- what Mark will actually see/do/experience there;
- whether it is a room, house, ghat, temple, cave, memorial, working station, landscape, etc.;
- if relevant, what specific event/person link occurred there;
- any material uncertainty in the identity or exact micro-location.

Purpose: Mark wants to be able to see from the itinerary itself whether some A's should become B's or vice versa. INDIA9 must NOT change grades itself; only expose the trade-off clearly.

## 4. HARD GEO REQUIREMENT FOR THE QUARTER-HOUR PLAN

Before a final operational itinerary can be trusted, **every retained-route A and B physical visit point must have a good Google Maps coordinate / verified Google official map location**, unless it is genuinely non-public/non-visitable or only resolvable as a zone.

Rules:
- check GitHub first and reuse existing exact/verified Google pins when valid;
- never promote an old `WORKING_GOOGLE_MAPS_PIN` simply because it looks plausible;
- verify the physical identity against address / official / institutional evidence;
- never guess a coordinate;
- if exact marker closure remains impossible, carry an explicit `ADDRESS_CONFIRMED_MARKER_NOT_CLOSED`, `ZONE_ONLY`, `GEO_CONFLICT`, or `NONPUBLIC_OR_NOT_FOR_VISIT` disposition and make the timing uncertainty visible.

A dedicated QA task has already been created:
`runs/active/INDIA8-RETAINED-ROUTE-AB-GEO-QA-001/TASK.md`
commit: `569aad46e4d53974b0f7ae956f5fb4c253e379e0`

That task requires complete retained-route A/B inventory QA, Google coordinate closure, silent-drop detection, and operational blockers. It must be consumed by India9 when results appear; do not duplicate or ignore it.

## 5. CRITICAL VARANASI FINDING — V2 SHORTHAND IS NOT THE FULL MARK CANON

During the last session INDIA8 re-opened the protected Varanasi decision files and found that the V2 route section only lists a **core shorthand**, not the whole protected Mark selection.

Protected Varanasi final selection from the regional package:
- **32 A**
- **5 B**
- **3 C**

### Varanasi A — 32
`001, 002, 003, 004, 005, 006, 007, 009, 010, 011, 014, 015, 016, 017, 018, 019, 020, 021, 022, 024, 028, 029, 030, 031, 032, 033, 034, 035, 036, 037, 038, 039`

Names:
- 001 Lahiri Mahasaya Samadhi / Satyalok
- 002 Lahiri Mahasaya original home
- 003 Manikarnika Ghat
- 004 Shri Tailanga Swami Math
- 005 Shree Shree Ma Anandamayi Ashram, Bhadaini
- 006 Sarnath sacred complex umbrella
- 007 Shri Kashi Vishwanath Temple
- 009 Dashashwamedh Ghat
- 010 Assi Ghat
- 011 Panchganga Ghat
- 014 Maa Annapurna Temple
- 015 Sankat Mochan Hanuman Temple
- 016 Durga Temple and Durga Kund
- 017 Vishalakshi Gauri Temple
- 018 Sankatha Devi Temple
- 019 Kedareshwar Temple and Kedar Ghat
- 020 Lalita Ghat
- 021 Nepali Temple / Kathwala Temple
- 022 Bindu Madhav Temple
- 024 Kabir Chaura Math
- 028 Bhaskarananda Samadhi / Anand Bagh
- 029 Dhamek Stupa
- 030 Mulagandha Kuti Vihara
- 031 Chaukhandi Stupa
- 032 Sarnath Archaeological Museum
- 033 Deer Park / Isipatana sacred landscape
- 034 Saranganath Temple
- 035 Tulsi Manas Temple
- 036 Tulsi Ghat
- 037 Lolark Kund
- 038 Ratneshwar Mahadev Temple
- 039 Shitala Mata Temple, Dashashwamedh

### Varanasi B — 5
- 008 Yogoda Satsanga Dhyana Mandali, Varanasi
- 012 Harishchandra Ghat
- 013 Kaal Bhairav Temple
- 023 Mrityunjay Mahadev Temple
- 025 Lahartara Kabir birthplace memorial

### Varanasi C — 3
- 026 Ramakrishna Mission Home of Service
- 027 Baba Keenaram Sthal / Krim Kund
- 040 Bharat Mata Temple

HARD implication: when building the 5 full Varanasi local days (6–10 Jan in V2), India9 must either place every current retained A/B or explicitly show the collision/overload. **No silent drops.** If a later explicit Mark decision supersedes one of these grades, apply precedence and document it; otherwise the protected status stands.

## 6. VARANASI GEO BOTTLENECK — FOUND, NOT SOLVED BY FIAT

The regional Varanasi geo audit explicitly states that most candidates had their physical identity confirmed but not an exact Google Maps marker.

Known exact/Google-official coordinate closures in that package included at least:
- 018 Sankatha Devi Temple — exact Google Maps marker `25.3126289, 83.0154469`;
- 019 Kedareshwar Temple/Kedar Ghat — exact Google Maps-linked marker `25.2995855, 83.0060964`;
- 029 Dhamek Stupa — verified Google official map link `25.380889, 83.024276`;
- 031 Chaukhandi Stupa — verified Google official map link `25.37402, 83.023588`;
- 033 Deer Park / Isipatana — verified Google official map link `25.3825, 83.024445`.

The old regional decision summary said **35 of 40 candidates still lacked a confirmed Google Maps marker** at that point. This is exactly why the new retained-route geo-closure task exists.

Special warnings already known:
- 008 YSS Varanasi: old coordinate `25.3045, 82.979369` was explicitly rejected; DO NOT reuse it.
- 023 Mrityunjay Mahadev: independent-source geography differed by roughly 3 km from the old comparison point; requires explicit closure.
- Sahi River View Guesthouse is LOCKED_BY_MARK but its exact Google Maps marker was not yet confirmed in that old package; address is `B1/158 A2, Assi Ghat Rd, Varanasi, Uttar Pradesh 221005`.

## 7. EXISTING VARANASI TRAVEL GROUPING IS USEFUL INPUT, NOT FINAL TIMING

The repository already contains:
`runs/active/VARANASI-GEO-DELIVERY-REPAIR-001/GOUD/REGIONAL/TRAVEL/DAGROUTES.md`

Useful grouping recovered:
- Bhadaini/Assi/Durgakund walk/short-rickshaw cluster;
- Old City / Dashashwamedh / Vishwanath / Manikarnika / Lalita / Panchganga contiguous walk cluster;
- Kriya/Bengali Tola + Kabir + north-old-city taxi cluster;
- Sarnath as a separate trip (roughly 30–45 min each way depending traffic).

The old route module proposed 4 days for the full Varanasi core. V2 now gives five complete local days, but the actual protected 32A+5B inventory is larger than V2's shorthand. Quarter-hour planning is therefore required before claiming that five days are comfortable.

## 8. BODH GAYA — OLDER PROTECTED DECISIONS RE-FOUND; DO NOT SILENTLY OVERRIDE LATER CANON

The last session also re-opened old locked Bodh Gaya files:
- 2026-08-05: 046 Mahabodhi Temple Complex = A; 047 Sujata Stupa = A; 048 Dungeshwari Cave Temples = A; 049 Great Buddha Statue = A.
- 2026-08-08: B grades included 050 Archaeological Museum of Bodh Gaya, 052 Tergar Monastery, 070 Mangala Gauri Temple, 073 Jagannath Temple beside Mahabodhi; several others were locked C.

However, the current final handoff contains newer shorthand in which at least Great Buddha / Dungeshwari appear differently graded. Therefore India9 MUST apply the established precedence rule and find the newest explicit Mark decision before planning them. The finding to preserve is: **there is a real cross-generation grade discrepancy; do not choose one version by convenience.**

## 9. TIRUVANNAMALAI / ARUNACHALA — CURRENT LODGING INTENT

The A-anchor itself remains locked by Mark. For this latest planning round, Ramana Maharshi is one of the two people for whom Mark explicitly wants the ashram-stay experience. Therefore:
- treat Sri Ramanasramam as intended ashram sleep if access/application permits;
- build the quarter-hour local days around the actual ashram gate/base when possible;
- if unavailable, use the existing Ramana Nagar / Chengam Road hotel zone as fallback, not another unrelated ashram.

## 10. LONELY PLANET / TRAVELER-GEM LAYER — EXPAND TO EVERY RETAINED CLUSTER

Mark explicitly requested that the Lonely Planet / experienced-traveler micro-gem layer be worked out for **ALL retained cluster locations**, not only Kumaon or the already-swept north corridor.

For every retained cluster in V2 — Delhi arrival/final buffer, Haidakhan/Kumaon, Kukuchina/Dunagiri/Dwarahat, Nainital/Kainchi, Rishikesh/Haridwar/Kankhal, Agra, Vrindavan/Braj/Mathura, Prayagraj, Varanasi/Sarnath, Bodh Gaya/Gaya, Tiruvannamalai/Arunachala — India9 must have a compact traveler-gem layer before final day cards.

Rules:
- do not make generic top-10 tourist lists;
- look for old bakeries/pastry shops/sweet shops, cult addresses, short distinctive walks, viewpoints, unusual stations/bridges/streets/markets, local craft, architecture/ruins, specific local products/rituals/experiences, and exceptional nature/archaeology;
- prefer items that ride almost free on the actual day geometry;
- major detours remain explicit and do not silently displace A's;
- preserve already identified examples such as Sakley's, Bal Mithai/Kheem Singh, Ram Bhandar, winter malaiyo, Gulabi Meenakari, Sri Ram Tilkut Bhandar, etc., where the relevant cluster remains in route.

## 11. CURRENT V2 CALENDAR REMAINS THE STARTING GRID

Do not invent a new route before testing this grid:
- 19 Dec overnight train Delhi -> Kathgodam
- 20–22 Dec Haidakhan, 3 nights
- 23–25 Dec Kukuchina/Joshi Guest House, 3 nights
- 26–28 Dec Nainital/Hotel Evelyn, 3 nights
- 29–31 Dec Rishikesh, 3 nights — **hotel, not ashram sleep**
- 1 Jan Agra, 1 night
- 2–3 Jan Vrindavan, 2 hotel nights
- 4 Jan overnight train Mathura -> Prayagraj
- 5–10 Jan Varanasi, 6 nights
- 11–13 Jan Bodh Gaya/Gaya, 3 hotel nights
- 14–18 Jan Tiruvannamalai/Arunachala, 5 nights — **Sri Ramanasramam desired ashram stay**
- 19–20 Jan Delhi, 2 hotel/buffer nights
- return flight 21 Jan 2027 12:20 DEL.

The point of the quarter-hour pass is to discover which A/B choices, night counts, transfers or route assumptions fail in practice. Do not pre-emptively hide overload by deleting protected sites.

## 12. CURRENT EXECUTION / HANDOFF STATE

Already executed by INDIA8 before handoff:
- protected Varanasi 32A/5B/3C canon re-opened and recovered;
- Varanasi old geo limitations re-opened and recognized as a real planning blocker;
- old Varanasi day-grouping file re-opened;
- old Bodh Gaya decision files re-opened and discrepancy against newer shorthand identified;
- dedicated retained-route A/B geo + silent-drop QA task created at commit `569aad46e4d53974b0f7ae956f5fb4c253e379e0`.

India9 should continue from this exact state. Do not ask Mark to repeat these instructions.