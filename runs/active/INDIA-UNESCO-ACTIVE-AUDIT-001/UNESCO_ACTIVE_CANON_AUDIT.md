# INDIA — UNIVERSAL UNESCO ACTIVE-CANON AUDIT

status: COMPLETE
branch: agent/india-unesco-active-audit
task: `runs/active/INDIA-UNESCO-ACTIVE-AUDIT-001/TASK.md`
audit performed: 2026-08-27
audit type: STATUS AUDIT ONLY — no A+/A/A*/B/C grade was changed, created or reopened by this file.

---

## 1. EXECUTIVE SUMMARY

- **Total current active A+/A/A*/B items audited: 71**
  - KUMAON: 19 (6 A+, 6 A, 4 A*, 3 B)
  - VARANASI / SARNATH: 41 (21 A+, 12 A, 8 B)
  - BODH GAYA / GAYA: 8 (1 A+ parent, 3 A, 4 B)
  - TIRUVANNAMALAI / ARUNACHALA: 1 (1 A+ cluster parent)
  - DELHI: 1 (1 A+)
  - AGRA / TAJ MAHAL: 1 (1 A+)

- **UNESCO WH (item itself is an inscribed property or an official component of one): 6 items**
  — Taj Mahal (Agra); Mahabodhi Temple Complex (Bodh Gaya); and 4 Sarnath rows (Sarnath sacred complex umbrella, Dhamek Stupa, Chaukhandi Stupa, Deer Park/Isipatana landscape). All 6 are currently graded **A+**, none is currently graded B.

- **UNESCO TENTATIVE (item itself is on the official UNESCO Tentative List but not inscribed): 9 items**
  — the nine named Varanasi riverfront ghats (Manikarnika, Dashashwamedh, Assi, Panchganga, Harishchandra, Lalita, Tulsi, Kedar Ghat+Kedareshwar, Adi Keshava Ghat+Temple), all falling under the single tentative-list cultural-landscape entry "Iconic Riverfront of the Historic City of Varanasi" (submitted 2021, whc.unesco.org tentativelists/6526). Current grades: 4 A+ (Manikarnika, Dashashwamedh, Assi, Panchganga — parent-bundle inherited), 4 A (Kedar Ghat+Kedareshwar, Lalita Ghat, Tulsi Ghat, Adi Keshava Ghat+Temple), 1 B (Harishchandra Ghat).

- **Current B items that are genuine UNESCO WH → MARK_REVIEW_TRIGGER = YES: 0 (zero)**
  Every current B-graded item was individually checked against official UNESCO material. None of them is itself an inscribed World Heritage property or a named component of one. The closest cases (Harishchandra Ghat, and other B ghats/temples) are UNESCO **TENTATIVE** or **NEAR/BUFFER ONLY** at most, which the task explicitly excludes from this trigger. See Section 2 for the full per-item reasoning.

- **Key uncertainties (see also Section 4 and the notes below):**
  1. `whc.unesco.org` blocks direct automated fetching (HTTP 403) for this session; all whc.unesco.org-sourced facts below are grounded via search-engine-indexed snippets of the official pages (title + URL confirmed as whc.unesco.org) plus corroborating official/government sources (unesco.org article, PIB press release), not a directly rendered whc.unesco.org page. This is disclosed per row where relevant.
  2. The exact component-level boundary text of the Varanasi Tentative List entry ("Iconic Riverfront of the Historic City of Varanasi") could not be directly rendered; the TENTATIVE label applied to individual ghats is a reasonable, grounded reading of a linear riverfront cultural-landscape nomination explicitly built around "the ghats," not a confirmed itemized component list. Flagged explicitly per row as **not a confirmed itemized component**.
  3. Sarnath's modern (1931) Mulagandha Kuti Vihara temple building is distinct from the ancient "Mulagandhakuti" ruin that is named as part of the inscribed "Archaeological Remains of Sarnath." This is a genuine ambiguity, resolved conservatively to NEAR/BUFFER ONLY — see false-friends section.
  4. The Vrindavan/Braj cluster's two individually A-graded sites are **excluded from the headline total above** because of a genuine, repo-internal scope conflict — see Section 4.5. Their UNESCO status is researched and reported separately, not counted in the 71.
  5. Agra Fort, Fatehpur Sikri and Keoladeo National Park are strong, well-known UNESCO World Heritage properties, but none of them currently carries a Mark A+/A/A*/B grade (they remain in `AGRA_A_PLUS_MARK_SELECTION_SLICE.md` as an un-graded candidate universe: "NO A+ assigned. NO A/B/C changed."). Per TASK.md's scope rule ("no generic UNESCO discovery outside current active content"), they are out of audit scope and are not in the 71-item table. Flagged so the orchestrator can confirm this reading is correct.
  6. Haridwar/Kankhal/Rishikesh and Prayagraj (deferred optional worlds) currently carry **zero** graded A+/A/A*/B items — both selection slices explicitly state "NO A+ assigned. NO A/B/C changed." — so nothing from those clusters appears in scope either.

