# BRONS → ZILVER operationele handoff

RESULTAATSTATUS: PARTIAL
RUN_ID: KUMAON-ROUTE-OPTIMIZATION-001
VOLTOOIDE_ROL: BRONS
FASE_COMPLETION_COMMIT: 73c11932a17f9ab0186c32621597c21a8f8b1984
WORKER_CLAIM_CLOSED: YES
TRANSITION_COMMIT: THIS_ATOMIC_COMMIT
CONTROLLER_CLAIM_CLOSED: YES
NEXT_ROLE: ZILVER
NEXT_ROLE_READY: YES
NEXT_EXPECTED_STATE: READY_FOR_ZILVER
NEXT_CONTEXT_MANIFEST: research/active/KUMAON-ROUTE-OPTIMIZATION-001/context/ZILVER_CONTEXT.yaml
HOOGSTE_BLOCKERS: NONE

VOLGENDE_METAAL_STARTOPDRACHT_BEGIN
GitHub ZILVER:

Activeer in deze chat onmiddellijk de GitHub-connector en houd deze gedurende de volledige uitvoering beschikbaar. Dit onderzoek gebruikt GitHub als enige bron van waarheid en overdrachtskanaal. Test vóór ieder inhoudelijk werk zowel GitHub-read als GitHub-write voor repository bnzgxknwrv-tech/india-knowledge-base. Ontbreekt read of write, antwoord dan uitsluitend: MARK: IK MIS GITHUB CONNECTOR!

Open pipeline/ENTRYPOINT.md in repository bnzgxknwrv-tech/india-knowledge-base.

Controleer dat pipeline/NEXT_ACTION.yaml semantisch exact deze lower-case velden bevat:
- run_id: KUMAON-ROUTE-OPTIMIZATION-001
- route: ZILVER
- expected_state: READY_FOR_ZILVER
- context_manifest: research/active/KUMAON-ROUTE-OPTIMIZATION-001/context/ZILVER_CONTEXT.yaml

Voer uitsluitend de aangewezen actie uit. Lees uitsluitend het gepinde contextmanifest en de daarin genoemde required files. Haal de volledige gevalideerde predecessoroutput uit GitHub; gebruik deze geplakte overdracht niet als onderzoeksbron.

Voer het volledige gepinde rolcontract, de methodologie, protocollen en quality gates uit. Stop bij ontbrekende GitHub-write, een ACTIVE bestaande claim, state/event-desynchronisatie, ontbrekend of afgekapt required bestand, hashafwijking, ongeldige bronreferenties of een andere gepinde stopvoorwaarde.

Schrijf en commit de volledige fase. Sluit de workerclaim aantoonbaar in de completioncommit. Wanneer NEXT_ACTION de modus INLINE_POST_PHASE_CONTROLLER expliciet toestaat, beëindig daarna de workerrol en voer als afzonderlijke controllerrol uitsluitend de geldige transition naar het volgende metaal uit. Sluit ook de controllerclaim in de transitioncommit. Bij GOUD: schrijf verplicht het volledige MARK_FINAL_REPORT en CANONICAL_INTEGRATION_PROPOSAL, voer alleen gepinde deterministische canonieke integratie uit, valideer de finale readback en lever het rapport rechtstreeks aan Mark.
VOLGENDE_METAAL_STARTOPDRACHT_EINDE

END_OF_ARTIFACT
