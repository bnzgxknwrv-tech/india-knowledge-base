# INDIA11 — UNESCO CURRENT-CANON SWEEP — ZILVER

status: READY
role: INDIA ZILVER
branch: agent/indiazilver-cluster-completeness-audit
central_regie_branch: agent/india8-cluster-casting
purpose: one consolidated UNESCO audit so Mark is not used as courier and INDIA11 can continue Varanasi planning in parallel.

## WHY
Mark stated that UNESCO World Heritage status creates extra magnetism for him and can make an existing B worth reconsidering as A. This status must therefore be visible in the recognition-rich display name of every current A+/A/A*/B item when applicable.

## SCOPE — ONE QUESTION, ONE OUTPUT
Audit ALL CURRENT A+/A/A*/B items across the India trip canon. Do NOT audit C items except where needed to resolve component boundaries. Do NOT invent or change grades.

Use the newest current canon/decision truth on central branch `agent/india8-cluster-casting` as reference, especially:
- governance/CURRENT_STATE.md
- runs/active/INDIA10-CLUSTER-COVERAGE-REAUDIT-001/A_PLUS_MARK_DECISION_LOG.md
- runs/active/INDIAZILVER-ENTITY-ID-PROXIMITY-BACKFILL-001/PROTECTED_CANON_BASELINE.csv
- latest cluster decision artifacts where newer than protected baseline.

## SOURCE STANDARD
Primary authority: official UNESCO World Heritage Centre pages/list only.
If needed use official ASI/state source only to disambiguate exact physical component/site identity, never as substitute for UNESCO inscription status.

Distinguish EXACTLY:
- `UNESCO WH` = currently inscribed World Heritage property/component;
- `UNESCO WH — COMPONENT OF <property>` = exact current item is a named component of a serial/cluster property;
- `UNESCO TENTATIVE` = only on Tentative List, NOT World Heritage;
- `NO UNESCO WH MATCH` = no current inscription match found;
- `AMBIGUOUS_COMPONENT` = surrounding city/region is UNESCO but exact item may lie outside the inscribed property; explain.

Do NOT label an entire neighborhood/city `UNESCO WH` merely because one component inside it is inscribed.

Important fresh example to handle correctly:
- Ancient Buddhist Site of Sarnath was inscribed in 2026. Verify the exact official property/component boundaries/names. The user-facing Sarnath label should explain what Mark physically visits, not just say `Sarnath`.

## REQUIRED OUTPUT PER CURRENT A+/A/A*/B ITEM
For each item:
1. exact current canon name;
2. current grade/status copied, never changed;
3. exact UNESCO label from the list above;
4. official UNESCO property name if matched;
5. exact component/boundary explanation where relevant;
6. official UNESCO URL/provenance;
7. `B_REVIEW_TRIGGER = YES/NO` where YES only if current grade is B and exact item is UNESCO WH/component. Do NOT recommend the new grade; only flag for Mark review.

## ALSO PRODUCE
A compact `MARK_REVIEW_ONLY` section containing ONLY current B items with `B_REVIEW_TRIGGER=YES`, recognition-rich Dutch display names, why UNESCO applies, and zero grade mutation.

A `DISPLAY_LABEL_PATCH` section giving the exact suffix to append to current Mark-facing names, e.g.:
- `— A [UNESCO WH]`
- `— B [UNESCO WH — component van ...]`
- `— A [UNESCO TENTATIVE]`
Only append a label when UNESCO/Tentative actually applies.

## DO NOT
- do not change A+/A/A*/B/C;
- do not re-open C;
- do not search for new attractions;
- do not build route/day plans;
- do not use tourism sites as authority for UNESCO status;
- do not ask Mark anything;
- do not create multiple output files.

## OUTPUT
Write exactly ONE file on this same worker branch:
`runs/active/INDIA11-UNESCO-CURRENT-CANON-SWEEP-001/UNESCO_CURRENT_CANON_SWEEP.md`

End with:
`status: COMPLETE`

INDIA11 central regie will poll GitHub itself, inspect the output, integrate labels/current B review candidates, and continue planning without asking Mark to shuttle text.
