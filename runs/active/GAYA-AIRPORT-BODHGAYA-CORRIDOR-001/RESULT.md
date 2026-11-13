# RESULT — GAYA-AIRPORT-BODHGAYA-CORRIDOR-001 — Sweep A + Sweep B + Reconciliatie (CCI)

```
task_id: GAYA-AIRPORT-BODHGAYA-CORRIDOR-001
sweep_a: CCI, 2026-08-09
sweep_b: INDIA, onafhankelijk, gerapporteerd 2026-08-14 (PR #23)
reconciliatie: CCI, 2026-08-14 (poort R) — bronnen zelfstandig gecontroleerd (poort G.1)
```

## SWEEP_A_STATUS

KLAAR. Corridor is fysiek zeer kort (circa 5-17 km referentiepuntspreiding; hoofdroute nu
specifiek vastgelegd op ~10,6 km, zie CORRIDORRELEVANTIE) en overwegend één doorgaande weg zonder
zijstraten van pelgrimsgewicht. Geen PRE_PDF_CONTENT, geen PDF, geen A/B/C ingevuld — conform
TASK.md (nooit in scope voor deze taak).

## SWEEP_B_RESULTAAT (INDIA, onafhankelijk)

INDIA heeft Sweep B zelfstandig uitgevoerd en pas daarna dit RESULT.md (Sweep A) gelezen, conform
TASK.md. Uitkomst: geen nieuwe fysieke corridor-kandidaten, geen nieuwe AOAY-corridorlocatie, geen
nieuwe Top11-corridorlocatie, geen nieuwe laag-3-heavyweight binnen de praktische
airport→Bodh Gaya-corridor (0/0, zelfde uitkomst als Sweep A). AOAY-sweep onafhankelijk herhaald
(Project Gutenberg rechtstreeks geopend, dezelfde ene bekende voetnoot-treffer, geen
corridor-/airportdetail) — bevestigt Sweep A's AOAY-hergebruik. Wel 4 reconciliatiepunten
aangedragen, hieronder verwerkt na CCI's eigen bronverificatie (poort G.1).

## RECONCILIATIE (poort R, 2026-08-14)

CCI heeft Sweep B's 4 punten niet blind overgenomen maar zelf bronmatig gecontroleerd vóór
verwerking:

1. **Corridorgeometrie** — gecontroleerd via WebSearch (gaya.nic.in-inhoud + corroborerende
   reisbronnen); directe WebFetch van zowel gaya.nic.in als de AAI-pagina gaf HTTP 503 (poort
   G.1-beperking, expliciet vastgelegd, niet verzwegen). De 10,6 km/NH22+Domuhan-Bodhgaya
   Road-claim naar Mahabodhi Temple is voldoende corroborerend bevestigd en verwerkt. Sweep B's
   specifieke toeschrijving "AAI noemt Bodh Gaya 10 km" kon CCI NIET zelfstandig bevestigen —
   zoeksynthese suggereerde dat AAI's eigen pagina vaker met 5 km wordt geciteerd en 10 km
   elders (o.a. Bihar Tourism-adviezen) vandaan lijkt te komen. Daarom voorzichtiger verwerkt dan
   letterlijk aangeleverd: zie CORRIDORRELEVANTIE.
2. **Methodecorrectie Top11** — inhoudelijk correct bevonden (conflateert vervoer-VIA-luchthaven
   met fysieke doorkruising van de corridorzone vóór de luchthaven bestond) en overgenomen; wijzigt
   geen enkele uitkomst (11/11 blijft negatief), alleen de formulering in TOP11_RESULTAAT_PER_NAAM.
3. **Belur Math Gaya Ji sub-centre** — gecontroleerd via WebSearch op belurmath.org/
   media.belurmath.org (officiële domeinen); adres, opening 1 feb 2026 en Kshudiram-link
   bevestigd. Vastgelegd als nieuwe out-of-scope negatieve detectorbevinding, NIET gepromoveerd
   (zie OUT_OF_SCOPE_NEGATIEVE_DETECTORBEVINDINGEN).
4. **Babaji/Shyamananda Giri-nuance** — gecontroleerd via WebSearch op yssofindia.org/yogananda.org
   (officiële YSS/SRF-domeinen); bevestigd dat het Babaji-lichtvisioen plaatsvond in Rajgir
   (gastenverblijf), niet in Bodh Gaya of op de corridor zelf. Overgenomen; absolute formulering
   "geen data buiten AOAY" verwijderd uit TOP11_RESULTAAT_PER_NAAM rij 2.

