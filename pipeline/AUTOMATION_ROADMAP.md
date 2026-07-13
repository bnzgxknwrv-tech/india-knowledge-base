# Automation roadmap — minimale MARK-belasting

## Doelbeeld

Mark hoeft uiteindelijk alleen een onderzoeksopdracht te geven en na GOUD een inhoudelijk eindpakket te beoordelen. Technische transitions, validaties, repinning en routing verlopen automatisch.

## Niveau 1 — direct toepasbaar

- Iedere rol gebruikt het SELF_ROUTING_PROTOCOL.
- Iedere rol noemt exact de bestemming en één volgende handeling voor Mark.
- Iedere rol levert een volledig kopieerbaar `DOORSTUURTEKST`-blok.
- Mark hoeft workerberichten niet meer te interpreteren.
- Een universele startopdracht vervangt afzonderlijke lange BRONS-, ZILVER- en GOUD-prompts.

Handwerk voor Mark: connector activeren, universele startopdracht plakken, één slotblok doorsturen.

## Niveau 2 — repository-controller via GitHub Actions

Een workflow reageert op wijzigingen in `research/active/*/state.yaml` en `*/COMPLETED`.

De workflow:

1. valideert JSONL/YAML, sentinels, required outputs, unieke IDs en source-referenties;
2. vergelijkt state en eventlog;
3. bepaalt de definitieve predecessorcommit;
4. genereert het volgende gepinde contextmanifest;
5. schrijft het transitionevent en de READY-state;
6. actualiseert `pipeline/NEXT_ACTION.yaml`;
7. stopt hard bij iedere fout en schrijft een machineleesbaar blockerbestand.

Handwerk voor Mark: alleen connector activeren en in iedere nieuwe chat dezelfde universele startopdracht plakken. Tussen BRONS, ZILVER en GOUD is geen terugkeer naar SUBREGIE INDIA nodig wanneer de Action groen is.

## Niveau 3 — één GitHub-dispatchpunt

Gebruik één vast GitHub Issue of een repositorybestand als mailbox:

- titel/bestand: `INDIA_PIPELINE_DISPATCH`;
- bevat actieve run, volgende rol, status, contextpad en laatste validatie;
- workers lezen dit als eerste na ENTRYPOINT;
- GitHub Actions actualiseert het na iedere geldige transition.

Mark hoeft geen run-id of rol meer te onthouden.

## Niveau 4 — volledige externe orchestratie

Een externe orchestrator, bijvoorbeeld n8n of een eigen controllerdienst, gebruikt:

- een GitHub App/token voor repository-read/write;
- model-API's voor afzonderlijke BRONS-, ZILVER- en GOUD-uitvoeringen;
- webresearchtools per agent;
- een deterministische state machine;
- menselijke goedkeuring uitsluitend bij projectbesluiten of BLOCKED.

Deze laag kan workers automatisch na elkaar starten. Dit kan niet betrouwbaar worden bereikt door de ChatGPT-connector zelf, omdat een chat de connector niet autonoom in een andere chat kan activeren.

## Aanbevolen volgorde

1. SELF_ROUTING_PROTOCOL invoeren.
2. `NEXT_ACTION.yaml` en universele startopdracht invoeren.
3. Een read-only validator als GitHub Action bouwen.
4. Pas na meerdere groene runs automatische controllerwrites toestaan.
5. Daarna eventueel n8n/API-orchestratie toevoegen.

## Veiligheidsgrens

Automatisering mag nooit:

- A/B/C toekennen;
- inhoudelijke onzekerheid gladstrijken;
- een BLOCKED-run automatisch forceren;
- actieve claims overschrijven;
- gepinde input wijzigen;
- INDIA2 belasten met technische logs.

END_OF_ARTIFACT