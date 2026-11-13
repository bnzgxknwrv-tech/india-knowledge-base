# LAHIRI_MAHASAYA_INDIAROOD_DELTA

```
task_id: TOP11-CORE-KRIYA-INDIAROOD-DELTA-RECONCILIATION-001
cci_task: CCI_TASK 092
uitgevoerd_door: CCI
uitgevoerd_op: 2026-08-19
indiarood_input: agent/indiarood-core-kriya-sweep, commit fc8418b8785cdd22edd389f0a461586ce239ff17,
  runs/active/TOP11-INDIAROOD-BLIND-SWEEP-001/LAHIRI_MAHASAYA_INDIAROOD_FREEZE.md (40 records + 6
  negatieve associaties) — blob-sha 01778b6f43198db8080c1460402b12a478842314, geverifieerd vóór
  opening (exacte match).
cci_088_input: runs/active/TOP11-CORE-KRIYA-RECONCILIATION-001/LAHIRI_MAHASAYA_RECONCILIATION.md
  (19 interne + 60 externe ChatGPT-records)
```

## 0. Belangrijkste structurele bevinding: een tweede, andere kernbron

CCI_TASK 088's externe ChatGPT-freeze steunde voor het overgrote deel op **PP** (Ashoke Kumar
Chatterjee, *Purana Purusha*), die `BRON_GEBLOKKEERD` bleef (dokumen.pub "under maintenance").
IndiaROOD gebruikt een **andere, eveneens niet eerder in dit project geraadpleegde bron**: Swami
Bidyananda Giri's *Biografia de Sri Lahiri Mahasaya* (Portugese webtranscriptie van een
familiebiografie door kleinzonen Anandamohan en Abhoycharan Lahiri), plus RYKYM's *Life in
Illustrations*-blogpost. Dit zijn dus **twee onafhankelijke secundaire familiebiografie-tradities**
die elkaar op meerdere punten kruisen — een sterke test voor consistentie.

**Toegankelijkheid gecontroleerd**: Bidyananda-bron (pdfcoffee.com) geeft `HTTP 403` — technische
toegangscontrole, **bewust niet omzeild**, blijft `BRON_GEBLOKKEERD` voor directe herlezing.
RYKYM's blogpost (`rykym.org/blog/lahiri-mahasaya-life-illustrations`) is wél volledig open (HTTP
200) en is deze taak **volledig gedownload en gebruikt voor Tier-1-verificatie**.

## 1. Directe bronverificatie — resultaten

| claim | route | resultaat |
|---|---|---|
| Buxar- en Gorakhpur-werkposten (LM-012, LM-013) + november-1868-Ranikhet-transfer | rechtstreeks gefetcht: rykym.org blogpost | **VOLLEDIG BEVESTIGD, woordelijk**: "Initially stationed in Ghazipur..., transferred to several places, including Mirzapur, Buxar, and Gorakhpur. In November 1868, he received a transfer order to Ranikhet." Dit **triangule­ert** het 1861-vs-1868-conflict dat zowel 088 (via PP) als IndiaROOD (LM-016) al signaleerden: nu bevestigd via een DERDE, onafhankelijk toegankelijke bron — AOAY blijft bij 1861 (Yogananda's eigen narratief), maar twee onafhankelijke familiebiografie-lijnen (PP én Bidyananda/RYKYM) wijzen op 1868. Nog steeds niet definitief opgelost (AOAY is de enige eerste-persoonsbron), maar het gewicht verschuift. |
| Trailanga Swami-ontmoeting bij Panchganga Ghat Ashram (LM-025) | idem | **VOLLEDIG BEVESTIGD, woordelijk**: "When Yogiraj arrived at the Panchganga Ghat Ashram, Tailang Swami... rose excitedly and embraced him." **Dit is een volledig nieuwe locatie die noch mijn interne 088-freeze, noch de externe PP-freeze had.** |
| Rana Mahal Ghat, vallende-baksteen-episode met Krishnaram (LM-026) | idem | **VOLLEDIG BEVESTIGD, woordelijk**: "Yogiraj often took morning baths at Rana Mahal Ghat with his devotee, Krishnaram... a brick fell from a roof and struck Yogiraj's foot." **Eveneens volledig nieuw voor beide eerdere detectoren.** |
| Postmortale verschijningsclaims (LM-035 t/m LM-038: Keshabananda's hermitage Hardwar, Keshabananda's kamer Benares, Panchanon Bhattacharya's huis Calcutta, Pranabananda's onbekende stad) | rechtstreeks gefetcht en volledig gelezen: `en.wikisource.org/wiki/Autobiography_of_a_Yogi/Chapter_36` | **VOLLEDIG BEVESTIGD, woordelijk**, inclusief het detail dat Pranabananda's eigen stad niet genoemd wordt in AOAY zelf (IndiaROOD's eigen nauwkeurige toelichting: "Ranchi is slechts de latere plek waar Pranabananda dit vertelde... **niet** de gebeurtenislocatie" — dit klopt exact met de brontekst: "at the time he visited my Ranchi school"). **Dit zijn AOAY-EIGEN passages die in mijn oorspronkelijke interne 087/088-freeze volledig ontbraken** — een echte lossless-fout in mijn eigen pas, nu via IndiaROOD gecorrigeerd. Analoog aan de Kebalananda-camp-correctie bij Babaji. |
| Ramnagar-paleis/Kashi Naresh-tutorschap (LM-028) | vergelijking met 088's PP-record 21 (Pravunarayan Singh) | **DRIEWEG-CONVERGENTIE**: IndiaROOD noemt onafhankelijk dezelfde koning (Kashi Naresh Ishwari Narayan Singh) en een naamsvariant van dezelfde prins (Prabhu Narayan Singh ≈ Pravunarayan Singh). Twee onafhankelijke secundaire bronnen (PP en Bidyananda) bevestigen elkaar op een claim die CCI zelf niet kon verifiëren (PP `BRON_GEBLOKKEERD`). Status verandert van `BRON_GEBLOKKEERD/niet overgenomen` naar `PLAUSIBLE` (tweevoudig secundair bevestigd, nog geen eerste-persoonsbron). |
| Huisadres D/31/58, Madanpura (LM-023) | vergelijking met 088's PP-record 13 | **CONVERGENTIE VIA DERDE, ONAFHANKELIJKE ROUTE**: IndiaROOD citeert hetzelfde adres via een moderne webbron (yappe.in), niet via PP. Twee onafhankelijke moderne routes wijzen op hetzelfde adres — verhoogt vertrouwen zonder PP zelf gelezen te hebben. |

