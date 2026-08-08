#!/usr/bin/env python3
"""Bouwt de definitieve, menselijk leesbare Bodh Gaya-keuze-reisgids-PDF, in het
Varanasi-reisgidsformaat. Geen nieuw onderzoek -- uitsluitend bestaande, al goedgekeurde
brondata uit MARK_SELECTION_REPORT.md, MARK_DECISIONS_2026-08-05.jsonl en
DISCOVERY_CANDIDATES.jsonl, ná de retroactieve E.1-canontoets (commit 557cfd2).

046-049: bestaande Mark-keuze A (LOCKED, niet opnieuw ter keuze).
Open kandidaten (20 -> 16 na aftrek 046-049): 050, 051, 052, 058, 060, 061, 062, 063, 068,
070, 071, 072, 073, 074, 077, 078 -- DOOR MARK TE BEOORDELEN. Negen daarvan zijn expliciet
TWIJFELGEVAL (058, 060, 061, 063, 068, 073, 074, 077, 078): niet verborgen, wel met een
duidelijke kanttekening zodat Mark zelf kiest. EXCLUDED_HARD_REASON-nummers (053, 054, 055,
056, 057, 059, 064, 065, 066, 067, 069, 075) worden hier niet als keuze aangeboden. 076
(Akshayavat) is verwerkt als sublocatie bij 051.

Twee-pass build: pass 1 rendert met een placeholder-index om de echte paginanummers per
kandidaat te bepalen (via een onzichtbare Marker-flowable), pass 2 rendert de definitieve
PDF met de juiste paginanummers in de keuze-index. Layout/inhoud is tussen beide passes
identiek, dus de paginering verschuift niet.
"""
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import cm
from reportlab.lib import colors
from reportlab.platypus import (
    SimpleDocTemplate, Paragraph, Spacer, PageBreak, Table, TableStyle, HRFlowable, Flowable
)
from reportlab.lib.enums import TA_CENTER

# Versienummer VOORAAN in de bestandsnaam (Mark-besluit 2026-08-06), oplopend per sweep, nooit
# hergebruikt. Vorige, ongeversioneerde builds (BODHGAYA_046_049_KEUZE_REISGIDS.pdf,
# BODHGAYA_046_058_KEUZE_REISGIDS.pdf) blijven staan als historisch record. Dit is de eerste
# build onder de V1_-naamgevingsregel voor deze run, gebouwd na een opdracht met het letterlijke
# veld `PDF_GO: JA` (INDIA6 bericht 048, PR #23) plus `CONTENT_QA_ACCEPTED: JA`.
OUT = "runs/active/BODHGAYA-DISCOVERY-001/GOUD/USER/V1_BODHGAYA_KEUZE_REISGIDS.pdf"
TMP = "/tmp/claude-0/-home-user-india-knowledge-base/1fd594af-6399-554f-b402-799cc673ccdc/scratchpad/_bgy_pdf_pass1.pdf"

styles = getSampleStyleSheet()
styles.add(ParagraphStyle("CoverTitle", parent=styles["Title"], fontSize=26, spaceAfter=6, alignment=TA_CENTER))
styles.add(ParagraphStyle("CoverSub", parent=styles["Normal"], fontSize=13, alignment=TA_CENTER, spaceAfter=4, textColor=colors.HexColor("#444444")))
styles.add(ParagraphStyle("CandTitle", parent=styles["Heading1"], fontSize=16, spaceBefore=6, spaceAfter=4, textColor=colors.HexColor("#7a3b12")))
styles.add(ParagraphStyle("SectionHead", parent=styles["Heading2"], fontSize=12, spaceBefore=10, spaceAfter=10))
styles.add(ParagraphStyle("SubHead", parent=styles["Heading3"], fontSize=10.2, spaceBefore=7, spaceAfter=3, textColor=colors.HexColor("#7a3b12")))
styles.add(ParagraphStyle("Body", parent=styles["Normal"], fontSize=9.8, leading=13.8, spaceAfter=5))
styles.add(ParagraphStyle("Bijzonder", parent=styles["Normal"], fontSize=10.2, leading=13.8, spaceAfter=7, textColor=colors.HexColor("#1f5c1f"), fontName="Helvetica-Oblique"))
styles.add(ParagraphStyle("Onzeker", parent=styles["Normal"], fontSize=9.4, leading=13, spaceAfter=6, textColor=colors.HexColor("#8a4b00")))
styles.add(ParagraphStyle("Twijfel", parent=styles["Normal"], fontSize=9.6, leading=13.4, spaceAfter=6, textColor=colors.HexColor("#8a1f1f"), fontName="Helvetica-Oblique"))
styles.add(ParagraphStyle("TechBlock", parent=styles["Normal"], fontSize=7.6, leading=10.3, textColor=colors.HexColor("#555555")))
styles.add(ParagraphStyle("ClusterHead", parent=styles["Heading2"], fontSize=13, spaceBefore=14, spaceAfter=6, textColor=colors.HexColor("#7a3b12")))
styles.add(ParagraphStyle("StatusA", parent=styles["Normal"], fontSize=10, spaceAfter=6, textColor=colors.HexColor("#1f5c1f"), fontName="Helvetica-Bold"))
styles.add(ParagraphStyle("StatusOpen", parent=styles["Normal"], fontSize=10, spaceAfter=6, textColor=colors.HexColor("#a05a00"), fontName="Helvetica-Bold"))
styles.add(ParagraphStyle("StatusTwijfel", parent=styles["Normal"], fontSize=10, spaceAfter=6, textColor=colors.HexColor("#8a1f1f"), fontName="Helvetica-Bold"))
styles.add(ParagraphStyle("CellText", parent=styles["Normal"], fontSize=8.0, leading=9.6))
styles.add(ParagraphStyle("CellHead", parent=styles["Normal"], fontSize=8.3, leading=10, textColor=colors.white, fontName="Helvetica-Bold"))
styles.add(ParagraphStyle("CellGreen", parent=styles["Normal"], fontSize=8.0, leading=9.6, textColor=colors.HexColor("#1f5c1f"), fontName="Helvetica-Bold"))
styles.add(ParagraphStyle("CellOrange", parent=styles["Normal"], fontSize=8.0, leading=9.6, textColor=colors.HexColor("#a05a00"), fontName="Helvetica-Bold"))
styles.add(ParagraphStyle("CellRed", parent=styles["Normal"], fontSize=8.0, leading=9.6, textColor=colors.HexColor("#8a1f1f"), fontName="Helvetica-Bold"))

page_map = {}


class Marker(Flowable):
    """Onzichtbare flowable die het huidige paginanummer registreert onder 'key'."""

    def __init__(self, key):
        Flowable.__init__(self)
        self.key = key

    def wrap(self, availWidth, availHeight):
        return (0, 0)

    def draw(self):
        page_map[self.key] = self.canv.getPageNumber()


# ---------------------------------------------------------------------------
# Kandidaatdata -- uitsluitend overgenomen uit MARK_SELECTION_REPORT.md /
# DISCOVERY_CANDIDATES.jsonl (na de retroactieve E.1-canontoets). Geen nieuw onderzoek.
# ---------------------------------------------------------------------------

