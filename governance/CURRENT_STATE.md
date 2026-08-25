# CURRENT STATE — INDIA

Last updated: 2026-08-25
Purpose: compact durable boot state. Older handoffs are provenance only.

## MANDATORY BOOT
1. Read `README.md`.
2. Read `governance/INDIA_REGIE_CRITICAL_BOOT_AND_NO_DEFERRAL_2026-08-23.md`.
3. Read `governance/INDIA_SUCCESSOR_BOOT_PROTOCOL.md`.
4. Read THIS file.
5. Reconcile protected canon + later Mark supersedes before presenting anything as new.
6. Read only task/output files relevant to the active question.
7. Check PR #23 before a major central build/write.

## EXECUTION / REPLACEABILITY — HARD
Mandatory loop: `SCAN -> DO -> RECORD -> RESCAN -> repeat -> REPLY`.
Every INDIA-regisseur is disposable. Before reply ask: `IF THIS INDIA DISAPPEARS NOW, CAN THE NEXT INDIA CONTINUE FROM GITHUB ALONE?` If not, update GitHub first.
A user interruption does not cancel unfinished work unless Mark explicitly STOPs/cancels/supersedes it.

## USER-FACING NAME PROTOCOL — ABSOLUTE HARD
Every Indian/non-obvious place, institution, temple, ashram, ghat, cave, festival, local term or experience shown to Mark MUST be written every time as:
`CLUSTER / PLAATS / PLEK (korte Nederlandse uitleg: wat het concreet is / waarom relevant) — huidige status: A+ / A / A* / B / C / OPEN`.
This also applies in headings, tables, recaps, shorthand confirmations and side references. Never rely on Mark remembering local names.
For EVERY walk/hike/loop shown to Mark, the explanatory name MUST contain approximate walking distance + realistic walking duration FROM THE PHYSICAL WALK START/TRAILHEAD. It must also state separately how far/time the walk start lies from the relevant A+/A/A* anchor. Never write a bare walk distance that can be confused with distance from hotel/base/anchor. If any metric is not verified, explicitly write `nog te verifiëren`.
For Manikarnika always preserve: `VARANASI / MANIKARNIKA / Manikarnika Ghat (heilige crematieghat waar Lahiri Mahasaya werd gecremeerd) — ...`.
Never abbreviate:
- `BODH GAYA / BAKRAUR / Sujata Stupa (plek waar Sujata de uitgemergelde Siddhartha voedsel gaf; keerpunt van extreme ascese naar de Middenweg vóór zijn verlichting) — ...`
- `BODH GAYA / DUNGESHWARI HILLS / Dungeshwari–Mahakala Caves (grotten waar Siddhartha extreme ascese beoefende vóór Sujata en de verlichting) — ...`
`kosten` / `gratis` are money-only words; logistics use reistijd/extra reistijd/omweg/duur.

## GRADE SEMANTICS — ABSOLUTE HARD / MARK 2026-08-25
- `A+` = KERNLOCATIE / DIT IS WAAROM MARK DEZE REIS MAAKT. Nul discussie over inclusion. Route may bend/omrijden solely for it.
- `A` = Mark wil hier HEEL GRAAG OOK heen. Default PLAN/RETAIN. Re-open only if actual burden is clearly disproportionate: very large detour, isolated major excursion, unusually long visit, extra night(s), or material collision with stronger priorities. Distance/time is a discussion trigger, never an automatic downgrade.
- `A*` = DISPLAY SUBTYPE OF FORMAL `A`, NOT A FIFTH FORMAL GRADE. Corridor/bycatch A: not one of Mark's original first-choice destinations, but an attractive extra discovery retained because it fits the route unusually well. Operationally `SKIP_FIRST`: if Mark is tired, delayed, weather is poor or the day is overloaded, A* may be skipped before intrinsic A. A* must not by itself force a dedicated detour, extra night or major schedule sacrifice. Always display the `*` plus parenthetical explanation. Canon: `formal_grade=A`, `display_subtype=A*`, `reason=CORRIDOR_BYCATCH/EASY_CAPTURE`, `operational_priority=SKIP_FIRST`.
- `B` = reserve/bycatch only. Normally NOT planned. Only consider if already there, almost frictionless, or unexpected spare time. A B may not independently steer route/create taxi outing/half-day/night.
- `C` = NIET heen. Do not plan, route for, optimize for or re-present unless Mark explicitly reopens it.
- `OPEN` regional/traveler/Lonely-Planet/Komoot finding = ungraded and may become A+, intrinsic A, A*, B or C. Provenance never limits maximum grade.
- Model `A*`: KUMAON / KAKRIGHAT / Kakrighat (Kosi-rivierplek waar Vivekananda in 1890 een belangrijke realisatie had; inhoudelijk gewenst maar door corridor vrijwel gratis mee te nemen) — huidige status: A* (formeel A; corridor-bijvangst, SKIP_FIRST).

