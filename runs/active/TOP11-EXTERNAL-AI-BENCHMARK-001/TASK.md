# TASK — TOP11-EXTERNAL-AI-BENCHMARK-001

```
task_id: TOP11-EXTERNAL-AI-BENCHMARK-001
issued_by: INDIA
issued_at: 2026-08-16
mode: INDEPENDENT_EXTERNAL_AI_UNION_BENCHMARK
```

## Aanleiding
CCI heeft `TOP11-INDIA-PERSON-CENTRIC-MEGASWEEP-001` afgerond met circa 90 atlaspunten en 11/11 `PERSON_SWEEP_SATURATED: JA`. Dit is nog NIET als bewezen volledige waarheid geaccepteerd. De eigen synthese vermeldt dat de definitieve passes methodisch selectief waren en dat o.a. een brede Vivekananda-reisperiode gebundeld is. Marks doel van het 'andersommetje' is maximale recall van verifieerbare fysieke India-touchpoints per Top-11-persoon.

Mark heeft daarom meerdere andere AI's onafhankelijk dezelfde persoon-sweep laten uitvoeren en de volledige antwoorden in een aparte chat laten samenvoegen tot een gecombineerde master-atlas/union. Die externe union moet als onafhankelijke recall-benchmark tegen CCI worden gelegd.

## Doel
Bepaal per persoon of CCI locaties heeft gemist die minstens één onafhankelijke externe AI vond, en omgekeerd. Het doel is NIET te stemmen op meerderheid, maar kandidaat-misses te ontdekken en vervolgens bronmatig te verifiëren.

## Input
1. CCI-atlas:
   - `PILOT_RESULT.md`
   - `SATURATION_RESULT.md`
   - `PHASE2_RESULT.md`
   - `PHASE2_SYNTHESIS.md`
2. Externe AI master-atlas/union: nog door Mark/INDIA aan te leveren.

## Vergelijkingsregels
- Match op fysieke identiteit, niet alleen naam.
- Verschillende spellingen/plaatsnamen voorzichtig normaliseren.
- Niet samenvoegen bij twijfel; markeer `POSSIBLE_IDENTITY_MATCH`.
- Iedere externe-only plek classificeren als:
  - `EXTERNAL_ONLY_VERIFIED_MISS`
  - `EXTERNAL_ONLY_UNVERIFIED`
  - `SAME_SITE_DIFFERENT_NAME`
  - `OUT_OF_SCOPE_OR_TRANSIT`
  - `FALSE_OR_UNSUPPORTED_EXTERNAL_CLAIM`
- Iedere CCI-only plek eveneens zichtbaar houden.
- Sterke externe-only plek pas als echte CCI-miss tellen nadat de bronclaim rechtstreeks is gecontroleerd.
- Host/gastheer/huis/landgoed-misses apart tellen.
- Geen A/B/C namens Mark.

## Beslisregel voor verdere externe sweeps
Als de onafhankelijke benchmark op Anandamayi Ma of een andere reeds geteste persoon één of meer betekenisvolle, bronmatig bevestigde fysieke locaties vindt die CCI miste, geldt CCI's `PERSON_SWEEP_SATURATED: JA` niet als voldoende kwaliteitsbewijs. Dan moet dezelfde onafhankelijke externe-unioncontrole over ALLE Top-11-personen worden uitgevoerd.

Gezien Marks doel en het beperkte aantal van 11 personen mag efficiëntie niet worden gebruikt om een aantoonbare recall-miss te negeren.

## Output
- `EXTERNAL_UNION_INPUT.md` of machineleesbare equivalent zodra aangeleverd.
- `BENCHMARK_RESULT.md` met per persoon union/matches/misses/conflicten.
- `STATUS.md` bijwerken.
- Indien structurele miss: voorstel voor protocolcorrectie, maar geen stille canonwijziging.
