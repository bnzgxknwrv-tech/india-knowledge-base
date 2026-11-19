# CCI REPO AUDIT — inconsistenties, gemiste updates, GitHub-structuur

```
uitgevoerd_door: CCI
uitgevoerd_op: 2026-08-20
aanleiding: Mark, rechtstreeks — "neem de gehele India repo door en kijk of je inconsistenties
  kunt vinden en fouten... het lijkt erop dat de huidige soms dingen mist die eerder wel
  weergegeven zijn... hoe zit de github in elkaar? Is er verbetering nodig?"
aard: PUUR ONDERZOEK — geen enkel bestand aangepast, geen fix uitgevoerd, geen A/B/C aangeraakt.
  Dit rapport is bedoeld voor ChatGPT/INDIA8 om op te reageren en prioriteiten te stellen.
```

## TL;DR voor ChatGPT

Er zijn geen datafouten in de zin van "verkeerde locatie" gevonden. Het probleem dat Mark voelt
("het mist soms dingen die eerder wel te zien waren") is **reëel en heeft een concrete, aanwijsbare
oorzaak**: dit project draait feitelijk **twee parallelle universums** die elkaar niet meer volledig
zien:

1. **Het "regio-GOUD"-universum** (Varanasi, Bodh Gaya, Kumaon) — PDF's, KML's, BESLISOVERZICHTen
   onder `runs/active/<REGIO>/GOUD/USER/` op de PR #23-werkbranch. Dit is wat Mark tot nu toe
   fysiek opent/leest voor zijn A/B/C.
2. **Het "INDIA8-master"-universum** — de nieuwe `ALL_FINDINGS_LOCATION_MASTER.jsonl` (700 rijen,
   575 fysieke entiteiten) en de zes kleur-agentbranches (BLAUW/ROOD/GEEL/WIT/TURQUOISE/ZILVER) +
   `agent/india8-cluster-casting`. Dit is verreweg het grootste en meest volledige onderzoekswerk
   van de laatste week, maar het staat **op branches die niet in enige open Pull Request zitten**
   en die de regio-GOUD-branch niet heeft.

Deze twee universums zijn nooit samengevoegd. Zie §1-§3 voor het bewijs, §4 voor concrete
datainconsistenties, §5 voor een prioriteitenlijst.

---

## 1. Hoe de GitHub-repo nu in elkaar zit

```
main (c21a24b, bevroren sinds vroege Varanasi-fase — 3 top-dirs: india4/, pipeline/, runs/)
 ├─ PR #23 (draft) — claude/werk-je-nu-of-niet-oa10y7 — 219 commits vóór main, 157 comments
 │    bevat: alle regio-GOUD-werk (Varanasi compleet, Bodh Gaya compleet, Kumaon deels),
 │    governance/, india4/, india5/ (grotendeels ongebruikt), CCI-eigen QA-runs
 ├─ PR #24 (draft) — agent/add-yogananda-location-atlas — 2 commits, geen relatie tot PR #23-flow
 │    bevat: één losstaand 114-record Yogananda-atlasdocument (nu al gereconcilieerd in de master)
 │
 └─ GEEN PR (dus onzichtbaar in de normale PR-lijst van de repo):
      agent/india8-cluster-casting              281 commits vóór main  ← centrale coördinatie
      agent/indiazilver-cluster-completeness-audit  253 commits vóór main  ← bevat PROTECTED_CANON_BASELINE.csv
      agent/indiawit-master-travel-readiness     241 commits vóór main
      agent/indiaturquoise-allperson-overlap     226 commits vóór main
      agent/indiablauw-trip-ops-prep             229 commits vóór main
      agent/indiageel-ramana-ramakrishna-sweep   222 commits vóór main
      agent/chatgpt-top11-parallel-sweep         170 commits vóór main
      agent/indiarood-core-kriya-sweep            12 commits vóór main
```

