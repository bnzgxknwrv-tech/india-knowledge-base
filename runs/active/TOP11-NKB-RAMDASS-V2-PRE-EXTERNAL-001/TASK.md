# TASK — TOP11-NKB-RAMDASS-V2-PRE-EXTERNAL-001

```
task_id: TOP11-NKB-RAMDASS-V2-PRE-EXTERNAL-001
cci_task: CCI_TASK 089
issued_by: INDIA7
issued_at: 2026-08-19
target_branch: claude/werk-je-nu-of-niet-oa10y7
state_on_issue: READY_FOR_CCI
pdf_status: VERBODEN
```

## 1. Doel

Voer twee verse, landelijke, corpus-first METHOD_V2 pre-external freezes uit:

1. Neem Karoli Baba
2. Ram Dass

Deze twee personen vormen een sterk gekoppeld netwerk, maar krijgen ieder een zelfstandige,
lossless persoonsatlas. Een plek uit een Neem Karoli Baba-verhaal is niet automatisch een plek waar
Ram Dass persoonlijk aanwezig was, en omgekeerd.

Dit is Fase 0-4 plus de interne onafhankelijke controle vóór externe vergelijking. Dit is GEEN
reconciliatietaak en GEEN regionale of clustersweep.

## 2. Blindheidsgrens — HARD

Voor beide persoonsfreezes zijn reeds onafhankelijke externe PRE-COMPARE-resultaten duurzaam
bevroren op een andere branch. Houd de interne pas schoon.

Vóórdat BEIDE interne persoonsfreezes afzonderlijk zijn geschreven en gecommit:

- lees NIET de branch `agent/chatgpt-top11-parallel-sweep`;
- lees NIET de externe Neem-Karoli-Baba- of Ram-Dass-freeze, STATUS, counts, bronlijst of commits;
- lees NIET IndiaROOD-resultaten;
- gebruik `PHASE2_RESULT.md`, `PHASE2_SYNTHESIS.md`, METHOD_V1-atlassen, bestaande
  regiokandidaten en oude kandidatenlijsten NIET als discoverychecklist;
- gebruik CCI_TASK 088 of andere reconciliaties niet om locaties voor deze twee personen te zaaien;
- voer geen repo-crosscheck uit vóór de verse persoonsfreeze van de betrokken persoon is gecommit.

Bekende oude repo-informatie mag niet worden "vergeten", maar mag de nieuwe discoveryvolgorde niet
sturen. Documenteer eerlijk als voorkennis onvermijdelijk was.

Na de tweede freezecommit: STOP. Open of reconcileer de externe freezes nog steeds NIET in deze
taak. Dat wordt een aparte opdracht, zodat de pre-external grenzen controleerbaar blijven.

## 3. Verplichte canon vóór uitvoering

Lees volledig:

1. dit `TASK.md` en bijbehorende `STATUS.md`;
2. `runs/active/TOP11-INDIA-PERSON-CENTRIC-MEGASWEEP-001/METHOD_V2.md`;
3. `governance/SWEEP_ERROR_CLASSES.md`;
4. de bron- en bewijsregels uit `governance/SWEEP_PROTOCOL.md`;
5. `decisions/TOP11_SWEEP_DEPTH_BY_PERSON_2026-08-18.md`.

De algemene repo-bootregel blijft gelden, met één tijdelijke uitzondering: externe freeze-inhoud en
oude kandidaatlijsten voor deze twee personen vallen onder de blindheidshold hierboven en worden
pas in een latere reconciliatietaak geopend.

## 4. METHOD_V2-uitvoering per persoon

Voer voor iedere persoon afzonderlijk en in de vaste volgorde uit:

### Fase 0 — corpus inventory

Inventariseer expliciet:

