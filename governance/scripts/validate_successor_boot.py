#!/usr/bin/env python3
"""Fail-closed INDIA successor boot validator — V8 (hardened finalization).

Authoritative boot membership comes from governance/BOOT_MANIFEST_V8.json.
Boot PASS requires an append-only per-session JSON receipt and explicit
--require-session-receipt <path> mode, with --expected-session and
--expected-nonce also mandatory in that mode. Warnings are fatal in receipt
mode: every inability-to-verify condition is treated as FAIL, never as a
soft pass.

`india_session`/`nonce` (and the matching `--expected-session`/`--expected-nonce`
CLI values) are format-validated against SESSION_RE/NONCE_RE below, and
`receipt_created_utc` is checked against the ACTUAL git commit timestamp of
the commit that added the receipt, not merely its own ISO-8601 shape. This
closes the "any non-empty string mechanically passes" gap: a mechanical PASS
now at least proves the session/nonce look like real values and the claimed
creation time is not fabricated relative to git's own clock. It still does
NOT prove the nonce/session actually originated in Mark's start prompt
rather than being invented by the same session that wrote the receipt --
only the independent CHECK (governance/INDIA14_START_AND_INDEPENDENT_CHECK.md,
enforced by governance/scripts/validate_independent_check.py) can bind that.

HONEST LIMIT: this script cannot prove what a model actually attended to.
It proves machine-checkable facts only — pinned git content, blob identity,
ancestor/branch/cleanliness of the repository state, receipt structure, and
literal verbatim substrings of the pinned source text. A mechanical PASS is
therefore explicitly NOT content authorization; only an independent second
CHECK session (see governance/INDIA14_START_AND_INDEPENDENT_CHECK.md) can
grant that.

RECEIPT COMMIT SHAPE (read this before writing a receipt by hand): a
commit's hash cannot be known before its own content is fixed, so a
receipt's `boot_head_final` field can never literally equal the hash of the
very commit that adds the receipt file (that would require finding content
whose hash matches a value embedded in that same content — a hash-puzzle
search, not something a session does by design). The required shape is
therefore two commits: first commit all mandatory content and call ITS hash
`boot_head_final`; then, as a SEPARATE follow-up commit whose diff contains
ONLY the new receipt file and nothing else, commit the receipt itself. The
validator checks exactly this: current HEAD's first parent must equal
`boot_head_final`, and the diff between them must be exactly the one
receipt file.
"""
from __future__ import annotations

import argparse
import json
import re
import subprocess
import sys
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
MANIFEST = ROOT / "governance/BOOT_MANIFEST_V8.json"

# Session labels: real INDIA sessions (`INDIA14`, ...) or explicitly-namespaced
# test fixtures (`TEST_FIXTURE_GOLDEN`, ...) that can never collide with a real
# label (see governance/boot_receipts/README.md safeguard 2). Nothing else —
# empty, lowercase, garbage, or a real-looking-but-malformed label — passes.
SESSION_RE = re.compile(r"^(INDIA[0-9]+|TEST_FIXTURE_[A-Z0-9_]+)$")
# Nonces: uppercase alphanumeric, 6-32 chars. Deliberately strict — a nonce is
# supposed to be a short fresh token from Mark's start prompt, not free text.
NONCE_RE = re.compile(r"^[A-Z0-9]{6,32}$")
# Tolerance between a receipt's self-reported `receipt_created_utc` and the
# actual git commit timestamp of the commit that added it. This is what makes
# `receipt_created_utc` a freshness check rather than a format-only field: a
# receipt whose claimed creation time drifts far from when it was actually
# committed is evidence the timestamp was copied/fabricated rather than
# generated live at commit time.
RECEIPT_TIMESTAMP_TOLERANCE_SECONDS = 6 * 3600
RECOVERY_DELTAS = "governance/INDIA_RECOVERY_DELTAS_CURRENT.md"
CURRENT_STATE = "governance/CURRENT_STATE.md"
SAFE_STATE = "governance/SUCCESSOR_SAFE_STATE.md"
CROSS_REF_FILES = [
    "governance/INDIA_MASTER_BOOT.md",
    "governance/INDIA_CURRENT_KNOWLEDGE_MAP.md",
    "governance/FRESH_SESSION_BOOT_GATE.md",
]

