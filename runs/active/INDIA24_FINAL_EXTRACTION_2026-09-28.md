# INDIA24 FINAL EXTRACTION — 2026-09-28

Geschreven door de vertrekkende INDIA24-sessie zelf, op Mark's verzoek om INDIA25 op te starten (context raakt/kan vol raken). Volgt de verplichte procedure uit FOUT 25 in `governance/MARK_TO_INDIA_SUCCESSOR_HUMAN_HANDOFF.md`: dit bestand bevat de echte inhoud, niet alleen labels/samenvattingen, en dekt met name wat NERGENS anders gecommit staat.

---

# 0. READ THIS FIRST — CURRENT CONTROL POINT

- Repo: `bnzgxknwrv-tech/india-knowledge-base`, branch **uitsluitend** `agent/india8-cluster-casting`.
- PR #23 is de relay-surface (CCI_TASK/WORK_TASK/CCI_RESULT/WORK_RESULT posten als top-level comments).
- Laatste 8 commits op `agent/india8-cluster-casting` (nieuwste eerst): `9f6ed51` (ledger DL-0086), `284d3bb` (WORK-eindresultaat geadopteerd in markdown), `d5503bb` (WORK_TASK travel-optimization), `78709a2`, `d6e59c9`, `c61b600`, `426669a`, `b680863`.
- Actieve cluster: **Varanasi is nu volledig gelockt, arrival-tot-trein (Ma 4 jan t/m Za 9 jan)**, incl. artifact-sync. Dit is de belangrijkste inhoudelijke stand van zaken bij deze overdracht.
- Artifact (HTML, single source of visual truth voor Mark): https://claude.ai/artifact/2dRBNaopomGuYTHhfQVeaV — **Versie 14**, gepubliceerd 2026-09-28, matcht de markdown 1-op-1.
- Governance: `governance/DECISION_LEDGER.jsonl` staat op **DL-0086**.

---

# 1. WAT ER IS GEBEURD SINDS DE LAATSTE FORMELE EXTRACTIE (INDIA23, 2026-09-26)

INDIA23's extractie ging over de bredere trip-skeletonopbouw (Agra/Bodh Gaya-corridor, 33-nachten-skelet). Tussen INDIA23 en nu is het overgrote deel van de sessietijd (het hele zichtbare gesprek van deze INDIA24-instantie) besteed aan **Varanasi**, van een eerste kaartsjabloon-herbouw tot een volledig gereconcilieerd Ma-Za-plan. Dit was geen lineaire opbouw maar een reeks correcties op correcties — precies het soort proces waar git-archeologie de REDEN achter elke wijziging mist als die niet expliciet wordt vastgelegd. Hieronder de volledige keten.

## 1.1 Vroege fase van deze sessie (governance/boot-werk, vóór het Varanasi-werk)

