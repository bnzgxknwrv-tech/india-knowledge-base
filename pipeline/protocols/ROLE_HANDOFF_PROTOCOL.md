# ROLE_HANDOFF_PROTOCOL v1.1

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
2. Commit de fase, schrijf completionstate en completionevent en sluit de workerclaim met `claim_status: CLOSED`.
3. Controleer dat de gesloten workerclaim dezelfde completioncommit noemt.
4. Beëindig de workerrol; verdere fasewrites zijn verboden.
5. Lees de controllerprotocollen opnieuw en herhaal GitHub-preflight.
6. Controleer dat inline control expliciet is toegestaan.
7. Schrijf een nieuwe controllerclaim met `claim_status: ACTIVE`; hergebruik de workerclaim nooit.
8. Valideer predecessor, sentinels, registers, state en events.
9. Stel de definitieve predecessorcommit vast.
10. Maak en pin het opvolgercontextmanifest.
11. Synchroniseer state, events en `pipeline/NEXT_ACTION.yaml`.
12. Sluit de controllerclaim in de transitioncommit.
13. Commit de transition en voer volledige readback uit.
14. Lever alleen bij volledige overeenstemming de volgende startopdracht.

## Overdracht

De geplakte overdracht bevat alleen bediening en GitHub-pointers. Zij is nooit inhoudelijk predecessorbewijs. De volgende rol herleest altijd de gepinde GitHub-context.

`NEXT_ROLE_READY: YES` is alleen geldig wanneer state en events synchroon zijn, het contextmanifest en de hashes kloppen, NEXT_ACTION exact naar de opvolger wijst, worker- en controllerclaims `CLOSED` zijn, geen andere actieve claim bestaat en finale readback is geslaagd.

Bij een afwijking geldt `NEXT_ROLE_READY: NO` en:

`VOLGENDE_METAAL_STARTOPDRACHT: GEEN — EERST BLOCKER OPLOSSEN.`

## GOUD

Bij `post_completion.mode: MARK_FINAL_REPORT` schrijft GOUD verplicht:

- `research/active/<RUN_ID>/GOUD/MARK_FINAL_REPORT.md`;
- `research/active/<RUN_ID>/GOUD/CANONICAL_INTEGRATION_PROPOSAL.md`.

Wanneer `canonical_integration.mode: DETERMINISTIC_NON_DECISIONAL` expliciet is gepind, voert GOUD uitsluitend de toegestane mechanische integratie uit volgens het gepinde voorsteltemplate. GOUD wijzigt geen formele of adviserende A/B/C-status en creëert geen nieuwe decision-ID of beslistekst.

Na canonieke writes controleert GOUD syntax, unieke LOCATION_ID's, bestaande decision-ID's, ongewijzigde A/B/C-velden en finale readback. Daarna commit GOUD, sluit de workerclaim en toont het volledige Markrapport inhoudelijk gelijk in de chat.

Wanneer een inhoudelijke beslissing van Mark nodig is, wordt de betreffende canonieke wijziging niet toegepast. Het eindrapport bevat dan exact:

- `MARK_DECISION_REQUIRED: YES`;
- de concrete keuze;
- de gevolgen per optie;
- de eerstvolgende korte handeling voor Mark.

Een geldige PASS of PARTIAL vereist geen normale eindredactie door INDIA2. INDIA2 blijft alleen nodig voor echte cross-run koerskeuzes of besluiten die Mark niet rechtstreeks in het rapport kan nemen.

## Harde verboden

- Geen opvolgercontext door de workerrol.
- Geen workerclaim hergebruiken als controllerclaim.
- Geen fasewrites na de rolwissel.
- Geen volgende prompt zonder geldige READY-state.
- Geen stil inhoudelijk herstel tijdens de transition.
- Geen protocolwijziging binnen een actieve run.
- Geen nieuwe formele of adviserende A/B/C-status door een metaal.
- Geen canonieke write buiten het vooraf geschreven integratievoorstel.
- Geen canonieke write wanneer een beslissing van Mark nodig is.

## Fallback

Wanneer inline control niet expliciet is gepind of niet veilig slaagt, blijft de fasecompletion behouden maar wordt geen opvolgercontext of READY-state gemaakt. Routeer dan naar SUBREGIE INDIA voor technisch herstel of naar INDIA2 voor een echt inhoudelijk beslispunt.

END_OF_ARTIFACT