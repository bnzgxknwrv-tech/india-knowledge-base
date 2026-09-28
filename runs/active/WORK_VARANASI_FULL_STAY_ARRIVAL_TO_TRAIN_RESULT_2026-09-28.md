# WORK_RESULT — Varanasi complete planning, arrival through train departure

Status: **COMPLETE — END-TO-END REPLAN**  
Input head: `d5503bba4f12690b47cf68104898dc482549932b`  
Scope: Varanasi arrival Monday 4 January 2027 through departure train Saturday 9 January 2027.  
Supersedes for planning purposes: the bounded Tuesday/Friday-only result on this branch.  
Unchanged: all grades, the Sarnath cut, excluded temples, hotel base, five-night structure and Kolkata train choice.

## Direct answer

The currently assembled Varanasi plan was **not yet one coherent arrival-to-train schedule**. It combined several successive edits that individually made sense but contradicted each other when read as a whole. The main defects were:

1. Assi Ghat [A+] was only implicit/optional on arrival day after its former Friday block disappeared.
2. Tuesday's markdown still contained the old 06:15 dawn sequence, while the newest fixed Tuesday begins with the 09:00 Bhrigu appointment and later returns to Tulsi.
3. Wednesday said Lahiri Mahasaya's house had a one-hour baseline, but its clock gave only 30 minutes.
4. Moving Vishwanath/Annapurna to Friday solved Friday locally but broke the whole-week balance: it emptied Wednesday and overloaded the train-departure day.
5. Thursday's old full-Panchganga route and the newer direct-Manikarnika route both remained in the project at once.
6. Friday still carried stale Dashashwamedh/Aarti wording even though the newest lock puts that Aarti on Tuesday.
7. A 00:10 hotel departure plus a stated 16–40 minute drive cannot guarantee the claimed 45–50 minute station buffer before a 01:30 train.

The recommended complete plan below resolves all seven.

## Final end-to-end structure

| Date | Hotel departure / arrival | Core content | Character |
|---|---|---|---|
| **Mon 4 Jan** | BSB 13:00 → hotel ~14:00 | check-in/recovery + dedicated Assi Ghat [A+] sunset presence | light arrival day |
| **Tue 5 Jan** | hotel 08:15 → return ~19:45–20:00 | Bhrigu [A+] → Tulsi [A] → Anandamayi [A+] → boat → Dashashwamedh/Aarti [A+] | longest fixed day |
| **Wed 6 Jan** | hotel 08:45 → return ~16:30–16:45 | Lahiri house [A+] → Satyalok [A] → old-city walk/paan [A] → Vishwanath [A] → Annapurna [A] | coherent old-city day |
| **Thu 7 Jan** | hotel 06:15 → baseline return ~13:30, later okay | full dawn-boat experience [A+] direct to Manikarnika zone → Ratneshwar [A+] → Manikarnika [A+] open end | early and intense, but not overstuffed |
| **Fri 8 Jan** | hotel 08:30 → return ~14:05–14:35 | Duniya → Tailanga/Panchganga [A/A] → long ghat walk → Kedar [A] | full but manageable departure day |
| **Sat 9 Jan** | room 23:50 / car 00:00 | BSB 01:30 train 22324 → KOAA ~13:05 | protected night-train transfer |

## Why this is the global optimum

- Tuesday's four fixed anchors form one south/central progression and have no better alternative order.
- Wednesday already enters Bengali Tola/Chowk. Vishwanath and Annapurna belong on this same old-city line; moving them to Friday adds burden to the least suitable day and leaves Wednesday artificially empty.
- Thursday retains the dawn boat as an experience rather than reducing it to the fastest possible transfer, but lands directly in the Manikarnika zone. Tailanga/Panchganga move to Friday, removing the northbound extension and southbound backtrack.
- Friday goes north once and then walks consistently south toward Kedar and the hotel. Its difficult cost is visible: a 2.1–2.2 km / 35–45 minute ghat walk.
- Monday and Friday protect recovery around the heaviest days. No A*-filler or excluded temple is used.

---

## MA 4 JAN — arrival and real Assi Ghat coverage

| Time | Plan | Operational meaning |
|---|---|---|
| 13:00 | Train 20887 arrives Varanasi Junction (BSB) | exact 2027 timetable remains `LIVE_RECHECK` |
| 13:00–14:00 | station exit, luggage and car to Sahi River View Guesthouse | one-hour whole-human allowance |
| 14:00–16:30 | check-in, late lunch and recovery | no sightseeing pressure after the Bodh Gaya transfer |
| 16:30–17:30 | **Assi Ghat — Kashi's southern river boundary and the physical A+ hotel-world anchor [A+]** | dedicated presence at the ghat around the ~17:21 sunset; zero transport burden |
| after 17:30 | dinner/rest | protects Tuesday's long day |

