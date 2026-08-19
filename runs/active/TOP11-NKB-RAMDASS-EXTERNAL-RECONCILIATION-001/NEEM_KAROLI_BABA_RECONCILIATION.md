# NEEM_KAROLI_BABA_RECONCILIATION

```
task_id: TOP11-NKB-RAMDASS-EXTERNAL-RECONCILIATION-001
cci_task: CCI_TASK 091
uitgevoerd_door: CCI
uitgevoerd_op: 2026-08-19
internal_source: runs/active/TOP11-NKB-RAMDASS-V2-PRE-EXTERNAL-001/NEEM_KAROLI_BABA_V2_PRE_EXTERNAL_FREEZE.md
  (21 records: 19 origineel + 2 uit CCI_TASK 090-delta)
external_source: agent/chatgpt-top11-parallel-sweep,
  runs/active/TOP11-PARALLEL-CHATGPT-SWEEP-001/NEEM_KAROLI_BABA_PRE_COMPARE_FREEZE.md
  (113 records; commit 180bf023a0a06f7ebb0d9df762e5fe0530f59954, blob-sha 867d96559886a911b585b72134bd44dace86661a
  — integriteit bevestigd via directe GitHub-blobvergelijking vóór opening)
```

## 0. Directe bronverificatie — methode en dekking

De belangrijkste externe primaire bron (**P1**, Sudhir "Dada" Mukerjee, *The Near and the Dear:
Stories of Neem Karoli Baba and His Devotees*, dokumen.pub) bleek — in tegenstelling tot *By His
Grace* op dezelfde site — **wél volledig legaal toegankelijk** (HTTP 200, geen inlog, geen
"under maintenance"). Volledige platte tekst gedownload (688K tekens) en corpusbreed doorzocht.

Toegepaste verificatiediepte per bewering:

- **Tier 1 — volledig gelezen in context** (directe quote gecontroleerd): de Panki-
  bilocatie-episode (record 89), de doodslocatie/-volgorde (records 109-113).
- **Tier 2 — corpusaanwezigheid bevestigd** (plaats-/persoonsnaam daadwerkelijk in P1
  teruggevonden, met steekproefsgewijze contextlezing, maar niet elke afzonderlijke episode
  woord-voor-woord doorgelicht): de meerderheid van de P1-gebaseerde external-only-records
  (Fatehgarh, Bijnor, Ram Narayan Sinha, 4 Church Lane, Allahabad-episodes, Nainital/Bhowali/
  Bhimtal/Haldwani/Almora-keten, Bareilly, Kotdwara/Pauri, Kedarnath/Badrinath/Gangotri/Gomukh/
  Haridwar/Rishikesh, Varanasi/Vindhyachal/Chitrakut, Dwarka/Rameshwaram/Puri/Dakshineshwar,
  Kanpur/Lucknow-huizen, Gomati-brug-episode). Dit is eerlijk een lichtere verificatietrap dan
  Tier 1, expliciet zo benoemd.
- **Tier 3 — extern geverifieerd via secundaire bron, probleem gevonden**: de doodsvolgorde
  (zie §2, conflict Mathura-tussenstop).
- **Niet verifieerbaar**: claims die uitsluitend op *Miracle of Love* of *By His Grace* rusten
  blijven `BRON_GEBLOKKEERD`, zoals in CCI_TASK 090 vastgesteld — niet opnieuw geforceerd.

Twee zoekfouten van mezelf zijn tijdens deze pas ontdekt en gecorrigeerd (spellingvarianten
"Chitrakoot"→"Chitrakut", "Rameswaram"→"Rameshwaram", "Dakshineswar"→"Dakshineshwar",
"Gomti"→"Gomati"): eerste greps op de externe spelling misten deze termen, een tweede ronde met
brontrouwe spelling vond ze alle terug. Dit wordt hier vermeld omdat het aantoont dat de externe
P1-citaten in deze gevallen **wél correct** waren — niet gehallucineerd.

## 1. Matrix — interne records tegen externe records

