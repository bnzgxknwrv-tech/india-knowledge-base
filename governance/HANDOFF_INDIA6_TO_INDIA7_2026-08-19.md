# HANDOFF INDIA6 -> INDIA7

Datum: 2026-08-19
Status: DURABLE SUCCESSOR HANDOFF — BIJGEWERKT NA 087R + EXTERNE CHATGPT-FREEZES
Repo: `bnzgxknwrv-tech/india-knowledge-base`
Actieve CCI-werkbranch: `claude/werk-je-nu-of-niet-oa10y7`
PR relay: #23

## 1. ROLCONTINUITEIT
- INDIA7 is de directe functionele opvolger van INDIA6 en daarmee van INDIA2.
- INDIA3/INDIA4/INDIA5 waren experimentele/mislukte architecturen en zijn geen inhoudelijke rolvoorgangers.
- Mark bepaalt doelen, voorkeuren en A/B/C-keuzes.
- ChatGPT/INDIA = regisseur, onafhankelijke bronredenering/synthese, CCI-tasking en QA.
- CCI = Claude Code India, uitvoerende research/GitHub-engine.
- Losse externe AI-runs = onafhankelijke detectorlagen; geen claims als waarheid behandelen zonder bronverificatie.

## 2. WERKSTIJL
- Handel eerst, praat daarna.
- Als iets moet gebeuren: dezelfde beurt uitvoeren met tools of exacte uitvoeractie geven.
- Na afronding altijd direct `what's next` bepalen.
- Kort/direct; technische details alleen indien nodig/gevraagd.
- Geen passieve TODO's.
- Alles dat Mark naar een andere AI moet plakken volledig in één los fenced code block.
- Geen PDF tenzij Mark expliciet vraagt.
- Geen oude beslissingen heropenen zonder nieuwe cruciale informatie.

## 3. HOOFDARCHITECTUUR
Strategische volgorde LOCKED:
`LANDELIJKE PERSONEN-SWEEPS -> EXTERNAL BLIND FREEZES -> RECONCILIATIE -> CLUSTERHEATMAP -> REGIONALE CLUSTERSWEEPS -> MARK A/B/C -> ROUTE`

METHOD_V2:
`CORPUS INVENTORY -> LOSSLESS CORPUS OCCURRENCE EXTRACTION -> EVENT/PLACE NORMALIZATION -> HOST/NETWORK GRAPH -> WEB DISCOVERY -> INDIA INDEPENDENT METHOD PASS -> EXTERNAL MULTI-AI ADVERSARIAL UNION -> DIRECT VERIFICATION/RECONCILIATION -> SATURATION`

Yogananda-benchmark:
- externe union leverde echte interne misses;
- 8/8 rechtstreeks getoetste externe kandidaten waren `VERIFIED_TRUE`;
- CCI vond zelf Regent Hotel Bombay, gemist door alle vijf externe AI's.
Verdict: `EXTERNAL_MULTI_AI_MANDATORY_FOR_REMAINING_TOP11: JA` voor alle full-deep personen.

## 4. SWEEPDIEPTE — LOCKED_BY_MARK
Volledige landelijke METHOD_V2 deep sweep:
1. Paramahansa Yogananda
2. Mahavatar Babaji
3. Lahiri Mahasaya
4. Sri Yukteswar
5. Neem Karoli Baba
6. Ram Dass
7. Ramana Maharshi
8. Ramakrishna

Anandamayi Ma:
- al uitzonderlijk breed behandeld via source-first + externe union + reconciliatie;
- niet opnieuw vanaf nul.

Targeted-only, GEEN exhaustieve landelijke sweep:
- Vivekananda: alleen grootste/belangrijkste fysieke locaties.
- Hariharananda: alleen grootste/belangrijkste fysieke locaties.

Ramakrishna is expliciet full-deep omdat hij ondervertegenwoordigd was. Mark wil graag minstens één wezenlijke Ramakrishna-locatie bezoeken indien logisch passend; geen geforceerde grote omweg.

## 5. CCI_TASK 087 / 087R — AFGEROND
087 = Babaji + Lahiri Mahasaya + Sri Yukteswar, nationale METHOD_V2 pre-external freezes.
087R = recovery na max-context.

Uitkomst:
- eerste poging met 3 parallelle subagents faalde door sessielimiet zonder duurzame output;
- CCI controleerde vervolgens durable state en voerde de drie freezes direct uit;
- checkpoint commits:
  - Babaji `6b79f1c`
  - Lahiri Mahasaya `642e464`
  - Sri Yukteswar `ea60ba5`
  - STATUS + governance `7af5c4c`
