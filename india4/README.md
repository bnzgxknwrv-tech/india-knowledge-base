# INDIA 4

Status: ACTIVE

INDIA 4 is de eenvoudige onderzoeksworkflow voor India-runs. De vaste route is:

BRONS -> ZILVER -> GOUD -> KLAAR

Er is geen controller, transitionchat, SHA-matrix of verplicht contextmanifest. Iedere rol leest de oorspronkelijke runopdracht en de voorgangeroutput rechtstreeks uit GitHub, schrijft één volledige overdracht, commit en levert exact één startvraag voor de volgende rol.

## Start
Gebruik `india4/START.md`.

## Structuur
- `india4/roles/`: drie inhoudelijke rollen.
- `india4/protocols/`: zes korte kwaliteitsprotocollen.
- `india4/templates/`: run-, handoff- en completionmodellen.
- `runs/active/<run_id>/`: één runbestand, rolmappen en één statusbestand.
- `runs/completed/<run_id>/`: afgesloten runs.

## Besluitregel
Alleen Mark maakt nieuwe A/B/C-keuzes. Een worker bewaart bestaande keuzes en noteert andere kandidaten als `DOOR_MARK_TE_BEOORDELEN`.

## Blokkeerregel
Alleen ontbrekende GitHub-read/write, ontbrekende runopdracht, ontbrekende of corrupte voorgangeroutput, geldige eerdere voltooiing van dezelfde rol, of een direct conflict met een expliciet Mark-besluit blokkeert een volledige rol. Kandidaatgebonden onzekerheid wordt geïsoleerd en blokkeert andere kandidaten niet.
