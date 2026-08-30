#!/usr/bin/env python3
"""Fail-closed validator for an INDIA independent CHECK artifact — V8.

This is the "second key" the 2026-08-30 Work audit (PR #23 comment
5470210435, MUST_FIX 2) found missing: until this script existed, nothing
mechanically verified that a `CHECK_GATE: PASS` in `governance/boot_checks/`
actually corresponded to the exact receipt path/session/start-nonce/receipt-
commit, was created strictly after the receipt, carried two genuinely new
verbatim quotes from sources not already used in the receipt, and recorded
at least the mandatory set of semantic challenges. A stale, copied, or
self-declared CHECK could otherwise be treated as content authorization.

CONTENT-SUBSTANCE HARDENING (2026-08-30 FRESH RE-AUDIT, PR #23 comment
5470939825, MUST_FIX 1): the first version of this script only checked that
each challenge's `answer`/`evidence` fields were non-empty -- an auditor
demonstrated that replacing all eight with the literal string "x" (valid
topics/questions/verdicts, valid C->R->K git shape otherwise intact) still
produced exit 0 / CONTENT_AUTHORIZATION: GRANTED. Two changes close that:
  1. Schema split: each challenge now records `start_session_answer` (the
     verbatim reply relayed back from the ORIGINAL START session, via Mark
     -- see governance/INDIA14_START_AND_INDEPENDENT_CHECK.md section 2.4a)
     separately from `checker_evidence` (the CHECK session's own citation of
     concrete pinned source material) and `checker_verdict`. A checker can
     no longer author both the "answer" and its own grading of that answer
     as one self-authored field.
  2. Anti-triviality floor: both fields are rejected if empty, a known
     placeholder/filler string, too short, too few words, identical to each
     other, or -- for checker_evidence -- lacking a concrete citation of a
     real governance/ or runs/ file path drawn from the mandatory source set
     or the reviewed receipt.
This is explicitly a FLOOR, not a complete solution -- see HONEST LIMIT
below and governance/boot_checks/README.md: nothing here cryptographically
proves start_session_answer was actually relayed verbatim from a genuinely
separate session rather than authored by the checker itself. It does,
however, close the concrete demonstrated bypass: a checker can no longer
get to GRANTED by self-authoring eight trivial one-character non-answers.

This script validates ONE check artifact against ONE receipt artifact and
the live git state. It does NOT re-validate the receipt itself (that is
validate_successor_boot.py's job) -- governance/scripts/final_authorization.py
runs both and is the ONLY place that may print CONTENT_AUTHORIZATION: GRANTED.

HONEST LIMIT: same as validate_successor_boot.py -- this proves machine-
checkable facts (paths, git shape, verbatim quotes, minimum-substance and
source-citation checks on structured challenge records) only. It cannot
prove the challenge answers are actually correct in a travel-domain sense,
that start_session_answer was genuinely relayed verbatim from the real
START session rather than authored by the checker, nor that the "CHECK"
session is a genuinely different reasoning process from the START session.
See governance/boot_checks/README.md and
governance/INDIA14_START_AND_INDEPENDENT_CHECK.md section 2.6/HONEST LIMIT
for that residual, irreducible limit.

RECEIPT/CHECK COMMIT SHAPE: three commits in a chain --
  C (content, hash = boot_head_final)
  -> R (receipt commit; R^ == C; diff(C,R) == [receipt file only])
  -> K (check commit;   K^ == R; diff(R,K) == [check file only]; K == actual current HEAD)
"""
from __future__ import annotations

import argparse
import json
import re
import subprocess
import sys
from datetime import datetime
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
MANIFEST = ROOT / "governance/BOOT_MANIFEST_V8.json"

SESSION_RE = re.compile(r"^(INDIA[0-9]+|TEST_FIXTURE_[A-Z0-9_]+)$")
NONCE_RE = re.compile(r"^[A-Z0-9]{6,32}$")
CHECK_TIMESTAMP_TOLERANCE_SECONDS = 6 * 3600

