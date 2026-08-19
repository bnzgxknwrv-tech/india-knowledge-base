# HANDOFF INDIA6 -> INDIA7

Datum: 2026-08-19
Status: DURABLE SUCCESSOR HANDOFF
Repo: `bnzgxknwrv-tech/india-knowledge-base`
Actieve CCI-werkbranch: `claude/werk-je-nu-of-niet-oa10y7`
PR relay: #23

## 1. ROLCONTINUITEIT
- INDIA7 is de directe functionele opvolger van INDIA6 en daarmee van INDIA2.
- INDIA3/INDIA4/INDIA5 waren experimentele/mislukte architecturen en zijn geen inhoudelijke rolvoorgangers.
- Mark bepaalt doelen, voorkeuren en A/B/C-keuzes.
- ChatGPT/INDIA is regisseur, onafhankelijke bronredenering/synthese, CCI-tasking en QA.
- CCI = Claude Code India, uitvoerende research/GitHub-engine.
- Losse externe AI-runs zijn onafhankelijke detectorlagen, niet de waarheid zonder bronverificatie.

## 2. WERKSTIJL DIE BEWAARD MOET BLIJVEN
- Handel eerst, praat daarna.
- Als iets moet gebeuren: dezelfde beurt uitvoeren met tools of exact uitvoerbare actie geven.
- Na iedere afgeronde stap altijd direct bepalen wat de volgende stap is.
- Korte, directe antwoorden; technische details alleen wanneer nodig/gevraagd.
- Geen passieve TODO-lijsten zonder concrete vervolgstap.
- Tekst die Mark naar een andere AI moet kopieren moet volledig in een eigen fenced code block staan.
- Geen PDF tenzij Mark expliciet vraagt.
- Geen oude beslissingen heropenen zonder nieuwe cruciale informatie.

## 3. HUIDIGE HOOFDARCHITECTUUR
Strategische volgorde is LOCKED:
`LANDELIJKE PERSONEN-SWEEPS -> CLUSTERHEATMAP -> REGIONALE CLUSTERSWEEPS -> MARK A/B/C -> ROUTE`

METHOD_V2:
`CORPUS INVENTORY -> LOSSLESS CORPUS OCCURRENCE EXTRACTION -> EVENT/PLACE NORMALIZATION -> HOST/NETWORK GRAPH -> WEB DISCOVERY -> INDIA INDEPENDENT METHOD PASS -> EXTERNAL MULTI-AI ADVERSARIAL UNION -> DIRECT VERIFICATION/RECONCILIATION -> SATURATION`

Yogananda prospectieve benchmark heeft bewezen dat geen enkele laag alleen voldoende is:
- externe multi-AI union leverde echte externe misses;
- 8/8 rechtstreeks getoetste externe kandidaten bleken waar;
- CCI vond zelf de Regent Hotel, Bombay, die alle vijf externe AI's misten.
Verdict: `EXTERNAL_MULTI_AI_MANDATORY_FOR_REMAINING_TOP11: JA` voor personen die full-deep worden uitgevoerd.

## 4. SWEEPDIEPTE PER PERSOON — MARK BESLUIT
Volledige landelijke METHOD_V2 deep sweep:
1. Paramahansa Yogananda
2. Mahavatar Babaji (reeds in lopende 087-scope)
3. Lahiri Mahasaya
4. Sri Yukteswar
5. Neem Karoli Baba
6. Ram Dass
7. Ramana Maharshi
8. Ramakrishna

Anandamayi Ma:
- reeds uitzonderlijk breed onderzocht via source-first + externe union + reconciliatie;
- niet opnieuw vanaf nul.

Targeted-only, GEEN exhaustieve landelijke sweep:
- Vivekananda: alleen grootste/belangrijkste fysieke locaties.
- Hariharananda: alleen grootste/belangrijkste fysieke locaties.

Ramakrishna is door Mark expliciet full-deep gemaakt omdat hij ondervertegenwoordigd is. Mark zou graag minstens iets wezenlijks van Ramakrishna bezoeken als dit logisch in de route past; geen geforceerde dramatische omweg indien het niet past.

## 5. CCI ACTUELE TAAK / MAX-CONTEXT RECOVERY
- CCI_TASK 087 = Babaji + Lahiri Mahasaya + Sri Yukteswar, landelijke METHOD_V2 pre-external freeze.
- Claude Code liep tegen max-context/tokens.
- CCI_TASK 087R is daarom op PR #23 geplaatst als recovery/resume, NIET opnieuw beginnen.
- 087R moet reeds gecommitte checkpoints lezen, alleen onafgemaakte werkpakketten hervatten, parallel werken waar mogelijk en per afgerond pakket/persona committen.
- Op moment van deze handoff is nog geen `CCI_RESULT 087R` gezien.
- INDIA7 moet PR #23 op een nieuwer resultaat controleren voordat het iets nieuws taskt.