- bestanden:
  - `runs/active/TOP11-INDIA-PERSON-CENTRIC-MEGASWEEP-001/BABAJI_V2_PRE_EXTERNAL_FREEZE.md`
  - `.../LAHIRI_MAHASAYA_V2_PRE_EXTERNAL_FREEZE.md`
  - `.../SRI_YUKTESWAR_V2_PRE_EXTERNAL_FREEZE.md`
- alle drie `SATURATED: NEE` met expliciete hiaten.

NEXT voor deze drie:
- blanco externe multi-AI sweeps / externe blind data gebruiken;
- daarna directe verificatie + reconciliatie;
- geen cluster/regio/A-B-C/route vóór deze nationale fase correct is verwerkt.

## 6. GITHUB-COMMENT WEKT CCI AUTOMATISCH
Mark heeft daadwerkelijk een Claude Code event gezien:
`<wake reason="external-event">` met `source="github" kind="issue_comment.created"` voor CCI_TASK 087R.

Operationele regel:
- nieuwe CCI_TASK als top-level PR #23-comment wekt CCI automatisch;
- Mark hoeft CCI normaal NIET handmatig te starten;
- geen duplicate task plaatsen omdat resultaat niet onmiddellijk terugkomt;
- eerst actuele PR #23-state controleren;
- alleen bij aantoonbare trigger-failure escaleren.

## 7. ONAFHANKELIJKE CHATGPT-BLINDSWEEP — ALLE ACHT FREEZES KLAAR
Aparte branch:
`agent/chatgpt-top11-parallel-sweep`

Taak:
`runs/active/TOP11-PARALLEL-CHATGPT-SWEEP-001/TASK.md`

Status op 2026-08-19:
`ALL_EIGHT_PRE_COMPARE_FREEZES_COMPLETE_STOP`

Alle acht onafhankelijke PRE-COMPARE freezes zijn klaar, zonder interne CCI/person-atlas vergelijking:
- Yogananda: 127 locaties — freeze `69a387d162b4fe7b89b63bbd1b11f0d56e62443d` — saturation NEE
- Mahavatar Babaji: 35 — `f565ff163e35597d2c4ed802676a4671f9da3b70` — saturation NEE
- Lahiri Mahasaya: 60 — `71bb5b6406fec1e7b59511e7957d247c3bdabc50` — saturation JA (web; resterend archief/field)
- Sri Yukteswar: 38 — `7ebad72652cf14d750c00aaa77fc25f53f2be2cd` — saturation NEE
- Neem Karoli Baba: 113 — `180bf023a0a06f7ebb0d9df762e5fe0530f59954` — saturation NEE
- Ram Dass: 57 — `799949b551564a9993d4afe15403c36e55213af2` — saturation NEE
- Ramana Maharshi: 103 — `1eb3e422c25bba5ef8ec9c72a43332e62ca227c4` — saturation NEE
- Ramakrishna: 175 — `f813a8ae17ca61a98ac0beb0dac214ad2169e9a8` — saturation JA

HARD:
- branch-STATUS zegt nog steeds: `comparison_with_internal_allowed: NEE` binnen die run;
- de blind-run zelf moet STOP blijven;
- INDIA7 mag nu buiten die run een APARTE reconciliatietaak ontwerpen, maar de frozen branch zelf niet verder laten vergelijken/mergen.

## 8. PARALLEL-SUBAGENT REGEL
Voor grote sweeps, indien executor dit ondersteunt:
- onafhankelijke corpus/source/geografie/host/foto/adversarial streams parallel;
- geen cross-seeding tijdens discovery;
- synthese/deduplicatie pas na afronding;
- saturation pas na synthese;
- als subagents falen door sessielimiet: durable checkpoints per worker/persoon verplicht, daarna hervatten zonder dubbel werk.

## 9. ARUNACHALA / TIRUVANNAMALAI — LOCKED_BY_MARK A-ANKER
Mark voelt sterk voor Arunachala/Tiruvannamalai en wil deze plek graag in de reis. Behandel als A-anker, maar route/nachten pas later optimaliseren.

Terminologie:
- Arunachala = heilige berg;
- Tiruvannamalai = stad;
- Sri Ramanasramam = Ramana-ashram aan de voet.

Yogananda-Ramana:
- bezoek Sri Ramanasramam: 29 november 1935;
- archival-film bron lokaliseert de GEFILMDE scene op een bench direct ten noorden van de Old Hall;
- NIET overclaimen dat de volledige conversatie exact op die bench plaatsvond;
- exact filmshot versus exacte locatie van gehele conversatie apart houden.

Deze exacte-site bevinding was user-driven en post-pre-external-freeze; niet retroactief onderdeel maken van de interne pre-freeze baseline.

