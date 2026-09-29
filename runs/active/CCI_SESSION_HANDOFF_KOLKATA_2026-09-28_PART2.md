# SESSION-OVERDRACHT — KOLKATA-CLUSTER, VERVOLG OP INDIA24_FINAL_EXTRACTION_2026-09-28.md

Datum: 2026-09-28, laat op de dag
Branch: `agent/india8-cluster-casting` (alles hieronder al gecommit/gepusht — niets staat alleen lokaal)
Reden: Mark waarschuwde dat deze sessie weer tegen de tokenlimiet aan zit. Dit bestand vult `INDIA24_FINAL_EXTRACTION_2026-09-28.md` aan met alles wat DAARNA is gebeurd (die eerdere extractie ging over de Varanasi-afronding en de boot-coördinatie met INDIA25; dit bestand gaat over het volledige Kolkata-vervolg dat in dezelfde doorlopende sessie daarna is gedaan).

## WAAROM DIT BESTAAT
Deze sessie liep door na het schrijven van INDIA24's extractie (compactie gebeurde automatisch, geen nieuwe sessie nodig) en heeft sindsdien het hele Kolkata-cluster gebouwd en tweemaal grondig herzien. Als deze sessie nu alsnog stopt, moet een opvolger dit lezen vóór verder te werken aan Kolkata of Tiruvannamalai.

## WAT ER IS GEBEURD, CHRONOLOGISCH

1. **Kolkata kwartierplan gebouwd en herzien** — `runs/active/CCI_KOLKATA_QUARTERHOUR_PLAN_WITH_LINEAGE_LINKS_2026-09-28.md` is het hoofdbestand, meerdere keren bijgewerkt:
   - Dakshineswar-hoofdtempel verplaatst naar eind-van-dag flexibel blok op zo 10 jan; Yogoda Satsanga Math verplaatst naar eind van ma 11 jan (3,5u flexibel) — op Marks verzoek, past binnen de bestaande 6 nachten.
   - Alle reistijden die "CCI-inschatting" waren, zijn echt onderzocht (28 sep) en vervangen door gesourced/eerlijk-onzekere cijfers. **Belangrijkste correctie:** hotel↔Dakshineswar en Bagbazar↔Dakshineswar zijn realistisch 30-50 en 25-45 min, niet de eerder aangenomen 20-30 min (BT Road-congestie). Cossipore→Bagbazar: geen bron gevonden, alleen geografische inferentie.
   - Sri Yukteswar-hermitage (Serampore) en YSS Dhyana Kendra Garpar-sessietijden bijgewerkt met wat wel/niet gevonden is.
   - **Fout hersteld:** het plan claimde ten onrechte dat Yogananda zelf bij Panchavati mediteerde — onbevestigd bij onderzoek, gecorrigeerd in de kaart zelf.
   - **Hotel-open-item gecorrigeerd:** YSS Dakshineswar Math heeft wél een eigen gastenverblijf, toegankelijk voor YSS/SRF Lessons-studenten (dus ook Mark als Kriyaban) — eerdere aanname "waarschijnlijk niet beschikbaar" was fout.
   - **Meest recent (laatste commit e6272a8):** Mark's eigen grade/tijd-wensen verwerkt — Shyampukur Bati naar A*, Cossipore Udyanbati naar 2 uur, Balaram Mandir naar 1,5 uur met Mark's eigen voorwaarde ("als dat te veel tijd kost misschien niet") expliciet als eerste-inkort-optie vastgelegd. Cascade-effect eerlijk benoemd: Yogoda Satsanga Math start nu ~15:25 i.p.v. 13:30 — **dit is NOG NIET door Mark bevestigd, alleen door mij doorgerekend en gemeld.**

2. **Uitgebreide leesversie gebouwd** — `runs/active/CCI_KOLKATA_UITGEBREIDE_LEESVERSIE_2026-09-28.md` (nieuw bestand), op Marks expliciete verzoek ("UITGEBREID LEZEN... hoe groot is het, hoe lang blijven andere devotees, alles in relatie met mijn lineage"). Bevat per locatie: grootte/schaal, wat er te zien is, gesourced (of eerlijk "niet gevonden") devotee-verblijfsduur, en AOAY/Yogananda-connectie. **Belangrijkste inhoudelijke vondst:** Ramakrishna-lijn en Yogananda's Kriya-lijn zijn organisatorisch gescheiden (geen guru-op-guru-link); Belur Math komt NUL keer voor in AOAY; 4 Garpar Road draagt drie hoofdstukken inclusief de Babaji-deurbel-scène (h.37).

3. **Mark's reactie op de "lineage zwak"-framing:** ik had Shyampukur/Cossipore/Balaram Mandir als "zwakste lineage-case" gepresenteerd. Mark corrigeerde: Ramakrishna staat al in zijn EIGEN Top-X, dus Dakshineswar is sowieso een bevestigde enorme magneet — dat stond nooit ter discussie. Voor de drie andere plekken gaf hij zelf concrete grades/tijden (zie punt 1, laatste bullet). **Les: niet te snel "zwak" framen als Mark een plek al zelf op zijn Top-X heeft staan — eerst vragen/checken, niet aannemen.**

