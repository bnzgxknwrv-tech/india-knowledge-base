# BABAJI_RECONCILIATION

```
task_id: TOP11-CORE-KRIYA-RECONCILIATION-001
cci_task: CCI_TASK 088
uitgevoerd_door: CCI
uitgevoerd_op: 2026-08-19
interne_input: runs/active/TOP11-INDIA-PERSON-CENTRIC-MEGASWEEP-001/BABAJI_V2_PRE_EXTERNAL_FREEZE.md
  (freeze commit 6b79f1c8ad25572cb058c047673aef9d5c4284ce, 14 records)
externe_input: agent/chatgpt-top11-parallel-sweep:
  runs/active/TOP11-PARALLEL-CHATGPT-SWEEP-001/BABAJI_PRE_COMPARE_FREEZE.md
  (freeze commit f565ff163e35597d2c4ed802676a4671f9da3b70, 35 records: B01-B35)
INDIA_ROOD_PENDING: JA — bij checkpointmoment (2026-08-19 08:12 UTC) staat op PR #23 nog geen
  duurzame IndiaROOD-freeze-envelop met bestandspad + commit-SHA voor Babaji. Conform CCI_TASK 088's
  addendum (PR-comment over IndiaROOD, TASK.md-commit 5517e46) wordt de tweedetector-reconciliatie
  hieronder wel volledig uitgevoerd, maar RECONCILIATION_GATE is PROVISIONEEL en
  EXTERNAL_MODEL_DIVERSITY_GATE blijft NEE tot een IndiaROOD-freeze lossless is verwerkt.
```

## Methode

Bidirectionele match: elke interne rij (1-14) EN elke externe rij (B01-B35) krijgt exact één
reconciliatie-uitkomst uit de vaste taxonomie van `TASK.md` §5. Directe bronverificatie is
uitgevoerd voor elke external-only claim, elke internal-only claim en elk conflict — de externe
branch is niet gewijzigd, alleen gelezen.

## Canonieke epistemische regel — geen historische Babaji-verificatie

De onderstaande reconciliatie verifieert **claims en hun provenance**, niet Babaji's historische
bestaan of lichamelijke aanwezigheid. Labels als `BODILY_FIRSTHAND`, tier A of
`CLAIM_DOCUMENTED` betekenen alleen dat een bepaalde bron/traditie de ontmoeting als lichamelijk
rapporteert. Canoniek blijft voor ieder Babaji-record:
`HISTORICALLY_VERIFIED_BABAJI_PRESENCE: NIET_VASTSTELBAAR`.
De fysieke site en de aanwezigheid van een beter documenteerbare volgeling/getuige kunnen
afzonderlijk wel worden geverifieerd. Zie
`decisions/BABAJI_MYTHIC_FIGURE_EVIDENCE_RULE_2026-08-19.md`.

## Claimant-tradities in de externe set

De externe freeze dekt vier duidelijk gescheiden tradities. Mijn interne freeze dekte uitsluitend
de eerste, omdat die de enige is die in AOAY zelf voorkomt:

1. `YOGANANDA_LAHIRI_SRI_YUKTESWAR_SRF_YSS` — AOAY + YSS/SRF-lineage (extern B01-B18, plus B32).
2. `KRIYA_BABAJI_NAGARAJ_YOGI_RAMAIAH` — Zuid-Indiase Nagaraj/Ramaiah-Siddha-traditie (extern
   B19-B23 vallen deels ook onder een aparte Nath-lijn via Sri M/Maheshwarnath; B24-B31 zijn de
   kern-Nagaraj/Ramaiah-tak).
3. `HAIDAKHAN_BABAJI` — de historische leraar die 1970-1984 in Haidakhan leefde (extern B33-B35).
4. Sri M/Maheshwarnath's "Sri Guru Babaji" (Nath-sampradaya) is in de externe freeze zelf al apart
   gehouden van de Nagaraj-tak (B19-B22); hier gelabeld `OTHER_OR_UNKNOWN` omdat de externe freeze
   dit niet aan een van de drie bovenstaande vaste categorieën koppelt en de identiteitsclaim zelf
   uitdrukkelijk lineage-eigen/betwist is.