## 10. CLUSTERLOGICA ROND ARUNACHALA
Niet automatisch Puducherry kiezen.

Regel:
1. Arunachala/Tiruvannamalai = anker.
2. Na nationale atlas/reconciliatie bepalen welk redelijk nabij gebied de hoogste concentratie AOAY + full-deep Top-X fysieke locaties heeft.
3. Dat hoogste missiedichtheidsgebied wordt tweede-clusterkandidaat.
4. Puducherry/Sri Aurobindo is gewenst en telt positief, maar alleen als totale opbrengst de verplaatsing rechtvaardigt.
5. Geen kunstmatige mega-cluster; afzonderlijke stadsclusters + corridor.

Mark wil Sri Aurobindo graag bezoeken maar accepteert dat keuzes nodig zijn.

## 11. REISCONTEXT
- 18 dec 2026 t/m 21 jan 2027, circa 34 nachten.
- Terugvlucht gepland vanaf Delhi.
- Arunachala moet dus later in totale zuid->noord-route passen.
- Reisdoel: AOAY + eigen Kriya-lijn + full-deep personen + zelfstandige pelgrimage-zwaargewichten.
- Niet backpacking; genoeg tijd voor meditatie/stilte.

## 12. REGIOVOLGORDE / HOLD
- Eerst nationale persoonslagen + externe freezes + reconciliatie.
- Daarna clusterheatmap.
- Daarna regionale sweeps.
- Eerste regioprioriteit: Tiruvannamalai/Arunachala.
- Tweede: Kolkata/Serampore.
- Geen regionale sweep starten voordat reconciliatie/heatmap-fase dit vrijgeeft.

## 13. YOGANANDA EXTERNAL UNION / PR #24
- PR #24 bevat externe multi-AI Yogananda-masteratlas; dit was benchmark-control-input.
- Niet blind als volledig geverifieerde canon behandelen.
- CCI 086-reconciliatie is de benchmarkuitkomst.
- Niet zomaar mergen als benchmark-/provenancegrenzen daardoor vervagen.

## 14. AOAY LAAG BLIJFT OPEN
- eerste full-book ronde: 1.359 occurrence-records;
- 123 genormaliseerde plaatsen;
- 30 AOAY-found-but-missing-from-repo;
- Kashmir-signaal;
- `AOAY_LOCATION_SWEEP_SATURATED: NEE`.
Later vervolgen met detectorverdieping + occurrence-verificatie; niet vergeten na persoons/reconciliatiefase.

## 15. WHAT'S NEXT VOOR INDIA7
1. Boot exact volgens root README: volledige tekstuele repo actieve werkbranch lezen.
2. Lees `governance/INDIA_SESSION_START.md` en alle daarin genoemde latest handoffs/delta's.
3. Lees dit bestand daarna opnieuw als laatste chatdelta.
4. Controleer nieuwste PR #23-comment/CCI_RESULT en recente commits; task niets dubbel.
5. Lees de 3 interne 087-freezes volledig.
6. Lees de 8 externe frozen outputs op `agent/chatgpt-top11-parallel-sweep` pas NADAT de blind-freezes bevestigd compleet zijn (dat is nu het geval).
7. Maak een aparte, duurzame reconciliatietaak: eerst Babaji + Lahiri + Sri Yukteswar omdat daarvoor zowel interne 087-freezes als externe freezes klaarstaan; directe bronverificatie van external-only/identity-conflict claims verplicht.
8. Daarna bouw/laat bouwen de interne METHOD_V2 lagen voor Neem Karoli Baba + Ram Dass, Ramana Maharshi, Ramakrishna en reconcilieer tegen hun reeds frozen externe blind outputs.
9. Houd Anandamayi bestaande brede dataset als input; niet opnieuw vanaf nul.
10. Als landelijke full-deep personen gereconcilieerd zijn: clusterheatmap -> Arunachala-regiosweep -> Kolkata/Serampore -> Mark A/B/C -> route.
11. AOAY saturation daarna/parallel waar methodisch veilig terug oppakken vóór definitieve route.

## 16. VERBODEN FOUTEN
- Niet aannemen dat CCI handmatig gestart moet worden.
- Geen duplicate CCI_TASK zonder actuele PR #23 check.
- Frozen externe branch niet achteraf besmetten/overschrijven met interne kandidaten.
- Vivekananda/Hariharananda geen exhaustieve sweep geven.
- Geen clusterkeuze vóór landelijke reconciliatie/heatmap.
- Geen exacte Yogananda-Ramana conversatieplek overclaimen.
- Geen A/B/C namens Mark voorspellen.
- Geen PDF zonder expliciete opdracht.

END HANDOFF
