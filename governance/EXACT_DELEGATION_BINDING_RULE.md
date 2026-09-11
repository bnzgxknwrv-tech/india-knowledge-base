# EXACT DELEGATION BINDING RULE

Status: **HARD / SUCCESSOR-REQUIRED / CCI-WORK DISPATCH SAFETY**
Effective: 2026-09-11
Owner: Mark / INDIA regie
Branch: `agent/india8-cluster-casting`

## Waarom deze regel bestaat

Mark heeft expliciet vastgesteld dat algemene startzinnen zoals `voer de nieuwste taak uit`, `check de nieuwste planning` of `ga verder met de laatste opdracht` te ambigu zijn zodra PR #23 meerdere CCI/WORK-taken, oudere resultaten of parallelle audits bevat.

Dat heeft al geleid tot verwarring over welke taak een worker bedoelde en tot het risico dat een oudere opdracht of verkeerde artifactversie wordt uitgevoerd.

Daarom geldt vanaf nu voor INDIA19 en iedere opvolger:

> **Iedere delegatie aan CCI of WORK moet exact worden gebonden aan de bedoelde taak en artifactversie.**

## Verplichte velden bij iedere CCI/WORK-start

Een startopdracht moet, voor zover van toepassing, expliciet bevatten:

1. **exact PR-nummer**;
2. **exact PR-comment-ID van de taak**;
3. **exacte taakheader** (`CCI_TASK ...` of `WORK_TASK ...`);
4. **exacte commit-SHA / AUDIT_PACKET_HEAD / frozen input commit** waarop gewerkt moet worden;
5. **exact bestand of artifactpad** dat gecontroleerd of verwerkt moet worden;
6. **exacte tegenpartij-commit/resultaatbinding** bij cross-red-team/auditwerk;
7. **wat nadrukkelijk NIET opnieuw gedaan mag worden** (bijv. geen nieuwe globale solve, geen nieuwe research, frozen solve niet wijzigen);
8. **exacte verwachte resultaatkop** (`CCI_RESULT ...` / `WORK_RESULT ...`);
9. indien relevant: **solution-blind / independent-audit regel** en welk resultaat nog NIET gelezen mag worden.

## Verboden als enige instructie

De volgende formuleringen zijn op zichzelf onvoldoende en mogen niet als enige startinstructie worden gebruikt wanneer meerdere taken of versies kunnen bestaan:

- `Voer de nieuwste taak uit.`
- `Voer de nieuwste CCI_TASK uit.`
- `Voer de nieuwste WORK_TASK uit.`
- `Check de nieuwste planning.`
- `Ga verder waar je was.`
- `Doe de audit.`

Een korte startzin mag alleen als ALLE exacte bindingen al ondubbelzinnig in dezelfde actieve opdracht staan en er aantoonbaar geen concurrerende taak/version bestaat. Bij twijfel: **altijd exact specificeren**.

## Statuscontrole vóór opnieuw starten

Voordat INDIA een nieuwe startinstructie aan CCI of WORK geeft:

1. lees PR #23 opnieuw;
2. zoek de exacte resultaatheader van de bedoelde taak;
3. bepaal of die worker al loopt of klaar is;
4. start een reeds lopende/afgeronde taak NIET opnieuw;
5. als één partij klaar is en de andere niet, geef alleen de nog benodigde partij een echte startopdracht; voor de andere: `geen nieuwe actie`.

## Resultaatbinding

Een resultaat telt alleen als resultaat van de bedoelde taak wanneer het aantoonbaar verwijst naar dezelfde:

- taakcomment;
- commit/head;
- artifact/bestand;
- en verwachte resultaatheader.

`klaar`, `done`, `complete` of een generieke `PASS` zonder die binding is onvoldoende bewijs.

## Mark-facing copy blocks

Als Mark zelf iets moet starten, eindigt INDIA met twee korte afzonderlijke kopieerbare blokken wanneer beide rollen relevant zijn:

- `CCI:` met exact gebonden startinstructie of expliciet `geen nieuwe actie`;
- `WORK:` met exact gebonden startinstructie of expliciet `geen nieuwe actie`.

De blokken mogen kort zijn, maar mogen de noodzakelijke binding niet verliezen.

## Successor rule

Iedere nieuwe INDIA-sessie moet deze regel actief toepassen alsof Mark hem zojuist in de chat heeft herhaald.

Pre-answer/delegation test:

- `EXACT_TASK_COMMENT_BOUND?`
- `EXACT_COMMIT_OR_HEAD_BOUND?`
- `EXACT_ARTIFACT_BOUND?`
- `EXPECTED_RESULT_HEADER_BOUND?`
- `CURRENT_STATUS_RECHECKED?`

Eén relevante `NO` of `UNKNOWN` = **niet delegeren; eerst exact binden of status ophalen**.
