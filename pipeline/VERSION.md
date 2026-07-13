# Pipelineversie

**Versie:** 2.3.0  
**Status:** operationeel bewezen; regie-interface ingevoerd  
**Datum:** 2026-07-13

## 2.3.0

Aanleiding:
- de eerste end-to-end run heeft BRONS, controllertransition, ZILVER, controllertransition en GOUD volledig doorlopen;
- INDIA2 moet inhoudelijk schoon blijven en niet worden belast met workercoördinatie, state/events, connectorproblemen en protocolreparaties;
- er ontbrak een formele vaste tussenregie tussen Mark, de drie metalen en INDIA2.

Gewijzigd gedrag:
- `SUBREGIE INDIA` toegevoegd als vaste pipeline- en kwaliteitsregie;
- rolcontract toegevoegd onder `pipeline/roles/SUBREGIE_INDIA.md`;
- verplichte routering tussen INDIA2 en SUBREGIE INDIA vastgelegd in `pipeline/protocols/REGIE_INTERFACE_PROTOCOL.md`;
- INDIA2 stuurt alle operationele pipelineberichten verplicht door en ontvangt alleen een gevalideerd GOUD-regisseurspakket;
- SUBREGIE INDIA mag technische pipeline- en efficiëntieverbeteringen zelfstandig uitvoeren;
- methodologische en projectinhoudelijke wijzigingen blijven bij INDIA2 en Mark;
- berichtvorm en harde GitHub-connectorfoutmelding vastgelegd.

Verwachte kwaliteitswinst:
- INDIA2 blijft gericht op inhoudelijke projectkoers en integratie;
- minder contextvervuiling door technische uitvoeringsdetails;
- één consistente begeleider voor alle metalen en controllertransitions;
- snellere foutafhandeling en structureel leren tussen runs;
- duidelijkere bevoegdheidsgrenzen tussen Mark, INDIA2 en pipeline-uitvoering.

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