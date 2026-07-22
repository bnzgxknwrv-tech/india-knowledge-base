# USER DELIVERY PROTOCOL

GOUD must create `USER_DELIVERY_MANIFEST.yaml` before completion. The manifest declares the practical products required by the run, their exact paths, production status, validation results, preserved Mark decisions, open decisions and residual uncertainty.

For location or cluster candidate runs, the default required products are:
- a readable decision PDF containing every candidate;
- a complete KML containing every candidate, including uncertain GEO in a clearly marked folder.

A run may require CSV, DOCX or another format in addition. Technical Markdown/JSONL registers do not substitute for user products.

GOUD cannot return PASS or PARTIAL when any required practical product is missing, has the wrong candidate count, loses an active Mark decision, assigns a new A/B/C choice, fails reopen/parse/render validation or is not clearly locatable for Mark.

END_OF_ARTIFACT
