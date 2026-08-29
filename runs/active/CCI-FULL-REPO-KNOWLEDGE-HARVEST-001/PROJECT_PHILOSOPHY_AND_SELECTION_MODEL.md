# Project Philosophy and Selection Model

> Provenance note. This file was produced by the repository-wide knowledge harvest
> `CCI-FULL-REPO-KNOWLEDGE-HARVEST-001` on worker branch `agent/cci-full-repo-knowledge-harvest`,
> frozen against central commit `a37423639f7dabb0dfd55c8656d4689bb8a25351`.
> It is **archaeology and reconciliation**, not new decision-making. No Mark A/B/C grade, hotel or
> sleepbase lock, route lock or dwell decision was created, changed or inferred here.
> Every statement below carries its exact source so a successor can re-verify it independently.
> Where a statement contradicts a newer explicit Mark decision, **the newer Mark decision wins**.

Why this project exists, what it is looking for, and the rules that decide whether a place
becomes a candidate at all. This is the layer a successor needs in order to **judge a new find**
rather than merely repeat existing decisions.

Several of these principles survive **only** in commit messages or in files that were deleted
from every current branch tip. Those are marked in the `Note` line. They are recorded here so
they stop depending on git archaeology to be found.

---

## PHI-001

The project exists to plan ONE personal spiritual pilgrimage for Mark (18 Dec 2026 - 21 Jan 2027), not generic India tourism. The core object of research is always a PHYSICAL PLACE Mark can stand in and experience.

- **Class:** `CURRENT_CANON`  |  **Integration state:** `ADOPTED`
- **Source:** a37423639f7dabb0dfd55c8656d4689bb8a25351:governance/INDIA_MASTER_BOOT.md §9; PROJECT.md (india1 generation, commit 709fafe lineage)

## PHI-002

The governing question above every detector and above category completeness is: 'from which places would Mark say he absolutely would not have wanted to miss them?' — NOT 'which places exist here' and NOT 'which traditions are missing'.

- **Class:** `CURRENT_CANON`  |  **Integration state:** `ADOPTED`
- **Source:** commit b128674c (2026-08-04) Leg hoofdvraag-principe vast boven alle detectoren (INDIA2-besluit); NOT_TO_BE_MISSED_FRAMEWORK.md

## PHI-003

Eight NOT_TO_BE_MISSED rules: detectors are tools not authorities; category completeness is never on its own sufficient; a complete tradition may legitimately be absent; a sweep may end at ZERO candidates; a candidate must earn itself; fixed order EXISTS -> MEANING -> EXPERIENCEABLE -> NOT_TO_BE_MISSED -> candidate; the research radius is a research AREA not a hard cut-off; irreplaceability is not a hard gate but one of six strength grounds of which at least one must score exceptionally.

- **Class:** `CURRENT_CANON`  |  **Integration state:** `ADOPTED`
- **Source:** commits b128674c, d7fa7898 (2026-08-03/04); NOT_TO_BE_MISSED_FRAMEWORK.md

## PHI-004

Three PRIORITY_GROUPS weighting rules (Mark decision, 2026-07-12): (1) the STRENGTH OF THE PLACE outweighs the POSITION OF THE PERSON — a small YSS centre (person position 1) ranks below a great Krishna temple (position 13) that all of India visits; (2) position is a tie-breaker only at EQUAL place-strength — Krishna sits at 13 because Mark had little mental picture of him, not because he is worth less; (3) the priority index is NOT exhaustive — a powerful place outside the list must still be reported.

- **Class:** `CURRENT_CANON`  |  **Integration state:** `PARTIALLY_ADOPTED`
- **Source:** commit 2ee59451 (2026-07-12) message body; PRIORITY_GROUPS.md
- **Note:** The three rules survive only in the commit message and the india1-generation file; they are not restated in the current governance/ boot layer.

## PHI-005

AOAY (Autobiography of a Yogi) override: an AOAY check is MANDATORY in every cluster sweep, and AOAY places are the explicit EXCEPTION to the place-strength/size rule — for an AOAY place size does not count; a tiny temple Yogananda actually stood in is a destination. A NEGATIVE AOAY result must also be reported explicitly.

- **Class:** `CURRENT_CANON`  |  **Integration state:** `PARTIALLY_ADOPTED`
- **Source:** commit 2ee59451; AOAY_MASTERS.md; SWEEP_PROTOCOL poort A/E.1

## PHI-006

