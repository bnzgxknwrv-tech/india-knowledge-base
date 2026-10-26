#!/usr/bin/env python3
"""Durable regression test for deterministic_light_topics() in
validate_independent_check.py, added 2026-09-14 (successor-boot slimming +
Mark working-model hardening, PR #23).

Context: BOOT_MANIFEST_V8.json declared `light_check_always_required_topics`
(so a LIGHT check can never skip MARK_WORKING_MODEL_ACTIVE_RECALL) before the
validator actually implemented it -- a real, confirmed instance of the
"no prose may claim a check exists when the script does not implement it"
failure class this whole task exists to close. This test proves the fix and
is meant to be re-run whenever deterministic_light_topics() changes.

Run: python3 governance/scripts/test_light_check_topic_selection.py
Exits 0 and prints ALL TESTS PASSED, or exits 1 and prints which assertion
failed. No network, no git, no CI needed -- pure function under test.
"""
import hashlib
import sys

# Import the function under test directly from the validator module without
# triggering its top-level argparse (the module is a script, not a library).
import importlib.util

_spec = importlib.util.spec_from_file_location(
    "validate_independent_check_module",
    __file__.rsplit("/", 1)[0] + "/validate_independent_check.py",
)
_mod = importlib.util.module_from_spec(_spec)
# The module's top-level code calls argparse.parse_args() unconditionally,
# so importing it as-is would crash/exit outside a real CLI invocation.
# Extract just the one pure function via AST instead of executing the module.
import ast

_tree = ast.parse(open(_spec.origin).read())
_func_src = None
for node in _tree.body:
    if isinstance(node, ast.FunctionDef) and node.name == "deterministic_light_topics":
        _func_src = ast.get_source_segment(open(_spec.origin).read(), node)
        break
if _func_src is None:
    print("FAIL: could not locate deterministic_light_topics() in validate_independent_check.py")
    sys.exit(1)

_ns: dict = {"hashlib": hashlib}
exec(_func_src, _ns)
deterministic_light_topics = _ns["deterministic_light_topics"]

POOL = [
    "MARK_WORKING_MODEL_ACTIVE_RECALL", "TRAIN_FIRST_DOOR_TO_DOOR", "AL_BESLIST",
    "C_DO_NOT_RE_PRESENT", "NEWER_CENTRAL_OVER_CCI", "GEO_VETO", "CURRENT_FRONTIER",
    "ACTION_FIRST", "DURABLE_WHAT_WHY", "PRESENTATION_AND_GRADE_LETTERS",
    "RESEARCH_VS_TRIAGE_VS_DURATION", "FRONTIER_CONTRADICTION_CHECK",
    "SUCCESSOR_ACTIVE_MEMORY_HANDOFF", "EXACT_DELEGATION_BINDING",
]
ALWAYS = ["MARK_WORKING_MODEL_ACTIVE_RECALL"]

failures = []


def check(name: str, condition: bool):
    (print(f"PASS: {name}") if condition else (failures.append(name), print(f"FAIL: {name}")))


# PASS case 1: always-required topic present in every one of many fake boots.
all_present = True
all_len3 = True
all_unique = True
for trial in range(500):
    fake_head = hashlib.sha256(str(trial).encode()).hexdigest()
    sel = deterministic_light_topics(fake_head, POOL, 3, always_required=ALWAYS)
    if ALWAYS[0] not in sel:
        all_present = False
    if len(sel) != 3:
        all_len3 = False
    if len(set(sel)) != len(sel):
        all_unique = False
check("always-required topic present across 500 fake boot heads", all_present)
check("selection length always equals requested count", all_len3)
check("selection never contains duplicate topics", all_unique)

# PASS case 2: deterministic / reproducible for the same boot_head_final.
h = "abc123" * 8
r1 = deterministic_light_topics(h, POOL, 3, always_required=ALWAYS)
r2 = deterministic_light_topics(h, POOL, 3, always_required=ALWAYS)
check("same boot_head_final gives identical topic selection", r1 == r2)

# PASS case 3: backward compatibility -- empty always_required matches the
# pre-2026-09-14 algorithm exactly, so old FULL-check history isn't affected.
def _old_algorithm(boot_head_final, topic_pool, count):
    remaining = sorted(set(topic_pool))
    count = min(count, len(remaining))
    selected = []
    for i in range(count):
        digest = hashlib.sha256(f"{boot_head_final}:LIGHT_CHECK_TOPIC_SELECT:{i}".encode()).hexdigest()
        idx = int(digest, 16) % len(remaining)
        selected.append(remaining.pop(idx))
    return selected


backward_compat = all(
    _old_algorithm(hashlib.sha256(f"x{i}".encode()).hexdigest(), POOL, 3)
    == deterministic_light_topics(hashlib.sha256(f"x{i}".encode()).hexdigest(), POOL, 3, always_required=[])
    for i in range(200)
)
check("empty always_required exactly matches pre-hardening algorithm (200 trials)", backward_compat)

# FAIL-DEMONSTRATION case: without the fix (always_required ignored), the
# always-required topic would appear only ~3/14 of the time by chance, not
# 100%. Show the bug this test guards against would actually have been
# caught, by re-running the OLD (unfixed) algorithm and confirming it does
# NOT reliably include the topic.
old_hits = sum(
    1 for i in range(200)
    if ALWAYS[0] in _old_algorithm(hashlib.sha256(f"y{i}".encode()).hexdigest(), POOL, 3)
)
check(
    "sanity: the pre-fix algorithm did NOT reliably include the always-required "
    f"topic ({old_hits}/200 ~ {old_hits/200:.0%}, expected far below 100%) -- "
    "proves this test would have caught the original gap",
    old_hits < 200,
)

# Edge case: always_required topic not present in the pool at all must not
# crash and must not be force-inserted (defensive, in case of a future typo
# in the manifest).
sel_bad = deterministic_light_topics("deadbeef" * 5, POOL, 3, always_required=["NOT_A_REAL_TOPIC"])
check("unknown always_required topic is silently ignored, not force-inserted", "NOT_A_REAL_TOPIC" not in sel_bad)
check("count is still respected when always_required topic is unknown", len(sel_bad) == 3)

print()
if failures:
    print(f"{len(failures)} TEST(S) FAILED: {failures}")
    sys.exit(1)
print("ALL TESTS PASSED")
sys.exit(0)
