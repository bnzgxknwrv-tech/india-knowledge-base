#!/usr/bin/env python3
"""Bouwt de Bodh Gaya-keuze-reisgids-PDF voor 046-049, volgens
india4/templates/GOUD_PDF_TEMPLATE.md. Geen nieuw onderzoek -- uitsluitend bestaande,
al goedgekeurde brondata uit BODHGAYA_GOUD_REPORT.md / ZILVER-Z01.jsonl / DISCOVERY_CANDIDATES.jsonl.
"""
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import cm
from reportlab.lib import colors
from reportlab.platypus import (
    SimpleDocTemplate, Paragraph, Spacer, PageBreak, Table, TableStyle, HRFlowable
)
from reportlab.lib.enums import TA_CENTER

OUT = "runs/active/BODHGAYA-DISCOVERY-001/GOUD/USER/BODHGAYA_046_049_KEUZE_REISGIDS.pdf"

styles = getSampleStyleSheet()
styles.add(ParagraphStyle("CoverTitle", parent=styles["Title"], fontSize=26, spaceAfter=6, alignment=TA_CENTER))
styles.add(ParagraphStyle("CoverSub", parent=styles["Normal"], fontSize=13, alignment=TA_CENTER, spaceAfter=4, textColor=colors.HexColor("#444444")))
styles.add(ParagraphStyle("CandTitle", parent=styles["Heading1"], fontSize=17, spaceBefore=6, spaceAfter=4, textColor=colors.HexColor("#7a3b12")))
styles.add(ParagraphStyle("SectionHead", parent=styles["Heading2"], fontSize=12, spaceBefore=10, spaceAfter=10))
styles.add(ParagraphStyle("SubHead", parent=styles["Heading3"], fontSize=10.5, spaceBefore=8, spaceAfter=3, textColor=colors.HexColor("#7a3b12")))
styles.add(ParagraphStyle("Body", parent=styles["Normal"], fontSize=10.2, leading=14.5, spaceAfter=6))
styles.add(ParagraphStyle("Bijzonder", parent=styles["Normal"], fontSize=10.8, leading=14.5, spaceAfter=8, textColor=colors.HexColor("#1f5c1f"), fontName="Helvetica-Oblique"))
styles.add(ParagraphStyle("TechBlock", parent=styles["Normal"], fontSize=7.8, leading=10.5, textColor=colors.HexColor("#555555")))
styles.add(ParagraphStyle("ClusterHead", parent=styles["Heading2"], fontSize=13, spaceBefore=14, spaceAfter=6, textColor=colors.HexColor("#7a3b12")))

story = []

# --- Voorblad ---
story.append(Spacer(1, 5 * cm))
story.append(Paragraph("Bodh Gaya", styles["CoverTitle"]))
story.append(Paragraph("Keuze-reisgids -- 046 t/m 049", styles["CoverSub"]))
story.append(Paragraph("run_id: BODHGAYA-DISCOVERY-001 | 3 augustus 2026", styles["CoverSub"]))
story.append(Spacer(1, 1 * cm))
story.append(Paragraph(
    "Dit is een reisgids voor vier locaties die de NOT_TO_BE_MISSED-poort doorstonden. "
    "Voor de volledige onderbouwing, GEO-verificatie en de negen onderzochte maar afgevallen "
    "locaties, zie het technische GOUD-rapport (BODHGAYA_GOUD_REPORT.md) en WATCHLIST.jsonl.",
    styles["Body"]))
story.append(PageBreak())

# --- Samenvattingstabel ---
story.append(Paragraph("Samenvatting", styles["SectionHead"]))
story.append(Paragraph(
    "Van dertien onderzochte, sterk onderbouwde vondsten bleven na een strenge onderlinge "
    "vergelijking vier locaties over die kandidaatstatus en een permanent nummer kregen. De "
    "overige negen zijn onderzocht en bewust niet genummerd (zie laatste pagina).",
    styles["Body"]))