CANDIDATES = [
    dict(
        nr="046", naam="Mahabodhi Temple Complex", hook="de plek van de verlichting zelf",
        cluster="Kerncluster", mark_status="A", twijfel="",
        wat_is_het="Het complex rond de plek waar Boeddha 2500 jaar geleden verlichting bereikte. "
        "Omvat de Vajrasana (de diamanttroon, bewaard door keizer Ashoka) en de directe "
        "nakomeling van de oorspronkelijke Bodhi-boom.",
        waarom="Sta op de plaats waar Boeddha de verlichting bereikte -- niet een afbeelding of "
        "herdenkteken, maar de plek zelf.",
        betekenis="Binnen dezelfde ommuurde grens liggen ook de zeven traditionele plekken van de "
        "weken direct na de verlichting: de Animeshlochan Chaitya (waar Boeddha een week lang "
        "onafgebroken naar de boom staarde), de Ratnachakrama (het juwelenwandelpad, met stenen "
        "lotusbloemen die zijn voetstappen markeren), de Ratnaghar Chaitya, de Ajapala "
        "Nigrodh-boom, de Muchalinda-vijver en de Rajyatana-boom. Het geheel is UNESCO-"
        "werelderfgoed. Bijzonder: Swami Sri Yukteswar Giri -- Yogananda's eigen, directe guru, "
        "in Marks eigen Kriya-lijn (Babaji, Lahiri Mahasaya, Sri Yukteswar, Yogananda) -- werd "
        "hier op Guru Purnima, juli 1906, geinitieerd in de sannyas-orde.",
        ervaart="Het tempelgebouw, de eeuwenoude boom, monniken en pelgrims uit de hele "
        "boeddhistische wereld, votiefstoepa's rondom -- een levend, dagelijks bezocht "
        "heiligdom, geen stil monument.",
        onderscheidend="Een van de vier belangrijkste boeddhistische pelgrimsplaatsen ter wereld, "
        "en de enige plek die de verlichting zelf markeert.",
        bezoektijd="NOG NIET ONDERZOCHT",
        combineer="047 Sujata Stupa (circa 20 minuten lopen, inclusief oversteek Phalgu-rivier).",
        tips="Dagelijks vrij toegankelijk, geen inschrijving of speciale toegang nodig.",
        overslaan="Geen reden om over te slaan -- dit is de ankerplek van de hele regio.",
        onzekerheden="Exacte locatie van Sri Yukteswars sannyas-initiatie (1906) binnen Bodh Gaya "
        "niet vastgesteld -- de gebeurtenis zelf is wel bevestigd (zie governance-canon: "
        "gebeurtenis en exacte plek apart vastgelegd).",
    ),
    dict(
        nr="047", naam="Sujata Stupa, Bakraur", hook="waar de Middenweg begon",
        cluster="Kerncluster", mark_status="A", twijfel="",
        wat_is_het="Een archeologisch stoepacomplex (oorspronkelijke bouw 2e eeuw v.Chr., latere "
        "uitbreidingsfase 8e-10e eeuw CE) op de plek waar Sujata, een dorpsvrouw uit Bakraur, "
        "Boeddha een kom rijstpudding aanbood.",
        waarom="Bezoek de exacte plek waar een dorpsvrouw Boeddha's leven een beslissende wending "
        "gaf.",
        betekenis="Deze gebeurtenis beeindigde Boeddha's zesjarige extreme ascese en leidde "
        "rechtstreeks tot zijn ontdekking van de Middenweg -- een kernleerstuk van het "
        "boeddhisme.",
        ervaart="Een tastbaar, gedateerd monument op de exacte plek van deze gebeurtenis, circa 20 "
        "minuten lopen van het hoofdcomplex, rustiger en minder toeristisch.",
        onderscheidend="De enige plek die deze specifieke, verhaalbepalende gebeurtenis markeert "
        "-- complementair aan zowel Mahabodhi (de verlichting zelf) als Dungeshwari (de ascese "
        "die voorafging), geen overlap.",
        bezoektijd="NOG NIET ONDERZOCHT",
        combineer="046 Mahabodhi Temple Complex (circa 1,2 km, eenvoudig te combineren op dezelfde "
        "dag).",
        tips="Vereist een korte oversteek van de Phalgu-rivier vanaf Bodh Gaya.",
        overslaan="Geen duidelijke reden om over te slaan -- complementair aan 046 en 048.",
        onzekerheden="Geen open onzekerheden meer.",
    ),
    dict(
        nr="048", naam="Dungeshwari Cave Temples (Mahakala Caves)", hook="de grotten van de zes jaar ascese",
        cluster="Aanvullend", mark_status="A", twijfel="",
        wat_is_het="Rotsgehouwen grottempels (5e-6e eeuw CE) op de plek waar Boeddha zes jaar "
        "extreme ascese beoefende voor hij naar Bodh Gaya afdaalde voor de uiteindelijke "
        "verlichting.",
        waarom="Ga naar de plek waar Boeddha, voor zijn verlichting, zichzelf tot op het bot "
        "uithongerde op zoek naar waarheid.",
        betekenis="Het spiegelbeeld-verhaal van Sujata's aanbieding -- de ascese die eraan "
        "voorafging. Genoemd door de 7e-eeuwse Chinese pelgrim Xuanzang. Een van de grotten "
        "bevat een gouden beeld van de uitgemergelde Boeddha.",
        ervaart="Rustige rotsgrotten in de heuvels, ver van de drukte van het hoofdcomplex, met het "
        "aangrijpende uitgemergelde-Boeddhabeeld als middelpunt.",
        onderscheidend="Geen andere plek toont dit specifieke moment.",
        bezoektijd="NOG NIET ONDERZOCHT",
        combineer="Eigen rit nodig; niet zonder meer op dezelfde ochtend te combineren met de "
        "kerncluster.",
        tips="Circa 12-14 km van Bodh Gaya (bronnen varieren), vereist een aparte rit per taxi of "
        "auto-riksja.",
        overslaan="Geen duidelijke reden om over te slaan qua inhoud -- wel de grootste "
        "reisinspanning van de kerngroep.",
        onzekerheden="Geen bevestigde Google Maps-marker gevonden -- identiteit blijft wel "
        "eenduidig bevestigd via twee onafhankelijke overheidsbronnen en de dorpsnaam Larpur.",
    ),
    dict(
        nr="049", naam="Great Buddha Statue", hook="het grootste Boeddhabeeld van India",
        cluster="Optioneel", mark_status="A", twijfel="",
        wat_is_het="Een circa 20 m hoog zittend Boeddhabeeld (circa 24 m totale constructie "
        "inclusief lotus en voetstuk), gebouwd door Daijokyo Buddhist Temple (Japanse "
        "leken-boeddhistische organisatie, tempelgebouw geopend 13 februari 1983).",
        waarom="Bekijk het eerste en grootste Boeddhabeeld ooit gebouwd in modern India -- "
        "indrukwekkend, maar geen onderdeel van het historische verlichtingsverhaal zelf.",
        betekenis="Geconsacreerd door de 14e Dalai Lama op 18 november 1989 als symbool van de "
        "wereldwijde herleving van het boeddhisme.",
        ervaart="Een groot, vrij toegankelijk beeld in open lucht, in tuinen even buiten het "
        "centrum.",
        onderscheidend="Indrukwekkend landmark, maar niet essentieel voor het begrip van Boeddha's "
        "eigen verhaal, in tegenstelling tot de drie plekken hierboven.",
        bezoektijd="NOG NIET ONDERZOCHT",
        combineer="046 Mahabodhi Temple Complex (circa 1,1-1,5 km, eenvoudig te combineren).",
        tips="Vrij toegankelijk, altijd zichtbaar, geen inschrijving nodig.",
        overslaan="Geen onderdeel van Boeddha's eigen biografische verhaal.",
        onzekerheden="Geen bevestigde Google Maps-marker; hoogte van het beeld zelf is intern "
        "inconsistent tussen bronnen (18,5 m vs. 20 m).",
    ),
    dict(
        nr="050", naam="Archaeological Museum of Bodh Gaya (ASI)", hook="de originele Bodhi-boom-omheining",
        cluster="Bij Mahabodhi", mark_status="OPEN", twijfel="",
        wat_is_het="Een door de Archaeological Survey of India beheerd museum (opgericht 1956), "
        "direct naast het Mahabodhi-complex.",
        waarom="Bekijk de ORIGINELE stenen balustrade-fragmenten die ooit de Bodhi-boom zelf "
        "omsloten (Sunga-periode, circa 2e eeuw v.Chr.) -- geen replica, maar een direct fysiek "
        "object uit de kernplek van de verlichting.",
        betekenis="Geen ander museum heeft objecten die direct van de Bodhi-boom-omheining zelf "
        "afkomstig zijn -- uniek in zijn soort binnen Bodh Gaya.",
        ervaart="Gereconstrueerde stenen balustrade, reliefs, Pala-periode sculpturen, munten uit "
        "de Mughal-, Maurya- en Gupta-periode, in twee galerijen en een open binnenplaats.",
        onderscheidend="Het enige museum ter plekke met objecten rechtstreeks afkomstig van de "
        "Bodhi-boom-omheining zelf.",
        bezoektijd="NOG NIET ONDERZOCHT",
        combineer="046 Mahabodhi Temple Complex (grenst direct aan het complex).",
        tips="Regulier entreekaartje, geen speciale toegang of inschrijving nodig.",
        overslaan="Geen levende praktijk en geen directe biografische link met de verlichting zelf "
        "-- een museale, archeologische aanvulling op 046, geen zelfstandig verhaal.",
        onzekerheden="Geen gemeld.",
    ),
    dict(
        nr="051", naam="Vishnupad Temple, Gaya", hook="het voetspoor van Vishnu",
        cluster="Gaya-stad", mark_status="OPEN", twijfel="",
        wat_is_het="Een actieve hindoetempel aan de Falgu-rivier in Gaya-stad (circa 12-15 km van "
        "Bodh Gaya), met een 40 cm lange voetafdruk in zwart basaltgesteente, vereerd als het "
        "voetspoor van Vishnu. Binnen dezelfde tempelbinnenplaats groeit de Akshayavat, een als "
        "onvergankelijk vereerde eeuwenoude banyanboom (genoemd in de Purana's, de Ramayana en "
        "Jain-teksten) -- geen aparte kandidaat, maar onderdeel van hetzelfde bezoek.",
        waarom="Een singulier, fysiek uniek relict (geen generiek Vishnu-beeld), en een van de "
        "belangrijkste plekken in heel India voor Pind Daan (voorouder-verlossingsrituelen).",
        betekenis="Volgens overlevering bevrijdt een Pind Daan hier voorouders tot veertien "
        "generaties terug. De Akshayavat was volgens de Ramayana de enige getuige die de "
        "waarheid sprak toen Sita hier een Pind Daan voor koning Dasharatha uitvoerde. "
        "Toegangsregel: meerdere onafhankelijke reisbronnen melden consistent dat niet-hindoes de "
        "tempel zelf (en dus vermoedelijk ook de boom in dezelfde binnenplaats) niet mogen "
        "betreden (vergelijkbaar met de bekendere regel bij Jagannath Temple, Puri) -- geen "
        "officiele bron bevestigt of ontkent dit expliciet.",
        ervaart="Als niet-hindoe vermoedelijk GEEN toegang tot het tempelinterieur/het voetspoor "
        "zelf, en vermoedelijk ook niet tot de Akshayavat van dichtbij -- wel de omliggende "
        "straatjes, de buitenkant van de tempel, en de drukte van een actieve, levende "
        "bedevaartsplek eromheen.",
        onderscheidend="Geen andere plek in de straal heeft dit specifieke relict of deze "
        "specifieke, eeuwenoude rituele functie.",
        bezoektijd="NOG NIET ONDERZOCHT",
        combineer="Eigen stad, circa 12-15 km van de Bodh Gaya-kerncluster. Zelfde bredere "
        "Gaya-stad-zone als 070 Mangala Gauri, 071 Pretshila en 078 de gurdwara.",
        tips="Drukst tijdens Pitru Paksha (september); de omgeving is permanent toegankelijk. Het "
        "tempelinterieur is voor een niet-hindoe bezoeker vermoedelijk NIET toegankelijk.",
        overslaan="Geen directe koppeling aan Marks eigen Kriya-/boeddhistische focus, en het "
        "tempelinterieur zelf is voor een niet-hindoe bezoeker vermoedelijk niet toegankelijk.",
        onzekerheden="De toegangsbeperking voor niet-hindoes steunt op consistente reisbronnen, "
        "niet op een officiele bevestiging.",
    ),
    dict(
        nr="052", naam="Tergar Monastery", hook="het Karmapa-klooster",
        cluster="Studie/retraite", mark_status="OPEN", twijfel="",
        wat_is_het="Een Karma-Kagyu-klooster/studie-instituut, gesticht door Yongey Mingyur "
        "Rinpoche (grond geschonken door Tai Situ Rinpoche in 2000, gebouw voltooid 2006), met "
        "ruim 300 monniken.",
        waarom="Periodieke (doorgaans jaarlijkse) gastheer van het Kagyu Monlam-gebedsfestival "
        "onder leiding van de 17e Karmapa, een van de hoogste gezagsdragers binnen het Tibetaans "
        "boeddhisme.",
        betekenis="Enige klooster in Bodh Gaya met een directe, periodieke aanwezigheid van de "
        "Karmapa zelf.",
        ervaart="Buiten het festival: een actief studieklooster, monniken in studie/meditatie. "
        "Tijdens het Monlam: een grote internationale samenkomst met de Karmapa zelf. Bevestigde "
        "meest recente editie: 40e Kagyu Monlam Chenmo, 23 december 2025 -- 3 januari 2026. Datum "
        "volgende editie: ONBEKEND, nog niet gepubliceerd.",
        onderscheidend="Enige klooster met een directe, periodieke Karmapa-aanwezigheid.",
        bezoektijd="NOG NIET ONDERZOCHT",
        combineer="NOG NIET ONDERZOCHT.",
        tips="Kloostergebouw permanent aanwezig; bezoekbaarheid buiten het festivalseizoen is "
        "onzeker.",
        overslaan="De sterkste reden om te komen (Karmapa/Monlam) is evenement- en "
        "seizoensafhankelijk, met een datum die niet ver vooraf vaststaat; buiten die periode is "
        "het een regulier studieklooster.",
        onzekerheden="Bezoekbaarheid buiten het festivalseizoen niet bevestigd. Datum "
        "eerstvolgende editie nog niet gepubliceerd (ONBEKEND).",
    ),
    dict(
        nr="058", naam="Japanese Temple / Indosan Nippon (Nipponzan-Myohoji)", hook="stichter van de vredespagode-beweging",
        cluster="Internationale kloosters", mark_status="OPEN",
        twijfel="Twijfelgeval: niet uitgesloten omdat Fujii internationaal significant is als "
        "stichter van de wereldwijde vredespagode-beweging -- maar of dat voldoende is voor een "
        "eigen keuzeplek is aan Mark.",
        wat_is_het="Een klooster van de Nipponzan-Myohoji-orde, gesticht 1972 door Nichidatsu "
        "Fujii (1885-1985) -- apart en bevestigd verschillend van Daijokyo Buddhist Temple "
        "(eigenaar van 049).",
        waarom="Fujii was de stichter van de wereldwijde vredespagode-beweging (Peace Pagoda's) "
        "en nauw geassocieerd met geweldloosheidsfilosofie.",
        betekenis="Enige klooster in Bodh Gaya met een directe koppeling aan de internationale "
        "vredespagode-beweging.",
        ervaart="Een Japans klooster in Nichiren-traditie, gesticht door een figuur die wereldwijd "
        "bekend staat om zijn inzet voor vrede.",
        onderscheidend="Specifieke, internationaal significante stichtersgeschiedenis, geen "
        "anoniem nationaal paviljoen.",
        bezoektijd="NOG NIET ONDERZOCHT",
        combineer="NOG NIET ONDERZOCHT.",
        tips="Vrij toegankelijk, gratis entree (bevestigd).",
        overslaan="Geen directe biografische link met Boeddha's verlichting.",
        onzekerheden="Geen gemeld -- bevestigd als andere locatie dan 049 (Daijokyo Buddhist "
        "Temple).",
    ),
    dict(
        nr="060", naam="Palyul Namdroling Monastery", hook="Nyingma-traditie bij de Great Buddha Statue",
        cluster="Internationale kloosters", mark_status="OPEN",
        twijfel="Twijfelgeval: niet uitgesloten omdat de naam/lijn officieel is toegekend door "
        "zowel Drubwang Pema Norbu Rinpoche als de Dalai Lama -- maar of dat voldoende zwaarte "
        "geeft ten opzichte van 052/056 is aan Mark.",
        wat_is_het="Een groot Nyingma-klooster (Palyul-lijn) bij de Great Buddha Statue (049), nog "
        "deels in aanbouw.",
        waarom="Officiele naam gegeven door zowel Drubwang Pema Norbu Rinpoche als de Dalai Lama; "
        "minder toeristisch dan de meeste andere kloosters, expliciet geschikt om te mediteren.",
        betekenis="Vertegenwoordigt de Nyingma-traditie, de oudste school van het Tibetaans "
        "boeddhisme.",
        ervaart="Een groot, rustig kloostercomplex, deels nog in aanbouw, met ruimte voor stille "
        "meditatie.",
        onderscheidend="Andere Tibetaans-boeddhistische traditie (Nyingma) dan de andere "
        "Tibetaanse kandidaten in dit rapport.",
        bezoektijd="NOG NIET ONDERZOCHT",
        combineer="Bij de Great Buddha Statue (049), dus logisch te combineren met dat bezoek.",
        tips="Minder toeristisch dan vergelijkbare kloosters.",
        overslaan="Geen directe biografische link met Boeddha's verlichting.",
        onzekerheden="Geen officiele/academische bron gevonden.",
    ),
    dict(
        nr="061", naam="Burmese Vihara", hook="pionier onder de internationale kloosters",
        cluster="Internationale kloosters", mark_status="OPEN",
        twijfel="Twijfelgeval: niet uitgesloten ondanks de vertegenwoordigings-achtige framing, "
        "omdat pioniersstatus + een door de Birmese autoriteiten aangestelde abt + een "
        "doorlopende liefdadigheidspraktijk reele, zij het bescheiden, signalen zijn.",
        wat_is_het="Een Myanmarees (Birmees) klooster, gesticht 1936, aan de oorspronkelijke weg "
        "Gaya-Bodhgaya, dicht bij Mahabodhi.",
        waarom="Een van de vroegste internationale kloosters van Bodh Gaya -- pionierstatus binnen "
        "de internationale kloosterzone.",
        betekenis="Gesticht onder leiding van Eerwaarde U Dhammetsara, de eerste door de Birmese "
        "boeddhistische autoriteiten aangestelde abt.",
        ervaart="Een Boeddhabeeld gemaakt van riet (ongebruikelijk materiaal), een meditatiezaal, "
        "een bibliotheek, en een dagelijkse gratis vegetarische lunch (12.30u, op donatiebasis).",
        onderscheidend="Pioniersstatus en het rieten Boeddhabeeld, elders niet gemeld.",
        bezoektijd="NOG NIET ONDERZOCHT",
        combineer="Dicht bij Mahabodhi (046), eenvoudig te combineren.",
        tips="Vrij toegankelijk, gastenverblijf aanwezig.",
        overslaan="Geen directe biografische link met Boeddha's verlichting.",
        onzekerheden="Geen gemeld.",
    ),
    dict(
        nr="062", naam="Mahabodhi Society of India (Bodh Gaya-centrum)", hook="de organisatie die 046 heropende voor boeddhisten",
        cluster="Bij Mahabodhi", mark_status="OPEN", twijfel="",
        wat_is_het="Het honderd jaar oude, oudste bestaande kloostergebouw van Bodh Gaya, ten "
        "westen van de Mahabodhi-tempel, van de organisatie gesticht in 1891 door Anagarika "
        "Dharmapala (Sri Lanka).",
        waarom="Dit is de plek/organisatie die aan de basis lag van het herstel van boeddhistische "
        "eredienst bij de Mahabodhi-tempel zelf -- destijds beheerd door een Saivitische priester, "
        "met het Boeddhabeeld tot hindoe-icoon gemaakt en boeddhisten geweerd van aanbidding.",
        betekenis="Dharmapala's campagne leidde uiteindelijk tot de Bodh Gaya Temple Act (1949) en "
        "gedeeld beheer van het hoofdcomplex -- een direct, causaal verhaal achter de huidige, "
        "vrij toegankelijke status van 046.",
        ervaart="Het oudste kloostergebouw van de hele plek, met een tastbare band met de "
        "herstelgeschiedenis van Mahabodhi zelf.",
        onderscheidend="Niet 'nog een nationaal paviljoen', maar de organisatie achter de "
        "herstelde boeddhistische controle over het hoofdcomplex.",
        bezoektijd="NOG NIET ONDERZOCHT",
        combineer="Direct ten westen van 046, onderdeel van hetzelfde complexbezoek.",
        tips="Vrij toegankelijk, actieve organisatie.",
        overslaan="Geen levende praktijk in de zin van een klooster met monniken in dagelijkse "
        "studie; vooral relevant voor wie het herstelverhaal van 046 zelf wil begrijpen.",
        onzekerheden="Geen gemeld.",
    ),
    dict(
        nr="063", naam="Padmasambhava Grand Temple and Nyingma Center", hook="het nieuwste grote tempelcomplex",
        cluster="Internationale kloosters", mark_status="OPEN",
        twijfel="Twijfelgeval: niet uitgesloten omdat het complex jaarlijks de Nyingma Monlam "
        "Chenmo huisvest met Karmapa-aanwezigheid -- maar toegankelijkheid buiten het festival is "
        "volledig onbevestigd, dus onduidelijk wat een gewoon bezoek buiten die periode oplevert.",
        wat_is_het="Een nieuw ingewijd (23 januari 2026) tempelcomplex voor de Nyingma-traditie, "
        "geconsacreerd in verband met de 37e Nyingma Monlam Chenmo.",
        waarom="Het nieuwste grote toevoeging aan Bodh Gaya's internationale kloosterlandschap, "
        "met een ceremonie geleid door Kyabje Shechen Rabjam Rinpoche en aanwezigheid van de "
        "Karmapa.",
        betekenis="Huisvest monniken, nonnen en ngakpa's tijdens het jaarlijkse gebedsfestival -- "
        "een actief, groeiend centrum, geen statisch monument.",
        ervaart="Een grootschalig, nieuw tempelcomplex, tijdens het festivalseizoen (januari) vol "
        "met monniken/nonnen/ngakpa's.",
        onderscheidend="Een derde, aparte Nyingma-vestiging naast 060 en 068 (bevestigd andere "
        "locatie).",
        bezoektijd="NOG NIET ONDERZOCHT",
        combineer="NOG NIET ONDERZOCHT.",
        tips="ONBEVESTIGD BUITEN HET FESTIVAL: geen bron vermeldt reguliere openingstijden of "
        "bezoekersbeleid buiten de Monlam Chenmo (januari).",
        overslaan="Zeer nieuw, dus weinig onafhankelijke reisverslagen nog beschikbaar.",
        onzekerheden="Publieke toegankelijkheid buiten het festivalseizoen is een onopgeloste, "
        "keuze-relevante onzekerheid.",
    ),
    dict(
        nr="068", naam="Shechen Monastery (Shechen Tennyi Dargyeling)", hook="verbonden met Dilgo Khyentse Rinpoche",
        cluster="Internationale kloosters", mark_status="OPEN",
        twijfel="Twijfelgeval: niet uitgesloten omdat Shechen wereldwijd geassocieerd is met Dilgo "
        "Khyentse Rinpoche, een van de belangrijkste Tibetaans-boeddhistische leraren van de 20e "
        "eeuw -- maar dit is een dochterklooster, niet de hoofdzetel, en slechts één hoofdbron.",
        wat_is_het="Een Nyingma-klooster, officieel Shechen Tennyi Dargyeling, gebouwd 1996, "
        "ingewijd door de Dalai Lama, dicht bij de Mahabodhi-tempel.",
        waarom="Shechen is wereldwijd een van de bekendste Nyingma-kloosterlijnen, geassocieerd "
        "met Dilgo Khyentse Rinpoche.",
        betekenis="Internationale reputatie binnen de Nyingma-traditie, los van de andere "
        "Tibetaanse kandidaten in dit rapport.",
        ervaart="Een gevestigd (1996), actief klooster dicht bij het hoofdcomplex.",
        onderscheidend="Bevestigd andere locatie dan Padmasambhava Grand Temple (063).",
        bezoektijd="NOG NIET ONDERZOCHT",
        combineer="Dicht bij Mahabodhi (046).",
        tips="Vrij toegankelijk verwacht (niet expliciet bevestigd).",
        overslaan="Geen directe biografische link met Boeddha's verlichting.",
        onzekerheden="Eén hoofdbron met detail -- Tripadvisor en Google Maps bevestigen alleen "
        "naam/bestaan.",
    ),
    dict(
        nr="070", naam="Mangala Gauri Temple (Shakti Peeth)", hook="een van de 18 Maha Shakti Peethas van India",
        cluster="Gaya-stad", mark_status="OPEN", twijfel="",
        wat_is_het="Een van de 18 Maha Shakti Peethas van heel India, op een heuvel met circa 200 "
        "treden, circa 4 km van Gaya Junction.",
        waarom="Volgens de legende viel hier Sati's borst -- een van de nationaal belangrijkste "
        "Shakti-plekken van heel India, vermeld in de Padma Purana, Vayu Purana, Agni Purana en "
        "Devi Bhagwat Purana.",
        betekenis="Nationaal-religieus van een hogere orde dan een generieke tempel -- "
        "vergelijkbaar in gewicht met Vishnupad (051), maar een aparte traditie (Shakti i.p.v. "
        "Vishnu-voetspoor).",
        ervaart="Een actieve heuveltempel, bereikbaar via een trappenpad, met uitzicht over Gaya.",
        onderscheidend="Shakti-Peeth-status is een nationale religieuze categorie -- geen andere "
        "kandidaat in dit rapport heeft deze status.",
        bezoektijd="NOG NIET ONDERZOCHT",
        combineer="Zelfde bredere Gaya-stad-zone als 051, 071, 078.",
        tips="Actieve, publieke tempel.",
        overslaan="Geen directe koppeling aan Marks Kriya-/boeddhistische focus.",
        onzekerheden="Geen expliciete niet-hindoe-toegangsregel gevonden (niet hetzelfde patroon "
        "als 051) -- niet apart geverifieerd, dus ook niet bevestigd als vrij.",
    ),
    dict(
        nr="071", naam="Pretshila Hill", hook="Heuvel van de Geesten",
        cluster="Gaya-stad", mark_status="OPEN", twijfel="",
        wat_is_het="\"Heuvel van de Geesten\" -- centrum van hindoe voorouderverlossingsrituelen "
        "(pind daan), met een Yama-tempel gebouwd in 1787 door Ahilya Bai en de Brahma Kund "
        "eronder.",
        waarom="Volgens overlevering bezocht Rama deze heuvel met Sita om Pind Daan te doen voor "
        "koning Dasharatha.",
        betekenis="Een van de kernplekken van het bredere Gaya pind-daan-complex, met een eigen, "
        "specifiek relict (de Yama-tempel) en verhaal.",
        ervaart="Heuveltop bereikbaar via een trap, uitzicht, de Yama-tempel en de Brahma Kund.",
        onderscheidend="Ander specifiek relict/verhaal dan Vishnupad (051) en Mangala Gauri (070) "
        "-- geen duplicaat, wel onderdeel van hetzelfde bredere complex.",
        bezoektijd="NOG NIET ONDERZOCHT",
        combineer="Zelfde bredere Gaya-stad-zone als 051, 070, 078.",
        tips="GEVERIFIEERD: geen expliciete niet-hindoe-toegangsbeperking gevonden, in duidelijk "
        "contrast met 051 -- Mark kan naar verwachting de heuvel, de Yama-tempel en de Brahma "
        "Kund bezoeken/bekijken.",
        overslaan="Geen directe koppeling aan Marks Kriya-/boeddhistische focus.",
        onzekerheden="Afwezigheid van een gemeld verbod is geen garantie van vrije toegang.",
    ),
    dict(
        nr="072", naam="Brahmayoni Hill / Gayasisa Stupa (Vuurpreek-locatie)", hook="waar Boeddha de Vuurpreek hield",
        cluster="Boeddha-biografie na de verlichting", mark_status="OPEN", twijfel="",
        wat_is_het="Een heuvel (voorheen Gayasisa genoemd, nu Brahmayoni), waar volgens de "
        "Pali-canon Boeddha de Vuurpreek (Adittapariyaya Sutta) hield, gemarkeerd door de "
        "Gayasisa Stupa. De klassieke Pali-canon plaatst deze zelf op \"Gayasisa, near Gaya\" "
        "(Samyutta Nikaya; Vinaya). De identificatie met de huidige Brahmayoni-heuvel komt uit "
        "G.P. Malalasekera's academische \"Dictionary of Pali Proper Names\", die ook de "
        "7e-eeuwse Chinese pelgrim Xuanzang citeert die er de drie stoepa's van de bekeerde "
        "Kassapa-broers zag. Onafhankelijk hiervan zijn archeologische vondsten gedaan "
        "(Boeddhabeelden, een votiefstoepa, Pali-inscripties) die vroege boeddhistische "
        "aanwezigheid bevestigen -- een drievoudig onderbouwde identificatie (primaire canon + "
        "academisch naslagwerk + archeologie).",
        waarom="Boeddha preekte hier aan circa 1000 voormalige vuur-vererende asceten, die allen "
        "verlicht raakten tijdens het luisteren -- een van Boeddha's bekendste toespraken.",
        betekenis="Een biografisch/leerstellig moment NA de verlichting, in tegenstelling tot de "
        "bestaande kandidaten die de periode rond en vóór de verlichting dekken (046-049).",
        ervaart="Een heuvel met de Gayasisa Stupa als markering, uitzicht over de regio.",
        onderscheidend="Vergelijkbaar in soort biografische zwaarte met 047 (Sujata) en 048 "
        "(Dungeshwari), maar dekt een ander, later moment (na de verlichting, tijdens Boeddha's "
        "onderwijzende periode).",
        bezoektijd="NOG NIET ONDERZOCHT",
        combineer="In de bredere Gaya-omgeving; exacte afstand tot 046 nog niet berekend (geen "
        "bevestigd coordinaat).",
        tips="Publiek toegankelijke heuvel/pelgrimsplek (niet expliciet toegangsbeperkt).",
        overslaan="Geen bevestigd coordinaat, dus geen bekende exacte afstand of reistijd vanaf "
        "046 -- dat maakt inplannen nu nog lastig.",
        onzekerheden="Geen enkele officiele overheidsbron vermeldt de Vuurpreek-context zelf "
        "expliciet (wel de heuvel als bezienswaardigheid).",
    ),
    dict(
        nr="073", naam="Jagannath Temple (naast Mahabodhi)", hook="25 voet van de heiligste boeddhistische plek",
        cluster="Bij Mahabodhi", mark_status="OPEN",
        twijfel="Twijfelgeval: niet uitgesloten omdat de actieve, doorlopende praktijk (dagelijkse "
        "voedseluitdeling, jaarlijkse rathyatra) een reeel signaal is -- maar het gewicht leunt "
        "zwaar op de fysieke nabijheid tot 046, niet op onafhankelijke, eigen nationale "
        "bedevaartsfaam zoals bij 051/070.",
        wat_is_het="Een hindoetempel op officieel bevestigd 25 voet (7,5 m) afstand ten noorden "
        "van de Mahabodhi-tempel zelf, met grote idolen van Krishna, Balarama en Subhadra, en een "
        "nieuw gebouwde Ram-Janaki-tempel binnen hetzelfde complex.",
        waarom="De opvallende fysieke nabijheid tot de heiligste boeddhistische plek ter wereld -- "
        "een eigen interreligieus coexistentieverhaal, letterlijk op de drempel van 046.",
        betekenis="Jaarlijkse rathyatra (wagenprocessie) in juni/juli, gelijktijdig met het "
        "festival van de Jagannath-tempel in Puri.",
        ervaart="Een actieve tempel met dagelijkse Mahaprasad-uitdeling (12.00-14.00u, "
        "rijst/linzen/groenten/papadum door de week, khichdi op zaterdag).",
        onderscheidend="Geen andere kandidaat in dit rapport ligt zo dicht bij 046 met een eigen, "
        "andere traditie.",
        bezoektijd="NOG NIET ONDERZOCHT",
        combineer="Direct naast 046, geen extra reisinspanning.",
        tips="GEVERIFIEERD specifiek voor deze tempel (niet afgeleid van de Jagannath-tempel in "
        "Puri): de officiele Bihar Tourism-pagina noemt GEEN religie- of "
        "nationaliteitsgebonden toegangsbeperking. Beste bezoekperiode: september-april.",
        overslaan="Geen directe biografische link met Boeddha's verlichting.",
        onzekerheden="Het ontbreken van een vermelde beperking is geen absolute garantie, maar is "
        "wel een directe, tempel-specifieke bevinding.",
    ),
    dict(
        nr="074", naam="International Meditation Centre / Dhamma Bodhi", hook="eerste Vipassana-cursus van Bihar",
        cluster="Studie/retraite", mark_status="OPEN",
        twijfel="Twijfelgeval: niet uitgesloten omdat \"eerste Vipassana-cursus van heel Bihar\" "
        "(1970) een reele historische primeur is -- maar toegang is uitsluitend via volledige "
        "cursusinschrijving; een gewoon dagbezoek is hier, anders dan bij 053, geen optie.",
        wat_is_het="Een Vipassana-meditatiecentrum in de traditie van S.N. Goenka. Het formele "
        "centrum \"Dhamma Bodhi\" werd gesticht in 1994 (10 acres grond), met een Dhamma-hal voor "
        "100 studenten en een pagode met 70 cellen.",
        waarom="De eerste 10-daagse Vipassana-cursus van heel Bihar werd hier al in 1970 gehouden, "
        "in het naburige Samanvaya Ashram vlak bij de Mahabodhi-tempel.",
        betekenis="Andere traditie/lijn dan Root Institute (Tibetaans-boeddhistisch) -- "
        "Theravada-afgeleide, seculiere Vipassana-techniek.",
        ervaart="Sinds 2008 ook langere cursussen naast de standaard 10-daagse -- een omvangrijk, "
        "gevestigd meditatie-instituut.",
        onderscheidend="Historische primeur (eerste Vipassana-cursus van Bihar) en een eigen, "
        "herkenbare traditie (Goenka-Vipassana).",
        bezoektijd="NOG NIET ONDERZOCHT",
        combineer="Ontstaan bij het Samanvaya Ashram, vlak bij Mahabodhi (046).",
        tips="GECONTROLEERD: de officiele centrumbron beschrijft uitsluitend de residentiele "
        "10-daagse (en langere) cursussen, met vooraf-inschrijving en een vaste capaciteit (120 "
        "mannen, 80 vrouwen). GEEN dagbezoek, terreinbezichtiging of los verblijf zonder cursus "
        "vermeld.",
        overslaan="Zeer afhankelijk van of Mark tijd/interesse heeft voor een volledige "
        "Vipassana-cursus (minimaal 10 dagen) -- een kort of los bezoek is, voor zover bekend, "
        "geen optie hier.",
        onzekerheden="Een niet-deelnemende bezoeker heeft vermoedelijk geen toegang.",
    ),
    dict(
        nr="077", naam="Bitho Sharif Dargah", hook="soefi-heiligdom, signaleringszone",
        cluster="Signaleringszone", mark_status="OPEN",
        twijfel="Twijfelgeval: niet uitgesloten omdat een regionaal significant jaarlijks "
        "Urs-festival (naar verluidt bijgewoond door de zittende minister-president van Bihar) "
        "een reeel, bovenlokaal signaal is -- maar er is geen officiele bron, en de plek ligt "
        "buiten de volledig onderzochte kernstraal.",
        wat_is_het="Een soefi-heiligdom (Khanqah-e-Ashrafia) in het dorp Bitho, gesticht 1443 CE "
        "door Hazrat Makhdoom Syed Shah Durwesh Ashraf, met een moskee en een school op een "
        "terrein van circa 6-7 acres. Circa 20-25 km vanaf Bodh Gaya (20-30 km-signaleringszone, "
        "niet de volledig onderzochte 0-20 km-kernstraal).",
        waarom="Vertegenwoordigt een traditie (soefi-islam) die anders volledig afwezig is in de "
        "hele regio.",
        betekenis="Bekend om genezingsverhalen en als symbool van hindoe-moslim-eenheid; "
        "jaarlijkse driedaagse Urs-viering (10-12 Shaban) met Qawwali's, naar verluidt bijgewoond "
        "door de zittende minister-president van Bihar.",
        ervaart="Een actief heiligdom met een jaarlijks festival (Urs), moskee en schoolterrein.",
        onderscheidend="Enige soefi-/islamitische vertegenwoordiging binnen signaleringsbereik.",
        bezoektijd="NOG NIET ONDERZOCHT",
        combineer="Nog niet onderzocht -- signaleringszone, geen routegegevens verzameld.",
        tips="Sufi-heiligdommen staan in India in het algemeen bekend als doorgaans toegankelijk "
        "voor bezoekers van alle religies -- dit is een algemeen gegeven, GEEN specifiek "
        "bevestigd toegangsbeleid voor deze exacte plek.",
        overslaan="Buiten de kernstraal, extra reisinspanning; alleen relevant als Mark specifiek "
        "geinteresseerd is in interreligieuze/soefi-geschiedenis.",
        onzekerheden="Geen officiele overheidsbron gevonden; exacte afstand is een berekende "
        "schatting, geen bevestigd coordinaat.",
    ),
    dict(
        nr="078", naam="Gurdwara Sri Guru Tegh Bahadur Ji, Gaya", hook="waar twee Sikh-Guru's de pind-daan-praktijk bekritiseerden",
        cluster="Gaya-stad", mark_status="OPEN",
        twijfel="Twijfelgeval: niet uitgesloten omdat een overgeleverd bezoek van twee Sikh-Guru's "
        "met een specifieke, inhoudelijke leerstelling op deze exacte plek een reeel signaal is -- "
        "maar dit steunt uitsluitend op Sikh-eigen historiografie (SikhiWiki), niet op een "
        "academische of primaire bron.",
        wat_is_het="Een gurdwara nabij Vishnupad Temple (051), aan de Falgu-rivier, beheerd door "
        "Udasi-priesters (een Sikh-gerelateerde ordetraditie).",
        waarom="Volgens de Sikh-traditie bezochten zowel Guru Nanak Dev als later Guru Tegh "
        "Bahadur deze plek en bekritiseerden er direct de pind-daan-praktijk.",
        betekenis="Zij onderwezen dat iemands eigen goede daden tijdens het leven bepalend zijn "
        "voor het lot van de ziel, niet de rituelen die nakomelingen na de dood laten uitvoeren -- "
        "een inhoudelijke tegenstem, precies op de plek waar die praktijk het meest "
        "geconcentreerd voorkomt.",
        ervaart="Drie exemplaren van de Siri Guru Granth Sahib (Gurmukhi en Devnagri schrift) "
        "naast elkaar, in een rechthoekig paviljoen op een verhoogd platform.",
        onderscheidend="Enige Sikh-vertegenwoordiging in de hele straal, met een overgeleverd "
        "tweevoudig Guru-bezoek en een specifieke leerstelling op deze exacte plek.",
        bezoektijd="NOG NIET ONDERZOCHT",
        combineer="Zelfde bredere Gaya-stad-zone als 051, 070, 071.",
        tips="Actieve, publiek toegankelijke gurdwara.",
        overslaan="Geen directe koppeling aan Marks Kriya-/boeddhistische focus.",
        onzekerheden="Geen officiele overheidsbron gevonden; het historische Guru-bezoek zelf "
        "steunt uitsluitend op Sikh-eigen historiografie (SikhiWiki), niet op een onafhankelijke "
        "academische of primaire bron.",
    ),
]

