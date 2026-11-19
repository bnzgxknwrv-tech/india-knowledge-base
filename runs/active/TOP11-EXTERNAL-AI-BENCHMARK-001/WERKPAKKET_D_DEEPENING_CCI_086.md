# WERKPAKKET D — verdiepende parallelle verificatie (CCI_TASK 086 vervolg)

```
task_id: TOP11-EXTERNAL-AI-BENCHMARK-001
trigger: Mark — "voer de nieuwste CCI_TASK 086 volledig uit, gebruik parallelle subagents/workers
  zoals in de taak beschreven"
uitgevoerd_door: CCI, 6 parallelle subagent-workers (Werkpakket D-batches)
uitgevoerd_op: 2026-08-18
basis: runs/active/TOP11-EXTERNAL-AI-BENCHMARK-001/YOGANANDA_EXTERNAL_RECONCILIATION_CCI_086.md
  (eerste, sequentiële CCI_086-pas: 8/8 rechtstreeks geverifieerde external-only claims, allemaal
  VERIFIED_TRUE) + scratchpad/aoay/EXTERNAL_YOGANANDA_ATLAS.md (114-record externe union)
```

## Wat dit werkpakket toevoegt

De eerste CCI_086-pas verifieerde 8 van de ~114 externe records rechtstreeks en concludeerde
`EXTERNAL_MULTI_AI_MANDATORY_FOR_REMAINING_TOP11: JA`. Werkpakket D was de nog niet uitgevoerde
parallellisatie: zes onafhankelijke subagents, elk verantwoordelijk voor een eigen regionale batch
van de externe atlas, plus één aparte adversarial/kwaliteitscontrole-worker. Samen dekken ze
vrijwel de volledige 114-record atlas rechtstreeks tegen de lokale AOAY-brontekst (48 hoofdstukken).

