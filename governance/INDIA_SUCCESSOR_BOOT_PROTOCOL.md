# INDIA SUCCESSOR BOOT PROTOCOL — RETIRED COMPATIBILITY POINTER

Status: **SUPERSEDED 2026-08-28**
Superseded by: `governance/INDIA_MASTER_BOOT.md`

The former contents of this file remain in Git history as provenance. They are no longer an independent mandatory boot chain.

Reason for retirement:
- successive INDIA versions repeatedly loaded only part of the distributed boot chain;
- current state, human preferences, historical decisions and stale-source rules were spread across too many files;
- the old light/recovery logic still allowed successors to declare themselves ready before enough planning history had actually been loaded.

## Current rule
If any older task, handoff, README version or prompt points here, immediately read and execute:

`governance/INDIA_MASTER_BOOT.md`

The master boot owns:
- the mandatory always-read set;
- cluster-specific required source packages;
- authority precedence;
- stale/skip categories;
- the living Mark profile;
- the living current knowledge map;
- the living recovery-delta file;
- `AL BESLIST?`, recovery, action-first and replaceability rules.

Do not reconstruct boot logic from this retired file's Git history unless investigating a specific historical failure.