KEUZEHULP = {
    "046": "Bestaande keuze: A -- de verlichting zelf",
    "047": "Bestaande keuze: A -- waar de Middenweg begon",
    "048": "Bestaande keuze: A -- de zes jaar ascese",
    "049": "Bestaande keuze: A -- modern eerbetoon",
    "050": "Door Mark te beoordelen -- originele Bodhi-boom-omheining",
    "051": "Door Mark te beoordelen -- voetspoor van Vishnu + Akshayavat, Gaya-stad",
    "052": "Door Mark te beoordelen -- Karmapa-klooster, evenementafhankelijk",
    "058": "TWIJFELGEVAL -- vredespagode-stichter Fujii",
    "060": "TWIJFELGEVAL -- Nyingma, genoemd door Dalai Lama + Pema Norbu Rinpoche",
    "061": "TWIJFELGEVAL -- pionierklooster, rieten Boeddhabeeld",
    "062": "Door Mark te beoordelen -- organisatie achter herstel van 046",
    "063": "TWIJFELGEVAL -- nieuw Nyingma-complex, toegang buiten festival onbevestigd",
    "068": "TWIJFELGEVAL -- Shechen-lijn, Dilgo Khyentse Rinpoche",
    "070": "Door Mark te beoordelen -- Shakti Peeth, 1 van de 18 in heel India",
    "071": "Door Mark te beoordelen -- pind-daan-heuvel, Yama-tempel",
    "072": "Door Mark te beoordelen -- waar Boeddha de Vuurpreek hield",
    "073": "TWIJFELGEVAL -- Krishna-tempel 25 voet van Mahabodhi",
    "074": "TWIJFELGEVAL -- eerste Vipassana-cursus van Bihar, alleen via volledige cursus",
    "077": "TWIJFELGEVAL -- soefi-heiligdom, signaleringszone (20-25 km)",
    "078": "TWIJFELGEVAL -- Sikh-Guru-bezoek, alleen Sikh-eigen bron",
}