# ---------------------------------------------------------------------------
# Anti-triviality floor for start_session_answer / checker_evidence (Work
# audit 2026-08-30 fresh re-audit, MUST_FIX 1 -- see module docstring). This
# is a FLOOR against self-authored placeholder text, not proof of substance:
# it cannot verify travel-domain correctness or that an answer was actually
# relayed from a separate session. It can and does reject the concrete
# demonstrated bypass (all fields replaced by "x" or similar filler).
# ---------------------------------------------------------------------------
_BANNED_TRIVIAL_NORMALIZED = {
    "x", "xx", "xxx", "xxxx", "na", "none", "null", "tbd", "todo", "wip",
    "placeholder", "test", "testing", "asdf", "answer", "evidence", "yes",
    "no", "pass", "fail", "ok", "okay", "correct", "wrong", "true", "false",
    "seenote", "asabove", "samasanswer", "n a",
}
SOURCE_PATH_RE = re.compile(
    r"(?:governance|runs)/[A-Za-z0-9_\-./]+\.(?:md|json|jsonl)"
)


def _normalize(text: str) -> str:
    return re.sub(r"[^a-z0-9]", "", (text or "").lower())


def is_trivial_text(text: str) -> bool:
    """True if `text` is empty, whitespace-only, a known placeholder/filler
    string (after stripping punctuation/case), or made of a single repeated
    character (e.g. "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx")."""
    t = (text or "").strip()
    if not t:
        return True
    norm = _normalize(t)
    if not norm:
        return True
    if norm in _BANNED_TRIVIAL_NORMALIZED:
        return True
    if len(set(norm)) <= 1:
        return True
    return False


def cited_mandatory_paths(text: str, mandatory: set[str], extra: set[str]) -> set[str]:
    """Paths in `text` that look like a real repo source path AND are
    actually in the mandatory source set (or `extra`, e.g. the reviewed
    receipt path) -- i.e. a concrete, checkable citation, not just any
    path-shaped substring."""
    found = {m.group(0) for m in SOURCE_PATH_RE.finditer(text or "")}
    return found & (mandatory | extra)

p = argparse.ArgumentParser()
p.add_argument("--check", required=True,
                help="path to the independent CHECK artifact, e.g. "
                     "governance/boot_checks/INDIA14_CHECK__<NONCE>.json")
p.add_argument("--receipt", required=True,
                help="path to the receipt artifact this CHECK reviews")
p.add_argument("--expected-session", required=True)
p.add_argument("--expected-start-nonce", required=True,
                help="the ORIGINAL nonce from the START session's prompt (matches the receipt's own nonce)")
p.add_argument("--expected-check-nonce", required=True,
                help="a SEPARATE fresh nonce supplied by Mark in the CHECK prompt; must differ from the start nonce")
args = p.parse_args()

errors: list[str] = []


def fail(msg: str) -> None:
    errors.append(msg)


def git(*a: str) -> str:
    return subprocess.check_output(["git", *a], cwd=ROOT, text=True, stderr=subprocess.STDOUT).strip()


def git_ok(*a: str) -> bool:
    return subprocess.run(["git", *a], cwd=ROOT, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL).returncode == 0


# ---------------------------------------------------------------------------
# Manifest (for mandatory-source sets and required challenge topics)
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
required_topics = set(manifest.get("check_required_challenge_topics", []))
min_new_quotes = manifest.get("check_min_new_quotes", 2)
min_challenges = manifest.get("check_min_challenges", 6)
min_answer_chars = manifest.get("check_min_answer_chars", 40)
min_answer_words = manifest.get("check_min_answer_words", 8)
min_evidence_chars = manifest.get("check_min_evidence_chars", 25)
check_dir = manifest.get("check_directory", "governance/boot_checks")

if not required_topics:
    fail("manifest check_required_challenge_topics is empty -- cannot enforce mandatory veto challenge set")

# ---------------------------------------------------------------------------
# Basic argument format checks -- fail closed on garbage input, same as
# validate_successor_boot.py's session/nonce hardening (Work audit MUST_FIX 3).
# ---------------------------------------------------------------------------
if not SESSION_RE.fullmatch(args.expected_session or ""):
    fail(f"--expected-session does not match required format {SESSION_RE.pattern}: {args.expected_session!r}")
if not NONCE_RE.fullmatch(args.expected_start_nonce or ""):
    fail(f"--expected-start-nonce does not match required format {NONCE_RE.pattern}: {args.expected_start_nonce!r}")
