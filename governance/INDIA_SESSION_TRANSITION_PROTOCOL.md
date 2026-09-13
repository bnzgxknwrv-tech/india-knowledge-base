# INDIA SESSION TRANSITION PROTOCOL — MANDATORY EXTRACTION-FIRST HANDOFF

Status: **HARD / MANDATORY / EVERY INDIA<N> -> INDIA<N+1> TRANSITION**
Effective: 2026-09-13
Branch: `agent/india8-cluster-casting`
Trigger for creation: this exact failure recurred roughly 20 times across INDIA1-20 before being made a fixed, always-applied procedure instead of something CCI or a successor had to re-derive each time (Mark, 2026-09-13: "dit is iets wat nu al 21 keer voorgekomen is... dit moet toch wel inmiddels bekende zaak zijn").

## WHY THIS EXISTS

An outgoing INDIA<N> ChatGPT session's real memory is not just what it has committed to GitHub. It also holds live conversational context — an in-progress discussion, a half-formed idea, a question Mark just asked that has not yet been written anywhere — that exists ONLY inside that session. Git archaeology (reading commits, diffs, current governance files) can reconstruct everything that was ever durably written, but it can never recover a conversation thread that never left the chat.

Concrete incident that forced this file into existence: while INDIA20 was ending, CCI reconstructed a full "INDIA20 final extraction" purely from git history and current governance files, without first asking the still-live INDIA20 session to dump its own memory. That reconstruction completely missed an active, undocumented discussion between Mark and INDIA20 about Crank's Ridge/Kasar Devi, a house connected to Ram Dass, and a hippie commune that had been there historically — reopened specifically because a day had just become free (21 Dec, per `d6c5834`). None of that thread existed in any committed file, so no amount of careful git-history reading could have found it. Mark caught the gap only because he happened to remember what the live conversation had actually been about.

## THE HARD RULE

**Whenever an INDIA<N> session is ending (context filling, Mark says it must stop, or a successor is being started for any reason), the FIRST and only first action is to have INDIA<N> itself — while it is still reachable — write and commit its own complete final extraction to GitHub. Nothing else in the transition may start before that.**

This applies even if CCI, a prior extraction, or the committed governance files already seem to tell a complete story. They cannot prove the absence of an undocumented live thread; only asking the outgoing session can.

## THE FIXED SEQUENCE — FOLLOW EVERY TIME, DO NOT RE-DERIVE

1. **DETECT.** Notice or be told that INDIA<N> is ending.
2. **REQUEST THE DUMP FIRST — MANDATORY, NEVER SKIPPED.** Whoever has access to the live INDIA<N> session (normally Mark, since INDIA<N> sessions run in ChatGPT, not in this GitHub-integrated session) sends it a direct instruction to write a complete final extraction to `runs/active/INDIA<N>_FINAL_EXTRACTION_<date>.md` and commit it to `agent/india8-cluster-casting` — not merely describe it in chat. The instruction must explicitly ask for: (a) everything already committed that a successor needs routed to; (b) every open Mark-only decision; (c) **any live, in-progress, undocumented discussion thread** — this is the part git archaeology cannot recover and is exactly what step 2 exists to capture; (d) the exact next action. A ready-to-paste version of this request is maintained in section "COPY-PASTE REQUEST" below so it never has to be reworded from scratch.
3. **WAIT AND VERIFY.** Confirm the extraction file actually landed on the branch (`git log`, `git show`) before treating the transition as started. Read it in full.
4. **RECONCILE, DO NOT SUBSTITUTE.** CCI may enrich or cross-check the real extraction against git history (exactly as done for the person-provenance and grade-sync repairs elsewhere in this project), but CCI's own git-archaeology reconstruction is NEVER a substitute for step 2. If INDIA<N> is genuinely and permanently unreachable (confirmed, not merely assumed) and step 2 cannot be performed at all, CCI may reconstruct a best-effort extraction from git history, but it MUST be explicitly labeled as reconstructed/partial and flagged that any purely-conversational content could be missing — never presented as equivalent to a real self-written extraction.
5. **THEN, AND ONLY THEN, BOOT THE SUCCESSOR.** Follow `governance/INDIA_MASTER_BOOT.md` and `governance/INDIA14_START_AND_INDEPENDENT_CHECK.md` exactly as written: a genuinely separate session boots as INDIA<N+1> with its own fresh nonce (never invented by CCI on the successor's behalf — the nonce comes from Mark or the start prompt), writes its own receipt, and gets a genuinely independently-authored CHECK — never the same session grading its own boot.
6. **NUMBER CLASH GUARD.** If a label (`INDIA<N+1>`) was already used for anything other than a real, separately-booted successor session (for example, a self-administered exercise CCI ran under that label by mistake), do not reuse that exact label for the real successor — increment past it and record why, so `boot_receipts/`/`boot_checks/` history stays unambiguous about which artifact came from a genuinely separate session.

## COPY-PASTE REQUEST — SEND THIS TO THE OUTGOING SESSION, EVERY TIME

```
Je context raakt vol. Voordat je stopt: schrijf NU een volledig overdrachtsdocument naar GitHub (niet alleen aan mij in de chat vertellen) op het pad runs/active/INDIA<N>_FINAL_EXTRACTION_<datum>.md, commit het naar branch agent/india8-cluster-casting. Dit moet in elk geval bevatten: (1) alles wat al gecommit is en waar een opvolger naartoe moet worden gerouteerd; (2) alle nog openstaande Mark-only beslissingen; (3) ELK lopend, nog niet ergens vastgelegd gespreksonderwerp tussen jou en mij, ook als het nog niet af is — dit is het deel dat een opvolger NERGENS anders kan terugvinden; (4) de exacte eerstvolgende actie. Schrijf dit alsof de volgende opvolger jou nooit heeft gesproken en dit gesprek dus nooit meer kan navragen.
```

Replace `<N>` and `<datum>` with the actual session number and date before sending.

## SUCCESSOR RULE

Every future INDIA<N> or CCI session that participates in a transition must follow this exact sequence without needing Mark to re-explain it. If a transition is ever handled differently (extraction skipped, written from git archaeology alone without first asking the live session, or the same session self-checking its own boot), that is a **repeated-failure incident** per `governance/MARK_TO_INDIA_SUCCESSOR_HUMAN_HANDOFF.md` FOUT 25 and must trigger the standard recovery: stop, identify the missed step, repair, then resume.

END INDIA SESSION TRANSITION PROTOCOL
