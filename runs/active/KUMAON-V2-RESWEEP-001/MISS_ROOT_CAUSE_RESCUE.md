# MISS ROOT-CAUSE + RESCUE — KUMAON-V2-RESWEEP-001

```
task_id: KUMAON-V2-RESWEEP-001
uitgevoerd_door: CCI
uitgevoerd_op: 2026-08-15
trigger: CCI_TASK 078 (INDIA, PR #23) — QA-bevinding uit RECONCILIATION.md
```

## SAMENVATTING

Twee legacy-`LOCKED_A`-locaties (Turiya Niwas #36, Bodh Ashram #37) werden door zowel CCI Sweep A
als INDIA Sweep B gemist. Root cause voor beide geïdentificeerd en bevestigd via herverificatie.
Gerichte rescue-audit op alle 16 Kumaon-`LOCKED_A`-locaties uitgevoerd: **2 aanvullende, lagere-
ernst misses gevonden** (Babaji Smriti Bhavan, Crank's Ridge) — geen andere hoge-ernst misses.
Beide bevestigde misses opnieuw geverifieerd, geen identiteitsconflict met het bestaande
Mark-A-besluit. Permanente nummers 080/081 toegekend. Protocol minimaal gepatcht
(`governance/SWEEP_PROTOCOL.md`, poort E.1, twee gerichte toevoegingen).

## RESCUE-AUDIT — ALLE 16 KUMAON-LOCKED_A-LOCATIES

| # | Legacy-locatie | Sweep A (CCI) | Sweep B (INDIA) | Ernst |
|---|---|---|---|---|
| 15 | Babaji Cave | ✅ KUM-SWEEP-A-001 | ✅ KB2-001 | — (nu 079) |
| 16 | Babaji Smriti Bhavan | ❌ | ❌ | LAAG — sub-schrijn binnen de wél gevonden grotcluster (079); geen los zoekgat |
| 17 | Dunagiri Tempel | ❌ | ✅ KB2-044 | — |
| 18 | YSS Dwarahat Ashram | ❌ | ✅ KB2-004 | — |
| 19 | Kainchi Dham | ✅ KUM-SWEEP-A-002 | ✅ KB2-008 | — |
| 20 | Kasar Devi | ✅ KUM-SWEEP-A-003 | ✅ KB2-033 | — |
| 21 | Crank's Ridge | ❌ | ❌ | LAAG — dit is de heuvelrug/het gebied waarin Kasar Devi (wél gevonden) ligt, geen los puntobject |
| 22 | Kakrighat | ❌ | ✅ KB2-022 | — |
| 23 | Jageshwar | ✅ KUM-SWEEP-A-007 | ✅ KB2-043 | — |
| 24 | Hanuman Garhi | ❌ | ✅ KB2-010 | — |
| 29 | Ramakrishna Kutir | gedetecteerd, bewust OUT_OF_SCOPE gehouden | ✅ KB2-025 | — (bewuste keuze Sweep A, geen miss) |
| 30 | Chitai Golu Devta | ❌ | ✅ KB2-045 | — |
| 36 | **Turiya Niwas** | ❌ | ❌ | **HOOG — zie root cause** |
| 37 | **Bodh Ashram** | ❌ | ❌ | **HOOG — zie root cause, dubbele Top-11-link** |
| 46 | Haidakhan Vishwa Mahadham | ✅ KUM-SWEEP-A-005 | ✅ KB2-041 | — |
| 27 | Bhumiyadhar | ❌ | ✅ KB2-009 (als "Bhumiadhar") | — |

**Antwoord op de kernvraag ("precies deze twee, of meer?")**: er zijn in totaal 4 nominale misses
(16, 21, 36, 37), maar slechts 2 daarvan (36, 37) zijn echte, hoge-ernst blinde vlekken — losse,
zelfstandige fysieke locaties met eigen Top-11-/historische betekenis die door geen van beide
sweeps ontdekt werden. De andere 2 (16, 21) zijn geen zelfstandige zoekgaten: ze zijn sub-
onderdelen van een cluster (de Babaji-grot resp. Kasar Devi) dat wél gevonden werd, alleen niet
apart benoemd. Geen actie nodig voor 16/21 buiten het al bestaande cluster-nummer; wel voor 36/37.

## ROOT_CAUSE_BODH_ASHRAM

**Classificatie: onvoldoende bezoek-/host-/landgoedketen (primair), bron-indexeringsprobleem
(secundair voor Sweep B).**

Herverificatie (WebSearch, 2026-08-15) bevestigt de legacy-claim volledig: Bodh Ashram was
oorspronkelijk het landgoed van W.Y. Evans-Wentz (Tibetaans-boeddhistisch geleerde), later
bewoond door Lama Anagarika Govinda en zijn vrouw Li Gotami, op Crank's Ridge nabij de Kasar
Devi-tempel. **Zowel Anandamayi Ma als Neem Karoli Baba bezochten Lama Govinda hier** — een
directe, dubbele Top-11-fysieke-link, exact zoals legacy meldde.

**Waarom Sweep A (CCI) het miste**: mijn zoekstrategie voor Anandamayi Ma en Neem Karoli Baba
zocht naar hun EIGEN ashrams/instellingen (Patal Devi, Dhaulchina, Kainchi Dham) — niet naar
plekken waar zij als GAST bij een derde (niet-Top-11) persoon verbleven. Lama Govinda en
Evans-Wentz kwamen in geen van mijn zoektermen voor omdat mijn detectorlogica uitsluitend
vanuit de Top-11-namen zelf zocht, niet vanuit regionaal bekende landgoederen/gastheren.

**Waarom Sweep B (INDIA) het miste**: ondanks een aanzienlijk dichter Anandamayi Ma-cluster (7
locaties, waaronder Mirtola — een vergelijkbare "bezoek bij een ander"-locatie die wél gevonden
werd) miste ook Sweep B Bodh Ashram specifiek. Waarschijnlijke oorzaak: sterke afhankelijkheid
van anandamayi.org als hoofdbron, dat een kort, niet per se compleet bezoekoverzicht geeft;
Lama Govinda/Evans-Wentz-materiaal leeft vooral in Tibet-boeddhisme-/Beat-generation-historische
bronnen (bijv. Crank's Ridge-geschiedenisartikelen), een andere bronfamilie dan Sweep B primair
raadpleegde voor deze naam. Dit is dus een MENGVORM: bron-indexeringsprobleem gecombineerd met
dezelfde onderliggende te-nauwe-persoonsdetector-oorzaak als bij Sweep A.

**Identiteit vs. gebeurtenisbewijs, apart**: `gebeurtenis_geverifieerd` (Anandamayi Ma + Neem
Karoli Baba bezochten Lama Govinda op dit landgoed): JA, dubbel bronmatig bevestigd (Wikipedia
Crank's Ridge-artikel + onafhankelijke Kasar Devi-geschiedenisbron). `exacte_fysieke_locatie_
geverifieerd`: JA voor de algemene ligging (Crank's Ridge, bij Kasar Devi-tempel, huidig een
boeddhistisch centrum aangesloten bij de Drikung Kagyu-orde); geen exact GPS-punt geverifieerd.

## ROOT_CAUSE_TURIYA

**Classificatie: protocolgat + te veel focus op huidige/officiële ashrams/tempels.**

Turiya Niwas heeft GEEN Top-11-link (Alfred "Sunyata" Sorensen is geen Top-11-figuur) — zijn
A-status komt uitsluitend uit zelfstandige, laag-3-achtige historische/culturele zwaarte
(kluizenaarswoning, kern van de Crank's Ridge-spirituele-zoekersgeschiedenis) plus zijn rol als
cluster-anchor. Omdat geen van beide sweeps' laag-3-zoekstrategie verder ging dan formele
tempels/complexen (Jageshwar, Patal Bhuvaneshwar, Haidakhan), viel een informeel, niet-
institutioneel woonhuis buiten beide zoekvensters — niet toevallig, maar een structureel gat in
hoe laag-3 werd geïnterpreteerd.

Legacy-identiteit (reeds grondig gedocumenteerd, `CLUSTER_ANCHORS.md`, onderzoek 9 juli 2026, host-
bevestigd via Facebook/WhatsApp) blijft ongewijzigd en wordt hier niet opnieuw bevraagd — geen
nieuw tegenbewijs gevonden, geen identiteitsconflict.

## PROTOCOL_PATCH: JA

Twee gerichte, minimale toevoegingen aan `governance/SWEEP_PROTOCOL.md` poort E.1 (geen
overarchitectuur, geen nieuwe poort):

1. **Laag 2 (Top-11)**: expliciete eis om ook host-/gastheer-/landgoedketens mee te zoeken —
   niet alleen de eigen instellingen van een Top-11-naam, ook waar die persoon als gast verbleef.
2. **Laag 3**: expliciete bevestiging dat informele, niet-institutionele historische
   verblijfplaatsen (woonhuis/kluizenaarsverblijf van een regionaal bekende niet-Top-11-figuur)
   evengoed MARK_WAARDIG kunnen zijn — "geen tempel/complex" is geen reden om over te slaan.

Beide toevoegingen citeren dit incident als precedent, conform de bestaande stijl van het
protocol (zie eerdere berichtverwijzingen bij poort E/N).

## RESCUE — PERMANENTE TOEKENNING

Beide locaties opnieuw geverifieerd, geen Mark-conflict (bestaand Mark-A-besluit blijft
onaangetast, alleen bevestigd), dus zelfde bar gehaald als de Babaji-grot (079):

- **080 — Turiya Niwas** (Crank's Ridge, Kasar Devi, Almora-district). A, LOCKED_BY_MARK
  (legacy-precedent, `LOCKED_A.md` #36). Laag 3 (historische kluizenaarswoning, geen Top-11-link).
  Bron: legacy `CLUSTER_ANCHORS.md` (host-geverifieerd 9 juli 2026); geen nieuw tegenbewijs.
- **081 — Bodh Ashram** (voormalig landgoed Evans-Wentz/Lama Govinda, Crank's Ridge, Almora-
  district). A, LOCKED_BY_MARK (legacy-precedent, `LOCKED_A.md` #37). Top-11 (Anandamayi Ma,
  Neem Karoli Baba) — dubbele link, herverifieerd 2026-08-15 (Wikipedia Crank's Ridge + Kasar
  Devi-geschiedenisbronnen). Coördinaten nog open, zelfde status als 079/080.

## NIET GEDAAN (conform opdracht)

Geen PDF. Geen nieuwe Mark-vragen. Geen heropening van bestaande C-besluiten (Mirtola, Binsar,
Patal Bhuvaneshwar, Dhaulchina blijven C — geen nieuw bewijs dat die besluiten zelf ter discussie
stelt).

## EINDANTWOORD (kort formaat)

```
ROOT_CAUSE_BODH_ASHRAM: onvoldoende host-/landgoedketen-zoeklogica (Sweep A) + bron-indexering
  te smal (Sweep B) -- beide zochten vanuit Top-11-namen naar EIGEN instellingen, niet naar
  landgoederen waar zij als gast verbleven
ROOT_CAUSE_TURIYA: protocolgat -- laag-3-discovery beperkte zich tot formele tempels/complexen,
  geen Top-11-link dus niet via die route gevonden
LEGACY_A_RESCUE: 14/16 gevonden (2 laag-ernst sub-locatiemisses (16,21) + 2 hoog-ernst misses
  (36,37) nu gerescued -> effectief 2/2 hoge-ernst misses hersteld)
PROTOCOL_PATCH: ja -- governance/SWEEP_PROTOCOL.md poort E.1, twee gerichte toevoegingen
  (host-/landgoedketen bij Top-11-zoeken; informele historische verblijfplaatsen bij laag 3)
NEXT_ACTION: coordinaten voor 079/080/081 verifieren; resterende Sweep-B-tijdelijke kandidaten
  (Vivekananda-circuit e.a.) krijgen identity-check tegen legacy voor eigen permanente nummers
```

---
Geschreven door: CCI. Twee permanente nummers toegekend (080, 081), beide A/LOCKED_BY_MARK op
basis van bestaand legacy-Mark-besluit, geen nieuwe Mark-vraag. Geen PDF. `PDF_STATUS: VERBODEN`
gerespecteerd.