## 2. Nieuw sub-conflict gevonden

**Bishnupur, mei 1886 — wiens huwelijk?** 088's externe PP-record zegt dat de reis van mei 1886
was voor "dochter Harimohini's huwelijk" (Kadakuli). IndiaROOD's LM-029 zegt dat de Bishnupur-reis
van 1886 was voor "het huwelijk van zijn jongste zoon Dukari". Beide bronnen (PP resp. Bidyananda)
zijn het eens over plaats en jaar, maar noemen een ANDER familielid als bruid/bruidegom. Geen van
beide bronnen is deze taak zelf leesbaar (PP `BRON_GEBLOKKEERD`; Bidyananda HTTP 403) — dit blijft
een **onopgelost sub-conflict tussen twee secundaire familiebiografieën**, niet gekozen, expliciet
vastgelegd.

## 3. Cross-validatie van een bestaande 088-correctie

**Allahabad Kumbh Mela-aanwezigheid**: CCI_TASK 088 corrigeerde zelf al de externe ChatGPT-freeze's
negatieve bevinding hierover (die freeze zei "geen bewijs", terwijl AOAY hfst. 33 het expliciet
beschrijft). IndiaROOD's LM-033 (Kumbha Mela-terrein, Allahabad/Prayagraj, `JA`) bevestigt
**onafhankelijk** dat Lahiri hier wél was. Drieweg-consensus (intern-088 correctie + IndiaROOD)
tegen de eerste externe freeze se gemiste negatieve bevinding.

## 4. IndiaROOD's eigen correcte negatieve controle

IndiaROOD's `NEG-LM-06` wijst expliciet af dat Dashashwamedh Ghat een Lahiri-eigen-aanwezigheidsplek
is voor de Babaji-belofte-episode: "het verhaal... wordt door Yogananda verteld als ervaring van Ram
Gopal; de tekst bewijst geen fysieke aanwezigheid van Lahiri." Dit is exact consistent met de
Babaji-reconciliatie (waar Dashashwamedh Ghat wél een Babaji/Ram-Gopal-locatie is, maar niet
automatisch een Lahiri-eigen-bezoeklocatie). Geen correctie nodig, methodologisch bevestigd.

## 5. Wat IndiaROOD miste (088-only)

- **Gorakhpur-materialisatie aan Abinash Babu** (interne 088-record 18, AOAY hfst. 1): IndiaROOD's
  eigen Gorakhpur-record (LM-013) betreft alleen de PWD-werkpost, niet deze specifieke
  materialisatiescène. Blijft `088_ONLY` — een AOAY-hfst.-1-passage die ver van de door IndiaROOD
  gebruikte hfst. 32-36-focus ligt, net zoals bij de eerste externe freeze in 088.
