# LIVE CLOCK DELTA — DELHI ARRIVAL + 20/21/22 DEC NORTH REBUILD

Date: 2026-09-13
Status: **MARK-DIRECTED CLOCK DELTA / OUTRANKS OLDER DEC 19-22 SKELETON**
Branch: `agent/india8-cluster-casting`

## 19 DEC 2026 — DELHI ARRIVAL -> DLI STATION HOTEL -> 15013

International arrival:
- AI156 AMS -> DEL, working arrival ~10:15.

Mark's operating decision:
- after airport formalities/baggage, travel directly to a hotel **walkable to Old Delhi / Delhi Junction (DLI)**;
- use hotel as rest/baggage/safety base, not as sightseeing content;
- during afternoon Mark may calmly inspect station approach/entrance and the surrounding area, eat/rest/walk nearby;
- no late cross-city transfer to the train;
- walk from hotel to DLI well before train time.

Current 2026 timetable snapshot:
- 15013 Ranikhet Express reaches **Old Delhi / DLI ~21:50**;
- departs **~22:05** toward Kathgodam;
- current schedule reaches **Kathgodam ~05:05 on 20 Dec**.

Exact 19 Dec 2026 booked-train timetable/platform = `LIVE_RECHECK_LATER` when booking/current timetable is available. Current station anchor for hotel search is DLI, not NDLS.

## 20 DEC 2026 — KATHGODAM -> NAINITAL + A002 + A003

This day was previously underused. Mark explicitly pulls the old 21 Dec Nainital content forward.

Working rhythm:
- ~05:05 scheduled KGM arrival under current 15013 timetable;
- road transfer to Nainital / Hotel Evelyn;
- breakfast/bags/settling occurs naturally; no standalone `visit Hotel Evelyn` clock block;
- **A002 Naini Lake [A+]** during daytime at low tempo;
- **A003 Hanuman Garhi + Maharajji-kuti [A+]** late afternoon after the current 16:00 reopening;
- target sunset/presence window; 20 Dec 2026 astronomical sunset is ~17:17 local;
- return/evening free.

Feasibility note:
Current Hanuman Garhi public listing gives daily 05:00-12:00 and 16:00-21:00. The late-afternoon placement is therefore materially better than treating it as a random daytime stop.

## 21 DEC 2026 — FULL DAY RECOVERED

**STATUS: COMPLETE RECOVERED LOCAL DAY / DO NOT AUTO-FILL YET.**

A002 and A003 no longer consume 21 Dec.

This is a genuine full-day gain in the current trip architecture and must remain visible as such. Later day-plan reconstruction may assign the best remaining Kumaon content to it, but current PDF/content review must finish first.

`RECOVERED_DAY_21_DEC = YES`

## 22 DEC 2026 — KAINCHI DHAM -> BHUMIADHAR -> FREE

Mark's requested structure:
- depart Nainital early enough to be at **A004 Kainchi Dham at 08:00**;
- Kainchi Dham unhurried morning block;
- **13:00 depart Kainchi Dham**;
- continue directly to **A005 Bhumiadhar**;
- after Bhumiadhar, **rest of day free**.

Current geometry cues:
- Nainital -> Kainchi is roughly 17-20 km, typically ~45-70 min outside heavy traffic;
- Kainchi -> Bhumiadhar is roughly 12 km / ~25 min in current route guides;
- Kainchi current visitor timing source gives morning opening well before 08:00, so 08:00 is feasible subject to January live recheck.

### Why A004 + A005 are a good pair

They are both geographically and thematically coherent:
- same Nainital/Bhowali/Kainchi corridor rather than two unrelated excursions;
- Kainchi = central later Maharajji/Ram Dass guru-ashram world;
- Bhumiadhar = best-supported current location of the initial Ram Dass-Maharajji meeting / mother-spleen turning point;
- pairing them creates one coherent Maharajji/Ram Dass day while preserving free time after Bhumiadhar.

### Transport

Official Uber currently advertises Uber service in Nainital plus Reserve rides up to 30 days ahead. Do not interpret that as a guarantee of immediate onward pickup at Kainchi or Bhumiadhar in winter.

Robust execution preference:
`PREBOOK ONE PRIVATE DRIVER/CAR FOR NAINITAL -> KAINCHI -> BHUMIADHAR -> NAINITAL/BASE`.

Book via Hotel Evelyn/local operator or compare with Uber Reserve once the date opens. The same driver should wait/return rather than Mark depending on finding a new ride at each hill stop.

## Interaction with prior Tiru/Serampore work

This delta is a north-trip schedule repair only. It does not reopen A069/A070/A071; Mark explicitly keeps those A until the real later clock plan is tested.

`DEC20_BOTH_NAINITAL_A_PLUS_SITES = YES`
`DEC21_COMPLETE_DAY_GAIN = YES`
`DEC22_KAINCHI_0800 = YES`
`DEC22_KAINCHI_DEPART_1300_TO_BHUMIADHAR = YES`
`DEC22_AFTER_BHUMIADHAR_FREE = YES`
