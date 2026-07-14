# SUBREGIE INDIA — technische eindvalidatie

run_id: VRINDAVAN-SUPPLEMENT-001
validated_role: GOUD
validated_status: PARTIAL
worker_completioncommit: 41d6f7dd326df6daa0afae8d9fba646ff3870825
artifact_commit: 85127c2bd35fe9bb8010a5b76eb676f749e748ec
technical_integrity: PASS
validated_at: 2026-07-14T08:08:00+02:00

## Validatie

- `state.yaml` en `events.jsonl` zijn synchroon op `EVT-0013`.
- De run staat op `GOUD_PARTIAL`; er is geen actieve rol en geen actieve claim.
- Manifest, `COMPLETED`, handoff en decision stemmen overeen op status `PARTIAL`.
- Alle verplichte GOUD-artifacts bestaan en bevatten de eindsentinel.
- De uitvoering bleef beperkt tot exact de vijf gepinde Vrindavan-blockers.
- Alle zeven claimverwijzingen resolven naar unieke accepted of rejected source-ID's.
- De acht bestaande kandidaten, grenzen en onzekerheden zijn behouden.
- Geen A/B/C-status, rangorde, route-, verblijf- of prijsadvies is toegevoegd.
- Geen archivering is uitgevoerd.

## Eindbesluit

De aanvullende GOUD-uitkomst is technisch betrouwbaar en mag naar INDIA2 voor inhoudelijke verwerking. `PARTIAL` is de correcte status: de vijf vragen zijn scherper afgebakend, maar geen van de vijf is volledig gesloten op het vereiste bewijsniveau.

## Routering

Volgende bestemming: INDIA2.
Regisseurspakket: `research/active/VRINDAVAN-SUPPLEMENT-001/transitions/INDIA2_REGISSEUR_PACKAGE.md`.

END_OF_ARTIFACT