data = [
    ["Nr.", "Naam", "GEO-status", "NOT_TO_BE_MISSED"],
    ["046", "Mahabodhi Temple Complex", "CONFIRMED", "CORE_PASS"],
    ["047", "Sujata Stupa, Bakraur", "CONFIRMED", "CORE_PASS"],
    ["048", "Dungeshwari Cave Temples", "niet bevestigd", "CORE_PASS"],
    ["049", "Great Buddha Statue", "niet bevestigd", "OPTIONAL_PASS"],
]
t = Table(data, colWidths=[1.5 * cm, 7.5 * cm, 3.7 * cm, 4 * cm])
t.setStyle(TableStyle([
    ("BACKGROUND", (0, 0), (-1, 0), colors.HexColor("#7a3b12")),
    ("TEXTCOLOR", (0, 0), (-1, 0), colors.white),
    ("FONTSIZE", (0, 0), (-1, -1), 9.5),
    ("GRID", (0, 0), (-1, -1), 0.5, colors.HexColor("#cccccc")),
    ("VALIGN", (0, 0), (-1, -1), "MIDDLE"),
    ("ROWBACKGROUNDS", (0, 1), (-1, -1), [colors.white, colors.HexColor("#f7f0e8")]),
]))
story.append(t)
story.append(Spacer(1, 0.4 * cm))
story.append(Paragraph(
    "Legenda: CORE_PASS = Mark zou er waarschijnlijk echte spijt van hebben dit te missen. "
    "OPTIONAL_PASS = sterk genoeg om voor te leggen, geen automatische kernbestemming. "
    "GEO-status “CONFIRMED” = coordinaat rechtstreeks bevestigd via een geopende Google "
    "Maps/Earth-marker. “niet bevestigd” = geen geverifieerde marker gevonden, geen "
    "coordinaat geraden.", styles["Body"]))
story.append(PageBreak())


def candidate_block(nr, naam, hook, waarom, betekenis, watzieje, bijzonder, combineer,
                     tips, geo_status, coord_text, checked_at):
    story.append(Paragraph(f"{nr} {naam}{(' -- ' + hook) if hook else ''}", styles["CandTitle"]))
    story.append(Paragraph("Waarom hier naartoe?", styles["SubHead"]))
    story.append(Paragraph(waarom, styles["Body"]))
    story.append(Paragraph("Spirituele / historische betekenis", styles["SubHead"]))
    story.append(Paragraph(betekenis, styles["Body"]))
    story.append(Paragraph("Wat zie je hier?", styles["SubHead"]))
    story.append(Paragraph(watzieje, styles["Body"]))
    story.append(Paragraph(bijzonder, styles["Bijzonder"]))
    if combineer:
        story.append(Paragraph("Goed te combineren met", styles["SubHead"]))
        story.append(Paragraph(combineer, styles["Body"]))
    if tips:
        story.append(Paragraph("Praktisch", styles["SubHead"]))
        story.append(Paragraph(tips, styles["Body"]))
    story.append(Spacer(1, 0.15 * cm))
    story.append(HRFlowable(width="100%", thickness=0.4, color=colors.HexColor("#cccccc")))
    story.append(Paragraph(
        f"<b>Technisch:</b> candidate_id BGY-CAND-{nr} | GEO-status: {geo_status} | "
        f"{coord_text} | Mark-keuze: DOOR_MARK_TE_BEOORDELEN | laatst gecontroleerd: {checked_at}",
        styles["TechBlock"]))
    story.append(Spacer(1, 0.5 * cm))


# --- Kerncluster ---
story.append(Paragraph("Kerncluster -- samen te combineren, korte afstand lopend", styles["ClusterHead"]))

candidate_block(
    "046", "Mahabodhi Temple Complex", "de plek van de verlichting zelf",
    "Sta op de plaats waar Boeddha 2500 jaar geleden verlichting bereikte -- niet een "
    "afbeelding of herdenkteken, maar de plek zelf.",
    "Het complex omvat de Vajrasana (de diamanttroon, bewaard door keizer Ashoka) en de "
    "directe nakomeling van de oorspronkelijke Bodhi-boom. Binnen dezelfde ommuurde grens "
    "liggen ook de zeven traditionele plekken van de weken direct na de verlichting: de "
    "Animeshlochan Chaitya (waar Boeddha een week lang onafgebroken naar de boom staarde), "
    "de Ratnachakrama (het juwelenwandelpad, met stenen lotusbloemen die zijn voetstappen "
    "markeren), de Ratnaghar Chaitya, de Ajapala Nigrodh-boom, de Muchalinda-vijver en de "
    "Rajyatana-boom. Het geheel is UNESCO-werelderfgoed. Bijzonder: Swami Sri Yukteswar Giri "
    "-- Yogananda's eigen, directe guru, in Marks eigen Kriya-lijn (Babaji, Lahiri Mahasaya, "
    "Sri Yukteswar, Yogananda) -- werd hier op Guru Purnima, juli 1906, geinitieerd in de "
    "sannyas-orde door Swami Krishna Dayal Giri van Bodh Gaya.",
    "Het 50 meter hoge tempelgebouw, de eeuwenoude boom, monniken en pelgrims uit de hele "
    "boeddhistische wereld, votiefstoepa's rondom -- een levend, dagelijks bezocht heiligdom, "
    "geen stil monument.",
    "Uniek: dit is een van de vier belangrijkste boeddhistische pelgrimsplaatsen ter wereld, "
    "en de enige plek die de verlichting zelf markeert.",
    "047 Sujata Stupa (circa 20 minuten lopen, inclusief oversteek Phalgu-rivier).",
    "Dagelijks vrij toegankelijk, geen inschrijving of speciale toegang nodig.",
    "CONFIRMED", "24.6959222N, 84.9914193E (rechtstreekse Google Maps/Earth-marker)", "2026-08-03",
)