p = argparse.ArgumentParser()
p.add_argument("--require-session-receipt", dest="receipt", default=None,
               help="path to append-only per-session JSON receipt, "
                    "e.g. governance/boot_receipts/INDIA14__<NONCE>.json")
p.add_argument("--expected-session", default=None,
                help="mandatory in receipt mode: exact expected INDIA session label")
p.add_argument("--receipt-commit", dest="receipt_commit", default=None,
                help="OPTIONAL: pinned 40-char SHA of the commit that added the receipt "
                     "file, when it is not literally the current actual HEAD (e.g. when "
                     "a later independent-CHECK commit has since been added on top by "
                     "governance/scripts/final_authorization.py). Defaults to actual "
                     "current HEAD when omitted, matching the original START-time usage. "
                     "When given, it must still be a real ancestor-or-self of actual "
                     "current HEAD and must itself satisfy the exact required shape "
                     "(parent == boot_head_final, diff == the one receipt file) -- this "
                     "flag relaxes WHERE the receipt commit may sit relative to current "
                     "HEAD, never WHAT shape it must have.")
p.add_argument("--expected-nonce", default=None,
                help="mandatory in receipt mode: exact expected start-prompt nonce")
args = p.parse_args()

errors: list[str] = []


def fail(msg: str) -> None:
    errors.append(msg)


def git(*a: str) -> str:
    return subprocess.check_output(["git", *a], cwd=ROOT, text=True, stderr=subprocess.STDOUT).strip()


def git_ok(*a: str) -> bool:
    return subprocess.run(["git", *a], cwd=ROOT, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL).returncode == 0


# ---------------------------------------------------------------------------
# Manifest load + structural checks (also run in structural/default mode)
# ---------------------------------------------------------------------------
if not MANIFEST.is_file():
    fail("missing governance/BOOT_MANIFEST_V8.json")
    manifest = {}
else:
    try:
        manifest = json.loads(MANIFEST.read_text(encoding="utf-8"))
    except Exception as e:
        fail(f"invalid boot manifest JSON: {e}")
        manifest = {}

central = manifest.get("central_required", [])
cci = manifest.get("cci_required", [])
active = manifest.get("active_cluster_required", [])
cci_commit = manifest.get("cci_commit", "")
manifest_branch = manifest.get("branch", "")

# R36: do NOT hardcode an exact expected central_required count here. A
# literal exact-count trip wire (formerly "!= 16") mechanically FAILs every
# session the moment central_required legitimately grows (e.g. the
# compilation-gate file added in this consensus patch took it 16 -> 17) --
# that staleness is itself the READ_COMPLETE != ACTIVE_MEMORY_COMPILED
# failure class this patch exists to close, so this validator must not
# reproduce it. Only a non-empty floor is enforced; the real count is always
# read live from the manifest itself (`len(central)` throughout this file).
if len(central) < 1: fail("manifest central_required is empty")
if len(cci) != 6: fail(f"manifest CCI count {len(cci)} != 6")
if len(active) < 1: fail("manifest active-cluster set empty")
if len(set(central)) != len(central): fail("duplicate central path in manifest")
if len(set(cci)) != len(cci): fail("duplicate CCI path in manifest")
if len(set(active)) != len(active): fail("duplicate active-cluster path in manifest")

for rel in central + active:
    if not (ROOT / rel).is_file():
        fail(f"missing manifest file: {rel}")

# Structural cross-reference: master + map + gate must name manifest, not
# maintain a competing authority.
for rel in CROSS_REF_FILES:
    fp = ROOT / rel
    if not fp.is_file():
        fail(f"missing {rel}")
        continue
    txt = fp.read_text(encoding="utf-8")
    if "BOOT_MANIFEST_V8.json" not in txt:
        fail(f"{rel} does not point to canonical V8 manifest")

# R36 / confirmed INDIA16 bug: this validator used to check a receipt's
# active_cluster only against the MANIFEST's own active_cluster field, with
# no cross-check against governance/CURRENT_STATE.md's `manifest_active_cluster:`
# value -- the more authoritative, human-legible source. A session that
# correctly derived the frontier from CURRENT_STATE.md could mechanically
# FAIL while one that echoed a stale manifest value would PASS. This is a
# narrow, purely structural string-equality check: it does not judge which
# value is "right," only that the two currently-designated authorities agree.
current_state_fp = ROOT / CURRENT_STATE
if not current_state_fp.is_file():
    fail(f"missing {CURRENT_STATE}")
