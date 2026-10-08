# CCI — INDIA LONELY PLANET GAP-CHECK — RESULT

```
uitgevoerd_door: CCI
uitgevoerd_op: 2026-08-22
input: agent/indialonelyplanet-north-discovery (LONELY_PLANET_NORTH_DISCOVERY.md + .csv, 26 findings)
       agent/indialonelyplanet-ganges-south-discovery (LONELY_PLANET_GANGES_SOUTH_DISCOVERY.md + .csv, 54 findings)
aard: kleine onafhankelijke gap-check, GEEN nieuwe discoverysweep, GEEN A/B/C, GEEN route, GEEN nieuwe
      integratielaag. Geen bestand op de twee bronbranches aangeraakt.
drempel: hoog — max. 15 missers gerapporteerd, 0 is een geldig resultaat.
```

## Uitkomst: 3 evidente missers

Beide documenten zijn ongewoon grondig (80 findings totaal, consistente disposition-schaal,
consequente bronvermelding, expliciete "bewust gescreend"-secties). Bij een strenge "hoe kon je
DIT missen"-toets blijven drie kandidaten over — twee sterk, één gematigd — plus enkele serieus
overwogen kandidaten die NIET de drempel haalden (zie §3, met bewijs waarom).

| # | naam | cluster/corridor | waarom evident gemist | schaal/kwaliteit | omweg | bronbewijs |
|---|---|---|---|---|---|---|
| 1 | **Ganga Aarti, Har Ki Pauri** | Haridwar/Rishikesh (B) | De Varanasi-laag kreeg een eigen `VAR-008`-regel voor "kies één goede Aarti-positie"; Haridwar's eigen, minstens even iconische avondritueel ontbreekt volledig — geen enkele vermelding in het hele North-document, ook niet in de sectie die expliciet checkt of Haridwar "geen tweede grote magneet" heeft. Dit is geen persoonslocatie (geen Top-11-band), dus binnen scope. | Historisch ritueel sinds 1916 (gestart door Pandit Madan Mohan Malviya, georganiseerd door Shri Ganga Sabha); dagelijks grote massa's bezoekers aan beide oevers; door reisbronnen consequent als hét symbool van Haridwar aangeduid. | 0 km — kernpunt van Haridwar zelf, geen omweg. | <https://utsav.gov.in/view-darshan/haridwar-ganga-aarti> · <https://www.euttaranchal.com/tourism/ganga-aarti-haridwar.php> · <https://www.haridwarrishikeshtourism.com/ganga-aarti-haridwar.html> |
| 2 | **ISKCON Krishna-Balaram Mandir** | Vrindavan/Braj | BRAJ-sectie is met 9 regels (BRAJ-001 t/m 009) ongewoon rijk, maar mist juist het gebouw met de grootste internationale bekendheid in Vrindavan zelf — géén Top-11-persoonsband (Prabhupada staat niet op Marks Top-11), dus geen reden voor uitsluiting binnen deze niet-persoonslaag. | Gebouwd 1975; dagelijks grote aantallen bezoekers/pelgrims uit binnen- en buitenland; compleet complex met samadhi-museum, gastenverblijf, archief — een van de bekendste enkele bouwwerken van Vrindavan voor een internationaal publiek. | ~0–2 km binnen Vrindavan, geen praktische omweg. | <https://www.tripadvisor.com/Attraction_Review-g951350-d2646191-Reviews-ISKCON_Vrindavan-Vrindavan_Mathura_District_Uttar_Pradesh.html> · <https://mathuravrindavantourism.co.in/krishna-balaram-mandir-iskcon-vrindavan> |
| 3 | **Bharat Kala Bhavan (BHU-campus museum)** | Varanasi | Gematigde misser: de Varanasi-laag waardeert musea al expliciet (Man Mahal Observatory, VAR-005), maar dit BHU-campusmuseum — 100.000+ objecten, Gupta/Maurya-sculptuur, Mughal/Rajput/Pahari-miniaturen, Banarasi-textiel — ontbreekt volledig, terwijl het qua opzet exact past bij wat elders (Government Museum Mathura, BRAJ-005) al wél is opgenomen. | Sinds 1920; grootschalige, serieuze universitaire collectie; reisbronnen noemen het consequent een "hidden gem"; wisselende presentatiekwaliteit (sommige bezoekers vinden documentatie/uitstalling zwak) — vandaar `MICRO_GEM`-niveau, geen `CLUSTER_MAGNET`. | ~3–5 km binnen Varanasi (BHU-campus), lage extra reistijd. | <https://www.tripadvisor.com/ShowUserReviews-g297685-d478217-r347051531-Bharat_Kala_Bhavan-Varanasi_Varanasi_District_Uttar_Pradesh.html> · <https://wanderlog.com/place/details/148588/bharat-kala-bhavan-museum-bhu-varanasi> |

