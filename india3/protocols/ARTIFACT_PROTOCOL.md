# ARTIFACT PROTOCOL

Technical artifacts and user-facing artifacts are separate deliverables linked by stable candidate IDs and counts.

Every artifact records producer role, source commit, generation method, validation method, generated_at and residual uncertainty. Text artifacts end with `END_OF_ARTIFACT`. Binary/user products have checksums and reopen results in the delivery manifest.

A generated KML is validated separately for XML/KML syntax, folder structure, marker count, duplicate IDs, coordinate ranges and GEO evidence status. These technical checks do not establish geographic correctness.

A generated PDF is rendered and visually inspected for page count, candidate coverage, readability, clipping, navigation and decision fields.

END_OF_ARTIFACT
