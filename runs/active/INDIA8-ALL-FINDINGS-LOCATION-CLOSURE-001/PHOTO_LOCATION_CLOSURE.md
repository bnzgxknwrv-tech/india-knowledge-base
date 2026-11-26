# PHOTO_LOCATION_CLOSURE — Anandamayi Ma × Paramahansa Yogananda (addendum, 2026-08-20)

```
uitgevoerd_door: CCI
uitgevoerd_op: 2026-08-20
onderliggend_werk: YOGANANDA-ANANDAMAYI-PHOTO-LOCATION-001 (CCI_TASK 083, 2026-08-16) --
                    already executed earlier in this engagement, located and reconciled
                    into the master in this pass, not redone.
```

## Method note

This bounded subtask was already completed once, before this addendum arrived, under
CCI_TASK 083 (`runs/active/YOGANANDA-ANANDAMAYI-PHOTO-LOCATION-001/RESULT.md` on
`agent/india8-cluster-casting`). That result was built by directly reading the full primary text
of *Autobiography of a Yogi* chapter 45 (Project Gutenberg #7452, the same sha256-locked edition
used in `AOAY-FULL-LOCATION-ATLAS-001`) plus the official Anandamayi Ma Sangha photo archive and
life-history chronology, opened directly rather than from a snippet. This pass located that
existing result, verified it directly resolves the addendum's questions, and reconciled its two
physically-resolvable outputs into the row-level master (see `GLOBAL_ACCOUNTING.md`). No new
research was re-run; nothing in the existing result required correction.

## Required distinction (addendum point 3): confirmed, three separate events, not two

AOAY ch45 explicitly narrates **three** separate Yogananda–Anandamayi Ma encounters during the
1935-36 India visit, not one and not (as the earlier task's own working hypothesis wrongly
assumed) a single garden/Calcutta conflation:

1. **Bhowanipur, Calcutta — first meeting.** She was already outside, standing in an open-topped
   car blessing ~100 disciples, on the point of departure. Bholanath is explicitly, physically
   described here ("a broad-shouldered, fine-featured man... standing quietly in the midst of the
   gathering"). **No photography is mentioned in this passage.**
2. **Ranchi Vidyalaya — school visit, later.** Yogananda explicitly invites her to the garden "Mr.
   Wright will take some pictures"; AOAY confirms she "posed for many photographs." **This is the
   only passage in AOAY where photography with Yogananda is explicitly and multiply confirmed.**
   Bholanath is not mentioned here.
3. **Serampore station — farewell sighting, months later.** Brief platform encounter while she
   waited for a train. No photography mentioned.

## Findings against the addendum's known leads

- **YSS caption** "Ananda Moyi Ma, Bholanath and Yogananda in Calcutta" and the **Anandamayi
  Sangha archive caption** "Ma Anandamayi with Bholanath and Paramahamsa Yogananda" most plausibly
  belong to **event 1 (Bhowanipur)**, since Bholanath is textually placed there and not at Ranchi
  -- but this is a **plausible, not proven** attribution: AOAY's silence about a camera at
  Bhowanipur is not proof no photo was taken there, and the archive image itself could not be
  visually inspected (see blockers).
- The **motion-picture-film claim** from the official Anandamayi Sangha text could not be
  independently corroborated or localized to a specific one of the three events with the sources
  consulted; treated as an open, separately-flagged claim, not silently dropped.

## Physical resolution per event

| Event | R-class | Current physical identity | Access | Master row |
|---|---|---|---|---|
| Bhowanipur first meeting | **R5** | Neighbourhood only; exact house/host not recoverable from consulted sources | ACCESS_UNKNOWN_AFTER_EXHAUSTION | new row, `physical_entity_key = BLAUW-AYC-SRC-017` |
| Ranchi Vidyalaya garden (photo session) | **R1** | Yogoda Satsanga Sakha Math, Old Hazaribag Road, Ranchi, Jharkhand — same still-active, publicly accessible campus already resolved as `AYC-SRC-027` (Top-11 `ATL-PY-005`) | PUBLIC_OPEN (YSS ashram rules apply) | already in base master, `BLAUW-AYC-SRC-027` |
| Serampore station | **R1** | Serampore railway station, still existing, public | PUBLIC_OPEN | new row, `physical_entity_key = BLAUW-AYC-SRC-018` |

## Irreducible blockers (concrete, not "further research needed" hand-waving)

1. **Gurupriya Devi's diary** (*Mother As Revealed To Me*, the single most likely primary source
   for the exact Bhowanipur house/host) was retrieved as a PDF but is a scanned image with no
   text layer — automatic extraction returned nothing. Status: `BRON_GEBLOKKEERD` (technical, OCR
   or manual page-by-page inspection required), explicitly **not** `NIET_GEVONDEN`.
2. **The archive photo image itself** (`anandamayi.org/photos/118.jpg`) 404s; only the HTML
   caption page was reachable. A visual check of garden-vs-street decor in the actual image would
   help confirm or refute the Bhowanipur attribution and was not possible this pass.

## Required report fields

```
PHOTO_EVENTS_FOUND: 3
PHOTO_EVENTS_PHYSICALLY_RESOLVED: 2 fully (Ranchi R1, Serampore R1) + 1 at neighbourhood-only
  precision (Bhowanipur R5, irreducible with current sources)
UNRESOLVED_BLOCKERS: Gurupriya Devi diary is an unOCR'd scanned PDF; archive photo image 404s
ANANDAMAYI_RESEARCH_TRAVEL_SCOPE_READY: JA
```

`JA` because: all three known joint-event locations are identified and resolved as far as the
existing, consulted source corpus allows; the one residual gap (exact Bhowanipur house) has a
named, concrete, executable next step (OCR the diary) rather than an open-ended sweep; and no
further Anandamayi individual-house research is required under Mark's corrected scope unless a
new documented joint-photo event surfaces.
