# INDIA10 — KOMOOT WALK DISCOVERY LAYER

status: ACTIVE_HARD_LAYER
updated: 2026-08-25
branch: agent/india8-cluster-casting

## PURPOSE
Add Komoot as a separate walking/nature discovery layer ABOVE the regional + traveler/Lonely-Planet layer. Komoot is not only a verifier of known walks: it is also a discovery source for exceptional walks, hidden nature and corridor bycatch that LP/traveler sources may miss.

## MARK PRIORITIES
Prefer genuinely beautiful / memorable walks. Heavy positive weighting for:
- forest lakes / blue-green lakes / unusual waterside paths;
- waterfalls / cascades / river gorges;
- forest immersion;
- dramatic viewpoints / ridges;
- caves / unusual rock landscapes;
- spiritually meaningful footpaths;
- short high-reward walks near A+ / A corridors.
Avoid mediocre generic walks, repetitive hill walks, ordinary urban strolls and long hikes whose payoff is not exceptional.

## REQUIRED USE MODES
1. KNOWN-ROUTE MATCH: find the exact Komoot route/highlight corresponding to an already selected A+/A/A* walk so Mark can later type the route/highlight name into Komoot.
2. ANCHOR-RADIUS DISCOVERY: around every A+ and intrinsic A anchor, inspect Komoot hikes + highlights for exceptional nearby nature/walks.
3. CORRIDOR DISCOVERY: inspect transfer corridors between A+ anchors for waterfalls, lakes, forest walks, viewpoints and other short high-payoff stops.
4. HIGHLIGHT-FIRST DISCOVERY: search Komoot Highlights/categories (`lake`, `waterfall`, `viewpoint`, `forest`, `cave`, `ridge`, `temple`, `river`) because Indian route indexing is incomplete and exact place-name search may miss good content.
5. ROUTE-COMPARISON: if several walks reach the same attraction, compare them and retain only the most beautiful/practical variant(s), not every mediocre option.
6. EXPERIENCE-UPGRADE: Komoot evidence may promote an OPEN discovery to A+, A or A* if Mark decides its intrinsic/scenic value warrants it; provenance never limits grade.
7. WALK-CLOSURE: selected walks should have a searchable Komoot route/highlight name whenever one can be identified confidently.

## REQUIRED DATA PER WALK
Every candidate shown to Mark must include:
- full name protocol + current status;
- exact or best-searchable Komoot route/highlight name if found;
- start point in plain language;
- walking distance + realistic duration FROM THAT START POINT;
- elevation gain/loss where available;
- loop / out-and-back / point-to-point;
- terrain / technical difficulty;
- relevant A+ / A / A* anchor and its status;
- driving distance + realistic road time FROM THAT ANCHOR TO THE WALK START;
- incremental detour versus the mandatory corridor;
- total visit burden including walking, not only road detour;
- December/January winter fit and obvious access risks;
- scenic-value rationale: what is actually beautiful/special;
- whether the route contains water / forest / viewpoint / spiritual element;
- Komoot community signal where visible: highlights, tips, photos, ratings/users (signal only, not automatic truth);
- confidence and source date.

## WALK NAME PROTOCOL — EXTENSION
For any walk shown to Mark, the explanatory name includes at minimum:
`(ca. X km / Y–Z min walking FROM [physical trailhead/start]; [main attraction]; start is ca. N km / T min drive from [FULL A+/A anchor name + status])`
If a metric is unverified, say `nog te verifiëren`.
Never write a bare walk distance that could be mistaken as distance from a hotel/base/A+ anchor.

## KOMOOT SEARCH STRATEGY
Because Google/Komoot indexing for Uttarakhand and other Indian regions is incomplete, workers MUST use multiple query families:
- `site:komoot.com [anchor] hike`
- `site:komoot.com [nearby town] hike`
- `site:komoot.com [anchor] waterfall`
- `site:komoot.com [anchor] lake`
- `site:komoot.com [anchor] viewpoint`
- `site:komoot.com [anchor] forest`
- `site:komoot.com [regional place] highlight`
- exact attraction + `komoot`
- local spelling variants and nearby-village names.
Also inspect Komoot regional guides/highlights when accessible; Komoot itself exposes browsing categories including waterfalls, caves, lakes, peaks and hiking routes.

