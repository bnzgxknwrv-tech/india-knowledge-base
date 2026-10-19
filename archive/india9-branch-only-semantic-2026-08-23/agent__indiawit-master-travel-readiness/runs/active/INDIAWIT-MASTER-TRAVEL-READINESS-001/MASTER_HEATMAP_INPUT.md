# MASTER HEATMAP INPUT — INDIA WIT

status: PROVISIONAL_LOSSLESS_INPUT
snapshot_date: 2026-08-19
rule: every numerical overlap below is a lower bound and must be labelled `MIN_CONFIRMED`

## Heatmap semantics

Three overlap types are separate and must never be collapsed:

- `CITY_OVERLAP`: multiple persons have durable presence claims in the same city/metropolitan place, without implying one building.
- `REGION_OVERLAP`: multiple persons occur within one wider belt/region; not a city-level identity claim.
- `EXACT_SAME_SITE_OVERLAP`: two or more persons are durably tied to the same identifiable physical site/complex. Event-zones are separately marked.

Coverage state is independent from overlap count. `MIN_CONFIRMED` is not a completeness score and must not be converted into A/B/C.

## Governance anchors preserved without revaluation

### Arunachala / Tiruvannamalai
- governance: `LOCKED_BY_MARK`
- function: A-anchor
- person density: Ramana Maharshi + Paramahansa Yogananda
- exact overlap: Sri Ramanasramam
- action: retain as locked anchor; no agent re-ranking or new A/B/C.

### Kukuchina / Dunagiri
- governance: existing principal Babaji travel reason
- function: mission-critical single-person/cross-lineage anchor even if overlap count is low
- action: preserve separately from overlap ranking; do not demote because it is not a multi-person city leader.

## Consolidated city overlap layer

| city/place | MIN_CONFIRMED unique persons | persons/layer summary | maturity | exactness notes |
|---|---:|---|---|---|
| Prayagraj / Allahabad | 5 | Babaji, Sri Yukteswar, Lahiri Mahasaya, Yogananda, NKB | mixed strong reconciled + internal | 4 Church Lane exact NKB/Ram Dass; 1894 Kumbh is event-zone; station and Kumbh must remain separate |
| Varanasi / Kashi | 5 incl. Babaji tradition claim; 4 hard-historical | Lahiri, Sri Yukteswar, Ramakrishna, Anandamayi, Babaji tradition | high Core-Kriya + CCI094-strengthened Ramakrishna, mixed others | Lahiri residence exact with Sri Yukteswar; other city records not merged into that house |
| Kolkata / Calcutta metropolitan cluster | 4 | Yogananda, Vivekananda, Ramakrishna, Anandamayi | mixed internal + CCI094-strengthened Ramakrishna | Dakshineswar exact Ramakrishna/Vivekananda; Bhowanipur, Cossipore, Agarpara, ancestral house remain distinct |
| Vrindavan | 4 | NKB, Ram Dass, Anandamayi, Ramakrishna | NKB/Ram Dass reconciled but 095 pending; Ramakrishna CCI094 strengthened | exact NKB/Ram Dass ashram/mahasamadhi; Akrura Ghat separate |
| Puri | 3 | Sri Yukteswar, Hariharananda, Anandamayi | mixed | exact Karar Ashram Sri Yukteswar/Hariharananda; Anandamayi not promoted to that exact site |
| Ranchi | 2 | Yogananda, Anandamayi | targeted strong | exact/complex overlap at Ranchi Vidyalaya/YSS campus |
| Tiruvannamalai / Arunachala | 2 | Ramana, Yogananda | Ramana CCI094 reconciled; Yogananda internal | exact Sri Ramanasramam; `LOCKED_BY_MARK` |
| Serampore | 2 hard minimum | Sri Yukteswar, Yogananda | mixed | shared lineage site highly plausible; keep exact promotion provisional until Yogananda closure |
| Kainchi / Kainchi Dham | 2 | NKB, Ram Dass | reconciled current layer, 095 pending | exact Kainchi Dham |
| Almora | 2 | Anandamayi, Vivekananda | internal | city overlap only; wider Kumaon is regional cluster |
| Nainital | 2 | NKB, Ram Dass | reconciled current layer, 095 pending | Hanuman Garh exact where both records converge |

## Consolidated region overlap layer