This fixes the former semantic gap: sleeping beside Assi is not automatically the same as deliberately visiting it. If train delay removes the sunset hour, the fallback is Friday 16:30–17:30; it is not silently dropped.

Hotel-to-Assi travel is effectively zero. The dedicated hour is therefore almost pure experience time and does not create a new transfer.

---

## DI 5 JAN — fixed Bhrigu/Tulsi/Anandamayi/Dashashwamedh day

| Time | Plan | Transfer / protection |
|---|---|---|
| 08:15–09:00 | hotel/Assi → New Bhrigu Karyalaya / Bhadury Sadan | car, ~3.2–4 km / 20–35 min + early-arrival/check-in buffer |
| 09:00–12:00 | **New Bhrigu Karyalaya — personal Bhrigu reading in the living family practice [A+]** | fixed protected 3-hour envelope |
| 12:00–12:20 | Bhrigu → Tulsi Ghat | car, ~3.2–3.5 km / 15–20 min |
| 12:20–12:40 | packed lunch/toilet | no attraction or detour |
| 12:40–13:05 | **Tulsi Ghat — Tulsidas' living/writing/death ghat and active akhada [A]** | real 25-minute place visit |
| 13:05–13:10 | Tulsi → Anandamayi Ashram | walk, ~0.2 km / 4–6 min |
| 13:10–16:10 | **Shree Shree Ma Anandamayi Ashram — her own living worship complex [A+]** | protected 3-hour minimum |
| 16:10–16:20 | reach and board pre-arranged boat | access buffer |
| 16:20–16:45 | Bhadaini → Dashashwamedh | boat, ~2.2–2.4 km / 20–25 min |
| 16:45–19:00 | **Dashashwamedh Ghat — AOAY Babaji/Mataji/Lahiri/Ram Gopal anchor + Ganga Aarti [A+]** | 60–75 min place-presence before indicative ~18:00 ceremony; exact start `LIVE_RECHECK` |
| 19:00–19:45/20:00 | crowd exit + car to hotel | 45–60 min whole-human evening allowance |

### Tuesday robustness

- Anandamayi gets a real three hours, but cannot truthfully be called clock-open-ended while the same day contains a fixed Aarti.
- At most about 10–15 minutes extra is available if every earlier leg runs well.
- A Bhrigu overrun beyond 15 minutes erodes the pre-Aarti presence; it must not be solved by cutting the ashram below three hours.
- Hotel turnaround before Wednesday: about **12u45** between a 20:00 return and 08:45 departure.

The full card-level `TOTALE TIJD` and `TIJD VRIJGEMAAKT` calculations are preserved in the bounded Tuesday/Friday result on this branch.

---

## WO 6 JAN — complete Lahiri/Old-Kashi day

Vishwanath and Annapurna return to Wednesday because this is the natural old-city route. This is the most important change produced by reviewing the whole stay instead of Friday in isolation.

| Time | Plan | Transfer / protection |
|---|---|---|
| 08:45–09:15 | hotel → Bengali Tola/Madanpura edge | car + final walk, ~30 min |
| 09:15–10:15 | **Lahiri Mahasaya's original family home — actual house of the Kriya householder-guru [A+]** | corrected to the stated one-hour baseline; interior remains closed in January |
| 10:15–10:45 | slow walk to Chaustti Ghat/Satyalok | ~30 min; arrives after the ~10:30 opening |
| 10:45–11:45 | **Lahiri Mahasaya Samadhi/Satyalok — family shrine with Babaji meditation room [A]** | one-hour meditation baseline |
| 11:45–12:45 | **Bengali Tola–Thatheri Bazaar–Chowk — Lahiri's lived old-city world [A]**, with Banarasi paan [A] naturally inside the walk | one continuous route-through block, not two excursions |
| 12:45–13:30 | lunch/rest | whole-human break |
| 13:30–14:00 | walk/security approach | Vishwanath access buffer |
| 14:00–15:30 | **Shri Kashi Vishwanath Temple — Kashi's Golden Temple and living Jyotirlinga core [A]** | queue/security/darshan allowance |
| 15:30–16:00 | **Maa Annapurna Temple — feeding/abundance shrine beside Vishwanath [A]** | same microcluster; 30 min |
| 16:00–16:30/16:45 | exit old city + car to hotel | 30–45 min |

### Wednesday robustness