**Kernprobleem**: 8 van de 10 actieve branches — inclusief de branch met de canonieke 001-081
ID/coördinaten/ABC-baseline (`PROTECTED_CANON_BASELINE.csv` op ZILVER) en de branch met het
grootste, meest recente onderzoek (`agent/india8-cluster-casting`, 700-rijen master) — hangen
"los in de lucht": geen PR, dus niet zichtbaar voor een reviewer die alleen naar "Pull requests"
kijkt, geen geplande merge naar main, geen merge naar PR #23's eigen branch. Alles wat CCI het
afgelopen etmaal heeft opgeleverd (P0-build, scope-correctie, foto-locatiesluiting, TURQUOISE-
relaties, ROOD-labels) bestaat **uitsluitend** op `agent/india8-cluster-casting` — niet op main,
niet op PR #23's branch.

Dit is niet nieuw voor deze week: het is dezelfde structuur die eerder al één keer werk heeft
gekost (zie §2) en die het risico op precies Marks klacht ("iets dat ik eerder zag is nu weg")
structureel in stand houdt.

## 2. Precedent: dit patroon heeft al eerder tot verlies geleid

`governance/ACTIVE_STATE.md` documenteert zelf een eerdere episode van exact hetzelfde probleem:
een oudere architectuur (`KUMAON-COMPLETE-001`, branch
`controller/kumaon-complete-001-ready-for-zilver-20260719`) had al **28 eigen LOCKED_A-locaties**
voor Kumaon plus 4 LOCKED_C en 2 LOCKED_B — nooit gemerged, eigen incompatibele nummering. Toen
Kumaon later opnieuw werd gesweept, misten **beide** onafhankelijke nieuwe sweeps twee daarvan
(079 Turiya Niwas, 081 Bodh Ashram) totdat een aparte "miss-root-cause-rescue"-taak (CCI_TASK 078)
ze alsnog terugvond. Root cause destijds: dezelfde soort branch-eilandvorming als nu bij de
kleur-agents. Er is nooit een structurele fix doorgevoerd om herhaling te voorkomen — alleen een
incident-specifieke rescue.

## 3. `governance/ACTIVE_STATE.md` — het bestand dat elke nieuwe sessie "eerst moet lezen" — is 6 dagen stale

Het bestand zelf zegt (regel 3-4): *"Een nieuwe INDIA-regisseursessie moet eerst ACTIVE_STATE +
actieve protocolcanon lezen. Oude chatgeschiedenis is niet vereist voor correcte voortzetting."*
Het bestand is gedateerd **2026-08-14**. Sindsdien (2026-08-15 t/m 2026-08-20, dus het grootste
deel van het Top-11-persoonsgerichte onderzoek) is er:

- geen enkele vermelding van de zes kleur-agentbranches of `agent/india8-cluster-casting`;
- geen vermelding van `ALL_FINDINGS_LOCATION_MASTER.jsonl`, de 700-rijen master, of de
  QA/P0-bouwronde;
- geen vermelding van de foto-locatiesluiting Anandamayi×Yogananda;
- `ACTIVE_TASKS` bevat uitsluitend taken t/m 2026-08-15 (KUMAON-V2-RESWEEP-001,
  TOP11-INDIA-PERSON-CENTRIC-MEGASWEEP-001 "pilot klaar, wacht op QA") — de daadwerkelijke
  vervolgstappen (het volledige 6-persoons-multidetector-programma dat daarna liep) staan er niet
  in.

**Dit is zeer waarschijnlijk de directe oorzaak van Marks ervaring.** Als een nieuwe INDIA-sessie
— of Mark zelf — bootstrapt vanuit dit bestand (zoals het bestand zelf voorschrijft), ziet die
sessie een wereld die zes dagen oud is en mist het complete tweede-helft-onderzoek. Het bestand
is niet fout in wat er staat, het is alleen niet meer bijgewerkt sinds de INDIA8-architectuur
begon.

## 4. Concrete, verifieerbare inconsistenties (data-niveau)

### 4.1 Bodh Gaya KML toont 4 locaties, de bijbehorende PDF toont 33

