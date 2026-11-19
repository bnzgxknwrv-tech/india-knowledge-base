# INCIDENT — HAIDAKHAN LOCAL KAILASH SUMMIT CLASSIFICATION LEAK

Status: CONFIRMED PROCESS DEFECT / OPEN MARK CLASSIFICATION
Date reconstructed: 2026-09-13
Branch: agent/india8-cluster-casting

## Bottom line

The local Haidakhan/Kumaon Kailash summit meditation site was not rejected by Mark and was not graded B/C. It was researched as relevant to the 2026-27 trip, but it never received its own physical candidate/inventory record and therefore never reached the mandatory Mark classification gate. It subsequently disappeared from later A/A+ ledgers and Mark-facing PDFs.

This is a classification-pipeline defect, not a Mark decision.

## Reconstructed chronology

### 2026-07-10 — Haidakhan itself graded A
Mark explicitly selected Haidakhan Vishwa Mahadham/Ashram as A. Duration remained open.

### 2026-07-10 — separate Kailash inquiry
Mark separately made Kailash a central investigation topic and explicitly requested the local Haidakhan/Kumaon Kailash layer, sacred points, mountain walks/hotspots and whether there was a spiritual high point near the existing route.

The research at that time already distinguished two separate Haidakhan physical places:
- the cave/gufa associated with Babaji's appearance;
- a separate local Kailash summit / summit-temple meditation place associated in the Haidakhan tradition with a prolonged meditation period (later reconciled as 45 days).

The summit/walk was left UNGRADED / operationally unverified. It was not rejected.

### 2026-07-11 — Issue #1 structurally forbade grading
Issue #1 `Onderzoek: Kailash-laag rond huidige India-route` explicitly instructed the researcher to investigate the Haidakhan-local Kailash, reachable walks/temples/sacred points and winter visitability, while assigning NO A/B/C grade.

The closing conclusion explicitly said:
- relevant this trip: local Haidakhan-Kailash layer;
- mountain walk only after local winter verification.

Thus the only unresolved point was operational/winter feasibility, not content relevance.

### 2026-07-11 — handoff failure
The same continuity commit recorded the local Haidakhan-Kailash layer as relevant to this trip in `CURRENT_FOCUS.md` and `CHATGPT_HANDOFF.md`, but `CLUSTER_LOCATIONS.md` contained only one Haidakhan inventory entity: #46 Haidakhan Babaji Ashram.

The summit did not receive its own candidate number/entity.

Because classification required physical candidates to pass through Mark, the summit therefore had no route into `LOCKED_A.md`, `LOCKED_B.md`, or `LOCKED_C.md`.

### Later — cave survives, summit disappears
Later re-audits split the Haidakhan world into at least:
- KUM-01 Haidakhan Vishwa Mahadham/Ashram;
- KUM-02 historic Haidakhan cave/gufa.

Both eventually became A+ in the frozen A79 ledger.

But the local Kailash summit / summit-temple / 45-day meditation place was never restored as its own physical entity. The broad phrase `Haidakhan-Kailash layer` was effectively flattened into the ashram/cave world. The summit's distinct biographical event was therefore absent from A79 and PDF v3.

## Root cause

Pipeline gap:

`research discovery -> marked relevant to this trip -> NO PHYSICAL CANDIDATE ENTITY -> NO MARK CLASSIFICATION -> omitted from later locked ledger`

The defect was enabled by two process choices occurring together:
1. the Kailash research task correctly forbade the researcher from grading on Mark's behalf;
2. there was no mandatory post-research gate requiring every material discovered physical place to be converted into a separately reviewable Mark candidate before the research issue could be closed.

## Classification status now

The summit is NOT historically A/B/C. It is an UNGRADED MISSED CANDIDATE.

Do not backfill an A/A+ grade autonomously. Only Mark may classify it.

However, it is now mandatory to present it to Mark as a separate physical candidate because:
- Mark explicitly called the local Kailash layer a central inquiry topic;
- the 2026-07-11 closure already said the local Haidakhan-Kailash layer was relevant to this trip;
- the summit carries a distinct Haidakhan-Babaji biographical event and is not the same place as the cave/gufa;
- the remaining operational question is winter/trail feasibility, not whether the place exists as a spiritually meaningful candidate.

## Candidate identity to preserve

Working label:
`Haidakhan local Kailash summit / summit temple — prolonged meditation and early teaching place`

Must remain a separate physical entity from:
- Haidakhan Vishwa Mahadham/Ashram;
- historic Haidakhan cave/gufa.

Do not merge these three into one broad `Haidakhan world` for classification or Mark-facing explanation.

## Prevention rule

Any research task that is forbidden to grade must still emit every material physical discovery into a `NEEDS_MARK_CLASSIFICATION` queue before the research can be declared complete.

A research issue may not close merely with prose such as `relevant this trip`, `interesting local layer`, `winter-check later`, or `possible walk` if a distinct physical place is involved.

Mandatory closure check:
`EVERY_MATERIAL_DISCOVERED_PHYSICAL_PLACE_HAS_ENTITY_ID_AND_MARK_CLASSIFICATION_STATUS = YES`

Allowed statuses include `UNGRADED / NEEDS_MARK_CLASSIFICATION`; absence from the inventory is never an allowed substitute.

## Current repair state

- A012 cave-versus-summit distinction restored in `person-provenance/A012_HAIDAKHAN_KAILASH_SUMMIT_CORRECTION_2026-09-13.md`.
- This incident file records the historical classification leak.
- The summit still requires explicit Mark grading before it can be inserted into the locked A/A+ itinerary inventory.