| batch | regio | records gecontroleerd | bestand |
|---|---|---|---|
| 1 | Kolkata/Serampore/Bengal-kern | 1-39 (excl. reeds bevestigde #4/#12/#21, buiten scope #36-37) | `batch1_kolkata_serampore.md` |
| 2 | Ranchi/Puri/Bihar/UP | 21 records (#36-60-bereik) | `batch2_ranchi_puri_up.md` |
| 3 | Wardha/Mumbai/West-India | #61-70 | `batch3_wardha_mumbai.md` |
| 4 | Mysore/Bangalore/Tamil Nadu/Zuid-India | #71-93 | `batch4_mysore_south.md` |
| 5 | Kashmir-reis/Noordwest + buiten-India | #94-105, #114 | `batch5_kashmir_transit.md` |
| 6 | Adversarial bron-/identiteitscontrole (dwars door alle secties) | steekproef + zelftegenspraken | `batch6_adversarial.md` |

Alle zes bestanden staan lokaal in de scratchpad (niet in de repo — werkbestanden, geen definitieve
projectdata). Deze synthese neemt de betekenisvolle bevindingen over.

## Totaaltelling over de zes batches (excl. de 8 al in CCI_086 zelf geverifieerde records)

| verdict | aantal (indicatief, som van batches) |
|---|---|
| VERIFIED_TRUE | ~45 |
| VERIFIED_FALSE | ~10 |
| PARTIALLY_TRUE | ~11 |
| VERIFIED_TRUE_SECONDARY_ONLY (bevestigd via Wright-brief/YSS-chronologie, niet AOAY zelf) | 1 |
| UNRESOLVED / OUT_OF_SCOPE_FOR_LOCAL_CORPUS | ~9 |

Geen van de zes batches heeft een nieuwe, door alle vijf externe AI's gemiste fysieke plek
gevonden zoals het Regent Hotel-precedent uit de eerste CCI_086-pas. Het beeld van deze
verdiepingsronde is overwegend **precisiecorrectie**: op- en afwaarderingen van bewijskracht per
record, geen nieuwe missed-site-vondsten van het type dat CCI_086's kernconclusie zou veranderen.

## Belangrijkste materiële correcties op de externe atlas

1. **#27 Sri Yukteswars hermitage, Serampore — "Rai Ghat Lane" staat letterlijk in AOAY**, uit Sri
   Yukteswars eigen mond (hfst. 10) én Yogananda's eigen beschrijving (hfst. 11/12). De externe
   atlas verlaagt de fysieke-identiteitsscore naar DEELS vanwege een conflict tussen drie *moderne*
   adressen (3 Rai Ghat Lane / 57 Netaji Subhas Avenue / 3A Buro Bibi) — maar dat conflict zit in de
   hedendaagse adressering, niet in wat de primaire bron zelf zegt. AOAY zelf is hier sterker en
   eenduidiger dan de externe voorzichtigheid suggereert.
2. **#11 Yogoda Math, Dakshineswar — legacy-only, geen persoonlijke aanwezigheid mogelijk.** AOAY
   hfst. 40 dateert de wijding zelf tweemaal onafhankelijk (1938 in het bijschrift, 1939 in de
   lopende tekst) — beide ná Yogananda's laatste vertrek uit India (aug. 1936). De externe atlas'
   "WAARSCHIJNLIJK/BETWIST, DEELS" is te positief voor persoonlijke aanwezigheid; aanbevolen
   downgrade naar expliciet legacy-only, met een aparte, ongeverifieerde subclaim over mogelijke
   grondverwerving tijdens het 1935-36-verblijf.
3. **#42 Jagannath-tempel, Puri — hallucinatie-citaat.** De externe atlas citeert AOAY hfst. 12/42
   als "BEWEZEN/EXACT" (Gemini), maar het woord "Jagannath" (en varianten) komt **nul keer** voor in
   alle 48 hoofdstukken. Hoofdstukken 12/42 gaan wel over Puri/Karar Ashram (= correct record #40),
   maar noemen de Jagannath-tempel zelf niet. Aanbevolen downgrade naar GEEN BEWIJS.
4. **#16 Gandha Baba's huis, Burdwan — hard VERIFIED_FALSE**, geen giswerk nodig: AOAY hfst. 5 maakt
   met "Alakananda told me" ondubbelzinnig duidelijk dat dit Alakananda's verteld verhaal is, niet
   Yogananda's eigen ervaring.
5. **#31 Oom Sarada Prasad Ghosh — externe atlas juist te terughoudend.** AOAY hfst. 20 en 23
   bevestigen tweemaal expliciet een persoonlijk bezoek van Yogananda aan "the home of my Uncle
   Sarada" in Serampore. De externe atlas noteert dit ten onrechte als "niet bevestigd in AY"; dit is
   een zeldzaam voorbeeld van onderschatting in plaats van overschatting.
6. **#38 Giri Bala's huis, Biur — sterker fysiek beschreven dan aangenomen.** AOAY (via een letterlijk
   geciteerd Wright-dagboekfragment, hfst. 46) beschrijft het huis architectonisch ("a large,
   two-storied building of brick and plaster... dominating the surrounding adobe huts"), niet
   slechts de dorpsnaam Biur.
7. **#68 "Royal Hotel" — uitsluitend Wright-eigen-logiesbron, niet AOAY, niet Yogananda-aanwezigheid.**
   Bevestigd via volledige 48-hoofdstukken-grep: de naam komt nul keer in AOAY voor.
8. **Regent Hotel-detail bijgesteld**: bij nadere grep blijkt de naam "Regent Hotel" in hoofdstuk 43
   **éénmaal** letterlijk genoemd (niet tweemaal zoals eerder gemeld), gevolgd door twee generieke
   vervolgverwijzingen ("the Bombay hotel"). De kernvondst (een hotelnaam die geen van de vijf
   externe AI's vond) blijft onveranderd overeind; alleen het herhalingsaantal is nu preciezer.
9. **Golden Temple/Amritsar (#96), Trivandrum/Kanyakumari (#92-93), Hyderabad/Ellora/Ajanta/
   Kanchipuram (#88-91) — alle bevestigd `GEEN BEWIJS`** via volledige corpus-grep (nul treffers of
   uitsluitend beschrijvende/historische zinnen zonder eerste-persoonstaal), in lijn met wat de
   externe atlas zelf al vermoedde.
10. **Shalimar Bagh en Nishat Bagh (Kashmir) — wél degelijk met naam genoemd in AOAY zelf**
    ("at Shalimar and Nishat Bagh"), tegen de aanname in de batch-opdracht in dat dit mogelijk
    externe toevoegingen waren. Dal Lake eveneens expliciet met naam bevestigd.
11. **#23 Tagore-studeerkamer — interne conflatiefout in de externe atlas.** Het studeerkamer-detail
    hoort bij de latere Santiniketan-ontmoeting (= correct record #35), niet bij de eerste
    kennismaking in Calcutta. Vergelijkbaar met de reeds door de atlas zelf gesignaleerde
    "meerdere functies op één adres samengevoegd"-fout bij record #4.
12. **#61 Wardha-station en #63-64 Maganvadi-gastenhuis/Gandhi's schrijfkamer — sterker bevestigd**
    dan de opdracht veronderstelde, met drie aparte scènes in Gandhi's schrijfkamer, inclusief de
    allereerste ontmoeting.
13. **#66 Bombay-aankomsthaven — PARTIALLY_TRUE**: RAJPUTANA, 22 aug. 1935, "huge harbor of Bombay"
    bevestigd; geen specifieke pier/kade genoemd.
14. **#70 Bombay-lezingzalen — VERIFIED_TRUE_SECONDARY_ONLY**: AOAY hfst. 43 bevestigt zelf geplande
    lezingen ("I was scheduled for several public addresses in Bombay"), maar geen zaalnaam; de
    exacte data 8-10 juni 1936 zijn alleen via een Wright-brief bekend, niet uit AOAY zelf.
15. **#72 vs #84 Town Hall-verwarring opgelost**: AOAY hfst. 41 gebruikt "the Town Hall" zonder
    "Chetty" voor Mysore, en "the Chetty Town Hall" specifiek voor Bangalore. De externe koppeling
    van "Sir Puttanna Chetty Town Hall" aan Mysore is niet door de brontekst gedekt.
16. **#75/#77 (Third Princess's paleis, "Art of Contacting God"-lezing) en #85 Gokhale Hall Madras —
    geen enkele AOAY-basis** (nul treffers over alle 48 hoofdstukken); uitsluitend secundaire
    Wright-/krantenbronnen. #85's "BEWEZEN"-label rust op één niet-verifieerbare krantenbron van één
    AI en verdient downgrade tot krantenbron zelf gecontroleerd is.
17. **#103 Lahore — PARTIALLY_TRUE**: jeugdverblijf en vliegerverhaal bevestigd, geen adres, geen
    "amuletverhaal" gevonden. **#104 Chittagong — OUT_OF_SCOPE_FOR_LOCAL_CORPUS**: nul AOAY-treffers,
    steunt uitsluitend op de Mejda-memoire (niet gecheckt). **#114 afgezegde eerste Kashmir-reis**
    bevestigd geannuleerd — reden was Yogananda's eigen acute cholera-aanval in Serampore (hfst. 20),
    niet een regionale epidemie zoals verondersteld — correct GEEN locatiebezoek.
18. **Nieuwe tempelnaam in Vrindavan**: AOAY noemt de **Madanamohana-tempel** met naam; de externe
    atlas classificeert deze tempel ten onrechte als "onbekend".
19. **Taj Mahal-bezoek is dubbel**: jeugdbezoek hfst. 11 (~1910, met Jitendra) én een apart, opnieuw
    gefotografeerd bezoek in **hfst. 42** (1936, niet hfst. 41 zoals de atlas citeert), direct na de
    Kumbh Mela, op weg naar Keshabananda.
20. **Meerdere claims blijken volledig ongefundeerd in AOAY** (nul treffers over alle 48
    hoofdstukken): #42 Jagannath-tempel (zie boven), #49 Vishvanath-tempel, #43 vaderswoning Benares
    (AOAY spreekt dit zelfs zelf tegen — het gezin woonde toen in Bareilly), #60 Meerut.

## Adversarial-batch — systeembrede observatie

Batch 6's steekproef op zeven "unieke" AI-5-citaten bevestigde zes van de zeven als accuraat en
vond één volledige hallucinatie (#42). De atlas' eigen "hoeveel AI's noemen dit"-teller correleert
**niet betrouwbaar** met bewijskracht in beide richtingen: single-AI-records bleken soms sterker
(#7, #39, #52) en soms volledig ongefundeerd (#42) dan hun labelniveau suggereerde. Geen actieve
naam/plaats-collisiefout aangetroffen in de externe atlas zelf (in tegenstelling tot CCI's eigen
eerdere "Dwarka Prasad"- en "Belur"-fouten), maar twee hoogrisico-termen ("Kashi", "Dwarkanath")
bevestigd als terugkerende valkuilen voor toekomstige extracties.

## Gevolg voor het CCI_086-verdict

Geen van deze bevindingen wijzigt de kernconclusie van `YOGANANDA_EXTERNAL_RECONCILIATION_CCI_086.md`:
`EXTERNAL_MULTI_AI_MANDATORY_FOR_REMAINING_TOP11: JA` blijft staan (voor personen die een volledige
METHOD_V2 deep sweep krijgen — zie ook Marks scopebesluit `decisions/TOP11_SWEEP_DEPTH_BY_PERSON_
2026-08-18.md` voor Vivekananda/Hariharananda). Deze verdiepingsronde bevestigt bovendien het
CCI_086-inzicht dat noch interne, noch externe detectie alleen voldoende is: de externe atlas bevat
zowel echte precisiewinst (#27, #31, #38, Shalimar/Nishat Bagh) als aantoonbare fouten/hallucinaties
(#11, #42, #23) — rechtstreekse bronverificatie blijft in beide richtingen noodzakelijk, niet alleen
om externe missers te vangen maar ook om externe overconfidence te corrigeren.

## Onopgeloste punten (expliciet, niet verzwegen)

- #8 (Roma's huis, Girish Vidyaratna Lane): geciteerd hoofdstuk 22 bevat de scène niet; nadere
  brontraceercontrole nodig.
- #17 (Tulsi Bose), #24 (Kshattriya Conference), #26 (vroege lezingzalen), #28 (Rai Ghat-banyanboom),
  #85 (Gokhale Hall): steunen niet op AOAY, vereisen niet-AOAY bronnenonderzoek (krantenarchieven,
  Wright-brieven) buiten de scope van deze taak.
- #104 Chittagong: alleen via de Mejda-memoire (Sananda Lal Ghosh) te verifiëren, niet geprobeerd.

Geen A/B/C namens Mark. Geen PDF. Geen route/hotel. Geen permanente locatie-ID.

---
Geschreven door: CCI, op basis van 6 parallelle subagent-workers (Werkpakket D). Vervolg op
CCI_TASK 086. STOP hierna conform de bestaande CCI_086-stopvoorwaarde — wacht op INDIA-QA.
