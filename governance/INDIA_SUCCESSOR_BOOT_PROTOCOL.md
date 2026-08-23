# INDIA SUCCESSOR BOOT PROTOCOL

Status: **BINDEND / HIGHEST OPERATIONAL BOOT AUTHORITY** voor INDIA10 en latere INDIA-regisseurs totdat dit bestand expliciet wordt superseded.
Ingevoerd: 2026-08-23 door INDIA9, na volledige centrale semantische read + repo-brede audit + CCI red-team.

## 1. Doel
Een opvolgende INDIA-regisseur moet aantoonbaar minstens de kennis van zijn voorganger erven plus alle nieuwe delta, zonder Mark eerdere beslissingen opnieuw te laten uitleggen en zonder iedere generatie miljoenen onveranderde oude bytes opnieuw in actieve context te laden.

## 2. Definitie 100% kennis
`KNOWLEDGE_READY: 100%` vereist VIER afzonderlijke gesloten poorten:

1. `SEMANTIC_KNOWLEDGE_COVERAGE: 100%`
   - alle betekenisvolle kennis in de gecertificeerde baseline is gedekt;
   - 100% van alle betekenisvolle delta sinds die baseline is inhoudelijk gelezen/geclassificeerd.
2. `INTEGRITY_COVERAGE: 100%`
   - baseline, manifests, branch/path refs, blobs en delta zijn mechanisch/hashmatig gesloten; geen onverklaarde gaten.
3. `AUTHORITY_RECONCILIATION: PASS`
   - actuele Mark-besluiten, locks, canon, active state, task state en supersedes zijn opnieuw tegen elkaar gelegd.
4. `FRESHNESS_GATE: PASS_FOR_CURRENT_USE`
   - tijdgevoelige feiten die voor de actuele taak worden gebruikt zijn nog geldig of opnieuw gecontroleerd.

`KENNIS GEKEND` is niet hetzelfde als `FEIT NOG ACTUEEL`. Een visumregel, beschikbaarheid, treinregeling, openingstijd of hotelstatus kan volledig gekend maar `RECHECK_DUE` zijn.

## 3. Baseline + delta — standaard voor iedere opvolger
Wanneer `governance/KNOWLEDGE_BASELINE_LATEST.md` valideert:

1. Verifieer baseline cutoff, frozen branch/path universe en genoemde manifests/hashes.
2. Freeze de HUIDIGE volledige branch-tipset vóór delta-analyse.
3. Vergelijk huidige branch/path refs tegen de gecertificeerde baseline. Delta omvat verplicht:
   - nieuw bestand/pad;
   - gewijzigde blob op bestaand pad;
   - verwijderd pad/bestand;
   - rename/move;
   - nieuwe branch;
   - verwijderde branch/ref;
   - moved branch tip;
   - dezelfde blob op een nieuw pad wanneer dat pad authority/scope/currentness kan veranderen;
   - nieuwe of gewijzigde PR #23 relay/state sinds de baseline-receipt;
   - gewijzigde binary/PDF;
   - gewijzigde classificatie, supersede, decision of authority-relatie.
4. Classificeer iedere nieuwe/gewijzigde relevante branch/path-ref én iedere verwijdering/authoritymutatie. Een blob-SHA-union alleen is onvoldoende: paden en refs dragen zelf betekenis.
5. Lees 100% van de werkelijk unieke semantische delta inhoudelijk. Voor verwijderingen/moves moet expliciet worden vastgesteld of betekenis/provenance/authority verloren of verplaatst is.
6. Lees daarnaast ALTIJD opnieuw de actuele authority-set uit §5.
7. Reconcileer conflicts/supersedes.
8. Controleer vlak vóór een nieuwe baseline-certificering nogmaals of branch tips/PR-state sinds de freeze zijn gewijzigd. Zo ja: delta opnieuw sluiten.
9. Pas als alle vier poorten uit §2 sluiten: `KNOWLEDGE_READY: 100%`.

Ongewijzigde semantische broninhoud die door de gecertificeerde baseline aantoonbaar is gedekt hoeft NIET iedere opvolger opnieuw woord voor woord te lezen.

