# RESULT.md — INDIA5-ARCH-HARDEN-002

## Samenvatting

Alle 12 verplichte onderzoekspunten zijn doorlopen. Tijdens het dogfooden van de eigen
taakarchitectuur zijn **vier echte bugs** gevonden en gefixt (niet alleen documentatie):
1. `complete_task.py` controleerde `expected_outputs` op het verkeerde pad (al gevonden en
   gefixt tijdens INDIA5-ARCH-TEST-001, hier opnieuw bevestigd).
2. `expected_head`-exactgelijkheid was zelf-tegensprekend: het aanmaken/claimen van een taak
   verzet HEAD altijd voorbij de eigen `expected_head` — gefixt met een voorouder-check.
3. Handgeschreven YAML met een ongequote `#` (`"PR #23 CCI_TASK_ENVELOPE..."`) werd door de
   YAML-parser als commentaar geïnterpreteerd en stilzwijgend afgekapt bij de eerste
   her-serialisatie — data-integriteitsbug, gecorrigeerd + als les vastgelegd.
4. `check_forbidden_writes.py` gebruikte aanvankelijk alleen `git diff`, dat toont GEEN nieuwe
   (untracked) bestanden — een echte verboden write op een nieuw bestand zou dus ongemerkt
   voorbij zijn gegaan. Gefixt door `git ls-files --others` mee te nemen, en vervolgens een
   tweede laag gefixt: de reeds-vuile-paden-uitsluiting (nodig omdat andere, vastgehouden
   taken zoals de PRE-BRONS-bestanden anders altijd als "overtreding" werden gezien) moest
   map-prefixmatching gebruiken, niet exacte string-vergelijking.

## Bevindingen per punt

**1. git_commit_at_claim/git_commit_at_complete blijven null.** Gedocumenteerd als
fundamenteel niet-circulair oplosbaar (het bestand kan de hash van zijn eigen committende
commit niet bevatten). Niet-circulaire oplossing gebouwd: `resolve_task_commits.py`, een
read-only `git log --diff-filter=A`-opzoeking. Geverifieerd tegen de echte geschiedenis:
`INDIA5-ARCH-TEST-001` → claim_commit `0eb79f4`, complete_commit `568338d` (beide kloppen
tegen `git log`); `INDIA5-ARCH-HARDEN-002` → claim_commit `29c0a63` (klopt).

**2. expected_head-circulariteit.** Herzien van exacte gelijkheid naar een voorouder-check
(`git merge-base --is-ancestor`). Getest: (a) de eigen claim-commit (HEAD ligt legitiem ná
expected_head) → OK; (b) een synthetische divergente commit (aparte, nooit-gepushte branch,
achteraf verwijderd, geen sporen) → correct als `STALE_EXPECTED_HEAD` geblokkeerd.

**3. Exactly-once-semantiek.** Eén actieve taak systeembreed: getest (poging tot claim tijdens
actieve taak → geweigerd). Dezelfde taak niet tweemaal claimbaar: getest (taak niet meer in
queue/ na claim → natuurlijke weigering "niet gevonden"). Voltooide taak niet opnieuw
uitvoerbaar: NIEUW gebouwd (`claim_task.py` weigert nu expliciet als `task_id` al in `done/`/
`failed/` bestaat) en getest (kopie van `INDIA5-ARCH-TEST-001` teruggezet in `queue/`,
claimpoging correct geweigerd, kopie verwijderd). Parallelle sessie: geen code-mechanisme
nodig — git zelf serialiseert via fast-forward-only pushes; recoveryprocedure gedocumenteerd
(fetchen, lokale claim intrekken bij conflict, nooit force-pushen).

**4. Crashherstel, vier toestanden.** Alle vier gedocumenteerd in `TASK_PROTOCOL.md`. Toestand
1-3 vereisten geen nieuwe code (het ontwerp was al hervatbaar). Toestand 4 (na completion-move,
vóór resultaatcomment) miste een marker om te weten of de comment al geplaatst was — nieuw
veld `STATUS.yaml.result_comment_posted` toegevoegd aan het schema.

**5. Instructieprecedentie + HOLD/ABORT.** Vijfledige precedentielijst herzien en canoniek
vastgelegd in zowel `TASK_PROTOCOL.md` als `GOVERNANCE.md` sectie 6. HOLD-mechanisme NIEUW
gebouwd: `STATUS.yaml.hold`-object + afdwinging in `validate_task.py` (`check_hold()`). Getest
met een tijdelijke kopie van `STATUS.yaml` (hold.active=true → validatie faalt met duidelijke
reden; hersteld naar origineel → validatie slaagt weer).

**6. Autonome regioflow.** Gedocumenteerd in `TASK_PROTOCOL.md`: `scope: REGION_FULL_FLOW` kan
`PRE-BRONS → BRONS → ZILVER → GOUD/TRAVEL` dragen; interne batches/checkpoints blijven bestaan
maar zijn geen aparte `india5/tasks/`-taken. Cross-verwijzing naar het bestaande "Autonome
regio-doorloop"-principe in `india4/protocols/INDIA5-PROTOCOL.md` (geen duplicatie).

