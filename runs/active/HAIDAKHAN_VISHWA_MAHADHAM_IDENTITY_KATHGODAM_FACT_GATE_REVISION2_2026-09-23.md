# HAIDAKHAN VISHWA MAHADHAM IDENTITY + KATHGODAM ROAD FACT GATE — REVISION 2

Task: PR #23 comment 5770872749. Supersedes the weaker Revision 1 (`runs/active/HAIDAKHAN_VISHWA_MAHADHAM_IDENTITY_AND_DISTANCE_VERIFICATION_2026-09-21.md`), which honestly reported it could not obtain coordinates. This revision found a working method and got real data.

**What changed since Revision 1:** discovered that OpenStreetMap's Nominatim geocoder and the OSRM public routing engine both answer plain HTTPS requests with structured data my fetch tool can actually read — unlike Google Maps' JavaScript-rendered pages, which return nothing useful. This is genuine new capability, not re-reading the same blogs harder.

## 1. IDENTITY

- **Official name**: Haidakhan Vishwa Mahadham.
- **Official organization**: Haidakhandi Samaj (haidakhandisamaj.in) — the site never itself publishes a postcode or coordinates, confirmed by re-reading it.
- **Textual address given by every independent secondary source**: Village Haidakhan, PO Haidakhan, District Nainital, Uttarakhand — consistent across sources, matches what Mark specified.
- **Postcode conflict, resolved as "three real, different, nearby postal areas," not a contradiction**: independently queried three separate points in this immediate area and found three genuine, distinct pincodes:
  - **263139** — Haldwani town's broad postal circle (confirmed via direct pincode lookup: covers 244 villages around Haldwani). Several secondary listing sites (mindtrip.ai etc.) attach this pincode to the ashram, most likely because they default to "nearest big town's pincode" rather than the ashram's own local one.
  - **263126** — Amritpur village / "Chhakhata Range (P-2)", confirmed via direct Nominatim lookup (a real, distinct village a few km from Kathgodam).
  - **263136** — Banana village (Salyan), confirmed via pincode search — this is the village OSM associates with the strongest ashram candidate found (§2 below).
  None of these is provably "the" official ashram pincode, because no primary source publishes one — but 263139 is very likely just the generic Haldwani-area pincode misapplied, not evidence about the ashram's real location.

## 2. COORDINATES — REAL DATA, THREE DISTINCT CANDIDATES FOUND

Queried OpenStreetMap's Nominatim geocoder directly (`nominatim.openstreetmap.org/search`, live 2026-09-23). It returned three separate real place-of-worship entries with the name "Haidakhan" in this region — not one:

| # | OSM display name | Lat | Lon | District | Notes |
|---|---|---|---|---|---|
| 1 | Shri Shri 1008 Baba Haidakhan Aasahram, Kathghariya, Bhagwanpur Jaisingh, Haldwani | 29.2354651 | 79.4823826 | Nainital | Inside Haldwani town itself (Kathghariya is a Haldwani neighborhood) |
| 2 | Haidakhan Babaji Temple, NH109, Jalori, Chilyanaula, Ranikhet | 29.6623491 | 79.4129552 | **Almora** (263645) | The already-known separate Ranikhet-area temple |
| 3 | Haidakhan Babaji Ashram, Chhota Kailash Trek, Salyan, Banana | 29.2470710 | 79.6558933 | Nainital | Associated with "Chhota Kailash" — matches the "Haidakhan local-Kailash" feature already in this project's own Kumaon notes |

