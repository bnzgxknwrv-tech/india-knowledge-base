# COVERAGE_WARNINGS — INDIA TURQUOISE

status: PROVISIONAL_COVERAGE_MAP
purpose: make incompleteness explicit so overlap counts are not mistaken for final canon

## Person-layer coverage

| person | best durable layer currently usable here | coverage warning |
|---|---|---|
| Mahavatar Babaji | `RECONCILED` — Core-Kriya + IndiaROOD delta | Strongest reconciliation tier in this integration, but Babaji remains a mythic/tradition figure under the dedicated evidence rule. Reconciled source-presence claims are not historical-body proof. Claimant traditions must remain separated. |
| Lahiri Mahasaya | `RECONCILED` — Core-Kriya + IndiaROOD delta | Reconciliation gates improved to JA after IndiaROOD delta, but unresolved conflicts remain, notably Ranikhet-year and Bishnupur-related material. Do not flatten conflicting chronology. |
| Sri Yukteswar | `RECONCILED` — Core-Kriya + IndiaROOD delta | Strong reconciled layer; some biographical source-family coverage remains imperfect. Exact Serampore/Puri/Varanasi links are stronger than broad travel completeness. |
| Neem Karoli Baba | `RECONCILED` — CCI internal vs ChatGPT external | Current result explicitly says `SATURATED: NEE`; corpus, hostgraph, discovery and reconciliation gates are still partial. `Miracle of Love` and `By His Grace` remain blocked in that result. A multidetector task has been prepared but its result is not present on this branch. |
| Ram Dass | `RECONCILED` — CCI internal vs ChatGPT external | Current result explicitly says `SATURATED: NEE`; many external-only records depend on blocked/partial source families. Multidetector follow-up is prepared but not completed on this branch. |
| Ramana Maharshi | `INTERNAL_FREEZE` plus durable external/IndiaGEEL freezes available | A multidetector reconciliation task exists but is `READY_FOR_CCI`, not complete. Therefore exact/city links are usable provisionally but final counts may change. |
| Ramakrishna | `INTERNAL_FREEZE` plus durable external/IndiaGEEL freezes available | Same warning as Ramana: multidetector reconciliation is pending. Current West-Bengal/Varanasi/Vrindavan links remain provisional. |
| Paramahansa Yogananda | `INTERNAL_FREEZE` / nationwide CCI layer; targeted Yogananda–Anandamayi result | No completed all-detector reconciliation comparable to Core-Kriya is present. The nationwide layer is useful but should not be treated as final completeness. |
| Hariharananda | `INTERNAL_FREEZE` nationwide layer | No completed multidetector reconciliation present. Puri/Karar/Balighai links are durable internal findings; Bhagalpur personal-presence claim remains explicitly unconfirmed. |
| Vivekananda | `INTERNAL_FREEZE` nationwide layer | No completed multidetector reconciliation present. Broad parivrajaka travel was intentionally bundled, so city counts are structurally conservative and cannot be read as exhaustive. |
| Anandamayi Ma | `INTERNAL_FREEZE` pilot + `TARGETED_ONLY` Ranchi/Bhowanipur task | Pilot explicitly was not saturated. Many organization-listed ashram locations did not distinguish personal residence from posthumous/devotee institutional presence. Targeted Ranchi/Bhowanipur result is stronger for those specific events. |

## Specific overlap risks

### 1. Count inflation from organization-listed ashrams
Anandamayi Ma’s pilot contains a set of organization-listed ashrams where personal physical presence was not individually established. These may support `REGION_OR_PLACE_OVERLAP` or provisional city counts only when clearly labelled; they must not become exact historical-person sites by repetition.

### 2. Count inflation from same event viewed from two persons
The 1894 Allahabad Kumbh encounter is one event involving Babaji and Sri Yukteswar. It counts as two unique persons at city level but only one event/site-zone. Similar cross-person encounters must never become duplicate physical sites.

### 3. Metropolitan aggregation risk
Kolkata/Calcutta is used as a metropolitan cluster for ranking because durable records span Bhowanipur, Dakshineswar, Cossipore, Agarpara and central Kolkata. These are physically distinct. Heatmap logic must retain subsite separation.

### 4. Exact-site overreach
A city-level match is not enough for `EXACT_OR_COMPLEX_OVERLAP`. Examples explicitly kept separate: Ramakrishna Varanasi vs Lahiri’s house; Ramakrishna Akrura Ghat vs NKB Vrindavan Ashram; Anandamayi Puri vs Karar Ashram; Serampore station vs Sri Yukteswar’s ashram.

### 5. Babaji epistemic rule
For Mahavatar Babaji, `RECONCILED` means the reconciliation established what the source/tradition claims and how site identity is described. It does not certify historical bodily presence. Haidakhan, Hariharananda-derived, Siddha/Nagaraj and other claimant traditions are not silently collapsed into the AOAY/Yogananda-line Babaji.

### 6. Pending tasks can change the ranking
Two important multidetector reconciliations are not complete on this branch at integration time:
- NKB/Ram Dass multidetector reconciliation task exists but has no durable result file here.
- Ramana Maharshi/Ramakrishna multidetector reconciliation is `READY_FOR_CCI`.
Therefore current rank order is a **pre-heatmap snapshot**, not a frozen final atlas.

## What is deliberately NOT done

- no new web or person-location discovery;
- no source hunting to fill gaps;
- no permanent candidate IDs;
- no A/B/C choices;
- no route, nights or hotel choices;
- no PDF;
- no merge/PR.

## Interpretation rule for downstream agents

Treat every count in `ALL_PERSON_CITY_OVERLAP.md` as `MIN_CONFIRMED_COUNT`, not `TOTAL_TRUE_COUNT`. A later reconciled layer may add a person or downgrade/remove a weak claim. Never lower a coverage warning simply because several detector layers independently repeat the same unsupported statement.
