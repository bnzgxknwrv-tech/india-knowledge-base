# STATUS — INDIATURQUOISE-ALLPERSON-OVERLAP-001

state: COMPLETE
branch: agent/indiaturquoise-allperson-overlap
owner: INDIA TURQUOISE
mode: integration_not_blind
completed_at: 2026-08-19

outputs:
- runs/active/INDIATURQUOISE-ALLPERSON-OVERLAP-001/ALL_PERSON_CITY_OVERLAP.md
- runs/active/INDIATURQUOISE-ALLPERSON-OVERLAP-001/ALL_PERSON_EXACT_OVERLAP.md
- runs/active/INDIATURQUOISE-ALLPERSON-OVERLAP-001/PROVISIONAL_CLUSTER_SHORTLIST.md
- runs/active/INDIATURQUOISE-ALLPERSON-OVERLAP-001/COVERAGE_WARNINGS.md

constraints_respected:
- no new person-location research
- no A/B/C choices made for Mark
- Arunachala/Tiruvannamalai retained as LOCKED_BY_MARK A-anchor
- Babaji cave Kukuchina/Dunagiri retained as principal travel reason
- no route/nights/hotel choice
- no PDF
- no merge/PR

integration_note: counts are conservative MIN_CONFIRMED_COUNT values. Core-Kriya uses completed reconciled layers; NKB/Ram Dass use their current completed external reconciliation but remain unsaturated; Ramana/Ramakrishna multidetector reconciliation remains pending; Yogananda/Hariharananda/Vivekananda/Anandamayi rely on durable internal/targeted layers with explicit coverage warnings.

next_allowed_step: downstream heatmap/route-prep agents may consume these outputs as provisional integration layers, preserving COVERAGE_WARNINGS and without converting them into Mark decisions.
