# INDIA SUCCESSOR BOOT PROTOCOL

```
status: BINDING — highest operational boot authority for INDIA10+ and later versions,
        until explicitly superseded by a later dated version of this file.
effective_date: 2026-08-23
authorized_by: Mark, live chat confirmation on 2026-08-23 ("Luister naar hem, hij is
               nieuwe regisseur"), following INDIA9's explicit request in
               CCI_TASK — INDIA9-SUCCESSOR-ARCHITECTURE-CENTRAL-INTEGRATION-008/008R.
implemented_by: CCI, task 008.
supersedes: the brute-force "reread the entire repository every boot" mechanic
            previously implied by governance/INDIA_REGIE_CRITICAL_BOOT_AND_NO_DEFERRAL_2026-08-23.md
            — WHEN a certified baseline (see governance/KNOWLEDGE_BASELINE_LATEST.md)
            validates. That file's incident record, AL BESLIST rule, sleep-base-first
            rule, and no-deferral principle remain fully in force; only the read
            *mechanics* are replaced here.
```

## A. What "100% knowledge" means

`100% KNOWLEDGE` means **semantic coverage + integrity coverage** of everything that
currently matters, not literal word-for-word rereading of every unchanged byte in the
repository on every boot. A successor that has validated its baseline and read every
new/changed meaningful blob since that baseline, plus current authority state, is at
100% — even though it has not personally reread millions of bytes of unchanged,
already-certified content.

## B. The baseline-skip rule

A validated immutable baseline (see F) allows a successor to skip word-for-word
reread of unchanged semantic source content that baseline already certifies. The
successor MUST still semantically read **100% of NEW/CHANGED meaningful content since
that baseline**, plus **always reread current authority state** (see G), every boot.

## C. Fallback rule

If baseline/hash/precedence validation fails for any reason — a hash mismatch, a
missing manifest, an unreadable pointer file — controlled full-bootstrap fallback
(read everything, from scratch, exactly as the pre-2026-08-23 mechanic did) is
**mandatory**. Never silently trust an unvalidated baseline; never silently skip the
fallback.

## D. The four mandatory delta classes

Every new/changed blob since baseline must be classified into exactly one of:
- `UNIQUE_SEMANTIC_NOT_CENTRALLY_REPRESENTED` — must be fully, personally, semantically
  read before it can count toward 100%.
- `SEMANTICALLY_REPRESENTED_IN_CENTRAL` — its material content is already carried by an
  identified central file; a light-weight successor-path confirmation suffices.
- `HISTORICAL_INTERMEDIATE_SUPERSEDED` — provenance only; counts toward the denominator
  but not toward the "must personally read" numerator.
- `MECHANICAL_OR_REDUNDANT_SOURCE_ARTIFACT` — generated/duplicate packaging; hash
  verification suffices, no semantic read required.

This is the exact schema task 006 designed and applied to the 867-blob source-delta;
reuse it, do not re-derive it each generation.

## E. Four separate gates

Track these as **distinct** boolean/percentage states, never collapse them into one:
- `SEMANTIC_KNOWLEDGE_COVERAGE` — has the delta content actually been read?
- `INTEGRITY_COVERAGE` — do all blob hashes verify against the manifest?
- `AUTHORITY_RECONCILIATION` — has the precedence/supersedes graph been reconciled (no
  stale status field mistaken as current)?
- `FRESHNESS_GATE` — is time-sensitive content (visas, transport, weather, live rules)
  still within its `recheck_due` window?

A file can be 100% known (SEMANTIC_KNOWLEDGE_COVERAGE) yet `RECHECK_DUE` for
operational use (FRESHNESS_GATE) — these are not the same claim and must not be
reported as if they were.

## F. Baseline certificate contents

Each `governance/KNOWLEDGE_BASELINE_<date>.md` must record: frozen commit/tree,
frozen branch-tip universe (branch/head-SHA/tree-SHA table), semantic category totals
(per D), byte/blob totals, a precedence-snapshot reference (the supersedes graph state
at freeze time), and confirmation of a one-time binary semantic-clearance pass (has
every binary in the baseline been checked at least once for decision-unique content?).

## G. Always reread/reconcile current (every boot, no exceptions)

