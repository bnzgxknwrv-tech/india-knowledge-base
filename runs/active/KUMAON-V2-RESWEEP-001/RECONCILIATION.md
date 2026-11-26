# RECONCILIATION — KUMAON-V2-RESWEEP-001 (poort R)

```
task_id: KUMAON-V2-RESWEEP-001
uitgevoerd_door: CCI
uitgevoerd_op: 2026-08-14
inputs:
  - eigen Sweep A: runs/active/KUMAON-V2-RESWEEP-001/RESULT.md (8 temp-ID's, KUM-SWEEP-A-001..008)
  - INDIA Sweep B: runs/active/KUMAON-V2-RESWEEP-001/INDIA_SWEEP_B.md op branch
    india/kumaon-v2-sweep-b-001, freeze-commit 41bd4a7caebe83e44b9ee2470ecf1212d5111d9e
    (45 temp-ID's, KB2-001..045)
  - legacy: branch controller/kumaon-complete-001-ready-for-zilver-20260719
    (KUMAON_CANDIDATES.md, CLUSTER_LOCATIONS.md #1-46, LOCKED_A/B/C.md,
    places/PLACE-0001-babaji-cave-dunagiri.md, decisions/DECISION-0001,
    DECISION-0002, DECISION-0013)
  - deep-research audit: research/deep-research/MAHAVATAR-BABAJI-CAVE-A.md +
    KUMAON-DEEP-RESEARCH-STATE.md (behandeld als extra gatendetector, geen
    zelfstandige bron -- elke claim daaruit hieronder apart geverifieerd)
```

## LEESVOLGORDE ZOALS UITGEVOERD

Eigen Sweep A geopend -> frozen Sweep B geopend en vergeleken met Sweep A -> pas daarna legacy
KUMAON-COMPLETE-001 geopend als benchmark, conform de voorgeschreven volgorde in bericht 077 en
`KUMAON-DEEP-RESEARCH-STATE.md`.

## KERNRESULTAAT — MAHAVATAR BABAJI-GROT, DEFINITIEF GERECONCILIEERD

**Drie onafhankelijke processen identificeren dezelfde fysieke plek:**

| Bron | ID | Omschrijving |
|---|---|---|
| CCI Sweep A | `KUM-SWEEP-A-001` | Grot op Dunagiri-berg, Kukuchina, nabij Dwarahat/Ranikhet |
| INDIA Sweep B | `KB2-001` | Mahavatar Babaji's Cave, Pandukholi/Kukuchina, ~25 km van Dwarahat |
| Legacy (2026-06/07) | `#15` / `PLACE-0001` | Grot op Dunagiri-berg boven Kukuchina, ~25 km van Dwarahat |

Alle drie citeren dezelfde kernbron (AOAY hoofdstuk 34, Lahiri Mahasaya's initiatie door Babaji in
1861) en dezelfde moderne identificatie via de Yogoda Satsanga Society (Babaji Smriti Bhavan op de
inwijdingsplek). Dit is geen toevallige overeenkomst maar drievoudige onafhankelijke bevestiging.

**Mark-besluit, dubbel bevestigd:**
- **Legacy** (`LOCKED_A.md #15`, vóór vandaag): al A, zonder enige aanleiding vanuit dit gesprek.
- **Vandaag**, rechtstreeks in chat, buiten protocol-volgorde: “Ik weet het. Die grot is bijna
  reden 1 voor me om naar India te gaan. A dus.”

Twee onafhankelijke Mark-beslissingen, dezelfde uitkomst. Geen `MARK_BESLUIT_CONFLICT` —
maximale consistentie.

**Permanent nummer**: `079` (volgend op Bodh Gaya's laatste nummer 078 in de huidige,
geldende globale nummering van dit project). Legacy's eigen nummering (`CLUSTER_LOCATIONS.md`
#1-46, sequentieel binnen die eerdere projectopzet) en de nooit-toegepaste
`LOCATION_ID`-clusterblokken uit `DECISION-0013` (300-399/400-499 voor latere clusters) zijn twee
ANDERE, onderling incompatibele schema's uit een eerdere architectuur van dit project en worden
niet hergebruikt — 079 volgt de huidige, doorlopende globale nummering.