- De 24 overige AOAY-gedekte externe-088-records die IndiaROOD niet expliciet als aparte rijen
  heeft (samengevat in plaats van uitgesplitst, zie §6) — geen feitelijke tegenspraak, alleen
  andere granulariteit.

## 6. Matrix — samenvatting (volledige rijen in INDIAROOD_DELTA_MATRIX.jsonl)

| categorie | aantal | voorbeelden |
|---|---:|---|
| Drieweg/tweeweg `MATCH_EXISTING` | 14 | Ghurni-geboorte, Danapur, Naini Tal, Drongiri-grot-cluster, Kumbh Mela, Manikarnika-crematie |
| `INDIAROOD_MORE_GRANULAR` | 3 | Buxar/Gorakhpur apart (i.p.v. samengevoegd), Ghurni-tempel-sub­splitsing |
| `INDIAROOD_ONLY_CLAIM` — **Tier-1 bevestigd** | 4 | Panchganga Ghat/Trailanga Swami; Rana Mahal Ghat-baksteen; 4 postmortale verschijningen (AOAY-gap-fill) |
| `INDIAROOD_ONLY_CLAIM` — convergent met 088-extern, versterkt | 2 | Ramnagar-paleis/Kashi Naresh; D/31/58-adres |
| `CONFLICT` — onopgelost | 2 | 1861-vs-1868-Ranikhet (getrianguleerd, nog niet opgelost); Bishnupur-1886-huwelijk (Dukari vs. Harimohini) |
| `088_ONLY_MISS` | 2 | Gorakhpur-materialisatie Abinash Babu; diverse PP-only-sublocaties (Panagarh, Burdwan-station e.a.) |
| Negatieve controles, bevestigd consistent | 2 | Dashashwamedh Ghat (niet-Lahiri); Satyalok/Arya Mission (geen Lahiri-bezoek) |

## 7. Eindbeoordeling

- **Bestaande 088-records/claims**: 19 intern + 60 extern = 79 (met overlap).
- **IndiaROOD-records**: 40 positief + 6 negatief = 46.
- **Matches**: 14 direct/granulair.
- **IndiaROOD-only**: 6 (4 Tier-1 bevestigd, 2 convergent-versterkt).
- **088-only**: minimaal 2 kernrecords plus tientallen PP-only-sublocaties die IndiaROOD's andere
  bronroute niet dekt.
- **More-granular**: 3, richting IndiaROOD.
- **Conflicten**: 2, beide expliciet onopgelost gelaten (getrianguleerd Ranikhet-jaar; Bishnupur-
  huwelijk).
- **Rechtstreeks bevestigde correcties**: 4 nieuwe Tier-1-bevestigde locaties/gebeurtenissen
  (waarvan 4 een echte AOAY-lossless-gap in de oorspronkelijke interne freeze dichten).
- **Afgewezen claims/hallucinaties**: geen gevonden bij IndiaROOD deze taak.
- **Resterende bronblokkades**: PP (dokumen.pub) en Bidyananda (pdfcoffee.com, HTTP 403) blijven
  beide ontoegankelijk — twee onafhankelijke, elkaar deels bevestigende bronnen, geen van beide
  zelf gelezen.
- **Actuele METHOD_V2-gates**:
  - `CORPUS_COVERAGE_GATE`: **DEELS** (ongewijzigd qua PP/Bidyananda-toegang, maar RYKYM voegt een
    derde, wél toegankelijke bronlaag toe die vier nieuwe AOAY-eigen/familielijn-locaties Tier-1
    bevestigde).
  - `HOSTGRAPH_GATE`: **DEELS** (Krishnaram, Trailanga Swami's kring, Keshabananda/Panchanon/
    Pranabananda-netwerk nu Tier-1 bevestigd).
  - `DISCOVERY_GATE`: **DEELS → verbeterd** (een derde onafhankelijke bronfamilie geopend).
  - `RECONCILIATION_GATE`: **PROVISIONEEL → JA** voor de drieweg-vergelijking zelf.
    `EXTERNAL_MODEL_DIVERSITY_GATE`: **NEE → JA** (zelfde onderbouwing als bij Babaji).
- **Saturationstatus**: **`LAHIRI_MAHASAYA_SATURATED: NEE`** blijft eerlijk. Twee kernbronnen (PP,
  Bidyananda) blijven beide ontoegankelijk, twee conflicten blijven onopgelost, en tientallen
  PP-only-sublocaties (Panagarh, Burdwan-station, Nepalese-prins-onderwijs e.a.) zijn nog door geen
  enkele detector bronmatig bevestigd.

---
Geschreven door: CCI. Checkpoint 2/3 van CCI_TASK 092.