candidate_block(
    "047", "Sujata Stupa, Bakraur", "waar de Middenweg begon",
    "Bezoek de exacte plek waar een dorpsvrouw Boeddha's leven een beslissende wending gaf.",
    "Sujata, een jonge vrouw uit het dorp Bakraur, bood Boeddha hier een kom rijstpudding "
    "(kheer) aan nadat hij zichzelf zes jaar lang had uitgehongerd in extreme ascese. Zijn "
    "aanvaarding van dat voedsel markeert het moment waarop hij de Middenweg ontdekte -- "
    "noch overdadige genietingen, noch zelfkwelling. Het huidige stoepamonument dateert "
    "oorspronkelijk uit de 2e eeuw v.Chr., met een latere uitbreidingsfase in de 8e-10e eeuw.",
    "Een gedateerd, archeologisch stoepacomplex aan de overkant van de Phalgu-rivier, "
    "rustiger en minder toeristisch dan het hoofdcomplex.",
    "Onvervangbaar: dit is de enige plek die deze specifieke, verhaalbepalende gebeurtenis "
    "markeert -- niet inwisselbaar met een andere tempel.",
    "046 Mahabodhi Temple Complex (circa 1,2 km, goed te combineren op dezelfde ochtend of "
    "middag).",
    "Vereist een korte oversteek van de Phalgu-rivier vanaf Bodh Gaya.",
    "CONFIRMED", "24.6979887N, 85.0033228E (rechtstreekse Google Maps/Earth-marker, Plus Code M2X3+58W)", "2026-08-03",
)

# --- Aanvullende cluster ---
story.append(Paragraph("Aanvullende rit -- eigen tijd nodig, blijft kernwaardig", styles["ClusterHead"]))

candidate_block(
    "048", "Dungeshwari Cave Temples", "de grotten van de zes jaar ascese",
    "Ga naar de plek waar Boeddha, vóór zijn verlichting, zichzelf tot op het bot uithongerde "
    "op zoek naar waarheid.",
    "In deze rotsgehouwen grottempels (5e-6e eeuw CE) beoefende Boeddha zes jaar extreme "
    "ascese, voordat hij naar Bodh Gaya afdaalde. De 7e-eeuwse Chinese pelgrim Xuanzang "
    "beschreef deze plek al in zijn reisverslag. Een van de grotten bevat een gouden beeld "
    "van de uitgemergelde Boeddha -- een direct, fysiek beeld van deze episode.",
    "Rustige rotsgrotten in de heuvels, ver van de drukte van het hoofdcomplex, met het "
    "aangrijpende uitgemergelde-Boeddhabeeld als middelpunt.",
    "Onvervangbaar: het spiegelbeeld-verhaal van Sujata Stupa -- de ascese die aan de "
    "aanbieding voorafging. Geen andere plek toont dit moment.",
    None,
    "Circa 12-14 km van Bodh Gaya (bronnen varieren enigszins), vereist een aparte rit per "
    "taxi of auto-riksja.",
    "niet bevestigd", "geen bevestigde marker gevonden -- geen coordinaat geraden", "2026-08-03",
)

# --- Losse optionele plek ---
story.append(Paragraph("Optionele plek -- dichtbij, niet kernwaardig", styles["ClusterHead"]))

candidate_block(
    "049", "Great Buddha Statue", "het grootste Boeddhabeeld van India",
    "Bekijk het eerste en grootste Boeddhabeeld ooit gebouwd in modern India -- indrukwekkend, "
    "maar geen onderdeel van het historische verlichtingsverhaal zelf.",
    "Het circa 20 meter hoge zittende Boeddhabeeld (circa 24 meter totale constructie "
    "inclusief lotus en voetstuk) werd gebouwd door Daijokyo Buddhist Temple, een Japanse "
    "leken-boeddhistische organisatie, en op 18 november 1989 geconsacreerd door de 14e Dalai "
    "Lama, als symbool van de wereldwijde herleving van het boeddhisme.",
    "Een groot, vrij toegankelijk beeld in open lucht, in tuinen even buiten het centrum.",
    "Indrukwekkend landmark, maar niet essentieel: het missen ervan slaat geen gat in het "
    "begrip van Boeddha's eigen verhaal, in tegenstelling tot de drie plekken hierboven.",
    "046 Mahabodhi Temple Complex (circa 1,1-1,5 km, eenvoudig te combineren).",
    "Vrij toegankelijk, altijd zichtbaar, geen inschrijving nodig.",
    "niet bevestigd", "geen bevestigde marker gevonden -- geen coordinaat geraden", "2026-08-03",
)

