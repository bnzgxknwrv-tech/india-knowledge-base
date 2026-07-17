# ROLE_HANDOFF_PROTOCOL v1.0

## Doel

Nieuwe runs gebruiken de keten:

`INDIA2 -> BRONS -> inline controller -> ZILVER -> inline controller -> GOUD -> Mark`

Mark kopieert alleen de geldige overdracht naar een verse ZILVER-chat en daarna naar een verse GOUD-chat.

## Toepassing

Dit protocol geldt alleen wanneer `run.yaml` dit bestand pint en `pipeline/NEXT_ACTION.yaml` een geldig `post_completion`-blok bevat. Oude, reeds gepinde of geclaimde runs blijven hun oude proces volgen.

## Rolgrens

BRONS en ZILVER maken nooit als worker het contextmanifest van hun opvolger. Bij `post_completion.mode: INLINE_POST_PHASE_CONTROLLER` mag dezelfde sessie pas na volledige fasecompletion een afzonderlijke controllerrol starten.

Verplichte volgorde:

1. Schrijf en valideer alle fase-artifacts.
2. Commit de fase en schrijf completionstate en completionevent.
3. Beëindig de workerrol; verdere fasewrites zijn verboden.
4. Lees de controllerprotocollen opnieuw en herhaal GitHub-preflight.
5. Controleer dat inline control expliciet is toegestaan.
6. Schrijf een nieuwe controllerclaim; hergebruik de workerclaim nooit.
7. Valideer predecessor, sentinels, registers, state en events.
8. Stel de definitieve predecessorcommit vast.
9. Maak en pin het opvolgercontextmanifest.
10. Synchroniseer state, events en `pipeline/NEXT_ACTION.yaml`.
11. Commit de transition en voer volledige readback uit.
12. Lever alleen bij volledige overeenstemming de volgende startopdracht.

## Overdracht

De geplakte overdracht bevat alleen bediening en GitHub-pointers. Zij is nooit inhoudelijk predecessorbewijs. De volgende rol herleest altijd de gepinde GitHub-context.

`NEXT_ROLE_READY: YES` is alleen geldig wanneer state en events synchroon zijn, het contextmanifest en de hashes kloppen, NEXT_ACTION exact naar de opvolger wijst, geen claim actief blijft en finale readback is geslaagd.

Bij een afwijking geldt `NEXT_ROLE_READY: NO` en:

`VOLGENDE_METAAL_STARTOPDRACHT: GEEN — EERST BLOCKER OPLOSSEN.`

## GOUD

Bij `post_completion.mode: MARK_FINAL_REPORT` schrijft GOUD verplicht:

`research/active/<RUN_ID>/GOUD/MARK_FINAL_REPORT.md`

GOUD commit en leest het rapport opnieuw en toont daarna hetzelfde volledige rapport rechtstreeks aan Mark. Een geldige PASS of PARTIAL vereist geen normale terugkeer naar INDIA2.

## Harde verboden

- Geen opvolgercontext door de workerrol.
- Geen workerclaim hergebruiken als controllerclaim.
- Geen fasewrites na de rolwissel.
- Geen volgende prompt zonder geldige READY-state.
- Geen stil inhoudelijk herstel tijdens de transition.
- Geen protocolwijziging binnen een actieve run.
- Geen nieuwe formele of adviserende A/B/C-status door een metaal.

## Fallback

Wanneer inline control niet expliciet is gepind of niet veilig slaagt, blijft de fasecompletion behouden maar wordt geen opvolgercontext of READY-state gemaakt. Routeer dan naar SUBREGIE INDIA voor technisch herstel of naar INDIA2 voor een echt inhoudelijk beslispunt.

END_OF_ARTIFACT