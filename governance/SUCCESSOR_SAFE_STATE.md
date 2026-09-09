# INDIA SUCCESSOR SAFE STATE — CRASH-SAFE HANDOFF CHECKPOINT

STATUS: SAFE_TO_HANDOFF
Date: 2026-09-09
Branch: `agent/india8-cluster-casting`
Full handoff: `handoffs/INDIA_SUCCESSOR_ZERO_LOSS_HANDOFF_2026-09-09.md`

## CRASH RULE

`IF THIS CHAT ENDS NOW, CAN INDIA(N+1) CONTINUE WITHOUT ASKING MARK TO RECONSTRUCT STATE?`

Required answer: **YES**. If a later material Mark decision is not reflected here or in the full handoff, update GitHub before relying on chat memory.

## LATEST PHASE

**ROUTE TOPOLOGY + FULL A/A+ COVERAGE REOPENED FOR FINAL RECONCILIATION. NO BOOKING/CONTACT YET.**

Older files declaring `FINAL BOOKING CALENDAR LOCKED` and booking phase are superseded on that phase/status point by the 2026-09-09 reopen:
`decisions/FULL_A_COVERAGE_AND_GLOBAL_ROUTE_TOPOLOGY_REOPTIMIZATION_2026-09-09.md`.

## HARD ENVELOPE

- AI156: AMS->DEL, depart 18 Dec 2026 ~20:35, arrive 19 Dec ~10:15.
- AI155: DEL->AMS, depart 21 Jan 2027 ~12:20.
- exactly 33 physical India nights, 19 Dec through 20 Jan.
- exactly ONE final Delhi night immediately before AI155 `LOCKED_BY_MARK`.

## FINAL WORLD LOCK

IN: Delhi operational/Nirmal, Kumaon, Agra, Bodh Gaya, Varanasi/Sarnath, Kolkata/Dakshineswar, Tiruvannamalai/Arunachala, Chennai positioning/content if useful.

FINAL OUT — never re-present unless Mark explicitly reopens:
- Puri/Odisha;
- Serampore/Srirampur as trip world/stop/sleep/excursion;
- Vrindavan/Braj/Mathura/Govardhan.

## HARD DURATIONS / LIVE SENSITIVITY

Hard:
- Nainital 3n;
- Dunagiri/Kukuchina 3n;
- Haidakhan Vishwa Mahadham 3n + 2 complete protected quiet days;
- Agra 1 hotel night in retained architecture, Taj [A+] protected;
- Varanasi/Sarnath 8n `LOCKED_BY_MARK`;
- Kolkata/Dakshineswar current serious block 3n;
- final Delhi 1n.

Live current review:
- Bodh Gaya 3n strongly supported/current review surface; 2n comparison baseline.
- Tiruvannamalai 4n serious live option; old 5n state was explicitly reopened.
- Sri Chakra Puja is optional bonus, not a separate Mark-graded mandatory anchor; do not force Tiru5 because of it.

## NEWEST MARK DECISION — NIRMAL DHAM

Owner: `decisions/NIRMAL_DHAM_FINAL_DELHI_PLACEMENT_MARK_DECISION_2026-09-09.md`.

- Nirmal Dham remains IN and grade unchanged.
- **NOT on arrival day 19 Dec.**
- default **20 Jan final Delhi safety/buffer** after positioning into Delhi.
- if disruption consumes buffer, AI155 safety wins; Nirmal may be shortened/skipped operationally.
- 19 Dec is free to optimize for onward travel; do not penalize same-day GAY/VNS/CCU/MAA for missing arrival-day Nirmal.

## GLOBAL TOPOLOGY CHECKPOINT

Pre-Nirmal global test on `worker/global-route-topology-reoptimization`, commit `7c206ece6efee0f548e3b72ebf3022f3573282ca`, tested 11 route families.

Pre-override metrics:
- incumbent ~57 lost waking h; 2 heavy days; sleep ~4.0/5;
- same-day GAY ~55.5 h; 4 heavy days; sleep ~2.8/5;
- same-day VNS ~56 h;
- Agra-first ~58.5 h;
- Agra-last/reverse ~60 h;
- MAA-first ~64 h; CCU-first ~67 h; train-heavy ~75–82 h.

Pre-override verdict `KEEP INCUMBENT`, confidence ~0.70, is **NOT a final post-Nirmal verdict**. One disadvantage of GAY-first was later Nirmal staging and that constraint is now removed. Reconcile/rerun rather than blindly inherit.

### Corrected fact

Same-day DEL->GAY is NOT impossible. Air India official Winter Schedule 2026 publishes daily **AI429 15:00 DEL -> 16:40 GAY** effective 25 Oct 2026. After AI156 scheduled 10:15 arrival that is nominal ~4h45. Still test protection/terminal/immigration/bags/delay/fatigue.

### Agra insight

Agra current bridge has directional sleep value: Delhi->Agra is short, then 12988 Agra Fort ~18:45 -> Gaya ~07:50 can convert ~8–8.5 h into sleepable rail. Reverse Gaya->Agra is daytime-heavy. Agra-last tends to duplicate Delhi->Agra->Delhi. Preserve this reasoning in any new solve.

## A/A+ COVERAGE — OPEN BLOCKER

The 22-page BODH3/TIRU4 review itinerary does not individually guarantee every retained A/A+ site. Known audit seed:
- missing: Bodh same-hill ridge/context; Maa Annapurna; Vishalakshi Gauri; Bhaskarananda/Anand Bagh; Saranganath; Tulsi Manas;
- conditional: Lahiri Mahasaya family house; Shitala Mata;
- hidden under Sarnath: Dhamek, Mulagandha Kuti Vihara, Chaukhandi, Deer Park;
- special: Karkrighat [A*/SKIP_FIRST].

Full exact audit still required; avoid parent-child double counting. Never claim the seed is the final exact omission count.

## SIX EXTERNAL AIs — READY FOR RECONCILIATION

Six independent blind route analyses are complete. They must be reconciled, not majority-voted.
- evidence > majority;
- minority finding may be right;
- verify factual conflicts;
- synthesize a seventh route if stronger;
- prove 33/33;
- inject Nirmal-final-buffer rule even if the six answers predate it.

## DAY-PLAN USABILITY RULE

Mark likes the current 22-page review format. Next itinerary must show each retained physical A/A+ individually with:
- full recognizable name;
- WHAT it is;
- WHY Mark wanted it / relevance;
- current grade/status;
- exact date/time block.

Do not hide required sites under vague cluster labels when judging duration.

## EXACT NEXT ACTIONS

1. Reconcile the four external AI route analyses with new Nirmal placement (corrected count; an earlier pass said six in error — see `runs/active/INDIA18_FINAL_EXTRACTION_2026-09-09.md` §13.1).
2. Compare synthesis with CCI/Work; rerun top contenders if Nirmal change could alter rank.
3. Finish exact full A/A+ current-canon coverage matrix.
4. Build complete waking-hours itinerary with every retained A/A+ explicit.
5. Let Mark judge remaining duration/fit.
6. Only then reopen bookings/contacts.

## GUARDS

- Mark alone owns subjective A/A+/A*/B/C grades and personal choices.
- no silent grade/lock changes.
- no FINAL OUT resurrection.
- no premature booking.
- future operational claims verified or `LIVE_RECHECK_LATER`.
- PR #23 is CCI/Work relay.
- material knowledge must not remain chat-only.

For the complete reasoning and context, read `handoffs/INDIA_SUCCESSOR_ZERO_LOSS_HANDOFF_2026-09-09.md`.

UNSAVED_RISK:
GEEN

END SUCCESSOR SAFE STATE
