# BRONS — BATCHCONTRACT

Missie: onderzoek uitsluitend het kandidaatbereik van de genoemde BRONS-batch, maximaal tien kandidaten.

Lees uitsluitend: `india4/START.md`, dit contract, `india4/protocols/GITHUB_REQUIRED.md`, `india4/protocols/GEO.md`, `india4/protocols/MARK_DECISIONS.md`, de runopdracht, de kandidaatbron en het eigen batchbestand of voortgangsbestand.

Per kandidaat:
- zoek de volledige kandidaatnaam als openbare Google Maps-zoekopdracht;
- kies alleen een marker die inhoudelijk dezelfde fysieke plek is;
- controleer naam en waar nodig wijk, ghat, adres of plaatssoort;
- neem exact het markercoördinaat over;
- gebruik geen schatting, terreinmiddelpunt, oude KML-waarde, officieel websitecoördinaat als vervanging of nabijgelegen marker;
- wanneer geen passende openbare Google Maps-marker kan worden vastgesteld: `GOOGLE_MAPS_MARKER_NOT_CONFIRMED`, reden vastleggen en doorgaan.

Bestaande coördinaten zijn uitsluitend vergelijkingsmateriaal. BRONS wijzigt geen A/B/C-keuze.

Output: één JSONL-batchbestand met volledige records. Bij onvolledige uitvoering daarnaast `PROGRESS.yaml` met afgeronde candidate_id’s en `next_candidate`. Bij volledige uitvoering: readback, commit, batchstatus COMPLETED en exact één complete startvraag voor de volgende batch. Stop daarna.
