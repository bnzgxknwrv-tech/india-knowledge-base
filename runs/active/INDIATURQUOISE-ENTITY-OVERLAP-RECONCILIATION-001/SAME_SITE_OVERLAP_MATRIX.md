# SAME_SITE_OVERLAP_MATRIX — INDIA TURQUOISE

status: COMPLETE_ENTITY_RECONCILIATION_LAYER
scope: existing durable repo layers only; no new person-location research

## Relation classes

- `SAME_PHYSICAL_SITE`: source records converge on one identifiable physical place.
- `SAME_PHYSICAL_SITE_WITH_MICROSITES`: one parent site/complex, but rooms, shrines, verandas, ghats, caves or other sublocations remain separate child findings.
- `ALIAS_SAME_PHYSICAL_SITE`: spelling/name variants for the same physical site.
- `SAME_EVENT_ZONE_NOT_FIXED_BUILDING`: same event-ground/zone, but no stable exact structure may be inferred.
- `PROBABLE_SAME_PHYSICAL_SITE`: strong convergence, but prior reconciliation guardrail prevents hard merge yet.
- `DISTINCT_SITE_SAME_CITY`: explicitly not merged.

## Confirmed same-site / same-complex overlaps

| entity | place | persons / traditions | source-record IDs retained | relation | confidence | reconciliation outcome |
|---|---|---|---|---|---|---|
| Lahiri Mahasaya residence, D 31/58 Madanpura/Bangali Tola | Varanasi | Lahiri Mahasaya; Sri Yukteswar; Babaji source/tradition claim | `VNS-CAND-002`; `BJ-INT-07`; `B11`; `ATL-SY-003` | `SAME_PHYSICAL_SITE` | HIGH for house identity | One house entity; keep every person/event link. Babaji link remains epistemically separate. |
| Kainchi Dham | Kainchi | Neem Karoli Baba; Ram Dass | `NKB-5`; `ext-41..49`; `ATL-RD-002` | `SAME_PHYSICAL_SITE_WITH_MICROSITES` | HIGH | One parent complex, external sublocations remain children. |
| NKB Vrindavan Ashram / Mahasamadhi complex | Vrindavan | Neem Karoli Baba; Ram Dass | `NKB-8`; `ext-104..108`; `NKB-14`; `ext-107`; `ATL-RD-003` | `SAME_PHYSICAL_SITE_WITH_MICROSITES` | HIGH | One parent complex; room/verandah/cremation/memorial distinctions retained. |
| 4 Church Lane / Red House | Prayagraj | Neem Karoli Baba; Ram Dass | `ext-20..25` + Ram-Dass cross-person record | `SAME_PHYSICAL_SITE_WITH_MICROSITES` | MEDIUM-HIGH | Parent house only is merged; room, hall, veranda, kitchen and bathroom/front-area stay separate children. |
| Karar Ashram | Puri | Sri Yukteswar; Hariharananda; separate Hariharananda-Babaji claimant tradition | `ATL-SY-002`; `ATL-HH-002`; `B14`; `B15` | `SAME_PHYSICAL_SITE_WITH_DISTINCT_MICROSITES` | HIGH site identity | One ashram complex; different rooms/events and claimant traditions remain separate. |
| Sri Ramanasramam | Tiruvannamalai | Ramana Maharshi; Yogananda | `ATL-RM-006`; `ATL-PY-009` | `SAME_PHYSICAL_SITE` | HIGH site identity | One ashram entity; separate person-events. |
| Ranchi Vidyalaya / present YSS campus | Ranchi | Yogananda; Anandamayi Ma | `ATL-PY-005`; targeted Ranchi photo-event | `HISTORIC_NAME_TO_CURRENT_SAME_CAMPUS` | HIGH | Same campus identity; historic/current names both retained. Garden is unresolved child sublocation. |
| Dakshineswar Kali Temple complex | Kolkata metro | Ramakrishna; Vivekananda | `ATL-RK-002` + Vivekananda cross-person link | `SAME_PHYSICAL_COMPLEX` | HIGH site identity | Same temple complex; not merged with any other Kolkata site. |
| Hanuman Garh / Hanuman Garhi | Nainital | Neem Karoli Baba; Ram Dass | `NKB-19`; `ext-31..34` + Ram-Dass cross-person record | `ALIAS_SAME_PHYSICAL_SITE` | MEDIUM-HIGH | Name variants merged at entity layer only; original labels retained. |
| Allahabad Kumbh 1894 | Prayagraj | Babaji; Sri Yukteswar | `BJ-INT-04`; `B09`; `ATL-SY-004` | `SAME_EVENT_ZONE_NOT_FIXED_BUILDING` | MEDIUM | One event-zone, never converted into a building-level entity. |

## Same place name but NOT same entity

| geography | records that must remain separate | reason |
|---|---|---|
| Varanasi | Lahiri residence; Dashashwamedh Ghat underground-cave claim; Anandamayi Ramghat ashram; Ramakrishna city-level pilgrimage | Same city is not physical-identity evidence. |
| Prayagraj | 4 Church Lane; railway station; Ganges bank; Flooded Hanuman Temple; Kumbh/Magh fair zone | Distinct physical sites/events. |
| Vrindavan | NKB Ashram/Mahasamadhi complex; Ramakrishna Mission Hospital; Akrura Ghat; Anandamayi ashram | Distinct complexes/locations. |
| Serampore | Sri Yukteswar/Yogoda ashram candidate; railway station encounter; Rai Ghat banyan claim | Same town, distinct or unresolved physical sites. |
| Kolkata metro | Dakshineswar; Cossipore; Vivekananda ancestral house; Bhowanipur disciple-house event; Agarpara | Metropolitan aggregation is not a merge rule. |
| Delhi | Jonapur NKB ashram; unnamed estate cross-person site; north-Delhi Hanuman temple | No merge based on Delhi label. |
| Kumaon | Babaji cave landscape; Kainchi; Bhumiadhar; Kakrighat; Hanuman Garh; Mayavati; Patal Devi; Dhaulchina | Regional cluster only; sites remain physically distinct. |

## Special-priority region result

- **Varanasi:** one strong cross-person exact house entity; Dashashwamedh remains separate ghat-zone entity.
- **Kumaon:** strongest parent/child problem is Dunagiri initiation landscape and Kainchi microsites; no regional mega-merge.
- **Bodh Gaya/Gaya:** no additional cross-person exact merge established from the durable inputs inspected; existing IDs/links remain untouched.
- **Tiruvannamalai/Arunachala:** Sri Ramanasramam is a same-site cross-person entity; Arunachaleswarar, Virupaksha, Mango Tree Cave and Skandashram remain separate Ramana micro/standalone sites.
- **Vrindavan/Braj:** NKB/Ram Dass exact complex overlap is strong; hospital, Akrura Ghat and other Braj sites remain separate.
- **Prayagraj:** 4 Church Lane is a parent house with child microsites; Kumbh is an event-zone; station/riverbank/temple remain distinct.
- **Delhi:** Jonapur and unnamed estate are explicitly kept separate.
- **Heritage stays:** no hotel/stay entity is merged into a person-site without physical identity evidence; route/stay decisions remain out of scope.
- **Oost-data:** Kolkata/Serampore/Puri/Ranchi entities are included without reopening any route.
