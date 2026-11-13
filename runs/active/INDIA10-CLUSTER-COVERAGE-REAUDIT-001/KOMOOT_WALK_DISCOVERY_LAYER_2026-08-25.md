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
- short high-reward walks near A+ / A corridors;
- dawn / early-morning and evening walks when scenery + safety make that sensible.
Avoid mediocre generic walks, repetitive hill walks, ordinary urban strolls and long hikes whose payoff is not exceptional.

## REQUIRED USE MODES
1. KNOWN-ROUTE MATCH: find the exact Komoot route/highlight corresponding to an already selected A+/A/A* walk so Mark can later type the route/highlight name into Komoot.
2. ANCHOR-RADIUS DISCOVERY: around every A+ and intrinsic A anchor, inspect Komoot hikes + highlights for exceptional nearby nature/walks.
3. CORRIDOR DISCOVERY: inspect transfer corridors between A+ anchors for waterfalls, lakes, forest walks, viewpoints and other short high-payoff stops.
4. HIGHLIGHT-FIRST DISCOVERY: search Komoot Highlights/categories (`lake`, `waterfall`, `viewpoint`, `forest`, `cave`, `ridge`, `temple`, `river`) because Indian route indexing is incomplete and exact place-name search may miss good content.
5. ROUTE-COMPARISON: if several walks reach the same attraction, compare them and retain only the most beautiful/practical variant(s), not every mediocre option.
6. EXPERIENCE-UPGRADE: Komoot evidence may promote an OPEN discovery to A+, A or A* if Mark decides its intrinsic/scenic value warrants it; provenance never limits grade.
7. WALK-CLOSURE: selected walks should have a searchable Komoot route/highlight name whenever one can be identified confidently.
8. SAFETY-CLOSURE: no walk may be recommended operationally before wildlife/legal/solo/daylight safety is checked for that exact trail/forest zone.

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
- confidence and source date;
- SAFETY fields below.

## SAFETY LAYER — ABSOLUTE HARD
For EVERY walk/hike/forest route, explicitly determine:
- `solo_safety`: SAFE_SOLO / DAYLIGHT_ONLY / PREFER_COMPANY / GUIDE_RECOMMENDED / GUIDE_REQUIRED / DO_NOT_WALK;
- whether walking is legally permitted on that exact route/forest/reserve;
- daylight window: sunrise/early morning/day/late afternoon/evening/dark; say when NOT to walk;
- wildlife relevant to that exact zone: tiger, leopard, elephant, sloth bear, wild boar, snakes, monkeys/langurs, feral dogs, other locally material risks;
- evidence level: official forest/park rule > district/forest notice > recent local reporting > multiple recent traveler reports; never guess from generic India wildlife;
- whether the trail is inside/bordering a tiger reserve, wildlife sanctuary, reserve forest or remote forest block;
- whether a registered guide is mandatory or prudent;
- whether solo walking is locally normal or should be avoided;
- recent human-wildlife incidents nearby if material and verifiable;
- mobile signal / remoteness / easy retreat to road or habitation where available;
- terrain risks: slippery rock, exposed cliff, river crossing, ice/snow, landslide, poor waymarking;
- winter-specific risk in Dec–Jan;
- recommended practical mitigation (daylight, local confirmation same morning, group/guide, driver waiting, no headphones, avoid dusk/dawn where wildlife risk dictates).

Do NOT write `safe` merely because a Komoot route exists. Komoot publication is route evidence, not a safety certification.

### Official example proving why this matters
Corbett Tiger Reserve official rules explicitly state that walking/trekking inside the Tiger Reserve is strictly prohibited, sunset driving is prohibited, and official registered guides are mandatory for excursions. The reserve contains tiger, leopard, wild elephant, sloth bear, king cobra and other wildlife. Therefore any Komoot/user-generated line crossing or entering such protected land must NOT be treated as a legal walk merely because it appears on a map.

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

## EXTRA DISCOVERY METHODS
Workers should also:
- inspect Komoot routes that pass close to A+/A/A* anchors even when the anchor is not in the route title;
- inspect repeated Highlights appearing across several popular routes: these often reveal the true scenic payoff;
- compare route photos/tips to identify whether the best section can be shortened into a higher-reward walk;
- look for walkable connectors between two selected locations so one taxi segment can become a memorable walk;
- search lake/waterfall/forest/viewpoint Highlights 5–30 km around mandatory transfer roads for A* SKIP_FIRST candidates;
- search sunrise/sunset routes separately, but only retain them if safety/daylight is suitable;
- check whether a route can be done as a short out-and-back rather than the full long Komoot loop;
- flag `DRIVER_WAIT` when a remote trailhead is best handled with a driver waiting rather than relying on local transport.

## QUALITY FILTER
Do NOT pass everything to Mark. Keep only:
- clear A+/A potential;
- plausible A* `SKIP_FIRST` corridor gems;
- B only when unusually attractive and nearly frictionless.
Hard-suppress ordinary or repetitive walks.
For long walks, require an exceptional payoff. A 3–5h generic viewpoint hike should normally remain B/C; a spiritually unique or world-class landscape walk may justify A/A+.

## CURRENT EXAMPLES
- KUMAON / NAINITAL / Naini Lake-rondwandeling (ca. 3,2 km / 55–75 min from Nainital lakefront; full lake loop) — selected A+; exact Komoot route/highlight naming still to close.
- KUMAON / DHOKANEY-SUYALBARI / Dhokaney Waterfall-wandeling (ca. 1,0–1,2 km / ca. 30–45 min from waterfall access/trailhead; start reached by road from Kainchi A+ anchor) — selected A; Komoot exact-match/route-name + exact safety classification still to close.
- KUMAON / SATTAL / Sattal / Seven Lakes — selected A* / SKIP_FIRST because Mark strongly likes this type of lake/forest experience but it must not force route sacrifice; exact best Komoot walk + safety classification still to close.

