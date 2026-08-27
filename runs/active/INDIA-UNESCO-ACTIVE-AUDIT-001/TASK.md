# INDIA — UNIVERSAL UNESCO ACTIVE-CANON AUDIT

Status: READY
Branch ONLY: `agent/india-unesco-active-audit`
Repository: `bnzgxknwrv-tech/india-knowledge-base`

## PURPOSE
Audit ALL currently active trip content with grades/statuses A+, A, A* or B for official UNESCO World Heritage status.

Mark has explicitly said that UNESCO World Heritage has extra magnetism for him. A current B may therefore deserve a later Mark re-review if it is genuine UNESCO World Heritage.

This task is a STATUS AUDIT ONLY. Do NOT change any A+/A/A*/B/C grade.

## MINIMUM READ SET
Read current truth, not stale handoffs as authority:
1. `governance/ACTIVE_FRAMEWORK.md`
2. `governance/MARK_TRAVEL_PREFERENCES_CURRENT.md`
3. `governance/CURRENT_STATE.md`
4. `runs/active/INDIAZILVER-ENTITY-ID-PROXIMITY-BACKFILL-001/PROTECTED_CANON_BASELINE.csv`
5. `runs/active/INDIA10-CLUSTER-COVERAGE-REAUDIT-001/A_PLUS_MARK_DECISION_LOG.md`
6. latest current decision artifacts referenced by CURRENT_STATE, including post-baseline grade changes.

If current files conflict, resolve by newest explicit Mark decision. Do not resurrect C or superseded items.

## SCOPE
Audit every CURRENT active:
- A+
- A
- A*
- B

Across the whole current trip universe, including fixed-core and still-active optional worlds where these grades remain current.

Do NOT spend time re-auditing C items except when necessary to establish that an old item is no longer active.

## OFFICIAL SOURCE RULE
Only official UNESCO World Heritage Centre evidence may justify `UNESCO WH` or `UNESCO TENTATIVE`.

Use current 2026 UNESCO status.

Known trap: Sarnath was formerly Tentative but was inscribed in July 2026. Do not rely on stale tentative-only pages.

## EXACT STATUS LABELS
For each current A+/A/A*/B item, assign exactly one of:
- `UNESCO WH` — item itself is an inscribed World Heritage property or an official component of one;
- `UNESCO TENTATIVE` — item itself is on UNESCO Tentative List but not inscribed;
- `UNESCO NEAR/BUFFER ONLY` — close to / within buffer or same city/precinct, but item itself is not a listed component/property;
- `NO UNESCO WH/TENTATIVE` — no official UNESCO WH or Tentative status found for the item itself.

Do NOT label an entire city/cluster `UNESCO WH` merely because one component inside it is listed.

## COMPONENT PRECISION — HARD
Where a serial property has multiple components, give:
- official UNESCO property name;
- exact component name if applicable;
- UNESCO list number if easily available;
- whether the current Mark item equals the component, contains it, or merely sits nearby.

Examples of the level of precision required:
- Sarnath: distinguish official Sarnath components from unrelated temples/museum items nearby;
- Delhi: distinguish individual properties/components from the generic city;
- Agra: Taj Mahal, Agra Fort, Fatehpur Sikri are separate UNESCO properties;
- Keoladeo = separate UNESCO natural property;
- Mahabalipuram = Group of Monuments at Mahabalipuram, not generic Chennai corridor.

## MARK REVIEW TRIGGER
Every CURRENT `B` with genuine `UNESCO WH` must also get:
`MARK_REVIEW_TRIGGER = YES`

This does NOT change B. It means central INDIA must later show it to Mark for possible B->A review because UNESCO WH is a newly explicit Mark preference.

For A/A*/A+ with UNESCO WH, label it but do not reopen unless current central planning needs it.

## OUTPUT
Write ONE file directly to this branch:
`runs/active/INDIA-UNESCO-ACTIVE-AUDIT-001/UNESCO_ACTIVE_CANON_AUDIT.md`

Required sections:
1. `EXECUTIVE SUMMARY`
   - total current A+/A/A*/B audited;
   - count UNESCO WH;
   - count UNESCO TENTATIVE;
   - count B + UNESCO WH review triggers;
   - uncertainties.

2. `MARK_REVIEW_TRIGGERS`
   - ONLY current B items with genuine UNESCO WH;
   - full recognition-rich name;
   - current grade B;
   - official UNESCO property/component;
   - concise reason why the match is exact.

3. `FULL ACTIVE TABLE`
Columns:
- cluster
- current full item name + Dutch recognition hook if known
- current grade/status
- UNESCO label
- official UNESCO property name
- component name if relevant
- UNESCO source URL/title
- precision note (`exact property`, `exact component`, `near/buffer only`, etc.)
- Mark review trigger YES/NO

4. `FALSE-FRIENDS / IMPORTANT NON-MATCHES`
List items where generic online descriptions often incorrectly imply WH status, but official UNESCO precision says otherwise.

5. `CURRENT-CANON INPUTS USED`
List files/commits used to establish current active grades.

## NO GRADE MUTATIONS
Do not edit A_PLUS_MARK_DECISION_LOG, protected canon, CURRENT_STATE or any Mark decision file.
Do not create A+/A/A*/B/C decisions.

## QUALITY BAR
- completeness of current active A+/A/A*/B is more important than finding extra attractions;
- no generic UNESCO discovery outside current active content;
- no Wikipedia-only status decisions;
- no stale pre-2026 Sarnath conclusion;
- if official UNESCO evidence is ambiguous, label uncertainty explicitly rather than guessing.

## COMPLETION
When complete:
1. commit `UNESCO_ACTIVE_CANON_AUDIT.md` on this SAME branch;
2. final chat response must contain branch + commit SHA + output path only, plus at most one sentence on number of B review triggers.

END TASK