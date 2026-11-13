# INDIA5 TASK PROTOCOL

Status: VERPLICHT vanaf 2026-08-02 (INDIA2-architectuurbesluit, PR #23, taken "INDIA5 VEILIGE
TAAKARCHITECTUUR INVOEREN" en "INDIA5-ARCH-HARDEN-002"). Versie: `1.1.0` (dit is de waarde die
nieuwe `TASK.yaml`-bestanden in `protocol_version` moeten zetten). Zie ook
`india5/GOVERNANCE.md` voor de gemigreerde governance-besluiten (rolverdeling, escalatie,
detectorbibliotheek-eigendom, enz.) die niet-technisch/procesmatig van aard zijn.

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
  GOVERNANCE.md                  <- gemigreerde governance-besluiten (rollen, escalatie, enz.)
  schemas/
    task.schema.json
    status.schema.json
    knowledge_gate.schema.json
  templates/
    KNOWLEDGE_GATE_REVIEW_TEMPLATE.md
  scripts/
    validate_task.py             <- schema/hash/expected_head/HOLD-validatie
    claim_task.py                <- atomische claim, snapshot van reeds-vuile paden
    complete_task.py             <- active -> done/failed, roept check_forbidden_writes.py aan
    resolve_task_commits.py      <- niet-circulaire opzoeking van claim-/completion-commit
    check_forbidden_writes.py    <- afdwinging van forbidden_writes sinds de claim-commit
    validate_global_numbering.py <- repositorybrede nummeringscontrole (alleen-lezend)
    validate_knowledge_gate.py   <- validatie van een KNOWLEDGE_GATE_REVIEW.json
  tasks/
    queue/<TASK_ID>/              <- nieuw uitgegeven, nog niet geclaimd
      TASK.yaml                   <- machineleesbare envelop, IMMUTABLE na uitgifte
      TASK.md                     <- volledige, mensleesbare taakinhoud
      STATUS.yaml                 <- enige plek waar voortgang leeft (incl. hold, pre_existing_dirty_paths)
    active/<TASK_ID>/              <- geclaimd, in uitvoering (max. 1 tegelijk)
      ... zelfde bestanden, plus RESULT.md zodra geschreven, plus evt. aparte reviewbestanden
      (bv. *_HOLD_INVENTORY.md, *_REVIEW.md) die WEL in de taak leven maar NIET automatisch
      betekenen dat hun inhoud elders gecommit wordt
    done/<TASK_ID>/                 <- afgerond, COMPLETED
      ... + RESULT.md (verplicht)
    failed/<TASK_ID>/               <- afgerond, FAILED
      ... + STATUS.yaml met failure_reason
