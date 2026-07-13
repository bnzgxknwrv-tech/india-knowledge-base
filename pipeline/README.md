# BRONS–ZILVER–GOUD-pijplijn v2.1

## Status

**IMPLEMENTATIE GEREED VOOR INTEGRATIETEST.**

De architectuur en transitionregels zijn aanwezig. De pipeline wordt pas `OPERATIONEEL BEWEZEN` genoemd nadat één volledige end-to-end proefrun BRONS → controller → ZILVER → controller → GOUD zonder protocolfout is afgerond.

## Doel

Eén onderzoeksrun wordt in drie opeenvolgende, volledig nieuwe AI-sessies opgebouwd. GitHub is het enige overdrachtskanaal.

1. **BRONS** detecteert breed en bouwt de eerste volledige faseversie.
2. **CONTROLLER** valideert BRONS en genereert het gepinde ZILVER-contextmanifest.
3. **ZILVER** verifieert, spreekt tegen, vult aan en bouwt een volledige verbeterde faseversie.
4. **CONTROLLER** valideert ZILVER en genereert het gepinde GOUD-contextmanifest.
5. **GOUD** synthetiseert, valideert en levert het enige dossier voor de regisseur.

De onderzoeksrollen en controller kunnen worden uitgevoerd door iedere AI die de repository volledig kan lezen én schrijven en het betreffende contract volgt. Modellen zonder GitHub-write kunnen deze rollen niet uitvoeren.

## Start

Iedere uitvoerende onderzoekssessie begint bij `pipeline/ENTRYPOINT.md` met alleen een run-id en rol. Controllertransitions beginnen bij `pipeline/protocols/CONTROLLER_TRANSITION_PROTOCOL.md`. Er wordt geen voorgangerrapport in de chat geplakt.

Bij runcreatie bestaat alleen `BRONS_CONTEXT.yaml`. ZILVER en GOUD krijgen hun contextmanifest pas nadat de controller de vorige fase volledig heeft gevalideerd en op de definitieve resultaatcommit heeft gepind.

## Architectuur

- `knowledge/methodology/` — generieke onderzoeksmethodologie;
- `knowledge/project/` — India-specifieke overlays en projectdata;
- `pipeline/roles/` — modelonafhankelijke rolcontracten;
- `pipeline/protocols/` — uitvoering, context, controllertransitions en bewijs;
- `pipeline/templates/` — run- en artifacttemplates;
- `research/active/<run-id>/` — geïsoleerde lopende run;
- `research/completed/<run-id>/` — afgeronde, standaard niet-ingelezen run.

## Verplichte principes

- Nooit “lees de repository”; altijd “lees het gepinde contextmanifest”.
- Iedere run is geïsoleerd.
- Iedere fase schrijft naar haar eigen map.
- De worker genereert nooit het contextmanifest van zijn opvolger.
- Iedere transition wordt door een apart geactiveerde controller uitgevoerd.
- Rapporten zijn logisch volledig maar fysiek opgesplitst.
- Geen primair bestand boven 1500 regels.
- Claims en bronnen zijn ook machineleesbaar vastgelegd.
- Iedere tekstartifact eindigt met `END_OF_ARTIFACT`.
- Geen `COMPLETED` zonder herlezing en validatie.
- Geen protocolwijziging midden in een run.
- Alleen Mark kent A/B/C toe.

## Methodologie

Methodology v2.0 onderzoekt blijvende spirituele bestemmingen via afzonderlijke lagen: fysieke identiteit, institutionele identiteit, historische identiteit, traditie, lineage, levende praktijk, bezoekbaarheid en getuigenissen.

Verschillende soorten onderbouwing worden nooit samengevoegd tot één totaalscore. Mythische of bovennatuurlijke figuren worden onderzocht via gedragen traditie en lineage, niet via een onmogelijke klassieke biografische bewijsproef.

Projectspecifieke interpretatie-overlays staan apart in `knowledge/project/OVERLAYS_INDIA.md`.

## Doorontwikkeling

India2, Claude, ChatGPT en andere bevoegde schrijvers mogen de pipeline na een run verbeteren via een expliciete commit of pull request. Iedere verbetering:
- benoemt een waargenomen fout of kwaliteitswinst;
- controleert gevolgen voor alle drie rollen en de controller;
- verhoogt `pipeline/VERSION.md`;
- respecteert AI_RULES en Marks exclusieve beslissingsrecht;
- verandert nooit stil de gepinde regels van een actieve run.

END_OF_ARTIFACT