**Correctie op een aanname uit `research/deep-research/MAHAVATAR-BABAJI-CAVE-A.md`**: het
vermoeden “LOCATION_ID 400” was een redelijke, met reden onderbouwde gok (Kumaon zou na Braj
(200-299) logisch in het 300-399- of 400-499-blok vallen volgens `DECISION-0013`), maar dat
schema is voor Kumaon in de legacy-run NOOIT daadwerkelijk toegepast — `PLACE-0001` heeft geen
`LOCATION_ID`-veld ingevuld gekregen (de run stopte vóór de GOUD/geo-fase). Niet overgenomen als
feit.

**Coördinaten**: nog open. Legacy `PLACE-0001` had `coordinates: ""` (nooit ingevuld, run bereikte
de GOUD-fase niet). Noch Sweep A noch Sweep B leverde exacte WGS84-coördinaten. Dit is de
concrete `NEXT_ALLOWED_STEP` voor deze locatie, niet een blocker voor de A-status zelf.

**Identiteitsdiscipline bevestigd, geen wijziging nodig**: alle drie processen houden onafhankelijk
van elkaar de Babaji-grot gescheiden van Babaji Smriti Bhavan (de schrijn, niet de grot zelf),
Dunagiri Tempel (aparte Shakti/Durga-tempel), en Haidakhan Vishwa Mahadham (aparte, levende
traditie, waarvan de Babaji-identificatie expliciet als traditieclaim behandeld wordt, niet als
feit). Geen actie nodig, drievoudige consistentie.

## NIEUW_INTERSECT_OUD (Sweep A/B vinden opnieuw wat legacy al had)

