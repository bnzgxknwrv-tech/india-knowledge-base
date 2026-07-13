# Pipelineversie

**Versie:** 2.2.1  
**Status:** implementatie gereed voor integratietest  
**Datum:** 2026-07-13

## 2.2.1

Aanleiding:
- ZILVER blokkeerde uitsluitend omdat de branch-head na contextvoorbereiding was gewijzigd;
- alle gepinde BRONS-bestanden en blob-SHA's waren inhoudelijk ongewijzigd;
- hierdoor werd een onafhankelijke protocolcommit ten onrechte als inputdrift behandeld.

Gewijzigd gedrag:
- `source_commit` is voortaan de gepinde invoersnapshot, niet een eis dat de branch-head gelijk blijft;
- onafhankelijke branch-headwijzigingen zijn toegestaan wanneer alle required files en gepinde blob-SHA's gelijk blijven;
- alleen materiële inputdrift, ontbrekende of afgekapt gelezen bestanden, state-desynchronisatie of een geldige bestaande claim blokkeren;
- de systeemles is vastgelegd als `PL-0002`.

Verwachte kwaliteitswinst:
- rollen blokkeren niet meer op ongerelateerde commits;
- actieve runs kunnen veilig naast protocolverbeteringen bestaan;
- SHA-controle beschermt de werkelijke invoer in plaats van de globale branchpositie.

## 2.2.0

Aanleiding:
- de eerste BRONS-integratietest bevatte een claimreferentie naar `R-001`, terwijl afgewezen bronnen geen unieke source-ID hadden;
- de bestaande gate benoemde referentiële integriteit, maar schreef geen volledige cross-registercontrole en geen structurele leeractie voor.

Gewijzigd gedrag:
- `CONTINUOUS_LEARNING_PROTOCOL.md` toegevoegd;
- iedere fout wordt geclassificeerd en krijgt een expliciete leerbeslissing;
- lokale runreparatie en structurele systeemverbetering zijn strikt gescheiden;
- systeemlessen worden append-only vastgelegd in `pipeline/learning/LESSONS.jsonl`;
- quality gate valideert alle claim-sourceverwijzingen over accepted en rejected registers;
- de assistent vermeldt voortaan bij iedere fout wat lokaal wordt gerepareerd en wat blijvend aan rollen/protocollen wordt verbeterd;
- actieve runs blijven onder hun gepinde versie werken.

Verwachte kwaliteitswinst:
- dezelfde fout wordt niet stil in volgende runs herhaald;
- minder afhankelijkheid van chatgeheugen;
- aantoonbare en versieerbare verbetering van BRONS, ZILVER, GOUD en controller;
- structurele lessen blijven beschikbaar voor iedere toekomstige GitHub-capabele worker.

## 2.1.0

Controllertransitions, dynamische opvolgercontexten, claimterminologiecorrectie, strikte SAMADHI-definitie en integratieteststatus ingevoerd.

## 2.0.0

GitHub-native BRONS–ZILVER–GOUD-architectuur ingevoerd met geïsoleerde runs, contextmanifesten, Methodology v2.0, claim-locks, gestructureerde claims en bronnen, sentinels en completion markers.

## 1.0.0

Eerste seriële BRONS–ZILVER–GOUD-conceptversie. Deze versie was chat-gecentreerd en is vervangen.

## Wijzigingsregel

Iedere inhoudelijke protocolwijziging verhoogt de versie en vermeldt aanleiding, gewijzigd gedrag, betrokken bestanden en verwachte kwaliteitswinst. Actieve runs blijven op hun gepinde versies.

END_OF_ARTIFACT