else:
    cs_text = current_state_fp.read_text(encoding="utf-8")
    m = re.search(r"^manifest_active_cluster:\s*`([^`]+)`", cs_text, flags=re.MULTILINE)
    if not m:
        fail(f"{CURRENT_STATE} has no parseable `manifest_active_cluster:` line")
    else:
        manifest_active_cluster_value = m.group(1)
        if manifest_active_cluster_value != manifest.get("active_cluster"):
            fail(f"active_cluster mismatch: {CURRENT_STATE} manifest_active_cluster "
                 f"{manifest_active_cluster_value!r} != manifest active_cluster "
                 f"{manifest.get('active_cluster')!r}")

# Existing crash-safe hard fields remain mandatory.
safe = ROOT / "governance/SUCCESSOR_SAFE_STATE.md"
if safe.is_file():
    st = safe.read_text(encoding="utf-8")
    if "STATUS: SAFE_TO_HANDOFF" not in st: fail("safe state not SAFE_TO_HANDOFF")
    if not re.search(r"UNSAVED_RISK:\s*\nGEEN", st): fail("safe state UNSAVED_RISK is not GEEN")
else:
    fail("missing SUCCESSOR_SAFE_STATE.md")

if args.receipt is None:
    # Deliberately NOT a boot PASS. Structural mode cannot authorize content.
    if errors:
        print("INDIA_BOOT_STRUCTURE: FAIL")
        for e in errors: print(f"- {e}")
        sys.exit(1)
    print("INDIA_BOOT_STRUCTURE: PASS")
    print("CONTENT_AUTHORIZATION: NOT_GRANTED — structural mode only; "
          "rerun with --require-session-receipt <path> --expected-session <s> --expected-nonce <n>")
    sys.exit(2)

# ---------------------------------------------------------------------------
# Receipt / authorization mode — every inability to verify is fatal here.
# ---------------------------------------------------------------------------
if not args.expected_session:
    fail("--expected-session is mandatory in receipt mode")
elif not SESSION_RE.fullmatch(args.expected_session):
    fail(f"--expected-session does not match required format {SESSION_RE.pattern}: {args.expected_session!r}")
if not args.expected_nonce:
    fail("--expected-nonce is mandatory in receipt mode")
elif not NONCE_RE.fullmatch(args.expected_nonce):
    fail(f"--expected-nonce does not match required format {NONCE_RE.pattern}: {args.expected_nonce!r}")

receipt_path = ROOT / args.receipt
if not receipt_path.is_file():
    fail(f"receipt not found: {args.receipt}")
    receipt = {}
else:
    try:
        receipt = json.loads(receipt_path.read_text(encoding="utf-8"))
    except Exception as e:
        fail(f"invalid receipt JSON: {e}")
        receipt = {}

# Append-only path and identity binding.
if not args.receipt.startswith("governance/boot_receipts/"):
    fail("receipt is not under append-only governance/boot_receipts/")
session = receipt.get("india_session")
nonce = receipt.get("nonce")
if not session or not nonce:
    fail("receipt missing session or nonce")
else:
    if not SESSION_RE.fullmatch(session):
        fail(f"receipt india_session does not match required format {SESSION_RE.pattern}: {session!r}")
    if not NONCE_RE.fullmatch(nonce):
        fail(f"receipt nonce does not match required format {NONCE_RE.pattern}: {nonce!r}")
if args.expected_session and session != args.expected_session:
    fail(f"session mismatch: {session} != {args.expected_session}")
if args.expected_nonce and nonce != args.expected_nonce:
    fail("nonce mismatch")
if receipt.get("boot_gate") != "PASS": fail("receipt boot_gate != PASS")
if receipt.get("summary_substitution_used") is not False: fail("summary substitution not explicitly false")
if receipt.get("unfinished_truncations") != 0: fail("unfinished truncations != 0")

created = receipt.get("receipt_created_utc", "")
if not re.fullmatch(r"\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}Z", created or ""):
    fail("receipt_created_utc missing or not a valid UTC ISO-8601 timestamp")

# Manifest must be exact source of truth.
if receipt.get("manifest_path") != "governance/BOOT_MANIFEST_V8.json": fail("receipt manifest_path mismatch")
try:
    manifest_blob = git("hash-object", "governance/BOOT_MANIFEST_V8.json")