## MARK DECISION CARD — HARD
Never ask Mark to choose from a bare name or isolated distance. Each real decision card includes: who/tradition, what happened, why relevant, what is visitable now, current status, relevant A+ anchors, corridor relation, practical distance/time, incremental detour, bundle vs side excursion, likely time/day impact.
For walk cards additionally include walk start/trailhead, loop/out-and-back, elevation where available, winter fit, and Komoot exact/best-searchable route or Highlight name if found.

## CORRIDOR-FIRST METHOD — GLOBAL HARD
Judge against mandatory corridors BETWEEN fixed A+ anchors, not just nearest-base distance.
Classes: `ON_CORRIDOR`, `SMALL_TRANSFER_DETOUR`, `ALTERNATIVE_CORRIDOR_BUNDLE`, `TRUE_SIDE_EXCURSION`, `OFF_CORRIDOR_DROP`.
Handling: C remove; A+ protect absolutely; intrinsic A assume retain and first seek easy capture/bundles; A* retain as optional corridor extra but SKIP_FIRST; B never route for; OPEN -> hard cuts -> easy captures -> alternative bundles -> true ties / possible A+ magnets.
Working friction bands are advisory only. Over ~150 min extra or standalone half/full day is a legitimate discussion trigger for an existing intrinsic A, not an automatic downgrade.

## KOMOOT WALK DISCOVERY LAYER — HARD
Komoot is now a separate discovery layer ABOVE regional + traveler/Lonely-Planet, not just a verifier. Controlling file:
`runs/active/INDIA10-CLUSTER-COVERAGE-REAUDIT-001/KOMOOT_WALK_DISCOVERY_LAYER_2026-08-25.md`.
Use Komoot to:
1. find exact/searchable route or Highlight names for already selected A+/A/A* walks;
2. discover exceptional walks around A+/A anchors;
3. discover short high-payoff nature stops along A+ transfer corridors;
4. search Highlights/categories as well as exact route names because Indian indexing is incomplete;
5. compare multiple walks to the same attraction and retain only the most beautiful/practical variants.
Mark preferences: forest lakes, blue/green water, waterfalls/cascades, river/gorge, forest immersion, dramatic viewpoints/ridges, caves, spiritually meaningful paths, short high-reward walks. Suppress mediocre/generic/repetitive walking content.
There is currently no installable Komoot plugin available through the connected plugin catalog, so public Komoot web pages/indexes/Highlights and broader current web research remain the execution method.

## CENTRAL TRUTH / ACTIVE FILES
Branch: `agent/india8-cluster-casting`.
- `runs/active/INDIA10-CLUSTER-COVERAGE-REAUDIT-001/A_PLUS_MARK_DECISION_LOG.md`
- `runs/active/INDIA10-CLUSTER-COVERAGE-REAUDIT-001/CURRENT_OLD_A_PROMOTION_MASTER.md` — old-A promotion CLOSED.
- `runs/active/INDIA10-CLUSTER-COVERAGE-REAUDIT-001/TRAVELER_OVERLAY_CORRIDOR_PASS_2026-08-24.md` — regional/traveler/LP overlay.
- `runs/active/INDIA10-CLUSTER-COVERAGE-REAUDIT-001/KOMOOT_WALK_DISCOVERY_LAYER_2026-08-25.md` — active Komoot overlay.
- `runs/active/INDIA10-CLUSTER-COVERAGE-REAUDIT-001/A_PLUS_WALK_COVERAGE_MATRIX_2026-08-25.md` — current A+ walk coverage/status matrix.
- `runs/active/INDIA10-CLUSTER-COVERAGE-REAUDIT-001/GLOBAL_TRANSFER_LEDGER_2026-08-25.md` — HARD transport bridge; raw travel times may never be treated as full calendar blocks.
- `runs/active/INDIA10-CLUSTER-COVERAGE-REAUDIT-001/CLUSTER_TOPOLOGY_FEASIBILITY_2026-08-25.md` — ACTIVE global zoom-out/topology truth before any new calendar.
- `runs/active/INDIA10-CLUSTER-COVERAGE-REAUDIT-001/KUMAON_TRAVELER_HARD_CUT_MARK_DECISIONS_2026-08-24.md`.
- `runs/active/INDIA10-CLUSTER-COVERAGE-REAUDIT-001/KUMAON_TRAVELER_EASY_CAPTURE_PASS_2026-08-24.md`.
- `runs/active/INDIA10-CLUSTER-COVERAGE-REAUDIT-001/KUMAON_EASY_CAPTURE_MARK_DECISIONS_2026-08-25.md` — latest Kumaon Mark decisions + A* SKIP_FIRST + walk-name rule.
- corridor matrices: Kumaon, Varanasi, Bodh Gaya in same run directory.
- traveler master: `runs/active/INDIA10-MULTIAI-TRAVELER-DISCOVERY-001/TRAVELER_EXPERIENCE_MASTER_UNION_LEDGER.md` — 150 canonical rows from 221 represented raw inputs.
Regional discovery: 8/8 integrated.