| intern # | interne locatie | externe match(es) | classificatie | toelichting |
|---:|---|---|---|---|
| 1 | Akbarpur (geboortedorp) | ext #1-3 | SAME_SITE_DIFFERENT_GRANULARITY | Extern splitst in dorp/geboortehuis/latere-tempel (2001, negative control). Extern district: Firozabad; intern noemde Ambedkar Nagar/Faizabad als onzeker alternatief — extern bevestigt Firozabad als lineage-bron, met expliciete waarschuwing dat tertiaire bronnen Ambedkar Nagar fout toeschrijven. **Correctie overgenomen** (zie §3). |
| 2 | Badam Baas (echtgenotes dorp) | geen | INTERNAL_ONLY | Extern bevat geen equivalent record; niet weersproken, ook niet bevestigd. |
| 3 | Vavania (Gujarat) | ext #4-7 | SAME_SITE_MORE_GRANULAR | Extern splitst in ashram/vijver/Hanuman-murti/Zuid-Indiaroute; intern had dit als één record. |
| 4 | Neem Karoli-dorp/station (naamgevende episode) | ext #8-12 | SAME_SITE_MORE_GRANULAR | Extern splitst dorp/grot/murti/station/perron. Direct bronmatig geverifieerd via P1 (Tier 2): treinepisode aanwezig en consistent. |
| 5 | Kainchi Dham | ext #41-49 | SAME_SITE_MORE_GRANULAR | Extern levert 9 sublocaties (rivierstenen, chabootara, kantoor/tucket, verandah, keuken, achterkamer, gronden). Waardevolle sublocatie-uitbreiding, geen conflict. |
| 6 | Bhumiadhar Ashram | ext #38-40 | SAME_SITE_MORE_GRANULAR | Extern voegt eerste hut vóór de tempel toe. |
| 7 | Kakrighat | ext #50-51 | SAME_SITE_MORE_GRANULAR | Extern voegt oeverlocatie toe; P1 zelf noemt de plaatsnaam "Kakrighat" niet letterlijk (S8 is hoofdbron, P1 alleen als "Almora-road episodes" secundair aangehaald) — secundaire P1-koppeling is losser dan de tabel suggereert, geen harde fout maar wel vermeldenswaardig. |
| 8 | Vrindavan Ashram | ext #104-108 | SAME_SITE_MORE_GRANULAR | Extern voegt kamer/verandah/crematieplek toe en behoudt hetzelfde `NEE`-negative-control-record voor de latere Mahasamadhi Mandir (#108) dat intern al impliciet als "later" behandelde. Consistent. |
| 9 | Panki Hanuman-tempel Kanpur (NIET persoonlijk bij opening) | ext #89 | SAME_EVENT — **CONFIRMED_TRUE (Tier 1)** | Rechtstreeks in P1 gelezen: de bilocatie-episode ("Babaji had been there in the morning, but at twelve he suddenly disappeared" tegenover Mr. Jagati's ooggetuigenverslag dat Babaji de hele tijd ziek op bed lag) komt woordelijk overeen met zowel het interne als externe verslag. Beide bronnen classificeren dit terecht als `ONZEKER`/niet-fysieke-aanwezigheid, geen upgrade naar bewezen bilocatie. |
| 10 | Kamer in Allahabad (bilocatieclaim) | ext #89 (zelfde episode, ander perspectief) | DUPLICATE_OR_ALIAS | Dit is dezelfde gebeurtenis als intern record 9/extern #89, bekeken vanuit de kant "waar was hij dan echt" — geen apart fysiek record, samengevoegd in de toelichting. |
| 11 | Mathura Railway Station (laatste reis) | ext #112 | SAME_SITE — **CONFLICT (zie §2)** | Extern bevestigt het treinstation, maar een tweede extern-geciteerde bron (S15) beschrijft een andere reisvolgorde zonder Mathura-tussenstop. Zie §2. |
| 12 | Agra (vertrekpunt) | ext #109-111 | SAME_SITE_MORE_GRANULAR — CONFLICT (zie §2) | Extern splitst in familiehuis/kliniek/station. |
| 13 | Ziekenhuis (naamconflict onopgelost) | ext #113 Ramakrishna Mission Hospital, Vrindavan | **CONFLICT OPGELOST — CONFIRMED_TRUE (Tier 1)** | Rechtstreeks bronmatig geverifieerd via S15 (maharajji.love/heaven-at-shri-vrindavandham/, WebFetch 2026-08-19): "he left his body in Ramakrishna Mission hospital at Vrindavan the same night." Interne freeze wordt bijgewerkt: ziekenhuis = **Ramakrishna Mission Hospital, Vrindavan** (niet Mathura). Zie §2 voor een nieuw, apart conflict over de exacte reisvolgorde. |
| 14 | Crematieplaats Vrindavan | ext #107 | SAME_SITE | Consistent. |
| 15 | Rishikesh Ashram (ONZEKER) | ext #76 Veerbhadra (ONZEKER) | SAME_SITE_DIFFERENT_GRANULARITY | Beide bronnen behouden terecht onzekerheid; extern voegt toe dat huidig complex grotendeels na 1984 is gebouwd. |
| 16 | Lucknow Ashram (ONZEKER) | ext #97 Sankat Mochan/Hanuman Setu (ONZEKER) | SAME_SITE | Consistent, beide onzeker. |
| 17 | Shimla Ashram (ONZEKER) | ext #100-101 Taradevi hut + Sankat Mochan Shimla (ONZEKER) | SAME_SITE_MORE_GRANULAR | Extern voegt Taradevi-hut (9-10 dagen, jaren '50) toe vóór het tempelplan. |
| 18 | Delhi Ashram (ONZEKER) | ext #102-103 Jonapur Ashram (**JA/EXACT**, zomer 1973) | **CONFLICT OPGELOST — interne onzekerheid opgeheven** | Extern (S9, maharajji.love/delhi-ashram) geeft een concrete datum (zomer 1973 inauguratie) en EXACT-status. Niet apart rechtstreeks herbevestigd via S9 zelf binnen deze taak (tijdsbudget), maar wel intern overgenomen als sterkere claim dan de eigen oorspronkelijke ONZEKER — zie §3. |
| 19 | Hanuman Garhi (Kumaon-heuvels, ONZEKER) | ext #31-34 Hanumangarhi Nainital (**JA/EXACT**) | **CONFLICT OPGELOST** | Extern plaatst dit specifiek bij Nainital (niet generiek "Kumaon-heuvels") met stichtingsgeschiedenis. Kruisverband: Ram Dass bezocht dezelfde tempel later (Ram-Dass-extern #30) — zie RAM_DASS_RECONCILIATION.md. Let op: P1 zelf bevat de term "Hanuman Garhi"/"Hanuman Garh" **niet** (corpuscontrole negatief) — S5 (maharajji.love) is hier de enige echte primaire bron, P1 is niet bruikbaar als onafhankelijke tweede bevestiging voor déze specifieke naam. |
| 20 (090) | Forestry camp (onbenoemd) | Ram-Dass-extern #16 (cross-person) | SAME_SITE | Extern NKB-freeze heeft geen eigen Forestry-camp-record; bevestigd via de Ram Dass-kant van dezelfde externe sweep. Geen conflict. |
| 21 (090) | Onbenoemde "estate" bij Delhi | Ram-Dass-extern #6 (cross-person) | SAME_SITE | Idem. |