- officiële/lineage chronologieën en trust-/ashramgeschiedenissen;
- biografieën, autobiografieën en naaste-devotee-memoires;
- brieven, dagboeken, interviews, fotobijschriften en reisverslagen;
- familie-, host-, medische, spoor-, hotel-, tempel-, ashram- en archiefbronnen;
- beschikbare talen/spellingsvarianten;
- per bronfamilie: `FULL`, `PARTIAL`, `UNAVAILABLE` of `BRON_GEBLOKKEERD`, met reden.

### Fase 1 — lossless corpus occurrence extraction

Registreer iedere India-gerelateerde fysieke plaatsoccurrence vóór relevantiefiltering, inclusief:

- privéhuizen, kamers, veranda's, keukens, tuinen en landgoederen;
- ashrams, tempels, grotten, ghats, mela-terreinen en ziekenhuizen;
- stations, wegen, voertuigstops, hotels en dharmashala's;
- geboorte-, familie-, jeugd-, werk-, ziekte-, sterf- en crematieplaatsen;
- host-/gastheerlocaties en tijdelijk verblijf;
- alleen-plaatsniveau, naamloze en onzekere occurrences;
- negatieve bevindingen en expliciet niet bezochte plekken.

### Fase 2 — event/place normalization

Per record minimaal:

- tijdelijk record-ID;
- naam + alternatieve spellingen;
- plaats, district en staat;
- gebeurtenis + datum/periode;
- `PERSONALLY_PRESENT: JA / ONZEKER / NEE`;
- aanwezigheidstype: fysiek/levend, herinnering over andere persoon, visionair/postuum,
  latere instelling of symbolische associatie;
- `PHYSICAL_IDENTITY: EXACT / DEELS / ALLEEN_PLAATS / ONBEKEND`;
- historische plek versus huidig gebouw/instituut;
- host/gastheer/netwerk;
- bron + exacte locator;
- onzekerheid, conflict en negatieve claim.

### Fase 3 — host/network graph

Maak aantoonbare, benoemde hostgraphs. Zoek iedere relevante gastheer, familie, discipel,
organisator, arts, patroon of instelling terug naar de concrete fysieke bezoekplek. Een algemene
verklaring "host-as toegepast" volstaat niet.

### Fase 4 — discovery na corpus

Voer pas daarna brede discovery uit met alternatieve namen, transliteraties, oude districtnamen,
Hindi-/Bengaalse spellingsvarianten waar relevant, hostnamen en locatiecategorieën. Leg gebruikte
zoekroutes en negatieve zoekresultaten vast.

### Interne onafhankelijke controle

Voer na Fase 0-4 een tweede interne miss-detectionpass uit via een andere bron-/queryroute. Gebruik
de eerste genormaliseerde lijst pas bij vergelijking na de onafhankelijke pass; laat deze controle
niet ontaarden in het nalopen van een bestaande checklist.

## 5. Persoonsspecifieke scheidingsregels

### Neem Karoli Baba

Scheid strikt:

- eigen levenslange fysieke aanwezigheid;
- verhalen over Lakshman Das/Neem Karoli Baba met onzekere datering of identiteit;
- tempels/ashrams die hij persoonlijk bezocht, stichtte of inwijdde;
- instellingen die pas later ter nagedachtenis zijn gebouwd;
- devoteehuizen en kamers met aantoonbare aanwezigheid;
- verhalen waarin alleen een devotee of verteller op de plek was;
- postume/visionaire/symbolische claims.

Een eigen ashramnaam is geen automatisch bewijs van persoonlijke aanwezigheid.

### Ram Dass

Scheid strikt:

- Ram Dass' eigen Indiareizen en verblijfplaatsen;
- locaties waar hij Neem Karoli Baba werkelijk ontmoette;
- plaatsen die alleen in door hem vertelde Maharajji-verhalen voorkomen;
- huizen/hotels/ashrams/stations/medische locaties waar Ram Dass zelf aanwezig was;
- latere herdenkings-, retreat- of organisatieplekken zonder zijn fysieke aanwezigheid;
- buitenlandse plekken: bewaren als context indien bronmatig nodig, maar niet als India-atlasrecord.