## Antwoorden op de zes gestelde controlevragen

1. **Mist Haridwar/Rishikesh nog één echt grote magneet?** **JA** — zie misser #1 (Har Ki Pauri
   Ganga Aarti). Dit is onafhankelijk van de rafting-vraag die het document al goed beantwoordt.
2. **Mist Kumaon belangrijke natuur?** **NEE, niet op hoog niveau.** Corbett, Binsar, Sattal,
   Pangot-Kilbury en Nandhaur dekken samen wildlife, bos en panorama al breed. Kausani (bekend
   Himalaya-panorama, "Zwitserland van Kumaon") is overwogen maar niet gerapporteerd: het voegt
   echte extra reisafstand toe als losstaand hillstation-doel en het document dekt panorama al via
   Binsar Zero Point — onvoldoende "hoe kon je dit missen"-gewicht om de drempel te halen.
3. **Mist Varanasi ondanks de rijke lijst nog een evidente ervaring?** **DEELS** — zie misser #3
   (Bharat Kala Bhavan), gematigd niveau. Geen grote ervaringsmisser gevonden: de kern-ervaringslaag
   (dawn-boot, Subah-e-Banaras, gali's, weefatelier, aarti, Sarnath) is al zeer compleet.
4. **Staat Barabar/Nagarjuni terecht als zware Gaya-discovery aangemerkt?** **JA.** India's oudste
   bewaarde rotsarchitectuur (Mauryaans/Ashokaans, met de beroemde Lomas Rishi-grot), sterk
   graniet-/heuvellandschap, `CLUSTER_MAGNET` is gerechtvaardigd — geen bezwaar.
5. **Ontbreekt op de Varanasi–Bodh Gaya-corridor een evidente natuur/erfgoedstop?** **NEE.** Sher
   Shah Suri's Tomb (Sasaram), Tutla Bhawani-waterval en Rohtasgarh Fort (terecht `TOO_FAR`) dekken
   deze corridor al; Chandra Prabha/Rajdari-Devdari is al overwogen en terecht als `TOO_FAR`
   afgewezen (VAR-013). Geen aanvullende evidente stop gevonden.
6. **Kan Mysore/Bengaluru terecht C blijven?** **JA.** De drie gevonden magneten (Mysore Palace,
   Somanathapura, Shravanabelagola) zijn terecht alleen als C-challenger-signaal bewaard, niet als
   statuswijziging. Geen normale Bengaluru-highlight haalt de drempel. Hampi is bewust niet
   meegenomen als kandidaat: het ligt ver buiten Mysore/Bengaluru-geografie en zou de smalle
   C-gap-check-scope van deze taak overschrijden, consistent met hoe het document zelf met
   `TOO_FAR`-items omgaat.

## Overwogen maar bewust NIET gerapporteerd (met reden)

- **Magh Mela, Prayagraj** — overwogen als mogelijke kalendertreffer omdat de South-doc dat patroon
  elders wel toepast (Ramnagar Ramlila, Nag Nathaiya, Lathmar Holi, Karthigai Deepam). Bronnen zijn
  het onderling niet eens over de startdatum 2027: sommige bronnen noemen Makar Sankranti
  (~15 januari 2027), andere expliciet Paush Purnima (**22 januari 2027**) als officiële start — dat
  laatste valt net ná Marks reisvenster (t/m 21 januari 2027). Gegeven deze datumonzekerheid en de
  hoge drempel is dit NIET als evidente misser opgenomen; wel het vermelden waard als iets dat
  ChatGPT/Mark apart zou kunnen laten uitzoeken als de exacte 2027-Snan-kalender ooit nodig is.
- **Neelkanth Mahadev Temple** (bos-berg-tempel bij Rishikesh) — serieus, populair, maar
  functioneel vergelijkbaar met al opgenomen tempel-/natuurlagen elders in het document; haalt de
  "hoe kon je dit missen"-drempel niet apart.
- **Ramnagar Fort & Museum, Varanasi** (los van de al opgenomen Ramnagar Ramlila) — degelijk maar
  tweede-tier vergeleken met wat al is opgenomen; niet gerapporteerd.

## Kwaliteitsindruk van de twee brondocumenten zelf

Geen kritiek op methode nodig. Beide documenten zijn consistent qua schaal, gebruiken dezelfde
disposition-taal, onderbouwen bijna elke regel met minstens één primaire/officiële bron plus
reizigerssignaal, en zijn expliciet transparant over wat bewust is uitgesloten. De 3 hierboven
gerapporteerde missers zijn kleine aanvullingen op een sterk fundament, geen structurele
tekortkoming.

---
Geschreven door: CCI. Geen bestand op de twee bronbranches aangepast, geen A/B/C, geen route, geen
nieuwe integratielaag gebouwd — uitsluitend deze gap-check.
