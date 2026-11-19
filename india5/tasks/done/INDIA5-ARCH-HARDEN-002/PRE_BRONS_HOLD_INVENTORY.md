# Inventaris + vergelijking: vastgehouden PRE-BRONS/protocolbestanden (punt 11)

Status: deze bestanden blijven ONGECOMMIT. Dit document inventariseert en vergelijkt ze met de
canonieke INDIA2-besluiten, maar committeert ze NIET als onderdeel van deze hardeningstaak.

## Inventaris (`git diff --stat` + `git status --short` op 2026-08-02)

Gewijzigd (bestaande bestanden):
```
india4/protocols/INDIA5-PROTOCOL.md | 124 ++++++++++++++++++++++++++++++++++++
india4/roles/BRONS.md               |  18 +++---
india4/templates/BATCH_OUTPUT.md    |  12 ++++
3 files changed, 146 insertions(+), 8 deletions(-)
```

Nieuw (untracked):
- `india4/roles/PRE-BRONS.md` (65 regels) — nieuw rolcontract voor de PRE-BRONS-stap.
- `india4/templates/PRE_BRONS_REGION_CONTENT_BRIEF_TEMPLATE.md` (49 regels) — verplichte
  structuur voor de regio-inhoudsbrief.
- `india4/registries/DETECTOR_LIBRARY.jsonl` (1 regel, alleen header/schema, geen echte
  detectoren) — detectorbibliotheek, leeg schema.
- `india4/registries/DETECTOR_RUN_HISTORY.jsonl` (1 regel, alleen header/schema).
- `india4/scripts/validate_detector_library.py` (89 regels).
- `india4/scripts/validate_pre_brons_brief.py` (106 regels).

Doel per bestand: BRONS.md/BATCH_OUTPUT.md/INDIA5-PROTOCOL.md-wijzigingen voegen de nieuwe
volgorde (PRE-BRONS → detectoren → kandidaten → betekenis → onderscheid → Mark-relevantie →
cluster/koepeltoets → GEO → ZILVER → GOUD) en de verplichte betekenisvelden
(WHY_THIS_ONE/WHY_NOT_THE_OTHERS/MEANING_EVIDENCE/LIVING_OR_MONUMENTAL/MARK_RELEVANCE_LINK) toe
aan BRONS's batchcontract. De nieuwe bestanden implementeren PRE-BRONS zelf, de
detectorbibliotheek en bijbehorende validators.

## Vergelijking met de canonieke INDIA2-besluiten (PR #23, comment 5159503692, "BESLUITEN OP 7 OPEN VRAGEN")

| Punt uit het besluit | Vastgehouden implementatie | Oordeel |
|---|---|---|
| Canoniek pad `india4/registries/DETECTOR_LIBRARY.jsonl` | Exact dit pad gebruikt | **AKKOORD** |
| Apart append-only `india4/registries/DETECTOR_RUN_HISTORY.jsonl`, niet genest | Exact zo gebouwd, apart bestand | **AKKOORD** |
| Detector-recordvelden (`detector_id`, `name`, `definition`, `purpose`, `trigger_conditions`, `exclusion_conditions`, `required_source_families`, `applicability_facets`, `discovered_in_run`, `status`, `parent_detector_id`, `aliases`, `created_at`, `approved_by`) | Alle velden aanwezig in de headerregel/schema-verwachting van `DETECTOR_LIBRARY.jsonl` en gecontroleerd door `validate_detector_library.py` | **AKKOORD** |
| CCI mag PROVISIONAL zelfstandig gebruiken, promotie alleen door INDIA2 | Nog niet in code afgedwongen in de india4-versie (geen script controleert PROVISIONAL->ACTIVE-promotieautoriteit); WEL nu in `india5/GOVERNANCE.md` sectie 3 canoniek vastgelegd | **DEELS** -- governance-tekst compleet, technische afdwinging in `india4/scripts/validate_detector_library.py` beperkt zich tot schema/status-geldigheid, niet tot "wie mag promoveren" (dat is sowieso geen bestandsniveau-controle, eerder een procesregel) |
| Multi-label `applicability_facets`, geen starre lijst nu | `DETECTOR_LIBRARY.jsonl`-schema-commentaar vermeldt dit veld als object, geen aparte vaste-taxonomielijst afgedwongen | **AKKOORD** |
| PRE-BRONS-output: `REGION_CONTENT_BRIEF.md`+`.json`, `PRE_BRONS_DETECTORS.jsonl`, `SOURCE_FAMILY_PLAN.jsonl`, verplichte inhoud incl. "welke dramatisch te missen A-locatie..." | `PRE_BRONS_REGION_CONTENT_BRIEF_TEMPLATE.md` bevat exact deze structuur en dat verplichte veld | **AKKOORD** |
| BRONS start pas na interne consistentie, geen tussentijdse Mark-goedkeuring | `india4/scripts/validate_pre_brons_brief.py` implementeert precies deze consistentiecontrole | **AKKOORD** |
| Verzadigingsdrempel (hybride, DISCOVERY_SATURATED/NOT_YET_SATURATED) | Beschreven in de vastgehouden `INDIA5-PROTOCOL.md`-sectie, nog geen apart script (was ook niet expliciet gevraagd als apart script in het besluit) | **AKKOORD**, geen afwijking |
| Elke kandidaat: `why_this_one`/`why_not_the_others`/`meaning_evidence`/`living_or_monumental`/`mark_relevance_link` vóór GEO | Toegevoegd aan `BATCH_OUTPUT.md` en `BRONS.md`, in die volgorde | **AKKOORD** |
| Retroactief: Varanasi krijgt een begrensde `VARANASI_DISCOVERY_COVERAGE_AUDIT` | Genoemd in de vastgehouden `INDIA5-PROTOCOL.md`-sectie "Retroactiviteit", NIET uitgevoerd (conform "verboden" in deze en de kennistoets-taak) | **AKKOORD**, correct niet uitgevoerd |

## Conclusie

Geen inhoudelijke afwijking gevonden tussen de vastgehouden PRE-BRONS/protocolbestanden en de
canonieke INDIA2-besluiten van comment 5159503692. Het enige punt dat nog niet
volledig 1-op-1 dekt is de PROVISIONAL->ACTIVE-promotieautoriteit als technische controle
(dat is inherent een procesregel, niet iets wat een enkel bestand kan afdwingen) — dit is nu
wel expliciet als governance-tekst vastgelegd in `india5/GOVERNANCE.md` sectie 3, wat WEL
onderdeel is van deze hardeningstaak.

**Aanbeveling**: de vastgehouden bestanden zijn inhoudelijk klaar en stemmen overeen met de
canonieke besluiten. Commit ervan valt buiten de scope van deze architectuurtaak (expliciet
verboden in zowel de kennistoets- als de hardeningsopdracht) en vereist een aparte, expliciete
vrijgave/opdracht van Mark of INDIA2.