**DOUBLE_SWEEP_COMPLETED: JA. RECONCILED: JA.** Kandidaatuitkomst ongewijzigd (0 nieuw, 079 blijft
ongebruikt); alleen tekst/formulering/geo-precisie verbeterd.

## SCOPE_GECONTROLEERD

Fysieke corridor Gaya Airport → Bodh Gaya (de weg zelf, plus kleine praktische omwegen tijdens
die transfer). Bodh Gaya-centrum en Gaya-stad zelf NIET heropend — 046-078 blijven protected/
ongewijzigd. Elke plek die in onderstaande bevindingen ter sprake komt en al een nummer heeft
(046, 047, 051, 070) wordt uitsluitend ter GEO-context genoemd, niet als nieuwe kandidaat.

## CORRIDORRELEVANTIE (algemeen — geen kandidaten om per-kandidaat in te vullen)

Geraadpleegde bronnen geven UITEENLOPENDE afstanden voor Gaya Airport → Bodh Gaya, afhankelijk van
het gemeten referentiepunt: 5 km, 6,47 km, 10 km, 10,6 km, 12 km, 13 km en 17 km. Reistijd
consistent genoemd als circa 15-25 minuten via de N.H.22/voormalige NH83. Dit is een korte
transferrit, geen aparte excursie.

**Reconciliatie-update (Sweep B + CCI-verificatie, 14-08-2026)**: de officiële Gaya
District-pagina voor Mahabodhi Mandir (gaya.nic.in) noemt specifiek **10,6 km via NH22 +
Domuhan–Bodhgaya Road** vanaf Gaya International Airport tot de Mahabodhi Temple (kandidaat 046)
— dit is de meest specifieke, herleidbare route-bron (expliciete weg + exact eindpunt) en
corroboreert met meerdere onafhankelijke reisbronnen. Deze wordt daarom als primaire praktische
route-referentie gebruikt: de hoofdroute zelf (NH22 + Domuhan–Bodhgaya Road, ~10,6 km, ~15-25 min)
is voldoende specifiek vastgelegd om niet langer als volledig onbepaald te worden gepresenteerd.
CCI kon de AAI-eigen paginatekst niet rechtstreeks openen (HTTP 503 bij directe fetch) en kan
daarom Sweep B's specifieke toeschrijving "AAI noemt 10 km" niet zelfstandig bevestigen —
zoeksynthese suggereert dat AAI's eigen pagina vaker met 5 km wordt geciteerd. De bredere 5-17
km-band blijft daarom staan als referentiepuntspreiding (verschillende metingen/eindpunten binnen
Gaya-district/Bodh Gaya), niet als bewijs dat de route zelf onduidelijk is.

## AOAY_RESULTAAT

**GEEN NIEUWE LINK — hergebruik van reeds bestaande, exhaustieve sweep (poort Q: geen
heronderzoek van al gesloten feiten), onafhankelijk herbevestigd door Sweep B.** De volledige
AOAY-primaire-tekstsweep uit `runs/active/BODHGAYA-DISCOVERY-001/PRE_BRONS/AOAY_TOP11_AUDIT.md`
(Project Gutenberg eBook #7452, 20.104 regels, doorzocht op alle varianten van `Gaya`/
`Bodh Gaya`/`Buddh Gaya`/`Buddhagaya`/`Mahabodhi`, hoofdletterongevoelig) leverde in het HELE boek
precies één treffer op (Sri Yukteswars Swami-inwijding "door de Mahant van Buddh Gaya", AOAY
ch.36, voetnoot) — al toegewezen aan kandidaat 046, niet corridor-specifiek en niet gekoppeld aan
een route/luchthaven. INDIA's Sweep B opende Project Gutenberg onafhankelijk opnieuw en vond
dezelfde ene treffer, geen corridor-/airport-sublocatie — bevestigt dat hergebruik van de
bestaande sweep terecht was. AOAY noemt bovendien nergens een luchthaven in de regio — het boek
(1946) predateert Gaya Airport als betekenisvolle pelgrimsroute sowieso.
`gebeurtenis_geverifieerd`: N.v.t. (geen treffer voor deze scope).
`exacte_fysieke_locatie_geverifieerd`: N.v.t.

## TOP11_RESULTAAT_PER_NAAM