CLUSTER_INTRO = {
    "Kerncluster": "Kerncluster -- samen te combineren, korte afstand lopend (bestaande Mark-keuze: A)",
    "Aanvullend": "Aanvullende rit -- eigen tijd nodig, blijft kernwaardig (bestaande Mark-keuze: A)",
    "Optioneel": "Optionele plek -- dichtbij, niet kernwaardig (bestaande Mark-keuze: A)",
    "Bij Mahabodhi": "Direct bij/naast het hoofdcomplex -- door Mark te beoordelen",
    "Gaya-stad": "Gaya-stad: hindoeisme en sikhisme -- door Mark te beoordelen",
    "Studie/retraite": "Boeddhistische studie- en retraitecentra -- door Mark te beoordelen",
    "Internationale kloosters": "Internationale kloosters -- door Mark te beoordelen (bevat meerdere twijfelgevallen)",
    "Boeddha-biografie na de verlichting": "Na de verlichting: het onderwijs begint -- door Mark te beoordelen",
    "Signaleringszone": "Signaleringszone (20-30 km) -- door Mark te beoordelen",
}
CLUSTER_ORDER = [
    "Kerncluster", "Aanvullend", "Optioneel", "Bij Mahabodhi", "Gaya-stad", "Studie/retraite",
    "Internationale kloosters", "Boeddha-biografie na de verlichting", "Signaleringszone",
]