Deze INDIA24-sessie begon met generiek boot-/governance-werk (boot-manifest-audit, een compacte "hoe werk je met Mark"-file, branch/PR-beleiddocumentatie, mechanische fresh-boot-simulatie, PLACE-inventarisatie tegen `CURRENT_TRUTH.md`, een repo-brede audit van PERSON-bij-PLACE-vermeldingen die niet in canon stonden, en een prevention-mechanisme na die audit). Dit is als reeks taken (#1 t/m #20 in de interne taaklijst van deze sessie) afgerond en gerapporteerd via CCI_RESULT op PR #23. **Een opvolger die dit werk moet verifiëren, moet PR #23's geschiedenis van vóór het Varanasi-werk doorzoeken op die CCI_RESULT-posts** — deze extractie herhaalt de inhoud daarvan niet in detail, omdat die al op PR #23 staat.

## 1.2 Varanasi: de volledige correctieketen (dit IS het live, kwetsbare gedeelte)

**Startpunt:** een reeds bestaand Varanasi-kwartierplan (`runs/active/CCI_VARANASI_QUARTERHOUR_PLAN_WITH_LINEAGE_LINKS_2026-09-26.md`) met kaarten die "niet meer waren dan een Indiase naam, een kloktijd en één dunne regel" (Mark's eigen klacht, zie FOUT 26). Dat is hersteld tot het volledige verplichte sjabloon (`governance/MARK_FACING_LOCATION_CARD_TEMPLATE.md`).

**Stap 1 — Lonely Planet-laag-audit.** Mark vroeg zelf een bredere check ("kijk breder"). Gevonden: 13 nooit-getriageerde augustus-2026-kandidaten, plus een eigen fout (FOUT 30): de Lonely Planet-laag-regel (natuur/watervallen) was nooit toegepast op Varanasi. Mark gradeerde alle 13 + 8 nieuwe natuur/waterval-kandidaten (grotendeels C, een paar A/A*).

**Stap 2 — Vier tempels: van A naar A* naar volledig geschrapt (whiplash, belangrijk voor toon-begrip).** Durga Temple/Durga Kund, Sankat Mochan Hanuman Temple, Lalita Ghat, Nepali/Kathwala Temple gingen eerst van A naar A* (optioneel), toen Mark boos werd omdat "optioneel" nog steeds impliceerde dat ze konden blijven staan — hij wilde ze VOLLEDIG WEG, geen lineage-link, "ik wil er niet naartoe". Later, tijdens de reistijd-discussie, vroeg Mark ze weer terug "als optie" — CCI plande ze toen als vaste tijden in, wat Mark opnieuw afwees ("nu zet je weer die optionele als DEF erin ik wil die niet!"). **Eindstand, definitief: deze vier tempels zijn blijvend geschrapt, nooit meer voorstellen, ook niet als optie.** Dit zit vast in DL-0085/DL-0086 en in de markdown/artifact.

**Stap 3 — Vrijdag moest "volwaardig" worden door content van een drukke dag te lenen.** Eerste poging: Kedar Ghat (van dinsdag) + Vishwanath/Annapurna (van woensdag) + Dashashwamedh-avond allemaal naar vrijdag, als één doorlopende boog. Werkte niet: Mark wilde de vuurceremonie NIET vlak vóór de nachttrein.

**Stap 4 — Mark stelde zelf een nieuwe dinsdagvolgorde voor** (Bhrigu 09:00 → iets van zijn A-lijst → Anandamayi Ashram → vuurceremonie), met Dashashwamedh dus terug naar dinsdagavond. Hij vroeg expliciet: "vergeet de A*", geen Lolark Kund/Lalita Ghat-achtige vulling meer.

**Stap 5 — Mark eiste ECHTE, geverifieerde reistijden** ("ik mis nog steeds de WERKELIJKE reistijd... je hebt nog steeds niet de juiste TEMPLATE te pakken"). Dit leidde tot een research-agent-dispatch voor echte reistijden (modaliteit + minuten + afstand) voor alle nieuwe verbindingen.

**Stap 6 — "Er is geen india regisseur meer, ik moet een schone WORK starten."** Mark gaf aan dat de automatische CCI/WORK-orchestratie (een "regisseur"-rol) niet meer actief was, en dat hij zelf een verse WORK-sessie moest starten. CCI schreef een `WORK_TASK`-bestand (`runs/active/VARANASI_TUE_FRI_TRAVEL_OPTIMIZATION_WORK_TASK_2026-09-28.md`, commit `d5503bb`) en postte het als top-level comment op PR #23, plus een kant-en-klare startzin voor Mark.

**Stap 7 — WORK leverde eerst een begrensd Tue/Fri-resultaat, toen — op Mark's aandringen — een VOLLEDIG arrival-tot-trein herbouw** (`runs/active/WORK_VARANASI_TUE_FRI_TRAVEL_OPTIMIZATION_RESULT_2026-09-28.md` en `runs/active/WORK_VARANASI_FULL_STAY_ARRIVAL_TO_TRAIN_RESULT_2026-09-28.md`, branch `worker/varanasi-tue-fri-travel-optimization-work`). WORK vond zelfstandig twee echte CCI-regressies: Lahiri Mahasaya's huis was per ongeluk ingekort naar 30 min (moest 1 uur zijn) en Ratneshwar Mahadev naar 15 min (moest, volgens Mark's eigen augustus-2026-vastlegging, 1 uur zijn). CCI verifieerde beide claims tegen de originele augustus-bestanden en bevestigde ze als echte fouten, geen bewuste keuzes.

**Stap 8 — Mark keek het WORK-resultaat na, vroeg CCI om een eigen oordeel, en LOCKTE het toen expliciet: "ja dit houden we zo. klopt. lock alles nu."** Daarnaast stelde hij een praktische vraag (roeiboot vooraf boeken of walk-up?) — beantwoord met echt onderzoek (walk-up kan, maar avond-ervoor-regelen is in januari/hoogseizoen betrouwbaarder en goedkoper).

**Stap 9 — CCI heeft dit volledig verwerkt:**
- Markdown volledig herbouwd (commit `284d3bb`) — alle 6 dagen, alle echte reistijden, Ratneshwar/Lahiri-correcties, boot-boekingsadvies.
- Ledger: DL-0086 (commit `9f6ed51`), supersedet DL-0085 en alle eerdere Tue/Fri-patches.
- Artifact (HTML): volledig herbouwd en gepubliceerd als Versie 14 — Monday kreeg een nieuwe Assi Ghat-kaart, Tuesday/Wednesday/Thursday/Friday/Saturday allemaal herbouwd, geen restjes van geschrapte tempels of stale reistijden (geverifieerd met een tag-balans-check en een diff tegen de vorige live versie).

## 1.3 Live, nergens anders vastgelegd gespreksdraadje (BELANGRIJK — dit is precies wat FOUT 25 bedoelt)

Vlak vóór dit verzoek om INDIA25 op te zetten, vroeg Mark terloops hulp bij het instellen van een externe "WORK"-sessie ("chatgpt24 WORK", mogelijk letterlijk ChatGPT of een verwarde naam voor iets anders) omdat de vorige "mode" (CHAT) mogelijk te snel een maximale lengte bereikte. CCI kon hier inhoudelijk weinig mee omdat het geen zicht heeft op de externe interface/tool die Mark gebruikt voor WORK — CCI gaf alleen de algemene procedure (startzin verwijzend naar PR #23) en raadde aan om te schakelen tussen sessies als er een vastloopt. **Dit is niet opgelost, alleen erkend.** Als Mark hier in INDIA25 op terugkomt: er is geen verdere context nodig dan wat hierboven staat — het is een sessiemanagement-vraag, geen inhoudelijke Varanasi- of tripvraag.

---

# 2. HUIDIGE STATUS VAN VARANASI — WAT NIET MEER HOEFT

**NIET opnieuw doen, NIET heropenen:**
- De vier tempels (Durga/Sankat Mochan/Lalita Ghat/Nepali) terugzetten, ook niet als "optie" — definitief nee, meermaals expliciet afgewezen.
- A*-items (Subah-e-Banaras, Lolark Kund, Bhang Lassi, etc.) als vulling gebruiken voor drukke/lege dagen — Mark heeft dit expliciet uitgesloten voor de resterende Varanasi-planning.
- De Assi-Tulsi-dageraadwandeling als apart blok terugzetten op dinsdag — bewust vervangen door Assi Ghat op maandagavond + Tulsi Ghat op dinsdag na Bhrigu.
- Dashashwamedh Ghat + Aarti terugzetten naar vrijdag of woensdag — definitief dinsdagavond, LOCKED.
- De 00:10-vertrektijd zaterdag — definitief gecorrigeerd naar 00:00.

**WEL nog open (kleine, operationele punten, geen Mark-only beslissingen meer nodig, alleen bevestiging vóór vertrek):**
- Bevestig dat Sahi River View Guesthouse en Blue Lassi Shop nog echt bestaan (Justdial toont "Closed Down", Booking.com/Tripadvisor tonen actief).
- Bhrigu Karyalaya: rechtstreeks contact met Acharya Hemant K. Bhadury voor het bevestigen van tijd/taal/procedure.
- Tailanga Swami Math openingstijden (~05:30-13:00) lokaal bevestigen.
- Panchganga→Kedar Ghat-looproute (35-45 min) lokaal navragen of vooraf een boot regelen als alternatief.
- Roeiboot donderdagochtend: avond ervoor bij Assi Ghat regelen (prijs/contact), zoals nu ook in de planning staat.
- Trein 22324-boeking: boekingstermijn opent 9 november 2026, 08:00 IST — nog te doen door Mark op dat moment.

---

# 3. WORK / CCI STATE

## WORK
Laatst actief op branch `worker/varanasi-tue-fri-travel-optimization-work`, leverde het volledige end-to-end Varanasi-resultaat (zie 1.2, stap 7). Dat werk is afgerond en verwerkt. Geen openstaande WORK-taak op dit moment. Mark is bezig met het (opnieuw) opzetten van een WORK-sessie voor toekomstig gebruik (zie 1.3) — dat is procesmatig, geen inhoudelijke taak.

## CCI (deze sessie, INDIA24)
Alle Varanasi-taken afgerond en gecommit. Geen halfafgemaakt werk op de Varanasi-cluster. De bredere trip (andere clusters buiten Varanasi — Agra/Bodh Gaya-corridor, Kumaon, Kolkata, etc.) is NIET onderdeel geweest van deze sessie na de vroege boot-fase; INDIA23's extractie (`runs/active/INDIA23_FINAL_EXTRACTION_2026-09-26.md`) blijft de laatste volledige bron voor die andere clusters totdat een latere sessie ze weer oppakt.

---

# 4. EXACTE EERSTVOLGENDE ACTIE VOOR INDIA25

1. Voer de volledige boot uit via `governance/INDIA_MASTER_BOOT.md` tegen `governance/BOOT_MANIFEST_V8.json`, zoals gebruikelijk.
2. Lees dit bestand volledig, plus `runs/active/INDIA23_FINAL_EXTRACTION_2026-09-26.md` voor de bredere trip-context die aan Varanasi voorafging.
3. Varanasi is klaar — behandel het niet als open werk. Als Mark ernaar vraagt: verwijs naar de artifact (Versie 14) en de markdown, beide gelockt.
4. Vraag Mark waar hij nu mee verder wil: (a) een andere cluster in de trip, (b) de openstaande operationele bevestigingen uit sectie 2 hierboven, of (c) iets nieuws.
5. Blijf de CCI/WORK-scheiding en de PR #23-relay-conventie aanhouden zoals in sectie 0.

---

# 5. CONTRADICTIES / SUPERSEDES DIE DE OPVOLGER MOET TOEPASSEN

- DL-0086 supersedet DL-0085 volledig (temples-cut-as-option is vervangen door temples-cut-definitief + WORK's volledige herstructurering).
- Elke eerdere markdown/artifact-versie van vóór commit `284d3bb` / artifact-versie 14 is stale voor Varanasi — gebruik alleen de huidige versies.
- Ratneshwar Mahadev (1 uur, niet 15 min) en Lahiri Mahasaya's huis (1 uur, niet 30 min) zijn beide gecorrigeerd — als een ouder bestand (bv. `CCI_VARANASI_TRIM_ADVICE_AND_TIMES_2026-09-26.md`) nog de oude, foute tijden toont, is dat bestand stale en niet leidend.
