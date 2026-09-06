# CCI — MINICLUSTER HISTORICAL ABC + EXCLUSION PROVENANCE AUDIT

Status: **TRAVEL EXECUTION SUPPORT — PROVENANCE/EVIDENCE ONLY, NO MARK DECISION**
Worker branch: `agent/india17-cci-kumaon-geometry`
Central HEAD read: `9c14918e8e5cf81a600cd90805a6b38b1e52de42` (2026-09-06)
Applied: `decisions/INTERRUPTION_DOES_NOT_CANCEL_PENDING_WORK_MARK_RULE_2026-09-06.md` (this task and the parallel WORK_TASK are both preserved and completed, not cancelled by each other).

No A+/A/A*/B/C grade, cluster status, fixed duration, route lock, or hotel lock changed anywhere in this file.

## REVISION NOTE (this version)
This is a corrected re-run of the same task. Mark independently flagged that the first version (committed `e5a4fd9`, PR comment `5557907840`) undercounted real historical grades — he was right. A deeper search of `runs/active/INDIA8-ALL-FINDINGS-LOCATION-CLOSURE-001/` and `runs/active/INDIA8-MARK-CLUSTER-DECISIONS-2026-08-20/` (not fully searched in the first pass) surfaced **12 confirmed Braj A's instead of 2**, and **real confirmed grades for Prayagraj (0 → 3 A's, 1 B, 2 C's) that the first version reported as entirely ungraded**. Every correction below is stated explicitly, not silently absorbed.

## HEADLINE PROVENANCE FINDING — A REPEATING BUG, NOT AN ISOLATED ONE

The same failure class recurs **at least three times independently** across two different clusters:

1. **Braj:** `runs/active/INDIA8-ALL-FINDINGS-LOCATION-CLOSURE-001/VRINDAVAN_BRAJ_PARENT_DECISION_MAP.md` (2026-08-20) records 12 confirmed A visit-units. The later 2026-08-24 `BRAJ_A_PLUS_MARK_SELECTION_SLICE.md` re-presents at least two of them — **Madan Mohan Temple** and **Nidhivan grove** — as fresh, ungraded "candidates," with no reference to the 2026-08-20 map at all.
2. **Prayagraj:** `runs/active/INDIA8-MARK-CLUSTER-DECISIONS-2026-08-20/PRAYAGRAJ_MARK_DECISIONS_RECONCILED_2026-08-23.md` — itself already a repair of an earlier omission ("repair omission from latest cluster-level summary; do NOT ask Mark to re-grade these") — records **Triveni Sangam, Akshayavat, and Bade/Lete Hanuman Ji as confirmed A**. The very next day, the 2026-08-24 `PRAYAGRAJ_A_PLUS_MARK_SELECTION_SLICE.md` re-presents **Triveni Sangam itself** as candidate item #1 of an ungraded "merged A+-selection universe," again with no reference to the Aug-23 reconciliation.
3. **Haridwar/Kankhal/Rishikesh:** was explicitly **DROPPED** as a standalone cluster by Mark on 2026-08-19 (`MARK_DECISION_HARIDWAR_KANKHAL_RISHIKESH.md`), carrying a real site-level **A** (Anandamayi Ma Ashram + Samadhi Mandir, Kankhal). On 2026-08-22 this softened to cluster-level **B** ("attractive but currently not strong enough"). By 2026-08-24 it had become `READY_FOR_MARK_A_PLUS_SELECTION` (`OPEN`), with the 2026-08-19 word **"DROP"** never mentioned again. Current central files (`CURRENT_DECISIONS_MASTER.md`, `CURRENT_STATE.md`) list it simply as `OPEN`.

The common pattern: **each 2026-08-24 "selection slice" sweep appears to have been built without reading the corresponding 2026-08-19/20/22/23 decision files that already existed one to five days earlier**, in the same repository, in adjacent directories. This is not one clerical slip — it is a systematic gap in how that particular round of regional sweeps was scoped. Reported here as a pattern, not silently patched.

