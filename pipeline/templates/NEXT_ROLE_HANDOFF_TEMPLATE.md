# NEXT_ROLE_HANDOFF_TEMPLATE v1.0

Gebruik uitsluitend na een geldige inline controllertransition.

```text
RESULTAATSTATUS: <COMPLETED|PARTIAL|BLOCKED|FAILED>
RUN_ID: <run-id>
VOLTOOIDE_ROL: <BRONS|ZILVER>
FASE_COMPLETION_COMMIT: <sha|NONE>
TRANSITION_COMMIT: <sha|NONE>
NEXT_ROLE: <ZILVER|GOUD>
NEXT_ROLE_READY: <YES|NO>
NEXT_EXPECTED_STATE: <READY_FOR_ZILVER|READY_FOR_GOUD>
NEXT_CONTEXT_MANIFEST: <pad|NONE>
HOOGSTE_BLOCKERS: <NONE|korte lijst>

VOLGENDE_METAAL_STARTOPDRACHT_BEGIN
GitHub <ZILVER|GOUD>:

Activeer in deze chat onmiddellijk de GitHub-connector en houd deze gedurende de volledige uitvoering beschikbaar. Dit onderzoek gebruikt GitHub als enige bron van waarheid en overdrachtskanaal. Test vóór ieder inhoudelijk werk zowel GitHub-read als GitHub-write voor repository bnzgxknwrv-tech/india-knowledge-base. Ontbreekt read of write, antwoord dan uitsluitend: MARK: IK MIS GITHUB CONNECTOR!

Open pipeline/ENTRYPOINT.md in repository bnzgxknwrv-tech/india-knowledge-base.

Controleer dat pipeline/NEXT_ACTION.yaml exact verwijst naar:
- RUN_ID: <run-id>
- ROUTE: <ZILVER|GOUD>
- EXPECTED_STATE: <READY_FOR_ZILVER|READY_FOR_GOUD>
- CONTEXT_MANIFEST: <pad>

Voer uitsluitend de aangewezen actie uit. Lees uitsluitend het gepinde contextmanifest en de daarin genoemde required files. Haal de volledige gevalideerde predecessoroutput uit GitHub; gebruik deze geplakte overdracht niet als onderzoeksbron.

Voer het volledige gepinde rolcontract, de methodologie, protocollen en quality gates uit. Stop bij ontbrekende GitHub-write, geldige bestaande claim, state/event-desynchronisatie, ontbrekend of afgekapt required bestand, hashafwijking, ongeldige bronreferenties of een andere gepinde stopvoorwaarde.

Schrijf en commit de volledige fase. Wanneer NEXT_ACTION de modus INLINE_POST_PHASE_CONTROLLER expliciet toestaat, beëindig daarna de workerrol en voer als afzonderlijke controllerrol uitsluitend de geldige transition naar het volgende metaal uit. Bij GOUD: schrijf verplicht het volledige MARK_FINAL_REPORT, valideer de finale readback en lever het rapport rechtstreeks aan Mark.
VOLGENDE_METAAL_STARTOPDRACHT_EINDE
```

Wanneer `NEXT_ROLE_READY: NO`, vervang het volledige startopdrachtblok door:

`VOLGENDE_METAAL_STARTOPDRACHT: GEEN — EERST BLOCKER OPLOSSEN.`

De waarden in dit blok moeten exact overeenkomen met de gecommitte GitHub-state. De volgende rol vertrouwt uitsluitend GitHub.

END_OF_ARTIFACT