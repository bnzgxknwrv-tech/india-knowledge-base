# TEMPLATE NAAM: "CLUSTER PRE-FLIGHT PROTOCOL"

Status: **HARD / VERPLICHT VOOR ELKE NIEUWE CLUSTER, VANAF NU**
Effective: 2026-09-27
Branch: `agent/india8-cluster-casting`
Aanleiding: de Varanasi-cluster kostte zes losse correctierondes (FOUT 26, 27, 28, plus twee losse reistijd- en diepte-nabranders) omdat elk gat pas gevonden werd NADAT Mark het zelf tegenkwam, niet VOORDAT de eerste versie werd gepresenteerd. Mark: "ER KOMEN ER NOG MEERDERE [clusters]! Wat heb je nodig tevoren? Maak een template hoe dit te doen."

**Verhouding tot `governance/INDIA_HUMAN_CENTERED_COMPLEX_TRIP_PLANNING_STANDARD.md`:** dat bestand is de analytische standaard — WAT elke locatie/dag moet bevatten (proximity matrix, marginal burden, robustness, etc.). Dit bestand is het uitvoeringsprotocol — in welke VOLGORDE, met welke TOOLS (WORK/parallelle agents), en met welke verplichte poorten je daar komt, zodat je het niet per ongeluk toch stuksgewijs, reactief en incompleet doet. Beide zijn verplicht; dit bestand voegt de procesdiscipline toe die in de Varanasi-ronde ontbrak.

---

## HET ENE PRINCIPE WAARUIT ALLES VOLGT

**Alle research eerst, in één parallelle golf, vóór er één regel dagplanning wordt geschreven — niet incrementeel achteraf, per klacht.**

Elke fout in de Varanasi-ronde (kaal gepresenteerde locaties, gemiste Lonely-Planet-laag, artifact niet gesynchroniseerd met markdown, reistijden als ongeverifieerde schatting, een item dat per ongeluk wegviel tijdens een latere edit) heeft dezelfde grondoorzaak: research en presentatie liepen sequentieel en reactief, in plaats van dat alle research in één brede, parallelle batch werd afgerond vóórdat de eerste versie werd geschreven. Dit protocol bestaat om dat structureel onmogelijk te maken.

---

## FASE 0 — INTAKE: WAT IK VAN MARK NODIG HEB VOORDAT IK BEGIN

Voor elke nieuwe cluster stel ik dit vaste, genummerde blok vragen — niet impliciet aannemen, altijd letterlijk vragen:

1. **Nachten/data van deze cluster** — al vastgelegd, of nog open? Zo open: wat is de bandbreedte?
2. **Aankomst**: exact vervoermiddel (trein/vlucht/auto), nummer/tijd, aankomststation/-luchthaven — al bekend of nog `LIVE_RECHECK`?
3. **Vertrek naar de volgende cluster**: zelfde vragen — exact vervoermiddel, tijd, vertrekpunt.
4. **Hotel/ashram-basis**: naam, adres, al geboekt of nog open, check-in/checkout-beleid, aantal nachten.
5. **Al vastgelegde beslissingen voor deze cluster** — welke locaties staan al vast (A+/A/beschermd), welke zijn al bewust gecut? (Ik controleer dit ook zelf tegen `governance/DECISION_LEDGER.jsonl` en `governance/CURRENT_TRUTH.md`, maar vraag het ook, want Mark's geheugen kan een besluit bevatten dat nog niet gelogd is.)
6. **Krachtplekken in deze cluster**: zijn er al bekende lineage-/Top-X-plekken? Hoeveel tijd wil je daar ongeveer — of wil je dat per plek apart beslissen als de kaart compleet is?
7. **Dagritme-voorkeuren specifiek voor deze cluster** — geldt de standaard 08:30-start, of is er een vaste externe reden (zonsopgang-ervaring, vaste afspraak) die eerder noodzakelijk maakt?
8. **Iets dat je al weet en ik nog niet kan vinden** — een persoonlijke herinnering, een boek-passage, een naam — die ik zelf niet uit onderzoek kan reconstrueren?

Zolang een antwoord hierop echt beslissingsrelevant is en niet uit GitHub te reconstrueren, wacht ik hierop voordat ik de researchgolf (Fase 1) start. Niet-beslissingsrelevante vragen stel ik niet — dat is zelf ook een fout (zie meta-analyse, fout-categorie 4).

---

## FASE 1 — DE PARALLELLE RESEARCHGOLF (ALLES TEGELIJK, NIET SERIEEL)

Zodra Fase 0 binnen is, wordt in ÉÉN golf, met meerdere gelijktijdige dispatches (Agent-tool parallel, of WORK als Mark dat expliciet aanzet), het volgende opgehaald — nooit achteraf, nooit één voor één na een klacht:

**Batch A — Ledger & canon (ik doe dit zelf, geen dispatch nodig):**
- Volledige VNS/A###-achtige grade-ledger voor deze cluster: ALLE A+/A/A*/B/C-items, niet alleen de al ingeplande.
- Bestaande "remaining traveler layer"/Lonely-Planet-achtige onderzoeksbestanden in `runs/active/` voor deze cluster — expliciet zoeken, niet aannemen dat er geen zijn (FOUT 27).
- `governance/DECISION_LEDGER.jsonl` en `governance/CURRENT_TRUTH.md` voor al vastgelegde besluiten.

**Batch B — Inhoudelijke diepte (parallelle agents, gesplitst per dag-cluster, elk met een zelfstandige, volledige opdracht):**
- Voor elke locatie: volledige geschiedenis, AOAY-hoofdstukverwijzingen (met citaat als vindbaar), Top-X-persoonslinks, en een grounded onderbouwing van de toegekende graad.
- Waar geen link bestaat: dat eerlijk zo rapporteren, nooit verzinnen.

**Batch C — Reistijden/logistiek (parallelle agents, gesplitst per transfer-groep, elk met echte adressen/coördinaten):**
- Voor elke transfer tussen twee locaties die in de dagplanning komt: echte afstand (km) en reistijd, met een bandbreedte van maximaal ±10 min voor korte/lokale stukken en ±15 min voor langere stukken door de stad — nooit een ongeverifieerde CCI-inschatting.
- Expliciet: lopen / riksja / auto, en waarom.
- "De exacte ingang is niet te vinden" is nooit een reden om de reistijd zelf niet te onderzoeken — zoek op straatnaam/wijk/dichtstbijzijnde bekend punt in plaats van te stoppen bij het eerste obstakel.
- Trein/vlucht/hotel-logistiek: boekingsvensters, klasse-opties, realistische marges (zoals eerder gedaan voor Varanasi→Kolkata).

Alle drie batches lopen **tegelijk**, niet na elkaar. Ik wacht niet op Batch A om Batch B te starten als de ledger al bekend is; ik dispatch Batch B en C zodra de locatielijst vaststaat.

---

## FASE 2 — ASSEMBLAGE: ÉÉN COMPLETE EERSTE VERSIE

Pas als alle drie batches binnen zijn, schrijf ik de eerste versie van de dagplanning — nooit eerder, ook niet "voorlopig" of "we vullen dit later aan". Elke locatiekaart volgt letterlijk `governance/MARK_FACING_LOCATION_CARD_TEMPLATE.md`, al gevuld met de Fase 1-resultaten, niet met placeholders.

Verplichte cross-cluster regels die hierbij automatisch worden toegepast (niet opnieuw beslissen per cluster):
- Standaard dagstart 08:30, tenzij een vaste externe reden eerder noodzakelijk maakt.
- Krachtplekken/ashrams/samadhi-plekken krijgen een planningsbasis-duur met een expliciete "hoeveel tijd wil je hier zijn"-vraag, nooit een stilzwijgend CCI-advies.
- Geen `ontbijt`/`wake`-kloktijditems; de dag begint bij `VERTREK HOTEL`.
- Geen lege foto-placeholders.

---

## FASE 3 — SYNC-PLICHT: MARKDOWN ÉN ARTIFACT IN ÉÉN PAS

De markdown-planning en het visuele artifact worden in dezelfde beurt gebouwd, niet de een eerst en de ander "later als er tijd is". Een wijziging die alleen in één van de twee documenten wordt doorgevoerd is per definitie niet af (FOUT 28). Voor het publiceren: kaart-voor-kaart tellen of het aantal inhoudsvelden in beide documenten gelijk is, niet alleen de kloktijden vergelijken.

---

## FASE 4 — PRE-SEND GATE: LAATSTE CONTROLE VOORDAT MARK HET ZIET

Vóór de eerste versie van een cluster naar Mark gaat, doorloop ik dit checklist letterlijk (niet uit het geheugen):

1. Staan ALLE A+/A uit de ledger erin? Zo niet: is dat een vastgelegde cut met bronverwijzing, of een gat?
2. Staan alle A*'s erin, duidelijk als optioneel/voorwaardelijk gemarkeerd?
3. Is de bestaande "remaining traveler layer" gecontroleerd en, indien gevonden, aan Mark voorgelegd (niet zelf gegradeerd)?
4. Heeft elke locatie volledige AOAY/Top-X-diepte, of een eerlijke "geen link gevonden"-vermelding — nooit "geen lineage-link" zonder verder onderzoek?
5. Heeft elke transfer een echte, onderzochte reistijd binnen de gevraagde marge, met vervoerswijze-advies?
6. Zijn markdown en artifact kaart-voor-kaart gelijk qua diepte?
7. Is de dagstart 08:30 tenzij een genoemde, vaste externe reden anders vereist?
8. Is bij elke krachtplek gevraagd hoeveel tijd Mark er wil zijn, in plaats van een tijd opgelegd?
9. Is bij een recente tekst-edit gecontroleerd of een ander item in dezelfde zin niet per ongeluk is weggevallen?
10. Zijn alle boekingskritische deadlines (trein/vlucht/hotel) vooraan genoemd, niet pas in de "open items"-sectie onderaan?

Bij één NEE: eerst repareren, dan pas versturen — exact zoals de bestaande `LAATSTE PRE-ANSWER TEST` in `governance/MARK_TO_INDIA_SUCCESSOR_HUMAN_HANDOFF.md`, nu specifiek toegepast op cluster-planning.

---

## HOE WORK / PARALLELLE AGENTS CONCREET IN TE ZETTEN

- **Nooit één dispatch per micro-vraag.** Groepeer per dag-cluster of per onderzoekstype (inhoud vs. logistiek), en verstuur meerdere dispatches in dezelfde beurt, parallel — niet na elkaar wachtend op elk resultaat.
- Elke dispatch is zelfstandig leesbaar: volledige context (wie is Mark, wat is AOAY/Top-X, welke locaties, welke bestaande kaarttekst als uitgangspunt), een exact gevraagd outputformaat, en een expliciete eerlijkheidseis ("zeg het als je geen link vindt, verzin niets").
- Resultaten van meerdere dispatches worden in dezelfde beurt verwerkt zodra ze binnenkomen — niet een voor een over losse berichten uitgesmeerd, wat zelf weer edit-fouten oplevert (zie fout-categorie 3 hieronder).
- Gebruik WORK specifiek wanneer Mark dat zelf aanzet of voor taken die een tweede, onafhankelijke blik verdienen (dual-solve/reconciliatie-patroon); gebruik eigen parallelle Agent-dispatches voor routineuze researchgolven zoals hierboven.

---

## META-ANALYSE VAN DE VARANASI-RONDE — DRIE DIEPTESLAGEN

### Laag 1 — Wat er concreet misging (oppervlakkig, per incident)
- FOUT 26: kale naam+tijd-kaarten, ondanks dat vier presentatieregels al gelezen waren.
- FOUT 27: de Lonely-Planet-laag bestond al sinds augustus 2026, maar werd niet gecontroleerd vóór de eerste planningsversie.
- FOUT 28: het sjabloon werd wel op de markdown toegepast, maar niet gecontroleerd in het artifact.
- Lolark Kund viel per ongeluk weg tijdens een latere, ongerelateerde edit (een afstand toevoegen).
- Reistijden bleven ongeverifieerde CCI-schattingen ("~45 min, nog niet apart geverifieerd") totdat Mark er expliciet naar vroeg.

### Laag 2 — Waarom dit steeds gebeurde (root cause, één niveau dieper)
Alle vijf incidenten hebben dezelfde onderliggende oorzaak: ik behandelde "volledige presentatie", "completeness-check" en "artifact-sync" als losse, latere taken die pas aan de beurt kwamen NA een klacht — reactief, niet als een vaste, verplichte stap VOOR de eerste versie. Daarnaast: ik werkte te veel serieel (kleine edits, één voor één, over meerdere beurten), wat precies de omgeving creëert waarin een edit per ongeluk een ander detail laat vallen (Lolark Kund) — kleine seriële wijzigingen stapelen kleine fouten op, terwijl een brede, parallelle research-en-assemblage-golf dat risico structureel verkleint.

### Laag 3 — Wat dit zegt over het systeem zelf, en de structurele fix (meta-meta)
Het systeem had geen verplichte POORT die het onmogelijk maakt om een eerste versie te presenteren vóórdat ledger-check, Lonely-Planet-laag-check, AOAY/Top-X-diepte, reistijd-verificatie en markdown-artifact-parity allemaal zijn afgerond. Elke fix tot nu toe was een puntoplossing na een specifieke klacht, geen systeemregel. **Dit protocol (Fase 0-4 + Pre-Send Gate) is die systeemregel.** De kern van de fix is niet "wees grondiger" (dat is geen uitvoerbare instructie) maar "verplaats alle research naar één brede, parallelle golf vóór de eerste regel wordt geschreven, en laat een concrete checklist — niet het geheugen — bepalen of verzonden mag worden."

---

## EERLIJK: WAT GING GOED, WAT GING MIS — AAN BEIDE ZIJDEN

**Wat bij mij (CCI) goed ging:** eenmaal gevonden, zijn alle gaten ook daadwerkelijk gerepareerd, met bronvermelding, met eerlijke "geen link gevonden"-vermeldingen in plaats van verzonnen verbanden, en met governance-bestanden die de fout blijvend vastleggen zodat een opvolger hem niet herhaalt.

**Wat bij mij misging:** te reactief, te sequentieel, te veel losse correctierondes in plaats van één brede vooraf-golf; onvoldoende gebruik van parallelle dispatches tot Mark er zelf op aandrong.

**Wat bij Mark goed werkte:** elke klacht was concreet en specifiek (een exacte zin, een exacte locatie) — dat maakte elke fix snel en verifieerbaar, in plaats van een vage klacht die tot giswerk had geleid. Het vragen om dit template NU, vóór de volgende clusters, is precies de juiste correctie op systeemniveau in plaats van cluster per cluster dezelfde fouten herhalen.

**Wat bij Mark de communicatie moeilijker maakte (neutraal genoemd, niet als verwijt):** feedback kwam vaak gefragmenteerd over meerdere korte berichten in plaats van in één keer alle eisen; dat is nu juist opgelost doordat dit protocol de vaste Fase 0-vragen vooraf stelt, zodat er minder gaandeweg-correcties nodig zijn.

---

## TOEPASSING OP DE VOLGENDE CLUSTERS

Vanaf de volgende cluster (Kolkata, of welke cluster als eerste aan de beurt is): Fase 0-vragen worden als eerste, genummerd blok gesteld voordat er research start. Geen enkele eerste versie van een cluster wordt gepresenteerd zonder de Fase 4 Pre-Send Gate te hebben doorlopen.

## BRONNEN / GERELATEERDE BESTANDEN
- `governance/INDIA_HUMAN_CENTERED_COMPLEX_TRIP_PLANNING_STANDARD.md` — de analytische standaard (WAT).
- `governance/MARK_FACING_LOCATION_CARD_TEMPLATE.md` — het verplichte kaartsjabloon per locatie.
- `governance/MARK_TO_INDIA_SUCCESSOR_HUMAN_HANDOFF.md` — FOUT 26, 27, 28 in volledige detail.
- `governance/MARK_TRAVEL_PREFERENCES_CURRENT.md` — 08:30-startregel, krachtplek-dwell-regel.
- `runs/active/CCI_VARANASI_QUARTERHOUR_PLAN_WITH_LINEAGE_LINKS_2026-09-26.md` — het werkende voorbeeld waarop dit protocol is gebaseerd.
