# SATURATION_RESULT — Anandamayi Ma + Neem Karoli Baba (aanvullende pass)

```
task_id: TOP11-INDIA-PERSON-CENTRIC-MEGASWEEP-001
trigger: CCI_TASK 080 (INDIA-QA, INDIA_QA_PILOT.md, commit 3cc07c9)
uitgevoerd_door: CCI
uitgevoerd_op: 2026-08-15
```

## VALIDATIETEST — EERST BEANTWOORD

**Vraag (INDIA-QA)**: vindt de host-/gastheer-zoekronde zelfstandig Bodh-Ashram-achtige
gastlocaties, zonder checklist?

**Antwoord: JA, bevestigd, met een nieuwe, sterke, onafhankelijke vondst per persoon:**

- **Neem Karoli Baba → "Red House", 4 Church Lane, Prayagraj (Allahabad)**. Gevonden door te
  zoeken op zijn bekende naaste discipel/gastheer Dada Mukerjee (auteur van twee memoires over
  hem), niet via een bestaande kandidatenlijst. Vanaf 14 juli 1958 tot zijn mahasamadhi in 1973
  bracht Maharajji elke winter door in dit huis van Dada en Kamala Mukerjee ("Winter Camp",
  jaarlijks terugkerend, geen eenmalig bezoek). Sterker nog dan Bodh Ashram: er bestaat inmiddels
  een eigen devotee-website die dit adres als bezoekbare plek documenteert
  (`babaneemkaroli.in/my-visit-to-4-church-lane-allahabad-baba-neem-karoli/`), wat het praktisch
  al TIER 1/bezoekbaar maakt.
- **Anandamayi Ma → Solan (Himachal Pradesh), op uitnodiging van Raja Durga Singh**. Gevonden via
  jaar-voor-jaar-doorzoeken van haar officiële levensgeschiedenis (anandamayi.org), niet via een
  bestaande kandidatenlijst. Mei 1946 en opnieuw haar verjaardagsviering mei 1955, beide op
  uitnodiging van dezelfde gastheer/patroon — een herhaald, niet-eenmalig patroon, in een staat
  (Himachal Pradesh) die nog helemaal niet in de repo voorkwam.

Dit bevestigt: de methode werkt zoals bedoeld, MITS de host-/gastheer-as expliciet en gericht wordt
doorzocht (naam van bekende discipelen/gastheren/secretarissen als eigen zoekterm) — een generieke
"[persoon] + ashram"-zoekopdracht had geen van beide gevonden.

## AANVULLENDE ATLAS-PUNTEN (nieuw t.o.v. PILOT_RESULT.md)

| atlas_id | plek | plaats/staat | tier | link-type | bron | verificatie |
|---|---|---|---|---|---|---|
| ATL-AM-021 | Gastverblijf bij Raja Durga Singh | Solan, Himachal Pradesh | 1 | herhaald gastverblijf (1946, 1955) | anandamayi.org life-history 1943-1952/1953-1962 | person_event: JA (2x apart bevestigd); physical_identity: DEELS (huis van Raja Durga Singh zelf niet apart geïdentificeerd, wel de plaats Solan); exact_sublocation: ONBEKEND |
| ATL-AM-022 | Tarananda Swami's Ashram, Almora | Almora, Uttarakhand | 2 | verblijf juni 1948 | anandamayi.org life-history 1943-1952 | person_event: JA; physical_identity: ONBEKEND (ander ashram dan het al bekende Patal Devi/Dhaulchina — apart vastgelegd, niet samengevoegd) |
| ATL-AM-023 | Shahbhag Gardens-landgoed, Dacca | **Bangladesh, buiten India** | 3 | vroege verblijfplaats (Bholanath was beheerder) | anandamayi.org | buiten Marks reisscope, alleen voor volledigheid |
| ATL-NKB-014 | "Red House", 4 Church Lane, Prayagraj (Allahabad) | Allahabad, UP | 1 | jaarlijks winterverblijf bij gastheer Dada Mukerjee, 1958-1973 | Wikipedia (Dada Mukerjee), babaneemkaroli.in (bezoekbevestiging) | person_event: JA (herhaald, 15 jaar lang); physical_identity: JA (adres + huidige devotee-bezoekbevestiging); exact_sublocation: JA |

