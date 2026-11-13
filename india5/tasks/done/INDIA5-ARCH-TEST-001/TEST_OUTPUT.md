# TEST_OUTPUT.md — INDIA5-ARCH-TEST-001

## Claim

`python3 india5/scripts/claim_task.py INDIA5-ARCH-TEST-001` slaagde: de taakdirectory is
verplaatst van `india5/tasks/queue/INDIA5-ARCH-TEST-001/` naar
`india5/tasks/active/INDIA5-ARCH-TEST-001/`, `STATUS.yaml` kreeg `state: ACTIVE`,
`claimed_by: CCI`, `claimed_at`/`started_at` ingevuld, en een `CLAIMED`-regel in `history`. De
verplaatsing is direct daarna gecommit (commit `0eb79f4`), vóórdat er verder inhoudelijk werk
werd gedaan — dat is de atomische grens uit `india5/TASK_PROTOCOL.md`.

## Validatie (queue-stage, vóór claim)

```
$ python3 india5/scripts/validate_task.py INDIA5-ARCH-TEST-001 --stage queue
VALIDATIE OK -- INDIA5-ARCH-TEST-001 (stage=queue) is geldig, geen fouten.
```

## Validatie (active-stage, ná claim, vóór completion)

```
$ python3 india5/scripts/validate_task.py INDIA5-ARCH-TEST-001 --stage active
VALIDATIE OK -- INDIA5-ARCH-TEST-001 (stage=active) is geldig, geen fouten.
```

Beide validaties controleerden: alle verplichte `TASK.yaml`-velden aanwezig, `scope` geldig,
`status: QUEUED` in `TASK.yaml` zelf (immutable, ongeacht de echte voortgang in `STATUS.yaml`),
geen overlap tussen `allowed_writes`/`forbidden_writes`, `task_file_sha256` klopt met de
werkelijke hash van `TASK.md`, en `expected_head` kwam overeen met de HEAD van
`claude/werk-je-nu-of-niet-oa10y7` op het moment van claimen.

## Bewijs van hervatbaarheid

Als deze sessie was afgebroken direct na de claim-commit (`0eb79f4`), zou een volledig nieuwe
sessie het volgende hebben aangetroffen zonder enige aanname uit chatgeschiedenis nodig te
hebben:

- `india5/tasks/active/INDIA5-ARCH-TEST-001/` bestaat (en `queue/` bevat de taak niet meer) --
  dus er is precies één actieve taak, ondubbelzinnig.
- `STATUS.yaml` zegt `state: ACTIVE`, `claimed_by: CCI`, met een tijdstip -- de nieuwe sessie
  weet exact dat deze taak geclaimd maar nog niet afgerond is.
- `RESULT.md` ontbreekt nog op dat moment -- dus de nieuwe sessie weet dat de uitvoering nog
  moet gebeuren of moet worden hervat, niet dat de taak al klaar is.
- `python3 india5/scripts/validate_task.py INDIA5-ARCH-TEST-001 --post-hoc` zou op dat moment
  GEEN inconsistentie melden (state=ACTIVE zonder RESULT.md is een normale tussentoestand, geen
  fout) -- pas als `STATUS.yaml` `COMPLETED` zou zeggen zonder `RESULT.md` zou dat als fout
  worden gemarkeerd ("commit zonder RESULT").

Er is dus geen enkel moment waarop de status van deze taak dubbelzinnig is voor een nieuwe
sessie: de bestandslocatie (welke map) + `STATUS.yaml.state` zijn samen altijd voldoende.