if not NONCE_RE.fullmatch(args.expected_check_nonce or ""):
    fail(f"--expected-check-nonce does not match required format {NONCE_RE.pattern}: {args.expected_check_nonce!r}")
if args.expected_start_nonce and args.expected_check_nonce and args.expected_start_nonce == args.expected_check_nonce:
    fail("--expected-check-nonce must be a SEPARATE fresh value from --expected-start-nonce, not a reuse of it")

if not args.check.startswith(f"{check_dir}/"):
    fail(f"check artifact is not under append-only {check_dir}/")

check_path = ROOT / args.check
if not check_path.is_file():
    fail(f"check artifact not found: {args.check}")
    check = {}
else:
    try:
        check = json.loads(check_path.read_text(encoding="utf-8"))
    except Exception as e:
        fail(f"invalid check JSON: {e}")
        check = {}

receipt_path = ROOT / args.receipt
if not receipt_path.is_file():
    fail(f"referenced receipt not found: {args.receipt}")
    receipt = {}
else:
    try:
        receipt = json.loads(receipt_path.read_text(encoding="utf-8"))
    except Exception as e:
        fail(f"invalid receipt JSON: {e}")
        receipt = {}

# ---------------------------------------------------------------------------
# Identity/binding fields
# ---------------------------------------------------------------------------
session = check.get("india_session")
start_nonce = check.get("start_nonce")
check_nonce = check.get("check_nonce")

if not session or not SESSION_RE.fullmatch(session):
    fail(f"check india_session missing/invalid: {session!r}")
elif session != args.expected_session:
    fail(f"check india_session mismatch: {session} != {args.expected_session}")

if not start_nonce or not NONCE_RE.fullmatch(start_nonce):
    fail(f"check start_nonce missing/invalid: {start_nonce!r}")
elif start_nonce != args.expected_start_nonce:
    fail(f"check start_nonce mismatch: {start_nonce} != {args.expected_start_nonce}")

if not check_nonce or not NONCE_RE.fullmatch(check_nonce):
    fail(f"check check_nonce missing/invalid: {check_nonce!r}")
elif check_nonce != args.expected_check_nonce:
    fail(f"check check_nonce mismatch: {check_nonce} != {args.expected_check_nonce}")

if start_nonce and check_nonce and start_nonce == check_nonce:
    fail("check_nonce must differ from start_nonce (a copied/self-declared check cannot reuse the start nonce)")

if receipt and session and start_nonce:
    if receipt.get("india_session") != session:
        fail(f"check india_session does not match reviewed receipt's india_session: "
             f"{session} != {receipt.get('india_session')}")
    if receipt.get("nonce") != start_nonce:
        fail(f"check start_nonce does not match reviewed receipt's nonce: "
             f"{start_nonce} != {receipt.get('nonce')}")

if check.get("receipt_path") != args.receipt:
    fail(f"check receipt_path does not match --receipt: {check.get('receipt_path')!r} != {args.receipt!r}")
if session and start_nonce:
    expected_basename = f"{session}__{start_nonce}.json"
    if not (args.receipt.startswith("governance/boot_receipts/")
            and args.receipt.endswith(f"/{expected_basename}")):
        fail(f"--receipt does not match the canonical naming convention for this "
             f"session/nonce (expected basename {expected_basename!r} under "
             f"governance/boot_receipts/, optionally in a test_fixtures/ "
             f"subdirectory): {args.receipt!r}")

boot_head_final = check.get("boot_head_final")
if not re.fullmatch(r"[0-9a-f]{40}", boot_head_final or ""):
    fail(f"check boot_head_final missing/invalid: {boot_head_final!r}")
elif receipt and receipt.get("boot_head_final") != boot_head_final:
    fail(f"check boot_head_final does not match reviewed receipt's boot_head_final: "
         f"{boot_head_final} != {receipt.get('boot_head_final')}")

receipt_commit = check.get("receipt_commit")
if not re.fullmatch(r"[0-9a-f]{40}", receipt_commit or ""):
    fail(f"check receipt_commit missing/invalid: {receipt_commit!r}")

# ---------------------------------------------------------------------------
# Git shape: C -> R -> K, where K must be actual current HEAD.
# ---------------------------------------------------------------------------
try:
    actual_head = git("rev-parse", "HEAD")
except Exception as e:
    fail(f"cannot resolve HEAD: {e}")
    actual_head = None

