# LAHIRI_MAHASAYA_RECONCILIATION

```
task_id: TOP11-CORE-KRIYA-RECONCILIATION-001
cci_task: CCI_TASK 088
uitgevoerd_door: CCI
uitgevoerd_op: 2026-08-19
interne_input: runs/active/TOP11-INDIA-PERSON-CENTRIC-MEGASWEEP-001/LAHIRI_MAHASAYA_V2_PRE_EXTERNAL_FREEZE.md
  (freeze commit 642e464ac96ca011f75df93c0f3ce71653948d6f, 19 records)
externe_input: agent/chatgpt-top11-parallel-sweep:
  runs/active/TOP11-PARALLEL-CHATGPT-SWEEP-001/LAHIRI_MAHASAYA_PRE_COMPARE_FREEZE.md
  (freeze commit 71bb5b6406fec1e7b59511e7957d247c3bdabc50, 60 records)
INDIA_ROOD_PENDING: JA — geen duurzame IndiaROOD-freeze voor Lahiri Mahasaya beschikbaar op dit
  checkpointmoment. RECONCILIATION_GATE: PROVISIONEEL, EXTERNAL_MODEL_DIVERSITY_GATE: NEE.
```

## Belangrijkste bevinding vooraf: nieuwe primaire bron

De externe freeze gebruikt een bron die ik niet had: **PP — Ashoke Kumar Chatterjee, *Purana Purusha
Yogiraj Sri Shama Churn Lahiree: A Complete Biography*** (familie-/lineagebiografie, 26 dagboeken/
brieven van nakomelingen). Dit is potentieel de rijkste beschikbare bron over Lahiri Mahasaya's
leven en verklaart waarom de externe set (60) mijn interne set (19) ver overtreft in aantal.