Three-layer discovery priority (poort A / E.1): layer 1 = AOAY + per-Top-11-person detector (100% sweep obligation, mission-critical); layer 2 = all other lenses (bonus material, may never displace layer-1 effort); layer 3 = other religious/pilgrimage places at a HIGH independent-weight threshold. A layer-2 finding may only support a SATURATED=JA claim once layer 1 is itself SATURATED or EXPLICITLY_UNAVAILABLE.

- **Class:** `CURRENT_CANON`  |  **Integration state:** `ADOPTED`
- **Source:** commit b29cbca2 (2026-08-08); governance/SWEEP_PROTOCOL.md poort A/C/J/E.1

## PHI-007

Pilgrimage search is RELIGION-INDEPENDENT. The question is 'which physical places here have exceptional religious/spiritual/pilgrimage weight?' — never 'which well-known religions are present here?'. A major world religion earns no automatic inclusion; an obscure tradition with an extreme pilgrimage site MUST be found. Religion categories are additional search terms only, never a boundary.

- **Class:** `CURRENT_CANON`  |  **Integration state:** `ADOPTED`
- **Source:** commit 6f37c298 (2026-08-08); SWEEP_PROTOCOL poort E.1; error class FK-011

## PHI-008

Definitive Top-11 persons: Yogananda, Mahavatar Babaji, Lahiri Mahasaya, Sri Yukteswar, Ram Dass, Neem Karoli Baba, Anandamayi Ma, Ramakrishna, Ramana Maharshi, Hariharananda, Vivekananda. Shri Mataji Nirmala Devi is tracked SEPARATELY with her own Mahasamadhi-location wish. Buddha and Krishna were deliberately REMOVED from this list (candidate-inflation risk) and fall entirely under layer 3.

- **Class:** `CURRENT_CANON`  |  **Integration state:** `ADOPTED`
- **Source:** commit b70742e9 (2026-08-08); PR #23 message 046

## PHI-009

Vivekananda and Hariharananda receive TARGETED-ONLY sweeps. Mark decided they get NO exhaustive nationwide deep sweep.

- **Class:** `CURRENT_CANON`  |  **Integration state:** `ADOPTED`
- **Source:** commit (india: lock targeted-only scope for Vivekananda and Hariharananda); runs/active/TOP11-INDIAGEEL-VIVEKANANDA-HARIHARANANDA-TARGETED-001/TASK.md

## PHI-010

The host/guest axis is a MANDATORY separate search axis from the start. Searching a person's OWN institutions is not enough: the Bodh Ashram miss happened because the sweep looked for Anandamayi Ma's and Neem Karoli Baba's own institutions rather than for the ESTATE OF THEIR HOST (Lama Govinda, formerly Evans-Wentz) where they were guests. Layer 3 explicitly confirms that INFORMAL, NON-INSTITUTIONAL historical dwelling places can be MARK_WAARDIG.

- **Class:** `CURRENT_CANON`  |  **Integration state:** `ADOPTED`
- **Source:** commit de9f5ca7 (2026-08-15) KUMAON miss root-cause; SWEEP_PROTOCOL poort E.1 patch

## PHI-011

Host-axis validation proof: using known hosts/disciples as independent search terms found, without any checklist, the 'Red House' at 4 Church Lane, Allahabad — Neem Karoli Baba's annual winter residence with host Dada Mukerjee for 15 years (1958-1973), stronger evidence than Bodh Ashram itself — and Anandamayi Ma's repeated guest stays with Raja Durga Singh at Solan, Himachal Pradesh (1946 + 1955), a whole new state.

- **Class:** `CURRENT_CANON`  |  **Integration state:** `ADOPTED`
- **Source:** commit 219f7e9f (2026-08-15) CCI_TASK 080

## PHI-012

Event and exact location must be recorded SEPARATELY for Top-11 connections. Example precedent: Sri Yukteswar's formal Swami-Order initiation 'by the Mahant of Buddh Gaya' is verified as an EVENT from AOAY ch. 36 footnote, but AOAY specifies no building — the exact place is NOT established, and the 'July 1906 / Guru Purnima' date comes from a secondary source, not AOAY.

- **Class:** `CURRENT_CANON`  |  **Integration state:** `ADOPTED`
- **Source:** commits b29cbca2, 8e6943ee (2026-08-08)

## PHI-013

Historic place continuity must be distinguished from STRUCTURE continuity: a site can be the same historic place while the building is not the same structure. Grade the place, state the structure honestly.

