# METHOD_V2 — Top-11 person-centric megasweep (opvolger van METHOD_V1)

```
method_status: FORMALIZED_FROM_BENCHMARK_RESULT
formalized_by: CCI
formalized_at: 2026-08-16
basis: CCI_TASK 084 / BENCHMARK_RESULT.md (Anandamayi Ma driewegbenchmark) +
  RECONCILIATION_CCI_084.md
supersedes: METHOD_V1.md (blijft bewaard als historisch precedent; NIET stil verwijderd)
```

## Waarom V1 werd vervangen

METHOD_V1 (goedgekeurd na de Anandamayi Ma/Neem Karoli Baba-pilot, CCI_TASK 080) begon met
zoekmachine-discovery ("naam + ashram/gastheer/..."), met chronologie/hostketens als aanvullende
laag. Voor een veelreizende, decennialang gedocumenteerde persoon als Anandamayi Ma bleek dat de
verkeerde volgorde: CCI's eigen "verzadigde" sweep (~23 punten) miste tientallen expliciet in de
officiële bronchronologie genoemde fysieke plekken — bevestigd zowel door een externe 156-locatie-
AI-union als, onafhankelijk daarvan, door een source-first-corpuspass en door CCI's eigen
rechtstreekse verificatie in `RECONCILIATION_CCI_084.md` (8-9 harde CCI-misses, 13
source-first-only vondsten, allemaal met exacte datum in de officiële chronologie bevestigd).