Regardless of baseline validity, every boot must read fresh: explicit Mark
decisions/locks, `PROTECTED_CANON_BASELINE.csv`, accommodation/base locks,
cluster/site decisions, `governance/ACTIVE_FRAMEWORK.md`,
`governance/PRECEDENCE_MAP.jsonl`, the current handoff/session-start files, any active
`TASK.md`/`STATUS.md` for in-progress work, the newest commits/decisions since the
baseline, and `governance/CENTRAL_INTEGRATION_REGISTRY.jsonl`.

## H. `AL BESLIST?` gate

Before presenting any location, cluster, hotel, base, or route choice to Mark, check it
against `PROTECTED_CANON_BASELINE.csv` and `PRECEDENCE_MAP.jsonl`. A hit in either is
an automatic hard-stop on re-presenting that item as a new choice.

## I. Never ask Mark to repeat history

Mark is not a courier between CCI and INDIAN. Everything needed to continue must be
retrievable from GitHub; do not ask Mark to re-explain something already committed.

## J. No substantive work before `KNOWLEDGE_READY: 100%`

No route/A-B-C/hotel/travel-readiness advice may be given while any of the four gates
(E) is not passing for the current delta + authority state.

## K. Multi-turn circuit breaker

If boot cannot finish in one chat turn: write
`runs/active/<IndiaN>-BOOT-<date>/BOOT_PROGRESS.md` with the exact percentage (per the
formula below), counts, the last completed blob SHA, and the remaining set. Tell Mark
`KNOWLEDGE_READY: NEE — X%` plus the literal next-turn continuation prompt. The next
turn resumes from the checkpoint; it never rereads already-proven work.

```
byte_weighted_knowledge_pct =
    ( baseline_bytes_covered
    + SUM(size_bytes for delta blobs actually semantically read this generation,
          restricted to category UNIQUE_SEMANTIC_NOT_CENTRALLY_REPRESENTED
          and any not-yet-spot-checked SEMANTICALLY_REPRESENTED_IN_CENTRAL) )
    / ( baseline_bytes_covered + total_new_project_source_bytes_since_baseline )
    * 100
```

## L. Same-turn self-replacement

Any Mark decision, correction, precedence change, blocker, task-state change,
integration event, or next-executable-state determination is committed to GitHub in
the same session it happens in. Never deferred to "I'll write this up later."

## M. No-deferral retained

Anything safely, independently executable now is executed now. Only genuinely
Mark-only decisions or real external blockers (live booking/price acceptance,
awaiting a third party) may remain open.

## N. Completion is dimensional

`worker_output_state` (a worker says "done") is NOT the same claim as
`central_integration_state` (central actually merged it) is NOT the same claim as
"travel ready" is NOT the same claim as "person/topic saturated." Track these as
separate fields, always — see `governance/CENTRAL_INTEGRATION_REGISTRY.jsonl`. This
directly closes the failure this task's own integration is fixing: ZILVER's own
`STATUS.md` said `PARTIAL_COMPLETE` while nothing downstream noticed the "partial."

## O. Freshness discipline

Any source whose truth depends on live rules — visa requirements, transport
timetables, availability, weather, entry/admin rules — must carry `last_verified` and
`recheck_due` fields. Content past its `recheck_due` may not be used operationally
without revalidation, even if it is otherwise 100% "known."

## P. Baseline evolution

Each successor inherits the prior certified baseline plus its own delta. A new
baseline is certified only after semantic delta coverage AND authority reconciliation
are both complete. Goal: each successor generation starts with strictly more
structured knowledge than its predecessor — never a flat re-parse of the same raw byte
pile — while spending less context on rediscovery than the previous generation did.

## Q. Audit packaging is not a mandatory reread

Once a stream/page/review-volume's source identity and derivation from its underlying
blob is hash-proven (as tasks 002/003/005/007 already did), it never needs to be
reread word-for-word again just because it exists. Its hash-verified status is
permanent; only the underlying source blob's own change would invalidate that.

---
Geschreven door: CCI, task 008, on explicit Mark authorization. This file is the single
binding boot authority; it does not erase or invalidate the reasoning history in
`governance/INDIA_REGIE_CRITICAL_BOOT_AND_NO_DEFERRAL_2026-08-23.md` or
`runs/active/INDIA9-SUCCESSOR-BOOT-KNOWLEDGE-ARCHITECTURE-006/*` — it is their
operational successor.