if receipt_commit and boot_head_final and re.fullmatch(r"[0-9a-f]{40}", receipt_commit) and re.fullmatch(r"[0-9a-f]{40}", boot_head_final):
    try:
        r_parent = git("rev-parse", f"{receipt_commit}^")
    except Exception as e:
        fail(f"cannot resolve parent of receipt_commit: {e}")
        r_parent = None
    if r_parent != boot_head_final:
        fail(f"receipt_commit's parent {r_parent} != check boot_head_final {boot_head_final} "
             f"(receipt_commit does not sit directly on top of the pinned content commit)")
    else:
        try:
            r_files = git("diff", "--name-only", boot_head_final, receipt_commit).splitlines()
        except Exception as e:
            fail(f"cannot diff receipt_commit: {e}")
            r_files = None
        if r_files != [args.receipt]:
            fail(f"receipt_commit must add ONLY the receipt file; found: {r_files}")

if actual_head and receipt_commit and re.fullmatch(r"[0-9a-f]{40}", receipt_commit):
    if actual_head == receipt_commit:
        fail("actual current HEAD equals receipt_commit directly: the CHECK commit "
             "itself must sit on top of the receipt commit as its own single commit "
             "(no independent-CHECK commit has actually been made yet)")
    else:
        try:
            k_parent = git("rev-parse", f"{actual_head}^")
        except Exception as e:
            fail(f"cannot resolve parent of current HEAD: {e}")
            k_parent = None
        if k_parent != receipt_commit:
            fail(f"branch movement after check (or before it): current HEAD's parent "
                 f"{k_parent} != receipt_commit {receipt_commit} (more than one commit, "
                 f"or an unrelated commit, lies between the receipt and current HEAD)")
        else:
            try:
                k_files = git("diff", "--name-only", receipt_commit, actual_head).splitlines()
            except Exception as e:
                fail(f"cannot diff check commit: {e}")
                k_files = None
            if k_files != [args.check]:
                fail(f"check commit on top of the receipt commit must add ONLY the check "
                     f"file itself; found: {k_files}")

# Branch identity + clean tree, same discipline as the receipt validator.
try:
    current_branch = git("branch", "--show-current")
except Exception as e:
    fail(f"cannot resolve current branch: {e}")
    current_branch = ""
if not current_branch:
    fail("cannot verify branch: detached HEAD (inability to verify is fatal in check mode)")
elif manifest_branch and current_branch != manifest_branch:
    fail(f"wrong branch: {current_branch} != manifest branch {manifest_branch}")

try:
    dirty = git("status", "--porcelain", "--untracked-files=no")
except Exception as e:
    fail(f"cannot check working tree cleanliness: {e}")
    dirty = "unknown"
if dirty:
    fail("tracked working tree is not clean; cannot trust proof against pinned refs")

if actual_head and re.fullmatch(r"[0-9a-f]{40}", actual_head or ""):
    if not git_ok("cat-file", "-e", f"{actual_head}:{args.check}"):
        fail(f"check artifact not committed at current head: {args.check} not found in {actual_head[:12]}")

# ---------------------------------------------------------------------------
# Timestamps: check_created_utc must be a valid ISO-8601 UTC timestamp, must
# be strictly AFTER receipt_created_utc, and must be close to the ACTUAL git
# commit time of the check commit (actual_head here), not merely well-formed.
# ---------------------------------------------------------------------------
check_created = check.get("check_created_utc", "")
if not re.fullmatch(r"\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}Z", check_created or ""):
    fail("check_created_utc missing or not a valid UTC ISO-8601 timestamp")

receipt_created = receipt.get("receipt_created_utc", "") if receipt else ""
if check_created and receipt_created:
    try:
        check_dt = datetime.fromisoformat(check_created.replace("Z", "+00:00"))
        receipt_dt = datetime.fromisoformat(receipt_created.replace("Z", "+00:00"))
        if check_dt <= receipt_dt:
            fail(f"check_created_utc {check_created} is not strictly after "
                 f"receipt_created_utc {receipt_created} (a CHECK must be produced "
                 f"after the receipt it reviews)")
    except Exception as e:
        fail(f"cannot compare check_created_utc to receipt_created_utc: {e}")