## 6. BELANGRIJK: GITHUB COMMENT WEKT CCI AUTOMATISCH
Mark heeft daadwerkelijk een Claude Code wake-event laten zien:
`<wake reason="external-event">` met `source="github"`, `kind="issue_comment.created"` voor CCI_TASK 087R.

Daarmee geldt voortaan operationeel:
- een nieuwe CCI_TASK als GitHub PR-comment triggert/waket CCI automatisch;
- Mark hoeft CCI normaal NIET handmatig te starten;
- zet geen duplicate recovery-task neer alleen omdat een resultaat nog niet direct terug is;
- wacht op CCI_RESULT / controleer actuele GitHub-state;
- alleen bij aantoonbare trigger-failure escaleren.

## 7. PARALLELLE ONAFHANKELIJKE CHATGPT-SWEEP
Er is een aparte branch aangemaakt voor een onafhankelijke externe ChatGPT-run:
`agent/chatgpt-top11-parallel-sweep`

Taakbestand:
`runs/active/TOP11-PARALLEL-CHATGPT-SWEEP-001/TASK.md`

Deze run omvat dezelfde acht full-deep lijnen/personen:
Yogananda, Babaji, Lahiri, Sri Yukteswar, Neem Karoli Baba, Ram Dass, Ramana Maharshi, Ramakrishna.

HARD blind-protocol:
- voor alle PRE-COMPARE freezes alleen TASK.md + STATUS.md lezen;
- GEEN root README/governance/interne persoonsatlassen/CCI-resultaten/PR #24/METHOD_V1/Anandamayi-union voordat alle eigen freezes klaar zijn;
- openbare internetbronnen wel gebruiken;
- per persoon onafhankelijk werken;
- waar omgeving subagents/workers ondersteunt: acht personen parallel, en binnen persoon bronfamilies/hosts/reizen/foto's/adversarial miss-finding verder paralleliseren;
- per persoon direct committen op eigen branch;
- na alle acht: NIET vergelijken met interne data; stop voor latere INDIA-reconciliatie.

Belangrijk: aparte branch voorkomt write-conflicten met CCI en bewaart onafhankelijke discovery.

## 8. PARALLEL-SUBAGENT REGEL
Voor grote research-sweeps, indien executor dit ondersteunt:
- onafhankelijke corpus/source/geografie/host/foto/adversarial streams parallel uitvoeren;
- geen cross-seeding tussen workers tijdens discovery;
- pas na afronding synthese/deduplicatie;
- saturation pas na synthese;
- als subagents niet beschikbaar zijn, aparte onafhankelijke passes emuleren zonder correctness te verlagen.

## 9. ARUNACHALA / TIRUVANNAMALAI — MARK-PREFERENTIE EN ROUTELOGICA
Mark voelt sterk voor Arunachala/Tiruvannamalai en wil deze plek graag in de reis. Behandel als A-anker/kandidaat dat later nog tegen totale tijd/route wordt getoetst.

Correcte geografische termen:
- Arunachala = heilige berg;
- Tiruvannamalai = stad;
- Sri Ramanasramam = Ramana-ashram aan de voet van Arunachala.

Yogananda-Ramana:
- Yogananda bezocht Sri Ramanasramam op 29 november 1935.
- Sterkste huidige directe publieke aanwijzing: archival-films bron plaatst de GEFILMDE scene met Ramana op een bench direct ten noorden van de Old Hall.
- NIET zonder extra broncheck beweren dat de volledige gesproken ontmoeting/conversatie exact op die bench plaatsvond. Onderscheid: exact filmshot versus exacte locatie van gehele conversatie.
- Dit exacte-site-vraagstuk is voor Mark keuze-relevant en verdient directe bronverificatie zodra benchmarkpuriteit dit toelaat.

Deze bevinding ontstond na de Yogananda pre-external freeze door een user-driven vraag. Niet retroactief als pre-freeze interne vondst behandelen.

## 10. CLUSTERLOGICA ROND ARUNACHALA
Mark wil NIET automatisch Puducherry/Sri Aurobindo als tweede stop alleen omdat het dichtbij ligt.

