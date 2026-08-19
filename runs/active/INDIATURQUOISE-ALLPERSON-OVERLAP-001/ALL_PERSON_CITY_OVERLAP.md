# ALL_PERSON_CITY_OVERLAP — INDIA TURQUOISE

status: PROVISIONAL_PRE_HEATMAP
scope: existing durable project layers only; no new person-location research
count_rule: minimum confirmed unique-person count from explicitly available durable layers

## Layer taxonomy used

- `RECONCILED`: a durable reconciliation result exists for the person/claim. This does **not** imply every underlying claim is saturated; claim-level conflicts remain conflicts.
- `INTERNAL_FREEZE`: durable CCI/person-sweep freeze, not yet fully multidetector-reconciled.
- `EXTERNAL_FREEZE`: durable external blind detector freeze exists but has not yet been folded into a completed reconciliation for this person.
- `TARGETED_ONLY`: a durable targeted location task confirms a specific cross-person link, but is not a full person sweep.
- `LEGACY_UNVERIFIED`: older repo layer only; never used to upgrade a claim silently.

The ranking below is intentionally a **lower bound**. Missing/pending layers can only increase later counts; they are not guessed into this file.

## Ranked city/place overlaps

| rank | city/place | minimum unique persons | persons and provenance | overlap class / notes |
|---:|---|---:|---|---|
| 1 | Prayagraj / Allahabad | **5** | Mahavatar Babaji — `RECONCILED` (1894 Kumbh claim); Sri Yukteswar — `RECONCILED` (same 1894 event); Lahiri Mahasaya — `RECONCILED` (Kumbh attendance confirmed in CCI 088/092 line); Paramahansa Yogananda — `INTERNAL_FREEZE` (Kumbh 1936); Neem Karoli Baba — `RECONCILED` (4 Church Lane / station corpus) | `CITY_OVERLAP`; Babaji + Sri Yukteswar share one 1894 event and must not be double-counted as two physical sites. Person count is still 2 persons. |
| 2 | Varanasi / Kashi | **5** | Lahiri Mahasaya — `RECONCILED` (house + samadhi complex); Sri Yukteswar — `RECONCILED` (repeated visits to Lahiri house + additional reconciled Varanasi records); Ramakrishna — `INTERNAL_FREEZE` (pilgrimage at city level); Anandamayi Ma — `INTERNAL_FREEZE` (Ramghat ashram/verblijf); Mahavatar Babaji — `RECONCILED` only as a **tradition/source claim** at Dashashwamedh Ghat, not historical-body verification | `CITY_OVERLAP`; epistemic warning: Babaji contribution is a source/tradition presence claim, not proof of historical physical presence. Without Babaji the hard-historical lower bound is 4. |
| 3 | Kolkata / Calcutta metropolitan cluster | **4** | Paramahansa Yogananda — `INTERNAL_FREEZE` (family/return visit); Vivekananda — `INTERNAL_FREEZE` (ancestral house + metropolitan lineage sites); Ramakrishna — `INTERNAL_FREEZE` (Dakshineswar/Cossipore metropolitan cluster); Anandamayi Ma — `INTERNAL_FREEZE` (Agarpara) plus `TARGETED_ONLY` Bhowanipur meeting with Yogananda | `CITY_OVERLAP`; Bhowanipur exact house remains unidentified. Metropolitan aggregation is explicit; individual physical sites are not merged. |
| 4 | Vrindavan | **4** | Neem Karoli Baba — `RECONCILED` (ashram + mahasamadhi); Ram Dass — `RECONCILED` (same NKB ashram complex / later Maharajji years); Anandamayi Ma — `INTERNAL_FREEZE` (ashram/verblijf); Ramakrishna — `INTERNAL_FREEZE` (Akrura Ghat pilgrimage event) | `CITY_OVERLAP`; contains one exact NKB/Ram Dass complex overlap plus separate Anandamayi/Ramakrishna sites. |
| 5 | Puri | **3** | Sri Yukteswar — `RECONCILED` (Karar Ashram); Hariharananda — `INTERNAL_FREEZE` (Karar Ashram + Balighai Gurukulam); Anandamayi Ma — `INTERNAL_FREEZE` (organization-listed Puri layer, personal-presence depth still weaker) | `CITY_OVERLAP`; exact shared Karar site is only Sri Yukteswar + Hariharananda. Anandamayi contribution remains provisional because the pilot did not distinguish every organization-listed ashram from personal stay. |
| 6 | Ranchi | **2** | Paramahansa Yogananda — `INTERNAL_FREEZE` (Yogoda Satsanga Sakha Math / Ranchi Vidyalaya); Anandamayi Ma — `TARGETED_ONLY` (explicit Ranchi school visit and photographed garden session with Yogananda) | `EXACT_OR_COMPLEX_OVERLAP` at the Ranchi Vidyalaya/YSS campus; current campus identity confirmed in targeted task. |
| 7 | Tiruvannamalai / Arunachala | **2** | Ramana Maharshi — `INTERNAL_FREEZE` (Arunachaleswarar, Virupaksha, Skandashram, Ramanasramam); Paramahansa Yogananda — `INTERNAL_FREEZE` (1935 visit to Sri Ramanasramam) | `CITY_OVERLAP`, with one exact shared complex at Sri Ramanasramam. `LOCKED_BY_MARK` A-anchor remains unchanged. |
| 8 | Serampore | **2** | Sri Yukteswar — `RECONCILED` (Serampore ashram / associated reconciled corpus); Paramahansa Yogananda — `INTERNAL_FREEZE` (return to guru at Yogoda Math); Anandamayi Ma has a station event in the targeted Yogananda task but the available targeted result does not establish it as the same physical ashram/site | minimum hard person count **2**; station event kept separate and not used to inflate exact-overlap count. |
| 9 | Kainchi / Kainchi Dham | **2** | Neem Karoli Baba — `RECONCILED`; Ram Dass — `RECONCILED` | `EXACT_OR_COMPLEX_OVERLAP`, same ashram complex. |
| 10 | Almora | **2** | Anandamayi Ma — `INTERNAL_FREEZE` (Patal Devi, Dhaulchina, Kasar Devi/Bodh Ashram layer); Vivekananda — `INTERNAL_FREEZE` (Almora lecture/tour presence) | `CITY_OVERLAP`; not same physical site. |
| 11 | Nainital | **2** | Neem Karoli Baba — `RECONCILED`/known Hanuman Garh layer; Ram Dass — `RECONCILED` contains cross-person Hanuman Garh overlap in the reconciliation corpus | `CITY_OVERLAP`; exact-site status is retained only where both records point to Hanuman Garh, otherwise city-level. |
| 12 | West-Bengal Hooghly/Kolkata lineage belt (regional place cluster, not one city) | **4+** | Ramakrishna, Vivekananda, Sri Yukteswar, Paramahansa Yogananda — mixed `RECONCILED`/`INTERNAL_FREEZE`; Lahiri Mahasaya adds Nadia-birth-region context | `REGION_OR_PLACE_OVERLAP`; included because the durable synthesis explicitly identifies this as a dense cross-person belt. Do not treat as one city. |