---

# TASK A — COMPLETE NON-CORE MINICLUSTER INVENTORY

| # | Cluster | Current cluster-level status | Owning source |
|---|---|---|---|
| 1 | Braj / Mathura–Vrindavan–Govardhan | `A+ GATE OPEN` (2 site A's fixed inside it) | `decisions/VRINDAVAN_BRAJ_CLUSTER_DROPPED_BY_MARK_2026-08-26.md` (a DROP was recorded then explicitly invalidated same day) |
| 2 | Haridwar–Kankhal–Rishikesh | `OPEN` (current) / was `DROP AS STANDALONE CLUSTER` (2026-08-19, see HEADLINE FINDING) | `MARK_DECISION_HARIDWAR_KANKHAL_RISHIKESH.md`; `HARIDWAR_RISHIKESH_A_PLUS_MARK_SELECTION_SLICE.md` |
| 3 | Prayagraj | `OPEN`, `CORRIDOR_COMPATIBLE / NOT_ROUTE_REQUIRED`; INDIA11's own provisional regie preference was `RETAIN_ONLY_IF_MAGH_MELA_ALIGNS` | `PRAYAGRAJ_A_PLUS_MARK_SELECTION_SLICE.md`; `OPTIONAL_CLUSTER_MARK_DECISION_CARDS.md` |
| 4 | Mysuru/Mysore–Bengaluru | `EXCLUDED / CONTROL`, challenged only by Hampi (see #10) | `CLUSTER_TOPOLOGY_FEASIBILITY_2026-08-25.md`; `OUT_OF_RADIUS_WORLD_MAGNET_A_PLUS_CHALLENGERS.md` |
| 5 | Ranchi | `EXCLUDED_BY_MARK`, part of the East Route Family skip | `decisions/EAST_ROUTE_FAMILY_SKIPPED_BY_MARK_2026-08-19.md` |
| 6 | Kolkata/Calcutta–Hooghly–Serampore–Dakshineswar | `EXCLUDED_BY_MARK`, same East Route Family skip | same file |
| 7 | Puri/Odisha | `EXCLUDED_BY_MARK`, same East Route Family skip | same file |
| 8 | Sri Aurobindo Ashram / Puducherry | `EXCLUDED_BY_MARK / DO_NOT_REPRESENT` (archival only) | `governance/SUCCESSOR_SAFE_STATE.md` (updated 2026-09-06), `governance/CURRENT_DECISIONS_MASTER.md` §12 |
| 9 | Kasar Devi–Almora / Crank's Ridge (internal Kumaon mini-module) | `DEPRIORITIZED` (module-level), NOT excluded — individual sites preserved as possible free ride-alongs | `KASAR_DEVI_ALMORA_MODULE_REEVALUATION_2026-08-23.md`; `KASAR_ALMORA_YIELDS_TO_RISHIKESH_2026-08-23.md` |
| 10 | Out-of-radius world-magnet challengers: Khajuraho, Sri Harmandir Sahib/Golden Temple Amritsar, Hampi | `READY_FOR_MARK_A_PLUS_SELECTION`, none assigned | `OUT_OF_RADIUS_WORLD_MAGNET_A_PLUS_CHALLENGERS.md` |

## NOT_A_CLUSTER (gateways / single tangents, excluded from the list above)
- Sun Thermo Process (Tiruvannamalai-area) — single access-to-prove item.
- Panruti cashew, Delhi cashew shopping — food tangents, explicitly not destinations.
- Kumaon/Nainital aromatic-oil/distillation [B] — route-cheap unit, never independent.
- Pantnagar Airport, Lal Kuan, Haldwani, Kathgodam — gateways, not clusters.

---

# TASK B — HISTORICAL MARK ABC LEDGER PER CLUSTER

## 1. BRAJ
**Confirmed SITE-level grades**, per `VRINDAVAN_BRAJ_PARENT_DECISION_MAP.md` (2026-08-20, `status: ACTIVE_MARK_REVIEW`, definitive settled language throughout — not a blank ballot):

| Plek | Wat het is | Persoon/laag | Grade |
|---|---|---|---|
| Vrindavan Railway Station | Historisch station, aankomstplek in Yogananda's jeugdvlucht-episode (AOAY hfst 11) | Yogananda/AOAY | **A** |
| Madan Mohan Temple | Tempel die Yogananda persoonlijk bezocht (AOAY hfst 11) | Yogananda/AOAY | **A** |
| Keshabananda / Katyayani Peeth-terrein | Historisch ashram/kluizenaarsterrein, Kriya-lijn | Yogananda + Keshabananda + Lahiri Mahasaya-lijn | **A** |
| Samb Sadashiv Kunj | Plek verbonden aan de Mahavatar Babaji-overlevering | Babaji-lijn | **A** |
| Neem Karoli Baba Vrindavan Ashram | Ashram met samadhi, Maharajji-kantoor, tempelhof | Neem Karoli Baba + Ram Dass | **A** |
| Hathiwale Baba hut-terrein / huidige Gore Dauji-plek | Historische NKB-hutlocatie, huidige opvolgerplek | Neem Karoli Baba | **A** |
| Seth Anandram Jaipuria Bhawan | Pand waar Ram Dass verbleef; mogelijk overnachtingsoptie | Ram Dass | **A** |
| Banke Bihari Temple | Grote tempel, zowel Ram Dass- als Ramakrishna-verband | Ram Dass + Sri Ramakrishna | **A** |
| Fouzdar Kunj | Historisch pand met kamer + veranda waar Ramakrishna verbleef | Sri Ramakrishna | **A** |
| Nidhivan (heilig bosje) | Heilige plek, onderdeel van het Krishna/Braj-landschap | Sri Ramakrishna + Krishna-landschap | **A** |
| Anandamayi Ma Vrindavan Ashram | Ashram waar Anandamayi Ma zelf herhaaldelijk aanwezig was | Anandamayi Ma | **A** |
| Yamuna-rivierbezoek, Vrindavan | Rivierervaring | Ram Dass + algemeen Krishna/Braj | **A** |
| Ganga Mata hut-terrein/opvolgerpand | Bij Nidhivan | Sri Ramakrishna + Ganga Mata | **B** (→A indien praktisch gratis meelift met Nidhivan) |
| Vardhaman/Burdwan Kunj | Verblijfplek Anandamayi Ma, toegang lastiger | Anandamayi Ma | **B** |
| Mathura station (NKB laatste-reis-claim) | Tegenstrijdige bronnen, geen sterke bezoekervaring | Neem Karoli Baba | **C** |

Twee verder onderzochte items (Mani Sen-huis/parlour, Sri Radhakanta-tempel) bleken bij locatiecontrole in **Panihati, West-Bengalen** te liggen, niet in Vrindavan/Braj — expliciet uit deze lijst verwijderd door de bron zelf.

**CLUSTER-level status:** `A+ GATE OPEN` — 12 A's + 2 B's zijn vast en niet-onderhandelbaar; het aparte 25-item regionale uitbreidingsaanbod (Govardhan Parikrama, Radha Kund, etc. — zie `CCI_OPTIONAL_CLUSTER_VALUE_AND_CORRIDOR_CLOSURE.md`) blijft ongegradeerd. Of de hele CLUSTER een routebepalende A+ krijgt is een aparte, nog open vraag — zie HEADLINE FINDING.

## 2. HARIDWAR–KANKHAL–RISHIKESH
**Confirmed SITE-level grades**, dated 2026-08-19 (`MARK_DECISION_HARIDWAR_KANKHAL_RISHIKESH.md`) plus one from 2026-08-22 (`HARIDWAR_KANKHAL_RISHIKESH_CLUSTER_DECISION.md`):
- `Anandamayi Ma Ashram + Samadhi Mandir, Kankhal — ashram en rustplaats van Anandamayi Ma` — **A**
- `Matri Smriti Museum + bewaarde Anandamayi Ma-kamer, Kankhal — museumkamer waar Ma haar laatste maanden doorbracht` — **B**
- `Parmarth Niketan, Rishikesh — groot ashramcomplex` — **B**
- `Sivananda Ashram / Divine Life Society, Rishikesh` — **B**
- `Sapt Rishi Ashram, Haridwar` — **B**
- `Haridwar station — historische doorreis-/transitcontext, geen bestemmingswaarde op zich` — **C** (2026-08-22)
- `AOAY Haridwar hoofdstuk-4-gebeurtenisplek` — **POTENTIALLY A, NOT YET FINAL** (exact physical micro-site unresolved)

**CLUSTER-level status:** see HEADLINE FINDING — DROP (2026-08-19) → cluster-level B (2026-08-22) → currently treated as OPEN (2026-08-24 onward) without a logged explicit reopening statement at either transition. **This is the exact conflict Task E asks to resolve; see below.**

## 3. PRAYAGRAJ
**Confirmed SITE-level grades**, per `PRAYAGRAJ_MARK_DECISIONS_RECONCILED_2026-08-23.md` (itself explicitly a repair of an earlier omission — "do NOT ask Mark to re-grade these"):
- `Triveni Sangam — samenvloeiing van Ganges, Yamuna en de traditionele Saraswati, de kern-Sangam-rivierervaring` — **A**
- `Akshayavat — heilige "onsterfelijke" banyanboom binnen het Allahabad Fort/Patalpuri-gebied` — **A**
- `Bade/Lete Hanuman Ji — beroemd liggend Hanuman-heiligdom vlak bij de Sangam` — **A**
- `Bharadwaj Ashram — traditioneel ashram/tempelterrein van wijze Bharadwaj` — **B**
- `Anandamayi Ma standalone Prayagraj-locatie — onvoldoende zelfstandig gewicht t.o.v. haar sterkere kernplekken` — **C**
- `4 Church Lane — historisch privéhuis met Neem Karoli Baba/Ram Dass-verband, geen duidelijk openbaar heiligdomsadres` — **C**
- Yogananda familiehuis-kandidaat in Prayagraj: expliciet GEEN routestop tenzij ooit een publiek heiligdom/museum/duidelijk bezoekbaar adres bewezen wordt — geen privé-huis-aan-de-deur-bezoek.

**Routingregel uit dezelfde bron:** test Prayagraj als één compacte overnachting/corridordag met de drie A's; de B mag alleen meeliften als het geografisch/tijdsefficiënt is; C's kosten geen routetijd.

**CLUSTER-level status:** `OPEN`/`CORRIDOR_COMPATIBLE`, INDIA11's own provisional (non-binding) regie preference: `RETAIN_ONLY_IF_MAGH_MELA_ALIGNS`. **Zie HEADLINE FINDING: dezelfde re-presentatiefout als bij Braj trof ook hier Triveni Sangam zelf, exact één dag na de reconciliatie die dit repareerde.**

## 4. MYSURU/MYSORE–BENGALURU
**Confirmed SITE-level grades:** **none found** anywhere in governance or decisions. Four Karnataka traveler rows preserved below the reopening threshold (Somanathapura Keshava Temple, Mysore Palace illumination, Shettihalli Rosary Church, Shravanabelagola) — **ungraded candidates, not A's.**
**CLUSTER-level status:** `EXCLUDED / CONTROL` — the region functions as the baseline against which the Hampi challenger (Task E) is compared.

## 5-7. RANCHI / KOLKATA-HOOGHLY-SERAMPORE-DAKSHINESWAR / PURI-ODISHA
**Confirmed SITE-level grades:** none surfaced as current within these excluded families themselves. Individual person-history claims exist (e.g. Yogananda's Garpar Road childhood home sits in Kolkata — see TASK D) but these are historical-evidence records (`existing_mark_ABC: null` in `ALL_FINDINGS_LOCATION_MASTER.jsonl`), not Mark grades.
**CLUSTER-level status:** `EXCLUDED_BY_MARK`, per `decisions/EAST_ROUTE_FAMILY_SKIPPED_BY_MARK_2026-08-19.md`, reconfirmed still current in `governance/CURRENT_DECISIONS_MASTER.md` line 169.

## 8. SRI AUROBINDO ASHRAM / PUDUCHERRY
**Confirmed SITE-level grades:** none. **CLUSTER-level status:** `EXCLUDED_BY_MARK / DO_NOT_REPRESENT` (archival reconstruction only, per this task's own hard rule — not reopened or recommended here).

## 9. KASAR DEVI–ALMORA / CRANK'S RIDGE (Kumaon internal module)
**Preserved historical SITE-level evidence** (explicitly NOT deleted per the reevaluation file, though exact letter grades for each individual site were not independently re-verified this session):
- Kasar Devi — historically A-level significance tied to Vivekananda's 1890s visit.
- Kakrighat — historically A-level, tied to a specific 1890 Vivekananda meditation/realization event; does not require its own sleep base (transfer-stop only).
- Crank's Ridge / Turiya Niwas — historically meaningful (Alfred "Sunyata" Sorensen heritage stay), secondary value.
- Bodh Ashram, Ramakrishna Kutir, Chitai Golu Devta Temple, Jageshwar — preserved, lower-priority per the reevaluation.
**MODULE-level status:** `DEPRIORITIZED` (2026-08-23) — lost its automatic ~3-dedicated-nights claim, capacity reassigned to a Haridwar/Rishikesh trial module. Individual sites remain eligible as free ride-alongs if route geometry ever makes them cheap, but no dedicated module is currently assumed.

## 10. OUT-OF-RADIUS WORLD-MAGNET CHALLENGERS
**Confirmed grades: none.** Khajuraho, Golden Temple Amritsar, and Hampi are each `READY_FOR_MARK_A_PLUS_SELECTION`, explicitly requiring Mark's own intrinsic-value judgment before any route reopening is considered.

---

# TASK C — WHY WANTED / WHY DROPPED

| Cluster | Original appeal | Current status | Reason skipped/deferred | Category | Reopen rule |
|---|---|---|---|---|---|
| Braj | 12 Vrindavan A-anchors already fixed (Yogananda/AOAY, Babaji lineage, Neem Karoli Baba, Ram Dass, Sri Ramakrishna, Anandamayi Ma — spanning nearly every Top-11 person layer at once) | `A+ GATE OPEN` | Not skipped — genuinely still open, awaiting Mark's A+ scope choice (A-anchors-only / core-plus / broader) | none — open, not dropped | N/A, awaiting Mark |
| Haridwar–Kankhal–Rishikesh | Anandamayi Ma is "highly interesting to Mark" (Mark's own words in the 2026-08-19 decision) | `OPEN` (current), was `DROP` (2026-08-19) | Mark's stated reason for the 2026-08-19 drop: **"the cluster is not a sufficiently strong personal magnet... visiting a small number of truly important Anandamayi Ma sites is enough; the broader Rishikesh/Haridwar corridor does not currently justify the extra travel time."** This is **ROUTE BURDEN relative to person-interest density**, not content weakness — the content (Anandamayi Ma) was explicitly praised. | ROUTE_BURDEN (explicitly, in Mark's own words) | The 2026-08-19 file itself already anticipated a reopen path: "if a later route naturally passes through the corridor... individual sites may still be reconsidered." The 2026-08-24 sweep appears to have exercised exactly that path without a separate explicit Mark reopening statement being logged. |
| Prayagraj | Triveni Sangam confluence; potential Magh Mela overlap | `OPEN`, `CORRIDOR_COMPATIBLE / NOT_ROUTE_REQUIRED` | Not dropped — the direct Agra→Gaya overnight sleeper is simply a more time-efficient existing alternative; per INDIA11's own judgment, Prayagraj "has the weakest time-efficiency of the three open decisions" | ROUTE_BURDEN (relative efficiency, not exclusion) | INDIA11's own conditional: `RETAIN_ONLY_IF_MAGH_MELA_ALIGNS` |
| Mysuru/Bengaluru | none documented as ever having strong personal pull | `EXCLUDED/CONTROL` | Geographic/route detour, no independent content strong enough absent Hampi | ROUTE_BURDEN + CONTENT_WEAKNESS (until Hampi challenged it) | Mark may assign A+ to Hampi or another Karnataka challenger |
| Ranchi / Kolkata family / Puri-Odisha | Not documented in the files read this session as ever carrying strong independent pull before the skip | `EXCLUDED_BY_MARK` | Per `EAST_ROUTE_FAMILY_SKIPPED_BY_MARK_2026-08-19.md` — this file's own stated reason was not re-extracted verbatim this session (not re-read in full); flagged as `LIVE_RECHECK_NEEDED` for the exact original wording rather than guessed here | UNVERIFIED THIS SESSION | absent explicit reopen |
| Sri Aurobindo/Puducherry | Grew incidentally out of the Panruti-cashew adjacency idea, not an independent wanted world | `EXCLUDED_BY_MARK / DO_NOT_REPRESENT` | **SIDE-CHAIN ORIGIN**, explicitly — Mark's own characterization per `SUCCESSOR_SAFE_STATE.md`: "incidental side-cluster that grew from the earlier Panruti-cashew adjacency idea" | SIDE_CHAIN_ORIGIN | only if Mark explicitly reopens |
| Kasar Devi–Almora | Vivekananda-era heritage sites (Kasar Devi, Kakrighat) | `DEPRIORITIZED` (module), sites preserved | Explicitly NOT content weakness — Mark's own reasoning was that Jageshwar's A grade existed mainly because the route was already expected nearby, while Rishikesh has genuinely independent personal pull that outcompeted a full dedicated Almora module for scarce capacity | ROUTE_BURDEN / CAPACITY_REALLOCATION, not content weakness — **do not reinterpret this as poor content, per this task's own instruction** | "if later route geometry makes Kasar/Almora nearly free, those sites may still be reconsidered as ride-alongs" |
| World-magnet challengers (Khajuraho, Amritsar, Hampi) | Deliberately surfaced by a "no fixed radius" rule specifically to prevent exceptional finds from disappearing merely for being far away | `READY_FOR_MARK_A_PLUS_SELECTION` | Not dropped — genuinely awaiting Mark's own intrinsic-value judgment; distance/UNESCO status/worker enthusiasm are explicitly barred from substituting for that judgment | none — open | Mark assigns A+ to any/none |

---

# TASK D — YOGANANDA'S CHILDHOOD HOME, 4 GARPAR ROAD

**Cluster:** Kolkata/Calcutta family — inside the `EXCLUDED_BY_MARK` East Route Family (#6 above); the site itself has never been separately graded regardless of that exclusion.

**Mark grade/status:** **none.** Every stored record (`ALL_FINDINGS_LOCATION_MASTER.jsonl` rows MR-00003, MR-00070, MR-00172, MR-00252-254) carries `existing_mark_ABC: null`. It is historical-evidence-only, never presented to Mark as a graded candidate.

**What the project's own stored evidence says about the room:**
- The historically significant room is specifically the **attic/vestibule meditation room** (chapter-4 AOAY scene: Yogananda's planned escape to the Himalayas, and — per external reconciliation — the room where Babaji later visited him in 1920 to commission the Kriya Yoga mission to the West).
- Stored `access_status` values are deliberately cautious: `"historic house access variable; YSS says linked Garpar Road centre has Saturday meditation"` and `"PRIVATE_PERMISSION_POSSIBLE"` — **the repo never claims the bedroom is a confirmed open-access museum.**

**Fresh current-evidence check performed this session (web search, 2026-09-06):** The house is a **still-inhabited family home** (Yogananda's brother Sananda's family), not a public museum. Multiple independent devotee/pilgrimage-group sources (a dedicated site for the house, an Ananda Sangha blog account, a documented 2024 pilgrimage-group visit) consistently describe it as visitable **only by prior appointment through Yogoda Satsanga Math, Dakshineswar** — "you cannot just show up and enter the house." The attic meditation room is the room these accounts describe seeing.

**Verdict: `LIVE_RECHECK_NEEDED` for exact current terms**, but the qualitative picture is now reasonably clear and consistent across independent sources: **appointment-only, family-home shrine, not a walk-in museum, attic room specifically is the historic site.** This upgrades the repo's prior generic "access variable" placeholder with a concrete access *mechanism* (contact YSS Dakshineswar in advance), without claiming a guaranteed current booking process, exact hours, or fee — those remain unverified and should not be presented as fact.

---

# TASK E — PROVENANCE CONFLICTS

## 1. Haridwar/Kankhal/Rishikesh — RESOLVED (with the gap named, not silently closed)
The historical cluster source (`MARK_DECISION_HARIDWAR_KANKHAL_RISHIKESH.md`, 2026-08-19) **does** carry a real site-level **A** for Anandamayi Ma Ashram + Samadhi Mandir, Kankhal — my own prior two reports were **wrong** to say this cluster has "0 confirmed A grades"; those reports only checked the 2026-08-24 selection-slice file and missed the earlier, still-valid 2026-08-19 site-level decision. **Correction issued here, twice now.** Which source controls: per standard precedence, the **site-level A from 2026-08-19 remains valid and current** (never explicitly revoked), while the **cluster-level status has moved DROP (2026-08-19) → B (2026-08-22) → OPEN (2026-08-24 onward)** without a logged explicit Mark reopening statement at either transition — this is the real, still-open gap (see HEADLINE FINDING), not silently regraded here.

## 2. Braj — historical A's vs. current candidates, NOT cleanly separated (corrected from the prior version of this file)
The prior version of this section said there was "no conflict" between 2 historical A's and 25 ungraded candidates. That was itself incomplete: there are **12 historical A's**, not 2 (see Task B, corrected), and **at least 2 of those 12 — Madan Mohan Temple and Nidhivan grove — are re-listed as ungraded candidates in the 2026-08-24 sweep**, which is a genuine re-presentation conflict, not a clean separation. The remaining 23 candidate items appear to be genuinely new/additive (no matching prior grade found for them), but given this session found 2 real collisions purely by cross-checking file dates and names, a full name-by-name cross-check of all 25 candidates against the 2026-08-20 parent decision map is recommended before the candidate pool is presented to Mark again as if entirely fresh.

## 4. Prayagraj — historical A's vs. current candidates, same conflict as Braj
`PRAYAGRAJ_MARK_DECISIONS_RECONCILED_2026-08-23.md` confirms Triveni Sangam, Akshayavat, and Bade/Lete Hanuman Ji as **A**. The 2026-08-24 `PRAYAGRAJ_A_PLUS_MARK_SELECTION_SLICE.md` lists Triveni Sangam again as candidate item #1 of an ungraded pool, one day after the reconciliation that fixed this exact problem once already. Same pattern as Braj; not resolved by this report, only named.

## 3. Mysore/Bengaluru — cluster exclusion vs. historical site A's
**No conflict found.** No historical site-level A was located anywhere in governance or decisions for Mysore/Bengaluru itself — only four sub-threshold traveler rows (Task B, item 4), explicitly below the reopening threshold. The only real challenger is Hampi, which is itself ungraded (`READY_FOR_MARK_A_PLUS_SELECTION`), not a historical A being overridden.

---

# CONFIRMATION PER TASK GUARDS
No A+/A/A*/B/C grade, cluster status, fixed duration, route lock, hotel lock, or Mark decision changed. Where a real correction to my own prior report was found (Haridwar/Kankhal site-level A), it is stated explicitly as a correction, not silently absorbed. Skip/reopen judgment remains Mark's. Worker branch only, not merged to central.

END