def candidate_block(story, c):
    story.append(Marker(c["nr"]))
    story.append(Paragraph(f"{c['nr']} {c['naam']}{(' -- ' + c['hook']) if c['hook'] else ''}", styles["CandTitle"]))
    if c["mark_status"] == "A":
        story.append(Paragraph("Bestaande Mark-keuze: A", styles["StatusA"]))
    elif c["twijfel"]:
        story.append(Paragraph("DOOR MARK TE BEOORDELEN -- TWIJFELGEVAL", styles["StatusTwijfel"]))
    else:
        story.append(Paragraph("DOOR MARK TE BEOORDELEN", styles["StatusOpen"]))

    if c["twijfel"]:
        story.append(Paragraph(c["twijfel"], styles["Twijfel"]))

    story.append(Paragraph("Wat is het?", styles["SubHead"]))
    story.append(Paragraph(c["wat_is_het"], styles["Body"]))
    story.append(Paragraph("Waarom hier naartoe?", styles["SubHead"]))
    story.append(Paragraph(c["waarom"], styles["Body"]))
    story.append(Paragraph("Spirituele / historische betekenis", styles["SubHead"]))
    story.append(Paragraph(c["betekenis"], styles["Body"]))
    story.append(Paragraph("Wat ervaart Mark concreet?", styles["SubHead"]))
    story.append(Paragraph(c["ervaart"], styles["Body"]))
    story.append(Paragraph(c["onderscheidend"], styles["Bijzonder"]))
    story.append(Paragraph("Goed te combineren met", styles["SubHead"]))
    story.append(Paragraph(c["combineer"], styles["Body"]))
    story.append(Paragraph("Praktische bezoekbaarheid", styles["SubHead"]))
    story.append(Paragraph(c["tips"], styles["Body"]))
    story.append(Paragraph("Reden om eventueel over te slaan", styles["SubHead"]))
    story.append(Paragraph(c["overslaan"], styles["Body"]))
    story.append(Paragraph("Belangrijke feitelijke onzekerheden", styles["SubHead"]))
    story.append(Paragraph(c["onzekerheden"], styles["Onzeker"]))

    story.append(Spacer(1, 0.12 * cm))
    story.append(HRFlowable(width="100%", thickness=0.4, color=colors.HexColor("#cccccc")))
    status_text = "A (vastgelegd, zie MARK_DECISIONS_2026-08-05.jsonl)" if c["mark_status"] == "A" else "DOOR_MARK_TE_BEOORDELEN"
    story.append(Paragraph(
        f"<b>Technisch:</b> candidate_id BGY-CAND-{c['nr']} | Mark-status: {status_text}",
        styles["TechBlock"]))
    story.append(Spacer(1, 0.45 * cm))


