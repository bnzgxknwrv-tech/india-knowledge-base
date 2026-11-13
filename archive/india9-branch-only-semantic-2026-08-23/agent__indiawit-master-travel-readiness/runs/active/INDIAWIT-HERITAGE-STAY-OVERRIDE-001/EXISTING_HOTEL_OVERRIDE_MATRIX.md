# EXISTING_HOTEL_OVERRIDE_MATRIX — INDIA WIT

status: COMPLETE_AUDIT_SNAPSHOT
verified_at: 2026-08-19

## Rule

A heritage-stay candidate may trigger review, but **never changes a `LOCKED_BY_MARK` hotel automatically**. The only action this file can produce is `MARK_REVIEW_REQUIRED`.

## Known locked hotel decisions

### Varanasi — Sahi River View Guesthouse

- status: **LOCKED_BY_MARK**
- area: Assi Ghat / Varanasi
- decision source: personal recommendation from Debby
- mandatory notes already locked: request balcony room; greet Jitendre from Debby
- lock remains **UNCHANGED**.

### Override audit against heritage candidates

| candidate | same destination/cluster relation | current overnight possible | heritage advantage | logistics/comfort unknowns | matrix result |
|---|---|---|---|---|---|
| **Shree Shree Ma Anandamayi Ashram, Bhadaini** | **DIRECT** — same Varanasi south/Assi-Bhadaini cluster; existing hotel decision itself names this as nearby A-location | **JA** — current Sangha explicitly publishes room-booking and local dharamshala contacts | potentially sleep at an actual ashram personally associated with Anandamayi Ma rather than only nearby | room standard, bathroom, access rules, foreign-guest handling, exact room/location within complex, late arrival and luggage logistics not yet compared | **MARK_REVIEW_REQUIRED — HIGH-IMPACT-REVIEW**. Do not alter Sahi lock. |
| Yogananda Mahamandal-hermitage attic | Varanasi | identity unresolved | direct historic novice residence if ever identified | building itself unresolved | **NO OVERRIDE** now |
| Lahiri Mahasaya D 31/58 residence | Varanasi | no public lodging verified | extremely high person relevance | private/devotional house; not a hotel | **NO OVERRIDE** |
| other Varanasi private houses/rooms | Varanasi | mostly unknown/private | heritage visit value | no legal/public lodging basis | **NO OVERRIDE** |

## Other clusters without a known LOCKED_BY_MARK hotel in the audited source envelope

These do not override a lock, but should be inserted ahead of ordinary hotel selection if their cluster is chosen:

| cluster | heritage stay | review level | reason |
|---|---|---|---|
| Nainital | **Hotel Evelyn** | **HIGH-IMPACT-REVIEW** | Same operating hotel where Ram Dass stayed in 1971; unusually strong possibility of sleeping in the actual historical hotel. Historic room itself still unverified. |
| Tiruvannamalai | **Sri Ramanasramam guest accommodation** | **HIGH-IMPACT-REVIEW** | Arunachala/Tiruvannamalai is already LOCKED_BY_MARK as A-anchor. Modern guest rooms inside/around the ashram offer maximum same-complex immersion; sacred historical rooms/caves remain non-bookable. |
| Mumbai | **Taj Mahal Palace** | **HIGH-IMPACT-REVIEW** | Same historic hotel where Yogananda occupied a suite in 1935; current hotel is fully operational and bookable. Exact suite unknown. |
| Belur / Kolkata-Hooghly | **Belur Math guest house/Yatri Nivas** | **HIGH-IMPACT-REVIEW** | Same monastery complex strongly tied to Vivekananda, with official pilgrimage accommodation. Historic Vivekananda room is not itself lodging. |
| Serampore | YSS Serampore retreat | REVIEW | Allows stay in the same heritage town/lineage environment near Anandaloka and Sri Yukteswar Smriti Mandir; not the historic rooms themselves. |
| Kamarpukur | RKM Kamarpukur guest house | REVIEW | Official devotee guest lodging in the birthplace complex context of Ramakrishna; not his childhood room. |
| Kankhal | Anandamayi International Centre | REVIEW | Bookable devotee retreat immediately adjoining Ma's Ashram/Samadhi; separate modern facility. |
| Ranchi | YSS Ranchi guest accommodation | REVIEW / DATE-SENSITIVE | Strong Yogananda same-campus concept, but official accommodation is closed until early 2027; reopening must be verified against actual itinerary date. |
| Puri | Karar Ashram | REVIEW_PENDING_BOOKABILITY | Same exact shared heritage site for Sri Yukteswar + Hariharananda; public overnight policy not yet verified. |
| Vrindavan | Katyayani Peeth / Anandamayi Ashram / NKB-Ram Dass network | REVIEW | Multiple heritage-stay signals, but exact bookability and person-specific historical room continuity vary and need direct institution contact. |

## Override hierarchy for later hotel selection

When Mark has chosen a cluster and no hotel is locked, accommodation search should use this order:

1. `SAME_HISTORIC_ROOM_BOOKABLE = JA` — strongest possible heritage override.
2. `SAME_HISTORIC_HOTEL_OR_BUILDING_BOOKABLE = JA` — e.g. Hotel Evelyn/Taj if room cannot be proven.
3. `SAME_ASHRAM_OR_MONASTERY_COMPLEX_GUEST_ROOM = JA` — e.g. Sri Ramanasramam, Belur Math.
4. `ADJACENT_OFFICIAL_HERITAGE_GUESTHOUSE = JA` — e.g. Anandamayi International Centre, Kankhal.
5. ordinary logistics hotel.

This hierarchy is a **review order**, not an automatic decision rule. Comfort, access, winter/weather, transit and Mark's preferences can outweigh heritage value.

## Existing lock protection

No line in this audit supersedes `Sahi River View Guesthouse`. Its canonical state remains `LOCKED_BY_MARK` until Mark explicitly chooses otherwise.