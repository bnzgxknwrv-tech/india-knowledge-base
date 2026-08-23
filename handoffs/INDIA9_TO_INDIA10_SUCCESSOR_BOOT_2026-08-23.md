# HANDOFF — INDIA9 TO INDIA10 — SUCCESSOR BOOT

```
handoff_date: 2026-08-23
written_by: CCI, task 008, on Mark's direct authorization.
```

## Why this handoff replaces brute-force full reread

INDIA9's own boot (and CCI's supporting audit chain, tasks 001-008) surfaced a real,
repeated failure pattern: older-but-valid Mark canon getting under-read, worker output
marked "complete" that was never actually consolidated centrally, and — most acutely —
a literal instruction to "read the ENTIRE repository" turning out to be undefinable and
un-finishable in one chat turn once the repository grew to 54 branches / 1,680 unique
blobs / ~27MB. That is not a one-off inconvenience; it is the exact trigger that led
Mark to ask for this successor architecture in the first place.

The fix this handoff hands you is not "read less carefully" — it is "read once,
provably, then only read what actually changed." `governance/KNOWLEDGE_BASELINE_2026-08-23.md`
is proof that this works: every blob in the current frozen universe has already been
either personally semantically read (central baseline + the 62 category-1 blobs) or
hash-verified with its successor/provenance path recorded (everything else). You do
not need to re-earn that work from scratch.

## The exact start prompt for you (usable unchanged for many future versions)

```
Neem de INDIA-regie over als de volgende IndiaN. Voer eerst uitsluitend de Knowledge
Boot uit volgens governance/INDIA_SUCCESSOR_BOOT_PROTOCOL.md. Valideer de latest
baseline, precedence en integration state; semantically read 100% new/changed
meaningful delta + current authority; fallback to full bootstrap if validation fails;
if multi-turn, checkpoint en geef Mark de exacte continuation prompt; geen inhoudelijke
India-regie totdat alle gates slagen; vraag Mark nooit de geschiedenis opnieuw uit te
leggen; AL BESLIST vóór elke vraag; self-replace naar GitHub in dezelfde sessie.
```

## Where to start, concretely

1. Read `governance/KNOWLEDGE_BASELINE_LATEST.md` — it points to the current
   certificate.
2. Read that certificate (`governance/KNOWLEDGE_BASELINE_2026-08-23.md` as of this
   writing) for the exact frozen universe and gate state.
3. Read `governance/PRECEDENCE_MAP.jsonl` and `governance/ACTIVE_FRAMEWORK.md` for
   what is currently authoritative vs. provenance-only.
4. Read `governance/CENTRAL_INTEGRATION_REGISTRY.jsonl` and
   `governance/SEMANTIC_IMPORT_REGISTRY_2026-08-23.jsonl` for exactly what was
   promoted vs. archived, and why.
5. Run the delta-accounting procedure (reuse task 004's method: enumerate current
   branch tips, diff against the frozen baseline's branch-tip manifest) to find
   anything new since 2026-08-23, classify it into the four delta classes, and
   semantically read only category 1 + spot-check category 2.
6. Only then: start substantive India-regie work, with the `AL BESLIST?` gate applied
   to every location/cluster/hotel/base/route item before it reaches Mark.

## What is NOT covered by the current baseline

Anything pushed after 2026-08-23's freeze, and the freshness of any
`TIME_SENSITIVE_REFERENCE_RECHECK`-scoped content (visa/logistics, 15 archived blobs)
beyond its archival date. Both are exactly what step 5 above is for.

---
Geschreven door: CCI, task 008.
