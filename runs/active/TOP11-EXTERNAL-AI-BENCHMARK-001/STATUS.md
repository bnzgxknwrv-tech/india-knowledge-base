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

## Update — CCI_TASK 085 afgerond: definitieve pre-external Yogananda-freeze (CCI, 2026-08-16)

```
freeze_commit: cd0ff2b159900015fcdc3d69617850efc32bc550
freeze_file: runs/active/TOP11-INDIA-PERSON-CENTRIC-MEGASWEEP-001/YOGANANDA_V2_PRE_EXTERNAL_FINAL_FREEZE.md
YOGANANDA_V2_PRE_EXTERNAL_SATURATED: NEE
```

Pre-external completion-pass op de hiaten uit `YOGANANDA_V2_FREEZE.md`: alle 82 India-plaatsen uit
de AOAY-atlas herlezen met volledige occurrence-context (niet alleen de dichtste hoofdstukken).
Resultaat:
- **Tweede fout in de AOAY-locatie-atlas gevonden en gecorrigeerd**: "Dwarka" (5 occurrences) bleek
  "Dwarka Prasad" — een persoonsnaam (huisbaaszoon in Bareilly), geen vermelding van de
  bedevaartsstad Dwarka. Naamcollision, niet een plaats. Gecorrigeerd in `PLACE_ATLAS.jsonl`.
- **Hyderabad/Ellora/Ajanta definitief opgelost**: `YOGANANDA_PERSONALLY_PRESENT: NEE`, tekstueel
  onderbouwd (regionale geschiedenisdigressie zonder eerste-persoonstaal, in scherp contrast met de
  omringende Mysore/Bangalore-passages die wél "I"/"we" gebruiken).
- **Drie nieuwe bevestigde persoonlijke bezoeken**: Delhi (zwager Satish, hfst. 22), Simla
  (Kashmir-reis, hfst. 21), Purulia (hfst. 46).
- **Vier plaatsen gecorrigeerd van "mogelijk Yogananda" naar "eigenlijk Lahiri Mahasaya's eigen
  levensverhaal"**: Danapur, Ranikhet, Ghurni, Nadia (blijven geldig als Lahiri Mahasaya-punten,
  niet als Yogananda-eigen-aanwezigheid).
- **Belangrijke nuance**: Yogoda Math bij Dakshineswar (Yogananda's eigen stichting, gewijd 1939)
  is apart gehouden van zijn persoonlijke aanwezigheid — hij keerde na 1935-36 niet meer fysiek
  naar India terug, dus stichter zijn ≠ fysiek aanwezig bij de latere wijding.
- **Wright's volledige dagboek bevestigd structureel nooit gepubliceerd** (geen falende zoekactie).
  EAST-WEST-tijdschriftarchief gevonden maar ongeoCR'd, `BRON_GEBLOKKEERD/DEELS`.

Alle vier METHOD_V2-gates beoordeeld; corpus-coverage en discovery blijven `DEELS` met expliciet
benoemde, niet-verzwegen hiaten. `NEE` bewust gekozen boven een valse `JA`-claim.

## Update — CCI_TASK 086 afgerond: externe Yogananda-union gereconcilieerd (CCI, 2026-08-18)

```
task_id: TOP11-EXTERNAL-AI-BENCHMARK-001
state: YOGANANDA_EXTERNAL_RECONCILIATION_COMPLETE__VERDICT_JA__WACHT_OP_INDIA_QA
external_input: PR #24, head e8c7ef6899feaa2a8fdfd1d82d98986f85d8281d, atlas blob 089b652e
reconciliation_file: runs/active/TOP11-EXTERNAL-AI-BENCHMARK-001/YOGANANDA_EXTERNAL_RECONCILIATION_CCI_086.md
EXTERNAL_MULTI_AI_MANDATORY_FOR_REMAINING_TOP11: JA
```

De 114-record externe union (Grok/Gemini/DeepSeek/Copilot/AI-5-synthese) is gereconcilieerd tegen
de bevroren interne pre-external freeze (`cd0ff2b1`). Acht betekenisvolle `EXTERNAL_ONLY_CLAIM`/
`EXTERNAL_MORE_GRANULAR`-kandidaten zijn rechtstreeks tegen de lokale AOAY-brontekst geverifieerd —
**allemaal `VERIFIED_TRUE`** (Pranabananda's residentie Benares, Sri Yukteswars Rana Mahal-huis,
Bhaduri Mahasaya's woning, Bose Institute, Giri Bala/Biur, Keshabananda-ashram Brindaban, Kumbh
Mela 1936-persoonlijke-aanwezigheid, Taj Mahal Hotel Bombay). Vier zelf-gerapporteerde externe
identiteitsconflicten opgelost (Anandamayi Ma-ontmoeting is Bhowanipur/Ranchi niet Varanasi;
Gandhi-ontmoeting is Wardha niet Sabarmati; Ramana-ontmoeting is Tiruvannamalai niet "Bangalore";
Ellora/Ajanta/Hyderabad zijn geen bewezen bezoek).

**CCI vond bovendien zelf iets dat alle vijf externe AI's misten**: de externe atlas liet de kamer
van het Sri Yukteswar-"resurrection"-visioen expliciet `ONBEKEND`. Rechtstreekse lezing van
hoofdstuk 43 noemt tweemaal de **Regent Hotel, Bombay** (derde verdieping) — een derde, door geen
enkele externe AI genoemde naam, die noch met "Taj Mahal Hotel" (Grok) noch met "Royal Hotel"
(AI-5, voor Wright) overeenkomt.

**Root cause van de echte misses**: CCI's eigen token-/gazetteerdetector (uit
`AOAY-FULL-LOCATION-ATLAS-001`) is sterk voor plaatsnamen met een eigen toponiem, maar structureel
zwakker voor privéadressen die de tekst alleen via de bewonersnaam aanduidt ("huis van [naam]") —
precies het gat dat de externe host-netwerkanalyse dichtte.

