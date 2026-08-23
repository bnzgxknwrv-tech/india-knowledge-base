# INDIA — START HIER

## HIGHEST BOOT AUTHORITY — INDIA10+

Lees als eerste:
`governance/INDIA_SUCCESSOR_BOOT_PROTOCOL.md`

Dat protocol is vanaf 2026-08-23 de hoogste operationele bootautoriteit voor een nieuwe INDIA-regisseur totdat het expliciet wordt superseded.

## Waarom dit veranderd is

De eerdere regel dwong iedere opvolger opnieuw de volledige repository en alle relevante legacybranches woord voor woord te lezen. Dat voorkwam kennisverlies, maar veroorzaakte contextvervuiling, enorme herhaalkosten en vergrootte de kans dat oude snapshots opnieuw als actuele waarheid werden behandeld.

INDIA9 + CCI hebben daarom de volledige toenmalige 54-branch-universe mechanisch geaudit en de werkelijk unieke branch-only kennis semantisch gesloten. De gecertificeerde opvolgersmethode is nu:

`GECERTIFICEERDE BASELINE + 100% NIEUWE/GEWIJZIGDE SEMANTISCHE DELTA + ACTUELE AUTHORITY RECONCILIATION + FRESHNESS = KNOWLEDGE_READY 100%`

Een volledige semantische repo/bootstrap blijft de harde fallback wanneer de baseline of delta niet bewijsbaar valideert.

## Verplichte startvolgorde

1. `governance/INDIA_SUCCESSOR_BOOT_PROTOCOL.md`
2. `governance/KNOWLEDGE_BASELINE_LATEST.md`
3. `governance/ACTIVE_FRAMEWORK.md`
4. `governance/PRECEDENCE_MAP.jsonl`
5. `governance/CENTRAL_INTEGRATION_REGISTRY.jsonl`
6. `governance/SEMANTIC_IMPORT_REGISTRY_2026-08-23.jsonl` en eventuele latere opvolgers
7. `governance/CCI_COLLABORATION_PROTOCOL.md`
8. `governance/INDIA_REGIE_CRITICAL_BOOT_AND_NO_DEFERRAL_2026-08-23.md`
9. `governance/INDIA_SESSION_START.md`
10. nieuwste successor handoff onder `handoffs/`
11. actuele authority-set/delta volgens het successor protocol

Pas inhoudelijk handelen als alle verplichte knowledge gates sluiten.

## Harde kennispoort

Voor inhoudelijk werk moet de regisseur kunnen vaststellen:
- `SEMANTIC_KNOWLEDGE_COVERAGE: 100%`
- `INTEGRITY_COVERAGE: 100%`
- `AUTHORITY_RECONCILIATION: PASS`
- `FRESHNESS_GATE: PASS_FOR_CURRENT_USE` voor de actuele taak
- `KNOWLEDGE_READY: 100%`

Past booten niet in één beurt: checkpointen en exact hervatten. Geen inhoudelijke regie op halve kennis.

## Authority en oude bestanden

`governance/ACTIVE_STATE.md`, oude `pipeline/`, `india4/india5`, oudere handoffs, workerbranches en historische taskfiles blijven als provenance bestaan. Hun aanwezigheid maakt ze niet automatisch actueel.

Gebruik `ACTIVE_FRAMEWORK.md` + `PRECEDENCE_MAP.jsonl` + expliciete actuele beslissingen om te bepalen welk deel nog autoriteit heeft.

Belangrijkste regel:
**nieuwste expliciete Mark-beslissing / LOCKED_BY_MARK / expliciete supersede wint altijd van aanbevelingen, queues en oudere snapshots.**

## Protected canon

De centraal beschikbaar gemaakte protected-canon/integratiebundle staat onder:
`runs/active/INDIAZILVER-ENTITY-ID-PROXIMITY-BACKFILL-001/`

`PROTECTED_CANON_BASELINE.csv` beschermt de bestaande permanente 001–081 en relevante legacy/accommodation states. Staging- en reviewqueues in dezelfde directory zijn geen definitieve nieuwe IDs en geen Mark-keuzes.

## CCI-samenwerking

Lees `governance/CCI_COLLABORATION_PROTOCOL.md`.

Standaard:
`CCI worker/review -> INDIA integration branch -> validator -> CCI read-only red-team -> INDIA central fast-forward`.

PR #23 blijft relay/index. Mark is geen koerier. Zodra INDIA een CCI-task heeft opengezet, controleert INDIA zelf PR #23 bij grote fasegrenzen en vóór lange/eindantwoorden.

## Centrale regiebranch

Huidige centrale regiebranch tijdens deze successor-migratie:
`agent/india8-cluster-casting`

Een opvolger verandert de centrale branchnaam niet stilzwijgend. Branchmigratie is een expliciete governancehandeling.

## No-deferral en `AL BESLIST?`

De incidentguards uit `governance/INDIA_REGIE_CRITICAL_BOOT_AND_NO_DEFERRAL_2026-08-23.md` blijven bindend:
- vóór ieder item: `AL BESLIST?`;
- beschermde keuzes niet opnieuw aan Mark voorleggen;
- wat INDIA nu veilig zelfstandig kan uitvoeren, niet als losse toekomstige stap parkeren;
- nieuwe relevante state/correcties duurzaam vastleggen.

## Auditprovenance

De INDIA9 repo-wide knowledge-audit is centraal gearchiveerd onder:
`archive/india9-knowledge-audit-2026-08-23/`

De auditpackaging is bewijs, geen tweede live stateboom. De originele worker-/legacybranches zijn niet verwijderd.

## Nieuwe sessie

Gebruik de actuele letterlijke startprompt uit:
`handoffs/INDIA9_TO_INDIA10_SUCCESSOR_READY_2026-08-23.md`

Als die handoff nog geen `SUCCESSOR_ARCHITECTURE: PASS` bevat, is de migratie nog niet gereed en mag geen verse INDIA als volledig overgedragen worden beschouwd.