**Directe bronverificatie ondernomen, resultaat: BRON_GEBLOKKEERD.** Ik heb geprobeerd de PP-URL
(dokumen.pub) rechtstreeks op te vragen voor de vier meest consequente claims (exacte
overlijdenstijd, huisadres D/31/58, Ramnagar-paleis/Pravunarayan Singh-tutorschap, en het
1861-vs-1868-Ranikhet-conflict). De site meldt "under maintenance" — geen tekst beschikbaar. Ter
gedeeltelijke compensatie is het overlijden **onafhankelijk gecontroleerd bij een tweede bron**
(yssofindia.org/about/lahiri-mahasaya: "Lahiri Mahasaya entered mahasamadhi in Banaras, September
26, 1895") — dit bevestigt de datum (niet de kloktijd 17:25, niet het adres, niet de Ramnagar-claim).

**Consequentie voor deze reconciliatie**: alle PP-only claims (het overgrote deel van de externe
36 records zonder AOAY-locator) worden hieronder `EXTERNAL_ONLY_UNVERIFIED` met `BRON_GEBLOKKEERD`
i.p.v. `EXTERNAL_ONLY_VERIFIED_MISS`. Dit is geen afwijzing van de claims — PP oogt als een serieuze
familiebiografie met specifieke regelankers — maar conform TASK.md §6 ("BRON_GEBLOKKEERD of
UNRESOLVED is beter dan schijnzekerheid") mag ik ze niet als geverifieerd overnemen zonder de bron
zelf gelezen te hebben.

## Werkpakket A+B — matching tegen de 24 AOAY-gedekte externe records

Van de 60 externe records citeren er 24 (mede) AOY (mijn enige bron); de overige 36 steunen
uitsluitend op PP of secundaire veldbronnen.

| intern # | extern # | uitkomst | toelichting |
|---|---|---|---|
| 1 (Ghurni, geboorte 1828) | 1 (Ghurni ancestraal huis) | `SAME_SITE_SAME_EVENT` | Beide AOY 3872-3877; extern voegt PP-regelankers toe (BRON_GEBLOKKEERD voor die laag). |
| 2 (ancestraal huis, 1833-vloed) | 2 (familie-Shivatempel Ghurni) + 4 (herbouwde Ghurni Shiva Site) | `SAME_SITE_DIFFERENT_GRANULARITY` | Extern splitst mijn ene record correct in drie entiteiten: verwoeste tempel (2), herbouwd heiligdom (4, expliciet `PERSONALLY_PRESENT: NEE` — Lahiri was toen al in Kashi) en het zandbank-kindermeditatiepunt (3). Ik had dit onder één rij "1833-vloed" samengevat; extern is preciezer. Overgenomen als correctie. |
| 3 (Benares, algemene vestiging na 1833) | 6 (huis broer Chandrakanta, Simon Chauhatta, Madanpura) | `SAME_SITE_DIFFERENT_GRANULARITY` | Extern noemt de wijk/host (broer Chandrakanta) die ik niet had; PP-locator, `BRON_GEBLOKKEERD` voor die specificatie. AOY zelf (3875-3877) bevestigt alleen de verhuizing naar Kashi, geen broer-huis. |
| 4 (school Joy Narayan Ghosal) | 9 (Joynarayan English School) | `SAME_SITE_SAME_EVENT` | Beide AOY 3876-3877; extern voegt PP-locatiebeschrijving toe (Sadanand Market, tussen Ramapura/Rewari-talabs) — `BRON_GEBLOKKEERD`, niet AOY-eigen. |
| 5 (Gazipur) | 38 | `SAME_SITE_SAME_EVENT` | Beide AOY 3882 + PP 253-255. |
| 6 (Mirzapur) | 39 | `SAME_SITE_SAME_EVENT` | Idem, met een door PP gemeld chronologieconflict (zie hieronder). |
| 7 (Danapur) | 43 | `SAME_SITE_SAME_EVENT` — **chronologieconflict expliciet onopgelost** | Extern meldt zelf: AOY plaatst de Ranikhet-transfer in **1861** vanuit/naar Danapur; PP plaatst de transferorder op **23-11-1868**. Dit is een reëel, onopgelost conflict tussen AOAY en de nieuwe PP-bron — ik kan dit niet oplossen zonder PP zelf te kunnen lezen (`BRON_GEBLOKKEERD`). Classificatie: `IDENTITY_CONFLICT_UNRESOLVED` voor de exacte datering, terwijl de plaats zelf (Danapur) `SAME_SITE_SAME_EVENT` blijft. |
| 8 (Naini Tal) | 44 | `SAME_SITE_SAME_EVENT` | AOY 3882; extern merkt op dat PP deze post NIET noemt — mogelijk verwarring met Ranikhet-regio. Blijft staan zoals AOY het geeft. |
| 9 (Drongiri-grot/Ranikhet, 1861-ontmoeting) | 48 (Drongiri-berghelling) + 49 (initiatiegrot) + 50 (Gogash-oever) + 51 (paleis) | `SAME_SITE_DIFFERENT_GRANULARITY` | Extern splitst dit (net als bij Babaji) in vier sublocaties. Zelfde als de Babaji-reconciliatie hierboven — kruisverwijzing, niet dubbel geteld. |
| 10 (Garudeswar Mohulla, Benares, eigen woning) | 13 (D/31/58 Madanpura) + 14 (parlour/bedstee) + 15 (huis-shrine) | `SAME_SITE_DIFFERENT_GRANULARITY` — **exact adres niet zelf geverifieerd** | Kernlocatie identiek (mijn "Garudeswar Mohulla" = extern "Garureswar/Gurudham, D/31/58 Madanpura"). Extern splitst in drie sublagen (huis/parlour-sterfkamer/huis-schrijn) met PP-locators. Het exacte huisnummer D/31/58 en de kloktijd van overlijden (17:25) zijn `BRON_GEBLOKKEERD` — niet door mij bevestigd, wel plausibel en niet tegenstrijdig met AOY. De sterfdatum zelf (26-09-1895) is onafhankelijk bevestigd via YSS. |
| 11 (Moradabad, materialisatie aan Babaji-oproep) | 53 (huis Bengaalse vriend, Moradabad) | `SAME_SITE_SAME_EVENT` | AOY 4088-4107 + PP 323-324. PP dateert dit "jan. 1869", AOY impliceert kort na 1861 — zelfde onderliggende chronologieconflict als bij record 7/43. |
| 12 (Allahabad Kumbh Mela) | — | `INTERNAL_ONLY_UNVERIFIED` | Extern vermeldt expliciet in de negatieve-bevindingen-sectie: "Geen voldoende bewijs gevonden voor persoonlijke aanwezigheid in Allahabad/Prayagraj [...]". **Dit is een DIRECT CONFLICT** met mijn eigen record 12, dat steunt op AOAY hfst. 33/34 zelf (Lahiri vertelt zelf over het wassen van de voeten van een asceet op een Kumbha Mela). Ik heb deze AOAY-passage zelf gelezen en het staat er ondubbelzinnig. Classificatie: `FALSE_OR_UNSUPPORTED_EXTERNAL_CLAIM` voor de externe negatieve bevinding — de externe freeze heeft hier een AOAY-passage gemist die ik wel vond. **Dit is de belangrijkste single vondst in deze Lahiri-reconciliatie**: mijn eigen atlas is op dit punt aantoonbaar sterker dan de externe 60-record-set. |
| 13 (Retirement 1886, Benares parlor) | 21 (Ramnagar-paleis, na pensionering) | `SAME_SITE_DIFFERENT_NAME` (deels) + `EXTERNAL_ONLY_UNVERIFIED` | Extern voegt een volledig NIEUWE, grote locatie toe: dagelijkse boottocht naar en verblijf in het Ramnagar-paleis als tutor van Pravunarayan Singh, na pensionering, PP 348-349. Dit is niet in AOAY en niet in mijn interne freeze. Zeer plausibel gezien Lahiri's bekende rol als privéleraar (AOAY noemt elders al een andere maharadja-tutorschap), maar **niet door mij geverifieerd** (`BRON_GEBLOKKEERD`, PP ontoegankelijk). Genoteerd als belangrijke open lead, niet overgenomen als bevestigd feit. |
| 14 (Bengalitola-wijk, schoolstichting) | 16 (Bangalitola High School) | `SAME_SITE_SAME_EVENT` | AOY 3880-3882 + PP 272-275. |
| 15 (Krishnagar/Bishnupur, regionale KRIYA-invloed) | 55 + 56 (twee aparte Bishnupur-huwelijksreizen, 1886 en 1891) | `SAME_SITE_DIFFERENT_GRANULARITY` — **belangrijke precisering** | Ik had dit als vage regionale claim ("reisde meermaals naar Bengal, bezocht schoonfamilies") zonder data. Extern (PP) geeft TWEE aparte, gedateerde reizen: mei 1886 (dochter Harimohini's huwelijk, Kadakuli) en mei 1891 (jongste zoons schoonfamilie + Kailasbabu-initiatie), plus de Panagarh-route en de Tirol-Kali-tempel-medicijnreis (dec. 1892). Belangrijke verdieping, maar wederom `BRON_GEBLOKKEERD` voor de PP-details zelf — de onderliggende AOAY-basisclaim (hfst. 35, "traveled to Bengal... visiting the homes of the fathers-in-law") blijft wel mijn eigen, AOAY-bevestigde uitgangspunt. |
| 16 (sterfplaats Benares, 1895) | 14 (parlour/bedstee) + 32 (Manikarnika Ghat crematie) | `SAME_SITE_DIFFERENT_GRANULARITY` | Extern voegt de crematieplaats (Manikarnika Ghat) toe — logisch, plausibel, maar niet in AOAY en niet door mij geverifieerd (`EXTERNAL_ONLY_UNVERIFIED`, wel zeer waarschijnlijk gezien Manikarnika de standaard crematieghat van Benares is). |
| 17 (Calcutta, Arya Mission Institution — discipel-instelling) | negatieve bevinding | `SAME_SITE_SAME_EVENT` (bevestiging) | Extern bevestigt onafhankelijk hetzelfde: "geen bron gevonden die Lahiri's bezoek aantoont" — matcht mijn eigen `NEE`-classificatie voor Lahiri zelf op deze plek. Geen conflict. |
| 18 (Gorakhpur-materialisatie aan Abinash Babu) | — | `INTERNAL_ONLY_VERIFIED_MISS` | Geen externe tegenhanger. Door mij zelf rechtstreeks in AOAY hfst. 1 geverifieerd (Lahiri Mahasaya materialiseert zich op een veld nabij Gorakhpur en spreekt Bhagabati Charan Ghosh/Abinash Babu aan — dit leidt tot Yogananda's vaders bekering). Extern noemt dit nergens, ook niet in de negatieve-bevindingensectie — waarschijnlijk simpelweg gemist omdat het in hoofdstuk 1 staat, ver van de "biografische" hoofdstukken 32-36 waar extern kennelijk primair zocht. Blijft een geldige, eigen vondst. |
| 19 (Benares, pensionering-tot-dood) | 13/14 (zie boven) | `SAME_SITE_SAME_EVENT` | Samengevoegd met record 10/13-15 hierboven — geen apart nieuw record. |

## Werkpakket B (vervolg) — externe records zonder interne tegenhanger, AOY-gedekt

- **Record 37** (Barrackpore-kamer, Shankari Mai + Babaji): dit is dezelfde scène als de Babaji-
  reconciliatie record BJ-INT-08/B12 — al gereconcilieerd daar, geen dubbele Lahiri-specifieke rij
  nodig. `SAME_SITE_SAME_EVENT`.

## Werkpakket B (vervolg) — 36 externe records uitsluitend op PP/secundaire bronnen (geen AOY-locator)

Records 5, 7, 8, 10-12, 17-20, 22-31, 33-36, 40-42, 45-47, 52, 54, 57-60: allemaal
`EXTERNAL_ONLY_UNVERIFIED` met `BRON_GEBLOKKEERD` (PP-bron ontoegankelijk op moment van deze taak).
Dit betreft o.a. de leerlocaties voor de Nepalese prins en Harashankar Prasad Singhs zoon, meerdere
naamloze discipelhuizen, Ranamahal Ghat + Krishnarams verandah, Panagarh-station en -cart-route,
Burdwan-station, de Tirol-Kali-tempel-reis, en de PWD-posten Buxar en Katwa (die AOAY zelf niet
noemt). Geen van deze is tegengesproken door AOAY — ze liggen simpelweg buiten mijn corpus. Volledige
lijst met PP-regelankers staat in de externe freeze zelf; niet hier herhaald om dubbele,
ongeverifieerde citatie te vermijden.

**Twee waardevolle negatieve bevindingen die mijn eigen terughoudendheid bevestigen** (geen conflict,
extern bevestigt wat ik nooit beweerde): Satyalok/D22/3 Chausattighat (`NEE`, latere memorialtempel)
en de "royale Kashi death-palace" (`NEE`, Lahiri weigerde er expliciet heen te gaan volgens PP).

## Werkpakket C — directe bronverificatie, resultaat

| claim | resultaat |
|---|---|
| Sterfdatum 26-09-1895 | **ONAFHANKELIJK BEVESTIGD** via yssofindia.org, apart van AOAY en van PP. |
| Sterftijd 17:25, huisadres D/31/58, Ramnagar-paleis/Pravunarayan Singh-tutorschap | **BRON_GEBLOKKEERD** — PP-bron (dokumen.pub) meldt "under maintenance", niet leesbaar op moment van deze taak. Niet overgenomen als bevestigd, niet verworpen als onwaar. |
| 1861 (AOAY) vs. 1868 (PP) Ranikhet-transferjaar | **ECHT, ONOPGELOST BRONCONFLICT** — beide bronnen zijn intern consistent met zichzelf maar spreken elkaar tegen. Niet geharmoniseerd, expliciet als `IDENTITY_CONFLICT_UNRESOLVED` gelaten. |
| Allahabad Kumbh Mela-aanwezigheid (Lahiri wast voeten van asceet) | **AOAY-EIGEN TEKST BEVESTIGT DIT WÉL** (hfst. 33) — de externe freeze's negatieve bevinding hierover is dus zelf onjuist/onvolledig. Belangrijkste correctie-in-de-andere-richting van deze reconciliatie. |
| Gorakhpur-materialisatie aan Abinash Babu | **AOAY-EIGEN TEKST BEVESTIGT DIT** (hfst. 1) — bevestigt mijn eigen eerdere directe lezing, blijft internal-only t.o.v. de externe set. |

## Werkpakket D — METHOD_V2-gates, herbeoordeeld

| gate | oordeel | onderbouwing |
|---|---|---|
| `CORPUS_COVERAGE_GATE` | **DEELS** | AOAY volledig (ongewijzigd); PP (de belangrijkste ontbrekende bronfamilie uit mijn oorspronkelijke freeze) is nu geïdentificeerd maar niet zelf gelezen — `BRON_GEBLOKKEERD`, niet stilzwijgend overgeslagen. |
| `HOSTGRAPH_GATE` | **JA voor AOAY; DEELS voor PP-hosts** | AOAY-hostrelaties ongewijzigd bevestigd. PP introduceert tientallen nieuwe hostnamen (Krishnaram, Panchanan Bhattacharya's reisrol, Devnarayan Sanyal, etc.) die ik niet zelf kan natrekken zolang PP ontoegankelijk is. |
| `DISCOVERY_GATE` | **DEELS** | Externe freeze opende een grote, plausibele nieuwe bronfamilie (PP) die mijn eigen Fase 4 niet vond; dat is precies waarvoor de externe detectorlaag bedoeld is. |
| `RECONCILIATION_GATE` | **PROVISIONEEL** | Alle 24 AOY-gedekte externe records + mijn 19 interne records hebben een expliciete uitkomst; één belangrijke interne correctie in mijn voordeel (Allahabad Kumbh Mela), twee grote nieuwe PP-only bevindingen (Ramnagar-paleis, Bishnupur-reisdetails) blijven `BRON_GEBLOKKEERD`/`UNVERIFIED`. PROVISIONEEL i.p.v. JA vanwege zowel PP-ontoegankelijkheid als de ontbrekende IndiaROOD-derde-detector. |
| `EXTERNAL_MODEL_DIVERSITY_GATE` | **NEE** | Zelfde reden als bij Babaji — één ChatGPT-sessie, geen multi-provider-bewijs. IndiaROOD nog niet beschikbaar. |

**`LAHIRI_MAHASAYA_SWEEP_SATURATED: NEE`** — blijft NEE, met twee concrete nieuwe hiaten (PP-bron
ontoegankelijk; IndiaROOD-delta openstaand) bovenop de al bekende hiaten uit de 087-freeze.

## Correcties toegepast op de interne pre-external freeze

1. Record 2 (1833-vloed) opgesplitst in drie entiteiten conform extern: verwoeste tempel, zandbank-
   meditatieplek, en de herbouwde Ghurni Shiva Site (expliciet `PERSONALLY_PRESENT: NEE` voor Lahiri
   zelf — hij was toen al in Kashi). Dit was in mijn oorspronkelijke freeze niet zo scherp
   onderscheiden.
2. Record 15 (regionale Bengal-reizen) verdiend een aantekening dat twee concrete, gedateerde reizen
   (1886, 1891) bestaan volgens PP — nog niet zelf bevestigd, wel als gerichte toekomstige lead
   vastgelegd i.p.v. vaag te blijven.

Geen enkele interne AOAY-eigen claim bleek bij verificatie fout. Het belangrijkste resultaat van deze
reconciliatie is in de ANDERE richting: de externe freeze's negatieve bevinding over Allahabad is
zelf onjuist gebleken bij directe AOAY-herlezing.

## next_allowed_step (voor deze persoon)

1. Verplichte lossless IndiaROOD-deltareconciliatie zodra beschikbaar.
2. Indien de PP-bron (dokumen.pub) later weer bereikbaar wordt: gerichte verificatieronde op de
   hoogste-impact-claims (Ramnagar-paleis/Pravunarayan Singh, sterftijd 17:25, huisadres D/31/58,
   1861-vs-1868-Ranikhet-conflict) — geen nieuwe brede discoverysweep, uitsluitend directe
   bronverificatie van reeds genoteerde claims.
3. Geen cluster/regio, A/B/C, permanente ID's, PDF of route.

---
Geschreven door: CCI, checkpoint 2 van CCI_TASK 088.
