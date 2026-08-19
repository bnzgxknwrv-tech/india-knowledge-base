# STATUS — INDIATURQUOISE-TRAVEL-PRIORITY-HEATMAP-001

state: COMPLETE
branch: agent/indiaturquoise-allperson-overlap
owner: INDIA TURQUOISE
mode: post_overlap_synthesis_no_new_person_research

outputs:
- TRAVEL_PRIORITY_HEATMAP.md
- CLUSTER_FAMILIES.md
- HIGH_IMPACT_GAPS.md
- MARK_DECISION_QUEUE_DRAFT.md

constraints_respected:
- no new person-location research
- no A/B/C decisions made for Mark
- Arunachala/Tiruvannamalai remains LOCKED_BY_MARK A-anchor
- Kukuchina/Dunagiri Babaji cave remains principal travel reason
- no route, nights, hotels, bookings, PDF, merge or PR

key_method:
- conservative MIN_CONFIRMED_COUNT retained
- exact-site quality separated from city/regional overlap
- physical/logistics concentration inferred only from existing project grouping, not from new travel research
- high-impact uncertainty separated from NON_BLOCKING micro-site gaps
- later Mark questions bundled at cluster-family level to reduce unnecessary decision load

next_allowed_step:
- INDIA/Mark may use these outputs as decision-support input or wait for pending reconciliation/travel-ops layers; no autonomous A/B/C promotion from this task.
