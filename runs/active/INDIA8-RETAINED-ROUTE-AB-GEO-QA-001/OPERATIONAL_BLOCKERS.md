# RETAINED ROUTE — OPERATIONAL BLOCKERS (high-impact only)

```
task_id: INDIA8-RETAINED-ROUTE-AB-GEO-QA-001
uitgevoerd_door: CCI
uitgevoerd_op: 2026-08-23
scope: Dec 19 2026 - Jan 20 2027 detailed schedule. High-impact only, no restaurant sweep,
       no route redesign.
```

## NEW — not previously flagged anywhere in the read repository

### B1. North India winter fog delays overnight/long-distance trains — HARD, affects the route's own core transport strategy

V2's headline efficiency gains rest on **three long overnight/evening train legs, all inside the
December-March North Indian fog season**: 19 Dec Delhi->Kathgodam, 4 Jan Mathura->Prayagraj,
5 Jan Prayagraj->Varanasi. None of the route/transport documents read (`WORKING_ROUTE_V2`,
`TRANSPORT_PREFERENCE_AND_EFFICIENCY_RULE_2026-08-23.md`, `TRIP_CALENDAR_RISK_LAYER.md`) mention
fog as a risk category at all.

Confirmed 2026 evidence: North Indian winter fog routinely delays Delhi-bound and UP/Bihar-corridor
trains by **up to 5-10 hours** in December-January, with East Central Railway (covering Bihar and
eastern UP -- i.e. exactly the Prayagraj/Varanasi/Gaya corridor) known to reduce or suspend services
on affected routes into late February in bad years. Delhi-NCR and the wider Uttar
Pradesh/Uttarakhand/Bihar belt are named as the most affected zones.

**Concrete consequence for this route**: the 19 Dec overnight train is designed to deliver Mark to
Kathgodam by ~05:05 so 20 Dec can start as a settling day rather than losing it to road transfer.
A fog-delayed arrival could remove that entire buffer. The 4-5 Jan Mathura->Prayagraj->Varanasi
chain is even more exposed: it is a same-day double-transfer (overnight train arriving ~04:50,
full sightseeing day, evening train to Varanasi) with **zero slack built in** for a multi-hour
morning delay.

`TRANSPORT_PREFERENCE_AND_EFFICIENCY_RULE_2026-08-23.md` already correctly says exact timetables
"are planning evidence, not booking locks" and must be revalidated -- but revalidating a train
*number* does not address fog risk, which is a same-day operational risk even for a correctly
booked train. Status: **TRANSPORT_CAUTION**. Recommend building an explicit fallback (e.g. accept
a compressed Prayagraj day, or hold the Varanasi evening train booking flexible) for the two
same-day double-transfer dates specifically, not just for booking-window revalidation.

### B2. Akshayavat / Patalpuri Temple sits inside an active Indian Army fort — access is not simple walk-in

Every current cluster/route file (`PRAYAGRAJ_MARK_DECISIONS_RECONCILED_2026-08-23.md`,
`WORKING_ROUTE_V2`) lists Akshayavat as a straightforward A visit alongside Triveni Sangam and
Bade Hanuman Ji. In reality, Akshayavat (the "indestructible banyan tree") sits inside **Patalpuri
Temple, itself inside Allahabad Fort, which remains an active Indian Army facility**. Multiple
current sources confirm visitors need **permission from the fort commandant/Indian Army office**
to enter that section; general fort timings (roughly 10:00-18:00, sources vary slightly) apply
only to the parts that are open at all, and access can tighten or loosen depending on military
activity or special events (some sources note Kumbh-period openings are wider than normal-year
access).

Status: **AVOID_IF_POSSIBLE without pre-arranged permission** -- not a hard closure, but treating
it as a normal drop-in stop (as the current route documents do) risks arriving on 5 Jan and being
turned away or delayed. Recommend the final trip guide add an explicit note to request/confirm
military-area access in advance, with a same-day Sangam/Hanuman Ji fallback plan if Akshayavat
access is denied that morning.