4. **Governance-bestand bijgewerkt:** `governance/MARK_CLUSTER_PREFLIGHT_PROTOCOL_2026-09-27.md` kreeg een nieuwe sectie "META-ANALYSE VAN DE KOLKATA-RONDE" (op Marks expliciete verzoek om meta/zelfreflectie). Kernbevinding: ik overtrad mijn eigen Batch C-regel (reistijden altijd echt onderzoeken vóór Fase 2) op de eerstvolgende cluster na het schrijven ervan. Nieuwe harde regels toegevoegd: Fase 2 mag niet beginnen met "CCI-inschatting" nog actief, schattingen bij twijfel naar het ruime/langzame eind, en een "heeft Mark dit zelf al opgelost?"-filter vóór elk ledger-item.

5. **WORK-coördinatie:** WORK viel offline; Mark start in plaats daarvan een schone ChatGPT-sessie ("CHAT"). Ik heb een zelfstandig te lezen brief gegeven (in de chat, niet in een apart bestand) met: repo `bnzgxknwrv-tech/india-knowledge-base`, branch `agent/india8-cluster-casting`, PR #23 als overlegkanaal, en als opdracht: Fase 1-onderzoek (Batch A/B/C) voor **Tiruvannamalai**, NIET Kolkata (om dubbel werk te voorkomen). Onbekend of Mark deze brief al aan een nieuwe CHAT-sessie heeft gegeven — **check dit bij hervatting.**

6. **Tiruvannamalai-status (nog niet gestart, wel voorbereid):** 4 nachten (15-18 jan) is gelockt en zit precies tussen Kolkata-vertrek en Chennai-buffer. Een stress-test uit 2026-09-08 (`decisions/BODH3_TIRU4_WAKING_HOURS_STRESS_TEST_RESULT_2026-09-08.md`) bevestigt dat de inhoud in 4 nachten past; enige zorg (Sri Chakra Puja op aankomstdag) heeft Mark zelf al opgelost door bewust voor de 09:00-vlucht te kiezen. Dag-invulling zelf is nog niet gebouwd — dat is de volgende cluster.

## WAT NOG OPEN STAAT (niet vergeten bij hervatting)

1. **Mark heeft de nieuwe Monday-cascade (Yogoda start ~15:25 i.p.v. 13:30) nog NIET bevestigd** — laatste bericht van mij, nog geen reactie. Vraag dit na bij hervatting, ga niet verder alsof het al akkoord is.
2. **Shyampukur/Cossipore/Balaram Mandir-tijden zijn Mark's eigen wens, maar nog niet in de DAGBELASTING-tabel-tekst volledig doorgerekend voor de allereerste transfer (hotel→Shyampukur, 08:30-09:00) — die staat nog als "CCI-inschatting, nog niet apart geverifieerd" (zie regel ~171). Dit is de ENIGE resterende ongeverifieerde hoofdtransfer in het hele Kolkata-plan — nog oppakken.**
3. **Hotel/basis-beslissing:** CCI-advies is YSS Dakshineswar-gastenverblijf aanvragen (e-mail via yssofindia.org/request-accommodation) — Mark heeft dit nog niet bevestigd of laten voorbereiden.
4. **Fase 3 (markdown+artifact-sync) en Fase 4 (pre-send checklist) voor Kolkata zijn nog niet gedaan** — er is nog geen visueel HTML-artifact voor Kolkata gebouwd (in tegenstelling tot Varanasi, dat wel een artifact heeft: `https://claude.ai/artifact/2dRBNaopomGuYTHhfQVeaV`). Overwegen of Mark dat nog wil voordat Kolkata definitief gelockt wordt.
5. **Completeness-audit Lonely Planet-laag Kolkata** (10 kandidaten: Victoria Memorial, Howrah Bridge, etc.) staat nog in het kwartierplan-bestand, nog niet door Mark gegradeerd.
6. **CHAT/WORK-brief voor Tiruvannamalai** — status onbekend of Mark die al heeft doorgegeven.

## GIT-STATUS
Alles gecommit en gepusht t/m commit `e6272a8` op `agent/india8-cluster-casting`. Geen lokale, ongecommitte wijzigingen op het moment van schrijven van dit bestand.

## VOOR EEN OPVOLGER: LEESVOLGORDE
1. Dit bestand.
2. `runs/active/INDIA24_FINAL_EXTRACTION_2026-09-28.md` (context van vóór Kolkata).
3. `runs/active/CCI_KOLKATA_QUARTERHOUR_PLAN_WITH_LINEAGE_LINKS_2026-09-28.md` (hoofdplan, huidige staat).
4. `runs/active/CCI_KOLKATA_UITGEBREIDE_LEESVERSIE_2026-09-28.md` (diepteonderzoek).
5. `governance/MARK_CLUSTER_PREFLIGHT_PROTOCOL_2026-09-27.md`, vooral de meta-analyse-secties onderaan (Varanasi én Kolkata) — dit is de opgebouwde procesdiscipline, niet opnieuw uitvinden.
6. `governance/CURRENT_TRUTH.md` voor de volledige 33-nachten-skeleton.

END