**7. Governance versus regio-uitvoering.** Vastgelegd in `GOVERNANCE.md` sectie 9: governance
in versiebeheerde bestanden, toekomstige regio's krijgen eigen run + bij voorkeur eigen PR, PR
#23 wordt niet de permanente queue. Geen nieuwe PR aangemaakt in deze taak (niet gevraagd, wel
expliciet "PR #23 niet mergen" gerespecteerd).

**8. Globale nummeringsvalidator.** Nieuw gebouwd: `validate_global_numbering.py`, puur lezend.
Getest tegen de echte, bestaande `NUMBERING_REGISTRY.jsonl` (Varanasi, 40 nummers) —
`VALIDATIE OK`, geen wijziging aan het bestand. Rapporteert het huidige bereik (001-040) zodat
een toekomstige regio vooraf een niet-overlappend bereik kan reserveren.

**9. Machineleesbare kennistoets-rubriek.** Nieuw gebouwd: `india5/schemas/knowledge_gate.schema.json`
+ `india5/templates/KNOWLEDGE_GATE_REVIEW_TEMPLATE.md` + `validate_knowledge_gate.py`. Getest
met een minimale, geldige voorbeeldreview (12 onderwerpen, alle PASS) → `VALIDATIE OK`.

**10. Governancemigratie.** `india5/GOVERNANCE.md` aangemaakt met alle 7 gevraagde
onderwerpen: rolverdeling Mark/INDIA2/CCI (1), PDF-op-verzoek (2, cross-ref naar bestaand
canoniek bestand), detectorbibliotheek-governance (3), PRE-BRONS-output/verzadigingsregels (4),
immutable numbering (5, cross-ref), instructieprecedentie (6, nieuw), task-file-relay (7,
cross-ref). Waar een besluit al canoniek elders stond, is uitsluitend samengevat + doorverwezen
om duplicatie te vermijden.

**11. Vastgehouden PRE-BRONS-bestanden.** Volledig geïnventariseerd + regel-voor-regel
vergeleken met de canonieke INDIA2-besluiten in `PRE_BRONS_HOLD_INVENTORY.md` (aparte,
reviewbare bijlage bij deze taak, blijft in de taakdirectory, wordt NIET elders gecommit).
Conclusie: geen inhoudelijke afwijking gevonden. De bestanden zelf blijven ONGECOMMIT, zoals
voorgeschreven — deze hardeningstaak committeert uitsluitend taakarchitectuurbestanden onder
`india5/`.

**12. Negatieve tests.** Zie testmatrix hieronder — alle uitgevoerd met wegwerpbare
kopieën/branches, geen enkel spoor achtergelaten in de definitieve staat.

## Testmatrix

| # | Test | Resultaat |
|---|---|---|
| 1 | Stale expected_head (divergente commit) | PASS -- correct geblokkeerd |
| 2 | expected_head = eigen claim-commit (legitieme opvolger) | PASS -- correct toegestaan |
| 3 | Dubbele claim (tweede claimpoging op reeds actieve taak) | PASS -- correct geweigerd |
| 4 | Ontbrekende completion marker in RESULT.md | PASS -- correct geweigerd |
| 5 | Gewijzigd TASK.md ná hashvastlegging (tamper) | PASS -- correct gedetecteerd |
| 6 | Verboden write-path (nieuw bestand op forbidden-pad) | PASS -- correct geweigerd (na fix van de untracked-bug) |
| 7 | Completed task opnieuw claimen | PASS -- correct geweigerd (na nieuwe check toe te voegen) |
| 8 | Twee queued taken terwijl één active is | PASS -- queue toegestaan, claim correct geweigerd |
| 9 | Afgekapt/ontbrekend taakbestand (TASK.md verwijderd) | PASS -- correct gedetecteerd |
| 10 | HOLD actief blokkeert validatie | PASS -- correct geblokkeerd, correct hersteld na unhold |
| 11 | expected_outputs-pad vóór/ná completion-move | PASS (bug gevonden+gefixt in INDIA5-ARCH-TEST-001, hier herbevestigd) |
| 12 | resolve_task_commits.py tegen echte geschiedenis | PASS -- klopt voor beide bestaande taken |
| 13 | validate_global_numbering.py tegen echte Varanasi-data | PASS -- 40/40, geen wijziging aan het bestand |
| 14 | validate_knowledge_gate.py met geldige voorbeeldreview | PASS |
| 15 | forbidden_writes-check negeert reeds-vuile paden correct (pre_existing_dirty_paths) | PASS (na map-prefixmatch-fix) |

## Gewijzigde/nieuwe bestanden

