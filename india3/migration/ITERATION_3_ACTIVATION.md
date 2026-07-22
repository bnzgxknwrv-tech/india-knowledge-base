# ITERATION 3 ACTIVATION

INDIA3 was activated only after iteration 1 preservation and iteration 2 critical scenario tests passed.

Activation changes:
- `pipeline/ACTIVE_SYSTEM.yaml` selects INDIA3 exclusively.
- `pipeline/ENTRYPOINT.md` now routes new clean chats through INDIA3.
- `pipeline/NEXT_ACTION.yaml` is neutral IDLE and controller-owned.
- Legacy INDIA1/INDIA2 control documents are indexed as archived reference-only while remaining available to historical pinned runs.
- Mark decisions are protected through an append-only register.
- GOUD practical delivery and GEO capability qualification are mandatory gates.

No historical research output was deleted. The temporary preflight marker is removed in the activation commit.

END_OF_ARTIFACT
