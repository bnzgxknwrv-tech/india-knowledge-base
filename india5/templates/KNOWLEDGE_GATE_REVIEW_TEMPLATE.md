# KNOWLEDGE_GATE_REVIEW — sjabloon

Status: VERPLICHT vanaf 2026-08-02 (INDIA5-ARCH-HARDEN-002). Bij elke toekomstige
kennis/capability-gate (vergelijkbaar met de eerdere prose-kennistoets op PR #23) levert de
review zowel dit mensleesbare bestand als een machineleesbare `KNOWLEDGE_GATE_REVIEW.json`
(schema: `india5/schemas/knowledge_gate.schema.json`) op.

## Vaste onderwerpenlijst (minimaal, uit de eerdere kennistoets INDIA5-PR23-KNOWLEDGE-GATE-002)

Elk onderwerp krijgt een verdict (`PASS`/`FAIL`/`PARTIAL`/`NOT_APPLICABLE`), een
`evidence_path` (repo-pad + evt. commit-SHA, of letterlijk `NOT_PROVEN_IN_GITHUB`), en een
korte toelichting:

1. Mark's A/B/C-filosofie
2. Immutable numbering
3. Bestaande kandidatenlijst van de betrokken regio('s)
4. Accommodatie-/hotelbesluiten (LOCKED_BY_MARK enz.)
5. Discovery versus GEO-verificatie
6. Detectorbibliotheek-governance
7. Kandidaat-inflatie / differentiatietoets (WHY_THIS_ONE / WHY_NOT_THE_OTHERS)
8. Koepelkandidaat versus deelsite
9. Betekenis vóór GEO
10. Geen stilzwijgende keuze / escalatieregels
11. Saturation/coverage-bewijs
12. Taakarchitectuur zelf (india5/TASK_PROTOCOL.md-naleving)

## Eindoordeel

`overall_verdict`: `READY` / `NOT_READY` / `READY_WITH_CONDITIONS`. Bij
`READY_WITH_CONDITIONS`: expliciete, niet-lege lijst van voorwaarden.

## Waarom dit sjabloon bestaat

De eerdere kennistoets (comment 5159570769 op PR #23) was één lange prose-comment. Bruikbaar
voor een eerste, uitgebreide beoordeling, maar niet herhaalbaar of machinaal vergelijkbaar over
opeenvolgende gates heen. Dit sjabloon + schema maakt elke toekomstige gate-beoordeling
diffbaar: item-voor-item vergelijkbaar met de vorige gate, in plaats van opnieuw een hele
prose-tekst te moeten doorlezen om te zien wat er is veranderd.
