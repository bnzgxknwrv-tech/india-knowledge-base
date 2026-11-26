# MARK-FACING PLACE CARD — TRAVEL VALUE / TOURISM-QUALITY PRESENTATION RULE

Date: 2026-09-13
Status: BINDING PRESENTATION RULE
Branch: agent/india8-cluster-casting

## Problem

Mark cannot make meaningful travel choices from cards that merely state category labels such as `major temple`, `sacred core`, `historic ashram`, `important ghat`, followed by logistics, queues, uncertainty or audit language.

A Mark-facing place card must read at least as informatively and compellingly as a serious tourism department / strong travel guide description, while remaining accurate and aligned to Mark's spiritual-person-centred trip.

## Required Mark-facing content order

For every place, before logistics or caveats:
1. **Recognition hook** — what uniquely distinguishes this place visually/experientially.
2. **Why it matters spiritually / historically / culturally** — not generic category words.
3. **What Mark actually experiences there** — e.g. darshan, room, cave, samadhi, ridge, aarti, silence, walk, old city lanes, food ritual, viewpoint.
4. **Why this may be worth Mark's finite trip time** — tied to person-life geography, sacred tradition, major travel experience, architecture, landscape or culture.
5. **Only then practical reality** — crowding, security, access, walking burden, timing, reservations, etc.

Do not lead with scepticism, proof language, queue burden or audit qualifiers unless a material wrong-place/wrong-person/access error would otherwise result.

## A026 example — Shri Kashi Vishwanath Temple

Old flat wording is insufficient:
`Major Jyotirlinga Shiva temple and living sacred core of Kashi... security and queues...`

Future Mark-facing presentation should make the actual travel value legible, for example:

**A026 — Shri Kashi Vishwanath Temple — Kashi's Golden Temple and one of the twelve Jyotirlingas [current grade unchanged]**

`The central Shiva shrine of Varanasi/Kashi: one of Hinduism's twelve Jyotirlingas and one of the city's defining pilgrimage destinations. The visit is not primarily about architecture; the core experience is entering the dense old-city sacred world and receiving darshan of the Vishwanath lingam — Shiva as 'Lord of the Universe' — inside the living ritual heart of Kashi. The present temple was rebuilt in 1780 by Ahilyabai Holkar and is recognizable by its gilded spires. For Mark, its value is the chance to experience one of India's strongest living Shiva pilgrimage sites from inside, amid active worship rather than as a museum monument.`

Practical reality may then follow separately:
`Very busy, security-heavy and potentially queue-intensive; exact darshan/aarti strategy can materially change the experience.`

## Decision-usability gate

A place card is not Mark-decision-safe unless Mark can answer from the card alone:
- What is special about this place?
- What will I actually see/do/feel there?
- Why might I personally care?
- What would I miss if I skipped it?
- What practical burden does it add?

If the first four cannot be answered without external research, the card has failed even if all factual fields are technically correct.

## HARD TIME-ACCOUNTING FIELDS — ADDED BY MARK 2026-09-13

Every location card that participates in an executable day/route must carry two separate time fields. These are **door-to-door / whole-human** values, not just nominal drive or visit duration.

### 1. `TOTALE TIJD VOOR DEZE LOCATIE`

Definition for current location `B`, previous itinerary anchor/location `A`, and next itinerary anchor/location `C`:

`TOTALE TIJD VOOR DEZE LOCATIE = reistijd A -> B + echte dwell/bezoektijd B + reistijd B -> C`

Rules:
- travel legs include relevant walking, station/ferry/parking/access transfer and realistic waiting/slack when materially part of the movement;
- for first/last item of a day, `A` or `C` may be the real sleep base, airport, station or other fixed anchor;
- for a sub-place within the same compound, the travel leg may be an internal walk rather than a separate transport journey;
- use a range when access/traffic/service uncertainty makes one exact number false precision;
- this is a **card-level burden field** and must NOT be blindly summed across adjacent cards because shared travel legs would otherwise be double-counted.

### 2. `TIJD VRIJGEMAAKT ALS DEZE GESKIPT WORDT`

This is the net time that disappears from the itinerary if location `B` is removed and `A` is connected directly to `C`.

Exact definition:

`TIJD VRIJGEMAAKT ALS B WORDT GESKIPT = reistijd A -> B + dwell B + reistijd B -> C - nieuwe directe reistijd A -> C`

Equivalent:

`= TOTALE TIJD VOOR DEZE LOCATIE - reistijd A -> C zonder B`

HARD consequence:
The field is NOT equal to dwell time and is NOT equal to `travel to B + dwell`. The direct predecessor-to-successor route must actually be recalculated.

Example only:
- A -> B = 25 min
- B dwell = 60 min
- B -> C = 30 min
- A -> C direct if B is skipped = 35 min

Then:
- `TOTALE TIJD VOOR DEZE LOCATIE = 1u55`
- `TIJD VRIJGEMAAKT ALS DEZE GESKIPT WORDT = 1u20`

### Recalculation guards

- If skipping B changes transport mode, ferry/train dependency, opening-window strategy, hotel return, luggage movement or another material route condition, recalculate the actual replacement chain rather than using simple map arithmetic.
- If A -> B -> C is itself a transport shortcut, skipping B may free surprisingly little time; the formula must expose that.
- If B is literally passed on the same corridor, the marginal time may be close to dwell only.
- If B requires an out-and-back detour, the freed time may be much larger than dwell.
- Never write `JE BENT ER TOCH`, `maar 10 minuten extra`, or a skip-saving number without this predecessor/current/successor comparison when the exact route matters.
- Exact future service schedules remain `LIVE_RECHECK_LATER`; use conservative current geometry/ranges until the travel date becomes bookable.

### Mark-facing display

When route geometry is known, show visibly:

`TOTALE TIJD VOOR DEZE LOCATIE: ...`
`TIJD VRIJGEMAAKT ALS DEZE GESKIPT WORDT: ...`
`BEREKENING: A -> B ... + B ... + B -> C ... - A -> C direct ...`

These two values are mandatory in the next decision-grade location-card/PDF layer wherever a predecessor and successor have been assigned.

## Scope

Apply this rule to all future India PDFs, summaries, overview cards, itinerary comparisons and successor sessions. It complements `MARK_PERSON_PROVENANCE_PLACE_MEANING_RULE.md`; it does not replace the person-provenance requirement.