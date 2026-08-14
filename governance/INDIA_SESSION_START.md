# INDIA_SESSION_START — duurzame bootstrap voor iedere nieuwe INDIA-regisseursessie

Datum snapshot: 2026-08-14

## Doel
Dit bestand maakt de huidige ChatGPT/INDIA-regisseur vervangbaar. Een nieuwe sessie hoeft de oude chat niet te lezen en mag Mark niet vragen de geschiedenis opnieuw uit te leggen.

## Eerste leesvolgorde
1. `governance/ACTIVE_STATE.md`
2. `governance/SWEEP_PROTOCOL.md`
3. dit bestand opnieuw als korte operationele samenvatting
4. het `STATUS.md` van de nieuwste actieve taak
5. het bijbehorende `TASK.md`
6. lees bij Kumaon óók de LIVE STATE hieronder vóór een `RESULT.md` wordt geopend; respecteer blindheid tussen onafhankelijke sweeps.

GitHub is de duurzame bron van waarheid. Oude chatgeschiedenis is niet nodig voor voortzetting.

## Projectdoel van Mark
De reis draait primair om:
1. iedere verifieerbare fysieke plek uit of direct verbonden met *Autobiography of a Yogi* (AOAY), hoe klein ook;
2. iedere relevante fysieke plek verbonden met Marks Top-11;
3. daarnaast alleen echte zelfstandige spirituele/pelgrimszwaargewichten als bonuslaag.

Top-11, in vaste volgorde:
1. Paramahansa Yogananda
2. Mahavatar Babaji
3. Lahiri Mahasaya
4. Sri Yukteswar
5. Ram Dass
6. Neem Karoli Baba
7. Anandamayi Ma
8. Ramakrishna
9. Ramana Maharshi
10. Hariharananda
11. Vivekananda

Geen A/B/C voorspellen namens Mark. Bestaande Mark-besluiten zijn beschermd en worden nooit stilzwijgend heropend. Nieuwe cruciale informatie kan alleen een `MARK_DECISION_CONFLICT` veroorzaken.

## Werkverdeling
- INDIA = regisseur, onafhankelijke tweede sweep, QA, synthese, bepaalt volgende stap.
- CCI = brononderzoek, extractie, bestanden, validators, reconciliatie en commits.
- Mark = doelen, echte persoonlijke keuzes en uiteindelijke A/B/C.
- PR #23 = korte relay/index; lange taakinhoud staat in `runs/active/<TASK_ID>/TASK.md`, status in `STATUS.md`, resultaat in `RESULT.md`.

## Harde onderzoeksregels
- V2 dubbele sweep: CCI Sweep A + onafhankelijke INDIA Sweep B + reconciliatie.
- Sweep B gebruikt Sweep A niet als zoekbasis.
- Open/retrieve daadwerkelijke brontekst voor keuze-relevante claims; geen snippet-only bevestigingen.
- AOAY en elk van de 11 Top-11-namen worden systematisch afgedekt, inclusief negatieve resultaten.
- Laag 3 is religie-onafhankelijk maar alleen voor echte zware pelgrims/spirituele locaties; geen quota.
- Geen PDF tenzij Mark expliciet `PDF_GO` geeft.
- Geen onnodige vragen aan Mark wanneer scope uit canon/repo kan worden bepaald.

## Afgeronde zware regio's
- VARANASI: inhoudelijke keuzefase afgerond; 001–040 beoordeeld en beschermd; 041–045 alleen op Marks initiatief.
- BODH GAYA: inhoudelijke keuzefase afgerond; 046–078-set verwerkt; bestaande Mark-keuzes beschermd; geen nieuwe Bodh Gaya-PDF.
- GAYA AIRPORT → BODH GAYA corridor: `DOUBLE_SWEEP_COMPLETED_RECONCILED`; 0 nieuwe fysieke kandidaten; 079 bleef ongebruikt.

## Regioprioriteit vanaf deze snapshot
Eerst de zware kernregio's, niet kleine toevallige vondsten.
1. KUMAON / BABAJI / DWARAHAT / KAINCHI — nu eerst.
2. TIRUVANNAMALAI / ARUNACHALA.
3. KOLKATA / SERAMPORE.
Rajgir/Nalanda staat voorlopig NIET in beeld als volgende actieve regio.

