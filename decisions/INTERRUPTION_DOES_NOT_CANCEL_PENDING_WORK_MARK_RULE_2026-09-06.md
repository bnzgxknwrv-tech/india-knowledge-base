# MARK RULE — INTERRUPTION DOES NOT CANCEL PENDING WORK — 2026-09-06

status: LOCKED_BY_MARK / UNIVERSAL_EXECUTION_RULE
source: explicit Mark instruction 2026-09-06

## RULE
A new Mark message does not cancel unfinished work from earlier messages.

Unless Mark explicitly cancels or replaces it, or the new instruction clearly makes it obsolete:

1. Preserve every unfinished still-valid task from prior messages, including both the penultimate and latest task.
2. Incorporate and answer the newest Mark message.
3. Automatically resume and finish all preserved work in the same execution chain.
4. A rapid or accidental follow-up message is never authorization to abandon earlier unfinished work.
5. Delegated work counts as unfinished until the task has actually been posted/triggered and its status/result has been checked.
6. Before the final reply verify:
   - `PREVIOUS_PENDING_COMPLETE`
   - `CURRENT_REQUEST_COMPLETE`
   - `DELEGATIONS_EXECUTED_OR_BLOCKED`
7. Do not ask Mark to repeat the earlier task merely because a newer message arrived.

## RELATION TO EXISTING RULES
This extends the existing FOUT18 / side-question rule. The earlier rule said a side-question must not cancel the underlying task. This rule applies to **all interruptions**, not only obvious side-questions.

## EXCEPTION
Only stop or discard prior unfinished work when Mark explicitly says to stop/cancel/replace it, or when the newest instruction unambiguously makes that work obsolete.