if check_created and actual_head and re.fullmatch(r"[0-9a-f]{40}", actual_head or ""):
    try:
        commit_ts = git("log", "-1", "--format=%cI", actual_head)
        commit_dt = datetime.fromisoformat(commit_ts)
        claimed_dt = datetime.fromisoformat(check_created.replace("Z", "+00:00"))
        delta = abs((commit_dt - claimed_dt).total_seconds())
        if delta > CHECK_TIMESTAMP_TOLERANCE_SECONDS:
            fail(f"check_created_utc {check_created} is {delta:.0f}s from actual commit time "
                 f"{commit_ts} of {actual_head[:12]} (tolerance {CHECK_TIMESTAMP_TOLERANCE_SECONDS}s)")
    except Exception as e:
        fail(f"cannot verify check_created_utc freshness against commit time: {e}")

# ---------------------------------------------------------------------------
# Two NEW verbatim quotes from sources NOT used in the original receipt.
# ---------------------------------------------------------------------------
mandatory_sources = set(central) | set(active) | set(cci)
receipt_proof_sources = {pr.get("source") for pr in (receipt.get("proof_of_read") or []) if isinstance(pr, dict)}
receipt_proof_quotes = {pr.get("quote") for pr in (receipt.get("proof_of_read") or []) if isinstance(pr, dict)}


def pinned_text_for(src: str) -> str | None:
    ref = cci_commit if src in cci else boot_head_final
    if not ref:
        return None
    try:
        raw = subprocess.check_output(["git", "show", f"{ref}:{src}"], cwd=ROOT)
        return raw.decode("utf-8", errors="replace")
    except Exception:
        return None


new_quotes = check.get("new_quotes", [])
if not isinstance(new_quotes, list) or len(new_quotes) < min_new_quotes:
    fail(f"need at least {min_new_quotes} new_quotes items")
    new_quotes = []

seen_new_sources: set[str] = set()
seen_new_quotes: set[str] = set()
for nq in new_quotes:
    if not isinstance(nq, dict):
        fail("malformed new_quotes item")
        continue
    src = nq.get("source", "")
    q = nq.get("quote", "")
    if src in seen_new_sources:
        fail(f"duplicate new_quotes source: {src}")
    if q in seen_new_quotes:
        fail("duplicate new_quotes quote")
    seen_new_sources.add(src)
    seen_new_quotes.add(q)

    if len(q) < 40 or not re.search(r"[.!?]$", q.strip()):
        fail(f"new_quotes item is not a meaningful full sentence (>=40 chars, ends in . ! or ?): {src}")
    if src not in mandatory_sources:
        fail(f"new_quotes source is not a mandatory file: {src}")
        continue
    if src in receipt_proof_sources:
        fail(f"new_quotes source was already used as a proof_of_read source in the "
             f"original receipt (must be a NOT-yet-used mandatory source): {src}")
    if q in receipt_proof_quotes:
        fail(f"new_quotes quote duplicates a quote already used in the original receipt: {src}")

    text = pinned_text_for(src)
    if text is None:
        fail(f"no pinned content available for new_quotes source: {src}")
        continue
    if q not in text:
        fail(f"new_quotes quote not verbatim in pinned source: {src}")

if len({nq.get("source") for nq in new_quotes if isinstance(nq, dict)}) < min_new_quotes:
    fail(f"new_quotes must come from at least {min_new_quotes} DISTINCT sources")

# ---------------------------------------------------------------------------
# Semantic challenges: >= min_challenges, structured, unique, covering the
# full mandatory veto topic set, with NO material FAIL verdict anywhere.
#
# Each challenge splits the old single self-authored `answer`/`evidence`
# pair into two independently-sourced fields (Work audit fresh re-audit,
# MUST_FIX 1 -- see module docstring):
#   - start_session_answer: the verbatim reply relayed back from the
#     ORIGINAL START session (via Mark -- see
#     INDIA14_START_AND_INDEPENDENT_CHECK.md section 2.4a). This is the
#     content actually being tested; the checker must not author it.
#   - checker_evidence: the CHECK session's own citation of concrete pinned
#     source material used to grade start_session_answer -- must name a
#     real mandatory (or receipt) file path, not just assert a verdict.
#   - checker_verdict: the checker's PASS/FAIL judgment, unchanged in kind
#     from the old `verdict` field but now clearly scoped as the checker's
#     own grading of a separately-sourced answer, not of its own text.
# Both text fields are rejected if empty, a known placeholder/filler string,
# too short, too few words, or identical to each other -- an anti-triviality
# FLOOR, not proof of substance (see HONEST LIMIT in the module docstring).
# ---------------------------------------------------------------------------
challenges = check.get("challenges", [])
if not isinstance(challenges, list) or len(challenges) < min_challenges:
    fail(f"need at least {min_challenges} challenges")
    challenges = []