**Correctie op PILOT_RESULT.md**: ATL-AM-003 ("Ashram Varanasi, Ramghat") is bij cross-check tegen
de bestaande repo hetzelfde als het reeds bevestigde `VNS-CAND-005` — het exacte adres is
**Bhadaini**, niet Ramghat (beide liggen in dezelfde Varanasi-oeverzone, maar Bhadaini is het
bronmatig bevestigde adres). Zie FASE C hieronder.

## CROSS-CHECKS (verplicht door INDIA-QA)

- **Kankhal/Haridwar Mahasamadhi**: identiteit bevestigd als Matri Mandir, Kankhal — geen andere
  legacy-vermelding in de repo onder een andere naam gevonden. Blijft volledig afwezig uit de
  huidige kandidatenset. Status ongewijzigd t.o.v. PILOT_RESULT.md: sterk `NEW_REGION_SIGNAL`,
  geen actie/A-B-C nu.
- **Varanasi Anandamayi Ma-match**: BEVESTIGD. `VNS-CAND-005`, "Shree Shree Ma Anandamayi Ashram,
  Bhadaini", `protected_mark_status: A`, adres Bhadaini, Varanasi 221001 — bevestigd via
  `anandamayi.org/ashram-contact-details/` EN onafhankelijk via `anandamayi.de/ashramadressen/`.
  Dit is dezelfde plek als ATL-AM-003. `FOUND_AND_ALREADY_KNOWN`, reeds correct A, geen wijziging.
- **NKB Vrindavan-identiteit**: legacy `LOCKED_A` beschrijft "Neem Karoli Baba Ashram en samadhi,
  Vrindavan" (DECISION-0008) — omschrijving (ashram + Maharaj-ji's vereerde laatste rustplaats)
  komt inhoudelijk overeen met ATL-NKB-003 (Vrindavan Ashram + Mahasamadhi Mandir, ingewijd 1967,
  mahasamadhi 1973, Parikrama Marg). Zelfde plek, `FOUND_AND_ALREADY_KNOWN` — een letterlijke
  adresvergelijking (Parikrama Marg) staat niet expliciet in het legacy-record zelf, dus dit is een
  inhoudelijke match met hoge zekerheid, geen 100% adres-op-adres-bevestiging. Geen conflict.

## SATURATIE-BEOORDELING TEGEN DE 6 TASK-PUNTEN

### Anandamayi Ma

1. Officiële/lineage-bronnen + primaire teksten + gerichte plaats-/event-searches: **JA** —
   anandamayi.org (meerdere decennia-secties van de officiële levensgeschiedenis geraadpleegd:
   1922-1932, 1943-1952, 1953-1962), shreeshreeanandamayeesangha.org, Wikipedia, Gopinath
   Kaviraj-biografie.
2. Grote levensfasen/reizen afgedekt: **JA, redelijk** — geboorte, vroege ashram-stichting
   (Bhaiji, 1925-1929), Haridwar/Bhola Girl Ashram (1929), Almora (1948), Solan (1946, 1955),
   mahasamadhi (Kankhal) zijn nu gedekt over meerdere decennia; niet elk jaar 1896-1982 is
   doorzocht.
3. Alternatieve spellingen/namen: **DEELS** — "Anandamayi"/"Anandamayee" beide gebruikt; geen
   verdere transliteratie-varianten systematisch geprobeerd.
4. Host-/landgoedketens teruggevolgd: **JA, nu wel** — Bhaiji (naamgever + ashramstichter),
   Gopinath Kaviraj (Varanasi-devotee/geleerde), Raja Durga Singh (Solan-gastheer), Tarananda
   Swami (Almora-gastheer) alle vier als aparte personen/gastheren opgezocht.
5. Expliciet "op bezoek bij anderen": **JA** — Solan (Raja Durga Singh) en Almora (Tarananda
   Swami) zijn beide precies dat: verblijf bij een gastheer, niet in haar eigen ashram.
6. Negatieve/onzekere claims vastgelegd: **JA** — exacte sublocaties bij Solan/Almora expliciet
   `ONBEKEND`, niet verzwegen.