- The prior clock error is repaired: Lahiri's house now actually receives the promised one hour, not 30 minutes.
- If Lahiri's house and/or Satyalok need another 30 minutes, hotel return becomes about 17:00–17:15; Thursday still has about 13 hours before its 06:15 departure.
- No Dashashwamedh/Aarti remains here; Tuesday owns that fixed block.
- Returning Vishwanath/Annapurna here removes roughly 2–2.5 hours of Friday content and prevents a departure-day old-city overload without creating a new Wednesday road journey.

---

## DO 7 JAN — protected boat/Manikarnika day

The narrow travel-time solve made the dawn boat almost a transfer. The full-stay plan corrects that: the boat remains a real experience but no longer extends to Panchganga.

| Time | Plan | Transfer / protection |
|---|---|---|
| 06:15–06:30 | hotel → Assi boat point | walk/meeting, 15 min |
| 06:30–08:00 | **Ganges dawn rowboat — Assi to the Manikarnika zone [A+]** | direct movement is ~35–50 min; the remaining time is deliberately slow rowing/viewing, preserving the dawn-boat experience without going to Panchganga |
| 08:00–09:00 | **Ratneshwar Mahadev — visibly leaning/submerged Shiva temple beside Manikarnika [A+]** | restores the still-unsuperseded direct Mark duration of one hour rather than the later unexplained 15-minute compression |
| 09:00–12:00+ | **Manikarnika Ghat — Lahiri Mahasaya's cremation place and living cremation ghat [A+]** | protected 3-hour minimum, genuinely open-ended |
| baseline 12:00–12:45 | lunch/quiet decompression and vehicle access | shifts one-for-one if Manikarnika runs long |
| baseline 12:45–13:30 | car to hotel/Assi | protected return allowance |

### Thursday robustness

- Tailanga/Panchganga are removed from this morning and moved intact to Friday.
- The dawn boat remains 90 minutes because it is A+ content, not merely transport. Its destination changes; its experiential value does not disappear.
- Manikarnika is the true open-ended day. Friday's 08:30 start and later afternoon rest absorb a reasonable overrun.
- Compared with the old full northern route, baseline hotel return moves from ~14:45 to ~13:30 while restoring Ratneshwar's full hour. If the currently compressed 15-minute Ratneshwar dwell is later explicitly confirmed by Mark, the released 45 minutes should flow into Manikarnika, not another attraction.

---

## VR 8 JAN — full, manageable departure day

| Time | Plan | Transfer / protection |
|---|---|---|
| 08:30–08:45 | hotel → Stichting Duniya, Nagwa | ~15 min; exact private address to confirm without publishing it |
| 08:45–10:45 | **Stichting Duniya — personally connected education/community visit** | fixed 2-hour visit |
| 10:45–11:25/11:35 | Nagwa → Maidagin/Bulanala edge → Panchganga | car 25–35 min + old-city walk 10–15 min; 40–50 total |
| 11:25/11:35–12:10/12:20 | **Shri Tailanga Swami Math — samadhi shrine linking Trailanga with Lahiri and Ramakrishna [A]** | 45 min, before the currently supported 13:00 closure |
| 12:10/12:20–12:40/12:50 | **Panchganga Ghat — five-river confluence tradition and Trailanga setting [A]** | 30 min, same microcluster |
| 12:40/12:50–13:15/13:35 | Panchganga → Kedar | walk, ~2.1–2.2 km / 35–45 min; no direct car route |
| 13:15/13:35–13:45/14:05 | **Kedareshwar Temple + Kedar Ghat — Ramakrishna's pilgrimage/ecstasy place [A]** | 30 min |
| 13:45/14:05–14:05/14:35 | Kedar → hotel | 20–30 min, ~1.4–1.6 km walk or mixed walk/auto |
| 14:35–15:30 | lunch | at/near hotel |
| 15:30–18:30 | room/rest | protected recovery before night train |
| 18:30–19:30 | early dinner | — |
| 19:30–23:30 | room/rest/pack | fifth paid night keeps the room available |
| 23:30–23:50 | final check and luggage to agreed pickup path | guesthouse assists through Assi's narrow access |

### Friday limit

This reaches real content until roughly 14:00 without fake filler. It is only honest if Mark accepts the 35–45 minute Panchganga→Kedar walk. Without that walk—or a later, locally verified point-to-point boat—the target cannot be reached with the retained content.

Friday is now substantially calmer than the stale version containing Duniya + Kedar + Vishwanath/Annapurna + Dashashwamedh/Aarti. The room/rest block before the night train grows to roughly nine hours.

---

## ZA 9 JAN — hotel to train

