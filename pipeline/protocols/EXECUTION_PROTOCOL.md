# Execution Protocol v2.0

## 1. Repository-only handoff

Een chat is een tijdelijke worker. Alle blijvende invoer, voortgang en uitvoer staat in GitHub. BRONS, ZILVER en GOUD communiceren niet via geplakte rapporten.

## 2. Runstatus

Iedere run bevat:
- `run.yaml` — onveranderlijke run-identiteit, scope en protocolpins;
- `state.yaml` — actuele afgeleide toestand;
- `events.jsonl` — append-only gebeurtenissen;
- één contextmanifest per rol;
- één geïsoleerde outputmap per fase.

`run.yaml` verandert niet nadat BRONS is geclaimd. Een noodzakelijke wijziging vereist een nieuwe run of expliciete migratie.

## 3. Toestanden

Toegestane fasevolgorde:

`READY_FOR_BRONS -> BRONS_CLAIMED -> BRONS_COMPLETE -> READY_FOR_ZILVER -> ZILVER_CLAIMED -> ZILVER_COMPLETE -> READY_FOR_GOUD -> GOUD_CLAIMED -> GOUD_PASS|GOUD_PARTIAL|GOUD_BLOCKED -> ARCHIVED`

Een overgang is alleen geldig wanneer:
1. de verwachte vorige toestand klopt;
2. een corresponderend event wordt toegevoegd;
3. verplichte output voor de overgang bestaat en is gevalideerd.

## 4. Claim-lock

Voor inhoudelijk werk schrijft de worker een claim in `state.yaml` en een `CLAIMED`-event met:
- `role`
- `claimed_by`
- `claimed_at`
- `source_commit`
- `expected_state`
- `output_path`

Claims zijn niet automatisch tijdgebonden. Omdat een AI-chat niet betrouwbaar op tijd kan worden hervat, mag een claim alleen worden overgenomen na expliciete activatie door Mark of een controller, vastgelegd als `CLAIM_OVERRIDDEN` met reden. Zo wordt stille dubbele schrijvers voorkomen zonder een schijnbaar betrouwbare leaseklok.

## 5. Source-commit pinning

De worker leest vanaf de commit die in het contextmanifest staat. Voor de eigen fase-uitvoer geldt die commit als `source_commit`. Verandert de branch vóór de claim of blijkt een expected hash afwijkend, dan stopt de worker.

Na claimen schrijft de worker alleen naar zijn eigen fase-output en de overeengekomen state/eventbestanden. Andere protocol- of onderzoeksbestanden worden niet gewijzigd.

## 6. Fase-output

Iedere fase schrijft minimaal:
- `manifest.yaml`
- `report/INDEX.md`
- opgesplitste rapportbestanden uit INDEX
- `claims.jsonl`
- `sources/registry.jsonl`
- `sources/rejected.jsonl`
- `audit.md`
- `handoff.yaml`
- `COMPLETED`

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
- next expected state;
- source commit voor de volgende fase;
- open blockers;
- required predecessor files.

De volgende rol leest uitsluitend zijn gepinde contextmanifest. Dat manifest verwijst expliciet naar de fase-output die nodig is.

## 9. Fouten en herstel

- Ontbrekend bestand of sentinel: fase blijft geclaimd of wordt `BLOCKED`; geen COMPLETE-status.
- State/event mismatch: append `DESYNC_DETECTED`, stop en laat Mark/controller herstellen.
- Partiële commit: maak een herstelcommit binnen dezelfde fase; schrijf pas daarna COMPLETED.
- Onjuiste claim: alleen expliciete override door Mark/controller.
- Protocolwijziging tijdens run: negeren; gepinde versie blijft leidend.

## 10. Archivering

Na GOUD PASS/PARTIAL en verwerking door de regisseur kan de volledige run van `research/active/` naar `research/completed/` worden verplaatst. Voltooide runs zijn standaard buiten context. Alleen een contextmanifest kan specifieke completed runs opnieuw toelaten.

END_OF_ARTIFACT
