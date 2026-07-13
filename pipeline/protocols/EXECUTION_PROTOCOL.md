# Execution Protocol v2.2.1

## 1. Repository-only handoff

Een chat is een tijdelijke worker. Alle blijvende invoer, voortgang en uitvoer staat in GitHub. BRONS, ZILVER en GOUD communiceren niet via geplakte rapporten.

## 2. Runstatus

Iedere run bevat:
- `run.yaml` — onveranderlijke run-identiteit, scope en protocolpins;
- `state.yaml` — actuele afgeleide toestand;
- `events.jsonl` — append-only gebeurtenissen;
- een definitief contextmanifest voor de actieve of eerstvolgende uitvoerbare rol;
- één geïsoleerde outputmap per fase.

`run.yaml` verandert niet nadat BRONS is geclaimd. Een noodzakelijke wijziging vereist een nieuwe run of expliciete migratie.

Bij runcreatie bestaat alleen een definitief `BRONS_CONTEXT.yaml`. `ZILVER_CONTEXT.yaml` en `GOUD_CONTEXT.yaml` worden pas na validatie van hun predecessor door een aparte controllertransition gegenereerd.

## 3. Toestanden

Toegestane fasevolgorde:

`READY_FOR_BRONS -> BRONS_CLAIMED -> BRONS_COMPLETE -> TRANSITION_TO_ZILVER_CLAIMED -> READY_FOR_ZILVER -> ZILVER_CLAIMED -> ZILVER_COMPLETE -> TRANSITION_TO_GOUD_CLAIMED -> READY_FOR_GOUD -> GOUD_CLAIMED -> GOUD_PASS|GOUD_PARTIAL|GOUD_BLOCKED -> ARCHIVED`

Een overgang is alleen geldig wanneer:
1. de verwachte vorige toestand klopt;
2. een corresponderend event wordt toegevoegd;
3. verplichte output voor de overgang bestaat en is gevalideerd;
4. voor `READY_FOR_ZILVER` of `READY_FOR_GOUD` het definitieve contextmanifest door de controller is gegenereerd en gepind.

## 4. Claim-lock

Voor inhoudelijk werk schrijft de worker een claim in `state.yaml` en een `CLAIMED`-event met:
- `role`;
- `claimed_by`;
- `claimed_at`;
- `source_commit`;
- `expected_state`;
- `output_path`.

Claims zijn niet automatisch tijdgebonden. Omdat een AI-chat niet betrouwbaar op tijd kan worden hervat, mag een claim alleen worden overgenomen na expliciete activatie door Mark of een controller, vastgelegd als `CLAIM_OVERRIDDEN` met reden.

Controllertransitions gebruiken een afzonderlijke transitionclaim volgens `pipeline/protocols/CONTROLLER_TRANSITION_PROTOCOL.md`.

## 5. Source-commit pinning

`source_commit` identificeert de gepinde invoersnapshot en predecessorcontext. Het is niet vereist dat deze commit gelijk blijft aan de actuele branch-head.

Een branch mag na contextvoorbereiding vooruitgaan door onafhankelijke commits. Dat blokkeert de worker niet wanneer:
- alle `required_files` nog bestaan;
- alle beschikbare `expected_git_blob_shas` exact overeenkomen;
- state en eventlog synchroon zijn;
- geen geldige bestaande claim bestaat;
- het contextmanifest zelf niet is vervangen door een ongeldig of ongeautoriseerd manifest.

De worker stopt alleen bij materiële inputdrift: een required file ontbreekt, is afgekapt of heeft een afwijkende gepinde hash; of bij een andere expliciete stopvoorwaarde. Een verschil tussen `source_commit` en de actuele branch-head is op zichzelf geen SHA-afwijking.

Na claimen schrijft de worker alleen naar zijn eigen fase-output en de overeengekomen state/eventbestanden. Andere protocol- of onderzoeksbestanden worden niet gewijzigd.

De worker schrijft nooit het contextmanifest van zijn opvolger. Na `BRONS_COMPLETE` of `ZILVER_COMPLETE` stopt hij. De controller bepaalt daarna de definitieve resultaatcommit en maakt het volgende contextmanifest.

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

Geen primair fasebestand mag groter zijn dan 1500 regels. Splits eerder wanneer leesbaarheid of contextbudget daar baat bij heeft.

`REPORT_ASSEMBLED.md` is optioneel en afgeleid. Het is nooit de primaire invoer voor de volgende fase.

## 7. Volledigheid en truncatie

Ieder tekstbestand eindigt met `END_OF_ARTIFACT`.

`manifest.yaml` noemt:
- alle verplichte bestanden;
- regel- of byteaantallen;
- hashes wanneer de uitvoerder die betrouwbaar kan berekenen;
- completion status;
- broncommit;
- rol- en protocolversies.

`COMPLETED` wordt pas geschreven nadat alle vereiste bestanden opnieuw zijn geopend en de sentinels zichtbaar zijn gecontroleerd. Het bestand vermeldt `PASS`, `PARTIAL` of `BLOCKED` en de lijst met outputs.

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

De worker mag in `handoff.yaml` geen toekomstige `source_commit` claimen. De controller stelt die pas vast nadat de fasecommit definitief bestaat.

De volgende rol leest uitsluitend het door de controller gegenereerde en gepinde contextmanifest.

## 9. Controllertransitions

Na `BRONS_COMPLETE` en `ZILVER_COMPLETE` is een aparte controllertransition verplicht. De controller valideert de predecessor, bepaalt de definitieve resultaatcommit, genereert het volgende contextmanifest, update state en events en commit de overgang. De volledige regels staan in `pipeline/protocols/CONTROLLER_TRANSITION_PROTOCOL.md`.

## 10. Fouten en herstel

- Ontbrekend bestand of sentinel: fase blijft geclaimd of wordt `BLOCKED`; geen COMPLETE-status.
- State/event mismatch: append `DESYNC_DETECTED`, stop en laat Mark/controller herstellen.
- Partiële commit: maak een herstelcommit binnen dezelfde fase; schrijf pas daarna COMPLETED.
- Onjuiste claim: alleen expliciete override door Mark/controller.
- Protocolwijziging tijdens run: negeren; gepinde versie blijft leidend.
- Ontbrekend opvolgercontextmanifest: volgende rol wordt niet geactiveerd; controllertransition uitvoeren.
- Alleen branch-head advancement zonder required-file drift: niet blokkeren.

## 11. Archivering

Na GOUD PASS/PARTIAL en verwerking door de regisseur kan de volledige run van `research/active/` naar `research/completed/` worden verplaatst. Voltooide runs zijn standaard buiten context. Alleen een contextmanifest kan specifieke completed runs opnieuw toelaten.

END_OF_ARTIFACT