except Exception as e:
    fail(f"cannot hash manifest: {e}")
    manifest_blob = None
if manifest_blob and receipt.get("manifest_blob") != manifest_blob:
    fail("receipt manifest blob mismatch")

initial = receipt.get("boot_head_initial", "")
final = receipt.get("boot_head_final", "")
if not re.fullmatch(r"[0-9a-f]{40}", initial or ""): fail("invalid boot_head_initial")
if not re.fullmatch(r"[0-9a-f]{40}", final or ""): fail("invalid boot_head_final")

# Branch delta must be represented; `final` is the pinned content boundary
# the session actually verified. `final` cannot literally equal the commit
# that adds the receipt file itself (that commit's hash cannot be known
# until after its content — including this very field — is fixed, which
# would require a hash-puzzle search to satisfy exactly). Instead: current
# HEAD must be either exactly `final`, or exactly ONE commit ahead of
# `final` whose ENTIRE diff is adding this one receipt file and nothing
# else — i.e. content was fully pinned at `final`, then the receipt
# recording that fact was committed on top, untangled from any other change.
try:
    actual_head = git("rev-parse", "HEAD")
except Exception as e:
    fail(f"cannot resolve HEAD: {e}")
    actual_head = None

# The receipt commit is normally exactly current actual HEAD (the START
# session just committed it). But this same validator is also invoked LATER,
# by governance/scripts/final_authorization.py, after a further independent-
# CHECK commit has been added on top of the receipt commit -- at that point
# actual HEAD is the CHECK commit, not the receipt commit. --receipt-commit
# lets the caller pin explicitly WHICH commit is being validated as the
# receipt commit in that case; it defaults to actual_head, preserving the
# original START-time behavior unchanged when omitted.
pinned_receipt_commit = args.receipt_commit or actual_head
if args.receipt_commit and not re.fullmatch(r"[0-9a-f]{40}", args.receipt_commit or ""):
    fail(f"--receipt-commit is not a 40-char SHA: {args.receipt_commit!r}")
    pinned_receipt_commit = None

if pinned_receipt_commit and final:
    if final == pinned_receipt_commit:
        fail("receipt final head must not equal the receipt commit directly: "
             "the receipt commit itself must sit on top of boot_head_final "
             "as its own single commit (see script docstring)")
    else:
        try:
            first_parent = git("rev-parse", f"{pinned_receipt_commit}^")
        except Exception as e:
            fail(f"cannot resolve parent of receipt commit: {e}")
            first_parent = None
        if first_parent != final:
            fail(f"receipt final head stale: receipt commit's parent {first_parent} "
                 f"!= receipt boot_head_final {final} (more than one commit, or an "
                 f"unrelated commit, lies between the pinned content and the receipt commit)")
        else:
            try:
                receipt_commit_files = git("diff", "--name-only", final, pinned_receipt_commit).splitlines()
            except Exception as e:
                fail(f"cannot diff receipt commit: {e}")
                receipt_commit_files = None
            if receipt_commit_files != [args.receipt]:
                fail(f"receipt commit on top of boot_head_final must add ONLY the receipt "
                     f"file itself; found: {receipt_commit_files}")
        # If a receipt commit was pinned explicitly (rather than defaulted from
        # actual_head), it must still be a real ancestor-of-or-equal-to actual
        # current HEAD -- it cannot point at an unrelated or future commit that
        # merely happens to satisfy the shape check above in isolation.
        if args.receipt_commit and actual_head and pinned_receipt_commit != actual_head:
            if not git_ok("merge-base", "--is-ancestor", pinned_receipt_commit, actual_head):
                fail(f"--receipt-commit {pinned_receipt_commit[:12]} is not an ancestor of "
                     f"actual current HEAD {actual_head[:12]} (branch moved to an unrelated "
                     f"state, or the pinned commit is stale/wrong)")

# Branch identity: current branch must equal the manifest's declared branch.
try:
    current_branch = git("branch", "--show-current")
except Exception as e:
    fail(f"cannot resolve current branch: {e}")
    current_branch = ""
if not current_branch:
    fail("cannot verify branch: detached HEAD (inability to verify is fatal in receipt mode)")
elif manifest_branch and current_branch != manifest_branch:
    fail(f"wrong branch: {current_branch} != manifest branch {manifest_branch}")