## Actuele keuze: Kumaon opnieuw, maar blind en modern
De oude repo bevat al veel `KUMAON-COMPLETE-001`-onderzoek en oudere locaties/Mark-statussen. Dat werk wordt NIET weggegooid, maar mag de nieuwe discovery niet sturen.

Aanpak voor `KUMAON-V2-RESWEEP-001`:
1. CCI Sweep A volledig vers vanaf nul onder huidige AOAY + Top-11 + laag-3-regels, zonder oude Kumaon-kandidatenlijst als zoekbasis.
2. INDIA Sweep B volledig onafhankelijk en blind voor zowel CCI Sweep A als de oude kandidaatset als discovery-basis.
3. Pas na beide sweeps wordt het oude Kumaon-onderzoek geopend als benchmark.
4. Reconciliatie vergelijkt `NIEUW∩OUD`, `NIEUW\OUD`, `OUD\NIEUW` en bronconflicten.
5. Oude Mark-besluiten/IDs nooit automatisch wijzigen; legacy-only locaties worden opnieuw geverifieerd, niet stil verwijderd.
6. Nieuwe fysieke vondsten krijgen pas na reconciliatie een permanente ID volgens de dan geldende registry; tijdens blinde discovery alleen tijdelijke sweep-ID's gebruiken.

## LIVE STATE — KUMAON-V2-RESWEEP-001

- CCI Sweep A: door Mark gestart en op dit snapshotmoment nog bezig; canonieke status altijd opnieuw controleren in `runs/active/KUMAON-V2-RESWEEP-001/STATUS.md`.
- INDIA Sweep B: REEDS parallel en blind uitgevoerd vóór inzage in CCI Sweep A of oude Kumaon-candidates.
- Sweep-B-bestand: `runs/active/KUMAON-V2-RESWEEP-001/INDIA_SWEEP_B.md`
- Sweep-B-branch: `india/kumaon-v2-sweep-b-001`
- Sweep-B-freeze-commit: `41bd4a7caebe83e44b9ee2470ecf1212d5111d9e`
- Sweep-B-status: `SWEEP_B_FROZEN_BLIND`.
- Blindheidsattest en tijdelijke `KB2-*`-kandidaten staan in dat bestand.
- CCI mag Sweep B niet gebruiken om zijn nog lopende Sweep A te sturen.

### NEXT_ACTION exact
1. Controleer canonieke `STATUS.md`.
2. Als CCI Sweep A NOG loopt: wijzig/lees CCI-resultaat niet als sturing; er is geen extra Mark-actie nodig.
3. Zodra CCI Sweep A expliciet KLAAR/BEVROREN is: open CCI `RESULT.md` en het reeds bevroren `INDIA_SWEEP_B.md`.
4. Vergelijk A vs B.
5. Open PAS DAARNA legacy `KUMAON-COMPLETE-001` en relevante oude Mark-besluiten als benchmark.
6. Reconcileer `NIEUW_INTERSECT_OUD`, `NIEUW_MIN_OUD`, `OUD_MIN_NIEUW`, `BRON_CONFLICTEN` en eventuele `MARK_BESLUIT_CONFLICTEN`.
7. Geen PDF en geen A/B/C voorspellen; daarna pas compacte keuze-ready kandidaatoutput voor Mark.

## Actieve taak
`runs/active/KUMAON-V2-RESWEEP-001/TASK.md`

## Startzin voor een nieuwe ChatGPT-sessie
Gebruik als eerste bericht:

`Neem de INDIA-regie over. Lees via GitHub eerst governance/INDIA_SESSION_START.md en volg de daar genoemde leesvolgorde. Oude chatgeschiedenis is niet nodig. Handel daarna direct de actuele NEXT_ACTION af zonder mij de geschiedenis opnieuw te laten uitleggen.`

## Successorregel
Een opvolgsessie die dit bestand + ACTIVE_STATE + actuele TASK/STATUS heeft gelezen, neemt dezelfde functionele rol over. Sessielabels (INDIA6/INDIA7/etc.) zijn alleen informatief en mogen nooit nodig zijn om de workflow te begrijpen.