## 4. Full-bootstrap fallback — hard
Als één van deze dingen niet valideert, vervalt de snelweg:
- baseline pointer/cutoff ontbreekt;
- frozen branch/path universe of manifest kan niet worden bewezen;
- huidige branch-tipset kan niet exhaustief worden gefreezed;
- semantische delta inclusief deletions/moves/ref changes kan niet exhaustief worden bepaald;
- precedence/supersede staat is inconsistent;
- beschermde canon ontbreekt of conflicteert;
- een bronclassificatie is niet verantwoord reproduceerbaar.

Dan geldt: gecontroleerde volledige semantische bootstrap van alle betekenisvolle project-/broninhoud, met mechanische accounting. Nooit doen alsof een onbewijsbare baseline geldig is.

## 5. Authority-set — ELKE sessie opnieuw lezen/reconciliëren
Minimaal:
- `README.md`;
- dit protocol;
- `governance/ACTIVE_FRAMEWORK.md`;
- `governance/PRECEDENCE_MAP.jsonl`;
- `governance/CENTRAL_INTEGRATION_REGISTRY.jsonl`;
- `governance/SEMANTIC_IMPORT_REGISTRY_2026-08-23.jsonl` en latere opvolgers daarvan;
- `governance/KNOWLEDGE_BASELINE_LATEST.md` + nieuwste certification receipt;
- `governance/CCI_COLLABORATION_PROTOCOL.md`;
- `governance/INDIA_REGIE_CRITICAL_BOOT_AND_NO_DEFERRAL_2026-08-23.md`;
- `governance/INDIA_SESSION_START.md`;
- nieuwste expliciete `decisions/*` en Mark-besluiten/locks;
- protected canon, accommodation/base locks, cluster- en sitebesluiten;
- alle werkelijk actuele `runs/active/*/TASK.md` + `STATUS.md` die door ACTIVE_FRAMEWORK / session state als live worden aangewezen;
- nieuwste relevante commits;
- PR #23 comments/envelopes ná de in de certification receipt genoemde laatste geziene relay-state.

Een bestand met naam `active` is niet automatisch actueel; authority komt uit precedence + explicit state.

## 6. Vier verplichte delta-klassen
Iedere nieuwe/gewijzigde betekenisvolle bronblob/path-ref krijgt exact één klasse:
1. `UNIQUE_SEMANTIC_NOT_CENTRALLY_REPRESENTED`
2. `SEMANTICALLY_REPRESENTED_IN_CENTRAL`
3. `HISTORICAL_INTERMEDIATE_SUPERSEDED`
4. `MECHANICAL_OR_REDUNDANT_SOURCE_ARTIFACT`

Klasse 1 moet inhoudelijk gelezen worden vóór 100%. Klasse 2 hoeft niet dubbel gelezen als representation bewijs sluit. Klasse 3 blijft provenance en mag actuele state nooit terugdraaien. Klasse 4 telt voor integrity maar niet voor actieve semantische context.

Deletions, renames, branch removals en authoritymutaties krijgen daarnaast een expliciete disposition (`NO_SEMANTIC_LOSS`, `MOVED_PRESERVED`, `SUPERSEDED`, `REQUIRES_REVIEW` of opvolger). Zij mogen nooit verdwijnen omdat er geen “nieuwe blob” bestaat.

## 7. Binary / PDF regel
Binaire artefacten hoeven niet generatie na generatie als base64 te worden herlezen wanneer:
- hun byte-identiteit is bewezen;
- eenmaal expliciet is vastgesteld dat geen unieke besliskennis uitsluitend daarin zit, OF hun semantische inhoud apart is vastgelegd.

Wijzigt de binary, of wordt hij als unieke inhoudelijke bron aangehaald, dan moet de semantische controle opnieuw.

## 8. `AL BESLIST?` — voor ELK item vóór presentatie aan Mark
Controleer:
- al A/B/C?
- `LOCKED_BY_MARK` of andere beschermde beslissing?
- later besluit dan huidige bron?
- parent/microsite van bestaand beoordeeld complex?
- al reserve/afgewezen/provisional?
- bestaande gekozen slaapbasis/hotel?
- actuele route/tijdregel die presentatie verandert?

Bij JA: niet als nieuwe keuze presenteren. Alleen de echte nieuwe delta melden.

## 9. Mark is geen koerier
INDIA schrijft CCI-opdrachten rechtstreeks naar het afgesproken GitHub-relaykanaal en leest resultaten daar terug. Vraag Mark nooit projectgeschiedenis opnieuw te plakken als GitHub die bevat.