`runs/active/BODHGAYA-DISCOVERY-001/GOUD/BODHGAYA_046_049.kml` bevat **4 Placemarks** (046-049).
De uiteindelijke, door Mark geaccepteerde PDF (`V1_BODHGAYA_KEUZE_REISGIDS.pdf`, na
`CONTENT_QA_ACCEPTED` + `PDF_GO`) dekt **046 t/m 078** (33 locaties, alle LOCKED_BY_MARK). Er is
geen KML-bestand dat de uiteindelijke 33 bevat — alleen een tussentijdse versie met de eerste 4.
Wie vandaag de Bodh Gaya-kaart opent, ziet dus 4 van de 33 vastgelegde locaties.
Er bestaan bovendien **drie PDF-bestanden** naast elkaar in dezelfde map
(`BODHGAYA_046_049_KEUZE_REISGIDS.pdf`, `BODHGAYA_046_058_KEUZE_REISGIDS.pdf`,
`V1_BODHGAYA_KEUZE_REISGIDS.pdf`) zonder dat de twee oudere gearchiveerd/verwijderd zijn — een
lezer die niet weet dat `V1_` de laatste is, kan makkelijk de verkeerde openen.

### 4.2 Geen enkel echt "globaal" nummerregister — twee losse regionale bestanden