- **Class:** `CURRENT_CANON`  |  **Integration state:** `ADOPTED`
- **Source:** a37423639f7dabb0dfd55c8656d4689bb8a25351:governance/MARK_HISTORIC_SITE_CONTINUITY_RULE_2026-08-20.md; commit "governance: distinguish historic place continuity from structure continuity"

## PHI-014

One Mark decision per PHYSICAL PARENT SITE. Child sites/micro-clusters collapse into their parent complex and inherit the parent's A+ rather than generating separate ballots.

- **Class:** `CURRENT_CANON`  |  **Integration state:** `ADOPTED`
- **Source:** a37423639f7dabb0dfd55c8656d4689bb8a25351:governance/MARK_DECISION_PARENT_MICROCLUSTER_RULE_2026-08-20.md; commits "Add parent-complex A+ inheritance rule", "Collapse child-site A+ ballots into parent complexes"

## PHI-015

Premature micro-site research during the A/B/C phase is forbidden — resolve the parent decision first.

- **Class:** `CURRENT_CANON`  |  **Integration state:** `ADOPTED`
- **Source:** commit "governance: avoid premature micro-site research during ABC phase"

## PHI-016

Location resolution comes BEFORE Mark's A/B/C. A lossless master location list is required before resolution, and resolution before grading.

- **Class:** `CURRENT_CANON`  |  **Integration state:** `ADOPTED`
- **Source:** a37423639f7dabb0dfd55c8656d4689bb8a25351:governance/LOCATION_RESOLUTION_BEFORE_ABC_2026-08-19.md

## PHI-017

R1-R5 physical-resolution scale: R1 EXACT_CURRENT_SITE; R2 EXACT_HISTORIC_SITE_SUCCESSOR; R3 STRONG_LOCALIZED_APPROXIMATION; R4 BROAD_PLACE_ONLY; R5 UNRESOLVED_CLAIM.

- **Class:** `CURRENT_CANON`  |  **Integration state:** `ADOPTED`
- **Source:** INDIA WIT canonical R1-R5 schema; used across INDIABLAUW/GEEL/ROOD/WIT closures

## PHI-018

PHYSICAL_IDENTITY vocabulary for person freezes: EXACT / DEELS / ALLEEN_PLAATS / ONBEKEND; PERSONALLY_PRESENT: JA / ONZEKER / NEE. Discovery saturation and physical-identity saturation are DIFFERENT things — of the whole person-freeze corpus only Lahiri Mahasaya (ChatGPT sweep) and Ramakrishna (ChatGPT sweep) ever claimed SATURATION: JA, and only for discovery.

- **Class:** `CURRENT_CANON`  |  **Integration state:** `ADOPTED`
- **Source:** TOP11-INDIAGEEL / INDIAROOD / PARALLEL-CHATGPT freeze files (branch-only)

## PHI-019

METHOD_V2: nine phases with four mandatory saturation gates — CORPUS_COVERAGE_GATE, HOSTGRAPH gate, DISCOVERY gate, RECONCILIATION_GATE — plus EXTERNAL_MODEL_DIVERSITY_GATE. A person sweep may not be called SATURATED while any gate is NEE or PROVISIONEEL.

- **Class:** `CURRENT_CANON`  |  **Integration state:** `ADOPTED`
- **Source:** commit 1b389a1e (2026-08-16) CCI_TASK 084 Deel B; METHOD_V2.md

## PHI-020

External multi-AI comparison is MANDATORY for the remaining Top-11, decided by a pre-agreed rule (>=1 significant verified external miss found). Root cause: CCI's own token/gazetteer detector is strong for toponyms but structurally WEAK for private-resident-named addresses — exactly where external host-network analysis added value.

- **Class:** `CURRENT_CANON`  |  **Integration state:** `ADOPTED`
- **Source:** commit a7054455 (2026-08-18) CCI_TASK 086

## PHI-021

Double-sweep rule (poort R): every region requires two independent sweeps (Sweep A and Sweep B by different agents, blind to each other) plus an explicit reconciliation gate. Error class FK-012.

- **Class:** `CURRENT_CANON`  |  **Integration state:** `ADOPTED`
- **Source:** commit 46fa5260 (2026-08-08); governance/SWEEP_PROTOCOL.md poort R

## PHI-022

Poort S / HUMAN_TOUCHPOINTS_MINIMIZED: GitHub/PR is the communication bridge between INDIA and CCI. Mark is NOT a courier between agents.