| region/belt | MIN_CONFIRMED signal | persons/anchors | warning |
|---|---|---|---|
| West Bengal Hooghly/Kolkata lineage belt | 4+ persons | Ramakrishna, Vivekananda, Sri Yukteswar, Yogananda; Lahiri adds Nadia context | not one city and not one walkable cluster; preserve subsite identities |
| Kumaon / Uttarakhand | multi-person regional density plus unique anchor | NKB/Ram Dass Kainchi-Nainital; Anandamayi/Vivekananda Almora; Kukuchina/Dunagiri Babaji anchor | do not merge separate microclusters or treat low-overlap Babaji anchor as low-value |
| Braj / Vrindavan-Govardhan context | at least 4 persons at Vrindavan plus Ramakrishna granular additions | NKB, Ram Dass, Anandamayi, Ramakrishna | CCI094 adds/clarifies Ramakrishna granularity; exact sites remain separate |

## Strict exact same-site / same-complex layer

| exact site/complex | place | persons | status |
|---|---|---|---|
| Lahiri Mahasaya residence, D 31/58 Madanpura/Bangali Tola | Varanasi | Lahiri Mahasaya; Sri Yukteswar | HIGH, reconciled |
| Kainchi Dham | Kainchi | NKB; Ram Dass | HIGH, current reconciled layer; final multidetector count still awaits 095 |
| Neem Karoli Baba Vrindavan Ashram / Mahasamadhi complex | Vrindavan | NKB; Ram Dass | HIGH, current reconciled layer; 095 pending |
| Karar Ashram, Swargadwar | Puri | Sri Yukteswar; Hariharananda | HIGH site identity; Hariharananda broader closure still limited/provisional |
| Sri Ramanasramam | Tiruvannamalai | Ramana Maharshi; Yogananda | HIGH site identity; Ramana now CCI094 reconciled |
| Ranchi Vidyalaya / YSS campus | Ranchi | Yogananda; Anandamayi Ma | HIGH targeted exact overlap |
| Dakshineswar Kali Temple complex | Kolkata metro | Ramakrishna; Vivekananda | HIGH site identity; Ramakrishna strengthened by CCI094 |
| Hanuman Garh / Hanuman Garhi | Nainital | NKB; Ram Dass | MEDIUM-HIGH; 095 pending for final multidetector closure |
| 4 Church Lane | Prayagraj | NKB; Ram Dass | MEDIUM-HIGH; 095 pending for final multidetector closure |
| 1894 Kumbh encounter ground/zone | Prayagraj | Babaji; Sri Yukteswar | EVENT_ZONE, not fixed-site identity; Babaji epistemic caveat applies |

## Explicit non-merges

- Varanasi city records for Ramakrishna/Anandamayi/Babaji must not be merged into Lahiri’s house.
- Prayagraj Kumbh, 4 Church Lane and station material are distinct.
- Vrindavan NKB ashram and Ramakrishna Akrura Ghat are distinct.
- Kolkata metro is an aggregation convenience only; Dakshineswar, Cossipore, Bhowanipur, Agarpara and Vivekananda ancestral sites remain distinct.
- Serampore station Yogananda–Anandamayi encounter is not Sri Yukteswar’s ashram.
- Anandamayi’s Puri organization layer is not evidence of her presence at Karar Ashram.
- Babaji claimant traditions are not collapsed into one physical-historical person/site layer.

## Person coverage state to carry into heatmap

- `RECONCILED_STRONG`: Babaji, Lahiri Mahasaya, Sri Yukteswar.
- `RECONCILED_CCI094_BUT_UNSATURATED`: Ramana Maharshi, Ramakrishna.
- `RECONCILED_CURRENT_BUT_095_PENDING`: Neem Karoli Baba, Ram Dass.
- `PROVISIONAL_INTERNAL_OR_TARGETED`: Yogananda, Hariharananda, Vivekananda, Anandamayi Ma.

## Required downstream fields

Every heatmap aggregation must preserve: `MIN_CONFIRMED unique_person_count`, `location_count`, `exact_site_count`, evidence maturity, conflict flags, provisional count, blocked count, locked-anchor flag, and `travel_significance: ONBESLIST`.

Do not calculate a destination score from counts. Overlap density, single-person mission-critical anchors and coverage confidence are separate dimensions.