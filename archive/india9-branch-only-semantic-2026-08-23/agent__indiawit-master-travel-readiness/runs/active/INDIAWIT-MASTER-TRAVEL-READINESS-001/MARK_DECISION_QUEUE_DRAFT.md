# MARK DECISION QUEUE DRAFT — INDIA WIT

status: DRAFT_ONLY
snapshot_date: 2026-08-19
hard_rule: this file does not make any A/B/C choice on behalf of Mark

## Purpose

Bundle future travel choices into the fewest high-impact decision moments. The system should prepare evidence, logistics and trade-offs; Mark decides travel significance and preference-sensitive choices.

## Batch 0 — protected anchors, no re-decision

These should be shown as context, not re-opened as ordinary A/B/C candidates:

- Arunachala/Tiruvannamalai: `LOCKED_BY_MARK` A-anchor.
- Kukuchina/Dunagiri Babaji cave: existing principal travel reason/governance anchor.

Only logistics, access and surrounding-cluster integration may later be optimized around them.

## Batch 1 — national cluster selection

Goal: one compact decision screen for all still-undecided major clusters, after the heatmap and travel-material reconciliations are sufficiently stable.

Per cluster show only:
- cluster name and geographic scope;
- `MIN_CONFIRMED` Top-person count;
- number/nature of strict exact shared sites;
- strongest unique single-person reason;
- evidence maturity and any material coverage warning;
- approximate travel friction class once route metadata exists;
- winter/access risk class;
- redundancy with already protected anchors or other clusters;
- what is lost if omitted.

Mark then decides travel significance for the cluster in one action, rather than site-by-site first.

Likely batch members from current provisional overlap layer: Prayagraj, Varanasi, Kolkata/Hooghly belt, Vrindavan, Puri, Ranchi, Kainchi/Nainital/Kumaon context, Serampore, Almora/wider Kumaon. This is not a recommendation or ranking; membership may change after the final heatmap.

## Batch 2 — intensity inside selected clusters

Only for clusters Mark keeps.

For each selected cluster, ask one compact intensity choice rather than dozens of site choices. Present:
- `CORE`: minimum set of highest-confidence/highest-relevance sites;
- `EXTENDED`: adds secondary same-person/cross-person sites that materially deepen the cluster;
- `DEEP`: includes specialist/micro-sites and requires more time/local transport.

The labels are interface levels, not pre-filled choices. The system may calculate consequences such as approximate site-days, travel friction and number of local transfers, but Mark chooses the intensity.

## Batch 3 — comfort versus route efficiency

After cluster and intensity decisions, combine preference-sensitive logistics into one decision moment. Present route alternatives using the same chosen destinations, varying only:
- fewer transfers versus faster progression;
- more buffers/rest versus tighter schedule;
- overnight train/early flight tolerance where relevant;
- tolerance for uncertain winter mountain access;
- tolerance for long travel-only days.

The system may optimize technically within the selected comfort envelope but must not infer Mark’s comfort preference.

## Batch 4 — final exceptions only

Ask Mark only about unresolved items that genuinely affect the itinerary after optimization, for example:
- one cluster cannot fit without displacing another selected cluster;
- a winter-access risk makes a chosen anchor operationally fragile;
- a train/flight schedule forces a materially different route shape;
- two sites thought separate turn out to require duplicate travel effort;
- an exact-site confidence downgrade changes the reason for staying an extra day.

Do not escalate minor academic uncertainty.

## Decisions agents may optimize without Mark

Once Mark has supplied cluster significance, intensity and comfort envelope, technical agents may normally optimize:
- ordering to reduce backtracking;
- transfer sequence and connection selection;
- reasonable arrival/departure times;
- buffers for fog/winter/remote access;
- grouping sites by locality;
- scheduling rest/buffer days within Mark’s stated tolerance;
- booking-window sequencing;
- fallback ordering that preserves Mark’s selected priorities.

Agents may not autonomously change A/B/C, drop a protected anchor, select a hotel, or convert an undecided cluster into a destination.

## Upstream dependency

INDIA PAARS is specifically tasked with the definitive preference profile, A/B/C rubric, minimal-decision design and hard-constraints register, but that branch is still `READY` at this snapshot. This WIT queue is therefore a safe structural draft, not a replacement for PAARS. When PAARS completes, reconcile this queue against PAARS rather than duplicating or overruling it.