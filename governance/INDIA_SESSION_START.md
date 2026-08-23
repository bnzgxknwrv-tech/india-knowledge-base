# INDIA_SESSION_START — actuele bootstrap

Snapshot: 2026-08-23
Status: SUCCESSOR_ARCHITECTURE_CANDIDATE_PENDING_FINAL_CCI_REDTEAM

## LEES EERST

1. `README.md`
2. `governance/INDIA_SUCCESSOR_BOOT_PROTOCOL.md`
3. `governance/KNOWLEDGE_BASELINE_LATEST.md`
4. `governance/ACTIVE_FRAMEWORK.md`
5. `governance/PRECEDENCE_MAP.jsonl`
6. `governance/CENTRAL_INTEGRATION_REGISTRY.jsonl`
7. `governance/SEMANTIC_IMPORT_REGISTRY_2026-08-23.jsonl`
8. `governance/CCI_COLLABORATION_PROTOCOL.md`
9. `governance/INDIA_REGIE_CRITICAL_BOOT_AND_NO_DEFERRAL_2026-08-23.md`
10. `handoffs/INDIA9_TO_INDIA10_SUCCESSOR_READY_2026-08-23.md`

## KENNISSTATUS VAN DE OVERDRACHT

Frozen audit-universe: 54 branch tips.
Repo-wide integrity accounting: compleet.
Werkelijk unieke branch-only semantische restset: 62 bestanden / 344.876 bronbytes.
INDIA9 semantic review van die restset: 62/62 compleet.
Protected ZILVER canon/integratiebundle: byte-identiek opgenomen op de successor integration branch.

De opvolger gebruikt na definitieve certificering:
`gecertificeerde baseline + 100% semantische delta + actuele authority reconciliation + freshness`.

Geen inhoudelijke regie vóór:
- `SEMANTIC_KNOWLEDGE_COVERAGE: 100%`
- `INTEGRITY_COVERAGE: 100%`
- `AUTHORITY_RECONCILIATION: PASS`
- `FRESHNESS_GATE: PASS_FOR_CURRENT_USE`
- `KNOWLEDGE_READY: 100%`

## CURRENT FRAMEWORK

Centrale regiebranch: `agent/india8-cluster-casting` zolang geen expliciete branchmigratie is gecanoniseerd.
Successor integration branch tijdens afronding: `agent/india9-successor-architecture-integration`.

`governance/ACTIVE_STATE.md` blijft historische/provenance-inhoud bevatten, maar de oude session labels/task snapshots daarin zijn niet automatisch live. `ACTIVE_FRAMEWORK` + `PRECEDENCE_MAP` + actuele Mark-besluiten/current task states bepalen authority.

## PROTECTED CANON

`runs/active/INDIAZILVER-ENTITY-ID-PROXIMITY-BACKFILL-001/PROTECTED_CANON_BASELINE.csv`
is hard protected.

Bestaande permanente locatie-IDs 001–081 en de beschermde A/B/C/lock-states mogen niet door staging, queues of worker-output worden gewijzigd.

`NEW_ID_REQUIRED_QUEUE.csv` en `ABC_REVIEW_AFTER_CLOSURE_QUEUE.md` zijn staging/review, geen definitieve nieuwe IDs of Mark-keuzes.

## CCI-SAMENWERKING

Standaard workflow:
`CCI worker/review -> INDIA integration branch -> validator -> CCI read-only red-team -> INDIA central fast-forward`.

CCI hoeft normaal niet rechtstreeks op de centrale regiebranch te schrijven.

Wanneer een CCI-task openstaat, controleert INDIA PR #23 zelf:
- bij iedere grote fase;
- vóór een lang/eindantwoord;
- vóór central fast-forward.

Mark is geen koerier.

## INCIDENTGUARDS

Voor ieder item vóór presentatie: `AL BESLIST?`.
Bestaande Mark A/B/C/locks/slaapbases worden niet opnieuw als nieuwe keuze aangeboden.
Wat INDIA veilig zelf kan uitvoeren, wordt niet onnodig uitgesteld.

## COMPLETION

Gebruik completion dimensioneel:
`WORKER_COMPLETE != CENTRALLY_INTEGRATED != MARK_REVIEWED != TRAVEL_READY != ROUTE_LOCKED != PERSON_SWEEP_SATURATED`.

## FRESHNESS

Tijdgevoelige informatie kan volledig gekend zijn maar toch `RECHECK_DUE` zijn. Voor operationeel gebruik opnieuw valideren wanneer vereist.

## SUCCESSOR-GATE

Zolang de handoff niet letterlijk `SUCCESSOR_ARCHITECTURE: PASS` vermeldt en de final validator niet PASS is, is INDIA10 nog niet definitief vrijgegeven.
