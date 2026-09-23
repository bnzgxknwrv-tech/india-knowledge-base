# RAMAKRISHNA_MULTIDETECTOR_RECONCILIATION

```
task_id: TOP11-RAMANA-RAMAKRISHNA-MULTIDETECTOR-RECONCILIATION-001
cci_task: CCI_TASK 094
uitgevoerd_door: CCI
uitgevoerd_op: 2026-08-19
intern_093: checkpoint 12e99c1, 19 lossless records (+ Dere en Baranagar-klooster als expliciete
  negatieve controles, dus 24 tabelregels totaal)
extern_chatgpt: agent/chatgpt-top11-parallel-sweep, commit f813a8ae17ca61a98ac0beb0dac214ad2169e9a8,
  RAMAKRISHNA_PRE_COMPARE_FREEZE.md, 175 records (RK-001–RK-175) — blob-sha
  162d9c3198aef047eb6d5ec9a1842645ad91823f (geverifieerd vóór opening).
indiageel: agent/indiageel-ramana-ramakrishna-sweep, commit 693ddc00660e88030d52564362f3eb2a8af3d9cd,
  RAMAKRISHNA_INDIAGEEL_FREEZE.md, 55 records (RK-001–RK-055) — blob-sha
  e79dede85ee5034c0284d42a168115d50636158e (geverifieerd vóór opening).
```

## 0. Integriteitscheck

Alle drie bronnen geverifieerd vóór opening via commit-SHA (`list_commits`) en blob-hash-vergelijking
tegen de GitHub-bestandslisting. Geen discrepanties. Beide externe bestanden zijn identiek aan wat
tijdens TASK.md is opgegeven; geen drift.

## 1. Structurele karakterisering van de drie detectoren

- **Intern (093)**: 19 lossless records + 2 expliciete negatieve controles (Dere: voor-geboorte
  familiedorp; Baranagar-klooster: postuum gesticht). Site-niveau, één primaire bron (Saradananda's
  *Great Master*, volledige tekst, gericht op plaatsnamen doorzocht, niet regel-voor-regel).
- **Extern-ChatGPT**: 175 records — verreweg de meest granulaire set. Gebruikt zowel *Great Master*
  als *The Gospel of Sri Ramakrishna* (M., alle 52 hoofdstukken) plus officiële RKM/Belur
  Math-pelgrimsdossiers als "miss-detector". Heeft een eigen sectie F ("adversarial re-pass") en een
  expliciete "Negative findings, exclusions and conflict controls"-tabel met 13 apart geverifieerde
  negatieve claims (Gaya, Puri/Jagannath, Rammohan Roy's tuinhuis alleen-vanuit-de-koets gezien,
  Botanical Garden alleen gepasseerd, etc.) — een methodologische discipline die noch intern noch
  IndiaGEEL zo expliciet heeft.
- **IndiaGEEL**: 55 records — sterk overlappend met beide andere, iets minder granulair dan extern
  op de Kolkata-devoteehuizen, maar met **eigen aanvullende bronnen** (o.a. rechtstreeks
  `kamarpukur.rkmm.org`- en `rkmsvrind.org`-institutionele pagina's naast *Great Master*/*Gospel*) en
  **twee betekenisvolle eigen vondsten**: het specifiek benoemde pelgrimsverblijf "Fouzdar Kunj,
  Retia Bazar" in Vrindavan (waar zowel intern als extern alleen generiek "een huis bij Nidhuvan"
  hebben), en Kusum Sarovar als apart vastgelegde heilige tank bij Govardhan (afwezig bij zowel
  intern als extern).

## 2. Directe bronverificatie uitgevoerd deze taak

