# KOMOOT COLOR INGEST TRACKER

status: ACTIVE_WAITING_FOR_COLOR_FREEZES
updated: 2026-08-25 11:09 Europe/Amsterdam

## Baseline branch heads
- BLAUW `agent/indiablauw-trip-ops-prep` -> `fcb456c2f0c0db7fe033c471f069db8f92706e37` WAITING
- ROOD `agent/indiarood-core-kriya-sweep` -> `5443eeceab292c714d3c4e5b328f55d300464259` WAITING
- ZILVER `agent/indiazilver-cluster-completeness-audit` -> `9300fcbb2ae65c06dac65ce55c89dff82ee23a6a` WAITING
- GOUD `agent/indiagoud-nonperson-anchor-audit` -> `23706035c1fe8a16cbcf8b0c4eff3ba041aa4660` WAITING
- ROZE `agent/indiaroze-route-builder-prep` -> `47fe4d52c3c3b8736f080705ddd4b6357c8aa06a` WAITING
- PAARS `agent/indiapaars-decision-rubric-prep` -> `0c28b6ca52103daad52915139ac57c9b39bc1a91` WAITING
- TURQUOISE `agent/indiaturquoise-allperson-overlap` -> `0aef428540474bcee26122f3913c26ced6aad10f` WAITING
- GEEL `agent/indiageel-ramana-ramakrishna-sweep` -> `9c0b1a0d7ec5b8990287cb79c53f17db52f93f09` WAITING

A different later branch head is a worker-response signal and must be inspected immediately.

## Ingest rules
For each arriving freeze: read only new changed files; normalize Komoot name, physical trailhead, walking km/time from that trailhead, elevation, route form, full relevant A+/A/A* anchor, road km/time from anchor to trailhead, corridor detour, total visit burden, winter fit, preferred time window, safety class, access restrictions, scenic uniqueness and water/forest/viewpoint/spiritual tags.

Deduplicate against canon + LP/traveler/regional + earlier Komoot color freezes. Existing C remains excluded unless Mark reopens. Existing A+/A/A* receives enrichment without automatic re-ballot. New rows remain OPEN and may become A+, A, A*, B or C only by Mark. A* remains formal A with operational SKIP_FIRST.

## While workers run
Do not wait passively. Continue the current Kumaon LP/traveler overlay, build a Kumaon walking board, close exact/best-searchable Komoot names for selected walks, add safety/time-window data, and continue hidden water/lake/waterfall/forest discovery along fixed A+ corridors.

## Next sequence
1. Finish Kumaon combined LP/traveler + Komoot review.
2. Ingest color freezes as soon as branch heads move.
3. Present only strong new candidates in small decision batches.
4. Repeat combined method for Varanasi/Sarnath, Bodh Gaya/Gaya, Arunachala/Tiruvannamalai, Delhi and Agra.
5. Calculate cluster days/nights only after walking footprint stabilizes.