# Clean tracked working tree: all proof text below is read from pinned git
# refs, never from a possibly-edited working tree.
try:
    dirty = git("status", "--porcelain", "--untracked-files=no")
except Exception as e:
    fail(f"cannot check working tree cleanliness: {e}")
    dirty = "unknown"
if dirty:
    fail("tracked working tree is not clean; cannot trust proof against pinned refs")

# initial HEAD must be an ancestor of final HEAD.
if initial and final:
    if not git_ok("merge-base", "--is-ancestor", initial, final):
        fail(f"boot_head_initial {initial[:12]} is not an ancestor of boot_head_final {final[:12]}")

# The receipt file itself must exist committed in the tree at current HEAD —
# not merely present on disk / staged. (It is deliberately NOT expected to
# exist yet at `final` — see the head-binding block above.)
if actual_head and re.fullmatch(r"[0-9a-f]{40}", actual_head or ""):
    if not git_ok("cat-file", "-e", f"{actual_head}:{args.receipt}"):
        fail(f"receipt not committed at current head: {args.receipt} not found in {actual_head[:12]}")

# receipt_created_utc freshness: the claimed timestamp must be close to the
# ACTUAL git commit time of the commit that added the receipt
# (pinned_receipt_commit -- actual_head by default, or the explicitly pinned
# receipt commit when this runs post-CHECK), not merely well-formed. A
# receipt copied/reused/fabricated long after (or before) it was actually
# committed fails here even though the ISO-8601 format check above would
# have let it through.
if created and pinned_receipt_commit and re.fullmatch(r"[0-9a-f]{40}", pinned_receipt_commit or ""):
    try:
        commit_ts = git("log", "-1", "--format=%cI", pinned_receipt_commit)
        commit_dt = datetime.fromisoformat(commit_ts)
        claimed_dt = datetime.fromisoformat(created.replace("Z", "+00:00"))
        delta = abs((commit_dt - claimed_dt).total_seconds())
        if delta > RECEIPT_TIMESTAMP_TOLERANCE_SECONDS:
            fail(f"receipt_created_utc {created} is {delta:.0f}s from actual commit time {commit_ts} "
                 f"of {pinned_receipt_commit[:12]} (tolerance {RECEIPT_TIMESTAMP_TOLERANCE_SECONDS}s)")
    except Exception as e:
        fail(f"cannot verify receipt_created_utc freshness against commit time: {e}")

# Per-file attestation sets must match manifest exactly, and content is
# fetched from the pinned ref via `git show`, never from the working tree.
def attest_map(key: str):
    rows = receipt.get(key, [])
    if not isinstance(rows, list):
        fail(f"{key} is not list")
        return {}
    out = {}
    for row in rows:
        if not isinstance(row, dict) or not row.get("path"):
            fail(f"bad attestation row in {key}")
            continue
        if row["path"] in out:
            fail(f"duplicate attestation {row['path']}")
        out[row["path"]] = row
    return out


# path -> (pinned text content, byte length), used later for proof-of-read.
pinned_text: dict[str, str] = {}

