# SATURATION_REPORT_003_ADDENDUM — Bodh Gaya, vijf openstaande punten opgelost

run_id: BODHGAYA-DISCOVERY-001
geschreven_op: 2026-08-06
geschreven_door: CCI
opdracht: INDIA6, bericht 026 ("SATURATED=JA nog niet geaccepteerd — los uitsluitend deze
laatste punten op")

Vervolg op `SATURATION_REPORT_002.md`. Geen bredere nieuwe sweep — uitsluitend de vijf
opgegeven controlepunten. `PDF_STATUS: VERBODEN` gerespecteerd, geen PDF/KML/pacing/route.

---

## 1. Sikhisme — gericht onderzocht, één MARK_WAARDIGE plek gevonden

**Gurdwara Sri Guru Tegh Bahadur Ji, Gaya** (nieuw genummerd: **078**) — nabij Vishnupad Temple
(051), aan de Falgu-rivier. Zowel Guru Nanak Dev als later Guru Tegh Bahadur bezochten deze plek
en bekritiseerden er direct de pind-daan-praktijk: zij onderwezen dat iemands eigen goede daden
tijdens het leven bepalend zijn voor het lot van de ziel, niet de rituelen die nakomelingen na de
dood laten uitvoeren. Beheerd door Udasi-priesters; drie exemplaren van de Siri Guru Granth Sahib
(Gurmukhi en Devnagri) zijn er ondergebracht. Binnen de 0-20 km-kernstraal (Gaya-stad, zelfde
zone als 051/070/075/076). Bron: sikhiwiki.org, worldgurudwaras.com — geen officiële overheidsbron
gevonden, wel meerdere onafhankelijke Sikh-specifieke bronnen die elkaar bevestigen. Geen andere
Sikh-locatie binnen de straal gevonden (de bekende Bihar-gurdwara's van Guru Nanak/Guru Gobind
Singh liggen in Patna, ver buiten zelfs de signaleringszone).

## 2. 063 versus 068 — DEFINITIEF OPGELOST: verschillende locaties, geen nummerprobleem

Bevestigd via een officiële bron (tibet.net, Central Tibetan Administration): Kyabje Shechen
Rabjam Rinpoche (voorzitter van de Nyingma Monlam Chenmo International Foundation) bracht een
apart bezoek aan "de uitbreiding van Shechen Karuna Bodh Gaya" ÉN inspecteerde afzonderlijk het
Padmasambhava-tempelcomplex vóór de consecratie — twee aparte bezoeken aan twee aparte fysieke
plekken, ook al zijn beide organisatorisch nauw met elkaar en met dezelfde persoon verbonden.
**Uitkomst: DIFFERENT_LOCATIONS, bevestigd.** Geen nummerintegriteitsprobleem — 063 en 068 blijven
beide staan zoals genummerd. Kandidaatrecords bijgewerkt met dit bewijs; 068's canonieke naam
aangevuld met de officiële naam "Shechen Tennyi Dargyeling" (gebouwd 1996). Correctierecord
toegevoegd aan `NUMBERING_REGISTRY.jsonl` (naam-aanvulling, nummer ongewijzigd).

## 3. 071 Pretshila en 076 Akshayavat — toegang geverifieerd

- **071 Pretshila**: GEEN expliciete niet-hindoe-toegangsbeperking gevonden, ondanks gerichte
  zoekopdracht — in duidelijk contrast met 051 (Vishnupad), waar meerdere onafhankelijke bronnen
  wél een verbod melden. Algemene reisbronnen beschrijven een gewone bezoekerservaring (heuveltop
  via trap, uitzicht, Yama-tempel uit 1787, Brahma Kund) met standaard kledingadvies, niet met een
  toegangsverbod. Afwezigheid van een gemeld verbod is geen garantie van vrije toegang, maar wijkt
  wezenlijk af van het 051-patroon. **Wat Mark naar verwachting kan bezoeken/zien**: de heuvel
  zelf, de Yama-tempel, de Brahma Kund.
- **076 Akshayavat**: BELANGRIJKE CORRECTIE — deze boom groeit BINNEN de tempelbinnenplaats van
  Vishnupad Temple (051) zelf, niet op een aparte, vrij toegankelijke plek (bevestigd door
  meerdere pind-daan-specifieke bronnen). Dit betekent dat de niet-hindoe-toegangsbeperking die
  bij 051 is vastgesteld hoogstwaarschijnlijk OOK hier geldt — een niet-hindoe bezoeker kan de
  boom naar verwachting NIET van dichtbij zien, net zomin als het Vishnupad-relict zelf. Dit is
  een redelijke afleiding op basis van de bevestigde ligging, geen apart bevestigde regel voor de
  boom. **Bronvoorbehoud**: één eerder gebruikte bron (prayagsamagam.com) bleek mogelijk over de
  ANDERE, bekendere Akshayavat in Prayagraj/Allahabad te gaan (een gelijknamige, andere boom met
  een vergelijkbare legende) — verwijderd als bron voor de Gaya-boom, niet gebruikt in de
  onderbouwing.
- **Nieuwe open categorisatievraag (niet zelf opgelost)**: omdat de Akshayavat fysiek binnen de
  tempelbinnenplaats van 051 ligt, is dit mogelijk eerder een sublocatie van hetzelfde bezoek dan
  een zelfstandige bestemming — vergelijkbaar met de weekplekken binnen 046. Nummer 076 blijft
  permanent gereserveerd (immutable), maar INDIA6/Mark beslist later of dit in het keuzerapport
  als eigen kandidaat of als sub-vermelding bij 051 wordt gepresenteerd.

## 4. 075 Jain Temple Gaya — EXCLUDED na hertoetsing

Herbeoordeeld tegen de exacte vraag: is er een zelfstandig verhaal, uniek object, levende
bijzondere ervaring of gebeurtenis boven "een Jaintempel"? Twee onderzoeksrondes (initiële sweep
+ deze hertoetsing) vonden niets buiten: gewijd aan Bhagawan Mahavira, een van twee Jaintempels in
Gaya-stad, een dharamshala voor pelgrims. Geen specifiek historisch moment, geen uniek
object/relict, geen bijzondere levende praktijk gevonden.

**Uitkomst: voldoet aan de harde uitsluitingsgrond "geen zelfstandige betekenis of ervaring".**
Status gewijzigd van MARK_WAARDIG naar `EXCLUDED_HARD_REASON` in `DISCOVERY_CANDIDATES.jsonl`.
Nummer 075 blijft permanent gereserveerd en wordt nooit hergebruikt (immutable-regel, zelfde
precedent als de al bestaande, niet-herbruikte Varanasi-nummers 041-045) — alleen de status
verandert. Niet kunstmatig behouden omdat het al genummerd was, zoals opgedragen.

## 5. Herbevestigingscontrole

- **Onbezochte relevante categorie**: sikhisme was de enige nog niet gerichte gecontroleerde
  categorie — nu gedaan (zie punt 1), leverde één MARK_WAARDIGE plek op. Christendom bleef
  gecontroleerd in `SATURATION_REPORT_002.md` (geen specifieke kerk gevonden). Geen andere
  onbezochte categorie geïdentificeerd.
- **Onopgeloste identiteit/dubbeling**: 063 vs. 068 is nu definitief opgelost (punt 2). Geen
  andere onopgeloste identiteitsvraag in de huidige kandidatenset.
- **Open lead die Marks A/B/C wezenlijk kan veranderen**: geen gevonden. De toegangscorrecties bij
  071/076 en de exclusie van 075 zijn feitelijke correcties, geen aanleiding voor verder onderzoek.
  Sikkim/Nepal/Laos/Taiwan-kloosternamen blijven `EXPLICIET ONBESCHIKBAAR` (ongewijzigd t.o.v.
  `SATURATION_REPORT_002.md`) — geen nieuwe zoekpoging deze ronde, conform opdracht ("geen bredere
  nieuwe sweep tenzij één van deze checks een concrete nieuwe lead oplevert" — geen van de vijf
  checks leverde zo'n lead op buiten de Sikh-gurdwara zelf).

## Nummerstand na deze ronde

BODHGAYA: 046-078 (was 046-077, +078 Gurdwara Sri Guru Tegh Bahadur Ji). 075 blijft binnen dit
bereik staan maar is nu EXCLUDED, niet MARK_WAARDIG. Globale nummering gevalideerd, geen
overlap met VARANASI (001-045).

## SATURATED = JA (herbevestigd)

Alle vijf opgegeven controlepunten zijn afgehandeld met een concrete uitkomst (niet ontweken):
één nieuwe kandidaat (078), één definitieve identiteitsoplossing (063/068, geen wijziging nodig),
twee toegangscorrecties (071/076), één eerlijke exclusie (075). De herbevestigingscontrole
(punt 5) leverde geen nieuwe open categorie, dubbeling, of wezenlijke lead op. Geen bredere sweep
uitgevoerd, conform opdracht.

---
Geschreven door: CCI, op verzoek van INDIA6 (PR #23, bericht 026). Geen A/B/C ingevuld namens
Mark. Geen PDF, geen KML, geen route/pacing/accommodatie. `PDF_STATUS: VERBODEN` gerespecteerd.
