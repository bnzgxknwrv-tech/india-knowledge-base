# Pipelineversie

**Versie:** 2.0.0  
**Status:** gereed voor ingebruikname  
**Datum:** 2026-07-12

## 2.0.0

Aanleiding:
- de eerste versie vereiste handmatig kopiëren van volledige rapporten tussen chats;
- één historisch bewijsmodel paste niet op levende tradities, lineages en getuigenissen;
- er ontbraken runisolatie, contextpinning, claim-locks en truncatiebeveiliging.

Gewijzigd gedrag:
- GitHub is het enige overdrachtskanaal;
- iedere rol schrijft een volledige eigen faseversie in een geïsoleerde runmap;
- iedere fase leest uitsluitend een gepind contextmanifest;
- Methodology v2.0 scheidt fysieke, institutionele, historische, traditie-, lineage-, levende-praktijk-, bezoekbaarheids- en getuigenislagen;
- India-overlays zijn projectspecifieke data buiten de generieke methodologie;
- claims en bronnen worden machineleesbaar vastgelegd;
- claim-lock, state machine, eventlog, source-commit-pinning, sentinels en COMPLETED-markers toegevoegd;
- GOUD geeft PASS, PARTIAL of BLOCKED;
- geen handmatige rapportoverdracht meer.

Betrokken hoofdbestanden:
- `pipeline/ENTRYPOINT.md`
- `pipeline/PIPELINE_CONTRACT.md`
- `pipeline/QUALITY_GATE.md`
- `pipeline/roles/*.md`
- `pipeline/protocols/*.md`
- `pipeline/templates/RUN_TEMPLATE.md`
- `knowledge/methodology/METHODOLOGY_V2.md`
- `knowledge/project/OVERLAYS_INDIA.md`
- `research/README.md`

Verwachte kwaliteitswinst:
- minder afkapping en contextverlies;
- reproduceerbare overdracht tussen modellen;
- correcter onderzoek van mythische figuren en levende lineages;
- sterkere brontraceerbaarheid;
- geen verborgen output in chats;
- behoud van BRONS- en ZILVER-ontwikkeling voor latere methodiekverbetering.

## 1.0.0

Eerste seriële BRONS–ZILVER–GOUD-conceptversie. Deze versie was chat-gecentreerd en is vervangen door 2.0.0.

## Wijzigingsregel

Iedere inhoudelijke protocolwijziging verhoogt de versie en vermeldt aanleiding, gewijzigd gedrag, betrokken bestanden en verwachte kwaliteitswinst. Actieve runs blijven op hun gepinde versies.

END_OF_ARTIFACT