`ACTIVE_STATE.md` spreekt van één doorlopende `LAST_GLOBAL_LOCATION_NUMBER` (081), maar er bestaat
geen machine-leesbaar globaal registerbestand. Er zijn twee **regionale**
`NUMBERING_REGISTRY.jsonl`-bestanden (Varanasi, Bodh Gaya) die onafhankelijk van elkaar bijhouden
welke nummers per regio zijn uitgegeven; de enige plek waar de globale doorlopende telling ("Bodh
Gaya eindigt op 078, Varanasi eindigt op 045, geen overlap") staat vastgelegd is **platte tekst**
in `ACTIVE_STATE.md`. Niets controleert machinaal of een toekomstige regio per ongeluk een al
gebruikt nummer hergebruikt buiten wat een mens/AI zelf naleest.

### 4.3 De canon-baseline (001-081, ABC, coördinaten) staat op een branch los van PR #23

`PROTECTED_CANON_BASELINE.csv` — het bestand met alle 81 permanente ID's, hun ABC-status en
coördinaten — bestaat alleen op `agent/indiazilver-cluster-completeness-audit`. Het staat **niet**
op PR #23's eigen branch (`claude/werk-je-nu-of-niet-oa10y7`) en niet op `main`. Als PR #23 vandaag
gemerged zou worden, zou de canonieke ID-baseline niet meevloeien.

### 4.4 `ALL_FINDINGS_LOCATION_MASTER.jsonl` (700 rijen): 27 "wees"-parent-clusters

Automatische check op de nieuwste master: 27 waarden van `parent_entity_key` (bv. "Vrindavan NKB
cluster", "Kainchi Ashram", "Delhi host network") verwijzen naar een cluster dat zelf nergens als
eigen `physical_entity_key`-rij bestaat. Geen dataverlies (de child-rijen zelf zijn compleet en
correct), maar een tool die op deze parent-sleutel zou groeperen/renderen zou een leeg of
ontbrekend clusterknooppunt tegenkomen.

### 4.5 `existing_permanent_id`-veld mengt twee ID-generaties

Van de 13 rijen met een ingevulde `existing_permanent_id` gebruiken 6 het schone canon-formaat
(`002`, `004`, `009`, `011`, `044`, `079`) en de overige een ouder, ander formaat
(`OLD31-13`, `OLD31-14`, `OLD31-21`, `OLD31-22`, `OLD31-28`, `OLD31-29`, `NKB_VRINDAVAN_EXISTING`).
Functioneel niet fout (beide zijn traceerbaar), maar het is een teken dat er ergens nog een
derde, oudere ID-reeks ("OLD31-...") meespeelt die nergens in `ACTIVE_STATE.md` als bestaand
systeem wordt genoemd.

### 4.6 `india5/` — een volledig tweede taak-architectuur, expliciet gedeprecieerd, nog steeds fysiek aanwezig

`india5/tasks/{active,queue,done,failed}/`, `india5/schemas/`, `india5/scripts/` vormen een eigen,
zwaardere taaksysteem (sha256-hash-pinning, allow/forbid-ACL's) dat `ACTIVE_STATE.md` zelf
"BESLOTEN ... NIET gereactiveerd. Blijft ongebruikt/gedeprecieerd" noemt — maar de bestanden staan
er nog steeds, met een eigen `GOVERNANCE.md` en `TASK_PROTOCOL.md` die qua naam bijna identiek zijn
aan de wél actieve `india4/protocols/INDIA5-PROTOCOL.md`. Een nieuwe sessie (mens of AI) die op
naam zoekt naar "INDIA5-protocol" kan zonder oplettendheid in het verkeerde, dode systeem
terechtkomen.

## 5. Wat dit betekent voor de huidige ABC-ronde specifiek

Voor zover nu vastgesteld raakt geen van bovenstaande punten de **inhoud** van Marks reeds gemaakte
ABC-besluiten (Varanasi 001-040 + hotel, Bodh Gaya 046-078) — die staan onveranderd en consistent
in `PROTECTED_CANON_BASELINE.csv`, de BESLISOVERZICHTen en de PDF's. Het risico zit in:

- **wat Mark ná deze twee regio's te zien krijgt**: als een volgende regio (Kolkata/Oost, Ranchi,
  Vrindavan/Braj) wordt klaargezet vanuit het INDIA8-mastersysteem zonder terugkoppeling naar de
  regio-GOUD-structuur die Mark gewend is, kan dat aanvoelen als "ineens anders" of "iets mist" —
  niet omdat data verloren is, maar omdat de twee universums nooit zijn samengevoegd tot één
  weergave;
- **de Bodh Gaya-kaart specifiek nu al** (§4.1) toont een verouderde, onvolledige selectie als
  iemand vandaag de KML opent.

## 6. Aanbevelingen (geen van alle uitgevoerd — ter beoordeling aan ChatGPT/Mark)

Op volgorde van vermoedelijke impact, niet van moeite:

1. **Eén consolidatiepad kiezen voor de INDIA8-kleur-architectuur.** Ofwel een PR openen voor
   `agent/india8-cluster-casting` (en/of de losse kleurbranches mergen in die ene branch eerst),
   ofwel expliciet besluiten dat PR #23 voortaan die branch als basis neemt. Zolang dit niet
   gebeurt, blijft al het recente werk (700-rijen master, canon-baseline) buiten het zicht van een
   gewone PR-review en buiten `main`.
2. **`governance/ACTIVE_STATE.md` bijwerken tot vandaag**, of expliciet vervangen door een
   verwijzing naar het nieuwere systeem, zodat een volgende sessie niet zes dagen werk mist bij het
   bootstrappen. Dit is de goedkoopste fix met de grootste kans om Marks klacht structureel op te
   lossen.
3. **Bodh Gaya-KML herbouwen** vanaf de uiteindelijke 33 LOCKED_BY_MARK-locaties (046-078), en de
   twee oudere PDF-versies uit `GOUD/USER/` verwijderen of duidelijk als "SUPERSEDED" markeren.
4. **Eén machine-leesbaar globaal nummerregister** invoeren (of de twee regionale bestanden
   samenvoegen/valideren tegen elkaar) in plaats van alleen een prozabeschrijving in
   `ACTIVE_STATE.md`.
5. **`india5/`-map verwijderen of duidelijk `DEPRECATED_DO_NOT_USE` markeren** in de bestandsnaam/
   directorystructuur zelf, niet alleen in proza elders — voorkomt naam-verwarring met het actieve
   `india4/protocols/INDIA5-PROTOCOL.md`.
6. **De 27 wees-`parent_entity_key`-waarden in de master ofwel promoveren tot eigen entiteitsrij,
   ofwel expliciet documenteren als "groeperingslabel, geen eigen fysieke plek"** — nu is het
   onderscheid niet zichtbaar zonder deze audit.
7. **`existing_permanent_id`-veld normaliseren** naar één ID-stijl, of het `OLD31-*`-systeem
   expliciet benoemen als een bestaand derde ID-systeem in de governance-canon.

---

Geschreven door: CCI. Geen bestand buiten deze rapportdirectory aangepast. Geen A/B/C, geen route,
geen PDF, geen fix uitgevoerd — uitsluitend onderzoek en rapportage, zoals gevraagd.
