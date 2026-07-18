#!/usr/bin/env python3
from __future__ import annotations
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent
fixture = json.loads((ROOT / "fixture.json").read_text(encoding="utf-8"))
report = (ROOT / "GOUD" / "MARK_FINAL_REPORT.md").read_text(encoding="utf-8")
chat = (ROOT / "GOUD" / "CHAT_OUTPUT.txt").read_text(encoding="utf-8")


def load_jsonl(path: Path):
    rows = [json.loads(line) for line in path.read_text(encoding="utf-8").splitlines() if line.strip()]
    assert rows[-1] == {"_sentinel": "END_OF_ARTIFACT"}
    return rows[:-1]


def strip_chat(text: str) -> str:
    assert text.startswith("GOUD ZEGT:\n")
    body = text[len("GOUD ZEGT:\n"):]
    suffix = "\n\nROUTING: VOOR_MARK\n/GOUD\n"
    assert body.endswith(suffix)
    return body[:-len(suffix)] + "\n"

results = {}

hp = fixture["happy_path"]
results["A"] = (
    fixture["run"]["run_type"] == "SYNTHETIC_TEST"
    and hp["states"] == ["READY_FOR_BRONS","BRONS_CLAIMED","BRONS_COMPLETE","TRANSITION_TO_ZILVER_CLAIMED","READY_FOR_ZILVER","ZILVER_CLAIMED","ZILVER_COMPLETE","TRANSITION_TO_GOUD_CLAIMED","READY_FOR_GOUD","GOUD_CLAIMED","GOUD_PASS"]
    and hp["content_chats"] == ["BRONS","ZILVER","GOUD"]
    and all(c["opened"] == "ACTIVE" and c["closed"] == "CLOSED" for c in hp["claims"])
    and len({c["id"] for c in hp["claims"]}) == 5
    and not hp["worker_claim_reused_as_controller"]
    and not hp["phase_writes_after_role_switch"]
    and hp["next_role_ready_released_after_readback"]
    and hp["state_events_synced"]
)
results["B"] = all([fixture["tests"]["B"]["detected"], fixture["tests"]["B"]["transition_blocked"], not fixture["tests"]["B"]["next_context_created"], not fixture["tests"]["B"]["ready_state_written"], not fixture["tests"]["B"]["prompt_released"]])
results["C"] = fixture["tests"]["C"]["claim_source_id"] not in fixture["sources"] and fixture["tests"]["C"]["transition_blocked"]
results["D"] = fixture["tests"]["D"]["state"] != fixture["tests"]["D"]["last_event_state"] and fixture["tests"]["D"]["desync_detected"] and fixture["tests"]["D"]["transition_blocked"]
results["E"] = all([fixture["tests"]["E"]["pasted_non_pinned_change_ignored"], fixture["tests"]["E"]["github_state_used"], not fixture["tests"]["E"]["stale_chat_claim_allowed"], fixture["tests"]["E"]["hash_mismatch_detected"], fixture["tests"]["E"]["worker_stopped"]])
results["F"] = all([not fixture["tests"]["F"]["controller_phase_write_allowed"], not fixture["tests"]["F"]["worker_claim_reuse_allowed"], fixture["tests"]["F"]["active_predecessor_claim_blocks"], fixture["tests"]["F"]["missing_close_fields_blocks"], fixture["tests"]["F"]["completion_commit_mismatch_blocks"]])
results["G"] = not fixture["tests"]["G"]["post_completion_pinned"] and fixture["tests"]["G"]["old_process_selected"] and not fixture["tests"]["G"]["inline_transition_allowed"]
required = ["## 1. Eindantwoord","## 2. Status","## 5. Definitieve locaties of kandidaten","## 6. Afgevallen of contextlocaties","## 9. Open punten","## 10. Aanbevolen vervolgstap","## 11. Canonieke integratie","## 13. Technische eindcontrole","## 14. Geschreven eindproducten","## 16. Definitieve afsluiting","END_OF_ARTIFACT"]
results["H"] = all(x in report for x in required)
results["I"] = strip_chat(chat) == report
results["J"] = fixture["tests"]["J"] == {"controller_claim_1":"ACCEPTED","controller_claim_2":"REJECTED_ACTIVE_CLAIM","metal_claim_1":"ACCEPTED","metal_claim_2":"REJECTED_STATE_CHANGED","new_claim_after_close_requires_current_state":True}
results["K"] = all([fixture["tests"]["K"]["predecessor_commit_mismatch_blocks"], not fixture["tests"]["K"]["state_changed_without_event_next_role_ready"], not fixture["tests"]["K"]["controller_transition_commit_mismatch_releases_handoff"]])

before = load_jsonl(ROOT / "fixture_registry_before.jsonl")
after = load_jsonl(ROOT / "fixture_registry_after.jsonl")
assert len(before) == len(after)
by_id_before = {r["place_id"]: r for r in before}
by_id_after = {r["place_id"]: r for r in after}
allowed = True
for pid, old in by_id_before.items():
    new = by_id_after[pid]
    for key in old:
        if key == "artifact_path":
            continue
        if old[key] != new[key]:
            allowed = False
location_ids = [r["location_id"] for r in after]
decisions_same = (ROOT / "fixture_decisions_before.yaml").read_text(encoding="utf-8") == (ROOT / "fixture_decisions_after.yaml").read_text(encoding="utf-8")
results["L"] = allowed and len(location_ids) == len(set(location_ids)) and decisions_same and fixture["tests"]["L"]["formal_status_change_blocked"] and fixture["tests"]["L"]["advisory_status_add_blocked"] and fixture["tests"]["L"]["new_decision_id_blocked"] and fixture["tests"]["L"]["new_decision_text_blocked"] and fixture["tests"]["L"]["mark_decision_required"] and not fixture["tests"]["L"]["decision_dependent_write_applied"]
results["M"] = all([not fixture["tests"]["M"]["production_run_before_result_allowed"], fixture["tests"]["M"]["synthetic_exception_allowed"], not fixture["tests"]["M"]["production_run_with_no_result_allowed"], not fixture["tests"]["M"]["production_run_with_yes_before_merge_allowed"], fixture["tests"]["M"]["production_run_with_yes_after_merge_alowed"]])

for path in [ROOT / "scope.md", ROOT / "GOUD" / "MARK_FINAL_REPORT.md", ROOT / "GOUD" / "CANONICAL_INTEGRATION_PROPOSAL.md"]:
    assert path.read_text(encoding="utf-8").rstrip().endswith("END_OF_ARTIFACT")
assert fixture["_sentinel"] == "END_OF_ARTIFACT"
assert (ROOT / "run.yaml").read_text(encoding="utf-8").rstrip().endswith("sentinel: END_OF_ARTIFACT")

for key in "ABCDEFGHIJKLMZ":
    print(f"TEST_{key}: {'PASS' if results[key] else 'FAIL'}")
if not all(results.values()):
    raise SystemExit(1)
print("ALL_TESTS_A_M: PASS")
