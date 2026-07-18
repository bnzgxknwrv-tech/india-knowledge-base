# Execution Protocol v2.3.1

## 1. Repository-only handoff

Een chat is een tijdelijke worker. Alle blijvende invoer, voortgang en uitvoer staat in GitHub. BRONS, ZILVER en GOUD communiceren niet via geplakte onderzoeksrapporten. Een geplakte rolhandoff bevat alleen bediening en GitHub-pointers.

## 2. Runstatus en protocolpins

Iedere run bevat:
- `run.yaml` — onveranderlijke run-identiteit, scope en protocolpins;
- `state.yaml` — actuele afgeleide toestand;
- `events.jsonl` — append-only gebeurtenissen;
- een definitief contextmanifest voor de actieve of eerstvolgende uitvoerbare rol;
- één geïsoleerde outputmap per fase.

`run.yaml` verandert niet nadat BRONS is geclaimd. Een wijziging vereist een nieuwe run of expliciete migratie.

Bij runcreatie bestaat alleen een definitief `BRONS_CONTEXT.yaml`. `ZILVER_CONTEXT.yaml` en `GOUD_CONTEXT.yaml` worden pas na predecessorvalidatie door een controllertransition gegenereerd.

Nieuwe inline-handoffruns pinnen tevens:
- `pipeline/protocols/ROLE_HANDOFF_PROTOCOL.md`;
- `pipeline/templates/NEXT_ROLE_HANDOFF_TEMPLATE.md`;
- `pipeline/templates/MARK_FINAL_REPORT_TEMPLATE.md`;
- `pipeline/templates/CANONICAL_INTEGRATION_PROPOSAL_TEMPLATE.md`;
- `pipeline/templates/NEXT_ACTION_V3_TEMPLATE.yaml`.

Ontbreken deze pins, dan geldt het oude proces.

## 3. Toestanden

Toegestane fasevolgorde:

`READY_FOR_BRONS -> BRONS_CLAIMED -> BRONS_COMPLETE -> TRANSITION_TO_ZILVER_CLAIMED -> READY_FOR_ZILVER -> ZILVER_CLAIMED -> ZILVER_COMPLETE -> TRANSITION_TO_GOUD_CLAIMED -> READY_FOR_GOUD -> GOUD_CLAIMED -> GOUD_PASS|GOUD_PARTIAL|GOUD_BLOCKED -> ARCHIVED`

Een overgang is alleen geldig wanneer:
1. de verwachte vorige toestand klopt;
2. een corresponderend event wordt toegevoegd;
3. verplichte output voor de overgang bestaat en is gevalideerd;
4. voor `READY_FOR_ZILVER` of `READY_FOR_GOUD` het definitieve contextmanifest door een controller is gegenereerd en gepind.

## 4. Claim-lock en claimsluiting

Voor inhoudelijk werk schrijft de worker een claim in `state.yaml` en een `CLAIMED`-event met:
- `role`;
- `claimed_by`;
- `claimed_at`;
- `source_commit`;
- `expected_state`;
- `output_path`;
- `claim_status: ACTIVE`.

Claims verlopen niet automatisch. Overname van een actieve claim vereist expliciete activatie door Mark of een controller en een `CLAIM_OVERRIDDEN`-event met reden.

Bij geldige fasecompletion moet dezelfde workerclaim in dezelfde completioncommit aantoonbaar worden gesloten met:
- `claim_status: CLOSED`;
- `claim_closed_at`;
- `completion_commit`;
- `completion_result: PASS|PARTIAL|BLOCKED`.

Het completionevent noemt dezelfde claimsluiting. Een claim met `claim_status: CLOSED` blokkeert geen opvolgende controllerclaim. Een ontbrekende, tegenstrijdige of nog `ACTIVE` workerclaim blokkeert iedere inline transition.

Controllertransitions gebruiken altijd een afzonderlijke transitionclaim met `claim_status: ACTIVE`. Een workerclaim wordt nooit hergebruikt.

## 5. Source-commit pinning

`source_commit` identificeert de gepinde invoersnapshot. De actuele branch-head mag vooruitgaan wanneer alle required files op de gepinde commit beschikbaar blijven en de verwachte blob-SHA's overeenkomen.

Een verschil tussen `source_commit` en branch-head is op zichzelf geen fout. Materiële inputdrift is wel een stopvoorwaarde: ontbrekend of afgekapt required bestand, afwijkende hash, state/event-desynchronisatie of ongeldig contextmanifest.

Na claimen schrijft de worker alleen naar zijn eigen fase-output en de overeengekomen state/eventbestanden, behalve de expliciet gepinde GOUD-integratiescope uit sectie 9.3.

## 6. Fase-output

Iedere fase schrijft minimaal:
- `manifest.yaml`;
- `report/INDEX.md`;
- opgesplitste rapportbestanden uit INDEX;
- `claims.jsonl`;
- `sources/registry.jsonl`;
- `sources/rejected.jsonl`;
- `audit.md`;
- `handoff.yaml`;
- `COMPLETED`.

Geen primair fasebestand is groter dan 1500 regels. Splits eerder wanneer leesbaarheid of contextbudget daar baat bij heeft.

`REPORT_ASSEMBLED.md` is optioneel en nooit de primaire opvolgerinvoer.

GOUD schrijft bij een gepinde `MARK_FINAL_REPORT`-modus aanvullend:
- `research/active/<RUN_ID>/GOUD/MARK_FINAL_REPORT.md`;
- `research/active/<RUN_ID>/GOUD/CANONICAL_INTEGRATION_PROPOSAL.md`.