seen_pairs: set[tuple] = set()
topics_seen: set[str] = set()
any_fail_verdict = False
for ch in challenges:
    if not isinstance(ch, dict):
        fail("malformed challenge item")
        continue
    topic = ch.get("topic", "")
    question = ch.get("question", "")
    answer = ch.get("start_session_answer", "")
    evidence = ch.get("checker_evidence", "")
    verdict = ch.get("checker_verdict", "")

    if not topic:
        fail("challenge missing topic")
    if not question or len(question) < 10:
        fail(f"challenge question missing/too short: topic={topic}")

    if is_trivial_text(answer):
        fail(f"challenge start_session_answer missing, empty, or a placeholder/filler "
             f"string (must be the ORIGINAL START session's verbatim relayed reply): topic={topic}")
    elif len(answer.strip()) < min_answer_chars:
        fail(f"challenge start_session_answer too short (<{min_answer_chars} chars): topic={topic}")
    elif len(answer.strip().split()) < min_answer_words:
        fail(f"challenge start_session_answer too few words (<{min_answer_words}): topic={topic}")

    if is_trivial_text(evidence):
        fail(f"challenge checker_evidence missing, empty, or a placeholder/filler string: topic={topic}")
    elif len(evidence.strip()) < min_evidence_chars:
        fail(f"challenge checker_evidence too short (<{min_evidence_chars} chars): topic={topic}")
    elif not cited_mandatory_paths(evidence, mandatory_sources, {args.receipt}):
        fail(f"challenge checker_evidence does not cite a concrete mandatory source path "
             f"(governance/... or runs/...) or the reviewed receipt path: topic={topic}")

    if (answer or "").strip() and (evidence or "").strip() and answer.strip() == evidence.strip():
        fail(f"challenge start_session_answer and checker_evidence must not be identical "
             f"(the checker's own citation cannot double as the answer being graded): topic={topic}")

    if verdict not in ("PASS", "FAIL"):
        fail(f"challenge checker_verdict must be PASS or FAIL, got {verdict!r}: topic={topic}")
    if verdict == "FAIL":
        any_fail_verdict = True

    pair = (topic, question)
    if pair in seen_pairs:
        fail(f"duplicate challenge (topic, question): {pair}")
    seen_pairs.add(pair)
    topics_seen.add(topic)

missing_topics = required_topics - topics_seen
if missing_topics:
    fail(f"challenge set is missing mandatory veto topics: {sorted(missing_topics)}")

if any_fail_verdict:
    fail("at least one challenge has verdict FAIL -- any material wrong answer is an "
         "unconditional FAIL of the CHECK, per INDIA14_START_AND_INDEPENDENT_CHECK.md section 2.5")

# check_gate field itself (declared) must say PASS -- necessary but, exactly
# like the receipt's boot_gate field, never sufficient on its own; every
# check above still runs regardless of what this field claims.
if check.get("check_gate") != "PASS":
    fail("check check_gate != PASS")

# ---------------------------------------------------------------------------
if errors:
    print("CHECK_GATE_VALIDATION: FAIL")
    for e in errors:
        print(f"- {e}")
    print("CONTENT_AUTHORIZATION: NOT_GRANTED")
    sys.exit(1)

print("CHECK_GATE_VALIDATION: PASS")
print(f"SESSION: {session}")
print(f"START_NONCE: {start_nonce}")
print(f"CHECK_NONCE: {check_nonce}")
print(f"RECEIPT: {args.receipt}")
print(f"CHECK: {args.check}")
print(f"NEW_QUOTES: {len(new_quotes)} from {len(seen_new_sources)} distinct not-previously-used sources")
print(f"CHALLENGES: {len(challenges)}; required topics covered: {len(required_topics)}/{len(required_topics)}")
print("CHECK_GATE: PASS")
sys.exit(0)