for key, expected, ref in [
    ("central_reads", central, final),
    ("cci_reads", cci, cci_commit),
    ("active_cluster_reads", active, final),
]:
    rows = attest_map(key)
    if set(rows) != set(expected):
        fail(f"{key} path set differs from manifest: "
             f"missing={sorted(set(expected) - set(rows))} extra={sorted(set(rows) - set(expected))}")
    for rel in expected:
        row = rows.get(rel, {})
        if row.get("eof_reached") is not True: fail(f"EOF not attested: {rel}")
        if row.get("tool_truncated") is not False: fail(f"truncation not false: {rel}")
        if not row.get("blob_sha"):
            fail(f"missing blob_sha: {rel}")
            continue
        try:
            actual_blob = git("rev-parse", f"{ref}:{rel}")
        except Exception as e:
            fail(f"cannot verify git object {ref[:12] if ref else ref}:{rel}: {e}")
            continue
        if row.get("blob_sha") != actual_blob:
            fail(f"blob mismatch: {rel}")
            continue
        try:
            raw = subprocess.check_output(["git", "show", f"{ref}:{rel}"], cwd=ROOT)
        except Exception as e:
            fail(f"cannot read pinned content {ref[:12] if ref else ref}:{rel}: {e}")
            continue
        pinned_text[rel] = raw.decode("utf-8", errors="replace")

        # Full non-overlapping read-range coverage over the pinned byte length.
        byte_length = row.get("byte_length")
        ranges = row.get("read_ranges")
        if byte_length != len(raw):
            fail(f"byte_length mismatch for {rel}: receipt={byte_length} actual={len(raw)}")
        if not isinstance(ranges, list) or not ranges:
            fail(f"missing read_ranges for {rel}")
        else:
            norm = []
            bad = False
            for r in ranges:
                if not (isinstance(r, list) and len(r) == 2 and all(isinstance(x, int) for x in r)):
                    fail(f"malformed read_range in {rel}: {r}")
                    bad = True
                    break
                s, e = r
                if s < 0 or e > len(raw) or s >= e:
                    fail(f"read_range out of bounds in {rel}: {r}")
                    bad = True
                    break
                norm.append((s, e))
            if not bad:
                norm.sort()
                cur = 0
                for s, e in norm:
                    if s > cur:
                        fail(f"gap in read coverage for {rel} at byte {cur}-{s}")
                        bad = True
                        break
                    if s < cur:
                        fail(f"overlapping read_ranges for {rel} at byte {s}")
                        bad = True
                        break
                    cur = e
                if not bad and cur != len(raw):
                    fail(f"incomplete read coverage for {rel}: reached {cur} of {len(raw)} bytes")

# Delta: any mandatory file changed initial->final must appear in reread list.
try:
    changed = set(git("diff", "--name-only", initial, final).splitlines()) if initial and final and initial != final else set()
except Exception as e:
    fail(f"cannot verify boot delta: {e}")
    changed = set()
mandatory_changed = changed.intersection(set(central + active + ["governance/BOOT_MANIFEST_V8.json"]))
reread = set(receipt.get("delta_reread_paths", []))
if not mandatory_changed.issubset(reread):
    fail(f"mandatory delta not reread: {sorted(mandatory_changed - reread)}")

# ---------------------------------------------------------------------------
# Proof-of-read: >=3 unique verbatim full-sentence quotes from distinct,
# correctly-labeled categories, verified against pinned source text. A
# category cannot be satisfied by a quote from the wrong source ("relabeling").
# ---------------------------------------------------------------------------
def newest_recovery_section(text: str) -> tuple[str, str]:
    """Return (heading, section_text) for the highest-numbered '# Rxx —' item."""
    headings = list(re.finditer(r"^# R(\d+)\s*—.*$", text, flags=re.MULTILINE))
    if not headings:
        return "", ""
    newest = max(headings, key=lambda m: int(m.group(1)))
    start = newest.end()
    later = [h for h in headings if h.start() > newest.start()]
    end = min((h.start() for h in later), default=len(text))
    also_end = text.find("\n# ", start)
    if also_end != -1 and also_end < end:
        end = also_end
    return newest.group(0), text[newest.start():end]


proofs = receipt.get("proof_of_read", [])
if not isinstance(proofs, list) or len(proofs) < 3:
    fail("need at least 3 proof_of_read items")
    proofs = []

seen_sources: set[str] = set()
seen_quotes: set[str] = set()
cats: set[str] = set()

recovery_heading, recovery_section = ("", "")
if RECOVERY_DELTAS in pinned_text:
    recovery_heading, recovery_section = newest_recovery_section(pinned_text[RECOVERY_DELTAS])
    if not recovery_heading:
        fail(f"could not locate a newest R-item heading in {RECOVERY_DELTAS}")

