# INDIA9 CANON RECONCILIATION — 2026-08-23

Status: CURRENT REGIE CANON PATCH
Branch: `agent/india8-cluster-casting`
Purpose: reconcile the full boot chain, later Mark decisions, protected legacy locks, current route V2, the 2026-08-23 quarter-hour-planning delta, and the completed retained-route geo-QA worker result.

This file is additive. It does NOT delete or downgrade any historic A/B/C decision. Where older files conflict with later explicit Mark decisions, the later decision controls current trip routing while the older record remains preserved as provenance.

## 1. PRECEDENCE APPLIED

For every location, cluster, sleep base or hotel, use this order before presentation:
1. newest explicit Mark decision / newest explicit `LOCKED_BY_MARK` or equivalent lock;
2. accommodation/base lock;
3. cluster decision;
4. site A/B/C decision;
5. reconciled master/decision files;
6. governance/handoff;
7. older protected locks;
8. old candidate/overview/research lists.

Never reopen a completed A/B/C or accommodation decision merely because an older overview still calls it provisional/open.

## 2. CURRENT ROUTE FRAME

Current route architecture remains `WORKING_ROUTE_V2_TRAIN_FIRST_NEWYEAR_RISHIKESH_2026-08-23.md`, except where explicitly corrected by the later handoff `handoffs/INDIA8_TO_INDIA9_QUARTER_HOUR_PLANNING_DELTA_2026-08-23.md` and this reconciliation.

Hard international frame:
- outbound Air India 18 Dec 2026 20:35 AMS -> DEL, arrival 19 Dec 10:15;
- return Air India 21 Jan 2027 12:20 DEL -> AMS;
- 33 India nights, including intentional overnight-train nights.

Current 33-night topology is unchanged:
- 19 Dec overnight train Delhi -> Kathgodam;
- 20–22 Dec Haidakhan, 3 nights;
- 23–25 Dec Kukuchina/Joshi Guest House, 3 nights;
- 26–28 Dec Nainital/Hotel Evelyn, 3 nights;
- 29–31 Dec Rishikesh, 3 nights;
- 1 Jan Agra, 1 night;
- 2–3 Jan Vrindavan, 2 hotel nights;
- 4 Jan overnight Mathura -> Prayagraj;
- 5–10 Jan Varanasi, 6 nights;
- 11–13 Jan Bodh Gaya/Gaya, 3 nights;
- 14–18 Jan Tiruvannamalai/Arunachala, 5 nights;
- 19–20 Jan Delhi, 2 buffer nights.

## 3. EXACTLY TWO ASHRAM STAYS

Newest Mark rule: exactly two desired ashram sleep experiences:
1. Haidakhan Ashram;
2. Sri Ramanasramam, if accommodation application is accepted/available.

Therefore:
- Parmarth Niketan remains a Rishikesh/New-Year spiritual EXPERIENCE target only;
- Parmarth Niketan is NOT the Rishikesh sleep base;
- Rishikesh sleep must be a normal hotel/guesthouse in the relevant Swarg Ashram / Parmarth-access zone;
- exact Rishikesh property is not `LOCKED_BY_MARK` and remains a bounded property/availability choice, not an unresolved citywide geography question.

Any older file calling Parmarth the preferred sleep base is superseded on the sleep question only.

## 4. KASAR / ALMORA — PROTECTED A, DELIBERATELY OFF CURRENT ROUTE

`KASAR_ALMORA_YIELDS_TO_RISHIKESH_2026-08-23.md` is an explicit Mark route decision.

Consequences:
- no dedicated Kasar/Almora sleep module in V2;
- this does NOT downgrade or delete protected A decisions;
- Turiya Niwas (080) remains `A / LOCKED_BY_MARK` as a destination but is not a current-trip sleep base;
- Bodh Ashram (081) remains `A / LOCKED_BY_MARK` but off the current V2 route;
- Kasar Devi, Crank's Ridge, Kakrighat, Jageshwar, Ramakrishna Kutir, Chitai Golu Devta and other preserved A records remain A where previously locked, but do not consume current V2 nights solely because of that status;
- B/C records remain preserved unchanged.