## 10. Multi-turn circuit breaker — hard
Past de Knowledge Boot niet veilig in één chatbeurt:
1. schrijf/werk bij `runs/active/<INDIAN>-BOOT-<DATE>/BOOT_PROGRESS.md`;
2. leg exact vast: baseline cutoff, frozen current branch-tipset, aantallen/bytes, voltooide set, laatste afgeronde path/blob/ref, resterende set en poortstatus;
3. meld aan Mark: `KNOWLEDGE_READY: NEE — <exact percentage/status>`;
4. geef één letterlijke vervolgprompt voor de volgende beurt;
5. hervat volgende beurt vanaf het checkpoint; bewezen werk NIET opnieuw lezen;
6. bij hervatten eerst controleren of de frozen current branch-tipset intussen is veranderd; nieuwe beweging wordt extra delta, niet reden om bewezen werk te vergeten.

Geen inhoudelijke reisregie zolang KNOWLEDGE_READY niet 100% is.

## 11. No-deferral + self-replacement
Alles wat INDIA nu veilig zelf kan doen, wordt in dezelfde sessie uitgevoerd. Alleen Mark-only keuzes of echte externe blockers mogen open blijven.

Iedere nieuwe Mark-beslissing, correctie, precedencewijziging, blocker, taakstatus, integratie of volgende uitvoerbare toestand wordt in dezelfde sessie duurzaam in GitHub vastgelegd. De volgende chat mag de vorige chat niet nodig hebben.

## 12. Completion is dimensioneel
Gebruik nooit één generiek `COMPLETE`/`SATURATED` als universeel eindpunt. Houd minimaal apart:
- discovery/corpus coverage;
- person-reverse coverage;
- physical identity/dedup;
- geocode/proximity;
- permanent-ID state;
- Mark review state;
- worker-output state;
- central-integration state;
- travel-readiness;
- route-lock;
- academic/person saturation.

`WORKER_COMPLETE != CENTRALLY_INTEGRATED != TRAVEL_READY != PERSON_SWEEP_SATURATED`.

## 13. Freshness
Tijdgevoelige records dragen waar relevant `last_verified`, `recheck_due` en/of `REVALIDATE_BEFORE_USE`. Oude kennis blijft provenance maar mag na de due-grens niet operationeel worden gebruikt zonder hercontrole.

## 14. Baseline-evolutie en cutoff — geen self-reference
Iedere opvolger erft:
`vorige gecertificeerde baseline + 100% semantische delta + actuele authority reconciliation`.

Een baseline mag niet proberen zijn eigen uiteindelijke commit-SHA in zijn eigen inhoud op te nemen. Gebruik daarom een expliciete `knowledge_cutoff_commit`: de laatste inhoudscommit die volledig semantisch is gesloten vóór de certification commit. De certification commit zelf en alles daarna vallen voor de opvolger gewoon in de volgende kleine delta.

Een nieuwe baseline mag pas `CERTIFIED` worden nadat alle gates sluiten, de post-freeze delta opnieuw is gecontroleerd en bewijs/manifests duurzaam zijn vastgelegd.

## 15. Auditpackaging
Lossless streams, review-pages, base64-PDF-chunks en andere auditderivaten zijn bewijs/verpakking. Zodra bronidentiteit en afleiding hashmatig bewezen zijn, zijn zij geen verplichte actieve-context-reread voor opvolgers. Een wijziging in packaging-classificatie zelf is wel authority/integrity-delta en moet worden verantwoord.

## 16. CCI-reviewbewijs vóór final certification
Een final successor-certificering vereist een duurzaam receiptbestand met minimaal:
- CCI review task/result-id;
- reviewed candidate head;
- validator preflight result;
- protected-canon result;
- audit-provenance result;
- post-freeze-delta result;
- findings en hun dispositions;
- `SAFE_TO_CERTIFY_AFTER_FIXES`.

De final validator moet dit receipt controleren. Een los woord `PASS` in een handoff is onvoldoende.

## 17. Minimale succesvolle boot-output
Voor inhoudelijk werk begint moet de opvolger expliciet kunnen vaststellen:
- `SEMANTIC_KNOWLEDGE_COVERAGE: 100%`
- `INTEGRITY_COVERAGE: 100%`
- `AUTHORITY_RECONCILIATION: PASS`
- `FRESHNESS_GATE: PASS_FOR_CURRENT_USE` (voor de actuele taak)
- `KNOWLEDGE_READY: 100%`

Zo niet: verder booten/checkpointen; niet adviseren.