| Cluster/plek | Sweep A/B temp-ID('s) | Legacy | Opmerking |
|---|---|---|---|
| Babaji-grot | KUM-SWEEP-A-001 / KB2-001 | #15, LOCKED A | zie hierboven, nu 079 |
| Kainchi Dham | KUM-SWEEP-A-002 / KB2-008 | #19, LOCKED A | drievoudig bevestigd |
| Kasar Devi-grot/tempel | KUM-SWEEP-A-003 / KB2-033 | #20, LOCKED A | drievoudig bevestigd |
| Hanuman Garhi, Nainital | KB2-010 | #24, LOCKED A | Sweep B + legacy, niet in Sweep A |
| Jageshwar-tempelcomplex | KUM-SWEEP-A-007 / KB2-043 | #23, LOCKED A | drievoudig bevestigd |
| Chitai Golu Devta Temple | KB2-045 | #30, LOCKED A | Sweep B + legacy |
| Ramakrishna Kutir, Almora | KB2-025 (out-of-scope in Sweep A) | #29, LOCKED A | alle drie: institutioneel, geen persoonlijke Ramakrishna-locatie |
| Haidakhan Vishwa Mahadham | KUM-SWEEP-A-005 / KB2-041 | #46, LOCKED A (DECISION-0001) | drievoudig bevestigd; Babaji-identificatie in alle drie behandeld als traditieclaim, niet feit |
| Bhumiyadhar (Ram Dass/NKB eerste ontmoeting) | KB2-009 (als "Bhumiadhar") | #27, LOCKED A (DECISION-0002) | zie BRON_CONFLICTEN hieronder — legacy lost Sweep B's identiteitsvraag op |
| Anandamayi Ashram, Patal Devi (Almora) | KUM-SWEEP-A-004 / KB2-017 | genoemd in CLUSTER_LOCATIONS-context (Almora-cluster), geen los nummer in LOCKED_A gezien | grotendeels bevestigd, exacte legacy-A-status voor dit specifieke sub-adres nog na te lopen |
| Lala Badri Sah's House | KB2-032 | #35, CLUSTER_LOCATIONS ("verbleef hier 1890 en 1897") | Sweep B + legacy; legacy-A-status voor #35 niet expliciet in LOCKED_A gezien, wel in neutrale inventaris |

## NIEUW_MIN_OUD (Sweep A/B vinden dingen die legacy niet had)

Vooral een groot, gedetailleerd Vivekananda-circuit uit Sweep B, gebaseerd op de officiële
Ramakrishna Kutir "three-visits"-pagina, die legacy destijds niet zo diep uitgewerkt had:
Kathgodam Railway Station (KB2-020), Kakrighat Jnana Vriksha (KB2-022, legacy had wel Kakrighat
zelf als #22 maar niet deze specifieke boom-/realisatieplek uitgesplitst), Vivekananda Shila/
Karbala (KB2-023), Lodhia-ontvangstzone/Vivekananda Dwar (KB2-024), Thompson House (KB2-026),
English Club (KB2-027), Oakley House/Nivedita Cottage (KB2-028), Government Inter College
(KB2-029), Amba Dutt's Garden (KB2-030), Raghunath Temple (KB2-031), Dewaldhar Estate (KB2-034),
Syahi Devi (KB2-035), Mornaula Dak Bungalow (KB2-036), Binsar Dak Bungalow (KB2-037), Mayavati
Advaita Ashrama (KB2-038). Ook nieuw: Yogoda Satsanga-meditatiecentra in Nainital/Kathgodam
(KB2-006/007, institutioneel YSS, geen persoonlijk Yogananda-bezoek), en Anandamayi Ma's Naina
Devi Temple/Nanda Devi Temple/Mirtola-ontmoeting (KB2-014/016/019).

Dit is substantieel nieuw materiaal, met name voor Vivekananda. Nog GEEN identity-check tegen
legacy CLUSTER_LOCATIONS-nummers uitgevoerd voor elk afzonderlijk punt — expliciet als openstaand
vermeld, niet stilzwijgend als "nieuw" gepromoveerd zonder verdere check.

## OUD_MIN_NIEUW (legacy had dingen die beide nieuwe sweeps misten)

- **Turiya Niwas** (#36, LOCKED A) — huis van Alfred "Sunyata" Sorensen op Crank's Ridge, nu
  homestay; tevens CLUSTER_ANCHOR. Niet gevonden in Sweep A of Sweep B — moet fysiek/inhoudelijk
  opnieuw geverifieerd worden conform TASK.md (niet automatisch verwijderen).
- **Bodh Ashram** (#37, LOCKED A) — voormalig landgoed Evans-Wentz/Lama Govinda, bezocht door
  Anandamayi Ma en Neem Karoli Baba, Beats bezochten Govinda hier. Niet gevonden in Sweep A of B
  — zelfde behandeling.
- **Ghorakhal Temple** (LOCKED_B, Golu Devta) — niet gevonden in Sweep A/B; status B (niet
  bezoeken tenzij tijd het toelaat), dus lagere prioriteit voor heropening maar wel vastgelegd.
- **Mirtola/Krishnaprem Ashram** (#31), **Binsar Wildlife Sanctuary** (#32), **Patal Bhuvaneshwar**
  (#33), **Dhaulchina Ashram** (#38) — alle vier legacy `LOCKED_C` (bewust afgewezen door Mark).
  Sweep A vond zelfstandig Patal Bhuvaneshwar (KUM-SWEEP-A-006) en Dhaulchina (binnen
  KUM-SWEEP-A-004) opnieuw als kandidaat zonder de bestaande C-status te kennen (blindheidsregel
  correct toegepast) — dit is GEEN fout van Sweep A, maar betekent wel: deze twee mogen NIET
  stilzwijgend als open kandidaat blijven staan. Mark heeft ze al eerder bewust afgewezen. Status
  C blijft van kracht, niet opnieuw aan Mark voorleggen tenzij nieuw doorslaggevend bewijs
  opduikt dat het eerdere C-besluit zelf ter discussie stelt — dat is hier niet het geval.

## BRON_CONFLICTEN

- **Bhumiadhar (NKB) vs Bhumiya Dhara (Anandamayi Ma)** — Sweep B (`INDIA_SWEEP_B.md`) markeerde dit
  expliciet als onopgeloste identiteitsvraag tussen twee mogelijk verschillende plekken met
  gelijkende namen. Legacy lost dit gedeeltelijk op: `#27 Bhumiyadhar` is in `DECISION-0002`
  specifiek vastgelegd als de plek van Ram Dass' EERSTE ontmoeting met Maharaj-ji in 1967, apart
  van Kainchi Dham zelf (#19). Dit bevestigt dat er minstens één specifieke, aparte
  "Bhumiyadhar"-locatie is voor de NKB/Ram Dass-context. Of dit dezelfde plek is als de
  "Bhumiya Dhara" die Sweep B aan Anandamayi Ma koppelt (vier mijl van Naina Temple) is
  NIET bevestigd of ontkracht door legacy-data — blijft een echt openstaand identiteitspunt,
  nu wel scherper geformuleerd dan voorheen.
- **Haidakhan Baba = Mahavatar Babaji?** — geen conflict: Sweep A, Sweep B en legacy zijn het er
  alle drie mee eens dat dit een traditie-eigen claim is, geen bevestigd feit. Consistente
  drievoudige voorzichtigheid.

## MARK_BESLUIT_CONFLICTEN

Geen. Het enige punt waar een vers Mark-besluit een legacy-A-besluit raakt (de Babaji-grot) is
volledig consistent: A toen, A nu, zelfde reden. Geen van de overige legacy A/B/C-besluiten wordt
door Sweep A- of Sweep B-bevindingen in twijfel getrokken.

## GEEN ACTIE / STATUS ONVERANDERD

Alle overige legacy `LOCKED_A`/`LOCKED_B`/`LOCKED_C`-besluiten (Bodh Gaya-, Varanasi-, Agra- en
Vrindavan-vermeldingen in dezelfde bestanden) vallen buiten deze Kumaon-taak en zijn niet geraakt.

## PERMANENTE TOEKENNING DEZE RONDE

Alleen de Babaji-grot krijgt nu een permanent nummer (079) — dit is de enige kandidaat met de
combinatie van drievoudige fysieke-identiteitsbevestiging + expliciet, herhaald Mark-besluit die
een veilige toekenning rechtvaardigt zonder verder identity-onderzoek. De overige 7
Sweep-A-tijdelijke ID's en 44 resterende Sweep-B-tijdelijke ID's blijven tijdelijk; zie
NIEUW_INTERSECT_OUD/NIEUW_MIN_OUD/OUD_MIN_NIEUW hierboven voor de stand per cluster.

## NEXT_ALLOWED_STEP

1. WGS84-coördinaten voor locatie 079 (Babaji-grot) verifiëren — nog nooit gedaan, ook niet in
   legacy.
2. Bhumiadhar/Bhumiya Dhara-identiteit verder uitzoeken (NKB vs Anandamayi Ma, mogelijk twee
   verschillende plekken met gelijkende naam).
3. Turiya Niwas en Bodh Ashram (legacy #36/#37) fysiek/inhoudelijk heropenen en bevestigen of
   afwijzen — gemist door beide nieuwe sweeps.
4. Voor de overige Sweep-B-Vivekananda-circuitpunten (NIEUW_MIN_OUD): per punt een identity-check
   tegen bestaande legacy-nummers, vóór verdere permanente toekenning.
5. Geen PDF, geen route, geen A/B/C-voorspelling voor andere locaties dan de Babaji-grot.

---
Geschreven door: CCI. Eén permanent nummer toegekend (079, Babaji-grot, A, LOCKED_BY_MARK). Geen
PDF, geen route. `PDF_STATUS: VERBODEN` gerespecteerd.
