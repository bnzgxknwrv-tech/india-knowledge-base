# ENTRYPOINT — BRONS / ZILVER / GOUD

Dit is het enige startpunt voor een nieuwe uitvoerende AI-sessie.

## Verplichte eerste instructie in iedere metaalopdracht

Iedere startvraag aan BRONS, ZILVER of GOUD begint met deze tekst:

`Activeer in deze chat onmiddellijk de GitHub-connector en houd deze gedurende de volledige uitvoering beschikbaar. Dit onderzoek gebruikt GitHub als enige bron van waarheid en overdrachtskanaal. Test vóór ieder inhoudelijk werk zowel GitHub-read als GitHub-write voor repository bnzgxknwrv-tech/india-knowledge-base. Ontbreekt read of write, antwoord dan uitsluitend: MARK: IK MIS GITHUB CONNECTOR! Ga alleen verder wanneer beide aantoonbaar werken.`

Een worker mag nooit beweren de connector zelf te hebben geactiveerd wanneer die niet beschikbaar is. De gebruiker activeert de connector in de chat; de worker test de feitelijke toegang.

## Universele activatie

Na de verplichte eerste instructie volstaat:

`Open pipeline/ENTRYPOINT.md en voer uitsluitend de actie uit die in pipeline/NEXT_ACTION.yaml staat.`

`NEXT_ACTION.yaml` bepaalt exact één run, rol, expected state en contextmanifest. Een worker leidt geen andere rol of vervolgactie af.

## Verplichte volgorde

1. Test GitHub-read en GitHub-write.
2. Open `pipeline/NEXT_ACTION.yaml`.
3. Controleer dat route, run, expected state en contextmanifest bestaan en onderling overeenstemmen.
4. Open `research/active/<run-id>/run.yaml` en `state.yaml`.
5. Controleer dat geen geldige claim actief is en state/eventcursor overeenkomen.
6. Lees het gepinde rolcontract, methodologie, evidence-protocol en quality gate.
7. Lees uitsluitend het contextmanifest en de daarin genoemde runbestanden.
8. Controleer source commit, hashes, volledigheid en sentinels.
9. Claim de fase volgens `EXECUTION_PROTOCOL.md`.
10. Voer uitsluitend de inhoudelijke rol en scope uit.
11. Schrijf alle verplichte outputs naar het toegewezen fasepad.
12. Valideer artifacts, bronverwijzingen, scope en sentinels.
13. Schrijf manifest, handoff, COMPLETED, state en events.
14. Commit de volledige fase-uitkomst en stop.

De worker maakt nooit zelf het contextmanifest van zijn opvolger. SUBREGIE INDIA of een geldige controllertransition doet dit.

## Inhoudelijke prioriteit

De metalen onderzoeken niet alleen bewijsbeperkingen. Iedere toekomstige plaats-sweep behandelt ook:

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
- een geldige bestaande claim bestaat;
- state en eventlog elkaar tegenspreken;
- een required file ontbreekt, afgekapt is of een gepinde hash afwijkt;
- de output niet volledig kan worden geschreven.

Bij ontbrekende GitHub-toegang is het volledige antwoord uitsluitend:

`MARK: IK MIS GITHUB CONNECTOR!`

## Geen protocolwerk tijdens een onderzoeksfase

Een uitvoerende rol wijzigt tijdens dezelfde run nooit zijn eigen rolcontract, methodologie, protocol, contextregels of schemas. Verbeteringen gebeuren na afloop via SUBREGIE INDIA en worden alleen ingevoerd wanneer zij aantoonbaar kwaliteit verhogen of Marks werk verminderen.

END_OF_ARTIFACT