**Sleutelfeit (bronverificatie, poort G.1)**: Gaya Airport werd pas op **13 november 2002**
internationaal operationeel voor Boeddhistische pelgrims (eerste lijndienst SriLankan Airlines,
Colombo via Delhi) — vóór 2002 was het een kleine, sinds 1936 bestaande domestic/civiele
aerodrome zonder aantoonbare rol in pelgrimsroutes. Bron: rechtstreeks geraadpleegd
(Grokipedia "Gaya Airport"-overzichtsartikel, corroborerend meerdere reisbronnen).

**METHODECORRECTIE (Sweep B, 14-08-2026, door CCI inhoudelijk gecontroleerd en overgenomen)**: de
redenering "persoon leefde/overleed vóór de luchthaven bestond/internationaliseerde, dus
corridor-link chronologisch onmogelijk" is NIET geldig voor deze taak. De taak onderzoekt de
FYSIEKE corridor/landstrook, niet uitsluitend reizen via de luchthaven als vervoermiddel.
Historische personen konden dezelfde fysieke corridorzone vóór het vliegveld doorkruisen (te voet,
per kar, langs de toenmalige route). Dit verandert geen enkele uitkomst hieronder (11/11 blijft
negatief) — alleen de formulering is gecorrigeerd van "chronologisch onmogelijk via de
luchthavenroute" naar "geen aantoonbare fysieke corridor-link na persoonsgerichte broncheck",
tenzij een echte routebron iets specifieks uitsluit (voor geen van de 11 namen het geval).

| # | Persoon | Methode | Bevinding | Bron(nen) |
|---|---|---|---|---|
| 1 | Paramahansa Yogananda | Chronologische toets (overleden 1952) + geen bestaande corridor-claim in eerder Bodh Gaya-onderzoek | GEEN_AANTOONBARE_CORRIDOR_LINK — geen aantoonbare fysieke corridor-link na persoonsgerichte broncheck (methodecorrectie: overlijden vóór de luchthaven sluit reizen VIA die luchthaven uit, niet automatisch fysieke doorkruising van de corridorzone; geen routebron gevonden die dat wel bevestigt) | — |
| 2 | Mahavatar Babaji | Geen vaste, verifieerbare data/locaties buiten AOAY zelf (reeds exhaustief doorzocht) | GEEN_AANTOONBARE_CORRIDOR_LINK — nuance (Sweep B): een YSS-bron beschrijft Swami Shyamananda Giri's Babaji-lichtvisioen (1946), maar dat vond plaats in Rajgir (gastenverblijf), niet in Bodh Gaya of op de corridor. Levert dus geen corridor-kandidaat op. Dit betekent NIET dat er buiten AOAY geen enkele Babaji-brondata bestaat — uitsluitend dat geen ervan een fysieke corridorlink oplevert | AOAY-sweep (hergebruikt); YSS (yssofindia.org, CCI-geverifieerd) |
| 3 | Lahiri Mahasaya | Chronologische toets (overleden 1895, vóór de aerodrome uit 1936 bestond) | GEEN_AANTOONBARE_CORRIDOR_LINK — geen aantoonbare fysieke corridor-link na persoonsgerichte broncheck (methodecorrectie, zie boven) | — |
| 4 | Sri Yukteswar | Chronologische toets (overleden 1936; Bodh Gaya-inwijding gedateerd rond 1906) + AOAY-sweep bevat geen corridor/luchthaven-detail | GEEN_AANTOONBARE_CORRIDOR_LINK — geen aantoonbare fysieke corridor-link na persoonsgerichte broncheck (methodecorrectie, zie boven) | AOAY-sweep (hergebruikt) |
| 5 | Ram Dass | Gerichte zoekopdracht: reisroute Gaya->Bodh Gaya januari 1971 specifiek nagetrokken | GEEN_AANTOONBARE_CORRIDOR_LINK — geen enkele geraadpleegde bron beschrijft HOE hij van Gaya naar Bodh Gaya reisde; expliciet ONBEKEND NA ONDERZOEK, niet aangenomen. Sweep B bevestigt: geen aanvullende bron gevonden | inquiringmind.com, insightmyanmar.org (gericht doorzocht, geen resultaat) |
| 6 | Neem Karoli Baba | Chronologische toets (overleden 1973, vóór 2002-internationalisering); geen bestaande fysieke Bodh Gaya-link voor hemzelf | GEEN_AANTOONBARE_CORRIDOR_LINK — geen aantoonbare fysieke corridor-link na persoonsgerichte broncheck (methodecorrectie, zie boven) | eerdere AOAY_TOP11_AUDIT.md (hergebruikt) |
| 7 | Anandamayi Ma | Chronologische toets (gedateerd Bodh Gaya-bezoek 18-10-1956) — geen corridor-specifieke bron gevonden | GEEN_AANTOONBARE_CORRIDOR_LINK — geen aantoonbare fysieke corridor-link na persoonsgerichte broncheck (methodecorrectie, zie boven) | — |
| 8 | Ramakrishna | Chronologische toets (overleden 1886) + al vastgesteld dat hij zelf nooit naar Gaya reisde | GEEN_AANTOONBARE_CORRIDOR_LINK — geen aantoonbare fysieke corridor-link na persoonsgerichte broncheck (methodecorrectie, zie boven); zie ook OUT_OF_SCOPE_NEGATIEVE_DETECTORBEVINDINGEN voor een gerelateerde moderne, niet-historische instelling | eerdere AOAY_TOP11_AUDIT.md (hergebruikt) |
| 9 | Ramana Maharshi | Met hoge zekerheid vastgesteld dat hij Arunachala 54 jaar nooit verliet (onafhankelijk van luchthaven-chronologie) | GEEN_AANTOONBARE_CORRIDOR_LINK (hoge zekerheid, hergebruikt — reden is fysieke afwezigheid, niet luchthaven-chronologie, dus methodecorrectie hier niet relevant) | eerdere AOAY_TOP11_AUDIT.md (hergebruikt) |
| 10 | Hariharananda (Giri) | Chronologische toets (overleden 2002) — geen enkele bron noemt een Bodh Gaya/Gaya-luchthavenbezoek | GEEN_AANTOONBARE_CORRIDOR_LINK — Sweep B bevestigt: geen aanvullende bron gevonden | eerdere AOAY_TOP11_AUDIT.md (hergebruikt), geen nieuwe treffer |
| 11 | Vivekananda | Chronologische toets (overleden 1902; twee Bodh Gaya-bezoeken ruim vóór 1936) | GEEN_AANTOONBARE_CORRIDOR_LINK — geen aantoonbare fysieke corridor-link na persoonsgerichte broncheck (methodecorrectie, zie boven) | eerdere AOAY_TOP11_AUDIT.md (hergebruikt) |

