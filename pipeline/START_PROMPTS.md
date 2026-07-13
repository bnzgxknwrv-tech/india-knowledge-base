# Minimale activaties

Iedere rol draait in een volledig nieuwe chat met GitHub-lees- en schrijfrechten. Er wordt geen rapporttekst tussen chats geplakt.

## BRONS

```text
Open pipeline/ENTRYPOINT.md in repository bnzgxknwrv-tech/india-knowledge-base. Voer rol BRONS uit voor run <run-id>. Lees uitsluitend het gepinde contextmanifest. Schrijf alle resultaten naar GitHub en stop bij ontbrekende write-toegang, SHA-afwijking, truncatie, geldige bestaande claim of state-desynchronisatie.
```

## CONTROLLER na BRONS

```text
Open pipeline/protocols/CONTROLLER_TRANSITION_PROTOCOL.md in repository bnzgxknwrv-tech/india-knowledge-base. Voer de controllertransition uit voor run <run-id> van BRONS_COMPLETE naar READY_FOR_ZILVER. Valideer BRONS volledig, genereer ZILVER_CONTEXT.yaml op de definitieve BRONS-resultaatcommit en schrijf uitsluitend de toegestane transitionbestanden.
```

## ZILVER

```text
Open pipeline/ENTRYPOINT.md in repository bnzgxknwrv-tech/india-knowledge-base. Voer rol ZILVER uit voor run <run-id>. Lees uitsluitend het door de controller gepinde contextmanifest en haal de volledige BRONS-output uit GitHub. Schrijf alle resultaten naar GitHub en stop bij ontbrekende write-toegang, SHA-afwijking, truncatie, geldige bestaande claim of state-desynchronisatie.
```

## CONTROLLER na ZILVER

```text
Open pipeline/protocols/CONTROLLER_TRANSITION_PROTOCOL.md in repository bnzgxknwrv-tech/india-knowledge-base. Voer de controllertransition uit voor run <run-id> van ZILVER_COMPLETE naar READY_FOR_GOUD. Valideer ZILVER volledig, genereer GOUD_CONTEXT.yaml op de definitieve ZILVER-resultaatcommit en schrijf uitsluitend de toegestane transitionbestanden.
```

## GOUD

```text
Open pipeline/ENTRYPOINT.md in repository bnzgxknwrv-tech/india-knowledge-base. Voer rol GOUD uit voor run <run-id>. Lees uitsluitend het door de controller gepinde contextmanifest en haal de volledige ZILVER-output uit GitHub. Schrijf het definitieve dossier en vrijgavebesluit naar GitHub en stop bij ontbrekende write-toegang, SHA-afwijking, truncatie, geldige bestaande claim of state-desynchronisatie.
```

## Regisseur

De regisseur ontvangt alleen:
- run-id;
- GOUD-commit;
- pad naar `GOUD/manifest.yaml` en `GOUD/report/INDEX.md`;
- status `PASS`, `PARTIAL` of `BLOCKED`.

BRONS en ZILVER blijven zichtbaar in hun eigen runmappen voor controle en latere verbetering van de werkwijze.

Alle uitvoerende rollen en controllertransitions vereisen GitHub-lees- en schrijfrechten. Modellen zonder deze rechten kunnen geen BRONS-, ZILVER-, GOUD- of controllerworker zijn.

END_OF_ARTIFACT