## Important non-overlap anchors retained

- Kukuchina/Dunagiri Babaji cave remains the principal Babaji travel reason and is not demoted merely because it is mainly a single-person site.
- Arunachala/Tiruvannamalai remains `LOCKED_BY_MARK` A-anchor; this integration task does not alter that decision.

## Counting cautions

1. `minimum unique persons` is not a completeness score. NKB/Ram Dass are explicitly not saturated after their current reconciliation; additional durable links can still appear.
2. Ramana Maharshi/Ramakrishna have completed internal/external blind freezes available, but the multidetector reconciliation task is still pending; their entries therefore remain provisional at `INTERNAL_FREEZE` unless a targeted result independently confirms a link.
3. Yogananda, Hariharananda, Vivekananda and Anandamayi Ma do not yet have a completed repo-wide multidetector reconciliation comparable to Core-Kriya; their counts must not be read as final.
4. A shared city never implies a shared building. Exact-site identity is listed separately in `ALL_PERSON_EXACT_OVERLAP.md`.
5. Mahavatar Babaji records preserve the project’s mythic/tradition-figure evidence rule: source-claimed presence is not silently upgraded to historical bodily presence.

## Durable source envelopes used

- `runs/active/TOP11-CORE-KRIYA-RECONCILIATION-001/RECONCILIATION_RESULT.md`
- `runs/active/TOP11-CORE-KRIYA-INDIAROOD-DELTA-RECONCILIATION-001/STATUS.md` and its referenced reconciliation result
- `runs/active/TOP11-NKB-RAMDASS-EXTERNAL-RECONCILIATION-001/RECONCILIATION_RESULT.md`
- `runs/active/TOP11-INDIA-PERSON-CENTRIC-MEGASWEEP-001/PHASE2_RESULT.md`
- `runs/active/TOP11-INDIA-PERSON-CENTRIC-MEGASWEEP-001/PHASE2_SYNTHESIS.md`
- `runs/active/TOP11-INDIA-PERSON-CENTRIC-MEGASWEEP-001/PILOT_RESULT.md`
- `runs/active/YOGANANDA-ANANDAMAYI-PHOTO-LOCATION-001/RESULT.md`
- current READY/pending reconciliation status envelopes for NKB/Ram Dass and Ramana/Ramakrishna