story.append(PageBreak())

# --- Compacte overzichtspagina ---
story.append(Paragraph("Overzicht en vergelijking", styles["SectionHead"]))

story.append(Paragraph("Indeling", styles["SubHead"]))
story.append(Paragraph(
    "<b>Kerncluster</b> (samen te combineren, kort lopen): 046 Mahabodhi Temple Complex, "
    "047 Sujata Stupa.<br/>"
    "<b>Aanvullende rit</b> (eigen tijd nodig, blijft kernwaardig): 048 Dungeshwari Cave "
    "Temples.<br/>"
    "<b>Optionele plek</b> (dichtbij, niet kernwaardig): 049 Great Buddha Statue.",
    styles["Body"]))

story.append(Paragraph("Korte vergelijking", styles["SubHead"]))
comp_data = [
    ["Nr.", "Kernvraag beantwoord", "Afstand tot 046", "Reisinspanning"],
    ["046", "De verlichting zelf", "-", "geen (ankerplek)"],
    ["047", "Waarom de ascese eindigde", "~1,2 km", "korte wandeling"],
    ["048", "Wat aan de verlichting voorafging", "~12-14 km", "aparte rit"],
    ["049", "Modern eerbetoon, geen biografisch moment", "~1,1-1,5 km*", "korte wandeling"],
]
t2 = Table(comp_data, colWidths=[1.5 * cm, 7 * cm, 3.3 * cm, 4.4 * cm])
t2.setStyle(TableStyle([
    ("BACKGROUND", (0, 0), (-1, 0), colors.HexColor("#7a3b12")),
    ("TEXTCOLOR", (0, 0), (-1, 0), colors.white),
    ("FONTSIZE", (0, 0), (-1, -1), 9),
    ("GRID", (0, 0), (-1, -1), 0.5, colors.HexColor("#cccccc")),
    ("VALIGN", (0, 0), (-1, -1), "MIDDLE"),
    ("ROWBACKGROUNDS", (0, 1), (-1, -1), [colors.white, colors.HexColor("#f7f0e8")]),
]))
story.append(t2)
story.append(Spacer(1, 0.2 * cm))
story.append(Paragraph(
    "* Afstand voor 049 is berekend op basis van een niet-bevestigd referentiecoordinaat "
    "(Wikipedia-infobox), niet op een geverifieerde marker -- indicatief, geen harde waarde.",
    styles["TechBlock"]))

story.append(Paragraph("Open onzekerheden", styles["SubHead"]))
story.append(Paragraph(
    "Exacte locatie van Sri Yukteswars sannyas-initiatie (1906) binnen Bodh Gaya niet "
    "vastgesteld. Muchalinda-vijver mogelijk twee gelijknamige plekken. UNESCO-brondocument "
    "voor 046 rechtstreeks ontoegankelijk (status wel elders bevestigd). Xuanzang-vertaling "
    "gelokaliseerd, specifieke Bodh-Gaya-passage nog niet geextraheerd. 048 en 049 hebben geen "
    "bevestigde Google Maps-marker ondanks meerdere zoekpogingen. Geen lokale insider-/"
    "kloosterbron geraadpleegd.", styles["Body"]))

story.append(Paragraph("Onderzocht, niet genummerd", styles["SubHead"]))
story.append(Paragraph(
    "Negen locaties zijn onderzocht en na een strenge onderlinge vergelijking bewust niet "
    "genummerd of van kandidaatstatus voorzien: Archaeological Museum of Bodh Gaya, Vishnupad "
    "Temple (Gaya), Tergar Monastery, Root Institute, Thai Monastery, Royal Bhutanese "
    "Monastery, een generiek Tibetaans klooster, een Vietnamese tempel, en de Japanese "
    "Temple/Indosan Nippon. Volledige redenen staan in WATCHLIST.jsonl.",
    styles["Body"]))

story.append(Spacer(1, 0.6 * cm))
story.append(HRFlowable(width="100%", thickness=0.6, color=colors.HexColor("#7a3b12")))
story.append(Spacer(1, 0.3 * cm))
story.append(Paragraph(
    "Voor de volledige technische onderbouwing, GEO-verificatie en brontabellen: zie "
    "GOUD/BODHGAYA_GOUD_REPORT.md, BRONS/BRONS-B01.jsonl en ZILVER/ZILVER-Z01.jsonl in deze run.",
    styles["TechBlock"]))

doc = SimpleDocTemplate(
    OUT, pagesize=A4,
    leftMargin=2 * cm, rightMargin=2 * cm, topMargin=2 * cm, bottomMargin=2 * cm,
    title="Bodh Gaya -- Keuze-reisgids 046-049", author="CCI / INDIA5-PROTOCOL",
)
doc.build(story)
print("OK, written", OUT)
