# TASK — TOP11-EXTERNAL-AI-BENCHMARK-001

```
task_id: TOP11-EXTERNAL-AI-BENCHMARK-001
issued_by: INDIA
issued_at: 2026-08-16
mode: MULTI-DETECTOR_RECALL_BENCHMARK
```

## Aanleiding
CCI heeft `TOP11-INDIA-PERSON-CENTRIC-MEGASWEEP-001` afgerond met circa 90 atlaspunten en 11/11 `PERSON_SWEEP_SATURATED: JA`. Dit is nog NIET als bewezen volledige waarheid geaccepteerd. De eigen synthese vermeldt dat de definitieve passes methodisch selectief waren en dat o.a. een brede Vivekananda-reisperiode gebundeld is. Marks doel van het 'andersommetje' is maximale recall van verifieerbare fysieke India-touchpoints per Top-11-persoon.

Mark heeft meerdere andere AI's onafhankelijk dezelfde persoon-sweep laten uitvoeren en de volledige antwoorden in een aparte chat laten samenvoegen tot een gecombineerde master-atlas/union. Daarnaast voert INDIA/ChatGPT zelf een eigen web-/bron-gebaseerde sweep uit, vóór inzage in Marks externe union waar praktisch mogelijk.

## Doel
Vergelijk drie onafhankelijke detectorfamilies:
1. **CCI** — bestaande Top-11-atlas.
2. **INDIA eigen sweep** — eigen onderzoek door de ChatGPT-regisseur, met eigen querystrategie en directe bronlezing; CCI-lijst niet als zoekchecklist gebruiken.
3. **EXTERNAL AI UNION** — samengevoegde bevindingen van meerdere andere AI's die zonder CCI-lijst zijn gestart.

Doel is niet meerderheid stemmen. Doel is maximale recall: iedere detector-only fysieke plek wordt vervolgens rechtstreeks bronmatig geverifieerd.

## Onafhankelijkheidsgrens INDIA
INDIA kent door projectregie al delen van CCI/legacy; een volledig cryptografisch blinde sweep is dus onmogelijk. Daarom mag INDIA zijn sweep NOOIT als volledig blind labelen. Wel geldt:
- geen CCI-lijst als zoektermen/checklist tijdens discovery;
- query's afleiden uit primaire/officiale chronologie, biografie, hosts, reizen en events;
- bevindingen vóór inzage in de externe AI-union freezen wanneer Mark die union nog niet heeft aangeleverd;
- daarna pas driehoeksvergelijking.

## Input
1. CCI-atlas:
   - `PILOT_RESULT.md`
   - `SATURATION_RESULT.md`
   - `PHASE2_RESULT.md`
   - `PHASE2_SYNTHESIS.md`
2. INDIA-eigen frozen sweep(s): onder deze benchmarktaak.
3. Externe AI master-atlas/union: door Mark/INDIA aan te leveren.

## Vergelijkingsregels
- Match op fysieke identiteit, niet alleen naam.
- Verschillende spellingen/plaatsnamen voorzichtig normaliseren.
- Niet samenvoegen bij twijfel; markeer `POSSIBLE_IDENTITY_MATCH`.
- Iedere detector-only plek classificeren als:
  - `VERIFIED_MISS_OTHER_DETECTORS`
  - `UNVERIFIED_CANDIDATE`
  - `SAME_SITE_DIFFERENT_NAME`
  - `OUT_OF_SCOPE_OR_TRANSIT`
  - `FALSE_OR_UNSUPPORTED_CLAIM`
- Host/gastheer/huis/landgoed-misses apart tellen.
- Sterke detector-only plek pas als echte miss tellen nadat de bronclaim rechtstreeks is gecontroleerd.
- Geen A/B/C namens Mark.

## Eerste benchmarkpersoon
Start met **Anandamayi Ma** omdat daarvoor al een externe multi-AI-union onderweg is en haar lange, goed gedocumenteerde reisleven een zware stresstest is voor recall.

INDIA moet vóór inzage in die externe union een eigen discovery-pass freezen voor zover dat in de actuele sessie nog mogelijk is. Omdat INDIA al CCI-data kent, wordt dit gelabeld als `INDEPENDENT_METHOD_PASS`, niet `BLIND_PASS`.

## Beslisregel voor ALLE Top-11
Als de driehoeksbenchmark op Anandamayi Ma één of meer betekenisvolle, bronmatig bevestigde fysieke locaties vindt die CCI miste, of als INDIA/externe union substantieel meer concrete touchpoints oplevert dan CCI, geldt CCI's `PERSON_SWEEP_SATURATED: JA` niet als voldoende recall-bewijs.

Dan wordt deze meervoudige-detectorcontrole voor ALLE 11 Top-11-personen uitgevoerd. Eerst mag worden getest of CCI+INDIA samen dezelfde union-recall kunnen halen; als externe AI's daarna nog unieke geverifieerde plekken leveren, blijven externe AI's als structurele derde detectorlaag nodig.

## Kwaliteitsvraag die expliciet beantwoord moet worden
Na Anandamayi Ma rapporteer:
- Wat vond CCI?
- Wat vond INDIA extra?
- Wat vond externe union extra?
- Welke extra's zijn na broncontrole echt?
- Kan een verbeterde gezamenlijke CCI+INDIA-methode alle geverifieerde externe vondsten reproduceren?
- Zo JA: externe AI's alleen steekproefsgewijs als audit.
- Zo NEE: externe multi-AI sweep verplicht voor de overige Top-11.

## Output
- `INDIA_PRE_EXTERNAL_SWEEP_ANANDAMAYI.md` — frozen eigen pass vóór externe-union-inzage.
- `EXTERNAL_UNION_INPUT.md` zodra aangeleverd.
- `BENCHMARK_RESULT.md` met CCI vs INDIA vs externe union, per fysieke plek.
- `STATUS.md` bijwerken.
- Indien structurele miss: protocolcorrectie voorstellen/vastleggen, geen stille canonwijziging.
