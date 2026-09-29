# OPTIONAL-WORLD GLOBAL CALENDAR OPTIMIZER — 2026-09-06

Status: ACTIVE DECISION-PREP / OBJECTIVE PLANNING ONLY
Owner: INDIA17 regisseur
Purpose: determine which optional-world combinations are objectively feasible before Mark compares their subjective content value.

## 1. Scope

Haridwar / Kankhal / Rishikesh is `FINAL_SKIP` and is not part of this optimizer.

Only these optional worlds remain in scope:

1. Braj / Mathura–Vrindavan–Govardhan
2. Kolkata / Calcutta–Hooghly–Serampore–Dakshineswar/Panihati
3. Puri / Odisha / Karar Ashram–Sri Yukteswar–Kriya world

No A/B/C/A+ grade is changed here. No optional world is selected here.

## 2. Two Kumaon universes

The optimizer must run twice.

### H+ — canonical baseline
Haidakhan Vishwa Mahadham — historical riverside Haidakhan Babaji ashram at Village Haidakhan, District Nainital [A+] remains included.

Current Kumaon physical nights:
- Nainital: 3
- Dunagiri/Kukuchina: 3
- true Haidakhan Vishwa Mahadham: 3
- total: 9 physical nights

Haidakhan remains `LOCKED_BY_MARK`; H+ is the actual canon unless Mark explicitly changes it.

### H− — hypothetical sensitivity only
Remove only true Haidakhan Vishwa Mahadham from the calendar, without changing its grade or historical decision status.

Current CCI sensitivity result:
- exactly 3 accommodation/overnight slots are freed;
- Kumaon becomes 6 physical nights / 2 bases;
- one base change disappears;
- two road legs collapse into one direct Dunagiri/Dwarahat/Kukuchina -> Kathgodam/Haldwani/Lal Kuan-side exit;
- expected pure mountain-road saving is roughly 1.5–4 hours, not a whole additional travel day;
- likely genuinely usable waking time recovered is about 1–2 days depending on onward rail timing;
- the two complete Haidakhan full days must NOT be added again on top of the three freed nights.

Therefore `3 freed nights != 3 extra clusters`.

## 3. Fixed calendar inputs

Use these until a later explicit Mark decision supersedes them:

- India accommodation/overnight budget: 33 slots.
- Varanasi/Sarnath: 8 nights, `LOCKED_BY_MARK FOR FIXED-CORE BUDGETING`.
- Agra: 1 hotel night, duration closed.
- Bodh Gaya: 2 nights default; 3 only conditional fallback; max 3.
- Tiruvannamalai/Arunachala: 5 nights, duration closed.
- Kumaon H+: 9 physical nights.
- Kumaon H− sensitivity: 6 physical nights.
- Fixed international departure: AI155 Delhi -> Amsterdam, 21 Jan 2027 12:20.
- Mark planning preference: reach Delhi on 20 Jan 2027 and use one final Delhi night, rather than spend a free full Delhi day on 19 Jan. This remains a preferred/provisional planning constraint, not a licence to weaken departure robustness.
- Overnight rail: 1A target; 2A only explicit fallback.

## 4. Scenario set

For BOTH H+ and H−, coarse-enumerate:

0. no optional world
1. Braj
2. Kolkata
3. Puri
4. Braj + Kolkata
5. Braj + Puri
6. Kolkata + Puri
7. Braj + Kolkata + Puri

Do not infer feasibility from night arithmetic alone. Every included world also carries insertion/exit burden.

## 5. Required dwell modules

For each optional world establish two objective modules:

- `MINIMUM_CREDIBLE`: enough physical time that the world is genuinely visitable and transfers do not dominate it.
- `COMFORTABLE`: no checklist pace and enough recovery/arrival tolerance for this trip.

