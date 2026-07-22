# QUICK START FOR MARK

Use one short prompt from `india3/START_PROMPTS.md` in a clean chat. You do not need to copy predecessor reports, context manifests or long instructions.

Use CONTROLLER to create a new run, repair routing or resume a blocked transition. Use BRONS, ZILVER or GOUD only when `pipeline/NEXT_ACTION.yaml` already names that role.

When a stop report appears, open a new clean chat and use the resume prompt. The chat reads the committed status and continues from the first incomplete validated step.

Final user products are stored under `research/active/<RUN_ID>/GOUD/USER/` and listed in `USER_DELIVERY_MANIFEST.yaml`. Technical audit files remain in the GOUD directory.

To give a decision, state the run ID, candidate ID or subject, and your explicit choice. INDIA3 records it append-only and does not overwrite earlier decisions.

For a GEO disagreement, name the candidate and reject or provide the exact link/point. The disputed candidate remains isolated; unrelated candidates continue.

END_OF_ARTIFACT
