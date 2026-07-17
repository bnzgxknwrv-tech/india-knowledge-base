# Consensusmatrix: ONE-SHOT BRONS–ZILVER–GOUD

Status: OPEN_FOR_CLAUDE_REVIEW

Doel: ChatGPT en Claude nemen per architectuurpunt een expliciet standpunt in. Alleen punten met wederzijdse ACCEPT of een gezamenlijk geaccepteerde vervanging gaan naar de uiteindelijke consensusversie.

## C-01 — Normale uitvoeringsmodus

Voorstel ChatGPT:

`EXTERNAL_ORCHESTRATED` is de normale modus. Een enkele gewone chat is uitsluitend fallback.

ChatGPT-oordeel: ACCEPT.

Claude-oordeel: OPEN.

Consensus: OPEN.

## C-02 — Externe orchestrator

Voorstel ChatGPT:

Gebruik n8n op Marks server als eerste implementatiekeuze, tenzij Claude een aantoonbaar eenvoudiger en veiliger alternatief onderbouwt.

ChatGPT-oordeel: ACCEPT_WITH_COMPARISON.

Claude-oordeel: OPEN.

Consensus: OPEN.

## C-03 — Verse run per metaal

Voorstel ChatGPT:

BRONS, ZILVER en GOUD draaien ieder in een afzonderlijke verse modelrun.

ChatGPT-oordeel: ACCEPT — HARD REQUIREMENT.

Claude-oordeel: OPEN.

Consensus: OPEN.

## C-04 — GitHub als enige duurzame waarheid

Voorstel ChatGPT:

Chatcontext is tijdelijk. Alleen GitHub-state, events, manifests, claims, bronnen, checkpoints en completions zijn duurzaam en overdraagbaar.

ChatGPT-oordeel: ACCEPT — HARD REQUIREMENT.

Claude-oordeel: OPEN.

Consensus: OPEN.

## C-05 — Geen tweede concurrerende statebron

Voorstel ChatGPT:

`state.yaml`, `events.jsonl` en `NEXT_ACTION.yaml` blijven canoniek. n8n mag uitvoeringsmetadata bewaren maar die mag de repository-state niet overrulen.

ChatGPT-oordeel: ACCEPT.

Claude-oordeel: OPEN.

Consensus: OPEN.

## C-06 — Controllertransitions blijven afzonderlijk

Voorstel ChatGPT:

Eén gebruikersopdracht betekent niet dat rollen worden samengevoegd. Na BRONS en ZILVER blijft een afzonderlijke technische controllertransition verplicht.

ChatGPT-oordeel: ACCEPT — HARD REQUIREMENT.

Claude-oordeel: OPEN.

Consensus: OPEN.

## C-07 — Worker/controller write-scheiding

Voorstel ChatGPT:

Workers schrijven alleen eigen fase-output plus toegestane claim/state/events. Controllers schrijven alleen opvolgercontext, state/events, NEXT_ACTION en transitionvalidatie.

ChatGPT-oordeel: ACCEPT.

Claude-oordeel: OPEN.

Consensus: OPEN.

## C-08 — Checkpoint behoudt claim

Voorstel ChatGPT:

Een hervatting gebruikt dezelfde claim en een idempotency key. Een checkpoint maakt geen completion en geen nieuwe claim.

ChatGPT-oordeel: ACCEPT — HARD REQUIREMENT.

Claude-oordeel: OPEN.

Consensus: OPEN.

## C-09 — Seriële GitHub-writes

Voorstel ChatGPT:

Writes naar hetzelfde pad zijn single-writer en serieel. Voor update wordt steeds de actuele blob-SHA gelezen en na write volgt readback.

ChatGPT-oordeel: ACCEPT — HARD REQUIREMENT.

Claude-oordeel: OPEN.

Consensus: OPEN.

## C-10 — Artifactsplit en truncatie

Voorstel ChatGPT:

Primaire bestanden blijven onder 1500 regels; intensief gewijzigde JSONL-delen streven naar maximaal 500 regels. Een mogelijk getrunceerde read mag nooit de basis zijn voor volledige vervanging.

ChatGPT-oordeel: ACCEPT_WITH_TESTING.

Claude-oordeel: OPEN.

Consensus: OPEN.

## C-11 — ZILVER-onafhankelijkheid

Voorstel ChatGPT:

ZILVER draait altijd vers. Een andere provider dan BRONS heeft voorkeur maar is niet verplicht; onafhankelijkheid wordt primair door contextisolatie, adversarial opdracht en gepinde inputs bewaakt.

ChatGPT-oordeel: ACCEPT.

Claude-oordeel: OPEN.

Consensus: OPEN.

## C-12 — GOUD-onafhankelijkheid

Voorstel ChatGPT:

GOUD draait altijd vers en leest alleen ZILVER plus expliciet gepinde loss-controlbestanden.

ChatGPT-oordeel: ACCEPT — HARD REQUIREMENT.

Claude-oordeel: OPEN.

Consensus: OPEN.

## C-13 — Automatische retries

Voorstel ChatGPT:

Alleen transiënte technische fouten krijgen maximaal drie automatische retries. Voor iedere retry worden state en SHA’s opnieuw gelezen. Inhoudelijke blockers worden niet automatisch omzeild.

ChatGPT-oordeel: ACCEPT.

Claude-oordeel: OPEN.

Consensus: OPEN.

## C-14 — Pushmelding na commit

Voorstel ChatGPT:

Notificatie wordt pas verzonden na eindcommit en finale readback. Een notificatiefout mag geen onderzoek herstarten.

ChatGPT-oordeel: ACCEPT.

Claude-oordeel: OPEN.

Consensus: OPEN.

## C-15 — Actieve runs niet stil migreren

Voorstel ChatGPT:

Het nieuwe protocol wordt eerst met een synthetische test-run gevalideerd. Een al geclaimde actieve run blijft onder de gepinde oude protocollen werken, tenzij Mark expliciet een migratie autoriseert.

ChatGPT-oordeel: ACCEPT — HARD REQUIREMENT.

Claude-oordeel: OPEN.

Consensus: OPEN.

## C-16 — Eén eindantwoord aan Mark

Voorstel ChatGPT:

Tijdens normale autonome uitvoering ontvangt Mark geen handmatige overdrachtsteksten. Hij ontvangt alleen een pushmelding en één eindrapport, behalve bij een harde blocker die zijn beslissing vereist.

ChatGPT-oordeel: ACCEPT.

Claude-oordeel: OPEN.

Consensus: OPEN.

## Consensusregel

Een punt wordt `CONSENSUS_ACCEPTED` wanneer:

1. ChatGPT en Claude beide ACCEPT geven; of
2. één CHANGE voorstelt en de ander de exacte vervanging accepteert.

Een punt blijft `MARK_DECISION_REQUIRED` wanneer:

- de voorstellen inhoudelijk botsen;
- kosten, providerkeuze of infrastructuur een persoonlijke voorkeur van Mark vereist;
- de veiligheids- of betrouwbaarheidsafweging niet technisch eenduidig is.

Na Claude-review schrijft SUBREGIE INDIA een nieuw document:

`pipeline/proposals/ONE_SHOT_BZG_CONSENSUS_FINAL.md`

Dat document bevat uitsluitend:

- geaccepteerde architectuurbesluiten;
- resterende Mark-beslissingen;
- minimale testimplementatie;
- definitieve startopdracht;
- implementatievolgorde.

Er wordt niets geïmplementeerd voordat Mark de finale consensus accepteert.

END_OF_ARTIFACT