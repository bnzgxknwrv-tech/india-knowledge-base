# INDIA5 TASK PROTOCOL

Status: VERPLICHT vanaf 2026-08-02 (INDIA2-architectuurbesluit, PR #23, taak "INDIA5 VEILIGE
TAAKARCHITECTUUR INVOEREN"). Versie: `1.0.0` (dit is de waarde die nieuwe `TASK.yaml`-bestanden
in `protocol_version` moeten zetten).

## Doel

Vervang de lange PR-commentrelay als plek waar taakinhoud en resultaten daadwerkelijk leven.
PR-comments worden voortaan korte, wegwerpbare enveloppen; de taak zelf, de status, en het
resultaat leven duurzaam in versiebeheerde bestanden onder `india5/tasks/`. Eén taak kan een
volledige regioflow dragen (`PRE-BRONS → BRONS → ZILVER → GOUD → TRAVEL`) zonder dat Mark meer
dan één korte startopdracht hoeft te geven.

## Directorystructuur

```
india5/
  TASK_PROTOCOL.md               <- dit bestand
  schemas/
    task.schema.json
    status.schema.json
  scripts/
    validate_task.py
    claim_task.py
    complete_task.py
  tasks/
    queue/<TASK_ID>/              <- nieuw uitgegeven, nog niet geclaimd
      TASK.yaml                   <- machineleesbare envelop, IMMUTABLE na uitgifte
      TASK.md                     <- volledige, mensleesbare taakinhoud
      STATUS.yaml                 <- enige plek waar voortgang leeft
    active/<TASK_ID>/              <- geclaimd, in uitvoering (max. 1 tegelijk)
      ... zelfde bestanden, plus RESULT.md zodra geschreven
    done/<TASK_ID>/                 <- afgerond, COMPLETED
      ... + RESULT.md (verplicht)
    failed/<TASK_ID>/               <- afgerond, FAILED
      ... + STATUS.yaml met failure_reason
```

Een taakdirectory verplaatst zich letterlijk tussen deze vier mappen (`queue → active → done`
of `queue → active → failed`) — er is nooit een taak tegelijk in twee mappen.

## PR-comment-enveloppen (het enige dat nog in PR-comments hoort)

**Taakenvelop (INDIA2 → CCI):**
```
CCI_TASK_ENVELOPE
task_id: <TASK_ID>
task_file: india5/tasks/queue/<TASK_ID>/TASK.yaml
task_file_sha256: <sha256 van TASK.md>
expected_head: <commit-SHA van target_branch>
```

**Resultaatenvelop (CCI → INDIA2):**
```
CCI_RESULT
task_id: <TASK_ID>
status: COMPLETED | FAILED | BLOCKED
commit: <commit-SHA na push>
files_created: [...]
validators: <welke validators gedraaid, met resultaat>
test_result: <indien van toepassing>
blockers: <indien van toepassing, anders "geen">
result_file: india5/tasks/done/<TASK_ID>/RESULT.md
result_file_sha256: <sha256 van RESULT.md>
completion_marker: <de marker, ter bevestiging>
```

De uitgebreide inhoud staat altijd in `TASK.md`/`RESULT.md`, nooit (meer) losstaand in de
PR-comment zelf. **Geen bestaande PR-comment geldt als canonieke bron van waarheid** — dat zijn
uitsluitend `TASK.yaml`/`STATUS.yaml`/`RESULT.md` en de canonieke protocol-/registerbestanden.

## Vereiste werking

1. PR-comments zijn voortaan alleen korte enveloppen (zie hierboven).
2. CCI voert nooit een taak uit zonder geslaagde validatie (`validate_task.py`) van schema,
   `task_file_sha256`-hash, branch en `expected_head`.
3. CCI claimt een taak atomisch door verplaatsing van `queue/` naar `active/`
   (`claim_task.py`), direct gevolgd door een git-commit — die commit ís de atomische grens
   (zie "Exactly-once claim" hieronder).
4. Eén taak kan een volledige regioflow `PRE-BRONS → BRONS → ZILVER → GOUD → TRAVEL` bevatten
   (`scope: REGION_FULL_FLOW`).
5. Mark hoeft bij normale voortgang maar één korte startopdracht te geven (bv. "Voer de
   nieuwste CCI_TASK op PR #23 uit" — CCI leest dan zelf de nieuwste taakenvelop-comment en
   volgt het pad naar de echte taak).
6. Resultaten worden volledig in `RESULT.md` + de outputbestanden zelf geschreven; de
   PR-comment bevat alleen de korte resultaatenvelop.
7. Geen bestaande PR-comment geldt als canonieke bron van waarheid (zie hierboven).
8. **Conflicterende instructies volgen deze prioriteit, hoog naar laag:**
   1. een expliciet nieuw Mark-besluit voor persoonlijke keuzes (A/B/C, hotel, enz.);
   2. een actieve, gevalideerde `TASK.yaml`;
   3. canonieke protocol-/registerbestanden (`india4/protocols/`, `india4/registries/` /
      `india5/`-equivalenten);
   4. lokale hooks of losse chattekst — deze staan NOOIT boven een actieve taak.
9. Geen taak mag stil worden uitgevoerd wanneer de inhoud afgekapt lijkt, de eindmarker
   (`completion_marker`) ontbreekt, of de hash niet klopt — dit blokkeert hard
   (`validate_task.py`/`complete_task.py` geven exit-code 1).