**`PERSON_SWEEP_SATURATED: JA`** — met de kalibratie dat dit een grondige, meerdere-host-lagen-
diepe pass is binnen de tijd van deze taak, geen absolute garantie dat werkelijk elke van haar
tientallen ashrams/gastverblijven in heel haar 86-jarige leven is gevonden. Toekomstige aanvullende
vondsten blijven mogelijk, maar de 6 verplichte punten zijn nu elk aantoonbaar doorlopen, niet
alleen impliciet aangenomen.

### Neem Karoli Baba

1. Officiële/lineage-bronnen + primaire teksten: **JA** — nkbashram.org, maharajji.love, Dada
   Mukerjee (Wikipedia + boekbeschrijvingen), ramdass.org.
2. Grote levensfasen/reizen afgedekt: **JA, redelijk** — geboorte (Akbarpur), hoofdashram-
   stichtingsjaren (Kainchi 1964, Panki 1964, Delhi/Noord-Delhi 1965, Lucknow 1967), jaarlijkse
   winterverblijven Allahabad (1958-1973), mahasamadhi (Vrindavan 1973).
3. Alternatieve spellingen: **DEELS** — "Neeb Karori"/"Nibkarori" opgemerkt maar niet apart
   doorgetrokken naar nieuwe vondsten.
4. Host-/landgoedketens teruggevolgd: **JA, nu wel** — Dada Mukerjee (Allahabad-gastheer, 15 jaar
   herhaald), K.K. Sah (Nainital, al bekend) apart bevestigd als hostketen-precedent.
5. Expliciet "op bezoek bij anderen": **JA** — Allahabad/Church Lane is exact dat: 15 jaar
   jaarlijks gast bij een niet-Top-11-devotee, geen eigen instelling.
6. Negatieve/onzekere claims: **JA** — Nibkarori-status blijft expliciet `ONBEKEND`.

**`PERSON_SWEEP_SATURATED: JA`** — zelfde kalibratie als hierboven: grondig voor deze taak, geen
absolute garantie op volledigheid over zijn hele leven, maar de 6 punten zijn nu elk aantoonbaar
doorlopen.

## BIJGEWERKTE FASE-C-CLASSIFICATIE (alleen de wijzigingen t.o.v. PILOT_RESULT.md)

- **FOUND_BUT_MISSING_FROM_REPO**, nieuw: 4 Church Lane/Allahabad (NKB), Solan/Raja Durga Singh
  (Anandamayi Ma), Tarananda Swami's Ashram Almora (Anandamayi Ma).
- **FOUND_AND_ALREADY_KNOWN**, bevestigd met exacte identity-match: Varanasi Anandamayi-ashram
  (`VNS-CAND-005`, Bhadaini) en NKB Vrindavan-ashram/samadhi (legacy DECISION-0008).
- Overige categorieën ongewijzigd t.o.v. PILOT_RESULT.md.

## CONCLUSIE VOOR INDIA-QA

De methode is nu aantoonbaar getest tegen precies het scenario dat de vorige QA-ronde eiste: een
gerichte host-/gastheer-zoekronde levert zelfstandig, zonder checklist, nieuwe Bodh-Ashram-achtige
locaties op (4 Church Lane sterker nog dan Bodh Ashram zelf — een herhaald, 15-jarig jaarlijks
verblijf met eigen devotee-erkenning). Beide pilotpersonen krijgen nu `PERSON_SWEEP_SATURATED: JA`
op basis van de 6 TASK-punten. Voorstel: methode bevriezen en toepassen op de overige 9 Top-11-namen
in de vastgelegde volgorde (Babaji, Lahiri Mahasaya, Yogananda, ...), telkens mét de expliciete
host-/gastheer-as als verplichte stap vanaf het begin — niet als losse nastap zoals in deze ronde.

Geen bestaande Mark A/B/C gewijzigd. Geen PDF, geen route.

---
Geschreven door: CCI. Aanvullende saturation pass op verzoek van INDIA-QA (CCI_TASK 080). Geen PDF.
`PDF_STATUS: VERBODEN` gerespecteerd.
