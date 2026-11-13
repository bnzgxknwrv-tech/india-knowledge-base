# YOGANANDA_V2_PRE_EXTERNAL_FINAL_FREEZE

```
task_id: TOP11-EXTERNAL-AI-BENCHMARK-001
trigger: CCI_TASK 085 (pre-external completion pass)
uitgevoerd_door: CCI
uitgevoerd_op: 2026-08-16
freeze_moment: bij commit van dit bestand (SHA in STATUS.md)
methode: METHOD_V2.md Fase 0-4, gevolgd door deze definitieve freeze. Fase 5-7 (onafhankelijke
  tweede pass, externe multi-AI-union, reconciliatie) volgen NIET in deze taak.
```

## Eerlijkheidsverklaring (ongewijzigd t.o.v. YOGANANDA_V2_FREEZE.md)

Corpus-eerst, niet zoekmachine-eerst. Niet geheugen-blind (CCI schreef eerder zelf `PHASE2_
RESULT.md`/ATL-PY-*); die lijst is in deze en de vorige ronde NIET als discovery-checklist
geraadpleegd. Vergelijking daarmee is Fase C en volgt apart, na deze freeze.

---

## WERKPAKKET A — corpus-coverage, bijgewerkte tabel

| bronfamilie | status | toelichting |
|---|---|---|
| *Autobiography of a Yogi* (Gutenberg #7452, volledige tekst, alle 48 hoofdstukken) | **VOLLEDIG DOORZOCHT, incl. occurrence-context** | Alle 82 India-plaatsen uit `AOAY-FULL-LOCATION-ATLAS-001/PLACE_ATLAS.jsonl` zijn deze ronde stuk voor stuk met hun volledige occurrence-context herlezen (niet alleen de dichtste hoofdstukken zoals in de vorige freeze). Twee fouten in de eerdere AOAY-atlas gevonden en gecorrigeerd (zie hieronder). |
| YSS officiële ashram-/locatie-index (`yssofindia.org/ashrams`) | **DOORZOCHT** | Bevestigt vijf officiële YSS-ashrams (Ranchi, Dakshineswar, Dwarahat, Noida, Chennai) + acht retraites (Igatpuri, Shimla, Pune, Dihika, Puri, Serampore, Telary, Coimbatore). Belangrijk: dit is de HUIDIGE (2026) institutionele voetafdruk van de organisatie, niet automatisch bewijs van Yogananda's eigen persoonlijke aanwezigheid — Noida, Chennai, Igatpuri, Telary, Coimbatore zijn zonder aanvullend bewijs NIET aangenomen als door hemzelf bezocht. |
| YSS "Return to India"-chronologie | **DOORZOCHT (herbevestigd)** | Zie eerdere freeze; ongewijzigd. |
| C. Richard Wright's volledige reisdagboek | **BRON_GEBLOKKEERD, bevestigd bij bron zelf.** | Gerichte zoekactie uitgevoerd: het volledige dagboek is, blijkens meerdere onafhankelijke Yogananda-lineage-bronnen (o.a. `ananda.org/ask/why-is-richard-wrights-travel-diary...-not-published`), NOOIT als geheel gepubliceerd. Alleen de fragmenten die Yogananda zelf in AOAY citeerde (reeds volledig verwerkt, o.a. hoofdstuk 41) zijn publiek. Dit is dus geen falende zoekactie maar een bevestigd, structureel ontoegankelijk archief. |
| EAST-WEST/Inner Culture-tijdschriftarchief (1920s-1940s) | **DEELS TOEGANKELIJK, niet verwerkt.** | Een ongeoCR'de PDF-scan is publiek gevonden (`amanuensis.us/page9.html`) plus een los OCR'de inhoudsopgave-index. De scan zelf is, net als Gurupriya Devi's dagboek, een beeld-PDF zonder doorzoekbare tekst — lezen zou bladzijde-voor-bladzijde visuele inspectie vergen, niet uitgevoerd in deze ronde. `BRON_GEBLOKKEERD/DEELS`, concreet benoemd i.p.v. verzwegen. |
| Gurupriya Devi/Anandamayi-kruisbron | **BRON_GEBLOKKEERD, ongewijzigd** | Zie `YOGANANDA-ANANDAMAYI-PHOTO-LOCATION-001/RESULT.md`; opnieuw geprobeerd noch opgelost deze ronde (buiten scope van de kern-Yogananda-corpora; blokkade blijft technisch, niet inhoudelijk verklaard). |
| Wikipedia (Yogananda, Yogoda Satsanga Mahavidyalaya, Dihika Ashram) | **DOORZOCHT** | Ongewijzigd, secundair. |

## Twee fouten in de eerdere AOAY-locatie-atlas gevonden en gecorrigeerd (bijvangst)

1. **"Dwarka" (AOAY-ATL-020)**: alle vijf occurrences (hoofdstuk 2, 4) bleken bij close-reading
   NIET de bedevaartsstad Dwarka (Gujarat) te zijn, maar **"Dwarka Prasad"**, de zoon van
   Yogananda's huisbaas in Bareilly — een persoonsnaam, later kortweg "Dwarka" genoemd. Naam-
   collision, geen echte plaatsvermelding. Gecorrigeerd in `PLACE_ATLAS.jsonl`.
2. **"Belur" (AOAY-ATL-106)**: al gecorrigeerd in de vorige freeze-ronde (CCI_TASK 084) — de
   Karnataka-tempel, niet Belur Math.

Beide fouten zijn in het bronbestand zelf gecorrigeerd, niet stil verwijderd — de oorspronkelijke
(foutieve) identificatie staat als toelichting in de `notes`-velden.

## Hyderabad / Ellora / Ajanta — definitief opgelost

**YOGANANDA_PERSONALLY_PRESENT = NEE (tekstueel onderbouwd, geen gok).** Alle vier occurrences in
hoofdstuk 41 staan in een aaneengesloten alinea-blok van algemene regionale geschiedenis/
architectuur ("Southern India, rich with historical and archaeological remains..."; "Hyderabad
history is a long, colorful story..."; "The most breath-taking display of architecture...is found
at Hyderabad in the ancient rock-sculptured caves of Ellora and Ajanta..."; "Hyderabad City is
graced by the Osmania University..."). Geen van de vier zinnen gebruikt eerste-persoonstaal ("I/we
visited/saw"), in scherp contrast met de onmiddellijk voorafgaande en volgende alinea's over Mysore
en Bangalore die wél expliciet "I", "we", "my companion and I" gebruiken. Dit is een bewuste
schrijfkeuze van Yogananda (regionale reisbeschrijving versus persoonlijk verslag), geen toevallig
ontbrekend detail. Conclusie: `TIER_AOAY_MENTION_ONLY`, `YOGANANDA_PERSONALLY_PRESENT: NEE`.

## Overige hard geclassificeerde India-plaatsen (aanvullend op de vorige freeze)

| plek | YOGANANDA_PERSONALLY_PRESENT | toelichting |
|---|---|---|
| **Delhi** | **JA — NIEUW gevonden deze ronde** | Hfst. 22: "Years later, I visited my brother-in-law in Delhi. I was overjoyed..." — expliciet eerste-persoonsbezoek, gastheer = zwager Satish Chandra Bose. |
| **Simla** | **JA — NIEUW gevonden deze ronde** | Hfst. 21: "leisurely stop was at Simla, a queenly city..."/"Our party soon left Simla and entrained for Rawalpindi" — bevestigde tussenstop tijdens de Kashmir-reis. |
| **Purulia** | **JA — NIEUW gevonden deze ronde** | Hfst. 46: "in a few hours we shall reach Purulia... our little circle in Purulia" — expliciet, eigen reis. |
| **Naini Tal** | **NEE (poging, niet aangekomen) — verscherpt** | Hfst. 2: "I fled that afternoon toward Naini Tal... Ananta gave determined chase; I was forced to return sadly to Bareilly." Hij probeerde als jongen te ontsnappen naar Naini Tal maar werd onderweg tegengehouden en teruggebracht — GEEN aankomst. Apart van de andere Naini Tal-vermelding (hfst. 32), die niet over Yogananda zelf gaat maar over Lahiri Mahasaya's ambtelijke overplaatsingen. |
| **Danapur, Ranikhet (ch. 32/33/34), Ghurni, Nadia** | **NEE voor Yogananda persoonlijk** | Deze occurrences beschrijven allemaal Lahiri Mahasaya's eigen levensloop/overplaatsingen/geboorteregio, zoals Yogananda die in zijn boek navertelt — niet Yogananda's eigen fysieke aanwezigheid. (Ranikhet/Danapur blijven uiteraard wel geldig als LAHIRI MAHASAYA-punten, al bevestigd in `PHASE2_RESULT.md`.) |
| **Kidderpore** | **NEE voor Yogananda persoonlijk** | Hfst. 36/42: gaat over een discipel die daar woonde en over een (mogelijk nooit doorgegaan) bezoekplan van Sri Yukteswar, niet over Yogananda zelf. |
| **Dehra Dun** | **NEE voor Yogananda persoonlijk** | Hfst. 45: Anandamayi Ma's eigen (toekomstige) hermitage, genoemd tijdens een gesprek op Serampore-station — niet Yogananda's eigen bezoek aan Dehra Dun. |
| **Patna, Rajputana, Kolar, Nasik, Ahmedabad, Poona** | **NEE, bevestigd mention-only** | Historische/economische/bibliografische zijsprongen (Chandragupta-hof; Kumbh Mela-context; Mysore-industrie; vier heilige Mela-steden algemeen; Gandhi-boekuitgever; Kasturba Gandhi's overlijdensplaats) — geen van alle beschrijft Yogananda's eigen aanwezigheid. |
| **Dakshineswar (tempel, hfst. 9/22)** | **JA, sterk** | Twee aparte, uitgebreide persoonlijke bezoeken: eerste pelgrimage met Master Mahasaya (hfst. 9, "the first of many pilgrimages"), en het dramatische visioen-bezoek met zuster Roma en zwager Satish (hfst. 22). Dit is de Ramakrishna Kali-tempel. |
| **Yogoda Math, Dakshineswar (hfst. 28/40, ander adres dan de tempel)** | **NEE/ONBEWEZEN voor persoonlijke aanwezigheid — belangrijke nuance** | Dit is Yogananda's EIGEN, latere hermitage-stichting op de Ganges-oever bij Dakshineswar, "dedicated in 1939" — maar Yogananda keerde na zijn 1935-36-bezoek niet meer fysiek naar India terug (hij overleed in 1952 in de VS). De AOAY-tekst zelf beschrijft de wijding in de derde/verleden tijd, zonder "I attended/I was there". Instellingsstichter ≠ automatisch fysiek aanwezig bij latere wijding — expliciet apart gehouden, niet aangenomen. |

## WERKPAKKET B — sublocaties + hostgraph, uitgebreid

### Zes Mysore/Bangalore-punten verder geverifieerd (van de vorige freeze)

- **Chamundi-tempel**: fysieke identiteit bevestigd als bestaande, actieve, publiek toegankelijke
  tempel op Chamundi Hill, Mysore (algemeen erkende, nog altijd bestaande grote pelgrimsplaats;
  geen aparte adrescontrole nodig gezien de eenduidigheid van de naam). `PHYSICAL_IDENTITY: EXACT`.
- **Krishnaraja Sagar Dam**: bestaande, nog altijd functionerende stuwdam nabij Mysore (KRS Dam/
  Brindavan Gardens); `PHYSICAL_IDENTITY: EXACT`, niet apart heradres-geverifieerd.
- **Yuvaraja's zomerpaleis**: `PHYSICAL_IDENTITY: DEELS` — AOAY noemt geen eigen naam voor dit
  specifieke zomerpaleis (onderscheiden van het hoofdpaleis, Mysore Palace); niet verder opgelost
  deze ronde.
- **Lezingzalen (Town Hall, Maharajah's College, University Medical School, Mysore; National High
  School, Intermediate College, Chetty Town Hall, Bangalore)**: `PHYSICAL_IDENTITY: DEELS` — namen
  bevestigd uit de brontekst zelf, huidige status/bestaan niet apart gecontroleerd deze ronde.
- **C.V. Raman-ontmoeting**: geen apart fysiek adres in AOAY; ontmoeting geplaatst binnen de
  Mysore-context, geen aparte locatie te claimen boven wat al genoteerd is.

### Hostgraph — bijgewerkt met nieuwe vondsten

| gastheer/netwerkpersoon | relatie | locatie |
|---|---|---|
| Satish Chandra Bose (zwager) | gastheer/gezelschap, twee aparte gelegenheden | Dakshineswar-tempel (hfst. 22), Delhi (hfst. 22) |
| Master Mahasaya (discipel van Ramakrishna) | gids/introductie | Dakshineswar-tempel (hfst. 9) |
| Prokash Das | latere directeur Yogoda Math Dakshineswar | Dakshineswar (institutioneel, niet Yogananda's eigen bezoek) |
| Lambadar Dey | gastheer/advocaat | Purulia (hfst. 46) |

Overige hostgraph-entries (Maharaja van Kashimbazar, Yuvaraja/Maharaja van Mysore, Gandhi,
Sri Yukteswar, Anandamayi Ma, C.V. Raman) ongewijzigd t.o.v. de vorige freeze.

## WERKPAKKET C — lossless resultaat

Alle occurrence-niveau brongegevens blijven in `AOAY-FULL-LOCATION-ATLAS-001/RAW_OCCURRENCES.jsonl`
(1.359 records, herbruikt, twee entries gecorrigeerd zoals hierboven) en `PLACE_ATLAS.jsonl` (123
records). Dit bestand voegt de Yogananda-specifieke `YOGANANDA_PERSONALLY_PRESENT`-laag toe die in
het generieke AOAY-atlasbestand ontbrak (dat bestand normaliseert per plaats, niet per persoon).
Geen apart nieuw JSONL-bestand aangemaakt deze ronde — de bovenstaande tabellen zijn de volledige,
voor Yogananda gefilterde laag; een toekomstige machine-leesbare export kan hieruit worden afgeleid
zonder informatieverlies (alle occurrence_ids herleidbaar naar de bronbestanden).

## WERKPAKKET D — definitieve gate-status

| gate | status | onderbouwing |
|---|---|---|
| **CORPUS-COVERAGE-GATE** | **DEELS** | AOAY volledig (alle 48 hoofdstukken, occurrence-niveau); YSS-chronologie + ashram-index doorzocht. Wright-dagboek en EAST-WEST-archief bevestigd `BRON_GEBLOKKEERD`/`DEELS` met concrete, benoemde reden — niet stilzwijgend overgeslagen, maar ook niet opgelost. |
| **HOSTGRAPH-GATE** | **JA voor de gevonden gastheren** | Alle in AOAY genoemde gastheren voor bevestigde Yogananda-aanwezigheid zijn teruggezocht; geen aanwijzing voor systematisch gemiste hostrelaties binnen het doorzochte corpus. |
| **DISCOVERY-GATE** | **DEELS** | Gerichte discovery uitgevoerd voor Wright-dagboek, EAST-WEST-archief, YSS-ashramindex; NIET voor elke individuele lezingzaal/sublocatie-adres. |
| **RECONCILIATIE-GATE** | **N.V.T. in deze taak** | Fase 7 vereist externe/detector-only claims om te reconciliëren; die bestaan nog niet voor Yogananda (dat is precies het doel van de prospectieve control-test). Geen externe claims geraadpleegd of gesimuleerd, conform de stopvoorwaarde. |

**`YOGANANDA_V2_PRE_EXTERNAL_SATURATED: NEE`**

Onderbouwing: twee bronfamilies (Wright's volledige dagboek, EAST-WEST-archief) blijven
structureel ontoegankelijk zonder OCR/handmatige scanpagina-inspectie — een eerlijke, benoemde
hiaat, geen verzwegen gok. `NEE` is hier bewust gekozen boven een schijnbare `JA`, conform de
taakinstructie dat `NEE` toegestaan en beter is dan een valse saturationclaim.

## Onopgeloste bronfamilies/claims — expliciete lijst

1. C. Richard Wright's volledige reisdagboek — structureel nooit gepubliceerd; alleen AOAY-citaten
   beschikbaar (al volledig verwerkt).
2. EAST-WEST/Inner Culture-tijdschriftarchief 1925-1945 — publiek gevonden maar ongeoCR'd; vereist
   bladzijde-voor-bladzijde visuele inspectie, niet uitgevoerd.
3. Gurupriya Devi/Anandamayi-dagboek — ongewijzigd geblokkeerd (gescande PDF).
4. Individuele adresverificatie voor de zes Mysore/Bangalore-lezingzalen en het Yuvaraja-
   zomerpaleis — namen bevestigd, exacte huidige adressen niet.
5. YSS-locatiepagina's voor Noida/Chennai/Igatpuri/Telary/Coimbatore — bestaan institutioneel,
   maar Yogananda's eigen persoonlijke aanwezigheid daar is NIET onderzocht/aangenomen (waarschijnlijk
   grotendeels postuum gesticht, maar dit is zelf niet hard geverifieerd in deze ronde — vermeld
   als open vraag, niet als aanname in beide richtingen).

Geen A/B/C namens Mark. Geen permanente locatie-ID. Geen PDF. Geen route.

---
Geschreven door: CCI. STOP hierna conform CCI_TASK 085 stopvoorwaarde — geen externe Yogananda-
resultaten gezocht, gesimuleerd of vergeleken.