- **Class:** `CURRENT_CANON`  |  **Integration state:** `ADOPTED`
- **Source:** commit 46fa5260 (2026-08-08); SWEEP_PROTOCOL poort S

## PHI-023

Poort G.1: mandatory PRIMARY-SOURCE verification of AOAY/Top-11 head claims before a claim counts as confirmed. Introduced as the direct fix for the retracted Ramakrishna/Bodh Gaya claim.

- **Class:** `CURRENT_CANON`  |  **Integration state:** `ADOPTED`
- **Source:** commit 17b92442 (2026-08-08)

## PHI-024

Poort G.2 / Babaji mythic-figure three-axis rule: for a mythic figure, tradition claim, physical claim and evidence tier must be held on three separate axes and never collapsed.

- **Class:** `CURRENT_CANON`  |  **Integration state:** `ADOPTED`
- **Source:** commit "Lock Babaji mythic-figure evidence semantics"; SWEEP_PROTOCOL poort G.2

## PHI-025

Poort L.1 / GEO combination symmetry: 'goed te combineren met' means GEOGRAPHIC/PRACTICAL proximity ONLY, never thematic kinship, and must be symmetric (A names B <=> B names A; a cluster names all its members). With insufficient data, state explicitly 'combineerbaarheid niet betrouwbaar vast te stellen na GEO-controle' rather than guessing or staying silent. Machine-readable `combine_with` field is the canonical source.

- **Class:** `CURRENT_CANON`  |  **Integration state:** `ADOPTED`
- **Source:** commits c4dcda24, 17b92442 (2026-08-08); SWEEP_PROTOCOL poort L.1

## PHI-026

Poort L.2 (Zwaarte voor Mark: pilgrim weight class, magnetism, relative context) and L.3 (factual-claim discipline). Absolute claims ('only/first/always/annually/exact place') must be scoped or removed — precedent: 'the only Thai temple in India' was FALSE (at least two others confirmed in Delhi).

- **Class:** `CURRENT_CANON`  |  **Integration state:** `ADOPTED`
- **Source:** commits 93dfa672, e52b7a9c (2026-08-07/08)

## PHI-027

Poort N: mandatory document order (mission / AOAY-Top11 hits -> decision matrix -> cluster map -> candidate cards -> A/B/C overview) and TEN mandatory candidate fields: Jouw link, Zwaarte, Magnetisme, Waarom-voor-Mark, Ervaring, Praktisch/GEO, Bezoektijd, Reisperiode-relevantie, Afweging, Echte onzekerheid met categorie. Placeholders (NOG NIET ONDERZOCHT / TODO / TBD) are FORBIDDEN for choice-relevant fields and machine-enforced.

- **Class:** `CURRENT_CANON`  |  **Integration state:** `ADOPTED`
- **Source:** commits 93dfa672, 17b92442; governance/scripts/preflight_validator.py --phase pdf

## PHI-028

The one-incident rule: a practical fix made after ONE incident becomes permanent canon only after a SECOND, independent occurrence. Machine-checkable validators may be added immediately. Precedent: poort T, canonised and retracted the same day.

- **Class:** `CURRENT_CANON`  |  **Integration state:** `ADOPTED`
- **Source:** commit 17b92442 (2026-08-08) message body, Deel 3
- **Note:** Exists only in the commit message and SWEEP_PROTOCOL Deel 3.

## PHI-029

Workers (BRONS/ZILVER/GOUD and all colour workers) may NEVER assign a formal or advisory A/B/C. Anything Mark has not chosen stays DOOR_MARK_TE_BEOORDELEN. Only Mark grades.

- **Class:** `CURRENT_CANON`  |  **Integration state:** `ADOPTED`
- **Source:** recovered deleted decisions/MARK_DECISIONS.jsonl record INDIA3-DECISION-0001 (blob 6314e359e86d); restated in current CURRENT_DECISIONS_MASTER.md §1

## PHI-030

A coordinate EXPLICITLY REJECTED by Mark may never be restored as a final point. Unresolved GEO must be isolated per candidate and must never block the other candidates.

- **Class:** `CURRENT_CANON`  |  **Integration state:** `ADOPTED`
- **Source:** recovered deleted decisions/MARK_DECISIONS.jsonl record INDIA3-DECISION-0003 (blob 6314e359e86d); enforced in VNS-CAND-008 handling

## PHI-031

Never claim geographic verification from syntax, counts, or copied coordinates. '40 markers' proves a coverage COUNT only; 'the KML opens' proves SYNTAX only. Never copy an inherited coordinate without an explicit verification action.

