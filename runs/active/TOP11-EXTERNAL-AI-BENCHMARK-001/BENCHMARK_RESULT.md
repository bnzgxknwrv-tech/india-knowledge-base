# BENCHMARK_RESULT — ANANDAMAYI MA — CCI vs INDIA vs EXTERNAL UNION

```
task_id: TOP11-EXTERNAL-AI-BENCHMARK-001
person: Anandamayi Ma
status: PRELIMINARY_THREE_WAY_RESULT__METHOD_DECISION_READY
performed_by: INDIA
performed_on: 2026-08-16
```

## Inputs
1. CCI: `PILOT_RESULT.md` + `SATURATION_RESULT.md` — circa 23 Anandamayi-atlaspunten.
2. External union: `EXTERNAL_UNION_INPUT.md` — 156 masterlocaties uit 4 onafhankelijke AI-uitkomsten.
3. INDIA: `INDIA_SOURCE_FIRST_SWEEP_ANANDAMAYI.md` — source-first reconstructie uit de officiële/lineage Anandamayi-corpus.

## Harde conclusie 1 — CCI `PERSON_SWEEP_SATURATED: JA` was onjuist als completeness-claim
De CCI-set is niet alleen iets smaller; hij mist hele categorieën die de eigen taak verplicht stelde: hosthuizen, gastashrams, dharmashala's, paleizen, sanatoria, scholen, forten, specifieke tempels en chronologische tussenstops.

Voorbeelden van CCI-misses die zowel door de externe union als rechtstreeks door officiële/lineage-bronnen worden ondersteund:
- Pandey Dharamshala, Varanasi.
- Burdwan Kunj, Vrindavan.
- Bhowali T.B. Sanatorium.
- Bhola Giri/Giriji Ashram, Kankhal.
- Salogra Temple cave.
- Chunar Fort.
- Baghat House, Haridwar.
- Juhu sea-beach Sanyam.
- Gwalior Palace.
- Sevagram.
- Swadeshi House, Kanpur.
- Baleswar Prasad residence, Allahabad.
- Rashtrapati Bhavan.
- Prime Minister's House.
- Kitty Shiva Rao garden/house, Delhi.
- Karar Ashram, Puri.
- Sri Aurobindo Ashram, Pondicherry.
- Sri Ramanasramam, Tiruvannamalai.

Dit is voldoende om CCI's eerdere saturation-label als recall-gate ongeldig te verklaren.

## Harde conclusie 2 — externe multi-AI union heeft echte meerwaarde
De 156-union is veel rijker dan CCI en bevat reële long-tail plekken die niet vanzelf uit een ashramlijst komen. De host/gastheer-as is vooral bij AI2 sterk.

Voorbeeld van een echte externe long-tail vondst die rechtstreeks via een lineage-bron is bevestigd:
- **Kitty Shiva Rao's garden/home, Delhi** — de officiële Anandamayi-site beschrijft expliciet dat J. Krishnamurti bij Kitty verbleef en de ontmoeting met Ma in haar tuin plaatsvond.

Dus externe AI's zijn niet alleen ruis: zij leveren echte detector-only kandidaten.

## Harde conclusie 3 — externe union is zelf ook aantoonbaar niet compleet
De INDIA source-first scan van de officiële `anandamayi.org` Life History 1896–1982 en Sangha-biografie vond daarna opnieuw vele expliciete fysieke sites/events die niet als afzonderlijk record in de 156-union voorkomen.

Sterke voorbeelden:
- Doonga, Dehradun.
- Yogendra Nagar / Tarananda Swami Ashram.
- Raj Rajeswari Temple, Chittagong.
- Shankar Mutt, Chittagong.
- Sita Kund.
- Buddha Temple + Vishnu Temple at Ramkut.
- Mirtola.
- Krishna Kunj + Sri Gopal Thakur Ashram, Allahabad.
- Assi Ghat, Varanasi.
- Ekdalia Road Ashram, Calcutta.
- Sarnath.
- Dr. J. Sen's house, Delhi.
- Barechina + Jageswar.
- Kullu palace garden royal camp.
- Manav Seva Sangh Ashram, Vrindavan.
- Parmarth Niketan + Sivananda Ashram, Rishikesh.
- Saptarishi Ashram, Haridwar.
- Kuchaman Fort.
- Shanti Niketan/Nitai Basu Mallick residence, Kankhal.
- Scindia Public School, Gwalior.
- N.N. Mukherjee residence, Allahabad.
- Pilani.
- Hazaribagh.
- J.K. Temple campus, Kanpur.
- Jaipuria House, Ramghat, Haridwar.
- Ganga Vihar Dharamshala + Naini Jaipuria House, Bithoor.
- Ganga Lahari Birla Guest House, Raiwala.
- Hawa Mahal, Gondal.
- Hathwa House, Patna.
- Ratu Palace, Ranchi.
- Narendra Brahmachari Ashram, Deoghar.
- Sant Ram Mandir, Nadiad.
- Belur Math.
- Bhasa residence/ashram, Calcutta.
- S.N. Ghosh Ganga-bank bungalow, Calcutta.
- M.S. Subbulakshmi/T. Sadasivan house + specially built lawn hut in Madras.
- Simhachalam, Vijayawada, Guntur, Mahabalipuram.
- Sir C.P. Ramaswamy Aiyer's house in Madras.
- Sagar, Barman Ghat, Ramghat and a river-Vyas dharmashala.

