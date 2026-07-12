# BRONS–ZILVER–GOUD-pijplijn v2.0

## Doel

Eén onderzoeksrun wordt in drie opeenvolgende, volledig nieuwe AI-sessies opgebouwd. GitHub is het enige overdrachtskanaal.

1. **BRONS** detecteert breed en bouwt de eerste volledige faseversie.
2. **ZILVER** verifieert, spreekt tegen, vult aan en bouwt een volledige verbeterde faseversie.
3. **GOUD** synthetiseert, valideert en levert het enige dossier voor de regisseur.

De rollen kunnen worden uitgevoerd door iedere AI die de repository volledig kan lezen én schrijven en het rolcontract volgt.

## Start

Iedere uitvoerende sessie begint bij `pipeline/ENTRYPOINT.md` met alleen een run-id en rol. Er wordt geen voorgangerrapport in de chat geplakt.

## Architectuur

- `knowledge/methodology/` — generieke onderzoeksmethodologie;
- `knowledge/project/` — India-specifieke overlays en projectdata;
- `pipeline/roles/` — modelonafhankelijke rolcontracten;
- `pipeline/protocols/` — uitvoering, context en bewijs;
- `pipeline/templates/` — run- en artifacttemplates;
- `research/active/<run-id>/` — geïsoleerde lopende run;
- `research/completed/<run-id>/` — afgeronde, standaard niet-ingelezen run.

## Verplichte principes

- Nooit “lees de repository”; altijd “lees het gepinde contextmanifest”.
- Iedere run is geïsoleerd.
- Iedere fase schrijft naar haar eigen map.
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
- controleert gevolgen voor alle drie rollen;
- verhoogt `pipeline/VERSION.md`;
- respecteert AI_RULES en Marks exclusieve beslissingsrecht;
- verandert nooit stil de gepinde regels van een actieve run.

END_OF_ARTIFACT