10. Bestaande Varanasi-nummers 001–040, A/B/C-besluiten, het hotelbesluit en GEO-afwijzingen
    zijn per definitie `forbidden_writes` voor elke architectuurtaak (`scope: ARCHITECTURE`).

## Globale veiligheidsregels (ontwerp)

- **Exactly-once claim**: de atomische grens is niet de bestandsverplaatsing zelf (die kan een
  agent altijd lokaal doen), maar de git-commit die de verplaatsing vastlegt. Zolang die commit
  niet bestaat, is de claim ongeldig/herroepbaar. `claim_task.py` weigert bovendien te claimen
  zolang er al een taak in `active/` staat (zie hieronder).
- **Hervatten na sessieverlies**: een nieuwe sessie leest uitsluitend `india5/tasks/active/`. Is
  daar een taak aanwezig, dan is dat de enige waarheid over "waar was ik gebleven" — nooit een
  aanname uit chatgeschiedenis. Staat er niets in `active/`, dan is er geen lopende taak, punt.
- **Commit zonder RESULT**: `complete_task.py` weigert een taak als `COMPLETED` te markeren
  zolang `RESULT.md` ontbreekt of de `completion_marker` niet exact voorkomt. `validate_task.py
  --post-hoc` detecteert dit alsnog achteraf als het toch gebeurd zou zijn (STATUS.yaml zegt
  COMPLETED, RESULT.md ontbreekt).
- **RESULT zonder commit**: een `RESULT.md` die lokaal bestaat maar nooit gecommit is, is per
  definitie niet zichtbaar voor een volgende sessie/voor INDIA2 — dat is de bedoelde makkelijke
  aanpak: als het niet gecommit is, bestaat het voor de rest van het systeem niet. Geen apart
  mechanisme nodig, wél een expliciete regel: CCI commit nooit een taak als "klaar" totdat
  `RESULT.md` + alle `expected_outputs` daadwerkelijk in dezelfde commit zitten.
- **Tweede taak terwijl eerste actief is**: `claim_task.py` controleert `india5/tasks/active/`
  en weigert een tweede claim zolang die niet leeg is (maximaal 1 actieve taak tegelijk,
  systeembreed).
- **Stale `expected_head`**: `validate_task.py` vergelijkt `expected_head` met de daadwerkelijke
  HEAD van `target_branch` vóór claim. Bij mismatch: hard blokkeren, nooit automatisch
  doorzetten — de opdrachtgever moet een nieuwe taak met een bijgewerkte `expected_head`
  uitgeven.
- **Non-fast-forward**: bij het pushen van een taak-commit geldt dezelfde regel als elders in
  deze sessie — nooit force-pushen. Bij een non-fast-forward-conflict: STOP, meld het als
  blocker in de resultaatenvelop, wacht op een nieuwe taak/instructie.
- **Cross-regio nummeringscontrole**: zodra een tweede regio (na Varanasi) start, moet de
  nummerings-validator (vandaag nog `runs/active/<run_id>/scripts/validate_numbering.py`,
  per-run) een GLOBALE variant krijgen die controleert dat geen enkel nummer uit een eerdere
  regio's `NUMBERING_REGISTRY.jsonl` opnieuw wordt uitgegeven. Dit is een ontwerpnotitie voor
  wanneer regio 2 daadwerkelijk start — niet nu gebouwd (buiten scope van deze architectuurtaak).
- **Aparte governance-PR en aparte regio-PR's**: aanbeveling voor de toekomst — architectuur-
  /tooling-wijzigingen (zoals deze taak) zouden idealiter in een eigen PR kunnen leven, los van
  regio-inhoud-PR's, zodat een architectuurwijziging nooit per ongeluk regio-data meesleept in
  een merge. Voor nu blijft alles op PR #23 (expliciete instructie van deze taak: "PR #23 niet
  mergen"), dit is puur een aanbeveling voor een volgende fase.

## Levenscyclus van een taak

1. INDIA2 (of Mark) schrijft `TASK.md` + `TASK.yaml`, plaatst ze in
   `india5/tasks/queue/<TASK_ID>/`, commit, en post de korte taakenvelop op de PR.
2. Mark stuurt CCI aan met een korte startopdracht.
3. CCI leest de nieuwste taakenvelop-comment, haalt `task_id`/`task_file`/
   `task_file_sha256`/`expected_head` op.
4. CCI draait `validate_task.py <TASK_ID> --stage queue`. Bij fouten: stoppen, blocker melden.
5. CCI draait `claim_task.py <TASK_ID>`, commit direct de verplaatsing naar `active/`.
6. CCI voert de taakinhoud uit zoals in `TASK.md` beschreven, binnen `allowed_writes` en nooit
   binnen `forbidden_writes`.
7. CCI schrijft `RESULT.md` (met de exacte `completion_marker`) + alle `expected_outputs`.
8. CCI draait `complete_task.py <TASK_ID>` (of `--fail "reden"` bij een blocker), commit de
   verplaatsing naar `done/` of `failed/`, en pusht.
9. CCI plaatst de korte resultaatenvelop op de PR, met de daadwerkelijke commit-SHA.

## Taak-ID-conventie

`INDIA5-<SCOPE>-<NNN>`, bv. `INDIA5-ARCH-TEST-001` (architectuurtest), `INDIA5-VNS-002`
(volgende Varanasi-taak). `<SCOPE>` correspondeert idealiter met het `scope`-veld in
`TASK.yaml`, maar is vrije tekst zolang het uniek en leesbaar blijft.