Do NOT ask Mark again whether this trade-off is accepted. It already is a Mark route decision.

## 5. RISHIKESH / KANKHAL / HARIDWAR — RETAINED ROUTE MODULE

Older cluster summaries calling this corridor only `B / reserve` are superseded by the later route decision that inserted the corridor for 29–31 Dec.

Site semantics remain separate:
- Kankhal Anandamayi Ma Mahasamadhi: strong A;
- Har Ki Pauri / Ganga Aarti: light/in-cluster A;
- Beatles Ashram: light/in-cluster A;
- Shivpuri–Rishikesh rafting: B and must remain visible in retained-A/B accounting even if a final day card explicitly drops it for weather, safety, season or overload;
- Parmarth/New-Year activity: experience/framework, not a new A/B/C and not an ashram sleep base.

## 6. VARANASI — PROTECTED FINAL SELECTION + LATER ADDITIONS

The durable Varanasi decision run is `VARANASI-GEO-DELIVERY-REPAIR-001`.

Protected original 001–040 final Mark selection remains exactly:
- A (32): 001, 002, 003, 004, 005, 006, 007, 009, 010, 011, 014, 015, 016, 017, 018, 019, 020, 021, 022, 024, 028, 029, 030, 031, 032, 033, 034, 035, 036, 037, 038, 039;
- B (5): 008, 012, 013, 023, 025;
- C (3): 026, 027, 040.

These 40 decisions are CLOSED and must never be replaced by a shorter V2 prose list.

Permanent names 001–040 remain those in `NUMBERING_REGISTRY.jsonl` of the Varanasi run.

Post-maintenance candidates 041–045 later received explicit Mark decisions and must be layered ADDITIVELY, without rewriting the 32/5/3 historical statement:
- 041 Parshvanath Digambar Jain Temple, Bhelupur — B;
- 042 Suparshvanath Jain Tirth, Bhadaini — B;
- 043 Shreyansanath Jain Tirth, Sarnath — A;
- 044 Ramnagar Fort — B;
- 045 Adi Keshava Ghat — A.

Thus quarter-hour/day-card planning must account for every retained A/B from 001–045 according to these protected + later decisions, or explicitly mark a B as not scheduled for a concrete operational reason. No silent drops.

Important semantic correction: older route prose that labels Kedar/Kedareshwar or Sankatha as B is not allowed to override immutable VNS decisions 019=A and 018=A. The immutable Varanasi decision files control those IDs.

## 7. VARANASI SLEEP BASE — CLOSED DECISION

Sahi River View Guesthouse, Assi Ghat:
- accommodation id: `VNS-HOTEL-001`;
- status: `LOCKED_BY_MARK`;
- room preference: balcony room;
- named contact: Jitendre;
- greetings from Debby;
- address recorded in accommodation register: B1/158 A2, Assi Ghat Rd, Varanasi, Uttar Pradesh 221005;
- exact Google Maps marker is not yet canonically verified; do not guess one.

Any older file saying Varanasi hotel research is open/provisional is superseded. Do not re-present alternative Varanasi hotels unless Mark explicitly reopens the decision.

## 8. BODH GAYA — HISTORIC LOCKS PRESERVED; LATEST TRIP SELECTION CONTROLS ROUTE

Older durable Bodh Gaya records include explicit `LOCKED_BY_MARK` A/B/C decisions, including the 2026-08-05 `046–049 = all A` decision and later 050–078 locks.

The 2026-08-23 V2 route contains later explicit trip decisions and therefore controls the current-trip selection where inconsistent:
- Mahabodhi Temple — A;
- Bodhi Tree — A parent/micro layer of the Mahabodhi enlightenment core;
- Sujata Stupa/Bakraur — A;
- Great Buddha Statue — B;
- Dungeshwari/Mahakala Cave Temples — C for the current trip;
- Barabar/Nagarjuni Caves — C;
- Gurpa Hill — C.