Current eastern lower-bound planning evidence:
- Kolkata: 2 base nights minimum-plausible; 3 safer/comfortable working module pending D2 exact-date proof.
- Puri: 2 base nights minimum-plausible; 3 safer/comfortable working module pending D3 exact-date proof.
- Braj: D1 must establish the minimum/comfortable module from current canon and actual insertion geometry; do not assume a number without the D1 proof.

## 6. Insertion hypotheses to test, not assume

### Braj
Test all objectively sensible placements:
- Delhi -> Braj -> Agra;
- Braj immediately before Agra if operationally distinct;
- Agra -> Braj -> eastbound core if objectively better;
- return-side insertion near final Delhi only if it actually beats the forward corridor and preserves 20-Jan Delhi robustness.

### Kolkata
Leading hypothesis: Varanasi/Sarnath -> Kolkata -> southern core, but train vs flight and actual weekdays must decide.

### Puri
Leading hypothesis: Varanasi/Sarnath -> Puri -> southern core, including Bhubaneswar-airport alternatives where useful.

### Kolkata + Puri
Must be tested as one possible extended east-coast corridor, not merely as two independent insertions.

## 7. Objective burden vector

Do not produce one arbitrary weighted score.

For every complete calendar track:
- physical nights consumed;
- overnight-travel slots;
- whole-human waking transport burden;
- base changes;
- arrival-quality penalty;
- fragile/weekly-service dependence and connection risk;
- train-class quality and flight count;
- backtracking/time burden;
- rough cost band/delta;
- robustness of final Delhi arrival on 20 Jan;
- residual free nights/hours.

Avoid duplicate axes that describe nearly the same burden. In particular, raw transfer time and waking-day hours lost should be collapsed or clearly distinguished.

## 8. Two-pass method

### PASS 1 — coarse global enumeration
Build one representative best-route calendar for every H+/H− scenario above. Reject impossible or plainly dominated variants early.

### PASS 2 — decision-grade refinement
Only for survivors:
- map actual 2026/27 weekdays;
- refine train/flight/car edges;
- test ±1 day only where weekly services materially alter outcome;
- apply realistic access/check-in/security/fog/delay buffers;
- expose `LIVE_RECHECK_LATER` where Jan-2027 inventory/fare is not yet truly knowable.

Then present a compact non-dominated/Pareto set. If many scenarios remain incomparable, use hard feasibility/robustness gates rather than inventing weights.

## 9. CCI D1–D5 work package — dispatched 2026-09-06

D1 — Braj insertion graph and minimum/comfortable dwell.

D2 — Kolkata actual-date insertion graph.

D3 — Puri actual-date insertion graph.

D4 — Kolkata + Puri combinability as one east-coast corridor.

D5 — global slot/calendar audit across all eight optional combinations under H+ and H−.

Required CCI result header:
`CCI_RESULT — OPTIONAL-WORLD D1–D5 DECISION PACKAGE`

## 10. Current Haidakhan-drop interpretation before D1–D5 closes

Objective result already proved by CCI:

H− returns exactly:
- 3 physical accommodation/overnight slots;
- 1 fewer Kumaon base;
- approximately 1.5–4 hours less mountain-road burden;
- likely 1–2 additional genuinely usable waking days, depending on onward train geometry.

Planning implication, NOT yet final feasibility:
- H− is large enough that one optional world can likely move from tight/minimal to comfortable;
- H− may be the difference between fitting one optional cluster and fitting two, especially `Braj + Kolkata`, `Braj + Puri`, or possibly `Kolkata + Puri`;
- H− does not by itself prove the three-world combination fits;
- exact pair/triple feasibility waits for D1–D5 global enumeration.

## 11. Decision gate for Mark

Do not ask Mark to choose the optional world yet.

First deliver one objective scenario table showing, for H+ and H−:
- how many clusters fit at minimum-credible dwell;
- how many fit comfortably;
- exact feasible singleton/pair/triple combinations;
- robust vs fragile classification;
- calendar/transfer/cost consequences;
- residual slack before 20-Jan Delhi.

Only after that objective surface exists should Mark compare subjective content value among the surviving calendars.
