# STATUS — TOP11-EXTERNAL-AI-BENCHMARK-001

```
task_id: TOP11-EXTERNAL-AI-BENCHMARK-001
state: ANANDAMAYI_EXTERNAL_UNION_INGESTED__INDIA_SOURCE_FIRST_PASS_COMPLETE__RECONCILIATION_NEXT
last_updated: 2026-08-16
last_updated_by: INDIA
```

## Ingevoerd
- `EXTERNAL_UNION_INPUT.md`: Marks gecombineerde onafhankelijke AI-union voor Anandamayi Ma, 156 masterlocaties.
- `INDIA_SOURCE_FIRST_SWEEP_ANANDAMAYI.md`: INDIA's eigen source-first corpuspass over de officiële/lineage Anandamayi-corpus.
- `TASK.md`: benchmark is nu expliciet driehoek CCI vs INDIA-source-first vs externe multi-AI-union.

## Harde QA-uitkomst tot nu toe
1. CCI's Anandamayi-atlas (~23 punten) is **aantoonbaar niet compleet genoeg**. Het eerdere `PERSON_SWEEP_SATURATED: JA` is voor recall-doeleinden voorlopig ingetrokken/provisioneel.
2. Marks externe union (156) is **veel rijker dan CCI** en bewijst de waarde van onafhankelijke AI-detectoren.
3. De externe union is zelf óók niet compleet: een source-first scan van `anandamayi.org` Life History 1896–1982 + Sangha-biografie levert opnieuw vele expliciete fysieke sites/events die niet als afzonderlijk record in de 156-union zichtbaar zijn.
4. Conclusie: AI-search alleen — ongeacht welke AI — mag niet de primaire completeness-engine zijn. Corpus-extractie moet vóór discovery komen.

## Voorlopige architectuur
`CORPUS EXTRACTIE -> CCI/INDIA independent-method discovery -> host/gastheer graph -> EXTERNAL MULTI-AI adversarial union -> directe bronverificatie -> identity reconciliation -> SATURATION`

## Test om te bepalen of externe AI structureel nodig blijft
Anandamayi Ma is door alle partijen inmiddels 'besmet' met elkaars resultaten en is daarom geen zuivere toekomstige blindtest meer. Gebruik haar voor methodebouw en reconciliatie.

Daarna een **prospectieve control-test op Paramahansa Yogananda**:
1. CCI + INDIA voeren eerst METHOD_V2 source-first uit en freezen de volledige Yogananda-atlas.
2. Pas daarna krijgt een onafhankelijke externe multi-AI-set dezelfde blanco opdracht zonder CCI/INDIA-lijst.
3. External-only claims worden rechtstreeks geverifieerd.
4. Als externe AI nog betekenisvolle geverifieerde plekken toevoegt => externe multi-AI wordt verplichte derde detector voor alle Top-11.
5. Als CCI+INDIA METHOD_V2 de externe geverifieerde union volledig reproduceert => externe AI kan terug naar periodieke/adversarial audit in plaats van iedere persoon volledig.

## Update — CCI_TASK 084 Deel A + B afgerond (CCI, 2026-08-16)

**Deel A**: `RECONCILIATION_CCI_084.md` — CCI heeft 8/10 CCI-misses, 13 source-first-only plekken
en 5 externe-only/verdachte claims rechtstreeks tegen de officiële `anandamayi.org`-chronologie
geverifieerd, niet de aangeleverde lijsten blind overgenomen. Bevindt onafhankelijk: `BENCHMARK_
RESULT.md`'s conclusies kloppen; de externe union bevat zowel echte waarde als minstens één
aantoonbare fout (Krishnamurti-ontmoeting: juiste plek is Kitty Shiva Rao's tuin, niet de
Rajghat/Krishnamurti Foundation-campus) en één vermoedelijk compilatieartefact (Mandi-claim
gesourcet aan "AI2's eigen methodesectie", geen echte plaatsvermelding).

**Deel B**: `runs/active/TOP11-INDIA-PERSON-CENTRIC-MEGASWEEP-001/METHOD_V2.md` geformaliseerd
(negen fasen, vier verplichte saturation-gates: corpus-coverage, hostgraph, discovery,
reconciliatie). Prospectief toegepast op Yogananda vóórdat een externe Yogananda-union bestaat:
`.../YOGANANDA_V2_FREEZE.md`, corpus-eerst (volledige AOAY-brontekst + YSS-chronologie), expliciet
NIET gebaseerd op de oude Fase-2-ATL-PY-lijst als checklist. Resultaat: zes nieuwe, bronmatig
bevestigde sub-locaties binnen Mysore/Bangalore (hoofdstuk 41, Chamundi-tempel, Krishnaraja Sagar
Dam, Yuvaraja's zomerpaleis, drie lezingzalen, C.V. Raman-ontmoeting) die de oude lijst niet had.
Bijvangst: één fout in de eerdere AOAY-locatie-atlas gevonden en gecorrigeerd (Belur Math/Bengal
verward met de Belur-tempel/Karnataka in hoofdstuk 41 — nu rechtgezet in `PLACE_ATLAS.jsonl`).
`AOAY_YOGANANDA_V2_SATURATED: NEE`, expliciete hiaten vastgelegd (zie freeze-bestand).

## next_allowed_step
STOP hier conform CCI_TASK 084 punt 11. Wacht op INDIA/Mark voor de prospectieve externe-AI-
blanco-sweep op Yogananda tegen `YOGANANDA_V2_FREEZE.md` — dit is de "zuivere beslisproef" die
bepaalt of externe multi-AI structureel verplicht blijft voor alle Top-11.

Geen PDF. Geen A/B/C.
