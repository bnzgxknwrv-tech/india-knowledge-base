# Research runs

## Structuur

```text
research/
  active/
    <run-id>/
      run.yaml
      state.yaml
      events.jsonl
      scope.md
      context/
      BRONS/
      ZILVER/
      GOUD/
  completed/
    <run-id>/
```

Iedere run is geïsoleerd. Een rol leest nooit automatisch andere active of completed runs. Gerelateerde eerdere onderzoeken worden alleen zichtbaar wanneer het fase-contextmanifest ze expliciet noemt.

## Overdracht

BRONS, ZILVER en GOUD schrijven hun eigen volledige fase-output in hun eigen map. De volgende rol leest deze output via het gepinde contextmanifest. Mark hoeft geen rapport tussen chats te kopiëren.

## Archief

Na verwerking van GOUD door de regisseur wordt de run naar `completed/` verplaatst. Git-geschiedenis is de onveranderlijke historie; er worden geen overbodige duplicaat-historymappen gemaakt.

## Groottegrens

Geen primair Markdown- of JSONL-bestand boven 1500 regels. Splits kandidaten, claims of bronnen in genummerde delen wanneer nodig en laat `INDEX.md` of het manifest de verplichte volgorde vastleggen.

END_OF_ARTIFACT