Daarmee is ook 'external union = waarheid' uitgesloten.

## Harde conclusie 4 — externe AI-claims moeten geverifieerd, niet gestemd
De union bevat ook identity-/bewijsproblemen. Voorbeelden:
- `Rajghat/Krishnamurti Foundation-campus` is waarschijnlijk NIET de plek van de Ma–Krishnamurti ontmoeting; de lineage-bron plaatst die expliciet in de tuin van Kitty Shiva Rao's huis in Delhi.
- `Vashishta Guha` is in de officiële Life History wel verbonden via Swami Purushottam Tirtha die Ma uitnodigt, maar die ene bronpassage bewijst niet op zichzelf dat Ma de grot daadwerkelijk bezocht.
- Badrinath-ashramclaim en postume instellingen vereisen apart bewijs van persoonlijke aanwezigheid.

Dus detector-consensus is geen verificatie.

## Root cause
De eerste persoon-methode begon nog steeds te veel met zoekmachine-discovery (`naam + ashram/birthplace/...`) en gebruikte chronologie/hostketens als aanvullende laag. Voor een zeer reizende figuur als Anandamayi Ma is dat de verkeerde volgorde.

## METHOD_V2 — vereiste architectuur

### Fase 0 — corpus inventory
Per persoon eerst een expliciete broncorpuslijst: officiële chronologie, autobiografie/biografie, dagboeken, memoirs, lineage-publicaties, reisverslagen, foto-captions, brieven en relevante archiefindexen.

### Fase 1 — lossless corpus extraction
Machine-assisted + handmatige chapter/year pass. Iedere plaatsvermelding als occurrence opslaan vóór relevantiefilter. Huizen, kamers, hostnamen, paleizen, sanatoria, stations, scholen, forten, rivierkampen, dharmashala's en transit worden niet genegeerd.

### Fase 2 — event/place normalization
Per occurrence apart:
- persoon aanwezig?
- gebeurtenis bewezen?
- fysieke identiteit exact/deels/plaatsniveau?
- exact subadres?
- host/gastheer?
- huidige instelling versus historische site?

### Fase 3 — host/network graph
Iedere genoemde gastheer, discipel, vorst, arts, geleerde, ashramhoofd en organisator terugzoeken naar huis/landgoed/instelling en bezoekcontext.

### Fase 4 — discovery search
Pas NU brede websearch/alternatieve spellings/regionale zoektermen voor plekken die de corpus niet expliciet indexeert.

### Fase 5 — onafhankelijke INDIA-pass
Andere query-/bronroute dan CCI; geen CCI-lijst als checklist tijdens discovery.

### Fase 6 — externe multi-AI adversarial union
Blanco prompt, geen bestaande kandidatenlijst. Detector-only kandidaten worden ingevoegd maar nog niet als feit.

### Fase 7 — directe verification + reconciliation
Alle detector-only of conflictpunten rechtstreeks naar bron. Duplicaten/sublocaties oplossen. Pas daarna saturation.

### Nieuwe saturationregel
`PERSON_SWEEP_SATURATED: JA` mag nooit meer alleen betekenen 'zes zoekcategorieën zijn geprobeerd'. Vereist:
1. benoemde corpusfamilies aantoonbaar doorlopen of expliciet `UNAVAILABLE`;
2. corpus-occurrence coverage-matrix;
3. host graph pass;
4. discovery pass;
5. detector reconciliation;
6. expliciete lijst van onopgeloste bronfamilies/tijdvakken.

## Zijn andere AI's structureel nodig?
Nog niet definitief beslist.

**Wat Anandamayi wél bewijst:**
- CCI alleen: onvoldoende.
- externe AI's: waardevolle echte aanvullingen.
- externe AI's alleen: eveneens onvoldoende.
- source-first corpus-extractie: noodzakelijk.

**Zuivere beslisproef:** gebruik METHOD_V2 prospectief op Yogananda. CCI + INDIA freezen eerst hun source-first union. Pas daarna laat Mark meerdere externe AI's blanco zoeken. Als externe AI daarna nog betekenisvolle geverifieerde plekken toevoegt, blijft multi-AI een verplichte detector voor alle 11. Als CCI+INDIA METHOD_V2 alles reproduceert, kan externe AI terug naar steekproef/adversarial audit.

## Besluit
`PERSON_METHOD_V1` is onvoldoende voor max-recall en moet voor toekomstige Top-11-completeness worden vervangen door `PERSON_METHOD_V2` zoals hierboven. De bestaande CCI-atlas blijft bruikbare input, maar niet de eindwaarheid.

Geen A/B/C. Geen PDF.
