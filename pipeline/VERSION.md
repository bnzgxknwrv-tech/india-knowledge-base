# Pipelineversie

**Versie:** 2.4.1  
**Status:** operationeel bewezen; gecontroleerde handmatige snelmodus actief  
**Datum:** 2026-07-13

## 2.4.1

Aanleiding:
- het project gebruikt naar verwachting maximaal ongeveer twintig sweeps;
- verdere platformarchitectuur kostte meer tijd dan zij binnen deze schaal bespaart;
- Vrindavan moet inhoudelijk doorgaan zonder opnieuw een theoretisch productiesysteem te ontwerpen.

Gewijzigd gedrag:
- `pipeline/OPERATING_MODE.yaml` zet de pipeline op `CONTROLLED_MANUAL_FAST`;
- onderzoeksvoortgang krijgt voorrang boven nieuwe architectuur;
- slechts één actieve run tegelijk en één globaal `NEXT_ACTION.yaml` zijn voor deze projectomvang aanvaardbaar;
- n8n, event sourcing, leases, staging branches, uitgebreide schemas en autonome orchestratie zijn uitgesteld;
- alleen actuele runblockers, reeds waargenomen herhaalfouten, beveiligingsproblemen en werkelijk dataverlies rechtvaardigen directe protocolwijziging;
- actieve gepinde runs blijven op hun eigen versie werken.

Verwachte kwaliteitswinst:
- minder tijdverlies aan infrastructuur;
- sneller door BRONS, ZILVER en GOUD;
- voldoende controle voor een klein aantal sequentiële sweeps;
- architectuurwerk wordt pas hervat wanneer de werkelijke schaal dat vereist.

## 2.4.0

Zelfroutering, vaste volgende actie voor Mark, universele startopdracht en automatiseringsroadmap ingevoerd.

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
