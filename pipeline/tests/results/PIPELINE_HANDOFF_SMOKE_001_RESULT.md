# PIPELINE-HANDOFF-SMOKE-001 — resultaat

Branch: `implementation/minimal-bzg-handoff`

Testspec: `pipeline/tests/PIPELINE_HANDOFF_SMOKE_001.md`

Fixturemap: `pipeline/tests/fixtures/PIPELINE-HANDOFF-SMOKE-001/`

Documentatiecorrectie:
- `pipeline/templates/RUN_TEMPLATE_V3.md` bevat nu `run_type: <CLUSTER_SWEEP|TARGETED_SUPPLEMENT|SYNTHETIC_TEST>`;
- correctiecommit: `6344fa47436e15111b89de11cda1cc09dc2bc067`.

Synthetische fixture- en uitvoercommit: `1c3bb20c1eb926a775f3609cb93eacf973a0c97c`.

Validator:
- script: `pipeline/tests/fixtures/PIPELINE-HANDOFF-SMOKE-001/validate_smoke.py`;
- output: `pipeline/tests/fixtures/PIPELINE-HANDOFF-SMOKE-001/VALIDATOR_OUTPUT.txt`;
- uitkomst: `ALL_TESTS_A_M: PASS`.

## Isolatie

Uitsluitend synthetische fixturedata gebruikt. De fixture bevat drie kunstmatige kandidaten, fixturekopieën van registry en decisions-index, een zelfstandig GOUD-rapport en een afzonderlijke chatweergave.

Niet gewijzigd:
- `pipeline/NEXT_ACTION.yaml`;
- `research/active/VRINDAVAN-KUMAON-CORRIDOR-001`;
- andere echte actieve runs;
- `knowledge/places/registry.jsonl`;
- `decisions/INDEX.yaml`.

De diff van de smoke-uitvoering vanaf correctiecommit `6344fa47436e15111b89de11cda1cc09dc2bc067` tot fixturecommit `1c3bb20c1eb926a775f3609cb93eacf973a0c97c` bevat uitsluitend bestanden onder `pipeline/tests/fixtures/PIPELINE-HANDOFF-SMOKE-001/`.

## Test A — happy path en claimsluiting

- Fixture: `fixture.json`, `run.yaml`, GOUD-rapport en integratievoorstel.
- Verwacht: BRONS → afzonderlijke inline controller → ZILVER → afzonderlijke inline controller → GOUD; gesloten worker- en controllerclaims; exact drie inhoudelijke chats; rapport rechtstreeks voor Mark.
- Feitelijk: volledige statevolgorde gevalideerd; vijf unieke claims doorliepen ACTIVE → CLOSED; workerclaims zijn niet als controllerclaim hergebruikt; geen fasewrites na rolwissel; contexten en NEXT_ACTION-routes volgen BRONS, ZILVER, GOUD; GOUD-rapport en integratievoorstel bestaan.
- Commit: `1c3bb20c1eb926a775f3609cb93eacf973a0c97c`.
- Resultaat: `PASS`.

## Test B — ontbrekende sentinel

- Fixture: scenario B in `fixture.json`.
- Verwacht: transition blokkeert zonder context, READY-state of prompt.
- Feitelijk: ontbrekende sentinel gedetecteerd; alle drie vervolgacties bleven uit.
- Commit: `1c3bb20c1eb926a775f3609cb93eacf973a0c97c`.
- Resultaat: `PASS`.

## Test C — ongeldige source-ID

- Fixture: kandidaat SYN-003 met `SRC-MISSING-999`.
- Verwacht: transition blokkeert.
- Feitelijk: bron-ID ontbreekt uit de synthetische source registry en de overgang is geblokkeerd.
- Commit: `1c3bb20c1eb926a775f3609cb93eacf973a0c97c`.
- Resultaat: `PASS`.

## Test D — state/event-desynchronisatie

- Fixture: scenario D in `fixture.json`.
- Verwacht: DESYNC/TRANSITION_BLOCKED en geen opvolgercontext.
- Feitelijk: `BRONS_COMPLETE` tegenover laatste event `BRONS_CLAIMED` werd als desync gedetecteerd en geblokkeerd.
- Commit: `1c3bb20c1eb926a775f3609cb93eacf973a0c97c`.
- Resultaat: `PASS`.

## Test E — stale handoff en stale NEXT_ACTION

- Fixture: scenario E in `fixture.json`.
- Verwacht: GitHub-state wint; stale ZILVER-chat claimt niet wanneer NEXT_ACTION GOUD noemt; hashmismatch stopt worker.
- Feitelijk: alle drie situaties leverden de vereiste GitHub-first uitkomst en stop op.
- Commit: `1c3bb20c1eb926a775f3609cb93eacf973a0c97c`.
- Resultaat: `PASS`.