## COLOR-WORKER START QUESTION — PASTE READY
Use this as the actual START MESSAGE in each color chat. They do not start autonomously; Mark must paste/send it.

```text
JIJ BENT [KLEUR].

Repository:
bnzgxknwrv-tech/india-knowledge-base

Gebruik uitsluitend je bestaande toegewezen branch en je bestaande rol/scope. Lees eerst de actuele centrale governance/methode die je volgens je bestaande opdracht mag lezen, plus:
runs/active/INDIA10-CLUSTER-COVERAGE-REAUDIT-001/KOMOOT_WALK_DISCOVERY_LAYER_2026-08-25.md

Voer nu een zelfstandige KOMOOT WALK DISCOVERY PASS uit voor ALLE regio's/locaties binnen jouw bestaande scope.

DOEL:
Gebruik Komoot als EXTRA discoverylaag bovenop bestaand person/location-onderzoek, regional discovery en Lonely-Planet/traveler discovery. Zoek niet naar zoveel mogelijk wandelingen, maar uitsluitend naar de MOOISTE en meest memorabele wandelingen die voor deze India-reis werkelijk relevant kunnen zijn.

MARK HOUDT ZEER VAN WANDELEN. Geef daarom extra gewicht aan:
- bosmeren en bijzondere meren;
- watervallen/cascades;
- rivieren, kloven en water;
- mooi bos;
- spectaculaire viewpoints/ridges;
- grotten/rotslandschap;
- spiritueel betekenisvolle paden;
- korte high-reward ochtend- of avondwandelingen;
- uitzonderlijk mooie routes direct bij A+, A of langs verplichte transfercorridors.

GEEN middelmatige of generieke wandelingen opnemen. Een lange wandeling alleen behouden als de payoff echt uitzonderlijk is.

KOMOOT MOET OP MINSTENS DEZE MANIEREN WORDEN GEBRUIKT:
1. Zoek exacte Komoot-route/Highlight voor reeds geselecteerde wandelingen zodat Mark later de NAAM letterlijk in Komoot kan intikken.
2. Zoek rond iedere bestaande A+, A en relevante A* naar onverwachte mooie wandelingen/Highlights.
3. Zoek langs verplichte transfercorridors naar verborgen bosmeren, watervallen, viewpoints, korte bosroutes enzovoort.
4. Zoek Komoot Highlights/categorieen: lake, waterfall, river, forest, viewpoint, ridge, cave, temple, peak.
5. Vergelijk concurrerende routes naar dezelfde plek en houd alleen de mooiste/praktisch beste variant.
6. Kijk of een lange route kan worden ingekort tot alleen het mooiste deel.

PER FINDING VERPLICHT:
- exacte/best-searchable Komoot route- of Highlight-naam;
- fysiek wandelstartpunt;
- loopafstand en realistische looptijd VANAF DAT STARTPUNT;
- hoogtemeters;
- loop / heen-en-terug / point-to-point;
- terrein en moeilijkheid;
- volledig uitgeschreven relevante A+/A/A* ankerplek + huidige status;
- rijafstand + realistische rijtijd VANAF DAT ANKER NAAR HET WANDELSTARTPUNT;
- extra omweg t.o.v. verplichte corridor;
- totale bezoektijd;
- winterfit december/januari;
- wat je concreet ziet/beleeft en waarom dit ECHT mooi/bijzonder is;
- water/forest/viewpoint/spiritual tags;
- Komoot community/photos/tips signal;
- bronlinks + confidence.

VEILIGHEID IS VERPLICHT PER WANDELING:
- is wandelen daar wettelijk toegestaan?;
- solo_safety = SAFE_SOLO / DAYLIGHT_ONLY / PREFER_COMPANY / GUIDE_RECOMMENDED / GUIDE_REQUIRED / DO_NOT_WALK;
- veilig in vroege ochtend / middag / late middag / avond / donker?;
- relevante wilde dieren voor PRECIES die zone: tijger, luipaard, olifant, beer, wild zwijn, slang etc.;
- ligt route in/bij tiger reserve, wildlife sanctuary, reserve forest of ander beschermd bos?;
- gids verplicht of verstandig?;
- recente relevante mens-dierincidenten indien verifieerbaar;
- mobiel bereik/remoteness indien vindbaar;
- terreinrisico's: glad, afgrond, rivierkruising, ijs/sneeuw, aardverschuiving, slechte markering;
- concrete mitigatie: alleen daglicht, samen lopen, lokale check dezelfde ochtend, driver laten wachten enz.

BELANGRIJK:
Een Komoot-route is GEEN bewijs dat wandelen daar legaal of veilig is. Controleer officiële forest/park/district-bronnen. Voorbeeld: in Corbett Tiger Reserve is wandelen/trekking officieel strikt verboden en zijn geregistreerde gidsen voor excursies verplicht.

GRADE:
Ken zelf GEEN A+/A/A*/B/C toe. Alleen Mark beslist. Geef wel per finding jouw advies: mogelijke A+, A, A* SKIP_FIRST, B of C, met reden.

OUTPUT:
Maak een compacte freeze op je eigen branch met uitsluitend serieuze kandidaten. 0 findings is geldig. Commit die freeze op dezelfde branch en rapporteer commit + aantal kandidaten + top veiligheidsissues.
```

## INTEGRATION RULE
Komoot findings are deduplicated against current canon + traveler master. Existing C remains C unless Mark explicitly reopens. Existing selected A+/A/A* walk gets Komoot enrichment without re-ballot unless genuinely new content changes the decision context.
