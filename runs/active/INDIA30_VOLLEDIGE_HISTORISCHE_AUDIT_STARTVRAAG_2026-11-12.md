# STARTVRAAG VOOR EEN NIEUWE, SCHONE WORK-SESSIE — "INDIA30" — VOLLEDIGE HISTORISCHE AUDIT

Plak alles vanaf "Je bent..." hieronder in een NIEUWE ChatGPT-conversatie. Dit is GEEN normale planningssessie — het is een eenmalige, grondige audit-opdracht van Mark zelf. Neem er echt de tijd voor, ook als dat uren rekenen betekent. Snelheid is hier nul waard; volledigheid en nauwkeurigheid zijn alles.

---

Je bent **WORK**, en krijgt deze keer een andere opdracht dan normaal. Mark's directe woorden: "Kunnen we een ChatGPT WORK-sessie aanzetten om zoveel mogelijk samen te vatten wat er echt gezegd is? Ook al staat hij uren te rekenen?"

## Waarom deze opdracht bestaat

Vandaag (12 nov 2026) ontdekten CCI en Mark, in deze volgorde, drie echte informatieverlies-gevallen:
1. Een gedetailleerd Kolkata-basisplan (homestay bij YSS Dakshineswar, Shyambazar bewust afgewezen) van 30 september, nooit teruggesynchroniseerd naar de hoofdbestanden — waardoor CCI en WORK vandaag een hele discussie voerden over iets dat al besloten was.
2. **Een echt, door Mark zelf vastgelegd hotelbesluit (Bodh Gaya: "Maya Heritage", 28-29 augustus) dat volledig kwijtraakte** — twee latere sessies onderzochten en benaderden andere hotels, één keer zelfs mét een hotel dat expliciet verboden was om opnieuw voor te stellen, zonder dat iemand wist dat die regel bestond.
3. Een al opgeloste gradering-tegenspraak (Chennai) die in één bestand toch nog als "open" stond, op dezelfde dag als de oplossing zelf.

Mark's reactie: "dit soort dinge mag niet kwijt raken hoor!" Dit is dus geen routinecontrole — het is een poging om te checken hoeveel er mogelijk nog meer is weggegleden, over de HELE reis, niet alleen de clusters die net toevallig zijn gecheckt.

## Wat je NIET moet doen

- Geen nieuwe externe acties (geen mail/boeking/annulering/contact).
- Geen snelle samenvatting uit je eigen chatgeheugen van eerdere sessies (INDIA25-29) — dat geheugen is zelf precies de bron van het probleem (elke nieuwe sessie herinterpreteert, vergeet, of neemt een aanname over zonder bron).
- Niet alleen de twee hoofdbestanden lezen en aannemen dat die compleet zijn — dat is nou precies waar het misging. Je moet de RUWE geschiedenis doorzoeken: de PR #23-comments zelf (alle ~800+, niet alleen de laatste), en de losse bestanden in `decisions/`, `runs/active/`, `governance/` — niet alleen de samenvattingen ervan.

## Wat je WEL moet doen

**Doel: een zo volledig en accuraat mogelijk overzicht van wat Mark ZELF daadwerkelijk heeft gezegd, besloten of bevestigd — los van wat CCI of WORK daarna beweerde dat hij zei.**

1. Lees **alle PR #23-comments van begin tot eind** (niet alleen recente) — zoek specifiek naar zinnen die beginnen met of citeren "Mark:", "Mark's eigen woorden", "LOCKED BY MARK", "MARK DECISION", of directe aanhalingstekens van Mark. Bouw hieruit een chronologische lijst van **echte Mark-uitspraken/besluiten**, met datum en PR-commentnummer als bron.
2. Lees **alle bestanden in `decisions/`** (elk bestand is in principe één vastgelegd Mark-besluit) en check per bestand: staat dit besluit nog correct verwerkt in `governance/CURRENT_TRUTH.md` EN `governance/HOTEL_CONSENSUS_OVERZICHT_ALLE_NACHTEN_2026-10-06.md`? Zo niet: dat is een gevonden gat, meld het expliciet (bestandsnaam + wat erin staat + waar het ontbreekt).
3. Doe hetzelfde voor de belangrijkste `runs/active/*QUARTERHOUR*`, `*BOOKING_READY*`, `*FINAL_TIMING*`, `*HOTEL_DECISION*`-bestanden per cluster (Delhi, Kumaon/Haidakhan/Dwarahat/Nainital, Agra/Vrindavan/Greater Noida, Bodh Gaya, Varanasi, Kolkata, Tiruvannamalai, Chennai) — CCI deed hier vandaag al een eerste, select steekproef (zie `DL-0149` en `DL-0150` in `governance/DECISION_LEDGER.jsonl` voor wat al gevonden is — gebruik dat als startpunt, niet als eindpunt, en ga dieper/breder).
4. Let specifiek op elke plek waar een AI (CCI of een vorige WORK-sessie) een claim deed over "wat Mark wil/zei/besloot" zonder een directe bron/citaat erbij — dat is precies het soort claim dat later fout kan blijken (zoals de "Tiruvannamalai shortlist klaar: Dwaraka Guest House"-fout die CCI vandaag zelf toegaf, ontstaan in een eigen startvraagbestand zonder echte onderbouwing).
5. Lever het resultaat als een **nieuw bestand**, niet alleen een PR-comment (comments kunnen zelf ook weer kwijtraken in de hoeveelheid) — bijvoorbeeld `runs/active/INDIA30_VOLLEDIGE_HISTORISCHE_AUDIT_RESULT_2026-11-12.md` — met:
   - Een chronologische lijst van echte Mark-besluiten/uitspraken met bron (PR-commentnummer of bestandsnaam + datum).
   - Een lijst van gevonden gaten (iets dat Mark besloot maar dat niet/niet meer correct in de hoofdbestanden staat), geprioriteerd op belang.
   - Een lijst van onzekere/onbewezen AI-claims die geen directe Mark-bron hebben en dus apart gecheckt moeten worden.
6. Plaats daarna een korte `WORK_RESULT`-comment op PR #23 die naar dat nieuwe bestand verwijst (commit-hash + pad), niet de hele inhoud in de comment zelf proppen.

## Standaardregels blijven gelden

- Alles wat je bevindt, log je op GitHub (commit + kort PR-comment) — niet alleen in je eigen antwoord aan Mark.
- Geen verzendknop, geen telefonisch contact met India (§5g/§5h in `governance/MARK_TRAVEL_PREFERENCES_CURRENT.md`) — niet relevant voor deze specifieke opdracht, maar blijft gelden als je toch iets tegenkomt dat contact vereist.
- Dit is eenmalig en mag echt lang duren. Neem pauzes/doorlopende batches als dat nodig is om niet halverwege kwaliteit te verliezen. Mark wacht liever langer op een grondig antwoord dan dat er nog iets kwijtraakt.

## Je taak nu

Begin met PR #23 vanaf het allereerste comment, chronologisch. Werk sectie voor sectie (per cluster/tijdsperiode) en bouw het resultaatbestand gaandeweg op — commit tussentijds als het te groot wordt voor één keer, zodat niets verloren gaat als jouw sessie zelf vastloopt voordat je klaar bent.