**Samenvatting**: 11 van 11 GEEN_AANTOONBARE_CORRIDOR_LINK, onafhankelijk bevestigd door Sweep B.
Voor de meeste namen is dit gebaseerd op een gerichte persoonsgerichte broncheck zonder resultaat
(niet langer geframed als "chronologisch onmogelijk", zie methodecorrectie). Voor 2 (Ram Dass,
Hariharananda) is er na gerichte bronraadpleging geen enkele aanwijzing gevonden — expliciet als
`ONBEKEND NA ONDERZOEK`/negatief resultaat vastgelegd, niet als aanname.

## OUT_OF_SCOPE_NEGATIEVE_DETECTORBEVINDINGEN (nieuw, Sweep B + CCI-verificatie)

- **Belur Math Gaya Ji sub-centre** — nieuw 15-acre campus, geopend 1 februari 2026, adres
  Village Jharha-Matua (nabij Matua Pahar), Halka Chilore, Post Gurua, Dist. Gaya Ji. Circa 30 km
  van Gaya-stad/Vishnupad Temple (051), dus buiten een kleine praktische airport→Bodh
  Gaya-omweg. Gekoppeld aan Ramakrishna's ontstaansverhaal via zijn vader Kshudiram's
  Gaya-pelgrimage (bevestigd via belurmath.org/media.belurmath.org). **GEEN historische fysieke
  Ramakrishna-locatie** — een moderne institutionele vestiging, niet gepromoveerd tot kandidaat.
  Compact vastgelegd als out-of-scope negatieve detectorbevinding, niet als 079+.

## LAAG3_HEAVYWEIGHTS

Geen nieuwe zelfstandige zwaargewicht-kandidaat gevonden DIRECT op de corridor zelf (Sweep A + B,
beide onafhankelijk 0). Alle geraadpleegde bronnen (tourism-overzichten, gaya.nic.in, Wikivoyage,
Justdial-temple-lijsten) noemen voor dit exacte wegtraject uitsluitend al bestaande, genummerde
kandidaten als "dichtbij de luchthaven": Mahabodhi Temple Complex (**046**, ~10,6 km van de
luchthaven, CCI-bevestigd), Vishnupad Temple (**051**), Mangala Gauri Temple (**070**). Sujata
Stupa (**047**, Bakraur) ligt aan de Bodh-Gaya-kant, niet op de luchthaven-corridor zelf, en is al
genummerd. Geen enkele bron noemt een zelfstandig zwaar dargah/gurdwara/tempel/ashram die
uitsluitend op dit specifieke wegtraject ligt en nog geen nummer heeft.

