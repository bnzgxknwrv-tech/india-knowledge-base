# STATUS — INDIAWIT-HERITAGE-STAY-OVERRIDE-001

state: COMPLETE
branch: agent/indiawit-master-travel-readiness
owner: INDIA WIT
scope: heritage-stay candidates + room-level/current existence/bookability + hotel override review only
completed_at: 2026-08-19

outputs:
- HERITAGE_STAY_CANDIDATES.md — commit `5f3c49982b00a3cf880c5033bd05568154ceaa95`
- ROOM_LEVEL_LEADS.md — commit `79264149d2e776699aac043023d9610831c1d7f2`
- CURRENT_EXISTENCE_AND_BOOKABILITY.md — commit `33036b8e4b564dac0be4b8cc20fc0c2e93d844ce`
- EXISTING_HOTEL_OVERRIDE_MATRIX.md — commit `fe2da4a5d1824c2df02a5fee10f45df0c7ecaee8`
- MARK_HOTEL_REVIEW_QUEUE.md — commit `c5f7029581e248779aeeab3acc3b08e4ff4de432`

key_findings:
- Existing Varanasi lock `Sahi River View Guesthouse` remains LOCKED_BY_MARK and unchanged.
- Anandamayi Ma's Bhadaini Varanasi Ashram currently publishes explicit room-booking/dharamshala contacts and therefore creates `MARK_REVIEW_REQUIRED — HIGH-IMPACT-REVIEW` against the existing Varanasi lock, without replacing it.
- Hotel Evelyn in Nainital still operates and is a high-impact same-historic-hotel candidate for Ram Dass; his 1971 top-floor `cave` room is not yet mapped to a current room number.
- The Taj Mahal Palace in Mumbai remains operational/bookable and is a same-historic-hotel candidate for Yogananda; exact 1935 suite identity is unresolved.
- Sri Ramanasramam currently accepts devotee accommodation requests; historic Nirvana Room/caves are not bookable, and overnighting on the hill/in caves is prohibited. This is a high-impact same-complex stay review because Tiruvannamalai remains LOCKED_BY_MARK A-anchor.
- Belur Math offers pilgrimage guest accommodation; Vivekananda's historic room itself is not bookable.
- YSS Ranchi guest accommodation is officially closed until early 2027 and needs exact-date recheck if Ranchi enters the route.
- Kainchi current booking search is contaminated by third-party/unofficial booking sites; only the official Shri Kainchi Hanuman Mandir Trust is accepted as authority. No historic Ram Dass/NKB room was marked bookable.
- No confirmed numeric historic room number was recovered; zero room numbers were invented.

constraints_respected:
- no broad new person-location sweep
- current web verification only for already-detected stay claims
- all investigated core-person layers represented, including unresolved lodging leads where identity is insufficient
- no room/floor/building continuity inferred without source
- no existing hotel lock changed
- no A/B/C decision made for Mark
- no hotel booking
- no PDF
- no merge/PR

blockers_downstream:
- Direct institution/hotel archive contact is needed for Hotel Evelyn historic room mapping, Taj 1935 suite identification, Kainchi historical room policy, Karar Ashram overnight policy and several other room-level leads.
- Ranchi reopening date is not exact enough yet for the Dec-2026/Jan-2027 trip.
- Some historic lodgings remain identity-unresolved and must not be matched to modern businesses by name similarity.

next_allowed_step:
- INDIA8/route layer may consume MARK_HOTEL_REVIEW_QUEUE only after route clusters/dates are chosen.
- For any selected cluster, resolve the small number of institution-specific factual blockers before asking Mark one compact hotel decision.
- Preserve Sahi River View Guesthouse as Varanasi LOCKED_BY_MARK unless Mark explicitly changes it.