## FIXED CORE WORLDS
1. Kumaon
2. Varanasi / Sarnath
3. Bodh Gaya / Gaya
4. Tiruvannamalai / Arunachala
5. Delhi
6. Agra / Taj Mahal
Reserve/deferred until fixed-core footprint known: Braj/Vrindavan/Mathura/Govardhan; Haridwar/Kankhal/Rishikesh; Prayagraj; out-of-radius challengers; Mysore/Bengaluru unless explicitly reopened.

## CURRENT A+ SPINE
### KUMAON
- KUMAON / KUKUCHINA-DUNAGIRI / Mahavatar Babaji's Cave (bezoekbare YSS/Kriya-pelgrimsgrot; hoofdreden voor de reis) — A+.
- KUMAON / KAINCHI / Kainchi Dham (Neem Karoli Baba-ashramcomplex; kernplek voor Neem Karoli Baba en Ram Dass) — A+.
- KUMAON / NAINITAL / Hotel Evelyn (historisch hotel waar Ram Dass verbleef; exacte kamer niet bewezen) — A+.
- KUMAON / NAINITAL / Naini Lake-rondwandeling (ca. 3,2 km / 55–75 min; volledige lus via Mall Road en de autovrije Thandi Road; voorkeur vroeg in de ochtend) — A+.
- KUMAON / HAIDAKHAN / Haidakhan Ashram (Haidakhan Babaji-pelgrimsashram; gewenste ashramovernachting) — A+.
- KUMAON / HAIDAKHAN / Historische Haidakhan-grot (grot uit aparte Haidakhan Babaji-traditie; niet dezelfde claim als Mahavatar Babaji's Cave bij Kukuchina/Dunagiri) — A+.

### VARANASI / SARNATH
- VARANASI / OLD CITY / Varanasi Kriya core (Lahiri Mahasaya-huis + samadhi + Yogananda/Sri Yukteswar-zone) — A+ parent.
- VARANASI / SARNATH / Sarnath sacred/archaeological complex (Boeddha's eerste-preeklandschap) — A+ parent.
- VARANASI / PANCHGANGA / Shri Tailanga Swami Math + Panchganga Ghat + Bindu Madhav Temple (heilige wereld rond yogi Tailanga Swami) — A+.
- VARANASI / BHADAINI / Shree Shree Ma Anandamayi Ashram (bezoekbaar ashram van Anandamayi Ma) — A+.
- VARANASI / OLD CITY / Kashi Vishwanath sacred core (grote Shiva-tempel + nabijgelegen heiligdommen) — A+.
- VARANASI / MANIKARNIKA / Manikarnika Ghat (heilige crematieghat waar Lahiri Mahasaya werd gecremeerd) — A+ parent/bundle; Ratneshwar Mahadev Temple is CHILD_A+.
- VARANASI / DASHASHWAMEDH / Dashashwamedh Ghat + Shitala Mata Temple (grote Ganga-Aarti-zone) — A+.
- VARANASI / ASSI / Assi Ghat (zuidelijke ochtend-/pelgrimsghat) — A+.

### BODH GAYA / GAYA
- BODH GAYA / BODH GAYA / Mahabodhi Temple Complex (Boeddha-verlichtingscomplex) — A+ parent; Bodhi Tree/internal enlightenment microsites inherit.
- BODH GAYA / BAKRAUR / Sujata Stupa (plek waar Sujata de uitgemergelde Siddhartha voedsel gaf; keerpunt van extreme ascese naar de Middenweg vóór zijn verlichting) — A+.
- BODH GAYA / DUNGESHWARI HILLS / Dungeshwari–Mahakala Caves (grotten waar Siddhartha extreme ascese beoefende vóór Sujata en de verlichting) — A+.

### TIRUVANNAMALAI / ARUNACHALA
- ARUNACHALA / TIRUVANNAMALAI / Arunachala / Ramana sacred world (heilige berg, ashram en directe Ramana Maharshi-levensplekken) — A+ parent.

### DELHI
- DELHI / CHHAWLA / Nirmal Dham (rustplaats/Mahasamadhi van Shri Mataji Nirmala Devi) — A+.

### AGRA
- AGRA / AGRA / Taj Mahal — A+; sunrise/earliest practical opening HARD.

## LATEST MARK TRAVELER / CORRIDOR DECISIONS — KUMAON
- KUMAON / MUNSIYARI / Munsiyari + Panchachuli views (ver oostelijk Himalayadorp met grote Panchachuli-bergpanorama's; aparte verre Kumaon-uitstap) — C.
- KUMAON / CHAUKORI / Chaukori Tea Gardens + Panchachuli views (hooggelegen theedorp met Himalaya-uitzicht en theevelden; forse oostelijke omweg buiten A+-ruggengraat) — C.
- KUMAON / NAMIK-RANTHAN / Namik–Ranthan high-Himalaya trek (afgelegen meerdaagse bergtrek richting Ranthan Top/Namik; aparte trekkingreis) — C.
- KUMAON / KAKRIGHAT / Kakrighat (Kosi-rivierplek waar Vivekananda in 1890 een belangrijke realisatie had; inhoudelijk gewenst maar door corridor vrijwel gratis mee te nemen) — A* (formeel A; corridor-bijvangst, SKIP_FIRST).
- KUMAON / DWARAHAT / Dwarahat historic temple groups (acht hoofdgroepen van 11e-eeuwse stenen tempels in het stadje dat al op de verplichte Babaji-corridor ligt) — A* (formeel A; corridor-bijvangst, SKIP_FIRST).
- KUMAON / BHIMTAL / Butterfly Research Centre (klein gespecialiseerd vlinder- en mottenmuseum/onderzoekscentrum in een bungalow bij Bhimtal) — C.
- KUMAON / SATTAL / Sattal / Seven Lakes (zeven bosmeren voor natuurwandeling en vogels; mooie transfer-bijvangst die Mark graag ziet maar waarvoor niet zelfstandig moet worden omgereden) — A* (formeel A; corridor-bijvangst, SKIP_FIRST).
- KUMAON / NAINITAL / Sakley's Restaurant & Pastry Shop (historisch café/banketadres uit 1944 in Nainital; ligt in Mallital, het noordelijke deel van Nainital) — A* (formeel A; base-bijvangst, SKIP_FIRST).
- KUMAON / RANIKHET / Kumaon Regimental Centre Museum (leger-/regimentsmuseum met oorlogstrofeeën, uniformen en historische stukken; ligt in Ranikhet op de Kainchi→Dwarahat/Babaji-corridor) — C.
- KUMAON / NAINITAL / Naina Peak-wandeling (ca. 6 km retour / ca. 3–5 uur; bosklim naar het hoogste punt boven Nainital met groot Himalaya-uitzicht) — B.
- KUMAON / DHOKANEY-SUYALBARI / Dhokaney Waterfall-wandeling (ca. 1,0–1,2 km retour / ca. 30–45 min lopen from waterfall access/trailhead; start reached by ca. 25–30 km road transfer from Kainchi Dham A+ anchor) — A.
- KUMAON / KATARMAL / Katarmal Sun Temple-wandeling (ca. 3 km retour / ca. 1–1¾ uur lopen from road/parking start below the temple complex; separate deviation from direct Babaji corridor) — B.
- KUMAON / ALMORA / historische bazaarwandeling (loopafstand nog te verifiëren / ca. 2 uur lopen from a start in Almora town; requires deliberate Almora deviation) — C.

## GLOBAL CALENDAR CORRECTION — HARD 2026-08-25
The earlier conversational/daily calendar layer is NON-AUTHORITATIVE because transfer time was not consistently deducted as occupied day time. Do not reuse old day/date sketches as itinerary truth.

Active method now:
`SELECTED SITES -> REAL DOOR-TO-DOOR TRANSFER BLOCKS -> GLOBAL CLUSTER TOPOLOGY -> MARK CLUSTER/DWELL-TIME CHOICES -> NIGHT SCENARIOS -> EXACT DATES`.

Hard consequences:
- raw road/rail/flight duration is never the complete travel-day duration;
- exact dates remain blocked until topology + selected dwell-time ranges are known;
- 31 Dec 2026 in Rishikesh is a `DATE_WISH`, not a calendar lock;
- protected A+/A and hotel decisions remain valid; the invalidation concerns the calendar/timing layer, not location research.

## CURRENT GLOBAL TOPOLOGY — ACTIVE HYPOTHESIS, NO DATES
Read `CLUSTER_TOPOLOGY_FEASIBILITY_2026-08-25.md` + `GLOBAL_TRANSFER_LEDGER_2026-08-25.md` before any new route/calendar advice.

Current strongest geometry to test first:
`DELHI -> optional HARIDWAR/RISHIKESH -> KUMAON (HAIDAKHAN -> NAINITAL -> KAINCHI -> DWARAHAT -> DUNAGIRI/KUKUCHINA) -> major Kumaon exit to plains -> optional BRAJ -> AGRA -> optional PRAYAGRAJ -> BODH GAYA/GAYA -> VARANASI/SARNATH -> VNS->BLR nonstop hypothesis -> road BLR->TIRUVANNAMALAI/ARUNACHALA`.

Current feasibility read:
- KUMAON: FIXED / REALISTIC / HIGH TRANSFER BURDEN; actual exit is from eastern Dwarahat/Dunagiri end, not Nainital.
- HARIDWAR/RISHIKESH/KANKHAL: OPTIONAL / REALISTIC / MODERATE EXTRA BURDEN; natural placement is once between Delhi and Kumaon; do not date-force a bounce.
- BRAJ: OPTIONAL / LOW GEOMETRIC BURDEN adjacent to Agra.
- PRAYAGRAJ: OPTIONAL / LOW-TO-MODERATE GEOMETRIC BURDEN on eastbound rail axis.
- BODH GAYA/GAYA + VARANASI/SARNATH: natural protected eastern pair.
- SOUTHBOUND: current strong hypothesis is finish east in Varanasi, then current daily/nonstop VNS->BLR (~2h35 block today) + ~232 km/~3h33 raw road BLR airport->Tiruvannamalai; exact Dec 2026/Jan 2027 service MUST be rechecked before lock.
- Gaya->Chennai currently has no nonstop and is therefore downranked as the default southbound topology.
- Bengaluru is an airport gateway only, not automatically a sightseeing cluster.

## CURRENT FRONTIER
PRIMARY: GLOBAL_CLUSTER_TOPOLOGY_FEASIBILITY + REAL_TRANSFER_BURDEN. Do not return to exact day planning yet.

Goal now is to determine which optional clusters are genuinely feasible around the fixed A+ spine once travel burden counts correctly. Exact number of days per cluster remains intentionally open because Mark is still deciding desired dwell time.

Parallel preserved work:
- traveler/regional/LP overlay remains valid;
- Komoot overlay remains valid and should continue to enrich selected routes/anchors, but it must not distract from the current global travel-time/topology correction.

## OPEN AUTONOMOUS GEO / OPS WORK
- exact protected GPS for the Babaji cave claimant before final precise Kumaon route math;
- Haidakhan ashram <-> historical Haidakhan cave exact route relation before final schedule;
- exact eastern Kumaon final-base -> plains transfer closure is high priority because it controls global topology time;
- exact Dec 2026/Jan 2027 VNS->BLR service recheck only when inventory/timetable is available and date selection approaches;
- exact winter day routing later; never fake precision.

## REPLACEABILITY CHECKPOINT
If INDIA10 disappears, INDIA11 must NOT reconstruct this from chat. Boot normally, then use:
1. this CURRENT_STATE;
2. `GLOBAL_TRANSFER_LEDGER_2026-08-25.md`;
3. `CLUSTER_TOPOLOGY_FEASIBILITY_2026-08-25.md`;
4. protected canon/Mark decision files.
The current user question is global feasibility of clusters with real transfer time included, especially whether Haridwar/Rishikesh remains worthwhile or creates excessive route friction. Do not prematurely ask for exact dates.