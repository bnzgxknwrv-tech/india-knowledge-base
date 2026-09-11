# WORK A79 independent relevance challenge — 2026-09-11

## Status and binding

- `STATUS: COMPLETE`
- `79_OF_79_COMPLETE`
- Task: PR #23 comment `5634606894`, **WORK_TASK — INDIA19 A79 INDEPENDENT RELEVANCE CHALLENGE + WEB RESEARCH — PARALLEL TO CCI**.
- Governance binding: `a72ba1deb4c84dc4e90a192dd782a84f88a3013c`.
- Frozen A79 ledger binding: `a2b71b2563f446480b012f0b9176a87e96fcb003`.
- Governing rule: `governance/MARK_PERSON_PROVENANCE_PLACE_MEANING_RULE.md` at the bound governance head.
- Current v2 provenance reconciliation inspected as required: `55f4498b51fcf32d588f051e501d3b872ba02d2e`.
- Independence: no future CCI result for this relevance task was opened, searched, quoted or used before this WORK result was frozen.
- Scope: advisory relevance/provenance audit only. No Mark grade, route, night, inclusion/exclusion, hotel or canon decision is changed.

## Outcome

The A79 set is not one homogeneous category of “important physical places”. It contains five materially different evidence geometries:

| Physical-link class | Count | Meaning |
|---|---:|---|
| `EXACT_LIFE_SITE` | 34 | Supported physical presence, life event, residence, death, cremation or practice landscape of a named person. Tradition-level certainty is stated where applicable. |
| `DIRECT_INSTITUTIONAL` | 5 | Living institution directly continuous with a person/tradition, without proof that the named person used the present fabric. |
| `MEMORIAL_OR_SUCCESSOR` | 7 | Later memorial, relic/samadhi container, museum or replacement/successor location. |
| `NAME_ONLY_OR_NO_PERSON_LINK` | 29 | Independent sacred, cultural, sensory or support value; no exact priority-person event was established. |
| `UNCERTAIN` | 4 | A precise event or birthplace is claimed by tradition, but the present marker cannot safely be equated with proved event coordinates. |

The independent advisory signal distribution is:

| WORK relevance signal | Count |
|---|---:|
| `VERY_STRONG` | 28 |
| `STRONG` | 20 |
| `MIXED` | 19 |
| `WEAK` | 12 |

These signals are not grades and must not be used to silently demote an A+/A, remove a location or shorten its allocated time. They answer only: *how well does the currently stated physical/person meaning survive adversarial provenance scrutiny?*

## Method

1. Locked the two specified commit bindings and the rule before substantive assessment.
2. Enumerated exactly A001–A079 from the frozen audit mirror and reconciled every A-number to its frozen source ID.
3. For every source ID, inspected its frozen-ledger provenance pointer and its detailed clock-PDF card. For person-bearing or disputed rows, searched the named GitHub histories/reconciliations and the current v2 provenance repair.
4. Independently searched official or primary institutional web sources first: UNESCO/ASI/government heritage bodies, YSS, Ramakrishna Math/Belur Math, Sri Ramanasramam, official temple/ashram bodies, and the organizations that operate the present site. Secondary lineage sources were used only where the claim is itself a lineage tradition.
5. Separated four questions that the PDF sometimes blends: **was the person physically here; is this present fabric contemporary; what exact subplace remains encounterable; what uncertainty survives?**
6. Assigned the required link class, strongest case for, strongest skeptical case, advisory signal, dwell mode and at least one new/corrective fact for all 79 rows.
7. Machine-checked row count, unique A001–A079 coverage, enum values and non-empty mandatory columns before freeze.

## 79-record challenge surface

The complete auditable record is `WORK_A79_RELEVANCE_MATRIX.csv`. The table below is a scan layer; it does not replace the exact person, event, physical subplace, sources, FOR/AGAINST, dwell and new-fact fields in that matrix.

| A range | Main finding |
|---|---|
| A001–A012 Kumaon | Six exact-life sites survive strongly, but Maa Dunagiri Vaishnavi Temple is sacred Babaji landscape rather than a proved Babaji event-site; Babaji Smriti Bhavan is modern memorial; YSS Dwarahat is direct institutional continuity. Bhumiadhar's first Ram Dass–Neem Karoli Baba meeting is materially under-described. |
| A013–A016 Agra | Three foods are experience/support entries with no person link. Taj Mahal is an exact funerary site and a documented Yogananda visit/photo-memory, not an uncited AOAY episode. |
| A017–A022 Bodh Gaya | Mahabodhi and the austerity landscape are core Buddha event geographies. Great Buddha is modern memorial. The monastery belt is living institutional. Sujata Stupa and the Pragbodhi ridge require explicit tradition/marker uncertainty. |
| A023–A060 Varanasi/Sarnath | The ledger combines exceptional exact sites with many independently meaningful no-person stops. The strongest hidden links are Dashashwamedh's AOAY episode, Bhadaini's repeated Anandamayi Ma presence, Lahiri's house/samadhi/cremation geography, Trailanga–Lahiri geography and Sarnath's differentiated first-sermon sequence. Bhadury Sadan must not inherit Kriyananda's 1959 Barnala event. |
| A061–A065 Kolkata | Dakshineswar, Belur Math and 4 Garpar Road are highly specific multi-person/exact-life anchors. YSS Dakshineswar is direct institutional; 37A Raja Dinendra Street is a successor center and must not substitute for 4 Garpar Road. |
| A066–A076 Tiruvannamalai | Ramana's mountain, caves, early shelters, circumambulation, temple and ashram form a rare continuous life geography. Three restaurants remain support experiences without Ramana provenance. |
| A077–A079 Delhi | Nirmal Dham's exact link is Shri Mataji's samadhi. Lotus Temple is a living Baha'i institution without founder/Top-11 physical presence. PVR Priya IMAX is conditional support/enjoyment, not spiritual provenance. |

