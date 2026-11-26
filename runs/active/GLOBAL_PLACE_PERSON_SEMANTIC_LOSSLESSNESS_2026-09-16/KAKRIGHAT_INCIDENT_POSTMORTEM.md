# KAKRIGHAT INCIDENT POSTMORTEM

Task: PR #23 comment `5692870622`. Positive-control test result: **PASS**.

## WHAT HAPPENED

Kakrighat has been researched twice by two different, disconnected processes:

1. **`runs/active/TOP11-NKB-RAMDASS-V2-PRE-EXTERNAL-001/NEEM_KAROLI_BABA_V2_PRE_EXTERNAL_FREEZE.md`** (a PERSON-centric sweep, tracing every place connected to Neem Karoli Baba). Row 7 of its place table:

   > `Kakrighat | Almora-Nainital-weg, Uttarakhand (bij de Kosi-rivier) | tempel/heilige plek | Installatie van het Hanuman-beeld; gedeelde heilige plek met Sombari Baba en Panjabi Baba | JA | EXACT | nkbmeditation.org`

   Confirmed, sourced, `EXACT`. This says Kakrighat is where Neem Karoli Baba installed a Hanuman idol, and that it is a holy place shared with two other saints, Sombari Baba and Panjabi Baba.

2. **`research/INDIA20_ROUTEWIDE_KAKRIGHAT_TYPE_DETOUR_AND_MISSED_MAJOR_SITE_AUDIT_2026-09-13.md`** (a PLACE-centric audit, three days ago, explicitly asking "are there more places like Kakrighat"). Section A of that very file repairs Kakrighat's *Vivekananda* meaning (correcting an earlier `A*/SKIP_FIRST` misclassification) — but never mentions Neem Karoli Baba, Sombari Baba, or Panjabi Baba at all, despite the NKB sweep already existing in the repository.

3. `governance/CURRENT_TRUTH.md` (today) presents Kakrighat only as **"Kakrighat / Swami Vivekananda Jnana Vriksha [A+]"** — the Vivekananda layer survived; the Neem Karoli Baba/Sombari Baba/Panjabi Baba layer did not.

## WHY THIS PASSED UNDETECTED

Every mechanical check this project has run (coverage checksums, 79/86-row population checks, numbering validators) asks **"is the PLACE present, with a grade?"** — Kakrighat always answered yes to that question, because its Vivekananda layer was intact. None of those checks ask **"are all previously-discovered PERSON↔PLACE edges for this PLACE still visible?"** — that question was never mechanically asked at all, only researched by hand, in scattered files, by processes that don't cross-reference each other.

## CLASSIFICATION

`VALID_RESEARCH_NOT_INTEGRATED` + `PERSON_PLACE_EDGE_MISSING` (Neem Karoli Baba, Sombari Baba, Panjabi Baba edges, all present in repo research since before 2026-09-13, none present in current canon).

## ROUTE IMPACT

- Does not change the grade Mark already gave Kakrighat (A+) — but the *reason* Mark was shown was incomplete. Mark holds Neem Karoli Baba/Maharajji in his core person set (Kainchi Dham, Hanuman Garhi are already A+ for this exact reason) — this is not a minor tourist-trivia overlap, it's a second, independent A+-tier reason to value a stop that's already locked into the route on 23 Dec.
- Does not require any route/day change — Kakrighat is already visited on 23 Dec regardless.
- Does require Mark to see the fuller meaning, since a place's *why* materially affects how it should be presented and how much dwell/attention it deserves.

**MARK_DECISIONS_TO_REOPEN:** none need reopening in the sense of changing a grade or route — Kakrighat's A+ and its place in the 23-Dec schedule stay. What should happen is a **presentation repair**: Kakrighat's Mark-facing description should name both layers (Vivekananda's microcosm-macrocosm realization AND Neem Karoli Baba's Hanuman-idol installation, shared with Sombari Baba and Panjabi Baba), not just one.

END KAKRIGHAT INCIDENT POSTMORTEM
