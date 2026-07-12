# ENTRYPOINT — BRONS / ZILVER / GOUD

Dit is het enige startpunt voor een nieuwe uitvoerende AI-sessie.

## Activatie

Een controller of Mark activeert exact één rol voor exact één run:

`Open pipeline/ENTRYPOINT.md. Voer rol <BRONS|ZILVER|GOUD> uit voor run <run-id>. Lees uitsluitend het gepinde contextmanifest. Schrijf alle resultaten naar GitHub en stop bij ontbrekende write-toegang, SHA-afwijking, truncatie, geldige bestaande claim of state-desynchronisatie.`

Geen rapporttekst wordt tussen chats geplakt. GitHub is het enige overdrachtskanaal.

## Verplichte volgorde

1. Controleer lees- en schrijfrechten voor de repository.
2. Open `research/active/<run-id>/run.yaml`.
3. Controleer dat de gevraagde rol overeenkomt met `state.yaml` en dat de verwachte fase gereed is.
4. Lees het gepinde rolcontract uit `run.yaml`.
5. Lees het gepinde protocol- en methodologiebestand uit `run.yaml`.
6. Lees uitsluitend `research/active/<run-id>/context/<ROLE>_CONTEXT.yaml` en de daarin genoemde bestanden.
7. Controleer `source_commit`, hashes, vereiste bestanden en contextbudget.
8. Claim de fase volgens `pipeline/protocols/EXECUTION_PROTOCOL.md`.
9. Voer de rol uit en schrijf uitsluitend naar het toegewezen fasepad.
10. Valideer alle verplichte outputs, sentinels en verwijzingen.
11. Schrijf `manifest.yaml`, `handoff.yaml`, `COMPLETED`, update `state.yaml` en append één event aan `events.jsonl`.
12. Commit de volledige fase-uitkomst.

## Stopvoorwaarden

Stop zonder inhoudelijk werk wanneer:
- GitHub-write ontbreekt;
- run of rol niet bestaat;
- `source_commit` niet overeenkomt;
- een niet-verlopen geldige claim van een andere worker bestaat;
- state en eventlog elkaar tegenspreken;
- het contextmanifest ontbreekt of niet volledig gelezen kan worden;
- een required file ontbreekt of een expected hash niet klopt;
- output wordt afgekapt of een verplichte sectie niet kan worden voltooid.

Schrijf bij een stop alleen een `BLOCKED`-event en, indien toegestaan, de blokkade in `state.yaml`. Maak geen gedeeltelijk fase-resultaat geldig.

## Verbod

Een uitvoerende rol wijzigt tijdens dezelfde run nooit zijn eigen rolcontract, methodologie, protocol, contextregels of schemas. Verbeteringen gebeuren na afloop in een afzonderlijke commit of pull request.

END_OF_ARTIFACT