- **Class:** `CURRENT_CANON`  |  **Integration state:** `ADOPTED`
- **Source:** recovered deleted india3/migration/ITERATION_1_AUDIT.md (9 principal failures); india3/roles/GOUD.md, ZILVER.md

## PHI-032

Forbidden unqualified words in user-facing output: checked / verified / definitive / complete / correct. Uncertainty must be stated in exact wording, never smoothed.

- **Class:** `CURRENT_CANON`  |  **Integration state:** `ADOPTED`
- **Source:** recovered deleted india3/USER_COMMUNICATION.md

## PHI-033

Evidence, indication and hypothesis must be distinguished; physical identity, spiritual/historical relation and CURRENT VISITABILITY are recorded SEPARATELY and never merged.

- **Class:** `CURRENT_CANON`  |  **Integration state:** `ADOPTED`
- **Source:** recovered deleted india3/roles/BRONS.md, ZILVER.md

## PHI-034

A candidate-specific blocker must never block unaffected candidates (candidate-level isolation of blockers).

- **Class:** `CURRENT_CANON`  |  **Integration state:** `ADOPTED`
- **Source:** recovered deleted india3/roles/ZILVER.md + templates/EXTERNAL_RESEARCH_QUESTIONS.md

## PHI-035

Access-status vocabulary: PUBLIC_OPEN, PUBLIC_LIMITED_HOURS, PRIVATE_PERMISSION_POSSIBLE, EXTERIOR_ONLY, LANDSCAPE_ACCESS, SUCCESSOR_SITE_VISITABLE, ACCESS_UNKNOWN, ACCESS_UNKNOWN_AFTER_EXHAUSTION, PROHIBITED, INSTITUTIONAL.

- **Class:** `CURRENT_CANON`  |  **Integration state:** `ADOPTED`
- **Source:** INDIAGEEL/INDIAROOD/INDIABLAUW current-access matrices (branch-only)

## PHI-036

Seven-layer KML semantics: A_FORMEEL, B_FORMEEL, C_FORMEEL, NOG_DOOR_MARK_TE_BEOORDELEN, CONTEXT_OF_AFGEVALLEN, STATIONS_EN_ROUTEKNOOPPUNTEN, MOGELIJKE_BASES_EN_OVERNACHTING.

- **Class:** `CURRENT_CANON`  |  **Integration state:** `ADOPTED`
- **Source:** KUMAON/BRAJ/CORRIDOR seven-layer KML (branch-only)

## PHI-037

UNESCO World Heritage status is displayed exactly where it applies and increases magnetism, but NEVER auto-upgrades a grade. A B item that is UNESCO WH must be VISIBLY re-reviewed by Mark. The 2026-08-27 UNESCO audit over all 71 active graded items found ZERO current B items that are genuine UNESCO WH, so MARK_REVIEW_TRIGGERS is empty by design.

- **Class:** `CURRENT_CANON`  |  **Integration state:** `ADOPTED`
- **Source:** commit c8b671d6 (2026-08-27); a37423639f7dabb0dfd55c8656d4689bb8a25351:governance/INDIA_MASTER_BOOT.md §7

## PHI-038

Confirmed UNESCO facts from that audit: Sarnath received FULL inscription July 2026 (List 927); Mahabodhi = 1056; Taj Mahal = 252; the Varanasi riverfront ghats are UNESCO TENTATIVE only (tentativelists/6526).

- **Class:** `CURRENT_FACT_WITH_RECHECK_TRIGGER`  |  **Integration state:** `ADOPTED`
- **Source:** commit c8b671d6 (2026-08-27)

---

### Reading order inside this file

`PHI-001` to `PHI-005` are the *why*: the trip's purpose, the governing question, the
NOT_TO_BE_MISSED rules, the place-versus-person weighting, and the AOAY override.
`PHI-006` to `PHI-012` are the *discovery model*: layer priority, religion-independence, the
Top-11, the host axis, and event-versus-location separation.
`PHI-013` to `PHI-018` are the *resolution model*: continuity, parent sites, R1-R5, identity.
`PHI-019` to `PHI-028` are the *method gates*: METHOD_V2, external diversity, the double sweep,
G.1/G.2, L.1/L.2/L.3, N, and the one-incident rule.
`PHI-029` to `PHI-038` are the *honesty constraints*: who may grade, rejected coordinates,
what may not be called verification, forbidden words, and the UNESCO rule.