## 7. Volledigheid en truncatie

Ieder tekstbestand eindigt met `END_OF_ARTIFACT`.

`manifest.yaml` noemt alle verplichte bestanden, regel- of byteaantallen, betrouwbare hashes, completionstatus, broncommit en protocolversies.

`COMPLETED` wordt pas geschreven nadat alle vereiste bestanden opnieuw zijn geopend en sentinels zichtbaar zijn gecontroleerd.

Bij GitHub Contents API-reads wordt het gerapporteerde `size`-veld vergeleken met de gedecodeerde contentlengte. Bij mismatch of lege content met `size > 0` wordt de Git Blob API gebruikt. Een mogelijk afgekapte read mag nooit als basis dienen voor volledige vervanging.

## 8. Handoff

`handoff.yaml` bevat geen rapporttekst. Het bevat:
- run-id;
- completed role;
- result status;
- output manifest path;
- next role;
- next expected transition;
- open blockers;
- required predecessor files.

De worker claimt geen toekomstige `source_commit`. De controller stelt die vast na de definitieve fasecommit.

De volgende rol leest uitsluitend het controllergegenereerde, gepinde contextmanifest.

## 9. Post-completion-modi

### 9.1 Oud proces

Zonder geldige nieuwe pins stopt BRONS na `BRONS_COMPLETE` en ZILVER na `ZILVER_COMPLETE`. Een afzonderlijk geactiveerde controller verzorgt de transition.

### 9.2 `INLINE_POST_PHASE_CONTROLLER`

Wanneer `run.yaml` en `NEXT_ACTION.yaml` dit expliciet toestaan, mag dezelfde sessie na volledige workercompletion een afzonderlijke controllerrol starten volgens `ROLE_HANDOFF_PROTOCOL.md`.

De workerrol moet eerst aantoonbaar eindigen. De workerclaim moet `CLOSED` zijn. Daarna zijn fase-outputwrites verboden. De sessie herhaalt GitHub-preflight, leest de controllerprotocollen opnieuw, schrijft een afzonderlijke controllerclaim en voert alleen controllerwrites uit.

### 9.3 `MARK_FINAL_REPORT` met deterministische canonieke integratie

GOUD schrijft eerst een volledig `CANONICAL_INTEGRATION_PROPOSAL.md`. Alleen wanneer `run.yaml` en `NEXT_ACTION.yaml` expliciet `canonical_integration.mode: DETERMINISTIC_NON_DECISIONAL` pinnen, mag GOUD vóór completion de exact voorgestelde canonieke writes uitvoeren naar:
- `knowledge/places/registry.jsonl`;
- `decisions/INDEX.yaml`.

Deze uitzonderlijke GOUD-write-scope geldt uitsluitend voor mechanische integratie die één-op-één uit gevalideerde GOUD-artifacts volgt. Toegestaan zijn technische documentstatus, artifactpaden, bestaande LOCATION_ID-koppelingen, gecontroleerde aliases/GEO-statussen en koppelingen naar reeds bestaande decision-ID's.

Absoluut verboden zijn:
- nieuwe of gewijzigde formele A/B/C-status;
- nieuwe of gewijzigde adviserende A/B/C-status;
- een nieuw decision-ID;
- nieuwe of herschreven beslistekst;
- een koerskeuze namens Mark;
- een canonieke wijziging bij twijfel of onvolledig bewijs.

Wanneer een beslissing van Mark nodig is, past GOUD de betreffende canonieke wijziging niet toe, zet het voorstel op `mark_decision_required: YES`, benoemt de keuze exact in het Markrapport en archiveert de run niet als volledig geïntegreerd.

Na toegestane canonieke writes valideert GOUD syntax, unieke LOCATION_ID's, bestaande decision-ID's, ongewijzigde A/B/C-velden en finale readback. Daarna schrijft GOUD completion, sluit de workerclaim en levert het volledige Markrapport.

## 10. Controllertransitions

Na `BRONS_COMPLETE` en `ZILVER_COMPLETE` blijft een controllertransition verplicht. Inline control verandert alleen wie de controllerrol direct daarna uitvoert; het verwijdert de rol- en write-scheiding niet.

## 11. Fouten en herstel

- Ontbrekend bestand of sentinel: geen COMPLETE-status of transition.
- State/event mismatch: append `DESYNC_DETECTED`, stop en laat Mark/controller herstellen.
- Partiële commit: herstel binnen dezelfde fase; schrijf pas daarna COMPLETED.
- Actieve of onduidelijk gesloten claim: geen inline transition.
- Onjuiste claim: alleen expliciete override.
- Protocolwijziging tijdens run: negeren; gepinde versie blijft leidend.
- Ontbrekend opvolgercontextmanifest: volgende rol niet activeren.
- Alleen branch-head advancement zonder required-file drift: niet blokkeren.
- Inline transition faalt: behoud geldige fasecompletion maar schrijf geen volgende READY-state of startopdracht.
- Canonieke integratie vereist een inhoudelijk besluit: wijzig de betreffende canonieke records niet; lever een exact beslispunt aan Mark.

## 12. Archivering

Na GOUD PASS/PARTIAL kan de run volgens het archiveringsprotocol worden verplaatst wanneer de deterministische canonieke integratie is voltooid of expliciet `NOT_APPLICABLE` is. Bij `mark_decision_required: YES` blijft de run zichtbaar als nog niet volledig geïntegreerd. Een geldig Markrapport vereist geen normale eindredactie door INDIA2.

END_OF_ARTIFACT