Additionally queried the "Chhakhata Range" forest-administration area (repeatedly named in travel descriptions of the ashram's setting): **Chhakhata Range (P-2), Amritpur, 29.2905351, 79.5520089** — a real hamlet/forest-range marker, not itself tagged as a place of worship.

## 3. MAP/ROUTE EVIDENCE — REAL ROAD ROUTING, NOT TEXT-MINED ESTIMATES

Used OSRM (the OpenStreetMap road-network routing engine) to compute actual drivable road distance from Kathgodam (79.545, 29.268) to each candidate:

| Candidate | Real road distance | Real road duration (engine estimate) | Verdict |
|---|---|---|---|
| #1 Kathghariya/Haldwani-town shrine | 8.7 km | ~12 min | **EXCLUDE** — far too close to match any independent travel account (all describe 1.5h+); this is a local Haldwani-town shrine, not the remote ashram |
| Chhakhata Range (P-2)/Amritpur admin point | 4.1 km | ~8 min | **EXCLUDE** — a forest-range marker/entry point, not the ashram itself; also far too close to match travel accounts |
| #3 Chhota Kailash Trek/Salyan/Banana | **34.1 km** | **~54 min (engine estimate)** | **BEST-SUPPORTED MATCH** |
| #2 Ranikhet/NH109 temple | not routed from Kathgodam (wrong district entirely — Almora, ~50+ km further north than Nainital district) | — | **EXCLUDE** — confirmed separate site, separate district, separate pincode (263645) |

**Candidate #3 is corroborated by independent triangulation from Revision 1**: Kathgodam→Bhimtal (~21–22 km, independently sourced) + Bhimtal→Haidakhan (~15.8 km, independently sourced) ≈ 37 km by component legs — closely matching OSRM's 34.1 km direct route. Two independent methods (real road-network routing, and adding two independently-sourced component legs) converge within ~3 km of each other. This is the strongest evidence yet.

**Caveat, stated plainly**: OSM's own label for candidate #3 says "Haidakhan Babaji Ashram," not "Vishwa Mahadham" by name, and no postcode was returned for it on reverse geocode. I am not claiming 100% certainty — I am reporting that of three real, distinct, independently-locatable "Haidakhan" religious sites in Nainital district, this is the only one whose road distance from Kathgodam is consistent with every independent travel account, and the only one geographically consistent with the Bhimtal-relative triangulation done independently in Revision 1.

I could not fetch an actual Google Maps pin (JavaScript-rendered, returns nothing to my tool) — Nominatim/OSRM is a genuine, real, independently-operated geocoding/routing service (not a Google product) and is the closest equivalent my tools can query directly. A live Google Maps check by you or a driver remains the one remaining independent cross-check I cannot perform myself.

## 4. PHOTO IDENTITY

Not pursued this pass — given real coordinate/routing evidence is now available and photo comparison would not add more certainty than the geocoding/routing convergence already found, this was judged lower priority than closing the distance question itself, which is what determines the sleep-geometry decision.

## 5. LOOKALIKES — FOUND AND EXCLUDED WITH REASONS

| Candidate | Address/district | Distance from Kathgodam | INCLUDE/EXCLUDE | Reason |
|---|---|---|---|---|
| Shri Shri 1008 Baba Haidakhan Aasahram, Kathghariya | Haldwani town, Nainital | 8.7 km road | **EXCLUDE** | Inside Haldwani town itself; too close to match any travel account of the remote ashram |
| Haidakhan Babaji Temple, NH109, Chilyanaula, Ranikhet | Almora district, 263645 | not on this corridor | **EXCLUDE** | Different district entirely; already identified in earlier session research as the separate Ranikhet-area temple |
| Chhakhata Range (P-2)/Amritpur | Nainital, 263126 | 4.1 km road | **EXCLUDE** | A forest-range administrative point/hamlet, not tagged as a place of worship |
| Haidakhan Babaji Ashram, Chhota Kailash Trek, Salyan/Banana | Nainital, likely 263136 | 34.1 km road | **INCLUDE (best-supported)** | Only candidate matching independent travel-account distances and the Bhimtal-relative triangulation |

## 6. REALISTIC DRIVABLE ROUTE

- **Real road distance (candidate #3 → Kathgodam Railway Station)**: **34.1 km**, per direct OSM road-network routing (not a straight-line guess).
- **Engine-estimated duration**: ~54 minutes. **Flagged as likely optimistic** for this terrain — every independent human travel account (tour operators, pilgrim blogs) describes 1.5–2.5 hours for similar or shorter distances in this specific area, consistent with a real forest/river-valley road (narrow sections, single-lane bridges, local/agricultural traffic, possible unpaved stretches near the ashram itself) that a generic routing engine's speed model likely doesn't fully capture.
- **Recommended conservative December planning time**: **1.5–2 hours**, using the real 34 km distance as the base, not the engine's raw 54-minute estimate and not the earlier ungrounded 45–75 min or 3–4h figures.
- **River/road factor**: confirmed a genuinely separate ~7 km one-way foot/trekking route exists along the Gaula river (crossing it 10–11 times) — that is a hiking route, not the drivable one. The real motorable road necessarily goes to an actual bridge rather than fording, which plausibly explains part of why real road distance (34 km) exceeds a naive straight-line guess, without requiring the 90 km figure to be true.

## 7. WHY THE THREE CITED FIGURES DIFFER (not resolved by averaging)

- **~27–32 km / 44–72 min (generic calculators)**: now explainable without assuming wrong geocoding — it is close to, but somewhat less than, the real OSRM-measured 34.1 km. Most likely a slightly different (marginally shorter/more optimistic) routing path, not necessarily a different place.
- **~35–50 km / 1.5–2.5h (practical route blogs)**: **this cluster is now confirmed as the accurate one** — the real OSRM road distance (34.1 km) sits right at the bottom of this range, and the independent Bhimtal-relative triangulation (~37 km) sits inside it.
- **~90 km (official Haidakhandi Samaj site)**: remains **unexplained and not reproduced by any independent geocoding/routing evidence found**. It is internally consistent with the same site's own ~337 km Delhi-distance claim, so it is not a random typo, but no routing evidence supports it for the Kathgodam-specific leg. Possible explanations (not confirmed): a legacy figure from before a more direct road existed, or a measurement via a different, longer official route. Recommend treating the official figure as likely stale rather than authoritative for current road planning, pending a live check.

## 8. DEPARTURE TIMES — ONLY BECAUSE THE FACT GATE IS NOW ADEQUATELY SUPPORTED

Using **34.1 km real road distance**, **1.5–2h conservative December driving allowance**, normal safe station buffer:

- **For a train around 08:40 at Kathgodam**: arrive station ~08:10–08:20 (20–30 min buffer) → depart Haidakhan **~06:15–06:45**.
- **For 12039 Shatabdi at 15:15**: arrive station ~14:30–14:45 (30–45 min buffer) → depart Haidakhan **~12:30–13:15** — a humane late-morning/early-afternoon departure, not a rushed one.

These replace the earlier untested "45–75 min" assumption and the unverified 3–4h/90 km assumption alike. Both remain **LIVE_RECHECK** pending a live map/driver confirmation, per the honest limitation in §3.

## NO VRINDAVAN OPTIMIZATION, NO ROUTE LOCK, NO CURRENT_TRUTH CHANGE

As instructed. This file only establishes the physical fact gate. Waiting on PR #23 before any further step.