**Hard uitgangspunt, conform TASK.md §7**: een site uit tradities 2-4 is GEEN locatie van "Yogananda's
Mahavatar Babaji" zonder expliciete, bronmatig verifieerbare identiteitsbrug. Zo'n brug is in geen
van deze 22 records (B19-B35, min B32) gevonden — de externe freeze zelf signaleert dit ook al
("expliciet betwist door andere Kriya-lineages", B33/B35-toelichting). Deze 22 records blijven dus
apart geregistreerd, niet gereconcilieerd tegen mijn AOAY-interne 14, en tellen niet mee voor
`PERSON_SWEEP_SATURATED` van "de" Babaji-figuur die in AOAY optreedt.

## Werkpakket A+B — volledige matrix (samenvatting; machineleesbare rijen in RECONCILIATION_MATRIX.jsonl)

### Tak 1 — YOGANANDA_LAHIRI_SRI_YUKTESWAR_SRF_YSS (interne 1-14 vs. externe B01-B13, B32)

| intern # | extern # | uitkomst | toelichting |
|---|---|---|---|
| 1 (Drongiri-grot, Ranikhet, 1861-ontmoeting+initiatie) | B01 (grot/richel) | `SAME_SITE_DIFFERENT_GRANULARITY` | Extern splitst mijn ene record in drie sublocaties (B01 grot, B02 Gogash-rivieroever, B03 tijdelijk paleis). Inhoudelijk identieke gebeurtenis/bron (AOAY hfst. 34), extern preciezer op sublocatieniveau. |
| 1 | B02 (Gogash-rivieroever) | `DISTINCT_SUBLOCATION` | Terecht aparte sublocatie binnen dezelfde gebeurtenis (reinigingsritueel na de initiatie) — AOAY hfst. 34 bevestigt de rivieroeverscène apart van de grot zelf. Ik nam dit direct verifieerbaar detail niet als eigen rij op; toegevoegd als correctie (zie §Correcties). |
| 1 | B03 (tijdelijk paleis) | `DISTINCT_SUBLOCATION` | Idem — het gematerialiseerde paleis is in AOAY zelf een aparte, tijdelijke ruimtelijke laag boven de grot ("the same caves... which yesterday had boasted no adjacency to palace"). Verdient een eigen sub-rij, niet subsumptie onder record 1. |
| (nieuw, ontbrak intern) | B04 (naamloos Himalayakamp: brandend hout + afgrondsprong) | `EXTERNAL_ONLY_VERIFIED_MISS` | **Geverifieerd bij bron**: AOAY hfst. 33 bevat beide Kebalananda-anekdotes woordelijk ("The master suddenly seized a burning log..."; "the arrival of a stranger... jump then... he opened his eyes"). Ik las dit tijdens de freeze maar registreerde het niet als eigen atlasrij — een echte lossless-fout in mijn eigen pas, nu gecorrigeerd. Locatie blijft terecht ONBEKEND/ALLEEN_PLAATS: AOAY noemt geen berg-/plaatsnaam. |
| 2 (algemeen "Badrinarayan"-regio) | B05 (Keshabananda-grot, Badrinath-regio) | `SAME_SITE_DIFFERENT_GRANULARITY` (deels) | Mijn record 2 was de algemene ch. 33-uitspraak dat Babaji "near Badrinarayan" verblijft; record 10 (hieronder) is al specifiek de Keshabananda-grot. Extern B05 komt overeen met mijn record 10, niet met het algemene record 2. Record 2 blijft `INTERNAL_ONLY_UNVERIFIED` als apart, vager regio-gegeven — extern normaliseert de regio-uitspraak niet los als eigen locatie. |
| 3 (Moradabad-huis) | B07 (privéhuis Bengaalse familie, Moradabad) | `SAME_SITE_SAME_EVENT` | Identieke gebeurtenis en bron (AOAY hfst. 34). Extern bevestigt: geen straat/huisnaam bekend — matcht mijn eigen ALLEEN_PLAATS-inschatting. |
| 4 (Allahabad Kumbh Mela-oever, Sri Yukteswar 1894) | B09 (Kumbh Mela 1894, brug+boom) | `SAME_SITE_SAME_EVENT` | Beide bronnen citeren AOAY hfst. 36. Extern voegt toe dat de ontmoeting begon bij een brug vóór de boom — een detail dat in de door mij gelezen passage ("under a tree...") ook staat maar dat ik niet apart als "brug eerst" markeerde. Geen conflict, aanvullende precisie. |
| 5 (Allahabad Kumbh Mela, Lahiri wast voeten van asceet) | B08 (Kumbh Mela, onbepaalde subplek) | `SAME_SITE_SAME_EVENT` | Beide: AOAY hfst. 33, zelfde passage. Extern bevestigt terecht dat dit een ANDERE gelegenheid is dan B09/mijn record 4 (geen jaartal, niet samengevoegd met 1894) — consistent met mijn eigen notitie. |
| 6 (Serampore-banyanboom) | B10 (Rai Ghat-banyan) | `SAME_SITE_SAME_EVENT` — **fysieke identiteit opgewaardeerd** | Extern classificeert dit als `EXACT` (i.p.v. mijn `DEELS`) op basis van S3 (YSS wijst dezelfde, nog bestaande banyan bij Rai Ghat aan). **Bronmatig gecontroleerd**: AOAY hfst. 36 noemt zelf geen straatnaam bij deze scène, dus de `EXACT`-claim steunt op de externe secundaire YSS-identificatie, niet op AOAY zelf. Ik houd `DEELS` aan voor de AOAY-tekst zelf, maar neem de moderne YSS-identificatie over als aanvullende, apart gelabelde institutionele laag (vergelijkbaar met mijn eigen record 14-aanpak). |
| 7 (Benares — Lahiri's parlour/drempel) | B11 (Lahiri's huis: parlour+drempel) | `SAME_SITE_SAME_EVENT` | Identiek, AOAY hfst. 36. Extern voegt een aparte, niet-AOAY lineage-overlevering toe (Pranabananda's ontmoeting met Babaji zou ook hier hebben plaatsgevonden) — dat sub-element is `EXTERNAL_ONLY_UNVERIFIED` (geen AOAY-bevestiging gevonden; AOAY's Pranabananda-hoofdstuk 27 bevat geen Babaji-scène in Lahiri's huis). |
| 8 (Barackpur-kamer) | B12 (privékamer Barrackpore) | `SAME_SITE_SAME_EVENT` | Identiek, AOAY hfst. 31, Shankari Mai Jiew. Geen conflict. |
| 9 (4 Gurpar Road, Yogananda's eigen ontmoeting) | B13 (4 Garpar Road, kamer+vestibule) | `SAME_SITE_SAME_EVENT` — **datumclaim niet bevestigd** | Kernfeit identiek en AOAY-bevestigd (hfst. 37). **Bronmatig gecontroleerd**: de externe freeze citeert een exacte datum "25 juli 1920" met locator "P1, hfdst. 37" — een volledige doorzoeking van hoofdstuk 37 op "1920"/"July"/datumvermeldingen levert alleen "I left India in August, 1920" op, GEEN datum voor de Babaji-scène zelf. De 25-juli-1920-datum staat dus niet in AOAY zelf, ondanks de citatie; het is vermoedelijk een veelgebruikte secundaire SRF/YSS-datering die abusievelijk aan hfst. 37 is toegeschreven. Classificatie: kerngebeurtenis `SAME_SITE_SAME_EVENT`, maar de datum-subclaim is `FALSE_OR_UNSUPPORTED_EXTERNAL_CLAIM` **als AOAY-eigen bewering** (kan alsnog extern correct zijn, alleen niet uit deze bron). |
| 10 (Badrinarayan-grot, Keshabananda) | B05 (naamloze grot bij Badrinarayan, Keshabananda) | `SAME_SITE_SAME_EVENT` | Identiek, AOAY hfst. 42. Extern preciseert "vorig jaar" (t.o.v. 1936-verteltijd) — consistent met mijn eigen "ca. 1935". |
| 11 (was: Ranbajpur/Tarakeswar, Ram Gopal's grot) | B06 (Dashashwamedh Ghat, Varanasi, ondergrondse grot) | `SAME_SITE_DIFFERENT_NAME` — **interne locatiefout gecorrigeerd** | **Bronmatig herlezen (ch. 33, regel ~225-260)**: Lahiri Mahasaya stuurt Ram Gopal (die op bezoek was in Benares, niet in zijn eigen grot) naar "de Dasasamedh bathing GHAT" in Varanasi; daar verschijnen Mataji vanuit een ondergrondse grot onder een stenen plaat, dan Lahiri Mahasaya, dan Babaji. Mijn interne record 11 plaatste deze visioenscène ten onrechte bij "Ram Gopal's eigen grot, Ranbajpur/Tarakeswar" — dat is de plek van een ANDER, apart AOAY-hoofdstuk-13-bezoek van Yogananda aan Ram Gopal, niet van dit visioen. **Correctie**: de Babaji/Mataji/Lahiri-verschijning hoort bij Dashashwamedh Ghat, Varanasi (extern B06 had gelijk); Ram Gopal/Ranbajpur/Tarakeswar blijft een geldig, apart Yogananda-eigen-bezoekpunt (reeds vastgelegd in de Yogananda-atlas), maar niet als locatie van déze Babaji-scène. |
| 12 (was: "Mataji's grot", onbepaald) | B06 | `SAME_SITE_DIFFERENT_NAME` — samengevoegd met de correctie hierboven | Met de correctie op record 11 vervalt de noodzaak voor een apart "Mataji's grot, onbepaald"-record: het IS de Dashashwamedh Ghat-ondergrondse grot uit B06. Record 12 wordt ingetrokken als apart record en opgenomen in het gecorrigeerde record 11/B06. |
| 13 (Badrinarayan, Pranabananda reïncarnatieclaim) | — | `INTERNAL_ONLY_UNVERIFIED` | Geen externe tegenhanger; blijft `SYMBOLIC_VISIONARY_OR_POSTHUMOUS_ONLY`/Tier D zoals origineel geclassificeerd. |
| 14 (modern: Mahavatar Babaji Cave, Kukuchina/Dunagiri) | B01 se secundaire bron S1 | `SAME_SITE_DIFFERENT_GRANULARITY` | Beide onafhankelijk (ik via WebSearch, extern via S1/yssofindia.org) op dezelfde moderne YSS-identificatie van de Drongiri-grot uitgekomen. Bevestigt elkaar, telt niet als twee onafhankelijke vondsten van dezelfde institutionele laag. |
| — | B32 (Satyalok/huis Shibendu Lahiri, Varanasi, jaren '80) | `EXTERNAL_ONLY_UNVERIFIED` | Buiten AOAY (dat eindigt narratief in de jaren '30-'40); geen lokaal primair bronmateriaal om te verifiëren. Blijft in de Yogananda/Lahiri-lijn omdat Shibendu Lahiri een directe Lahiri-Mahasaya-nazaat is, maar de gebeurtenis zelf (jaren '80) ligt ver buiten AOAY's tijdvak. `UNRESOLVED`, geen bronverificatie mogelijk binnen deze taak se toegankelijke corpus. |

### Tak 2-4 — niet-AOAY-tradities (extern B14-B31, B33-B35)

Deze 21 records (Hariharananda: B14-B18; Nagaraj/Ramaiah/Sri M: B19-B31; Haidakhan: B33-B35) hebben
GEEN interne tegenhanger, omdat mijn pre-external freeze bewust AOAY-gecentreerd was (conform
CCI_TASK 087's scope). Classificatie voor elk: `WRONG_PERSON_OR_TRADITION` — niet omdat de externe
freeze fout is (hij documenteert deze tradities zelf al zorgvuldig en apart, inclusief expliciete
identiteitswaarschuwingen), maar omdat deze claims buiten de scope vallen van "Babaji zoals AOAY
hem beschrijft" totdat een bronmatige identiteitsbrug wordt aangetoond. Geen enkele van deze 21
records is dus een miss op mijn interne freeze — ze zijn een correct aparte laag.

Twee vermeldenswaardige interne kruisverwijzingen:
- B14/B15 (Hariharananda, Karar Ashram Puri, 1949) liggen op DEZELFDE ashram-site als de reeds
  bevestigde Sri Yukteswar-hermitage in Puri (zie `SRI_YUKTESWAR_V2_PRE_EXTERNAL_FREEZE.md` record
  2) — een fysieke-plek-overlap tussen twee personen, geen Babaji-traditieoverlap. Vermeld ter
  info, niet gereconcilieerd als Babaji-record.
- B27 (Nagaraj-traditie, Badrinath, 18 maanden in een naamloze grot) en B05/mijn record 10
  (Keshabananda-grot, ook Badrinath-regio) liggen geografisch dicht bij elkaar maar zijn expliciet
  ANDERE tradities/grotten zonder gedeelde bron — terecht apart gehouden, zoals de externe freeze
  zelf ook al aangeeft.

## Werkpakket C — resultaat directe bronverificatie (samenvatting)

| claim | resultaat |
|---|---|
| B01-B03 sublocatie-opsplitsing (grot/rivier/paleis) | **BEVESTIGD** — AOAY hfst. 34 ondersteunt alle drie als aparte ruimtelijke momenten. |
| B04 (Kebalananda-Himalayakamp, brandend hout + afgrondsprong) | **BEVESTIGD als gemiste interne rij** — AOAY hfst. 33, letterlijk aanwezig. |
| B06 vs. mijn interne record 11/12 (Dashashwamedh Ghat vs. Ram Gopal's grot) | **INTERNE FOUT BEVESTIGD EN GECORRIGEERD** — zie boven, ch. 33 herlezen. |
| B09 datum/locatiedetail (brug vóór boom) | **BEVESTIGD, geen conflict**, alleen precisie. |
| B13 datum "25 juli 1920" | **NIET BEVESTIGD IN AOAY HFST. 37** — volledige tekstdoorzoeking op datumtermen levert de claim niet op; alleen "I left India in August, 1920" staat er. Kernscène zelf blijft wel `SAME_SITE_SAME_EVENT`. |
| B10 `EXACT`-upgrade (Rai Ghat-banyan) | **AOAY zelf ondersteunt dit niet met een straatnaam** — de `EXACT`-classificatie steunt op de externe S3-secundaire bron (YSS), niet op AOAY. Overgenomen als apart gelabelde institutionele laag, niet als AOAY-eigen precisie. |
| B11 Pranabananda-in-Lahiri's-huis sub-claim | **NIET BEVESTIGD** — AOAY hfst. 27 (Pranabananda's hoofdstuk) bevat geen Babaji-scène in Lahiri Mahasaya's huis. `EXTERNAL_ONLY_UNVERIFIED`. |

## Werkpakket D — METHOD_V2-gates, herbeoordeeld

| gate | oordeel | onderbouwing |
|---|---|---|
| `CORPUS_COVERAGE_GATE` | **DEELS** | AOAY volledig (ongewijzigd); YSS/SRF-secundaire bronnen nu wél gedeeltelijk gedekt via de externe freeze's S1-S9, maar niet zelf primair geraadpleegd door CCI. Print-only Hariharananda/Nagaraj/Ramaiah/Govindan-bronnen blijven buiten AOAY-scope, terecht. |
| `HOSTGRAPH_GATE` | **JA** | Alle AOAY-hostrelaties bevestigd; geen nieuwe gemiste hostrelatie binnen de AOAY-scope gevonden door de externe vergelijking. |
| `DISCOVERY_GATE` | **DEELS** | Externe freeze voegt vier grote alternatieve tradities toe die mijn discovery niet had geopend (bewust, buiten AOAY-scope) — deze blijven apart gedocumenteerd, niet geïntegreerd zonder identiteitsbrug. |
| `RECONCILIATION_GATE` | **PROVISIONEEL** | Alle 14 interne + 14 relevante externe (B01-B13, B32) records hebben een expliciete uitkomst tussen CCI-intern en de bestaande externe branch; twee interne fouten gecorrigeerd (Ram Gopal/Mataji-locatie, ontbrekende Kebalananda-camprij); één externe datumclaim ongefundeerd bevonden. PROVISIONEEL, niet JA, omdat IndiaROOD (derde detector) bij dit checkpoint nog geen duurzame freeze had — zie `INDIA_ROOD_PENDING: JA` hierboven. Verplichte lossless deltareconciliatie zodra IndiaROOD's Babaji-freeze duurzaam beschikbaar is. |
| `EXTERNAL_MODEL_DIVERSITY_GATE` | **NEE** | De externe freeze is één ChatGPT-sessie met interne parallelle streams — geen aantoonbare multi-provider/multi-model-union (in tegenstelling tot de Yogananda-benchmark met vijf verschillende AI's). Conform TASK.md §10 wordt dit expliciet NEE gelaten, niet als voldaan aangenomen. IndiaROOD (een tweede, onafhankelijke ChatGPT-sessie, momenteel door Mark opgestart) zou dit kunnen verbeteren zodra die freeze beschikbaar is, maar telt zelf ook niet als "ander model." |

**`BABAJI_SWEEP_SATURATED: NEE`** — blijft NEE. Corpus-coverage en discovery zijn DEELS, en
`EXTERNAL_MODEL_DIVERSITY_GATE` is expliciet NEE. Geen valse JA.

## Correcties toegepast op de interne pre-external freeze (vastgelegd, niet stilzwijgend)

1. Record 1 uitgebreid met twee expliciete sublocaties (Gogash-rivieroever, tijdelijk paleis) —
   voorheen impliciet in de narratieve toelichting, nu formeel eigen matrixrijen.
2. Nieuwe rij toegevoegd: Kebalananda's naamloze Himalayakamp (brandend-hout-test +
   afgrondsprong-test), AOAY hfst. 33 — ontbrak in de oorspronkelijke 14.
3. **Locatiefout gecorrigeerd**: de Babaji/Mataji/Lahiri-verschijning (voorheen records 11+12,
   "Ram Gopal's grot"/"Mataji's grot, onbepaald") is herlokaliseerd naar Dashashwamedh Ghat,
   Varanasi, conform de letterlijke AOAY-tekst (hfst. 33). Ram Gopal Muzumdars eigen grot bij
   Ranbajpur/Tarakeswar blijft een geldig, apart Yogananda-bezoekpunt, maar was nooit de locatie van
   déze specifieke visioenscène.

Deze drie correcties zijn NIET stilzwijgend verwerkt in het oorspronkelijke `BABAJI_V2_PRE_EXTERNAL_
FREEZE.md`-bestand (dat blijft ongewijzigd staan als bevroren record van de blinde pas) — ze staan
hier, in dit reconciliatiebestand, als expliciete, dateerbare correctie.

## next_allowed_step (voor deze persoon)

Verplichte lossless IndiaROOD-deltareconciliatie zodra een duurzame IndiaROOD-Babaji-freeze met
bestandspad + commit-SHA op PR #23 verschijnt — deze checkpoint wordt dan niet herschreven, de
delta wordt als aanvulling toegevoegd. Tot die tijd verder geen actie binnen deze taak. Geen
cluster/regio, A/B/C, permanente ID's, PDF of route.

---
Geschreven door: CCI, checkpoint 1 van CCI_TASK 088.

## DELTA — CCI_TASK 092 (2026-08-19, IndiaROOD-derde-detectorreconciliatie)

Volledige drieweg-reconciliatie tegen de nu duurzame IndiaROOD-freeze (50 records, commit
`f9e7e25`): zie `runs/active/TOP11-CORE-KRIYA-INDIAROOD-DELTA-RECONCILIATION-001/BABAJI_INDIAROOD_DELTA.md`.

**Belangrijkste uitkomst**: `INDIA_ROOD_PENDING: JA` hierboven is nu opgelost.
`EXTERNAL_MODEL_DIVERSITY_GATE` gaat van **NEE naar JA** — IndiaROOD is een tweede, aantoonbaar
onafhankelijke ChatGPT-sessie die een geheel nieuwe claimanttraditie vond (Hansavedas/Tryambaknath)
die noch CCI, noch de eerste externe sessie had ontdekt. `RECONCILIATION_GATE` gaat van
**PROVISIONEEL naar JA** voor de drieweg-vergelijking zelf.

Twee bestaande 088-correcties (Dashashwamedh Ghat i.p.v. Ram Gopal's grot; "25 juli 1920" als
niet-AOAY-eigen datum) zijn onafhankelijk drievoudig cross-gevalideerd doordat IndiaROOD zelf tot
dezelfde bevindingen kwam. Eén volledig nieuwe traditie (Hansavedas/Tryambaknath, records 29-31)
is Tier-1 bronmatig bevestigd. IndiaROOD breidt de Haidakhan-tak uit van 3 naar 19 records, maar
mist de volledige Sri M/Nath-traditie (extern B19-B23) en vijf kleinere Yogananda-lijn-records
(Barrackpore, Hariharananda-stem-Ranikhet, twee Daya-Mata-visioenen, Satyalok/Shibendu Lahiri).

`BABAJI_SATURATED: NEE` blijft de eerlijke uitkomst — zie de volledige gate-heroverweging in de
delta-file.

Checkpoint: Babaji-IndiaROOD-delta, CCI_TASK 092, checkpoint 1/3.