for pr in proofs:
    if not isinstance(pr, dict):
        fail("malformed proof_of_read item")
        continue
    src = pr.get("source", "")
    q = pr.get("quote", "")
    cat = pr.get("category", "")
    if src in seen_sources: fail(f"duplicate proof source: {src}")
    if q in seen_quotes: fail("duplicate proof quote")
    seen_sources.add(src)
    seen_quotes.add(q)
    cats.add(cat)

    if len(q) < 40 or not re.search(r"[.!?]$", q.strip()):
        fail(f"proof is not a meaningful full sentence (>=40 chars, ends in . ! or ?): {src}")

    if src in central or src in active:
        text = pinned_text.get(src)
        if text is None:
            fail(f"no pinned content available for proof source: {src}")
            continue
    elif src in cci:
        text = pinned_text.get(src)
        if text is None:
            fail(f"no pinned content available for CCI proof source: {src}")
            continue
    else:
        fail(f"proof source not mandatory: {src}")
        continue

    if q not in text:
        fail(f"proof quote not verbatim in pinned source: {src}")

    # Category <-> source binding. A category cannot be satisfied by
    # relabeling a quote from an unrelated file.
    if cat == "current_state_or_safe":
        if src not in (CURRENT_STATE, SAFE_STATE):
            fail(f"category current_state_or_safe requires source {CURRENT_STATE} or {SAFE_STATE}, got {src}")
    elif cat == "newest_recovery_delta":
        if src != RECOVERY_DELTAS:
            fail(f"category newest_recovery_delta requires source {RECOVERY_DELTAS}, got {src}")
        elif recovery_section and q not in recovery_section:
            fail(f"newest_recovery_delta proof quote is not inside the newest R-item "
                 f"({recovery_heading.strip()}): {src}")
    elif cat == "cci":
        if src not in cci:
            fail(f"category cci requires a source from the six immutable CCI files, got {src}")
    elif cat == "":
        fail(f"proof item missing category: {src}")
    # other/unknown categories are allowed as extra evidence but do not
    # satisfy the three mandatory categories below.

if not {"current_state_or_safe", "newest_recovery_delta", "cci"}.issubset(cats):
    fail("proof categories incomplete: need current_state_or_safe, newest_recovery_delta, cci")

# Active cluster and validator identity fields.
if receipt.get("active_cluster") != manifest.get("active_cluster"): fail("active cluster mismatch")
if receipt.get("validator_mode") != "--require-session-receipt": fail("wrong validator mode in receipt")

# Control-veto checksum. governance/INDIA_MASTER_BOOT.md SS2B documents this as
# a "Minimum PASS field" ("control-veto checksum containing at least
# TRAIN_FIRST, AL_BESLIST, naming-every-occurrence, GEO verification,
# action-first, same-turn durable memory, CCI three-way filter, safe-state,
# full-source-layer, NU_DOEN, and the final successor active-memory handoff
# veto") but nothing here ever checked for it -- a receipt could omit the
# field entirely, including the final-handoff-veto attestation, and still
# print BOOT_AUTHORIZATION: MECHANICAL_GATE_PASS. This closes that gap.
REQUIRED_CONTROL_VETO_KEYS = (
    "TRAIN_FIRST_DOOR_TO_DOOR",
    "AL_BESLIST",
    "NAMING_EVERY_OCCURRENCE",
    "GEO_VERIFICATION_NO_GUESSED_PIN",
    "ACTION_FIRST",
    "SAME_TURN_DURABLE_WHAT_WHY",
    "CCI_THREE_WAY_FILTER",
    "SAFE_STATE",
    "FULL_SOURCE_LAYER",
    "NU_DOEN",
    "SUCCESSOR_ACTIVE_MEMORY_HANDOFF_VETO",
)
checksum = receipt.get("control_veto_checksum")
if not isinstance(checksum, dict):
    fail("receipt missing control_veto_checksum object (see INDIA_MASTER_BOOT.md SS2B)")
else:
    missing_veto_keys = [k for k in REQUIRED_CONTROL_VETO_KEYS if not checksum.get(k)]
    if missing_veto_keys:
        fail(f"control_veto_checksum missing/false required keys: {missing_veto_keys}")

# In boot mode, any inability to verify is already an error; there are no warnings.
if errors:
    print("INDIA_TRAVEL_BOOT_SANITY: FAIL")
    for e in errors: print(f"- {e}")
    print("CONTENT_AUTHORIZATION: NOT_GRANTED")
    sys.exit(1)

print("INDIA_TRAVEL_BOOT_SANITY: PASS")
print(f"SESSION: {session}")
print(f"NONCE: {nonce}")
print(f"BRANCH: {current_branch}")
print(f"HEAD: {final}")
print(f"CENTRAL: {len(central)}/{len(central)}; CCI: {len(cci)}/{len(cci)}; ACTIVE: {len(active)}/{len(active)}")
print("BOOT_AUTHORIZATION: MECHANICAL_GATE_PASS")
print("CONTENT_AUTHORIZATION: NOT_GRANTED — independent CHECK (INDIA14_START_AND_INDEPENDENT_CHECK.md) must still PASS")
sys.exit(0)