## 2. Onopgeloste conflicten — expliciet

### 2.1 Doodsvolgorde: Mathura-tussenstop wel of niet?

- **Interne freeze (Wikipedia-gebaseerd) + externe records #109-112**: Agra (familiehuis,
  hartkliniek 10 sept.) → nachttrein richting Kainchi → **stapte ziek uit te Mathura** (convulsies)
  → ziekenhuis.
- **S15 (maharajji.love/heaven-at-shri-vrindavandham/, direct gecontroleerd, Tier 1)**: "Baba
  left Kainchi on September 9... arrived at Agra on September 10... he left his body in
  Ramakrishna Mission hospital at Vrindavan the same night" — **geen Mathura-tussenstop genoemd**,
  en de volgorde is Kainchi→Agra→(dezelfde nacht)→Vrindavan, niet Agra→trein→Mathura→ziekenhuis.
- Dit is een **onopgelost bronconflict tussen twee secundaire tellingen**, niet opgelost binnen
  deze taak — beide varianten worden behouden, met dit conflict expliciet vermeld in plaats van
  stilzwijgend één versie te kiezen.

### 2.2 Kakrighat/Hanumangarhi als secundaire P1-citaten

Zoals hierboven genoteerd: de externe freeze citeert P1 als secundaire steun voor zowel Kakrighat
(#50) als Hanumangarhi (#33), maar geen van beide plaatsnamen komt letterlijk in P1 voor. Dit is
geen bewezen fout (P1 kan de gebeurtenis beschrijven zonder de huidige plaatsnaam te gebruiken,
zoals bij de Kainchi-naam in *Be Here Now* het geval bleek in CCI_TASK 090), maar het is een
zwakkere secundaire koppeling dan de tabel-opmaak suggereert. Genoteerd, niet als fout
geregistreerd.

## 3. Correcties overgenomen in de interne freeze

1. **Geboortedistrict Akbarpur**: Firozabad (extern, met lineage-onderbouwing) in plaats van het
   interne "Ambedkar Nagar (historisch Faizabad)" — de externe freeze citeert expliciet dat
   tertiaire bronnen Ambedkar Nagar fout toeschrijven, wat overeenkomt met de eigen interne
   voetnoot ("Firozabad-district... niet hard weerlegd"). Nu wel overgenomen.
2. **Doodsziekenhuis**: Ramakrishna Mission Hospital, Vrindavan — rechtstreeks bronmatig bevestigd
   (Tier 1), vervangt de interne "onopgelost naamconflict".
3. **Delhi Ashram en Hanuman Garhi**: interne ONZEKER-status opgeheven naar de externe JA/EXACT-
   bevindingen (Jonapur-ashram zomer 1973; Hanumangarhi Nainital), met de kanttekening dat S9/S5
   zelf niet binnen deze taak rechtstreeks zijn nagelopen (tijdsbudget) — wel overgenomen omdat de
   externe freeze's eigen adversarial-discipline (zie haar "Adversarial non-upgrades"-sectie)
   consistent bleek betrouwbaar bij alle steekproeven die wél rechtstreeks zijn gecontroleerd.

## 4. Nieuwe fysieke locaties bevestigd (samenvatting)

Circa 90 externe records zonder interne tegenhanger (Fatehgarh-kazerne, Bijnor, Ram Narayan Sinha's
huis, Dwarkadhish-tempel, de volledige 4 Church Lane-cluster in Prayagraj, Allahabad-station/
oever/overstroomde tempel, Nainital-straten/ziekenhuis, Bhowali/Bhimtal/Haldwani/Almora-keten,
Bareilly-netwerk, Kotdwara/Pauri/Kedarnath/Badrinath/Gangotri/Gomukh/Haridwar/Rishikesh-
pelgrimsroute, Varanasi/Vindhyachal/Chitrakut, Dwarka/Rameshwaram/Puri/Dakshineshwar/Kolkata,
Kanpur/Lucknow-devoteehuizen) — allemaal Tier-2-corpusaanwezigheid bevestigd in P1, toegevoegd als
`EXTERNAL_ONLY` in de matrix (zie `RECONCILIATION_MATRIX.jsonl`), niet stuk voor stuk woordelijk
herverifieerd binnen het tijdsbudget van deze taak.

## 5. Adversarial non-upgrades — bevestigd, geen wijziging nodig

De externe freeze's eigen negative-control-records (2001-Akbarpur-tempel, Vrindavan Mahasamadhi
Mandir, Panki-niet-persoonlijk-aanwezig, Veerbhadra-Rishikesh-na-1984, "India Hotel Nainital" niet
opgenomen) zijn beoordeeld als methodologisch correct en vergen geen interne correctie.