**Kernles**: bij een goed gedocumenteerde persoon zit de hoogste recall in het corpus zelf
(officiële chronologie, biografie, dagboeken), niet in een zoekmachine-discoveryronde. Zoekmachines
vinden vooral wat al vaak online herhaald is; een systematische corpus-extractie vindt ook de
eenmalige, minder bekende vermeldingen (privéhuizen, dharmashala's, forten, sanatoria, scholen).

## Harde volgorde — negen fasen, verplicht in deze volgorde

### Fase 0 — corpus inventory
Stel per persoon expliciet vast welke bronnen tot het corpus horen: officiële chronologie/
levensgeschiedenis, autobiografie/biografie, dagboeken/memoires van naaste discipelen, lineage-
publicaties (Sangha/Math/Mission-eigen uitgaven), reisverslagen, fotobijschriften, brieven,
relevante archiefindexen. Leg per bronfamilie vast: beschikbaar/doorzoekbaar, of
`UNAVAILABLE`/`BRON_GEBLOKKEERD` (bijv. gescande PDF zonder OCR — precedent:
`YOGANANDA-ANANDAMAYI-PHOTO-LOCATION-001`, Gurupriya Devi's dagboek).

### Fase 1 — lossless corpus extraction
Elke plaatsvermelding wordt EERST als occurrence vastgelegd, vóór enig relevantiefilter. Huizen,
kamers, hostnamen, paleizen, sanatoria, stations, scholen, forten, rivierkampen, dharmashala's en
transit worden niet genegeerd. Machine-assisted waar het corpus dat toelaat (vgl. de 3-detector-
aanpak uit `AOAY-FULL-LOCATION-ATLAS-001`), aangevuld met handmatige jaar-/hoofdstukpas.

### Fase 2 — event/place normalization
Per occurrence apart vastleggen: persoon aanwezig (J/D/O/N)? gebeurtenis bewezen? fysieke
identiteit exact/deels/alleen plaatsniveau? exact subadres? host/gastheer? huidige instelling
versus historische site (institutioneel eerbetoon ≠ persoonlijk bezoek)?

### Fase 3 — host/network graph
Iedere genoemde gastheer, discipel, vorst, arts, geleerde, ashramhoofd, patroon of organisator
apart terugzoeken naar diens eigen huis/landgoed/instelling en de bezoekcontext. Dit is de as die
bij METHOD_V1 achteraf werd toegevoegd; in V2 is hij vanaf fase 3 verplicht, vóór brede
websearch-discovery.

### Fase 4 — discovery search
Pas NU brede websearch, alternatieve spellingen en regionale zoektermen voor plekken die het
corpus zelf niet expliciet indexeert. Discovery ondersteunt en vult aan; hij vervangt de
corpus-extractie niet en gaat er nooit aan vooraf.

### Fase 5 — onafhankelijke tweede-pass (CCI/INDIA)
Een tweede partij (CCI of INDIA, afhankelijk van wie fase 0-4 deed) voert een eigen pass uit via
een andere query-/bronroute, zonder de eerste lijst als discoverychecklist te gebruiken.

### Fase 6 — externe multi-AI adversarial union
Blanco prompt naar onafhankelijke externe AI's, zonder bestaande kandidatenlijst vooraf (conform
`governance/EXTERNAL_AI_PROMPT_RULES.md`). Detector-only kandidaten worden genoteerd, niet als feit
behandeld.

### Fase 7 — directe verificatie + reconciliatie
Alle detector-only claims en conflictpunten rechtstreeks tegen de bron controleren, niet op
meerderheid stemmen. **Expliciete les uit CCI_TASK 084**: controleer ook of een externe claim
werkelijk een plaatsvermelding is en niet per ongeluk een stuk methodologie-/metatekst dat door de
union-samenvoeging als locatie is geregistreerd (precedent: de "Mandi"-claim gesourcet aan "AI2's
eigen methodesectie" bleek vermoedelijk een compilatieartefact, geen echte claim). Een claim die bij
verificatie op de verkeerde fysieke plek blijkt te slaan (precedent: de Krishnamurti-ontmoeting,
foutief aan een Rajghat-schoolcampus toegeschreven terwijl de bron ondubbelzinnig Kitty Shiva Rao's
tuin aanwijst) wordt expliciet `FALSE_OR_UNSUPPORTED_EXTERNAL_CLAIM`, niet stilzwijgend genegeerd of
omgekeerd stilzwijgend overgenomen.

### Fase 8 — saturation
Pas na fase 0-7 mag `PERSON_SWEEP_SATURATED` worden geclaimd.

## Nieuwe saturationregel — vier verplichte gates

`PERSON_SWEEP_SATURATED: JA` betekent NOOIT meer alleen "zes zoekcategorieën zijn geprobeerd". Alle
vier onderstaande gates moeten aantoonbaar zijn doorlopen en gedocumenteerd:

1. **CORPUS-COVERAGE-GATE**: expliciete lijst van benoemde bronfamilies (fase 0), elk aantoonbaar
   doorlopen of expliciet `UNAVAILABLE`/`BRON_GEBLOKKEERD` met reden. Geen bronfamilie mag stil
   ontbreken.
2. **HOSTGRAPH-GATE**: aantoonbare fase-3-uitvoering — een lijst van teruggezochte gastheren/
   netwerkpersonen, niet alleen een intentieverklaring dat de host-as "is toegepast".
3. **DISCOVERY-GATE**: fase 4 uitgevoerd NA, niet vóór, fase 1-3, met vermelding van gebruikte
   zoektermen/spellingsvarianten.
4. **RECONCILIATIE-GATE**: fase 7 uitgevoerd — elke externe/detector-only claim heeft een
   expliciete uitkomst (`EXTERNAL_ONLY_VERIFIED_MISS` / `EXTERNAL_ONLY_UNVERIFIED` /
   `SAME_SITE_DIFFERENT_NAME` / `OUT_OF_SCOPE_OR_TRANSIT` / `FALSE_OR_UNSUPPORTED_EXTERNAL_CLAIM`),
   geen ongeverifieerde claim mag stilzwijgend worden opgenomen of genegeerd.

Daarnaast verplicht: een expliciete lijst van onopgeloste bronfamilies/tijdvakken (bijv. "dagboek X
niet volledig doorzocht") — saturation ondanks bekende hiaten mag, maar alleen met die hiaten
zichtbaar vermeld, niet verzwegen.

## Verhouding tot externe multi-AI — nog niet definitief besloten

Volgens `BENCHMARK_RESULT.md` is de zuivere beslisproef: pas METHOD_V2 prospectief toe op een
nieuwe persoon (Yogananda) vóórdat een externe AI-union daarvoor bestaat. Voegt een latere externe
blanco-sweep dan nog betekenisvolle, geverifieerde plekken toe die METHOD_V2 miste? Zo ja, blijft
externe multi-AI een verplichte detector voor alle Top-11. Zo nee, kan externe AI terugschalen naar
steekproef-/adversarial-audit. Dit besluit wordt niet in dit document vooruitgelopen.

## Wat ongewijzigd blijft uit METHOD_V1

- Eén persoon volledig afwerken en freezen vóór de volgende.
- Bestaande regiokandidaten NIET als discovery-checklist tijdens Fase 1-4.
- Repo-cross-check pas ná freeze (Fase C/vergelijking, zoals in alle eerdere taken).
- Geen A/B/C namens Mark. Geen PDF. Geen route/hotelplanning. Geen permanente locatie-ID enkel op
  basis van discovery — eerst identity/reconciliatie.
- Bij blocker op één persoon: blocker vastleggen, doorgaan naar de volgende als niet systeemwijd.

---
Dit bestand is canoniek voor alle toekomstige person-centric megasweeps. METHOD_V1.md blijft
bewaard als historisch precedent en wordt niet stil verwijderd.
