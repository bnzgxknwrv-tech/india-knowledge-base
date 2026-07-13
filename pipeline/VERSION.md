# Pipelineversie

**Versie:** 2.1.0  
**Status:** implementatie gereed voor integratietest  
**Datum:** 2026-07-13

## 2.1.0

Aanleiding:
- ZILVER- en GOUD-contextmanifesten konden niet correct vooraf worden gepind omdat predecessor-output bij runcreatie nog niet bestaat;
- de verantwoordelijkheid voor het genereren van het volgende contextmanifest was niet formeel toegewezen;
- ENTRYPOINT gebruikte ten onrechte de term `niet-verlopen claim` terwijl claims niet automatisch verlopen;
- `SAMADHI` omvatte ten onrechte algemene herinneringsplaatsen;
- de pipeline was nog niet end-to-end bewezen.

Gewijzigd gedrag:
- expliciet `CONTROLLER_TRANSITION_PROTOCOL.md` toegevoegd;
- bij runcreatie wordt alleen `BRONS_CONTEXT.yaml` aangemaakt;
- na BRONS_COMPLETE valideert de controller BRONS en genereert hij pas daarna `ZILVER_CONTEXT.yaml` op de definitieve BRONS-resultaatcommit;
- na ZILVER_COMPLETE gebeurt hetzelfde voor `GOUD_CONTEXT.yaml`;
- workers genereren nooit het contextmanifest van hun opvolger;
- transitionclaims, eventtypen, toegestane controllerwrites en stopvoorwaarden vastgelegd;
- overal `geldige bestaande claim` gebruikt;
- `SAMADHI` beperkt tot graf-, as-, mahasamadhi- of expliciet als samadhi beheerde plaatsen;
- huidige status gewijzigd naar `IMPLEMENTATIE GEREED VOOR INTEGRATIETEST`.

Betrokken bestanden:
- `pipeline/ENTRYPOINT.md`;
- `pipeline/README.md`;
- `pipeline/START_PROMPTS.md`;
- `pipeline/protocols/EXECUTION_PROTOCOL.md`;
- `pipeline/protocols/CONTEXT_PROTOCOL.md`;
- `pipeline/protocols/CONTROLLER_TRANSITION_PROTOCOL.md`;
- `pipeline/templates/RUN_TEMPLATE.md`;
- `knowledge/methodology/METHODOLOGY_V2.md`.

Verwachte kwaliteitswinst:
- geen stale of onmogelijk vooraf gepind opvolgercontextmanifest;
- deterministische, controleerbare overgang tussen fasen;
- heldere scheiding tussen onderzoeksworker en controller;
- minder risico op dubbele writers, state-drift en ongeldige READY-status;
- eerlijkere operationele status totdat een volledige proefrun is geslaagd.

## 2.0.0

GitHub-native BRONS–ZILVER–GOUD-architectuur ingevoerd met geïsoleerde runs, contextmanifesten, Methodology v2.0, claim-locks, gestructureerde claims en bronnen, sentinels en completion markers.

## 1.0.0

Eerste seriële BRONS–ZILVER–GOUD-conceptversie. Deze versie was chat-gecentreerd en is vervangen.

## Wijzigingsregel

Iedere inhoudelijke protocolwijziging verhoogt de versie en vermeldt aanleiding, gewijzigd gedrag, betrokken bestanden en verwachte kwaliteitswinst. Actieve runs blijven op hun gepinde versies.

END_OF_ARTIFACT