## 6. Per-persoon rapportage

- **Internal count vóór reconciliatie**: 21.
- **External count**: 113.
- **Matched/duplicate**: 19 interne records matchen (direct of via granulariteit) op externe
  records; 1 is een duplicaat-perspectief (record 10 = record 9/ext #89); 2 (Forestry camp,
  estate) matchen cross-person op de Ram Dass-externe freeze.
- **External-only**: ca. 94 externe records zonder interne tegenhanger (grotendeels P1-
  gebaseerd, Tier 2 bevestigd).
- **Internal-only**: 1 (Badam Baas).
- **Verified true/false/partial/unresolved**: 2 volledig bronmatig bevestigd (Tier 1: Panki-
  bilocatie, doodsziekenhuis); 1 onopgelost conflict (doodsvolgorde/Mathura); ca. 90 Tier-2
  (corpusaanwezigheid, niet woordelijk); rest niet apart geverifieerd (blijft `BRON_GEBLOKKEERD`
  waar op MOL/By His Grace gebaseerd, of niet binnen budget nagelopen waar op S1-S16 gebaseerd).
- **Nieuw bevestigde fysieke locaties**: zie §4 (ca. 90, Tier 2).
- **Gecorrigeerde claims**: 3 (zie §3).
- **Resterende bronblokkades**: *Miracle of Love*, *By His Grace* — ongewijzigd `BRON_GEBLOKKEERD`
  sinds CCI_TASK 090.
- **Actuele vier METHOD_V2-gates**:
  - CORPUS-COVERAGE-GATE: **DEELS** (verbeterd van NEE — P1 nu volledig doorzocht; MOL/By His
    Grace blijven dicht).
  - HOSTGRAPH-GATE: **DEELS** (sterk uitgebreid: Jaidev Singh, Ram Narayan Sinha, Mukerjee-
    huishouden, Shukla-familie, Tularam, Jivan, Hubbaji, K.C. Tewari e.a. nu bevestigd).
  - DISCOVERY-GATE: **DEELS** (externe freeze dekt vrijwel de volledige P1-bibliografie).
  - RECONCILIATIE-GATE: **DEELS** (deze taak; IndiaROOD Core-Kriya-vergelijking blijft een aparte
    taak conform TASK.md §8).
- **Eerlijke saturationstatus**: **`NEEM_KAROLI_BABA_SATURATED: NEE`** — de externe freeze zelf
  claimt ook geen saturatie (P1 alleen dekt niet elk devoteehuis; MOL/By His Grace blijven dicht).

---
Geschreven door: CCI. Checkpoint 1/2 van CCI_TASK 091.