## Dwell-mode result

| Dwell recommendation | Count | Interpretation |
|---|---:|---|
| `LOOK` | 2 | Exterior/sensory pause is sufficient for the audited meaning. |
| `VISIT` | 22 | Enter/inspect/experience, but no provenance case for extended sitting was found. |
| `SIT_30M` | 11 | A short intentional sit is needed to encounter the meaning. |
| `SIT_60M_OR_MORE` | 21 | The site has sufficient person/practice/landscape density for a real sit. |
| `PILGRIMAGE_BLOCK` | 23 | The meaning depends on a multi-subplace sequence, ritual participation, access process or sustained encounter. |

The dwell labels challenge relevance only. They do not alter frozen clock allocations. A mismatch is a flag for the later human reconciliation, never an automatic edit.

## Key conflict findings

1. **Exact house versus current center:** A064 4 Garpar Road is Yogananda's historic family house; A065 at 37A Raja Dinendra Street is a current YSS successor center.
2. **Exact event versus analogous institution:** A038 Bhadury Sadan is a current Bhadury-family/Bhrigu institution. The documented 1959 Kriyananda reading was in Barnala, Punjab.
3. **Life site versus memorial:** A008 Babaji Smriti Bhavan, A018 Great Buddha, A055 Sarnath Museum and A058 Mulagandha Kuti Vihara cannot inherit the lifetime-event status of the person they commemorate.
4. **Documented visit versus AOAY episode:** A016 Taj Mahal has a supportable Yogananda visit/photo-memory, not a newly invented AOAY scene.
5. **Person site hidden by generic place label:** A005 Bhumiadhar, A024 Dashashwamedh Ghat, A052 Manikarnika Ghat, A063 Belur Math and A074 Arunachaleswarar Temple each carry a more exact biography/event layer than the short PDF description signals.
6. **Tradition versus empirical coordinates:** A009 Babaji Cave, A020 Sujata Stupa, A021 Dungeshwari, A022 Pragbodhi ridge, A031 Kabir Chaura and A059 Shreyansanath Tirth remain meaningful while their precision is stated honestly.

## Source register

All rows use the bound frozen ledger, the A79 audit mirror and the original GitHub provenance named by the corresponding source-ID row. The following web sources were independently checked on 2026-09-11; access, rites, closures and schedules remain subject to live recheck.

- UNESCO World Heritage Centre, Mahabodhi Temple Complex: https://whc.unesco.org/en/list/1056
- UNESCO World Heritage Centre, Taj Mahal: https://whc.unesco.org/en/list/252
- Archaeological Survey of India, Sarnath overview: https://artsandculture.google.com/story/sarnath-turning-the-wheel-of-law-archaeological-survey-of-india/kQWR2ftWElFKKQ?hl=en
- Yogoda Satsanga Society of India, Dwarahat Ashram: https://yssofindia.org/ashrams/dwarahat
- Yogoda Satsanga Society of India, Dakshineswar Math: https://yssofindia.org/ashrams/dakshineswar
- Belur Math / Ramakrishna Math and Mission: https://belurmath.org/
- Sri Ramanasramam: https://www.gururamana.org/
- Arunachaleswarar Temple / Tamil Nadu HRCE: https://annamalaiyar.hrce.tn.gov.in/
- Haidakhandi Samaj: https://www.haidakhandisamaj.in/
- Ram Dass Foundation: https://www.ramdass.org/
- Shri Shree Anandamayee Sangha: https://www.shreeshreeanandamayeesangha.org/
- Ananda India pilgrimage site histories: https://anandapilgrimages.org/
- Baha'i Houses of Worship: https://www.bahai.org/places-of-worship/
- Shri Mataji biography/institutional source: https://shrimataji.org/
- PVR INOX programme/venue source for later live check: https://www.pvrcinemas.com/

## Confidence

- **High:** 79/79 inventory coverage, source-ID/A-number mapping, modern-versus-historic address distinctions, official institutional identities, major documented residences/samadhi/cremation sites.
- **Medium:** traditional event-locus claims accepted by the relevant pilgrimage lineage but not independently archaeologically pinpointable; exact accessible room/subplace inside private or controlled institutions.
- **Low until live recheck:** January 2027 access, private-house entry, exact opening hours, festival-only relic visibility, restaurant/cinema continuity and show programming.

## Deliverable map

- `WORK_A79_RELEVANCE_MATRIX.csv` — exhaustive 79-row evidence and challenge matrix.
- `WORK_A79_NEW_DISCOVERIES_AND_CHALLENGES.md` — ranked new/corrected findings, top understatements, top overstatements/obscurations and blockers.
- This file — method, counts, synthesis, sources and confidence.
