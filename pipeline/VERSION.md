# Pipelineversie

**Versie:** 2.4.0  
**Status:** operationeel bewezen; zelfrouterende minimale-MARK-workflow ingevoerd  
**Datum:** 2026-07-13

## 2.4.0

Aanleiding:
- Mark moest completion- en blockerberichten nog zelf interpreteren en naar de juiste chat kopiëren;
- afzonderlijke lange startprompts en handmatige tussenregie veroorzaakten onnodige stappen;
- een ChatGPT-worker kan de GitHub-connector niet autonoom naar een andere chat verplaatsen of daar inschakelen.

Gewijzigd gedrag:
- `SELF_ROUTING_PROTOCOL.md` toegevoegd;
- iedere metaalworker geeft exact één bestemming, één volgende actie voor Mark en een volledig kopieerbare doorstuurtekst;
- BRONS en ZILVER mogen alleen rechtstreeks naar het volgende metaal wanneer een controller de volgende READY-state en context al aantoonbaar heeft voorbereid;
- GOUD gaat altijd eerst naar SUBREGIE INDIA voor technische eindvalidatie;
- universele startopdracht en `NEXT_ACTION_TEMPLATE.yaml` toegevoegd;
- automatiseringsroute via GitHub Actions en optionele externe orchestratie vastgelegd;
- rollen BRONS, ZILVER en GOUD aangescherpt op zelfroutering en vaste berichtvorm.

Verwachte kwaliteitswinst:
- Mark hoeft technische berichten niet meer te interpreteren;
- minder kopieerwerk en minder kans op verkeerde bestemming;
- dezelfde startopdracht kan voor iedere volgende metaalchat worden gebruikt;
- controllerautomatisering kan later de tussenkomst van SUBREGIE INDIA tussen fasen grotendeels verwijderen;
- heldere grens tussen wat via de ChatGPT-connector kan en wat een externe orchestrator vereist.

## 2.3.0

SUBREGIE INDIA en de schone interface met INDIA2 ingevoerd. De eerste end-to-end BRONS-ZILVER-GOUD-run verklaarde de pipeline operationeel bewezen.

## 2.2.1

Source-commitsemantiek gecorrigeerd: branch-headwijziging blokkeert niet wanneer alle gepinde required-file blob-SHA's gelijk blijven. Systeemles `PL-0002`.

## 2.2.0

Continuous learning ingevoerd met foutclassificatie, gescheiden runreparatie/systeemverbetering, learning register en cross-register source-ID-validatie.

## 2.1.0

Controllertransitions, dynamische opvolgercontexten, claimterminologiecorrectie, strikte SAMADHI-definitie en integratieteststatus ingevoerd.

## 2.0.0

GitHub-native BRONS–ZILVER–GOUD-architectuur ingevoerd met geïsoleerde runs, contextmanifesten, Methodology v2.0, claim-locks, gestructureerde claims en bronnen, sentinels en completion markers.

## 1.0.0

Eerste seriële BRONS–ZILVER–GOUD-conceptversie. Deze versie was chat-gecentreerd en is vervangen.

## Wijzigingsregel

Iedere inhoudelijke protocolwijziging verhoogt de versie en vermeldt aanleiding, gewijzigd gedrag, betrokken bestanden en verwachte kwaliteitswinst. Actieve runs blijven op hun gepinde versies.

END_OF_ARTIFACT