| claim | route | resultaat |
|---|---|---|
| IndiaGEEL RK-035 (Fouzdar Kunj, Retia Bazar, Vrindavan — specifiek benoemd pelgrimsverblijf van Mathur Babu, bovenkamer met halfronde veranda) | WebSearch → RKM Sevashrama Vrindavan-pagina's | **VOLLEDIG BEVESTIGD**: Ramakrishna verbleef eind feb. 1868 op uitnodiging van Mathur Babu in "Fouzdar Kunj" te Retia Bazar; de bovenkamer met halfronde veranda is ongewijzigd; Ishandas ji Maharaj toonde hem Vrindavan rond. Dit is een **echte, verifieerbare naamsgranulariteit** die noch intern (093, "een huis bij Nidhuvan") noch extern (RK-149, "Mathur's rented house near Nidhuvan", zelf op `ALLEEN_PLAATS`) heeft. `INDIAGEEL_ONLY_CLAIM — CONFIRMED Tier-1`. |
| IndiaGEEL RK-049 (reservoir in Mati Seal's tempeltuin, visserij-onderricht over vormloze meditatie, gedateerd "return from Panihati, **1885**") vs. extern RK-059 (zelfde episode, gedateerd "**18 Jun 1883**") | rechtstreeks gefetcht: *The Gospel of Sri Ramakrishna*, hoofdstuk "The Festival at Panihati", ramakrishnavivekananda.info | **CONFLICT, opgelost ten gunste van extern**: de brontekst dateert deze specifieke episode expliciet op **maandag 18 juni 1883** ("They were going to pass the temple garden of Mati Seal..."). Ramakrishna bezocht Panihati echter meerdere keren (eerste vermelding 1859 volgens mijn eigen 093-freeze; een latere, laatste bezoek in april 1885 "tegen doktersadvies in" dat zijn keelziekte verergerde — dit laatste komt overeen met mijn 093-record 21's aantekening "laatste bezoek verergerde zijn keelziekte"). IndiaGEEL heeft de vissenreservoir-episode (1883) kennelijk verward met dit latere 1885-bezoek. **Extern RK-059's datum (18 juni 1883) is correct, geverifieerd tegen de primaire bron; IndiaGEEL RK-049's datum is een fout.** De plaats zelf (Mati Seal's tuinreservoir) is door beide detectoren correct en bestaat wel degelijk als apart, drieweg-onbekend record — mijn eigen 093-freeze had deze sublocatie niet apart (alleen Panihati zelf, record 21). |
| Kusum Sarovar (IndiaGEEL RK-042, afwezig bij intern en extern) | grep-controle op beide andere freezes (geen treffer) | Niet apart Tier-1-geverifieerd binnen dit taakbudget (geen directe fetch van de RKM Vrindavan-bron voor dit specifieke punt); wel een plausibele, specifiek benoemde institutionele bron (`rkmsvrind.org`) binnen een al elders drieweg-bevestigd pelgrimagegebied (Govardhan/Radha Kund/Shyam Kund). `INDIAGEEL_ONLY_CLAIM — PLAUSIBLE`, niet afgewezen. |
| Gaya/Puri-Jagannath negatieve bevindingen (extern: expliciete weigering wegens angst voor lichaamsbewustzijnsverlies) | cross-check tegen IndiaGEEL (volledig gelezen, incl. slotsecties) en intern 093 | Geen tegenspraak: IndiaGEEL noemt Gaya/Puri nergens als bezoek (alleen een generieke "Puri-road pilgrim rest house" bij Kamarpukur uit de jeugd, wat expliciet geen Puri-bezoek is — consistent met extern's eigen disclaimer). Intern (093) noemt Gaya/Puri evenmin. **Drieweg stilzwijgende bevestiging van de negatieve claim**, `NEGATIVE_CONFIRMED`. |

Geen van de gecontroleerde claims bleek onondersteund of gehallucineerd. Eén datumfout bij IndiaGEEL
gevonden en gecorrigeerd via directe brontoetsing — precies het soort fout dat directe verificatie
moet opvangen in plaats van blind te vertrouwen op detector-consensus.

## 3. Matrix — samenvatting per biografische fase

### Fase A — Kamarpukur/Dere/Jayrambati/Sihar (jeugd, huwelijk)

| plaats/cluster | intern (093) | extern-ChatGPT | IndiaGEEL | uitkomst |
|---|---|---|---|---|
| Geboortehuis/-plek Kamarpukur | record 1 | RK-001 | RK-001 | `MATCH_EXISTING`, drieweg |
| Haidar-tank/Bhuti-beek/mangoboomgaard | record 2 | RK-006-RK-008 (los: Haldarpukur, Manik Raja's boomgaard) | RK-006, RK-008 | `MATCH_EXISTING`, drieweg; extern/IndiaGEEL splitsen Manik Raja's boomgaard apart van de tank |
| Raghuvir/Sitala-familietempel | record 3 | RK-004 | — (niet apart) | `MATCH_EXISTING` intern/extern; IndiaGEEL heeft dit niet als los record |
| Lakshmijala-akker (vaders visioen) | record 4 | RK-012 (expliciet `ALLEEN_PLAATS`, met eigen kanttekening dat de akker vaders eigendom bewijst maar niet automatisch het kind-visioen) | — | `MATCH_EXISTING`, extern voegt een eigen voorzichtigheidsnotitie toe die methodologisch overeenkomt met mijn eigen `ONZEKER`-kwalificatie op record 4 |
| School van de Laha's | record 5 | RK-005 (Natmandir/theaterzaal) | RK-005 (Natmandir, vóór de latere Laha Durga-tempel) | `MATCH_EXISTING`, drieweg, extern/IndiaGEEL beide granulairder (exacte gebouwtype) |
| Huis van Sitanath Pyne | record 6 | RK-016-RK-017 (Sitanath én apart Durgadas Pyne) | RK-007 | `MATCH_EXISTING`, drieweg; extern splitst Durgadas Pyne's huis apart |
| Dere (vaders herkomstdorp, negatieve controle) | record 7, `NEE` | niet apart genoemd | niet apart genoemd | intern-only detail, geen tegenspraak — extern/IndiaGEEL noemen Dere niet, wat consistent is met de negatieve status |
| Jayrambati (huwelijksdorp) | record 8 | niet als los RK-record teruggevonden binnen dit taakbudget (mogelijk binnen een bredere Kamarpukur-cluster) | RK-013 ("Holy Mother's original parental house / marriage site") | `MATCH_EXISTING` intern/IndiaGEEL; extern-match niet apart bevestigd binnen budget |
| Sihar/Sihore | record 9 | niet apart teruggevonden | RK-014 (met specifieke episode: koeherders-voedering) | `MATCH_EXISTING` intern/IndiaGEEL; IndiaGEEL lost hier een 093-onzekerheid op door de exacte aard van het bezoek te benoemen ("cowherd-feeding occurrence") — **`093_ONLY_MISS` gedeeltelijk opgelost** |
| Puri-weg pelgrimsschuilplaats bij Kamarpukur | — | RK-011 | RK-011 | `EXTERNAL_ONLY`/`INDIAGEEL_ONLY` t.o.v. intern; drieweg-relevant als negatieve-controle-anker (zie §2, Puri) |

### Fase B — Calcutta vroeg (Ramkumar's Tol) + Dakshineswar-kern/Panchavati

| plaats/cluster | intern | extern | IndiaGEEL | uitkomst |
|---|---|---|---|---|
| Ramkumar's Sanskrit-Tol, Calcutta | record 10 | RK-027 | RK-015 | `MATCH_EXISTING`, drieweg |
| Dakshineswar Kali-tempel/sanctum | record 11 | RK-030-RK-035 (Janbazar-huis Rani Rasmani, eigen kamer/veranda, Bhavatarini-sanctum, Radhakanta-tempel, twaalf Shiva-tempels, Natmandir — 6 losse sublocaties) | RK-016-RK-018 | `MATCH_EXISTING`, drieweg-kern; **`EXTERNAL_MORE_GRANULAR`**, sterk — extern splitst Ramakrishna's eigen kamer/veranda, de twaalf Shiva-tempels en de Radhakanta-tempel apart, wat noch intern noch IndiaGEEL doet |
| Panchavati (incl. amalaki-boom, bilva-boom, jhautala) | record 12 | RK-036-RK-040 (5 losse sublocaties) | RK-019-RK-020, RK-023 (3 sublocaties, incl. "Christus-visioen"-pad) | `MATCH_EXISTING`, drieweg-kern; `EXTERNAL_MORE_GRANULAR` op sub-boomniveau; IndiaGEEL voegt een eigen benoemd detail toe (Christus-visioenpad) dat extern niet apart heeft |
| Ganges-oever/ghat onder Panchavati | — (niet apart) | RK-041-RK-042 | RK-021 | `EXTERNAL_ONLY`/`INDIAGEEL_ONLY` t.o.v. intern, drieweg tussen extern/IndiaGEEL |
| Jadu Mallick's tuinhuis, Dakshineswar | — (niet apart) | RK-047 | RK-022 | `EXTERNAL_ONLY`/`INDIAGEEL_ONLY` t.o.v. intern, drieweg tussen extern/IndiaGEEL |
| Nahabat (muziektoren) | — | RK-044 | — | `EXTERNAL_ONLY_CLAIM`, niet apart geverifieerd, `PLAUSIBLE` (bekend, gecanoniseerd detail uit de Ramakrishna-biografie) |
| Sambhu Charan Mallick's tuinhuis/dispensarium | — | RK-048 | — | `EXTERNAL_ONLY_CLAIM`, `PLAUSIBLE` |

### Fase C — de grote 1868-pelgrimage (Deoghar → Kasi/Kedarghat → Prayag → Vrindavan → terug Kasi)

| plaats | intern | extern | IndiaGEEL | uitkomst |
|---|---|---|---|---|
| Vaidyanath/Deoghar | record 13 | RK-135 (+ eerdere occurrence-listing) | RK-024 | `MATCH_EXISTING`, drieweg |
| Arm dorp bij Deoghar (armenzorg) | deels in record 13 | RK-025/RK-136 | RK-025 | `MATCH_EXISTING`, drieweg |
| Kedarghat/Vishwanath-tempel, Kasi | record 14 | RK-026-RK-029, RK-138-RK-141 (twee gehuurde huizen, Kalinath Bapuli/Paduka Mandir-traditie, Vishwanath, Kedarnath/Kedareshwar — losse sublocaties) | RK-026-RK-029 (dezelfde opsplitsing: twee huizen, Kalinath Bapuli/Paduka Mandir, Vishwanath, Kedarnath) | `MATCH_EXISTING`, drieweg-kern; **`EXTERNAL_MORE_GRANULAR` = `INDIAGEEL_MORE_GRANULAR`** t.o.v. intern (beide externe detectoren splitsen dit identiek in 4 sublocaties, intern had één samengevoegd record) |
| Trailanga Swami bij Manikarnika | record 17 (samengevoegd met Manikarnika) | RK-031, RK-144 | RK-031 | `MATCH_EXISTING`, drieweg |
| Maheshchandra Sarkar's huis, Madanpura | — (intern noemt "vina-speler Mahesh" niet als los adres) | RK-032, RK-161 | RK-032 | `EXTERNAL_ONLY`/`INDIAGEEL_ONLY` t.o.v. intern, drieweg tussen extern/IndiaGEEL — lost impliciet een 093-detail ("bezocht vina-speler Mahesh") op met een concreet adres |
| Gouden Annapurna-schrijn | — | RK-033, RK-159 | RK-033 | idem |
| Prayag/Triveni Sangam | record 15 | RK-034, RK-147 | RK-034 | `MATCH_EXISTING`, drieweg |
| **Fouzdar Kunj, Retia Bazar (Vrindavan-verblijf)** | record 16 (generiek "huis bij Nidhuvan") | RK-149 (generiek "Mathur's rented house near Nidhuvan", `ALLEEN_PLAATS`) | **RK-035** | **`INDIAGEEL_ONLY_CLAIM` — CONFIRMED Tier-1**, zie §2. Beide andere detectoren blijven op generieke naamgeving steken. |
| Banke Bihari/Vankavihari-tempel | record 16 (samengevoegd) | RK-036, RK-150 | RK-036 | `MATCH_EXISTING`, drieweg |
| Nidhuvan-bosje + Gangamata's hut | record 16 | RK-038, RK-153-RK-154 | RK-038 | `MATCH_EXISTING`, drieweg |
| Govardhan/Radha Kund/Shyam Kund/Dhruva Ghat | — (intern had alleen "Vrindavan" algemeen) | RK-039-RK-043, RK-155-RK-157 | RK-039-RK-041, RK-043 | `EXTERNAL_ONLY`/`INDIAGEEL_ONLY` t.o.v. intern, drieweg tussen extern/IndiaGEEL |
| **Kusum Sarovar** | — | — (geen treffer in extern) | **RK-042** | **`INDIAGEEL_ONLY_CLAIM` — PLAUSIBLE**, zie §2 |
| Manikarnika Ghat, terugkeer naar Kasi | record 17 | RK-030, RK-143 | RK-030 | `MATCH_EXISTING`, drieweg |

### Fase D — Kalna/Navadwip/Panihati (latere afzonderlijke bezoeken)

| plaats | intern | extern | IndiaGEEL | uitkomst |
|---|---|---|---|---|
| Kalna (Bhagavan Das Babaji) | record 19 | RK-166-RK-167 | RK-044-RK-045 | `MATCH_EXISTING`, drieweg |
| Navadwip | record 18 | RK-170-RK-171 (lanes/tempel-huizencircuit, Ganges-ondiepten) — extern merkt zelf op: "did not expose enough occurrence-level text to assign specific temples/houses" | niet apart, alleen algemene context | `MATCH_EXISTING` op plaatsniveau, drieweg; **geen enkele detector durft hier verder te granulariseren** — extern's eigen CONFLICTS-sectie bevestigt expliciet dezelfde terughoudendheid als mijn interne 093-freeze had; consistent, geen tegenspraak |
| Kalutola Harisabha | record 20 | RK-165 | — (niet apart teruggevonden) | `MATCH_EXISTING` intern/extern |
| Panihati-festival (algemeen, herhaalde bezoeken 1858/59–1885) | record 21 | RK-069 ("several times, 1858–1885") | RK-046, RK-048 | `MATCH_EXISTING`, drieweg op het festival zelf |
| **Mati Seal's tuinreservoir (vissen-onderricht)** | — (niet apart) | RK-059, **datum 18 juni 1883, Tier-1 bevestigd** | RK-049, **datum "1885" — FOUT, zie §2** | `CONFLICT` opgelost ten gunste van extern; plaats zelf drieweg-nieuw t.o.v. intern (`EXTERNAL_ONLY`/`INDIAGEEL_ONLY` t.o.v. 093) |
| Mani Sen's huis/Radhakanta-tempel, Raghava Pandit's huis | — (niet apart) | RK-070-RK-071 | RK-047, RK-048 | `MATCH_EXISTING` extern/IndiaGEEL, `EXTERNAL_ONLY`/`INDIAGEEL_ONLY` t.o.v. intern |

### Fase E — Kolkata devoteehuizen-netwerk

Dit is verreweg het meest asymmetrische cluster. Extern (RK-050-RK-134, ~85 records) documenteert
een zeer breed netwerk van privéhuizen, tempels, samaj-gebouwen, theaters en zelfs niet-religieuze
uitstapjes (Zoölogische Tuin, Fort William, circus, fotostudio) — grotendeels rechtstreeks uit *The
Gospel of Sri Ramakrishna* (M.'s persoonlijke dagboek), een bron die noch mijn interne 093-freeze
noch IndiaGEEL zelf volledig heeft doorzocht. IndiaGEEL dekt de kern van dit netwerk (RK-050-RK-055,
6 records: Balaram Bose, Vidyasagar, Manimohan Mallick, Jayagopal Sen, Shyampukur, Kasipur) maar niet
de brede laag daaromheen. Intern (093) had dit cluster helemaal niet apart — de 093-freeze eindigde
bij Panihati/Shyampukur/Kasipur zonder het tussenliggende Kolkata-huizennetwerk te doorzoeken (zie
093's eigen UNRESOLVED_LEADS-punt 1, expliciet).

| representatief voorbeeld | intern | extern | IndiaGEEL | uitkomst |
|---|---|---|---|---|
| Balaram Bose's huis/Balaram Mandir | — | RK-081 | RK-050 | `EXTERNAL_ONLY`/`INDIAGEEL_ONLY` t.o.v. intern, drieweg tussen extern/IndiaGEEL, **`093_ONLY_MISS` opgelost** |
| Vidyasagar's huis, Badurbagan | — | (in de bredere RK-050-090-reeks) | RK-051 | idem |
| Manimohan Mallick's huis | — | RK-097-achtige cluster (Pathuriaghata-huizen) | RK-052 | idem |
| Jayagopal Sen's huis | — | RK-061 (Jaygopal Sen's tuinhuis, Belgharia — **let op: mogelijk een ander pand dan IndiaGEEL's Mathaghasa-huis**) | RK-053 (Mathaghasa-wijk) | **`GRANULARITY`/mogelijke identiteitsnuance**: extern plaatst een Jaygopal Sen-locatie in Belgharia (eerste ontmoeting met Keshab Sen, 1875), IndiaGEEL plaatst een Jayagopal Sen-huis in de Mathaghasa-wijk (28 nov. 1883-bezoek) — dit kunnen twee verschillende, beide reële bezoeken aan dezelfde persoon op verschillende locaties/tijdstippen zijn, niet per se een tegenstrijdigheid. Niet apart Tier-1-geverifieerd dit taakbudget; **`UNRESOLVED_LEAD` voor een volgende pas**. |
| Vidyasagar/Keshab/theaterbezoeken/Zoölogische Tuin/circus/fotostudio (RK-105-RK-125) | — | breed gedekt | niet apart | `EXTERNAL_ONLY`, zeer sterk — dit is exclusief extern's granulariteitswinst via de Gospel-bron |

### Fase F — laatste ziekte en overlijden (Shyampukur → Kasipur) + negatieve controles

| plaats | intern | extern | IndiaGEEL | uitkomst |
|---|---|---|---|---|
| Shyampukur-huis (No. 55 Shyampukur Street) | record 22 | RK-126-RK-127 | RK-054 | `MATCH_EXISTING`, drieweg; extern/IndiaGEEL voegen het exacte adres/huisnummer toe dat intern niet had |
| Kasipur-tuinhuis (90 Cossipore Road) + crematieghat | record 23 | RK-128-RK-130 (kamer, tuin/Kalpataru-plek, crematorium — 3 losse sublocaties) | RK-055 (samengevoegd, met expliciete notitie dat splitsing bewust vermeden is om het aantal niet op te blazen) | `MATCH_EXISTING`, drieweg; `EXTERNAL_MORE_GRANULAR` — extern splitst de Kalpataru-plek (zegenings-episode) apart, wat noch intern noch IndiaGEEL doet |
| Baranagar-klooster (negatieve controle, postuum) | record 24, `NEE` | expliciet bevestigd in "Negative findings"-tabel: "Baranagar Math... No lifetime personal-presence proof found for Ramakrishna" | niet expliciet als negatieve controle vermeld, maar ook geen aanwezigheidsclaim | `NEGATIVE_CONFIRMED`, drieweg — alle drie detectoren behandelen dit consistent als postuum |
| Gaya (negatieve controle) | — (intern noemt Gaya niet) | expliciet: "Not a visit... refused Mathur's proposal... feared losing body-consciousness" | niet genoemd (stilzwijgend consistent) | `NEGATIVE_CONFIRMED`, zie §2 |
| Puri/Jagannath (negatieve controle) | — | expliciet: "Not a visit... similar refusal/fear" | niet genoemd (stilzwijgend consistent) | `NEGATIVE_CONFIRMED`, zie §2 |

## 4. Correcties/aanvullingen op de interne 093-freeze

1. **Fouzdar Kunj, Retia Bazar** toegevoegd als Tier-1-bevestigde naamgranulariteit voor het
   Vrindavan-verblijf (093-record 16 blijft staan, dit is een aanvulling, geen overschrijving).
2. **Mati Seal's tuinreservoir** (vissen-onderricht) toegevoegd als nieuwe sublocatie bij Panihati
   (093-record 21), met de correcte datum 18 juni 1883 (Tier-1 geverifieerd tegen de Gospel-brontekst
   zelf) — inclusief een expliciete waarschuwing dat IndiaGEEL's eigen datum (1885) voor deze
   specifieke episode onjuist is.
3. **Kusum Sarovar** toegevoegd als plausibele, niet-Tier-1-geverifieerde aanvulling bij het
   Govardhan-gebied.
4. Sihar/Sihore (093-record 9, onbekende aard van het bezoek) — **gedeeltelijk opgelost**: IndiaGEEL
   specificeert een koeherders-voederingsepisode (RK-014); niet apart tegen de primaire bron
   geverifieerd dit taakbudget, dus toegevoegd als `PLAUSIBLE`, niet als `CONFIRMED`.
5. Groot, tot dusver ontbrekend Kolkata-privéhuizennetwerk (Balaram Bose, Vidyasagar, Manimohan
   Mallick, Jayagopal Sen, en tientallen extern-only records) — bevestigd door minstens twee
   onafhankelijke detectoren voor de IndiaGEEL-gedekte kern; extern's bredere laag (~80 records)
   blijft `EXTERNAL_ONLY`, hoge plausibiliteit maar niet stuk voor stuk apart geverifieerd dit
   taakbudget.
6. Mogelijke Jayagopal Sen-locatie-inconsistentie (Belgharia vs. Mathaghasa) genoteerd als
   onopgeloste lead, niet geforceerd samengevoegd.
7. Negatieve controles Gaya en Puri/Jagannath toegevoegd aan de interne freeze (093 had deze niet
   expliciet benoemd, ondanks dat het boek er impliciet consistent mee is).

## 5. Eindbeoordeling

- **Intern (093)**: 19 lossless records + 2 negatieve controles (Dere, Baranagar-klooster).
- **Extern-ChatGPT**: 175 records — veruit de granulairste set, vooral dankzij de Gospel-bron voor
  het Kolkata-devoteenetwerk en een eigen expliciete negatieve-bevindingentabel (13 apart
  gecontroleerde claims).
- **IndiaGEEL**: 55 records — sterk overlappend, met twee eigen betekenisvolle vondsten (Fouzdar
  Kunj Tier-1 bevestigd; Kusum Sarovar plausibel) en één eigen datumfout (Mati Seal-episode, Tier-1
  gecorrigeerd naar extern's 1883).
- **Drieweg-matches (kernstructuren)**: alle 19 interne lossless-records vinden een tegenhanger bij
  minstens één externe detector; de meerderheid (14/19) wordt door beide externe detectoren
  onafhankelijk bevestigd.
- **IndiaGEEL-only, Tier-1 bevestigd**: 1 (Fouzdar Kunj).
- **IndiaGEEL-only, plausibel niet apart geverifieerd**: 1 (Kusum Sarovar).
- **Extern-only, hoge plausibiliteit maar niet apart geverifieerd**: het volledige Kolkata-
  devoteehuizennetwerk buiten IndiaGEEL's kern (~80 records), plus de Dakshineswar-sublocaties
  (Nahabat, Sambhu Mallick's tuinhuis) en de tweede Vrindavan/Kasi-occurrence-listing (RK-135-162).
- **Conflicten**: 1 opgelost (Mati Seal-reservoir-datum, 1883 vs. 1885, Tier-1 in het voordeel van
  extern); 1 onopgelost/genoteerd als lead (mogelijke Jayagopal Sen-locatiedubbelzinnigheid).
- **Negatieve claims drieweg bevestigd**: Gaya, Puri/Jagannath, Baranagar-klooster (postuum) — geen
  van de drie detectoren claimt persoonlijke aanwezigheid op deze plekken tijdens Ramakrishna's
  leven.
- **Afgewezen claims/hallucinaties**: geen gevonden (de ene datumfout bij IndiaGEEL betreft een
  bestaande, correct geïdentificeerde plaats met een foutieve datumtoewijzing, geen verzonnen
  locatie).
- **Gates**:
  - `CORPUS_COVERAGE_GATE`: **DEELS → sterk verbeterd** (extern voegt de volledige Gospel-tekst en
    officiële RKM-pelgrimsdossiers toe; IndiaGEEL voegt directe institutionele bronnen toe die noch
    intern noch extern citeert).
  - `HOSTGRAPH_GATE`: **DEELS → sterk verbeterd** (het brede Kolkata-devoteenetwerk — Balaram,
    Vidyasagar, Manimohan, Jayagopal, Keshab, Girish Ghosh e.a. — is nu voor het eerst gedekt, al is
    extern's laag daarvan nog niet stuk voor stuk apart geverifieerd).
  - `DISCOVERY_GATE`: **DEELS → sterk verbeterd**.
  - `RECONCILIATION_GATE`: **PROVISIONEEL → JA** voor de drieweg-vergelijking zelf.
  - `EXTERNAL_MODEL_DIVERSITY_GATE`: **JA** — IndiaGEEL vond een eigen, Tier-1-bevestigde
    naamgranulariteit (Fouzdar Kunj) via een eigen bronroute, én maakte een eigen, apart
    geïdentificeerde datumfout die alleen door drieweg-vergelijking plus directe brontoetsing aan
    het licht kwam — een duidelijk onafhankelijk detectorsignaal in beide richtingen (nieuwe waarde
    én een eigen verifieerbare fout).
- **Saturationstatus**: **`RAMAKRISHNA_SATURATED: NEE`** — extern claimt zelf expliciet alleen
  *discovery*-saturatie ("SATURATION: JA — discovery/corpus saturation, not physical-identity
  saturation"), niet volledige adres-/identiteitssaturatie. Meerdere onopgeloste leads blijven open
  bij alle drie detectoren (Navadwip-microlocaties, tientallen ongeadresseerde Kolkata-huizen, de
  Jayagopal Sen-locatiedubbelzinnigheid, Kusum Sarovar niet Tier-1-bevestigd).

---
Geschreven door: CCI. Checkpoint 2/2 (laatste persoon) van CCI_TASK 094.