**Verdict**: `EXTERNAL_MULTI_AI_MANDATORY_FOR_REMAINING_TOP11: JA`, met de aanvullende bevinding dat
CCI's eigen directe bronverificatie evenmin gemist mag worden (Regent Hotel-vondst). De juiste
architectuur blijft de volledige METHOD_V2-keten: corpus -> CCI/INDIA-pass -> externe union ->
directe verificatie -> reconciliatie, niet "CCI OF externe AI".

## Update — Werkpakket D verdiepende parallelle verificatie afgerond (CCI, 2026-08-18)

```
werkpakket_d_bestand: runs/active/TOP11-EXTERNAL-AI-BENCHMARK-001/WERKPAKKET_D_DEEPENING_CCI_086.md
uitgevoerd_via: 6 parallelle subagent-workers, elk een eigen regionale batch of adversarial rol
```

Op Marks expliciete verzoek is de in CCI_086 nog ontbrekende parallellisatie alsnog uitgevoerd: zes
onafhankelijke workers hebben vrijwel de volledige 114-record externe atlas rechtstreeks tegen de
lokale AOAY-brontekst geverifieerd (i.p.v. de eerste pas se 8 steekproefrecords). Resultaat: ~45
VERIFIED_TRUE, ~10 VERIFIED_FALSE, ~11 PARTIALLY_TRUE, ~9 UNRESOLVED/OUT_OF_SCOPE. Geen nieuwe
door-alle-vijf-AI's-gemiste locatie zoals het Regent Hotel-precedent; wel diverse materiële
precisiecorrecties in beide richtingen (o.a. Rai Ghat Lane-adres bevestigd sterker dan het externe
atlas zelf durfde stellen; Yogoda Math Dakshineswar en de Jagannath-tempel-claim juist te positief
gelabeld door de externe atlas; oom Sarada-bezoek juist onderschat). Volledige lijst in het
werkpakket-D-bestand. **Wijzigt de CCI_086-kernconclusie niet** (`EXTERNAL_MULTI_AI_MANDATORY_FOR_
REMAINING_TOP11: JA` blijft staan), bevestigt wel dat bronverificatie in beide richtingen nodig
blijft — niet alleen om externe missers te vangen maar ook om externe overconfidence/hallucinaties
(record #42, Jagannath-tempel) te corrigeren.

## next_allowed_step
STOP hier conform CCI_TASK 086 stopvoorwaarde. Wacht op INDIA-QA-audit van dit verdict (nu inclusief
Werkpakket D). Geen nieuwe Top-11-persoon starten via dit taakspoor — CCI_TASK 087 (Babaji/Lahiri
Mahasaya/Sri Yukteswar) loopt apart en onveranderd. **Arunachala-regiosweep-hold blijft van kracht**
totdat INDIA deze 086-audit heeft afgerond. Geen A/B/C, geen PDF, geen route.