def build_body(story):
    current_cluster = None
    for c in CANDIDATES:
        if c["cluster"] != current_cluster:
            current_cluster = c["cluster"]
            story.append(Paragraph(CLUSTER_INTRO[current_cluster], styles["ClusterHead"]))
        candidate_block(story, c)
    story.append(PageBreak())
    story.append(Paragraph("Slot", styles["SectionHead"]))
    story.append(Paragraph(
        "046-049 zijn een vastgelegd Mark-besluit (alle vier A) en worden niet opnieuw ter keuze "
        "voorgelegd. De overige 16 kandidaten in dit document zijn permanent genummerd, volledig "
        "onderzocht en wachten op Mark's A/B/C -- negen daarvan zijn expliciet als twijfelgeval "
        "gemarkeerd (zie de rode kanttekening bij die kandidaten): een reeel maar betwistbaar "
        "zwaartesignaal, bewust niet zelfstandig door CCI beslist. Andere, eerder onderzochte "
        "locaties bleken bij nadere toetsing niet zelfstandig onderscheidend genoeg en zijn niet "
        "in dit document opgenomen; hun nummers blijven permanent gereserveerd. Voor de volledige "
        "technische onderbouwing: zie GOUD/MARK_SELECTION_REPORT.md in deze run. Geen route, geen "
        "nachten, geen hotel/ashram en geen pacing zijn onderdeel van dit document.", styles["TechBlock"]))