This is a supersede in current-trip selection, not deletion of historical decision provenance. Older `046–049 all A` must never silently resurrect Dungeshwari/Great Buddha as current route-driving A after the later Mark selection.

## 9. TIRUVANNAMALAI / ARUNACHALA

A decisions remain:
- Sri Ramanasramam;
- Virupaksha Cave;
- Skandashram;
- Arunachaleswarar Temple;
- Gurumurtam;
- Pavalakunru;
- Giripradakshina/Girivalam.

B decisions remain:
- Mango Tree Cave;
- Pachaiamman Temple.

Micro-sites inside Sri Ramanasramam remain nested under the parent A and must be surfaced in the final visit card, not re-voted as separate ABC locations.

Sri Ramanasramam accommodation is the second of the exactly two desired ashram stays. If unavailable, use a normal Ramana Nagar/Chengam Road fallback without changing the A decision for the ashram itself.

## 10. GEO QA WORKER — PARTIAL ACCEPTANCE ONLY

Worker branch: `agent/cci-retained-route-ab-geo-qa`
Worker commit: `3f2280ef45fb088efa00c634563902346f161dcb`

Accepted:
- useful retained-route inventory cross-checks;
- explicit operational blocker collection;
- preservation of unresolved geo states rather than inventing pins;
- several silent-drop warnings worth reconciling against the full canon.

Rejected as exact-map canon without additional proof:
- any row labelled `EXACT_GOOGLE_MAPS_MARKER` when the evidence in that row is only Wikipedia/derived coordinates rather than an actually opened and identity-matched Google Maps place record or approved official map record;
- the Madan Mohan / Banke Bihari coordinate collision cannot be treated as two exact map closures;
- any Varanasi completeness conclusion based only on V2 shorthand rather than the protected immutable 001–040 selection plus later 041–045 decisions.

Corrected worker interpretation:
- worker recommendation to ask Mark whether Kasar/Almora A-sites may be sacrificed is superseded by the explicit Mark yield decision; no repeat question;
- worker output is QA evidence, not a replacement master canon;
- unresolved markers remain visible as `ADDRESS_CONFIRMED_MARKER_NOT_CLOSED`, `ZONE_ONLY`, `GEO_CONFLICT`, or `NONPUBLIC_OR_NOT_FOR_VISIT` as appropriate.

## 11. ROUTE-BUILD ORDER — HARD

Every subsequent itinerary/day-card pass uses exactly:
1. SLEEP BASE;
2. EXISTING A;
3. DISTANCES / COMBINATIONS;
4. LONELY PLANET / traveler-gem layer;
5. ride-along B;
6. NIGHTS;
7. CALENDAR / CLOSURES;
8. TRANSPORT;
9. HOTEL;
10. DAY CARDS.

Never calculate from an arbitrary city centre when a concrete sleep base/anchor exists.

## 12. AL-BESLIST? GATE

Before presenting any location, cluster, hotel or sleep base as a choice:
- search newest Mark decisions and locks;
- search accommodation/base registers;
- search cluster decisions;
- search site ABC;
- search later supersedes;
- if already decided, present it as a fact/constraint, not as a new question.

## 13. TRUE USER / LIVE-BOOKING BOUNDARIES

The following are genuine user/live/external boundaries rather than unfinished discovery:
- exact final property choice inside still-unlocked bounded zones (e.g. Rishikesh, Vrindavan, Bodh Gaya, Agra), when Mark preference between actual properties is required;
- live availability/price acceptance and actual booking;
- Sri Ramanasramam/Haidakhan/retreat acceptance where the property/institution must confirm;
- future train/flight timetable and class availability when the booking window publishes the exact Dec-2026/Jan-2027 service;
- exact Google Maps place closure where public evidence remains insufficient after the completed QA and a guessed coordinate would violate GEO governance.

Everything else that is safely derivable from repository canon should be executed without returning the historical questions to Mark.