| Time | Plan | Robustness |
|---|---|---|
| 23:50 Fri | leave room with luggage | ten minutes for guesthouse-to-pickup access |
| **00:00** | car departs Assi pickup point | corrected from 00:10 |
| 00:16–00:40 | arrive Varanasi Junction | current real drive range 16–40 min |
| 00:40–01:20 | entrance, platform, coach position and boarding | 50–74 min total station margin before departure |
| **01:30** | train 22324 departs BSB | target 2A sleeper; exact 2027 time/coach/inventory `LIVE_RECHECK` |
| **~13:05** | arrive Kolkata Chitpur (KOAA) | Kolkata planning starts here |

The ten-minute correction matters: at the worst stated 40-minute drive, a 00:10 departure arrives 00:50 and leaves only 40 minutes—not the 45–50 minutes previously claimed. A 00:00 car departure guarantees at least 50 minutes under the same range without recreating the obsolete 1u45 wait.

## Rest and recovery audit

| Transition | Protected turnaround |
|---|---:|
| Monday hotel arrival → Tuesday hotel departure | ~18u15 |
| Tuesday hotel return → Wednesday hotel departure | ~12u45 |
| Wednesday hotel return → Thursday hotel departure | ~13u30–13u45 |
| Thursday baseline return → Friday hotel departure | ~19u00 |
| Friday hotel return → car departure | ~9u25–9u55 in/near the room |

There is no back-to-back late-evening/early-morning collision. Tuesday is the long day, Wednesday ends before evening, Thursday is early but finishes around lunch at baseline, and Friday preserves a large pre-train recovery block.

## Completeness audit — retained content

Covered explicitly:

- Assi Ghat [A+] — Monday dedicated sunset presence.
- New Bhrigu Karyalaya [A+], Tulsi Ghat [A], Anandamayi Ashram [A+], Dashashwamedh/Aarti [A+] — Tuesday.
- Lahiri house [A+], Satyalok [A], Bengali Tola/Thatheri/Chowk [A], Banarasi paan [A], Vishwanath [A], Annapurna [A] — Wednesday.
- Ganges dawn rowboat [A+], Ratneshwar [A+], Manikarnika [A+] — Thursday.
- Tailanga Math [A], Panchganga Ghat [A], Kedar [A] — Friday, plus the personally fixed Duniya visit.

No excluded temple, A*-filler, Sarnath content or new grade appears.

### One remaining canon decision: the distinct Assi–Tulsi dawn walk

The older ledger still describes the **Assi–Tulsi slow dawn walk [A]** as a distinct retained experience. The newest Tuesday instruction instead fixes Bhrigu first at 09:00, then Tulsi, Anandamayi and Dashashwamedh; reintroducing the old dawn walk there would duplicate Tulsi and turn Tuesday into a roughly 13-hour day. It is therefore **not in the recommended base plan**, but it has not been silently erased:

- Recommended decision: treat the newest Tuesday sequence as superseding the separate dawn-walk block; Assi [A+] is fully covered Monday and Tulsi [A] Tuesday.
- If Mark explicitly retains the separate dawn experience, the least-bad slot is Friday 06:15–07:00 with return/rest before the 08:30 start. That makes the train-departure day earlier and duplicates part of Tuesday, so it is not the optimum.

This is the only remaining content-status ambiguity found in the full arrival-to-train audit.

## Required live confirmations

1. Recheck trains 20887 and 22324, especially BSB arrival/departure and coach composition.
2. Confirm Sahi River View Guesthouse, balcony room, five paid nights, late-night luggage assistance and the exact car pickup point.
3. Confirm Bhrigu 09:00 appointment and three-hour envelope.
4. Pre-book Tuesday's Bhadaini→Dashashwamedh boat and recheck Aarti time.
5. Confirm Lahiri house exterior identity/access path and Satyalok's ~10:30 opening.
6. Confirm Vishwanath/Annapurna access/security strategy for Wednesday afternoon.
7. Pre-book Thursday's dawn boat to land near Ratneshwar/Manikarnika without continuing to Panchganga.
8. Confirm Duniya appointment privately and Tailanga's pre-13:00 access.
9. Validate the Panchganga→Kedar walking route locally; only replace it with a boat after a real point-to-point time/pickup is confirmed.

## Final recommendation

Use this as the controlling Varanasi planning spine:

**arrival/Assi → Tuesday fixed four-anchor day → Wednesday complete Lahiri/Old-Kashi day → Thursday boat/Manikarnika day → Friday Duniya/Panchganga/Kedar day → 00:00 station car → 01:30 train.**

This is more coherent than optimizing Tuesday and Friday alone. It restores the missing Assi moment, keeps geographically linked old-city content together, protects both major open-ended lineage places as far as the calendar allows, preserves real recovery before the night train, and exposes rather than hides the single remaining dawn-walk status ambiguity.