def build_cover(story):
    story.append(Spacer(1, 4.5 * cm))
    story.append(Paragraph("Bodh Gaya", styles["CoverTitle"]))
    story.append(Paragraph("Keuze-reisgids", styles["CoverSub"]))
    story.append(Paragraph("run_id: BODHGAYA-DISCOVERY-001 | protocol: governance/SWEEP_PROTOCOL.md", styles["CoverSub"]))
    story.append(Spacer(1, 1 * cm))
    story.append(Paragraph(
        "Leeswijzer -- Dit is een reisgids, geen technisch validatierapport. Elke locatie "
        "beschrijft wat het is, waarom de plek de moeite waard is, wat Mark er concreet ervaart, "
        "hoe onderscheidend het is en hoe die te combineren is met andere plekken in de buurt. "
        "De volledige technische onderbouwing staat NIET in dit document, maar in "
        "GOUD/MARK_SELECTION_REPORT.md in dezelfde run. Elke locatie heeft hier wel een klein "
        "technisch blok onderaan, uitsluitend ter referentie.", styles["Body"]))
    story.append(Paragraph(
        "Waar keuze-informatie ontbreekt staat expliciet \"NOG NIET ONDERZOCHT\" in plaats van een "
        "verzonnen antwoord. Negen kandidaten zijn gemarkeerd als TWIJFELGEVAL: een reeel maar "
        "betwistbaar zwaartesignaal (bijvoorbeeld een naamgenoemde belangrijke persoon, een "
        "jaarlijks festival, of een historische primeur) dat niet zelfstandig door CCI is "
        "afgewezen of goedgekeurd -- die keuze is uitdrukkelijk aan Mark.", styles["Body"]))
    story.append(Paragraph(
        "046-049 zijn een vastgelegd Mark-besluit (alle vier A, zie "
        "MARK_DECISIONS_2026-08-05.jsonl) en worden hier uitsluitend ter referentie getoond, niet "
        "opnieuw ter keuze voorgelegd. De overige 16 kandidaten staan open voor Mark's A/B/C -- "
        "dit document geeft geen voorspelde A/B/C-adviezen en bevat geen route, nachten, "
        "hotel/ashram of pacing.", styles["Body"]))
    story.append(PageBreak())


