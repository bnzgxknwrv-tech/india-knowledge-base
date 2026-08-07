#!/usr/bin/env python3
"""Bouwt de Bodh Gaya-keuze-reisgids-PDF voor 046-058, in het Varanasi-reisgidsformaat
(VARANASI_40_KEUZE_REISGIDS.pdf als visueel/inhoudelijk model). Geen nieuw onderzoek --
uitsluitend bestaande, al goedgekeurde brondata uit MARK_SELECTION_REPORT.md,
BODHGAYA_GOUD_REPORT.md, MARK_DECISIONS_2026-08-05.jsonl en DISCOVERY_CANDIDATES.jsonl.

046-049: bestaande Mark-keuze A (LOCKED, niet opnieuw ter keuze).
050-058: DOOR MARK TE BEOORDELEN.

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

OUT = "runs/active/BODHGAYA-DISCOVERY-001/GOUD/USER/BODHGAYA_046_058_KEUZE_REISGIDS.pdf"
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
styles.add(ParagraphStyle("TechBlock", parent=styles["Normal"], fontSize=7.6, leading=10.3, textColor=colors.HexColor("#555555")))
styles.add(ParagraphStyle("ClusterHead", parent=styles["Heading2"], fontSize=13, spaceBefore=14, spaceAfter=6, textColor=colors.HexColor("#7a3b12")))
styles.add(ParagraphStyle("StatusA", parent=styles["Normal"], fontSize=10, spaceAfter=6, textColor=colors.HexColor("#1f5c1f"), fontName="Helvetica-Bold"))
styles.add(ParagraphStyle("StatusOpen", parent=styles["Normal"], fontSize=10, spaceAfter=6, textColor=colors.HexColor("#a05a00"), fontName="Helvetica-Bold"))
styles.add(ParagraphStyle("CellText", parent=styles["Normal"], fontSize=8.0, leading=9.6))
styles.add(ParagraphStyle("CellHead", parent=styles["Normal"], fontSize=8.3, leading=10, textColor=colors.white, fontName="Helvetica-Bold"))
styles.add(ParagraphStyle("CellGreen", parent=styles["Normal"], fontSize=8.0, leading=9.6, textColor=colors.HexColor("#1f5c1f"), fontName="Helvetica-Bold"))
styles.add(ParagraphStyle("CellOrange", parent=styles["Normal"], fontSize=8.0, leading=9.6, textColor=colors.HexColor("#a05a00"), fontName="Helvetica-Bold"))

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
# BODHGAYA_GOUD_REPORT.md / DISCOVERY_CANDIDATES.jsonl. Geen nieuw onderzoek.
# ---------------------------------------------------------------------------

CANDIDATES = [
    dict(
        nr="046", naam="Mahabodhi Temple Complex", hook="de plek van de verlichting zelf",
        cluster="Kerncluster", mark_status="A",
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
        ervaart="Het 50 meter hoge tempelgebouw, de eeuwenoude boom, monniken en pelgrims uit de "
        "hele boeddhistische wereld, votiefstoepa's rondom -- een levend, dagelijks bezocht "
        "heiligdom, geen stil monument.",
        onderscheidend="Een van de vier belangrijkste boeddhistische pelgrimsplaatsen ter wereld, "
        "en de enige plek die de verlichting zelf markeert.",
        bezoektijd="NOG NIET ONDERZOCHT",
        combineer="047 Sujata Stupa (circa 20 minuten lopen, inclusief oversteek Phalgu-rivier).",
        tips="Dagelijks vrij toegankelijk, geen inschrijving of speciale toegang nodig.",
        overslaan="Geen reden om over te slaan -- dit is de ankerplek van de hele regio.",
        onzekerheden="Exacte locatie van Sri Yukteswars sannyas-initiatie (1906) binnen Bodh Gaya "
        "niet vastgesteld. De Muchalinda-vijver binnen het complex heeft mogelijk een tweede, "
        "gelijknamige plek in het dorp Mocharim (circa 1 km zuid) -- geen bron bevestigt de "
        "relatie tussen beide; dit vraagt geen actie tijdens een regulier bezoek.",
        geo_status="CONFIRMED", coord_text="24.6959222N, 84.9914193E (rechtstreekse Google Maps/Earth-marker)",
        checked_at="2026-08-05",
    ),
    dict(
        nr="047", naam="Sujata Stupa, Bakraur", hook="waar de Middenweg begon",
        cluster="Kerncluster", mark_status="A",
        wat_is_het="Een archeologisch stoepacomplex (oorspronkelijke bouw 2e eeuw v.Chr., latere "
        "uitbreidingsfase 8e-10e eeuw CE) op de plek waar Sujata, een dorpsvrouw uit Bakraur, "
        "Boeddha een kom rijstpudding aanbood.",
        waarom="Bezoek de exacte plek waar een dorpsvrouw Boeddha's leven een beslissende wending "
        "gaf.",
        betekenis="Deze gebeurtenis beeindigde Boeddha's zesjarige extreme ascese en leidde "
        "rechtstreeks tot zijn ontdekking van de Middenweg -- een kernleerstuk van het "
        "boeddhisme, geen zijdelings detail.",
        ervaart="Een tastbaar, gedateerd monument op de exacte plek van deze gebeurtenis, circa 20 "
        "minuten lopen van het hoofdcomplex, rustiger en minder toeristisch.",
        onderscheidend="Onvervangbaar: de enige plek die deze specifieke, verhaalbepalende "
        "gebeurtenis markeert -- complementair aan zowel Mahabodhi (de verlichting zelf) als "
        "Dungeshwari (de ascese die voorafging), geen overlap.",
        bezoektijd="NOG NIET ONDERZOCHT",
        combineer="046 Mahabodhi Temple Complex (circa 1,2 km, eenvoudig te combineren op dezelfde "
        "dag).",
        tips="Vereist een korte oversteek van de Phalgu-rivier vanaf Bodh Gaya.",
        overslaan="Geen duidelijke reden om over te slaan -- complementair aan 046 en 048.",
        onzekerheden="Geen open onzekerheden meer; een eerder gemeld drievoudig "
        "coordinaatconflict is opgelost via rechtstreekse Google Maps/Earth-bevestiging "
        "(inclusief Google Plus Code M2X3+58W).",
        geo_status="CONFIRMED", coord_text="24.6979887N, 85.0033228E (rechtstreekse Google Maps/Earth-marker, Plus Code M2X3+58W)",
        checked_at="2026-08-05",
    ),
    dict(
        nr="048", naam="Dungeshwari Cave Temples (Mahakala Caves)", hook="de grotten van de zes jaar ascese",
        cluster="Aanvullend", mark_status="A",
        wat_is_het="Rotsgehouwen grottempels (5e-6e eeuw CE) op de plek waar Boeddha zes jaar "
        "extreme ascese beoefende voor hij naar Bodh Gaya afdaalde voor de uiteindelijke "
        "verlichting.",
        waarom="Ga naar de plek waar Boeddha, voor zijn verlichting, zichzelf tot op het bot "
        "uithongerde op zoek naar waarheid.",
        betekenis="Het spiegelbeeld-verhaal van Sujata's aanbieding -- de ascese die eraan "
        "voorafging. Genoemd door de 7e-eeuwse Chinese pelgrim Xuanzang in zijn reisverslag. Een "
        "van de grotten bevat een gouden beeld van de uitgemergelde Boeddha.",
        ervaart="Rustige rotsgrotten in de heuvels, ver van de drukte van het hoofdcomplex, met het "
        "aangrijpende uitgemergelde-Boeddhabeeld als middelpunt.",
        onderscheidend="Onvervangbaar: geen andere plek toont dit specifieke moment.",
        bezoektijd="NOG NIET ONDERZOCHT",
        combineer="Eigen rit nodig; niet zonder meer op dezelfde ochtend te combineren met de "
        "kerncluster.",
        tips="Circa 12-14 km van Bodh Gaya (bronnen varieren), vereist een aparte rit per taxi of "
        "auto-riksja.",
        overslaan="Geen duidelijke reden om over te slaan qua inhoud -- toont een uniek moment dat "
        "nergens anders getoond wordt; wel de grootste reisinspanning van de kerngroep.",
        onzekerheden="Geen bevestigde Google Maps-marker gevonden ondanks vijf zoekpogingen over "
        "twee ZILVER-rondes -- identiteit blijft wel eenduidig bevestigd via twee onafhankelijke "
        "overheidsbronnen en de dorpsnaam Larpur.",
        geo_status="GOOGLE_MAPS_MARKER_NOT_CONFIRMED", coord_text="geen bevestigde marker gevonden -- geen coordinaat geraden",
        checked_at="2026-08-05",
    ),
    dict(
        nr="049", naam="Great Buddha Statue", hook="het grootste Boeddhabeeld van India",
        cluster="Optioneel", mark_status="A",
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
        overslaan="Geen onderdeel van Boeddha's eigen biografische verhaal -- wie voorrang geeft "
        "aan de kernverhalen mist hierdoor geen gat in het verlichtingsverhaal.",
        onzekerheden="Geen bevestigde Google Maps-marker; de gebruikte afstand tot 046 is "
        "gebaseerd op een niet-bevestigd Wikipedia-infobox-coordinaat, niet op een geverifieerde "
        "marker. Hoogte van het beeld zelf is intern inconsistent tussen bronnen (18,5 m vs. 20 m).",
        geo_status="GOOGLE_MAPS_MARKER_NOT_CONFIRMED", coord_text="geen bevestigde marker gevonden -- geen coordinaat geraden",
        checked_at="2026-08-05",
    ),
    dict(
        nr="050", naam="Archaeological Museum of Bodh Gaya (ASI)", hook="de originele Bodhi-boom-omheining",
        cluster="Naast 046", mark_status="OPEN",
        wat_is_het="Een door de Archaeological Survey of India beheerd museum (opgericht 1956), "
        "direct naast het Mahabodhi-complex.",
        waarom="Bekijk de ORIGINELE stenen balustrade-fragmenten die ooit de Bodhi-boom zelf "
        "omsloten (Sunga-periode, circa 2e eeuw v.Chr.) -- geen replica, maar een direct fysiek "
        "object uit de kernplek van de verlichting.",
        betekenis="Er is geen ander museum met objecten die direct van de Bodhi-boom-omheining "
        "zelf afkomstig zijn -- uniek in zijn soort binnen Bodh Gaya.",
        ervaart="Gereconstrueerde stenen balustrade, reliefs, Pala-periode sculpturen, munten uit "
        "de Mughal-, Maurya- en Gupta-periode, in twee galerijen en een open binnenplaats.",
        onderscheidend="Voor zover onderzocht het enige museum ter plekke met objecten "
        "rechtstreeks afkomstig van de Bodhi-boom-omheining zelf.",
        bezoektijd="NOG NIET ONDERZOCHT",
        combineer="046 Mahabodhi Temple Complex (grenst direct aan het complex).",
        tips="Regulier entreekaartje, geen speciale toegang of inschrijving nodig.",
        overslaan="Geen levende praktijk en geen directe biografische link met de verlichting zelf "
        "-- een museale, archeologische aanvulling op 046, geen zelfstandig verhaal.",
        onzekerheden="Geen gemeld.",
        geo_status="GOOGLE_MAPS_MARKER_NOT_CONFIRMED", coord_text="nog geen BRONS/ZILVER-GEO-stap doorlopen",
        checked_at="2026-08-05",
    ),
    dict(
        nr="051", naam="Vishnupad Temple, Gaya", hook="het voetspoor van Vishnu",
        cluster="Gaya-stad", mark_status="OPEN",
        wat_is_het="Een actieve hindoetempel aan de Falgu-rivier in Gaya-stad (circa 12-15 km van "
        "Bodh Gaya), met een 40 cm lange voetafdruk in zwart basaltgesteente, vereerd als het "
        "voetspoor van Vishnu.",
        waarom="Een singulier, fysiek uniek relict (geen generiek Vishnu-beeld), en een van de "
        "belangrijkste plekken in heel India voor Pind Daan (voorouder-verlossingsrituelen).",
        betekenis="Volgens overlevering bevrijdt een Pind Daan hier voorouders tot veertien "
        "generaties terug. Toegangsregel, gecorrigeerd na gerichte controle: meerdere "
        "onafhankelijke reisbronnen melden consistent dat niet-hindoes de tempel zelf niet mogen "
        "betreden (vergelijkbaar met de bekendere regel bij Jagannath Temple, Puri) -- geen "
        "officiele bron bevestigt of ontkent dit expliciet.",
        ervaart="Als niet-hindoe vermoedelijk GEEN toegang tot het tempelinterieur/het voetspoor "
        "zelf -- wel de omliggende straatjes, de buitenkant van de tempel, en de drukte van een "
        "actieve, levende bedevaartsplek eromheen.",
        onderscheidend="Geen andere plek in de straal heeft dit specifieke relict of deze "
        "specifieke, eeuwenoude rituele functie -- al is het relict zelf voor een niet-hindoe "
        "bezoeker vermoedelijk niet rechtstreeks te zien.",
        bezoektijd="NOG NIET ONDERZOCHT",
        combineer="NOG NIET ONDERZOCHT (eigen stad, circa 12-15 km van de Bodh Gaya-kerncluster, "
        "geen combinatie-informatie onderzocht).",
        tips="Drukst tijdens Pitru Paksha (september); de omgeving is permanent toegankelijk. Het "
        "tempelinterieur is voor een niet-hindoe bezoeker vermoedelijk NIET toegankelijk (zie "
        "hierboven).",
        overslaan="Geen directe koppeling aan Marks eigen Kriya-/boeddhistische focus, en het "
        "tempelinterieur zelf is voor een niet-hindoe bezoeker vermoedelijk niet toegankelijk -- "
        "wie strikt bij het boeddhistische verlichtingsverhaal wil blijven, kan dit overslaan.",
        onzekerheden="De toegangsbeperking voor niet-hindoes steunt op consistente reisbronnen, "
        "niet op een officiele bevestiging.",
        geo_status="GOOGLE_MAPS_MARKER_NOT_CONFIRMED", coord_text="nog geen BRONS/ZILVER-GEO-stap doorlopen",
        checked_at="2026-08-06",
    ),
    dict(
        nr="052", naam="Tergar Monastery", hook="het Karmapa-klooster",
        cluster="Studie/retraite", mark_status="OPEN",
        wat_is_het="Een Karma-Kagyu-klooster/studie-instituut, gesticht door Yongey Mingyur "
        "Rinpoche (grond geschonken door Tai Situ Rinpoche in 2000, gebouw voltooid 2006), met "
        "ruim 300 monniken.",
        waarom="Periodieke (doorgaans jaarlijkse) gastheer van het Kagyu Monlam-gebedsfestival "
        "onder leiding van de 17e Karmapa, een van de hoogste gezagsdragers binnen het Tibetaans "
        "boeddhisme.",
        betekenis="Enige klooster in Bodh Gaya met een directe, periodieke aanwezigheid van de "
        "Karmapa zelf.",
        ervaart="Buiten het festival: een actief studieklooster, monniken in studie/meditatie. "
        "Tijdens het Monlam: een grote internationale samenkomst met de Karmapa zelf. "
        "Datumcorrectie: de exacte data volgen de Tibetaanse maankalender, niet een vaste "
        "Gregoriaanse maand. Bevestigde meest recente editie: 40e Kagyu Monlam Chenmo, 23 "
        "december 2025 -- 3 januari 2026. Datum volgende editie: ONBEKEND, nog niet gepubliceerd.",
        onderscheidend="Enige klooster met een directe, periodieke Karmapa-aanwezigheid.",
        bezoektijd="NOG NIET ONDERZOCHT",
        combineer="NOG NIET ONDERZOCHT.",
        tips="Kloostergebouw permanent aanwezig; bezoekbaarheid buiten het festivalseizoen is "
        "onzeker -- geen bevestigde publieke bezoekersprogramma's buiten het festival gevonden. "
        "Exacte datum eerstvolgende editie nog niet gepubliceerd.",
        overslaan="De sterkste reden om te komen (Karmapa/Monlam) is evenement- en "
        "seizoensafhankelijk, met een datum die niet ver vooraf vaststaat; buiten die periode is "
        "het een regulier studieklooster.",
        onzekerheden="Bezoekbaarheid buiten het festivalseizoen niet bevestigd. Datum "
        "eerstvolgende editie nog niet gepubliceerd (ONBEKEND).",
        geo_status="GOOGLE_MAPS_MARKER_NOT_CONFIRMED", coord_text="nog geen BRONS/ZILVER-GEO-stap doorlopen",
        checked_at="2026-08-06",
    ),
    dict(
        nr="053", naam="Root Institute (FPMT)", hook="meerdaags meditatieprogramma",
        cluster="Studie/retraite", mark_status="OPEN",
        wat_is_het="Een retraitecentrum van de Foundation for the Preservation of the Mahayana "
        "Tradition (FPMT), gesticht in 1984 door Lama Thubten Yeshe en Lama Thubten Zopa "
        "Rinpoche, 15 minuten lopen van het hoofdcomplex.",
        waarom="Lama Yeshe beschouwde Bodh Gaya als \"de wortel waaruit de takken van het "
        "boeddhisme zich over de rest van de wereld verspreidden\". Correctie na officiele bron "
        "(rootinstitute.ngo): vier afzonderlijke manieren om hier te komen, niet alleen 'met of "
        "zonder cursus' -- (1) een gratis dagbezoek aan de tuinen tijdens openingstijden "
        "(doorgaans 9.00-17.00u), (2) dagelijkse meditatiesessies open voor iedereen, (3) een "
        "gewoon verblijf zonder cursus (geen hotel, wel accommodatie tegen betaling, met "
        "inachtneming van de kloosterprecepten), en (4) de residentiele meditatiecursus zelf.",
        betekenis="Het instituut biedt zowel vrij toegankelijke tuinen en dagelijkse "
        "meditatiesessies, gewoon verblijf zonder cursus, als een doorlopend programma van "
        "residentiele meditatiecursussen (circa 10 dagen, oktober-maart).",
        ervaart="Van een kort, gratis dagbezoek aan de tuinen en de dagelijkse meditatiesessies, "
        "tot een gewoon verblijf zonder cursus, tot een meerdaags, begeleid meditatieprogramma -- "
        "zie de vier opties hierboven.",
        onderscheidend="Onder de onderzochte kandidaten de enige plek met zowel vrij "
        "dagbezoek/gewoon verblijf als een gestructureerd (tegen inschrijving) meerdaags "
        "meditatieprogramma voor buitenstaanders.",
        bezoektijd="NOG NIET ONDERZOCHT",
        combineer="15 minuten lopen van het hoofdcomplex (046).",
        tips="Dagbezoek, tuinen, dagelijkse meditatiesessies en een gewoon verblijf zonder cursus "
        "zijn het hele jaar mogelijk; alleen de residentiele, begeleide cursus zelf is "
        "programma- en seizoensafhankelijk (oktober-maart, circa 10-daagse cursus) en vereist "
        "vooraf inschrijving.",
        overslaan="Wie geen interesse heeft in meditatie/retraite in welke vorm dan ook kan dit "
        "overslaan; voor wie dat wel heeft, is er nu een breder aanbod dan eerder vermeld (kort "
        "dagbezoek tot meerdaagse cursus).",
        onzekerheden="Geen -- eerdere onjuiste indruk ('alleen met cursusinschrijving') is "
        "gecorrigeerd aan de hand van de officiele bron.",
        geo_status="GOOGLE_MAPS_MARKER_NOT_CONFIRMED", coord_text="nog geen BRONS/ZILVER-GEO-stap doorlopen",
        checked_at="2026-08-06",
    ),
    dict(
        nr="054", naam="Wat Thai Buddhagaya (Thai Monastery)", hook="de Thaise tempel binnen Bodh Gaya",
        cluster="Internationale kloosters", mark_status="OPEN",
        wat_is_het="Het Koninklijk Thaise Klooster, gesticht in 1956/1957 (bronnen verschillen op "
        "het exacte jaar) op uitnodiging van Nehru ter gelegenheid van de 25e boeddhistische "
        "eeuw, gebouwd door de Thaise regering. De Thaise tempel binnen Bodh Gaya.",
        waarom="Gebouwd op uitdrukkelijke uitnodiging van India's eerste premier -- een concreet "
        "historisch-diplomatiek gegeven. Rijk verguld, sterk gelijkend op de tempels van Bangkok "
        "-- visueel volledig anders dan de rest van Bodh Gaya.",
        betekenis="Correctie na brongecontroleerde herbeoordeling: de claim \"eerste buitenlandse "
        "klooster van Bodh Gaya\" is niet hard te onderbouwen -- een bron noemt een veel oudere "
        "(4e-eeuwse) Sri Lankaanse Sangharam die aan de moderne internationale kloosters "
        "voorafging. De houdbare claim is: het eerste MODERNE buitenlandse klooster in Bodh Gaya. "
        "Verdere correctie: \"enige Thaise tempel in India\" is ONJUIST en verwijderd -- er "
        "bestaan minstens twee andere Thaise tempels in India (Wat Thai Temple, Sant Nagar, "
        "Delhi; Bhogal Buddha Vihar, Delhi).",
        ervaart="Een goudkleurig, sterk hellend gelakt dak en een groot bronzen Boeddhabeeld in "
        "het heiligdom (stevig bevestigd).",
        onderscheidend="De Thaise tempel binnen Bodh Gaya (niet: de enige in heel India -- zie "
        "correctie), met een concreet historisch-diplomatiek stichtingsverhaal.",
        bezoektijd="NOG NIET ONDERZOCHT",
        combineer="NOG NIET ONDERZOCHT.",
        tips="Vrij toegankelijk. Gemelde ochtend-/avondmeditatiesessies en een jaarlijkse stille "
        "retraite in januari zijn uitsluitend via reisbronnen bevestigd, niet institutioneel "
        "geverifieerd.",
        overslaan="Geen directe biografische link met Boeddha's eigen verlichtingsverhaal -- "
        "vooral relevant voor wie de internationale/architectonische diversiteit van Bodh Gaya "
        "wil zien.",
        onzekerheden="\"Enige Thaise tempel in India\" bleek ONJUIST en is verwijderd (minstens "
        "twee andere Thaise tempels bevestigd in Delhi). \"Eerste buitenlandse klooster\" blijft "
        "bijgesteld naar \"eerste moderne buitenlandse klooster\" (een oudere Sri Lankaanse "
        "Sangharam ging vooraf). Een apart gemeld 25 m hoog tuinbeeld is niet bevestigd door "
        "Wikipedia of een officiele bron en lijkt mogelijk verward met de aparte Great Buddha "
        "Statue (049). Stichtingsjaar wisselt tussen bronnen (1956/1957).",
        geo_status="GOOGLE_MAPS_MARKER_NOT_CONFIRMED", coord_text="nog geen BRONS/ZILVER-GEO-stap doorlopen",
        checked_at="2026-08-06",
    ),
    dict(
        nr="055", naam="Royal Bhutan Monastery", hook="Bhutaanse dzong-architectuur",
        cluster="Internationale kloosters", mark_status="OPEN",
        wat_is_het="Een klooster in authentieke Bhutaanse dzong-architectuur, gebouwd in de jaren "
        "'90 met steun van Bhutans Vierde Koning Jigme Singye Wangchuck.",
        waarom="Een van de meest opvallende voorbeelden van traditionele Bhutaanse "
        "dzong-architectuur buiten het Himalaya-koninkrijk -- vestingachtige witgekalkte muren "
        "met karakteristieke rode banden, een centrale utse-toren, en houtsnijwerk met de "
        "acht-spaaks Dharma-wiel, de eindeloze knoop en beschermende godheden.",
        betekenis="Een van de meest opvallende voorbeelden van authentieke dzong-architectuur "
        "buiten de Himalaya in de straal -- duidelijk onderscheidend van de andere internationale "
        "kloosters in Bodh Gaya.",
        ervaart="Een architectonisch geheel duidelijk anders dan de andere kloosters in Bodh "
        "Gaya, met kleiwerk en muurschilderingen die Boeddha's levensverhaal uitbeelden, en een "
        "zeven voet (circa 2,1 m) hoog Boeddhabeeld in het heiligdom.",
        onderscheidend="Enige authentieke dzong-architectuur in de straal.",
        bezoektijd="NOG NIET ONDERZOCHT",
        combineer="NOG NIET ONDERZOCHT.",
        tips="Bezoekers wordt gepaste kleding en respectvol gedrag gevraagd; publieke toegang "
        "officieel bevestigd (tourism.bihar.gov.in).",
        overslaan="Geen directe biografische link met Boeddha's verlichting -- vooral relevant "
        "voor wie architectuur/vormgeving waardeert.",
        onzekerheden="Een eerdere claim (\"architectuurstijl die verder nergens buiten de "
        "Himalaya bestaat\") was een overstatement en is gecorrigeerd naar de daadwerkelijke, "
        "minder absolute brontekst.",
        geo_status="GOOGLE_MAPS_MARKER_NOT_CONFIRMED", coord_text="nog geen BRONS/ZILVER-GEO-stap doorlopen",
        checked_at="2026-08-05",
    ),
    dict(
        nr="056", naam="Tibetan Temple", hook="Tibetaans klooster tegenover Mahabodhi",
        cluster="Internationale kloosters", mark_status="OPEN",
        wat_is_het="Een Tibetaans klooster direct tegenover het hoofdcomplex, officieel \"Tibetan "
        "Temple\" genoemd (tourism.bihar.gov.in), met een reuzengebedmolen en een "
        "Maitreya-Boeddhabeeld (Boeddha van de Toekomst).",
        waarom="De gebedsmolen zelf is een concreet, imposant object: officieel bevestigd circa "
        "10 meter hoog, goud- en roodgekleurd, met een gewicht van ruim 20 ton.",
        betekenis="De schaal van de gebedsmolen en de toekomstgerichte Maitreya-symboliek zijn "
        "concreet onderscheidend van de andere internationale kloosters in Bodh Gaya.",
        ervaart="Een grote (circa 10 m hoge, ruim 20 ton wegende) gouden en rode gebedsmolen, een "
        "Maitreya-Boeddhabeeld, monniken in studie/gebed, direct tegenover de hoofdtempel.",
        onderscheidend="Schaal van de gebedsmolen en de Maitreya-symboliek, onafhankelijk van "
        "enige ongeverifieerde Dalai-Lama-claim.",
        bezoektijd="NOG NIET ONDERZOCHT",
        combineer="046 Mahabodhi Temple Complex (direct tegenover, geen extra reisinspanning).",
        tips="Direct tegenover de hoofdtempel, geen extra reisinspanning nodig.",
        overslaan="Geen directe biografische link met Boeddha's verlichting -- de eerder "
        "gesuggereerde Dalai Lama-connectie is niet bevestigd.",
        onzekerheden="De eerdere identificatie als \"Namgyal Monastery\" met een Dalai "
        "Lama-connectie was onbevestigde speculatie en is gecorrigeerd; de officiele bron "
        "(tourism.bihar.gov.in) noemt geen Namgyal Monastery, Karma Temple of Dalai Lama. Namen "
        "als \"Namgyal Monastery\" of \"Karma Temple\" staan uitsluitend als onbevestigde "
        "aliassen. Exacte institutionele gelieerdheid blijft onbevestigd.",
        geo_status="GOOGLE_MAPS_MARKER_NOT_CONFIRMED", coord_text="nog geen BRONS/ZILVER-GEO-stap doorlopen",
        checked_at="2026-08-05",
    ),
    dict(
        nr="057", naam="Vietnamese Temple", hook="drakendak en Avalokiteshvara",
        cluster="Internationale kloosters", mark_status="OPEN",
        wat_is_het="Een door de Vietnamese regering gebouwde tempel (2002), ook bekend als "
        "\"Vietnam Phat Quoc Tu\", 500 m van het hoofdcomplex, als symbool van de banden tussen "
        "Vietnam en India.",
        waarom="Een driedelig dak met drakenversieringen -- architectonisch uniek in Bodh Gaya -- "
        "en een Avalokiteshvara-beeld (in plaats van uitsluitend een Boeddhabeeld) als centraal "
        "object.",
        betekenis="Onder de tot nu toe onderzochte kandidaten in de straal de enige tempel met "
        "specifiek Vietnamese (Mahayana) architectuur en een Avalokiteshvara-focus in plaats van "
        "een Boeddha-focus.",
        ervaart="Een sereen, modern gebouwd heiligdom met drakenmotieven, art-deco-elementen en "
        "uitgestrekte tuinen.",
        onderscheidend="Architectonisch en iconografisch uniek (Avalokiteshvara i.p.v. Boeddha) "
        "binnen Bodh Gaya.",
        bezoektijd="NOG NIET ONDERZOCHT",
        combineer="500 m van het hoofdcomplex (046).",
        tips="Vrij toegankelijk.",
        overslaan="Geen directe biografische link met Boeddha's eigen verhaal -- vooral relevant "
        "voor wie de architectonische/iconografische diversiteit wil zien.",
        onzekerheden="Geen apart officieel overheidsbron gevonden voor deze locatie; de "
        "onderbouwing steunt op algemene reisbronnen (geen enkelvoudige bron als "
        "kernonderbouwing).",
        geo_status="GOOGLE_MAPS_MARKER_NOT_CONFIRMED", coord_text="nog geen BRONS/ZILVER-GEO-stap doorlopen",
        checked_at="2026-08-05",
    ),
    dict(
        nr="058", naam="Japanese Temple / Indosan Nippon (Nipponzan-Myohoji)", hook="stichter van de vredespagode-beweging",
        cluster="Internationale kloosters", mark_status="OPEN",
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
        overslaan="Geen directe biografische link met Boeddha's verlichting -- te onderscheiden "
        "van de aparte Great Buddha Statue (049).",
        onzekerheden="Geen gemeld -- bevestigd als andere locatie dan 049 (Daijokyo Buddhist "
        "Temple).",
        geo_status="GOOGLE_MAPS_MARKER_NOT_CONFIRMED", coord_text="nog geen BRONS/ZILVER-GEO-stap doorlopen",
        checked_at="2026-08-05",
    ),
]

KEUZEHULP = {
    "046": "Bestaande keuze: A -- de verlichting zelf",
    "047": "Bestaande keuze: A -- waar de Middenweg begon",
    "048": "Bestaande keuze: A -- de zes jaar ascese",
    "049": "Bestaande keuze: A -- modern eerbetoon",
    "050": "Door Mark te beoordelen -- originele Bodhi-boom-omheining",
    "051": "Door Mark te beoordelen -- voetspoor van Vishnu, Gaya-stad",
    "052": "Door Mark te beoordelen -- Karmapa-klooster, evenementafhankelijk",
    "053": "Door Mark te beoordelen -- meerdaags retraiteprogramma",
    "054": "Door Mark te beoordelen -- de Thaise tempel binnen Bodh Gaya",
    "055": "Door Mark te beoordelen -- Bhutaanse dzong-architectuur",
    "056": "Door Mark te beoordelen -- Tibetaans klooster tegenover 046",
    "057": "Door Mark te beoordelen -- Vietnamese tempel, Avalokiteshvara",
    "058": "Door Mark te beoordelen -- vredespagode-stichter Fujii",
}

CLUSTER_INTRO = {
    "Kerncluster": "Kerncluster -- samen te combineren, korte afstand lopend (bestaande Mark-keuze: A)",
    "Aanvullend": "Aanvullende rit -- eigen tijd nodig, blijft kernwaardig (bestaande Mark-keuze: A)",
    "Optioneel": "Optionele plek -- dichtbij, niet kernwaardig (bestaande Mark-keuze: A)",
    "Naast 046": "Direct naast het hoofdcomplex -- door Mark te beoordelen",
    "Gaya-stad": "Eigen stad, verder weg -- door Mark te beoordelen",
    "Studie/retraite": "Boeddhistische studie- en retraitecentra -- door Mark te beoordelen",
    "Internationale kloosters": "Internationale kloosters -- door Mark te beoordelen",
}
CLUSTER_ORDER = ["Kerncluster", "Aanvullend", "Optioneel", "Naast 046", "Gaya-stad", "Studie/retraite", "Internationale kloosters"]


def candidate_block(story, c):
    story.append(Marker(c["nr"]))
    story.append(Paragraph(f"{c['nr']} {c['naam']}{(' -- ' + c['hook']) if c['hook'] else ''}", styles["CandTitle"]))
    if c["mark_status"] == "A":
        story.append(Paragraph("Bestaande Mark-keuze: A", styles["StatusA"]))
    else:
        story.append(Paragraph("DOOR MARK TE BEOORDELEN", styles["StatusOpen"]))

    story.append(Paragraph("Wat is het?", styles["SubHead"]))
    story.append(Paragraph(c["wat_is_het"], styles["Body"]))
    story.append(Paragraph("Waarom hier naartoe?", styles["SubHead"]))
    story.append(Paragraph(c["waarom"], styles["Body"]))
    story.append(Paragraph("Spirituele / historische betekenis", styles["SubHead"]))
    story.append(Paragraph(c["betekenis"], styles["Body"]))
    story.append(Paragraph("Wat ervaart Mark concreet?", styles["SubHead"]))
    story.append(Paragraph(c["ervaart"], styles["Body"]))
    story.append(Paragraph(c["onderscheidend"], styles["Bijzonder"]))
    story.append(Paragraph("Verwachte bezoektijd", styles["SubHead"]))
    story.append(Paragraph(c["bezoektijd"], styles["Body"]))
    story.append(Paragraph("Goed te combineren met", styles["SubHead"]))
    story.append(Paragraph(c["combineer"], styles["Body"]))
    story.append(Paragraph("Praktische tips", styles["SubHead"]))
    story.append(Paragraph(c["tips"], styles["Body"]))
    story.append(Paragraph("Reden om eventueel over te slaan", styles["SubHead"]))
    story.append(Paragraph(c["overslaan"], styles["Body"]))
    story.append(Paragraph("Belangrijke feitelijke onzekerheden", styles["SubHead"]))
    story.append(Paragraph(c["onzekerheden"], styles["Onzeker"]))

    story.append(Spacer(1, 0.12 * cm))
    story.append(HRFlowable(width="100%", thickness=0.4, color=colors.HexColor("#cccccc")))
    status_text = "A (vastgelegd, zie MARK_DECISIONS_2026-08-05.jsonl)" if c["mark_status"] == "A" else "DOOR_MARK_TE_BEOORDELEN"
    story.append(Paragraph(
        f"<b>Technisch:</b> candidate_id BGY-CAND-{c['nr']} | GEO-status: {c['geo_status']} | "
        f"{c['coord_text']} | Mark-status: {status_text} | laatst gecontroleerd: {c['checked_at']}",
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
        "voorgelegd. 050-058 zijn permanent genummerd, volledig onderzocht en wachten op Mark's "
        "A/B/C. Voor de volledige technische onderbouwing, GEO-verificatie en brontabellen: zie "
        "GOUD/MARK_SELECTION_REPORT.md, GOUD/BODHGAYA_GOUD_REPORT.md, BRONS/BRONS-B01.jsonl en "
        "ZILVER/ZILVER-Z01.jsonl in deze run. Geen route, geen nachten, geen hotel/ashram en geen "
        "pacing zijn onderdeel van dit document.", styles["TechBlock"]))


def build_cover(story):
    story.append(Spacer(1, 4.5 * cm))
    story.append(Paragraph("Bodh Gaya", styles["CoverTitle"]))
    story.append(Paragraph("Keuze-reisgids -- 046 t/m 058", styles["CoverSub"]))
    story.append(Paragraph("run_id: BODHGAYA-DISCOVERY-001 | protocol: INDIA5-PROTOCOL", styles["CoverSub"]))
    story.append(Spacer(1, 1 * cm))
    story.append(Paragraph(
        "Leeswijzer -- Dit is een reisgids, geen technisch validatierapport. Elke locatie "
        "beschrijft wat het is, waarom de plek de moeite waard is, wat Mark er concreet ervaart, "
        "hoe onderscheidend het is en hoe die te combineren is met andere plekken in de buurt. "
        "De volledige GEO-technische onderbouwing staat NIET in dit document, maar in "
        "GOUD/MARK_SELECTION_REPORT.md, GOUD/BODHGAYA_GOUD_REPORT.md en de BRONS/ZILVER-bijlagen "
        "in dezelfde run. Elke locatie heeft hier wel een klein technisch blok onderaan, "
        "uitsluitend ter referentie.", styles["Body"]))
    story.append(Paragraph(
        "Waar keuze-informatie ontbreekt staat expliciet \"NOG NIET ONDERZOCHT\" in plaats van een "
        "verzonnen antwoord.", styles["Body"]))
    story.append(Paragraph(
        "046-049 zijn een vastgelegd Mark-besluit (alle vier A, zie "
        "MARK_DECISIONS_2026-08-05.jsonl) en worden hier uitsluitend ter referentie getoond, niet "
        "opnieuw ter keuze voorgelegd. 050-058 zijn permanent genummerd en staan open voor Mark's "
        "A/B/C -- dit document geeft geen voorspelde A/B/C-adviezen en bevat geen route, nachten, "
        "hotel/ashram of pacing.", styles["Body"]))
    story.append(PageBreak())


def build_index(story, page_lookup):
    story.append(Paragraph("Keuze-index", styles["SectionHead"]))
    story.append(Paragraph(
        "Alle 13 kandidaten in een oogopslag. Groen = bestaande Mark-keuze A, grijs = door Mark "
        "te beoordelen.", styles["Body"]))
    head = lambda s: Paragraph(s, styles["CellHead"])
    data = [[head("Nr."), head("Naam"), head("Cluster"), head("Mark-status"), head("Keuzehulp in een zin"), head("Pag.")]]
    for c in CANDIDATES:
        status_style = styles["CellGreen"] if c["mark_status"] == "A" else styles["CellOrange"]
        status = "A" if c["mark_status"] == "A" else "open"
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
        "DOOR_MARK_TE_BEOORDELEN, permanent genummerd en volledig onderzocht.", styles["Body"]))
    story.append(PageBreak())


def make_doc(path, page_lookup):
    story = []
    build_cover(story)
    build_index(story, page_lookup)
    build_body(story)
    doc = SimpleDocTemplate(
        path, pagesize=A4,
        leftMargin=2 * cm, rightMargin=2 * cm, topMargin=2 * cm, bottomMargin=2 * cm,
        title="Bodh Gaya -- Keuze-reisgids 046-058", author="CCI / INDIA5-PROTOCOL",
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
