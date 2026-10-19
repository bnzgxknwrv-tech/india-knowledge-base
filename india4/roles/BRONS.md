# BRONS — BATCHCONTRACT

Missie: onderzoek uitsluitend het kandidaatbereik van de genoemde BRONS-batch, maximaal tien kandidaten.

**Vereiste vóór start (vanaf 2026-08-02, INDIA2-architectuurbesluit)**: BRONS mag pas starten
nadat PRE-BRONS een intern consistente `REGION_CONTENT_BRIEF.json` heeft opgeleverd (gevalideerd
met `india4/scripts/validate_pre_brons_brief.py`). Zie `india4/roles/PRE-BRONS.md`. De
kandidatenlijst voor deze batch komt uit die brief/het detectiewerk, niet uit een vooraf
aangeleverde naamlijst met een vast aantal.

Lees uitsluitend: `india4/START.md`, dit contract, `india4/protocols/GITHUB_REQUIRED.md`, `india4/protocols/GEO.md`, `india4/protocols/MARK_DECISIONS.md`, de runopdracht, de PRE-BRONS-brief van deze regio en het eigen batchbestand of voortgangsbestand.

Per kandidaat, IN DEZE VOLGORDE (eerst betekenis, dan pas geometrie):
1. Leg vast: `WHY_THIS_ONE` (waarom deze specifieke plek, niet als generieke categorie), `WHY_NOT_THE_OTHERS` (waarom niet de vergelijkbare/nabijgelegen alternatieven), `MEANING_EVIDENCE` (brongewogen onderbouwing van de betekenis, geen generieke toeristische bron), `LIVING_OR_MONUMENTAL` (is de traditie/praktijk hier nog levend, of uitsluitend monumentaal/historisch), `MARK_RELEVANCE_LINK` (koppeling aan Marks bekende interesses/A-criteria uit de PRE-BRONS-brief).
2. Pas daarna de GEO-kernregel toe: zoek de volledige kandidaatnaam als openbare Google Maps-zoekopdracht; kies alleen een marker die inhoudelijk dezelfde fysieke plek is; controleer naam en waar nodig wijk, ghat, adres of plaatssoort; neem exact het markercoördinaat over; gebruik geen schatting, terreinmiddelpunt, oude KML-waarde, officieel websitecoördinaat als vervanging of nabijgelegen marker; wanneer geen passende openbare Google Maps-marker kan worden vastgesteld: `GOOGLE_MAPS_MARKER_NOT_CONFIRMED`, reden vastleggen en doorgaan.

Bestaande coördinaten zijn uitsluitend vergelijkingsmateriaal. BRONS wijzigt geen A/B/C-keuze.

Output: één JSONL-batchbestand met volledige records. Bij onvolledige uitvoering daarnaast `PROGRESS.yaml` met afgeronde candidate_id’s en `next_candidate`. Bij volledige uitvoering: readback, commit, batchstatus COMPLETED en exact één complete startvraag voor de volgende batch. Stop daarna.