def build_index(story, page_lookup):
    story.append(Paragraph("Keuze-index", styles["SectionHead"]))
    story.append(Paragraph(
        f"Alle {len(CANDIDATES)} kandidaten in een oogopslag. Groen = bestaande Mark-keuze A, "
        "grijs = door Mark te beoordelen, rood = twijfelgeval (door Mark te beoordelen, met een "
        "reeel maar betwistbaar zwaartesignaal).", styles["Body"]))
    head = lambda s: Paragraph(s, styles["CellHead"])
    data = [[head("Nr."), head("Naam"), head("Cluster"), head("Status"), head("Keuzehulp in een zin"), head("Pag.")]]
    for c in CANDIDATES:
        if c["mark_status"] == "A":
            status_style, status = styles["CellGreen"], "A"
        elif c["twijfel"]:
            status_style, status = styles["CellRed"], "twijfel"
        else:
            status_style, status = styles["CellOrange"], "open"
        pag = str(page_lookup.get(c["nr"], "-"))
        data.append([
            Paragraph(c["nr"], styles["CellText"]),
            Paragraph(c["naam"], styles["CellText"]),
            Paragraph(c["cluster"], styles["CellText"]),
            Paragraph(status, status_style),
            Paragraph(KEUZEHULP[c["nr"]], styles["CellText"]),
            Paragraph(pag, styles["CellText"]),
        ])
    t = Table(data, colWidths=[1.0 * cm, 4.3 * cm, 2.5 * cm, 2.0 * cm, 5.9 * cm, 1.1 * cm], repeatRows=1)
    style_cmds = [
        ("BACKGROUND", (0, 0), (-1, 0), colors.HexColor("#7a3b12")),
        ("GRID", (0, 0), (-1, -1), 0.5, colors.HexColor("#cccccc")),
        ("VALIGN", (0, 0), (-1, -1), "MIDDLE"),
        ("ROWBACKGROUNDS", (0, 1), (-1, -1), [colors.white, colors.HexColor("#f7f0e8")]),
        ("TOPPADDING", (0, 0), (-1, -1), 3),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 3),
    ]
    t.setStyle(TableStyle(style_cmds))
    story.append(t)
    story.append(Spacer(1, 0.3 * cm))
    story.append(Paragraph(
        "Legenda: \"A\" = vastgelegd Mark-besluit (niet opnieuw ter keuze). \"open\" = "
        "DOOR_MARK_TE_BEOORDELEN, permanent genummerd en volledig onderzocht. \"twijfel\" = "
        "DOOR_MARK_TE_BEOORDELEN met een expliciete twijfelgeval-kanttekening.", styles["Body"]))
    story.append(PageBreak())


def make_doc(path, page_lookup):
    story = []
    build_cover(story)
    build_index(story, page_lookup)
    build_body(story)
    doc = SimpleDocTemplate(
        path, pagesize=A4,
        leftMargin=2 * cm, rightMargin=2 * cm, topMargin=2 * cm, bottomMargin=2 * cm,
        title="Bodh Gaya -- Keuze-reisgids", author="CCI / governance/SWEEP_PROTOCOL.md",
    )
    doc.build(story)


if __name__ == "__main__":
    import os
    os.makedirs(os.path.dirname(TMP), exist_ok=True)

    # Pass 1: placeholder index (zelfde rijaantal/opmaak) om echte paginanummers te bepalen.
    page_map.clear()
    make_doc(TMP, {})
    pass1_map = dict(page_map)

    # Pass 2: definitieve PDF met de juiste paginanummers in de index.
    page_map.clear()
    make_doc(OUT, pass1_map)

    print("OK, written", OUT)
    print("page map:", pass1_map)