### Gekoppeld netwerk

Houd records fysiek en persoonsmatig gescheiden. Pas nadat beide afzonderlijke freezes gecommit
zijn, mag in een korte interne notitie worden aangegeven welke locaties vermoedelijk dezelfde
fysieke site delen. Geen externe vergelijking in deze taak.

## 6. Verplichte output

Schrijf onder:

`runs/active/TOP11-NKB-RAMDASS-V2-PRE-EXTERNAL-001/`

1. `NEEM_KAROLI_BABA_V2_PRE_EXTERNAL_FREEZE.md`
2. `RAM_DASS_V2_PRE_EXTERNAL_FREEZE.md`
3. `STATUS.md`

Werk daarnaast bij:

4. `runs/active/TOP11-INDIA-PERSON-CENTRIC-MEGASWEEP-001/STATUS.md`
5. `governance/INDIA_SESSION_START.md`

Iedere freeze bevat minimaal:

- corpuscoverage-matrix;
- lossless occurrence-/locatie-inventaris;
- genormaliseerde atlas;
- benoemde hostgraph;
- discoverylog;
- negatieve en uitgesloten claims;
- lijst van bronblokkades en onopgeloste tijdvakken;
- pre-external gatebeoordeling;
- `PERSON_V2_PRE_EXTERNAL_SATURATED: JA/NEE`, eerlijk gemotiveerd;
- exacte volgende stap.

Geen permanente locatie-ID's toekennen.

## 7. Checkpoint- en contextverliesregel

1. Werk Neem Karoli Baba volledig af.
2. Schrijf freeze + status duurzaam weg.
3. Commit Neem Karoli Baba als zelfstandig checkpoint.
4. Werk daarna Ram Dass volledig af.
5. Schrijf freeze + status duurzaam weg.
6. Commit Ram Dass als zelfstandig checkpoint.
7. Maak een korte finale statecommit indien governance/status nog apart moeten worden bijgewerkt.

Wacht niet tot het einde met committen. Bij contextverlies hervat exact vanaf de laatste duurzame
checkpoint; herstart geen afgeronde persoon. Subagents/workers zijn alleen toegestaan als hun
afgeronde werkpakket onmiddellijk duurzaam wordt weggeschreven.

## 8. Saturation en stopvoorwaarde

Een pre-external `JA` mag alleen wanneer corpuscoverage, hostgraph en discovery aantoonbaar zijn
afgerond. De projectbrede `PERSON_SWEEP_SATURATED: JA` mag in deze taak NIET worden geclaimd,
omdat externe multi-detectorreconciliatie nog ontbreekt.

Stop pas wanneer beide freeze-bestanden, beide persoonscheckpointcommits en de state-updates
bestaan. Plaats daarna één korte CCI_RESULT-envelop op PR #23 met:

- volledige commit-SHA per persoon;
- bestandspad per freeze;
- counts per persoon;
- gate-uitkomsten;
- bronblokkades en grootste open hiaten;
- bevestiging dat externe freezes niet zijn geopend;
- `next_allowed_step: externe lossless reconciliatie in aparte taak`.

## 9. Harde grenzen

- Geen externe freeze openen of vergelijken.
- Geen IndiaROOD-resultaten lezen.
- Geen clusterheatmap.
- Geen regionale of clustersweep.
- Geen Arunachala/Tiruvannamalai-werk.
- Geen A/B/C namens Mark.
- Geen permanente IDs of globale nummering.
- Geen PDF.
- Geen route, nachten, vervoer of binnenlandse vluchten.
- Start Ramana Maharshi of Ramakrishna niet automatisch.
- Wijzig/merge geen externe branch en raak PR #24 niet aan.
- Stop na de CCI_RESULT-envelop en wacht op INDIA-QA.