## Test F — write-scope en ongesloten workerclaim

- Fixture: scenario F in `fixture.json`.
- Verwacht: controller mag fase-output niet wijzigen; geen claimhergebruik; ACTIVE of onvolledig gesloten predecessor blokkeert; commitmismatch blokkeert.
- Feitelijk: alle vijf verboden situaties zijn geweigerd.
- Commit: `1c3bb20c1eb926a775f3609cb93eacf973a0c97c`.
- Resultaat: `PASS`.

## Test G — oud protocol

- Fixture: scenario G zonder post_completion-pin.
- Verwacht: oud proces; geen inline transition.
- Feitelijk: fallback naar oud proces geselecteerd en inline transition geweigerd.
- Commit: `1c3bb20c1eb926a775f3609cb93eacf973a0c97c`.
- Resultaat: `PASS`.

## Test H — GOUD-rapportkwaliteit

- Fixture: `GOUD/MARK_FINAL_REPORT.md`.
- Verwacht: zelfstandig rapport met eindantwoord, status, kandidaten, afwijzingen, onzekerheden, vervolg, integratie, technische controle, artifacts en afsluiting.
- Feitelijk: alle verplichte rapportsecties en `END_OF_ARTIFACT` aanwezig.
- Commit: `1c3bb20c1eb926a775f3609cb93eacf973a0c97c`.
- Resultaat: `PASS`.

## Test I — chat-versus-commit-pariteit

- Fixture: `GOUD/MARK_FINAL_REPORT.md` en `GOUD/CHAT_OUTPUT.txt`.
- Verwacht: inhoud exact gelijk na verwijdering van toegestane wrapper en slotroutering.
- Feitelijk: byte-inhoud na normalisatie exact gelijk.
- Commit: `1c3bb20c1eb926a775f3609cb93eacf973a0c97c`.
- Resultaat: `PASS`.

## Test J — concurrerende sessies en claimrace

- Fixture: scenario J in `fixture.json`.
- Verwacht: eerste claim geaccepteerd; tweede geweigerd; bij twee metaalclaims exact één winnaar; nieuwe claim alleen op actuele state.
- Feitelijk: alle vier race-uitkomsten conform protocol.
- Commit: `1c3bb20c1eb926a775f3609cb93eacf973a0c97c`.
- Resultaat: `PASS`.

## Test K — transitioncommit-drift

- Fixture: scenario K in `fixture.json`.
- Verwacht: predecessorcommit-mismatch blokkeert; statewijziging zonder event geeft NEXT_ROLE_READY NO; claim/transitioncommit-mismatch geeft geen handoff.
- Feitelijk: alle drie driftgevallen geblokkeerd.
- Commit: `1c3bb20c1eb926a775f3609cb93eacf973a0c97c`.
- Resultaat: `PASS`.

## Test L — deterministische canonieke integratie

- Fixture: `fixture_registry_before.jsonl`, `fixture_registry_after.jsonl`, fixture-decisionsbestanden en integratievoorstel.
- Verwacht: alleen technische artifactpad-/bestaande LOCATION_ID-integratie; geen A/B/C-wijziging, adviserend label, nieuw decision-ID of nieuwe beslistekst; beslisafhankelijke wijziging blijft uit.
- Feitelijk: alleen `artifact_path` veranderde; LOCATION_ID's bleven uniek; formele statussen en decisions bleven identiek; verboden writes zijn geblokkeerd; `mark_decision_required: YES` zichtbaar.
- Commit: `1c3bb20c1eb926a775f3609cb93eacf973a0c97c`.
- Resultaat: `PASS`.

## Test M — productiepoort

- Fixture: scenario M en synthetische `run.yaml`.
- Verwacht: echte run geblokkeerd vóór geldig resultaat; alleen SYNTHETIC_TEST-uitzondering toegestaan; NO blokkeert; YES opent pas na merge.
- Feitelijk: alle poorttoestanden conform specificatie. De productiepoort wordt pas na merge operationeel.
- Commit: `1c3bb20c1eb926a775f3609cb93eacf973a0c97c`.
- Resultaat: `PASS`.

## Samenvatting A–M

- A: PASS
- B: PASS
- C: PASS
- D: PASS
- E: PASS
- F: PASS
- G: PASS
- H: PASS
- I: PASS
- J: PASS
- K: PASS
- L: PASS
- M: PASS

SMOKE_TEST_STATUS: PASS

PRODUCTION_READY: YES

Geen productiesweep gestart. De bestaande corridor-run blijft op haar oude gepinde schema-v2-proces.

END_OF_ARTIFACT
