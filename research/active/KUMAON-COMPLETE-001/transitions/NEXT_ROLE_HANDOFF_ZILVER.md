RESULTAATSTATUS: PARTIAL
RUN_ID: KUMAON-COMPLETE-001
VOLTOOIDE_ROL: BRONS
FASE_COMPLETION_COMMIT: 9afdbb21ab4cb202144c2a6346218d6e1a3639aa
WORKER_CLAIM_CLOSED: YES
TRANSITION_COMMIT: THIS_ATOMIC_COMMIT
CONTROLLER_CLAIM_CLOSED: YES
NEXT_ROLE: ZILVER
NEXT_ROLE_READY: YES
NEXT_EXPECTED_STATE: READY_FOR_ZILVER
NEXT_CONTEXT_MANIFEST: research/active/KUMAON-COMPLETE-001/context/ZILVER_CONTEXT.yaml
HOOGSTE_BLOCKERS: kleine/private locaties en historische micro-sites; buitengebied-WORKING_GEO; onvolledige beeld- en reviewdekking; winterwegen/trails/taxi/parking/reistijden; december 2026-spoordiensten

VOLGENDE_METAAL_STARTOPDRACHT_BEGIN
GitHub ZILVER:

Activeer in deze chat onmiddellijk de GitHub-connector en houd deze gedurende de volledige uitvoering beschikbaar. Dit onderzoek gebruikt GitHub als enige bron van waarheid en overdrachtskanaal. Test vóór ieder inhoudelijk werk zowel GitHub-read als GitHub-write voor repository bnzgxknwrv-tech/india-knowledge-base. Ontbreekt read of write, antwoord dan uitsluitend: MARK: IK MIS GITHUB CONNECTOR!

Open pipeline/ENTRYPOINT.md in repository bnzgxknwrv-tech/india-knowledge-base.

Controleer dat pipeline/NEXT_ACTION.yaml semantisch exact deze lower-case velden bevat:
- run_id: KUMAON-COMPLETE-001
- route: ZILVER
- expected_state: READY_FOR_ZILVER
- context_manifest: research/active/KUMAON-COMPLETE-001/context/ZILVER_CONTEXT.yaml

Voer uitsluitend de aangewezen actie uit. Lees uitsluitend het gepinde contextmanifest en de daarin genoemde required files en expliciet getriggerde optional files. Haal de volledige gevalideerde BRONS-output uit GitHub; gebruik deze geplakte overdracht niet als onderzoeksbron.

Voer het volledige gepinde ZILVER-rolcontract, de methodologie, protocollen en quality gates uit. Stop bij ontbrekende GitHub-write, een ACTIVE bestaande claim, state/event-desynchronisatie, ontbrekend of afgekapt required bestand, hashafwijking, ongeldige bronreferenties of een andere gepinde stopvoorwaarde.

Schrijf en commit de volledige ZILVER-fase. Sluit de workerclaim aantoonbaar in de completioncommit. Wanneer NEXT_ACTION de modus INLINE_POST_PHASE_CONTROLLER expliciet toestaat, beëindig daarna de workerrol en voer als afzonderlijke controllerrol uitsluitend de geldige transition naar GOUD uit. Sluit ook de controllerclaim in de transitioncommit en lever alleen bij geldige finale readback de GOUD-handoff.
VOLGENDE_METAAL_STARTOPDRACHT_EINDE

END_OF_ARTIFACT