## QUALITY FILTER
Do NOT pass everything to Mark. Keep only:
- clear A+/A potential;
- plausible A* `SKIP_FIRST` corridor gems;
- B only when unusually attractive and nearly frictionless.
Hard-suppress ordinary or repetitive walks.
For long walks, require an exceptional payoff. A 3–5h generic viewpoint hike should normally remain B/C; a spiritually unique or world-class landscape walk may justify A/A+.

## CURRENT EXAMPLES
- KUMAON / NAINITAL / Naini Lake-rondwandeling (ca. 3,2 km / 55–75 min; full lake loop from Nainital lakefront; A+ experience) — selected A+; exact Komoot route/highlight naming still to close.
- KUMAON / DHOKANEY-SUYALBARI / Dhokaney Waterfall-wandeling (ca. 1,0–1,2 km / ca. 30–45 min from waterfall access/trailhead; start reached by road from Kainchi A+ anchor) — selected A; Komoot exact-match/route-name still to close.
- KUMAON / SATTAL / Sattal / Seven Lakes — selected A* / SKIP_FIRST because Mark strongly likes this type of lake/forest experience but it must not force route sacrifice.

## WORKER/COLOR ASSIGNMENT TEMPLATE
Use this as a paste-ready task for each regional color worker, replacing REGION / BRANCH / allowed task paths as needed:

`KOMOOT WALK DISCOVERY PASS — [REGION]\n\nGebruik je bestaande toegewezen branch en respecteer alle bestaande governance/blindness/locks. Voeg GEEN eigen A/B/C/A+ toe; alleen Mark beslist.\n\nDoel: voer een aparte KOMOOT-laag uit bovenop de bestaande traveler/LP/regional discovery. Zoek NIET naar willekeurige wandelingen maar naar de MOOISTE en meest memorabele wandelingen/Highlights rond alle bestaande A+, A en relevante A* ankers en langs de verplichte transfercorridors. Prioriteit: bosmeren, bijzondere meren, watervallen/cascades, kloven/rivieren, bos, spectaculaire viewpoints/ridges, grotten, spirituele paden en korte high-reward wandelingen. Middelmatige generieke wandelingen NIET opnemen.\n\nGebruik Komoot op drie manieren: (1) exact-match voor reeds bekende geselecteerde wandelingen; (2) ontdekking rondom ankers; (3) ontdekking langs corridors. Zoek ook Komoot Highlights en categorieën lake/waterfall/viewpoint/forest/cave/ridge, plus lokale spellingsvarianten en nabijgelegen dorpen.\n\nPer finding verplicht: exacte/best-searchable Komoot routenaam of Highlight-naam indien vindbaar; startpunt; loopafstand; realistische looptijd VANAF DAT STARTPUNT; hoogteverschil; routevorm; moeilijkheid; relevante A+/A/A* ankerplek volledig uitgeschreven; rijafstand + rijtijd VANAF DAT ANKER NAAR HET STARTPUNT; extra omweg t.o.v. verplichte corridor; totale bezoektijd; winterfit dec-jan; wat je concreet ziet/beleeft; waarom uitzonderlijk mooi; water/forest/viewpoint/spiritual tags; Komoot community/photos/tips signal; bronlinks en confidence.\n\nGebruik afstand nooit zonder te zeggen WAARVANDAAN. Bij elke wandeling moet expliciet staan waar het loopdeel begint.\n\nLever alleen kandidaten op die potentieel A+/A, sterke A* SKIP_FIRST, of uitzonderlijk makkelijke B-bijvangst zijn. 0 findings is geldig. Geen middelmatige vulling.`

## INTEGRATION RULE
Komoot findings are deduplicated against current canon + traveler master. Existing C remains C unless Mark explicitly reopens. Existing selected A+/A/A* walk gets Komoot enrichment without re-ballot unless genuinely new content changes the decision context.