```

`STATUS.yaml` bevat minimaal: `state`, `claimed_at/by`, `started_at`, `completed_at`,
`git_commit_at_claim`/`git_commit_at_complete` (altijd `null`, zie hieronder),
`completion_marker_found`, `failure_reason`, `pre_existing_dirty_paths` (snapshot op
claimmoment, zie "Forbidden-writes-afdwinging" hieronder), `hold` (object met
`active`/`reason`/`set_at`/`set_by`, zie "HOLD/ABORT" hieronder), `result_comment_posted`
(bool), `history` (append-only logboek). Volledig schema: `india5/schemas/status.schema.json`.

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
   `task_file_sha256`-hash, branch, `expected_head` (zie "expected_head-semantiek" hieronder)
   en afwezigheid van een actieve `HOLD` (zie "HOLD/ABORT" hieronder).
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
8. **Conflicterende instructies volgen deze prioriteit, hoog naar laag** (herzien in
   INDIA5-ARCH-HARDEN-002, canoniek ook in `india5/GOVERNANCE.md` sectie 6):
   1. de canonieke `TASK.yaml`/`TASK.md` van de actieve, gevalideerde taak op de bedoelde
      branch;
   2. een expliciete `HOLD`/`ABORT`-status IN de taakbestanden zelf (`STATUS.yaml.hold.active`)
      — zie "HOLD/ABORT" hieronder;
   3. het Mark-besluitenregister (`RUN.yaml protected_mark_decisions`, `MARK_DECISIONS*.jsonl`,
      `ACCOMMODATION_REGISTER.jsonl`, enz.);
   4. PR-comments — uitsluitend als envelop/signaal, nooit als inhoudelijke bron van waarheid;
   5. lokale hooks of losse chattekst — deze staan NOOIT boven een actieve canonieke taak.
9. Geen taak mag stil worden uitgevoerd wanneer de inhoud afgekapt lijkt, de eindmarker
   (`completion_marker`) ontbreekt, of de hash niet klopt — dit blokkeert hard
   (`validate_task.py`/`complete_task.py` geven exit-code 1).
10. Bestaande Varanasi-nummers 001–040, A/B/C-besluiten, het hotelbesluit en GEO-afwijzingen
    zijn per definitie `forbidden_writes` voor elke architectuurtaak (`scope: ARCHITECTURE`).

## Globale veiligheidsregels

### git_commit_at_claim / git_commit_at_complete zijn ALTIJD null (niet-circulair, zie punt 1)

`STATUS.yaml` kan de hash van de commit die het bestand ZELF bevat niet in zich dragen — die
hash hangt af van de volledige boominhoud inclusief dat bestand, dus het schrijven van de hash
zou de hash veranderen, enzovoort. Dit is fundamenteel circulair, geen bug om te "fixen" door
harder te proberen. Deze twee velden blijven daarom in het gecommitte bestand altijd `null`.

De niet-circulaire oplossing: `india5/scripts/resolve_task_commits.py <TASK_ID>` bepaalt deze
commits ACHTERAF met een read-only git-log-query (`git log --all --diff-filter=A -- <pad>`,
meest recente resultaat), ná het moment dat de commit al bestaat. Dit is de enige geautoriseerde
manier om de daadwerkelijke claim-/completion-commit op te vragen — voor de `commit`-waarde in
de resultaatenvelop, of om een aparte, latere `STATUS.yaml`-patch-commit te schrijven (nooit in
dezelfde commit als de gebeurtenis zelf, dat zou opnieuw circulair zijn). Geverifieerd tegen de
echte geschiedenis van `INDIA5-ARCH-TEST-001` en `INDIA5-ARCH-HARDEN-002` (zie `RESULT.md`).

### expected_head-semantiek (herzien, zie punt 2)

`expected_head` betekent: de commit waarop deze taak is GEBASEERD, niet de exacte HEAD op
claimmoment. Exacte gelijkheid zou circulair zijn — het committen van `TASK.md`/`TASK.yaml`
zelf, en de claim-commit erna, verzetten HEAD altijd voorbij `expected_head`, ook bij een
volkomen geldige, verse taak. `validate_task.py` controleert daarom of `expected_head` een
VOOROUDER is van (of gelijk aan) de huidige HEAD (`git merge-base --is-ancestor`), niet of ze
identiek zijn. Alleen een echte divergentie (expected_head is GEEN voorouder meer, bv. door een
force-push elders) telt als `STALE_EXPECTED_HEAD` en blokkeert hard. Getest met een synthetische
divergente branch (zie `RESULT.md`) en met de eigen claim-commits (die legitiem ná
`expected_head` liggen).

### Exactly-once claim en exactly-once task_id

- de atomische grens is niet de bestandsverplaatsing zelf (die kan een agent altijd lokaal
  doen), maar de git-commit die de verplaatsing vastlegt. Zolang die commit niet bestaat, is de
  claim ongeldig/herroepbaar;
- `claim_task.py` weigert te claimen zolang er al een andere taak in `india5/tasks/active/`
  staat (maximaal 1 actieve taak tegelijk, systeembreed) — meerdere taken in `queue/`
  tegelijkertijd is wél toegestaan en normaal;
- `task_id` is immutable en wordt nooit hergebruikt (zelfde principe als Immutable Location
  Numbering): `claim_task.py` weigert een claim als hetzelfde `task_id` al bestaat in `done/` of
  `failed/`, ook als iemand per ongeluk een kopie in `queue/` zou terugzetten;
- een tweede, parallelle CCI-sessie tegen dezelfde lokale checkout kan in theorie ook lokaal
  claimen vóór de eerste pusht — de daadwerkelijke bescherming zit in git zelf: alleen de EERST
  gepushte claim-commit wint (fast-forward); de tweede sessie krijgt een non-fast-forward-fout
  bij het pushen. Recovery: fetchen, controleren of de taak al in `active/`/`done/` op de
  remote staat; zo ja, de eigen lokale claim intrekken (`git reset`/`git restore`, NOOIT force-
  pushen) en de taak als "al geclaimd door een andere sessie" behandelen.

### Crashherstel (vier toestanden, punt 4)

Een nieuwe sessie leest UITSLUITEND `india5/tasks/`, nooit chatgeschiedenis, om te bepalen waar
een vorige sessie is gebleven:

1. **Na queue-commit, vóór claim**: taak staat in `queue/`, `STATUS.yaml.state == QUEUED`. Geen
   bijzondere actie nodig — dit is gewoon de normale startsituatie, claim zoals gebruikelijk.
2. **Na claim-commit, vóór uitvoering**: taak staat in `active/`, `state == ACTIVE`,
   `RESULT.md` ontbreekt nog. De nieuwe sessie hervat de uitvoering volgens `TASK.md`, zonder
   opnieuw te claimen (de taak is al van haar).
3. **Na outputs, vóór completion**: taak staat nog in `active/`, maar `RESULT.md` +
   `expected_outputs` bestaan al. De nieuwe sessie draait gewoon `complete_task.py <TASK_ID>` —
   dat is precies het ontworpen hervattingspad, geen speciale code nodig.
4. **Na completion-move, vóór resultaatcomment**: taak staat al in `done/`/`failed/`,
   `state == COMPLETED`/`FAILED`, maar `STATUS.yaml.result_comment_posted == false`. De nieuwe
   sessie moet uitsluitend nog de korte resultaatenvelop op de PR plaatsen (met de via
   `resolve_task_commits.py` opgehaalde commit-SHA), en daarna `result_comment_posted` op
   `true` zetten (via een kleine, aparte vervolgcommit — nooit zelfreferentieel in dezelfde
   commit als de completion-move zelf).

### HOLD/ABORT (nieuw, punt 5)

`STATUS.yaml.hold` (`active`/`reason`/`set_at`/`set_by`) staat in de instructieprecedentie
BOVEN het Mark-besluitenregister, PR-comments en chattekst, maar ONDER de canonieke
`TASK.yaml`/`TASK.md` zelf. Zolang `hold.active == true` blokkeert `validate_task.py` harde
uitvoering (de taak mag nog wel gelezen/gerapporteerd worden, niet inhoudelijk worden
uitgevoerd). Dit formaliseert precies het patroon dat al informeel gebruikt is in deze sessie
(een `CCI_HOLD`-PR-comment die uitvoering pauzeerde) — vanaf nu hoort een HOLD in het
taakbestand zelf, niet uitsluitend in een PR-comment die kan wegraken tussen lange threads.

### Forbidden-writes-afdwinging (nieuw, punt 12 "verboden write-path")

`complete_task.py` roept vóór elke completion verplicht `check_forbidden_writes.py` aan. Dat
script bepaalt de claim-commit (niet-circulair, via `resolve_task_commits.py`), en vergelijkt
ALLE bestanden die sindsdien zijn gewijzigd — inclusief NIEUWE, ongetrackte bestanden
(`git diff` alleen toont GEEN untracked bestanden, dus `git ls-files --others` wordt apart
meegenomen; dit was een echte bug die tijdens deze hardeningsronde is gevonden en gefixt) —
tegen de `forbidden_writes`-padpatronen. Bestanden die al vóór het claimen vuil/ongetrackt
waren (bv. een ander, apart vastgehouden werk zoals een `CCI_HOLD`) worden via een
claimtijd-snapshot (`STATUS.yaml.pre_existing_dirty_paths`, met map-prefixmatching) uitgesloten
van deze taak — anders zou ELKE taak blokkeren zolang er ander werk ligt te wachten. **Bekende
resterende beperking**: als een pad al vóór het claimen vuil was ÉN deze taak dat exacte pad
verder wijzigt, wordt dat NIET apart gedetecteerd (path-niveau uitsluiting, geen content-diff
tegen de claimtijd-snapshot) — voor een striktere garantie zou een inhoudelijke snapshot-diff
nodig zijn, buiten scope van deze hardeningsronde.

### Non-fast-forward

Bij het pushen van een taak-commit geldt dezelfde regel als elders in deze sessie — nooit
force-pushen. Bij een non-fast-forward-conflict: STOP, meld het als blocker in de
resultaatenvelop, wacht op een nieuwe taak/instructie.

### Cross-regio nummeringscontrole (nu gebouwd, punt 8)

`india5/scripts/validate_global_numbering.py` (puur lezend) scant alle
`runs/*/NUMBERING_REGISTRY.jsonl`-bestanden repositorybreed en garandeert dat geen display_id
ooit in twee regio's aan verschillende fysieke locaties hangt, en dat een candidate_id nooit met
een ander nummer in een andere registry voorkomt. Gerapporteerd bereik per regio (nu:
VARANASI 001-040) laat een nieuwe regio vooraf een niet-overlappend bereik reserveren. Raakt
geen bestaand registrybestand aan.

### Governance-PR versus regio-PR's (nu vastgelegd, punt 7)

Zie `india5/GOVERNANCE.md` sectie 9: governance/canonieke architectuur hoort in
versiebeheerde bestanden, onafhankelijk van welke PR ze introduceert; elke toekomstige regio
krijgt idealiter een eigen run en bij voorkeur een eigen PR; PR #23 blijft Varanasi + deze
architectuurmigratie en wordt niet de permanente queue voor alle regio's.

### Autonome regioflow (punt 6)

Eén taak met `scope: REGION_FULL_FLOW` kan `PRE-BRONS → BRONS → ZILVER → GOUD/TRAVEL` volledig
autonoom doorlopen. Interne fasen mogen eigen checkpoints/batches hebben (zoals de bestaande
`BRONS-B01`..`B04`-batchstructuur), maar dat zijn GEEN aparte taken in `india5/tasks/` en Mark
hoeft ze niet apart te starten — dat is precies het "Autonome regio-doorloop"-principe dat al in
`india4/protocols/INDIA5-PROTOCOL.md` staat, nu ook op taakarchitectuurniveau bevestigd.

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