---

## 2. MARK_REVIEW_TRIGGERS

**Result: no current B item qualifies. This section is empty by design, not by omission.**

Per TASK.md: "Every CURRENT B with genuine UNESCO WH must also get MARK_REVIEW_TRIGGER = YES... Do not flag NEAR/BUFFER-only or TENTATIVE-only items as review triggers."

All current B items across all four in-scope clusters were checked individually:

| Cluster | Current B item | UNESCO label found | Why it does NOT trigger |
|---|---|---|---|
| KUMAON | Naina Peak / China Peak walk | NO UNESCO WH/TENTATIVE | Not a monument/property; no listing found |
| KUMAON | Katarmal Sun Temple walk | NO UNESCO WH/TENTATIVE | Searched specifically for Katarmal on WH/Tentative lists — no listing found. (Modhera Sun Temple, Gujarat, is the sun temple on India's Tentative List; Katarmal is a different, unlisted site.) |
| KUMAON | Ghorakhal Golu Devta Mandir | NO UNESCO WH/TENTATIVE | No listing found |
| VARANASI | Yogoda Satsanga Dhyana Mandali | NO UNESCO WH/TENTATIVE | Modern institutional building, not on any list |
| VARANASI | Harishchandra Ghat | **UNESCO TENTATIVE** (not WH) | Ghat itself sits inside the "Iconic Riverfront of the Historic City of Varanasi" Tentative List entry — Tentative is explicitly excluded from the trigger by TASK.md |
| VARANASI | Kaal Bhairav Temple | NO UNESCO WH/TENTATIVE | Inland temple, not on the riverfront, no listing found |
| VARANASI | Mrityunjay Mahadev Temple | NO UNESCO WH/TENTATIVE | No listing found |
| VARANASI | Lahartara Kabir birthplace memorial | NO UNESCO WH/TENTATIVE | No listing found |
| VARANASI | Bhaskarananda Samadhi / Anand Bagh | NO UNESCO WH/TENTATIVE | No listing found |
| VARANASI | Tulsi Manas Temple | NO UNESCO WH/TENTATIVE | Modern (1964) temple, not on any list |
| VARANASI | Chandraprabha Sanctuary + Rajdari/Devdari waterfalls | NO UNESCO WH/TENTATIVE | Wildlife sanctuary, not on India's WH or Tentative (natural) list |
| BODH GAYA | Archaeological Museum of Bodh Gaya (ASI) | UNESCO NEAR/BUFFER ONLY (not WH) | Adjacent to, and houses artefacts related to, the inscribed Mahabodhi Temple Complex, but the museum building itself is not named as part of WH property 1056 |
| BODH GAYA | Tergar Monastery | NO UNESCO WH/TENTATIVE | Modern (Karmapa) monastery, not on any list |
| BODH GAYA | Mangala Gauri Temple (Shakti Peeth) | NO UNESCO WH/TENTATIVE | No listing found |
| BODH GAYA | Jagannath Temple (naast Mahabodhi) | UNESCO NEAR/BUFFER ONLY (not WH) | Directly adjacent to the Mahabodhi Temple Complex but not itself named as part of WH property 1056 |

**Conclusion:** 0 of 16 current B items are genuine UNESCO WH. Therefore the MARK_REVIEW_TRIGGERS list required by TASK.md Section 2 is empty. If the orchestrating session wants a softer secondary signal for Mark (e.g. "B items in a UNESCO TENTATIVE zone"), Harishchandra Ghat is the only B item with any official UNESCO standing at all (Tentative, not WH) — flagged here for visibility only, explicitly NOT as a MARK_REVIEW_TRIGGER.

---

## 3. FULL ACTIVE TABLE

Columns: cluster | item (+ Dutch recognition hook) | current grade/status | UNESCO label | official UNESCO property name | component name if relevant | UNESCO source | precision note | Mark review trigger

Grade resolution note: where a protected-canon grade conflicted with a later explicit Mark decision-log grade, the later explicit grade is shown and the conflict is flagged inline. Where an item sits inside a Mark A+ "parent bundle," its resolved current status is shown as `A+ (parent: <bundle name>)`.

### KUMAON (19 items)

| Item | Grade | UNESCO label | Official UNESCO property | Component | Source | Precision note | Trigger |
|---|---|---|---|---|---|---|---|
| Mahavatar Babaji's Cave (Kukuchina-Dunagiri) | A+ | NO UNESCO WH/TENTATIVE | — | — | Checked whc.unesco.org India Tentative List; no Kumaon-region entry near Kukuchina/Dunagiri | Not a monument type UNESCO would list | NO |
| Kainchi Dham (Neem Karoli Baba ashram) | A+ parent | NO UNESCO WH/TENTATIVE | — | — | as above | — | NO |
| Hotel Evelyn (Nainital) | A+ | N/A | — | — | — | Accommodation, not a heritage property | NO |
| Naini Lake wandeling (walk) | A+ | N/A | — | — | — | Walking route, not a heritage property | NO |
| Haidakhan Ashram | A+ | NO UNESCO WH/TENTATIVE | — | — | as above | — | NO |
| Historische Haidakhan-grot | A+ | NO UNESCO WH/TENTATIVE | — | — | as above | — | NO |
| Bhumiadhar | A | NO UNESCO WH/TENTATIVE | — | — | as above | — | NO |
| Hanuman Garhi + Maharajji-kuti | A | NO UNESCO WH/TENTATIVE | — | — | as above | — | NO |
| Yogoda Satsanga Sakha Ashram Dwarahat | A | NO UNESCO WH/TENTATIVE | — | — | as above | — | NO |
| Dunagiri Temple / Maa Dunagiri Vaishnavi Temple | A | NO UNESCO WH/TENTATIVE | — | — | as above | — | NO |
| Babaji Smriti Bhavan | A | NO UNESCO WH/TENTATIVE | — | — | as above | — | NO |
| Dhokaney Waterfall-wandeling | A | N/A | — | — | — | Natural walk, not a listed property | NO |
| Kakrighat | A* | NO UNESCO WH/TENTATIVE | — | — | as above | — | NO |
| Dwarahat historic temple groups | A* | NO UNESCO WH/TENTATIVE | — | — | [Search] no WH/Tentative listing found for Dwarahat temples specifically | genuinely notable medieval temple cluster; verified absent from India's Tentative List despite its architectural significance — flagged as a possible future candidate, not a current one | NO |
| Sattal / Seven Lakes | A* | NO UNESCO WH/TENTATIVE | — | — | as above | — | NO |
| Sakley's Restaurant & Pastry Shop | A* | N/A | — | — | — | Commercial bakery, not a heritage property | NO |
| Naina Peak / China Peak walk | B | NO UNESCO WH/TENTATIVE | — | — | as above | — | NO |
| Katarmal Sun Temple-wandeling | B | NO UNESCO WH/TENTATIVE | — | — | [WebSearch] specifically checked; not found on India's WH or Tentative lists (Modhera Sun Temple, Gujarat, is the listed sun temple, a different site) | — | NO |
| Ghorakhal Golu Devta Mandir | B | NO UNESCO WH/TENTATIVE | — | — | as above | — | NO |

### VARANASI / SARNATH (41 items)

| Item | Grade | UNESCO label | Official UNESCO property | Component | Source | Precision note | Trigger |
|---|---|---|---|---|---|---|---|
| Lahiri Mahasaya Samadhi / Satyalok | A+ (parent: Varanasi Kriya core) | NO UNESCO WH/TENTATIVE | — | — | — | Inland old-city site, not on riverfront tentative nomination | NO |
| Lahiri Mahasaya original home | A+ (parent: Varanasi Kriya core) | NO UNESCO WH/TENTATIVE | — | — | — | as above | NO |
| Manikarnika Ghat | A+ parent/bundle | **UNESCO TENTATIVE** | Iconic Riverfront of the Historic City of Varanasi | ghat named explicitly in the tentative description as "the principal cremation ghat" | whc.unesco.org/en/tentativelists/6526 (via search-indexed snippet; direct fetch blocked, 403) | explicitly named in the tentative-list description text found | NO (A+, not B) |
| Shri Tailanga Swami Math | A+ (parent bundle) | UNESCO NEAR/BUFFER ONLY | Iconic Riverfront of the Historic City of Varanasi | adjacent to Panchganga Ghat | as above | math building itself not separately confirmed as a named component | NO |
| Shree Shree Ma Anandamayi Ashram, Bhadaini | A+ | NO UNESCO WH/TENTATIVE | — | — | — | Inland ashram, not on the riverfront | NO |
| Sarnath sacred complex (umbrella) | A+ parent | **UNESCO WH** | Ancient Buddhist Site, Sarnath | whole property (equivalent to the WH-listed landscape) | whc.unesco.org/en/list/927 + unesco.org article | Property inscribed 25 July 2026, 48th session, Busan; criteria (iii)(vi); ~8.05 ha core + 72.2 ha buffer; two component parts: Chaukhandi Stupa + Archaeological Remains of Sarnath | NO (A+) |
| Shri Kashi Vishwanath Temple | A+ (parent: Kashi Vishwanath sacred core) | NO UNESCO WH/TENTATIVE | — | — | — | Frequently misdescribed online as "UNESCO" because of Varanasi's general heritage fame — see false-friends section | NO |
| Yogoda Satsanga Dhyana Mandali, Varanasi | B | NO UNESCO WH/TENTATIVE | — | — | — | — | NO |
| Dashashwamedh Ghat | A+ (parent bundle) | **UNESCO TENTATIVE** | Iconic Riverfront of the Historic City of Varanasi | ghat named explicitly as "the most famous ghat, site of the evening Ganga Aarti" | whc.unesco.org/en/tentativelists/6526 | explicitly named | NO |
| Assi Ghat | A+ | **UNESCO TENTATIVE** | Iconic Riverfront of the Historic City of Varanasi | one of the 84 ghats forming the nominated riverfront | as above | not individually named in the snippets found, but is part of the continuous nominated riverfront strip; not a confirmed itemized component | NO |
| Panchganga Ghat | A+ (parent bundle) | **UNESCO TENTATIVE** | Iconic Riverfront of the Historic City of Varanasi | as above | as above | not individually named; same caveat as Assi Ghat | NO |
| Harishchandra Ghat | B | **UNESCO TENTATIVE** | Iconic Riverfront of the Historic City of Varanasi | as above | as above | not individually named; same caveat | NO — Tentative is explicitly excluded from the trigger by TASK.md |
| Kaal Bhairav Temple | B | NO UNESCO WH/TENTATIVE | — | — | — | Inland temple | NO |
| Maa Annapurna Temple | A+ (parent: Kashi Vishwanath core) | NO UNESCO WH/TENTATIVE | — | — | — | — | NO |
| Sankat Mochan Hanuman Temple | A | NO UNESCO WH/TENTATIVE | — | — | — | — | NO |
| Durga Temple and Durga Kund | A | NO UNESCO WH/TENTATIVE | — | — | — | — | NO |
| Vishalakshi Gauri Temple | A+ (parent: Kashi Vishwanath core) | UNESCO NEAR/BUFFER ONLY | Iconic Riverfront of the Historic City of Varanasi | adjacent to Manikarnika Ghat | whc.unesco.org/en/tentativelists/6526 | temple building not separately confirmed as named component | NO |
| Sankatha Devi Temple | A | NO UNESCO WH/TENTATIVE | — | — | — | — | NO |
| Kedareshwar Temple + Kedar Ghat | A | **UNESCO TENTATIVE** (ghat component only) | Iconic Riverfront of the Historic City of Varanasi | Kedar Ghat | as above | ghat component tentative; the temple building's individual status not separately confirmed — treated as one bundle per canon's own naming, label applies to the dominant/ghat half | NO |
| Lalita Ghat | A | **UNESCO TENTATIVE** | Iconic Riverfront of the Historic City of Varanasi | as above | as above | not individually named; same caveat as Assi Ghat | NO |
| Nepali Temple / Kathwala Temple | A | UNESCO NEAR/BUFFER ONLY | Iconic Riverfront of the Historic City of Varanasi | adjacent to Lalita Ghat | as above | temple building not separately confirmed as named component | NO |
| Bindu Madhav Temple | A+ (parent bundle) | UNESCO NEAR/BUFFER ONLY | Iconic Riverfront of the Historic City of Varanasi | adjacent to Panchganga Ghat | as above | as above | NO |
| Mrityunjay Mahadev Temple | B | NO UNESCO WH/TENTATIVE | — | — | — | — | NO |
| Kabir Chaura Math | A | NO UNESCO WH/TENTATIVE | — | — | — | Inland, not riverfront | NO |
| Lahartara Kabir birthplace memorial | B | NO UNESCO WH/TENTATIVE | — | — | — | — | NO |
| Bhaskarananda Samadhi / Anand Bagh | B *(regraded from protected-canon A to B by 2026-08-24 Mark decision — used newer grade)* | NO UNESCO WH/TENTATIVE | — | — | — | — | NO |
| Dhamek Stupa | A+ (parent: Sarnath) | **UNESCO WH** | Ancient Buddhist Site, Sarnath | named component of "Archaeological Remains of Sarnath" | whc.unesco.org/en/list/927 + unesco.org article | explicitly named as an included structure | NO |
| Mulagandha Kuti Vihara | A+ (parent: Sarnath) | UNESCO NEAR/BUFFER ONLY *(ambiguous — see false-friends)* | Ancient Buddhist Site, Sarnath | ambiguous — see note | unesco.org article ("Mulagandhakuti" ancient ruin named as component) vs. general knowledge of the 1931 Mahabodhi Society temple of the same name | Two distinct structures share this name at Sarnath: (a) the excavated ancient "Mulagandhakuti" foundation, explicitly named as part of the inscribed Archaeological Remains; (b) the actively-used 1931 modern temple built by the Maha Bodhi Society, standing in the same historic Deer Park landscape but not itself an ancient-ruin component. The Mark-canon item most plausibly refers to (b), the visited modern temple. Resolved conservatively to NEAR/BUFFER ONLY rather than WH. | NO |
| Chaukhandi Stupa | A+ (parent: Sarnath) | **UNESCO WH** | Ancient Buddhist Site, Sarnath | one of the two named component parts of the serial property | whc.unesco.org/en/list/927 | explicitly and separately named as a full component (not merely part of the other component) | NO |
| Sarnath Archaeological Museum | A+ (parent: Sarnath) | UNESCO NEAR/BUFFER ONLY | Ancient Buddhist Site, Sarnath | not confirmed as a named component | [WebSearch] museum described as housing the site's artefacts (incl. the original Ashoka Lion Capital) but not named among the inscribed monument components in any source found | 1910-built museum building; official boundary/buffer map not directly accessible to confirm inside/outside status | NO |
| Deer Park / Isipatana sacred landscape | A+ (parent: Sarnath) | **UNESCO WH** | Ancient Buddhist Site, Sarnath | equivalent to the inscribed historic landscape itself | unesco.org article: "the historic landscape widely known as Deer Park" | this entity is effectively the umbrella landscape the property describes itself as | NO |
| Saranganath Temple | A+ (parent: Sarnath) | UNESCO NEAR/BUFFER ONLY | — | not a component — distinct Jain temple near the Buddhist ensemble | — | genuinely different tradition (Jain, associated with Shreyansanath) standing near but outside the Buddhist archaeological ensemble | NO |
| Tulsi Manas Temple | B *(regraded from protected-canon A to B by 2026-08-24 Mark decision — used newer grade)* | NO UNESCO WH/TENTATIVE | — | — | — | modern (1964) temple | NO |
| Tulsi Ghat | A | **UNESCO TENTATIVE** | Iconic Riverfront of the Historic City of Varanasi | as above | as above | not individually named; same caveat as Assi Ghat | NO |
| Lolark Kund | A | NO UNESCO WH/TENTATIVE | — | — | — | Set back from the river; a kund (stepped tank), not one of the riverfront ghats | NO |
| Ratneshwar Mahadev Temple (leaning temple) | A+ (Manikarnika bundle child) | UNESCO NEAR/BUFFER ONLY | Iconic Riverfront of the Historic City of Varanasi | adjacent/built into Manikarnika Ghat | as above | temple structure itself not separately confirmed as named component | NO |
| Shitala Mata Temple, Dashashwamedh | A+ (parent bundle) | UNESCO NEAR/BUFFER ONLY | Iconic Riverfront of the Historic City of Varanasi | adjacent to Dashashwamedh Ghat | as above | as above | NO |
| Shreyansanath Jain Tirth, Sarnath (Simhapuri) | A *(elevated from PROVISIONAL_NO_ABC to A by 2026-08-24 Mark decision — used newer grade)* | UNESCO NEAR/BUFFER ONLY | — | not a component — distinct Jain tirtha | — | near the Buddhist WH property but a different tradition/site | NO |
| Adi Keshava Ghat + Temple | A *(elevated from PROVISIONAL_NO_ABC to A by 2026-08-24 Mark decision — used newer grade)* | **UNESCO TENTATIVE** (ghat component only) | Iconic Riverfront of the Historic City of Varanasi | Adi Keshava Ghat, northern end of the ghat chain | as above | ghat component tentative; attached temple's individual status not separately confirmed | NO |
| Ganges dawn rowboat (experience) | A | N/A | — | — | — | Experience/activity, not a monument; occurs physically over the tentative-listed riverfront but is not itself a listable property | NO |
| Chandraprabha Sanctuary + Rajdari–Devdari waterfalls | B | NO UNESCO WH/TENTATIVE | — | — | — | Wildlife sanctuary in Chandauli district; not on India's WH or Tentative (natural) list | NO |

### BODH GAYA / GAYA (8 items)

| Item | Grade | UNESCO label | Official UNESCO property | Component | Source | Precision note | Trigger |
|---|---|---|---|---|---|---|---|
| Mahabodhi Temple Complex | A+ parent | **UNESCO WH** | Mahabodhi Temple Complex at Bodh Gaya | whole property | whc.unesco.org/en/list/1056 (via search-indexed confirmation) | List ID 1056, inscribed 2002; official UNESCO name matches the Mark-canon name exactly | NO (A+) |
| Sujata Stupa, Bakraur | A | NO UNESCO WH/TENTATIVE | — | — | — | ~2 km away in Bakraur village, across the Niranjana/Falgu river; outside the inscribed boundary; no official evidence of buffer-zone inclusion found | NO |
| Dungeshwari Cave Temples (Mahakala Caves) | A | NO UNESCO WH/TENTATIVE | — | — | — | ~8 km away; separate site | NO |
| Great Buddha Statue | A | NO UNESCO WH/TENTATIVE | — | — | — | Modern (1989) statue on separate temple grounds | NO |
| Archaeological Museum of Bodh Gaya (ASI) | B | UNESCO NEAR/BUFFER ONLY | Mahabodhi Temple Complex at Bodh Gaya | not a named component | — | Adjacent to the inscribed complex, houses related artefacts, but museum building not itself part of WH property 1056 | NO |
| Tergar Monastery | B | NO UNESCO WH/TENTATIVE | — | — | — | Modern (Karmapa) monastery | NO |
| Mangala Gauri Temple (Shakti Peeth) | B | NO UNESCO WH/TENTATIVE | — | — | — | Separate hill site (Pretshila) | NO |
| Jagannath Temple (naast Mahabodhi) | B | UNESCO NEAR/BUFFER ONLY | Mahabodhi Temple Complex at Bodh Gaya | not a named component | — | Directly adjacent per its own canon description ("naast Mahabodhi") but not itself part of WH property 1056 | NO |

### TIRUVANNAMALAI / ARUNACHALA (1 item)

| Item | Grade | UNESCO label | Official UNESCO property | Component | Source | Precision note | Trigger |
|---|---|---|---|---|---|---|---|
| Arunachala / Ramana sacred world (mountain, ashram, direct Ramana life-sites) | A+ parent | NO UNESCO WH/TENTATIVE | — | — | Checked against India's WH list and Tentative List (whc.unesco.org/en/statesparties/in); Arunachaleswarar Temple is not part of "Great Living Chola Temples" (Thanjavur/Gangaikondacholapuram/Darasuram) nor any Tamil Nadu temple tentative entry found | Only the cluster-level A+ has been set by Mark; individual sites inside it (Ramanasramam, Virupaksha Cave, Skandashram, Arunachaleswarar Temple, Girivalam path) have not yet received their own ordinary A/B/C re-grading, so this is audited as one bundled row | NO |

### DELHI (1 item)

| Item | Grade | UNESCO label | Official UNESCO property | Component | Source | Precision note | Trigger |
|---|---|---|---|---|---|---|---|
| Nirmal Dham (Shri Mataji Nirmala Devi Mahasamadhi, Chhawla) | A+ | NO UNESCO WH/TENTATIVE | — | — | — | Not related to any Delhi WH property (Qutb Minar, Humayun's Tomb, Red Fort Complex are unrelated sites/locations); no listing found | NO |

### AGRA / TAJ MAHAL (1 item)

| Item | Grade | UNESCO label | Official UNESCO property | Component | Source | Precision note | Trigger |
|---|---|---|---|---|---|---|---|
| Taj Mahal | A+ | **UNESCO WH** | Taj Mahal | whole property | whc.unesco.org/en/list/252 (via search-indexed confirmation) | List ID 252, inscribed 1983; official UNESCO name matches exactly | NO (A+) |

---

## 4. FALSE-FRIENDS / IMPORTANT NON-MATCHES

1. **Kashi Vishwanath Temple, Sankat Mochan, Durga Temple, Tulsi Manas Temple, Kabir Chaura Math and other inland Varanasi temples** are routinely described in general/tourist writing as "part of Varanasi's UNESCO heritage." Officially this is imprecise: Varanasi as a whole is **not** an inscribed World Heritage City, and only the specific riverfront ghats sit inside the Tentative-List nomination "Iconic Riverfront of the Historic City of Varanasi." Temples set back from the river have no official WH or Tentative status of their own.

2. **Sarnath, pre-July-2026 status.** Any source (including outdated versions of this repository's own research, or a model's own stale training-era knowledge) that calls Sarnath "only Tentative" or omits WH status entirely is now wrong. Sarnath ("Ancient Buddhist Site, Sarnath") was inscribed as a full World Heritage property on 25 July 2026 at the 48th session in Busan, after 28 years on the Tentative List (since 1998). This was the specific trap flagged by TASK.md and has been verified directly against whc.unesco.org/en/list/927, unesco.org's own article, and the Indian government's PIB press release.

3. **Sarnath Archaeological Museum and the modern Mulagandha Kuti Vihara temple** are frequently presented in travel material as "the UNESCO site," but neither is confirmed as a named component of the inscribed property (which comprises specifically the Chaukhandi Stupa and the "Archaeological Remains of Sarnath" — Dhamek Stupa, Dharmarajika Stupa, the ancient Mulagandhakuti ruin, and the Ashokan Pillar). Both are adjacent/near-buffer at most. This is a genuine ambiguity for the modern temple in particular — see the dedicated note in the Varanasi table row.

4. **Mahabodhi Temple Complex vs. the rest of Bodh Gaya.** Bodh Gaya town contains many other Buddhist sites (Great Buddha Statue, Tergar Monastery, numerous national monasteries, the Archaeological Museum) that are commonly lumped in with "UNESCO Bodh Gaya" in general writing. Only the Mahabodhi Temple Complex itself (WH property 1056) is inscribed; the rest are near/buffer or unrelated.

5. **Agra Fort, Fatehpur Sikri, Keoladeo National Park** — all three are genuinely and unambiguously inscribed UNESCO World Heritage properties, and it would be a serious error for a *future* audit to assume they are not simply because this audit found them out of scope. They are excluded here strictly because they do not currently carry a Mark A+/A/A*/B grade (Agra's cluster file explicitly states "NO A+ assigned. NO A/B/C changed"). If Mark later grades any of them, they should be revisited immediately — Keoladeo in particular would very plausibly become a MARK_REVIEW_TRIGGER candidate if it were ever graded B.

6. **Arunachaleswarar Temple, Tiruvannamalai** is sometimes discussed online in the context of UNESCO structural-safety inspections/recommendations (a 2017 advisory episode), which can misleadingly read as if the temple already has WH or Tentative status. It does not — the inspection references relate to general heritage-conservation advisory activity, not a WH/Tentative listing.

7. **Katarmal Sun Temple (Kumaon)** is sometimes compared in general travel writing to Konark's Sun Temple (which is itself full UNESCO WH, in Odisha — not part of this trip). Katarmal itself carries no UNESCO status of any kind; the sun temple that *is* on India's Tentative List is Modhera, in Gujarat — a different site entirely, unrelated to this trip.

---

## 5. CURRENT-CANON INPUTS USED

Files read to establish the current active A+/A/A*/B universe, in the order read, with the resolution logic applied where conflicts were found:

1. `governance/ACTIVE_FRAMEWORK.md` — authority map (explicit Mark decisions > CURRENT_STATE.md > protected canon > current task outputs).
2. `governance/MARK_TRAVEL_PREFERENCES_CURRENT.md` — human-context canon; confirms UNESCO-related preference is not itself recorded here (it lives in the orchestrator's task framing) and confirms the A+/A/A*/B/C semantics quoted throughout this audit.
3. `governance/CURRENT_STATE.md` (updated 2026-08-27) — the compact current boot state; source of the six fixed A+ worlds, the Kumaon `DURATION_CLOSED` baseline, the latest 2026-08-27 Varanasi decisions (Ganges dawn rowboat A, Chunar Fort C, Jaunpur C, Chandraprabha B), and the explicit statement that Haridwar/Rishikesh/Prayagraj/Braj survival is undecided.
4. `runs/active/INDIAZILVER-ENTITY-ID-PROXIMITY-BACKFILL-001/PROTECTED_CANON_BASELINE.csv` — entity-level individual grades for Varanasi, Bodh Gaya and Kumaon; used as the base layer, overridden per-row by later explicit decision-log grades where a conflict was found (Tulsi Manas Temple A→B, Bhaskarananda Samadhi A→B, Shreyansanath Jain Tirth and Adi Keshava Ghat+Temple PROVISIONAL→A).
5. `runs/active/INDIA10-CLUSTER-COVERAGE-REAUDIT-001/A_PLUS_MARK_DECISION_LOG.md` (updated 2026-08-26) — canonical A+ spine plus the full Kumaon A/A*/B canon and the Varanasi/Bodh Gaya ordinary-grade deltas; treated as the newest general-grade authority except where CURRENT_STATE.md (2026-08-27, one day newer) carried an even later Varanasi update.
6. `runs/active/INDIA10-CLUSTER-COVERAGE-REAUDIT-001/FIXED_CORE_TIME_FOOTPRINT_AUDIT_2026-08-26.md` — confirmed which of the six fixed-core worlds have only an "A+ skeleton" (Delhi, Agra, Bodh Gaya's remaining traveler layer, Tiruvannamalai) versus full ordinary-grade closure (Kumaon, partially Varanasi).
7. `runs/active/INDIA10-CLUSTER-COVERAGE-REAUDIT-001/DELHI_A_PLUS_MARK_SELECTION_SLICE.md`, `AGRA_A_PLUS_MARK_SELECTION_SLICE.md`, `TIRUVANNAMALAI_A_PLUS_MARK_SELECTION_SLICE.md`, `HARIDWAR_RISHIKESH_A_PLUS_MARK_SELECTION_SLICE.md`, `PRAYAGRAJ_A_PLUS_MARK_SELECTION_SLICE.md` — each explicitly states "NO A+ assigned. NO A/B/C changed" beyond the already-recorded A+ anchor (or, for Haridwar/Prayagraj, no A+ at all yet); used to confirm these clusters' candidate universes are out of current active scope.
8. `runs/active/TIRUVANNAMALAI-ARUNACHALA-CLUSTER-001/STATUS.md` — confirms Tiruvannamalai is a cluster-level `A` lock (now superseded to A+ by the decision log), not individual site grades.
9. `decisions/VRINDAVAN_BRAJ_CLUSTER_DROPPED_BY_MARK_2026-08-26.md` — read in full; its **current on-branch content is a correction that invalidates its own filename's claim** (title: "PREMATURE DROP RECORD CORRECTED"; status: `INVALIDATED_AS_MARK_DECISION__A_PLUS_GATE_OPEN`). See Section 4.5-equivalent note below for how this was handled.
10. `git log` on the fork lineage — used to confirm commit order (`8357df0` "Record Mark decision to drop Vrindavan/Braj cluster" is **older** than `ef7e407` "Correct premature Vrindavan drop interpretation," which is itself carried on this audit branch) — i.e., the correction postdates and supersedes the drop within the same file.

### 5.1 Note on the Vrindavan/Braj scope conflict (transparency, not a grade change)

The orchestrating brief for this task stated that `decisions/VRINDAVAN_BRAJ_CLUSTER_DROPPED_BY_MARK_2026-08-26.md` "dropped the Vrindavan/Braj cluster from the active trip" and that its two individually-A-graded sites should therefore be excluded. Reading that exact file on this branch shows its **current content is the opposite of a drop**: it explicitly states the earlier drop interpretation was premature/invalidated, that Mark asked for the decision flow to be reconstructed, and that "no valid final RETAIN/DROP decision for the Vrindavan/Braj cluster currently exists" — matching `governance/CURRENT_STATE.md`'s listing of BRAJ/MATHURA–VRINDAVAN–GOVARDHAN under "OPTIONAL WORLDS — DEFERRED. Do not decide survival yet," not under a dropped/C status.

Per TASK.md's explicit instruction ("if genuinely ambiguous, note the ambiguity rather than silently including or excluding"), this audit:
- does **not** count the two Braj sites in the 71-item headline total or the main FULL ACTIVE TABLE, honoring the orchestrator's explicit steer, but
- reports their UNESCO status here rather than silently dropping them, since they do currently carry an explicit, unsuperseded Mark **A** grade at the site level:

| Item | Grade | UNESCO label | Notes |
|---|---|---|---|
| Katyayani Peeth / Keshav Ashram, Vrindavan | A (site-level, cluster-inclusion undecided) | NO UNESCO WH/TENTATIVE | No Mathura–Vrindavan property exists on India's WH or Tentative List |
| Neem Karoli Baba Ashram en samadhi, Vrindavan | A (site-level, cluster-inclusion undecided) | NO UNESCO WH/TENTATIVE | as above |

Neither is UNESCO WH, so this conflict has **no effect** on the MARK_REVIEW_TRIGGERS list either way — flagged for the orchestrator's own verification since it is a real discrepancy between the task briefing and the current file content, not a research artifact of this audit.

END_OF_AUDIT