**Nieuw:**
- `india5/GOVERNANCE.md`
- `india5/.gitignore`
- `india5/schemas/knowledge_gate.schema.json`
- `india5/templates/KNOWLEDGE_GATE_REVIEW_TEMPLATE.md`
- `india5/scripts/resolve_task_commits.py`
- `india5/scripts/check_forbidden_writes.py`
- `india5/scripts/validate_global_numbering.py`
- `india5/scripts/validate_knowledge_gate.py`
- `india5/tasks/queue/INDIA5-ARCH-HARDEN-002/TASK.md` + `TASK.yaml` (later verplaatst)
- `india5/tasks/active/INDIA5-ARCH-HARDEN-002/PRE_BRONS_HOLD_INVENTORY.md`
- `india5/tasks/active/INDIA5-ARCH-HARDEN-002/RESULT.md` (dit bestand)

**Gewijzigd:**
- `india5/TASK_PROTOCOL.md` (versie 1.0.0 -> 1.1.0: niet-circulaire commit-resolutie,
  expected_head-semantiek, crashherstel-vier-toestanden, HOLD/ABORT, forbidden-writes-
  afdwinging, cross-regio nummeringscontrole nu gebouwd, governance-PR-beleid)
- `india5/schemas/status.schema.json` (`pre_existing_dirty_paths`, `hold`, `result_comment_posted`)
- `india5/scripts/validate_task.py` (voorouder-check i.p.v. exacte gelijkheid, `check_hold()`)
- `india5/scripts/claim_task.py` (immutable task_id-check, `pre_existing_dirty_paths`-snapshot)
- `india5/scripts/complete_task.py` (verplichte `check_forbidden_writes.py`-aanroep)
- `india5/tasks/active/INDIA5-ARCH-HARDEN-002/STATUS.yaml` (retroactief `pre_existing_dirty_paths`
  toegevoegd, YAML-truncatiebug in de ISSUED-regel gecorrigeerd)

**NIET gewijzigd/gecommit** (expliciet buiten scope): `india4/` (alle PRE-BRONS-bestanden
blijven ongecommit, zie `PRE_BRONS_HOLD_INVENTORY.md`), `runs/` (geen Varanasi-data of GEO
aangeraakt), geen A/B/C-, hotel-, KML- of PDF-wijziging.

## Resterende risico's

- **Forbidden-writes-detectie op pad-niveau, niet content-niveau**: als een pad al vóór het
  claimen vuil was ÉN deze taak dat exacte pad verder wijzigt, wordt die extra wijziging niet
  apart gedetecteerd. Voor een striktere garantie is een content-snapshot-diff nodig (buiten
  scope van deze ronde).
- **Parallelle-sessie-race is niet volledig automatisch getest** (vereist twee echte,
  gelijktijdige checkouts) — de bescherming (git fast-forward + documented recovery) is
  ontworpen en beargumenteerd, niet end-to-end met twee live processen bewezen.
- **YAML-handauteurschap blijft een risico**: het gevonden `#`-truncatiebug laat zien dat elk
  handgeschreven (niet-via-script) YAML-bestand in `india5/tasks/queue/` een vergelijkbaar risico
  loopt. Aanbeveling voor een volgende ronde: een klein hulpscript dat een nieuwe TASK.yaml/
  STATUS.yaml altijd via `yaml.safe_dump` genereert, nooit handmatig.
- **`india4/`-inhoud blijft ongecommit**: functioneel klaar volgens de inventarisatie, maar
  vereist nog een aparte, expliciete vrijgave-opdracht voordat de PRE-BRONS-inhoud echt kan
  worden gebruikt.

## ARCHITECTURE_READY_FOR_CONTENT_TASKS: YES

Met de kanttekening dat de drie resterende risico's hierboven bekend en gedocumenteerd zijn,
niet blokkerend voor normaal gebruik, en dat de PRE-BRONS-inhoud zelf (in `india4/`) een aparte
vrijgave-opdracht nodig heeft vóórdat de eerste echte inhoudelijke taak (discovery of
coverage-audit) kan starten.

## Voorstel voor de eerstvolgende inhoudelijke taak (NIET uitgevoerd)

Voorgestelde volgende taak: `INDIA5-VNS-DISCOVERY-COVERAGE-003` — een taakenvelop-gedreven
uitvoering van de eerder afgesproken, begrensde `VARANASI_DISCOVERY_COVERAGE_AUDIT`
(retroactieve dekkingscontrole op de bestaande 40 kandidaten, geen A/B/C-wijziging), nu via de
nieuwe `india5/tasks/`-architectuur in plaats van losse PR-comments. Vereist eerst: (a) een
expliciete vrijgave-opdracht om de vastgehouden `india4/`-PRE-BRONS-bestanden te committen, (b)
een eerste echte, inhoudelijk gedefinieerde detector (bv. AOAY, met volledige definitie) in
`india4/registries/DETECTOR_LIBRARY.jsonl` als PROVISIONAL. Beide worden hier uitdrukkelijk
NIET uitgevoerd, alleen voorgesteld.

INDIA5-TASK-COMPLETE::INDIA5-ARCH-HARDEN-002