## ALREADY FLAGGED IN EXISTING CANON — reconfirmed, still valid, listed here for completeness per Task C's own requirement to surface every high-impact item

- **Taj Mahal closed Fridays.** Correctly handled: V2 deliberately places the Agra positioning
  night on Friday 1 Jan 2027 and the actual sunrise visit on Saturday 2 Jan. No action needed;
  reconfirmed correct.
- **Shivpuri-Rishikesh rafting has a seasonal closure window.** The CCI Lonely Planet North
  discovery sweep found normal season is roughly Sep-Jun with a locally-reported monsoon closure
  (reopening ~mid/late September). The trip's 29-31 Dec window falls inside the open season, so
  this is **not** a live blocker for these dates -- confirmed OK_NORMAL, but the seasonal
  dependency itself is worth restating since rafting was found silently dropped from V2's
  day-by-day list (see the companion `RETAINED_ROUTE_AB_CANON_QA.md`, finding 2).
  - Related access note that still stands: 2026 traveler reports flag construction/access
    problems at Beatles Ashram specifically (poor value, inaccessible buildings, March-April 2026
    reviews). V2 keeps Beatles Ashram as A-light without repeating this caution -- recommend
    re-verifying on-the-ground state closer to the visit date rather than assuming it has been
    fixed.
- **Sri Ramanasramam on-site accommodation is not guaranteed.** `PROVISIONAL_ROUTE_CALC_BASES_2026-08-23.md`
  itself states rooms are limited and "acceptance is not guaranteed" for foreign devotees who
  apply in advance. This is a genuine live booking-dependent blocker, already correctly flagged
  with a fallback (Rainbow Guest House / Ramana Nagar) in the same file.
- **Parmarth Niketan New Year participation is not yet confirmed/locked.** Already flagged in
  `WORKING_ROUTE_V2` as "first-choice... if booking/participation is accepted," with the
  understanding that New Year's Eve in Rishikesh will be extremely busy regardless of which
  specific ashram/venue is used.
- **Tamil Pongal period, 14-17 Jan 2027, overlaps the Tiruvannamalai module.** Already flagged in
  both `WORKING_ROUTE_V1` and `WORKING_ROUTE_V2` as a calendar caution (added cultural value, but
  also higher domestic travel demand and altered hours). No new evidence found that changes this
  assessment.
- **Girivalam monthly full-moon (Pournami) crowd day correctly avoided.** V1 explicitly notes the
  January 2027 Pournami falls around 22 Jan, after Mark's 21 Jan departure -- the current route
  therefore does NOT place Girivalam on the single most crowded day of the month. This is good
  planning, reconfirmed, not a blocker.
- **All exact train numbers/times throughout V2 are explicitly marked "planning patterns," not
  booking locks**, and must be revalidated for the actual Dec-2026/Jan-2027 timetable before
  booking. Reconfirmed as the correct posture; not re-litigated here.

## Checked and found to be non-issues this pass

- No Indian national public holiday falls inside 19 Dec 2026 - 20 Jan 2027 that independently
  changes transport operations beyond the items already listed above (Christmas/New Year in India
  are not blanket transport-affecting public holidays the way they are in some countries).
- Makar Sankranti (~14-15 Jan 2027 in most of North India) falls while Mark is in the Bodh
  Gaya/Gaya module (11-13 Jan) or in transit to Tiruvannamalai (14 Jan) -- it does not add crowd
  pressure to the Varanasi or Prayagraj river-confluence visits, which are already completed by
  10 Jan. No additional action needed beyond the Pongal flag already carried (Pongal is Tamil
  Nadu's regional form of the same solar-calendar festival, already flagged above).

---
Geschreven door: CCI. High-impact operational items only, no restaurant sweep, no route redesign,
no A/B/C changed.