Regel:
1. Arunachala/Tiruvannamalai eerst als anker.
2. Daarna op basis van de landelijke atlas bepalen welk REDELIJK NABIJ gebied de grootste concentratie heeft van AOAY + full-deep Top-X fysieke locaties.
3. Dat hoogste missiedichtheidscluster is kandidaat voor tweede cluster.
4. Puducherry/Sri Aurobindo is gewenst en krijgt positieve waarde, maar alleen kiezen als totale spirituele/AOAY/Top-X-opbrengst de verplaatsing rechtvaardigt.
5. Geen kunstmatige mega-cluster maken; Tiruvannamalai lokaal compact behandelen en andere steden als aangrenzende clusters/corridor.

Mark wil Sri Aurobindo graag bezoeken, maar accepteert dat keuzes nodig zijn.

## 11. REISCONTEXT DIE BIJ DE CLUSTERKEUZE MEE MOET
- Reis: 18 dec 2026 t/m 21 jan 2027, circa 34 nachten.
- Terugvlucht staat gepland vanaf Delhi.
- Arunachala moet dus later in totale zuid->noord-route en beschikbare tijd worden gepast; nog geen nachten vastzetten.
- Reisdoel: AOAY + eigen Kriya-lijn + full-deep personen + zelfstandige pelgrimage-zwaargewichten.
- Niet backpacking; genoeg tijd voor meditatie/stilte.

## 12. REGIOVOLGORDE / HOLD
- Eerst landelijke personenlaag afmaken.
- Daarna clusterheatmap.
- Daarna regionale sweeps.
- Tiruvannamalai/Arunachala is de eerste regioprioriteit zodra landelijke laag/QA dit vrijgeeft.
- Kolkata/Serampore daarna.
- Geen Arunachala-regiosweep starten terwijl de huidige personenlaag/freeze-workflow nog loopt.

## 13. YOGANANDA EXTERNAL UNION / PR #24
- PR #24 bevat externe multi-AI Yogananda-masteratlas op aparte branch.
- Deze versie was benchmark-control-input; niet blind als geverifieerde canon behandelen.
- Benchmark/reconciliatie-output staat op CCI-werkbranch en verdict is reeds JA voor verplichte externe AI-laag.
- PR #24 niet zomaar mergen als daardoor benchmark-/provenancegrenzen vervagen; eerst huidige repo-state en eventuele latere besluiten controleren.

## 14. AOAY LAAG BLIJFT OPEN
- AOAY full-book eerste ronde: 1.359 occurrence-records, 123 genormaliseerde plaatsen, 30 repo-misses, Kashmir-signaal.
- Saturation = NEE.
- AOAY vervolgronde blijft later nodig; niet vergeten na de persoons-sweeps.

## 15. WHAT'S NEXT VOOR INDIA7
Bij nieuwe start:
1. Lees conform root README de gehele tekstuele repo op actieve werkbranch.
2. Lees dit handoff-bestand daarna opnieuw.
3. Inventariseer PR #23, PR #24 en branch `agent/chatgpt-top11-parallel-sweep`.
4. Controleer of CCI_RESULT 087R inmiddels bestaat en welke 087 freezes/checkpoints klaar zijn.
5. Controleer STATUS van de parallelle ChatGPT-sweepbranch.
6. Task NIETS dubbel.
7. Houd de twee discovery-lagen blind/gescheiden tot hun freezes compleet zijn.
8. Na de drie 087 interne freezes: organiseer de verplichte externe adversarial sweeps/reconciliatie voor Babaji/Lahiri/Sri Yukteswar zonder de parallelle blind-run voortijdig te besmetten.
9. Daarna full-deep: Neem Karoli Baba + Ram Dass, Ramana Maharshi, Ramakrishna.
10. Pas na landelijke personenlaag: clusterheatmap -> Arunachala-regiosweep -> overige regio's -> Mark A/B/C -> route.

## 16. VERBODEN FOUTEN VOOR OPVOLGER
- Niet aannemen dat CCI handmatig gestart moet worden; GitHub comment is aangetoond wake-signaal.
- Geen duplicate CCI_TASK plaatsen zonder actuele PR #23-state te controleren.
- Geen parallelle ChatGPT-blind-run besmetten met interne kandidaten.
- Geen Vivekananda/Hariharananda exhaustive sweep starten.
- Geen clusterkeuze vóór landelijke heatmap.
- Geen exacte Yogananda-Ramana conversatieplek overclaimen; filmbench is exact voor filmshot, niet automatisch voor hele conversatie.
- Geen A/B/C namens Mark voorspellen.
- Geen PDF zonder expliciete opdracht.

END HANDOFF