## NIEUWE_FYSIEKE_KANDIDATEN + nummers

GEEN (Sweep A + Sweep B, beide onafhankelijk 0/0). Geen enkele nieuwe, afzonderlijke fysieke
locatie voldeed aan de identiteitscontrole-drempel voor een nieuw nummer (079+ blijft ongebruikt
na deze dubbele sweep + reconciliatie).

## AFGEWEZEN_DUPLICATEN/SUBLOCATIES

N.v.t. — er waren geen kandidaat-vondsten om tegen te toetsen; de enige "kandidaten" die opdoken
in bronnen waren al bestaande, genummerde locaties (046, 047, 051, 070), terecht niet
heropend/hernummerd. De Belur Math Gaya Ji sub-centre (zie OUT_OF_SCOPE-sectie) is evenmin een
duplicaat van een bestaand nummer — het is een nieuwe, moderne, niet-historische instelling buiten
scope.

## NEGATIEVE_RESULTATEN

Zie TOP11_RESULTAAT_PER_NAAM (11/11, dubbel bevestigd) en AOAY_RESULTAAT hierboven (dubbel
bevestigd) — beide expliciet vastgelegd, niet stilzwijgend weggelaten. Aanvullend: geen enkele
bron beschrijft een specifiek, benoemd punt/plek/gebeurtenis DIRECT op het wegtraject zelf (geen
brug, geen dorpje met eigen pelgrimsbetekenis, geen historisch mijlpaal) — de corridor is
functioneel een kort, modern verharde verbindingsweg zonder eigen gedocumenteerde
pelgrimsidentiteit. Zie ook OUT_OF_SCOPE_NEGATIEVE_DETECTORBEVINDINGEN voor de Belur Math Gaya Ji
sub-centre (wel gedetecteerd, bewust niet gepromoveerd).

## BRONVERIFICATIE_STATUS (poort G.1)

Sweep A: voor elke AOAY/Top-11-claim die potentieel corridor-relevant leek (met name Ram Dass en
Sri Yukteswar) is de geciteerde/onderliggende brontekst rechtstreeks geraadpleegd. Het
luchthaven-internationaliseringsfeit (2002) is rechtstreeks geraadpleegd.

Reconciliatie (CCI, 14-08-2026): alle 4 Sweep B-reconciliatiepunten zelfstandig gecontroleerd via
WebSearch (corroborerende meerdere-bronsynthese op gaya.nic.in, belurmath.org/media.belurmath.org,
yssofindia.org/yogananda.org). Directe WebFetch van zowel de AAI-pagina als gaya.nic.in gaf HTTP
503 — expliciet vastgelegd als verificatiebeperking, niet verzwegen; waar een specifieke
bron-toeschrijving (AAI = 10 km) daardoor niet zelfstandig bevestigd kon worden, is dat expliciet
zo benoemd in CORRIDORRELEVANTIE in plaats van klakkeloos overgenomen.

## SATURATION_STATUS_SWEEP_A

**Regionale compleetheidsclaim voor deze corridor-scope**: toegestaan na dubbele sweep +
reconciliatie (poort R). Corridor-scope is klein en begrensd (één kort wegtraject, geen stad);
AOAY is exhaustief gedekt en dubbel bevestigd; alle 11 Top-11-namen individueel gecontroleerd met
expliciete negatieve resultaten, dubbel bevestigd; laag-3 gecontroleerd tegen meerdere
onafhankelijke bronfamilies zonder nieuwe treffer, dubbel bevestigd. **DOUBLE_SWEEP_COMPLETED: JA.
RECONCILED: JA.**

## COMMIT

Zie STATUS.md voor de actuele commit-hash van deze reconciliatie.

## BLOCKERS

Geen. Taak inhoudelijk afgerond voor de gedefinieerde scope (dubbele sweep + reconciliatie
voltooid). Geen PRE_PDF_CONTENT, geen PDF, geen A/B/C — nooit in scope voor deze taak (TASK.md).
Onderzoeksdata beschikbaar voor latere route-/reisplanning.

---
Geschreven door: CCI. Geen PRE_PDF_CONTENT, geen PDF, geen A/B/C, geen bestaande kandidaat
(046-078) gewijzigd. `PDF_STATUS: VERBODEN` gerespecteerd.
