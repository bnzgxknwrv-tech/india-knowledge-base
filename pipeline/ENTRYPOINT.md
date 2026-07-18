# ENTRYPOINT — BRONS / ZILVER / GOUD v3.1.1

Dit is het enige startpunt voor een nieuwe uitvoerende AI-sessie.

## Verplichte eerste instructie

Iedere startvraag aan BRONS, ZILVER of GOUD begint met:

`Activeer in deze chat onmiddellijk de GitHub-connector en houd deze gedurende de volledige uitvoering beschikbaar. Dit onderzoek gebruikt GitHub als enige bron van waarheid en overdrachtskanaal. Test vóór ieder inhoudelijk werk zowel GitHub-read als GitHub-write voor repository bnzgxknwrv-tech/india-knowledge-base. Ontbreekt read of write, antwoord dan uitsluitend: MARK: IK MIS GITHUB CONNECTOR! Ga alleen verder wanneer beide aantoonbaar werken.`

Een worker beweert nooit dat hij een connector in een andere chat heeft geactiveerd. De gebruiker activeert de connector; de worker test de feitelijke toegang.

## Universele activatie

Na de verplichte eerste instructie volstaat:

`Open pipeline/ENTRYPOINT.md en voer uitsluitend de actie uit die in pipeline/NEXT_ACTION.yaml staat.`

`NEXT_ACTION.yaml` bepaalt exact één run, rol, expected state, contextmanifest en — uitsluitend voor nieuwe gepinde runs — één `post_completion`-actie. Een worker leidt geen andere rol of vervolgactie af.

## Verplichte volgorde

1. Test GitHub-read en GitHub-write.
2. Open `pipeline/NEXT_ACTION.yaml`.
3. Controleer route, run, expected state, contextmanifest en eventuele `post_completion`- en `canonical_integration`-velden.
4. Open `research/active/<run-id>/run.yaml` en `state.yaml`.
5. Controleer dat geen `ACTIVE` claim bestaat en state/eventcursor overeenkomen.
6. Lees het gepinde rolcontract, methodologie, evidence-protocol en quality gate.
7. Lees uitsluitend het contextmanifest en de daarin genoemde runbestanden.
8. Controleer source commit, hashes, volledigheid en sentinels.
9. Claim de fase met `claim_status: ACTIVE` volgens `EXECUTION_PROTOCOL.md`.
10. Voer uitsluitend de inhoudelijke rol en scope uit.
11. Schrijf alle verplichte outputs naar het toegewezen fasepad.
12. Valideer artifacts, bronverwijzingen, scope en sentinels.
13. Schrijf manifest, handoff en COMPLETED; sluit de workerclaim met `claim_status: CLOSED` in dezelfde completioncommit; synchroniseer state en events.
14. Commit de volledige fase-uitkomst en voer finale readback uit.
15. Controleer daarna uitsluitend de expliciet gepinde `post_completion`-modus:
    - zonder geldige nieuwe pin: stop en gebruik het oude routingproces;
    - `INLINE_POST_PHASE_CONTROLLER`: controleer dat de workerclaim `CLOSED` is, beëindig de workerrol formeel en voer daarna als afzonderlijke controllerrol het gepinde `ROLE_HANDOFF_PROTOCOL.md` en `CONTROLLER_TRANSITION_PROTOCOL.md` uit;
    - `MARK_FINAL_REPORT`: maak als GOUD het volledige gepinde Markrapport en canonieke integratievoorstel, voer alleen expliciet gepinde deterministische integratie uit, valideer alles en lever het rapport rechtstreeks aan Mark.

De worker maakt nooit als worker het contextmanifest van zijn opvolger. Alleen een afzonderlijke controllerrol doet dit.

## Expliciete rolwissel

Een sessie mag alleen naar `INLINE_POST_PHASE_CONTROLLER` wisselen wanneer `run.yaml` en `NEXT_ACTION.yaml` dit expliciet pinnen. De rolwissel vereist:

- volledige workercompletion en fasecommit;
- workerclaim `CLOSED` met dezelfde completioncommit;
- geen verdere fase-outputwrites;
- nieuwe GitHub-preflight;
- opnieuw lezen van de controllerprotocollen;
- een afzonderlijke `ACTIVE` controllerclaim;
- uitsluitend controllerwrites;
- sluiting van de controllerclaim in de transitioncommit;
- finale readback vóór een volgende startopdracht.

De workerclaim wordt nooit als controllerclaim hergebruikt.

## GOUD en de canonieke kennisbasis

GOUD vervangt de normale INDIA2-eindredactie door een volledig `MARK_FINAL_REPORT.md`. Om te voorkomen dat `knowledge/places/registry.jsonl` en `decisions/INDEX.yaml` achterlopen, schrijft GOUD tevens een gepind `CANONICAL_INTEGRATION_PROPOSAL.md`.

GOUD mag alleen mechanische, niet-beslissende integratie toepassen wanneer `canonical_integration.mode: DETERMINISTIC_NON_DECISIONAL` expliciet is gepind. Nieuwe of gewijzigde formele/adviserende A/B/C-statussen, nieuwe decision-ID's en nieuwe beslisteksten zijn verboden. Wanneer Mark moet beslissen, blijft de betreffende canonieke wijziging onuitgevoerd en bevat het eindrapport exact één beslispunt.

## Compatibiliteit

Oude, reeds gepinde of geclaimde runs worden niet stil gemigreerd. Ontbreekt een geldige `post_completion`-pin of het gepinde `ROLE_HANDOFF_PROTOCOL.md`, dan stopt BRONS of ZILVER na completion en routeert volgens het oude protocol naar SUBREGIE INDIA of een afzonderlijke controller. GOUD routeert in dat geval volgens zijn oude gepinde contract.

## Inhoudelijke prioriteit

Iedere toekomstige plaats-sweep behandelt ook:

- waarom devotees naar de plek gaan;
- wat mensen er werkelijk doen;
- of Mark respectvol kan deelnemen;
- sfeer, actuele beleving en representatieve beelden;
- institutionele, historische, lineage- en traditiebevestiging als afzonderlijke domeinen;
- praktische controles en nabijheid tot relevante ankers.

## Stopvoorwaarden

Stop zonder inhoudelijk werk wanneer:

- GitHub-read of GitHub-write ontbreekt;
- `NEXT_ACTION.yaml`, run, rol of context ontbreekt of tegenstrijdig is;
- een `ACTIVE` claim bestaat;
- state en eventlog elkaar tegenspreken;
- een required file ontbreekt, afgekapt is of een gepinde hash afwijkt;
- de output niet volledig kan worden geschreven.

Bij ontbrekende GitHub-toegang is het volledige antwoord uitsluitend:

`MARK: IK MIS GITHUB CONNECTOR!`

## Geen protocolwerk tijdens een onderzoeksfase

Een uitvoerende rol wijzigt tijdens dezelfde run nooit zijn rolcontract, methodologie, protocol, contextregels of schemas. Nieuwe pipelineversies gelden alleen voor runs die deze vóór de eerste claim expliciet pinnen.

END_OF_ARTIFACT