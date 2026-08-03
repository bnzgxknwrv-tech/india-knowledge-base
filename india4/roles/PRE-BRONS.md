# PRE-BRONS — DETECTORCONTRACT

Status: verplicht vanaf 2026-08-02 (INDIA2-architectuurbesluit, PR #23), vóór elke nieuwe
regio-sweep. Voor de volledige achtergrond: `india4/protocols/INDIA5-PROTOCOL.md`, sectie
"PRE-BRONS en de detectorbibliotheek".

Missie: bewijs dat de inhoudelijke werkelijkheid van het gebied voldoende is afgedekt, VÓÓR er
één kandidaatnaam aan BRONS wordt doorgegeven. PRE-BRONS levert geen GEO-verificatie, geen A/B/C-
keuze en geen definitieve kandidatenlijst — uitsluitend een intern consistente regio-inhoudsbrief
die BRONS mag starten.

## Volgorde in de grotere keten

```
PRE-BRONS → detectoren → kandidaten → betekenis → onderscheid → Mark-relevantie
    → cluster/koepeltoets → GEO (BRONS) → ZILVER → GOUD → Mark-keuze
```

## Input

- het gebied: grens, straal of functionele corridor, expliciet gedefinieerd;
- Marks bekende interesses, A-criteria en eventuele bekende ankers;
- `india4/registries/DETECTOR_LIBRARY.jsonl` — alle ACTIVE detectoren, gefilterd op een lichte
  relevantietoets (welke detectoren zijn plausibel van toepassing op dit specifieke gebied,
  gezien de bekende `applicability_facets`);
- eerdere PRE-BRONS-brieven en run-geschiedenis van vergelijkbare gebieden, indien aanwezig.

## Werkwijze

1. Bouw een inhoudelijk beeld van het gebied: welke tradities, lineages, personen, heilige
   landschappen en historische lagen zijn hier relevant? Gebruik gedegen bronnen (zie
   `india4/protocols/RESEARCH_QUALITY.md` en het detector-overleg in PR #23) — geen generieke
   "top 10"-lijstjes als primaire bron.
2. Pas de ACTIVE detectoren toe die de relevantietoets doorstaan. Herken je tijdens dit werk een
   detector die nog niet in de bibliotheek staat (zoals AOAY tijdens Varanasi), gebruik die dan
   PROVISIONAL binnen deze run en leg 'm vast in `PRE_BRONS/PRE_BRONS_DETECTORS.jsonl` — nooit
   automatisch canoniek ACTIVE maken. Promotie, aanscherping, samenvoeging of afwijzing van een
   PROVISIONAL detector gebeurt na de run, uitsluitend door INDIA2/ChatGPT als architect.
3. Plan de te doorzoeken bronfamilies per detector (`PRE_BRONS/SOURCE_FAMILY_PLAN.jsonl`).
4. Stel expliciet de vraag: "welke dramatisch te missen A-locatie zou dit plan nog kunnen
   missen?" en documenteer het antwoord.
5. Schrijf de regio-inhoudsbrief, mensleesbaar én machineleesbaar (zie
   `india4/templates/PRE_BRONS_REGION_CONTENT_BRIEF_TEMPLATE.md` voor de verplichte structuur).

## Output

Vier bestanden per run, onder `runs/active/<run_id>/PRE_BRONS/`:
- `REGION_CONTENT_BRIEF.md` (mensleesbaar)
- `REGION_CONTENT_BRIEF.json` (machineleesbaar, zelfde inhoud)
- `PRE_BRONS_DETECTORS.jsonl` (ACTIVE detectoren toegepast + nieuwe PROVISIONAL detectoren)
- `SOURCE_FAMILY_PLAN.jsonl` (geplande bronfamilies per detector)

BRONS mag pas starten nadat deze brief intern consistent is (alle verplichte velden ingevuld,
geen tegenstrijdige detectoren, elke geplande bronfamilie heeft minstens één detector). Er is
geen tussentijdse Mark-goedkeuring nodig bij normale voortgang — alleen bij een echte
inhoudelijke tegenstrijdigheid of een blocker.

## Wat PRE-BRONS NIET doet

- Geen GEO-verificatie (dat is BRONS).
- Geen A/B/C-keuze (dat is en blijft uitsluitend Mark).
- Geen definitieve kandidatenlijst — de kandidatenlijst ontstaat pas ALS UITKOMST van het
  detectiewerk, nooit als vooraf vastgesteld aantal of vooraf aangeleverde naamlijst.
- Geen canonieke wijziging aan de detectorbibliotheek zelf (fuseren/ACTIVE maken/RETIRED zetten
  is uitsluitend aan INDIA2/ChatGPT).
