# MISSING_FROM_PERSON_HEATMAP — INDIA GOUD

Datum: 2026-08-19

## Hoofdantwoord

**Nee:** een grote-clusterlijst die uitsluitend uit Top-person overlap/person-count is opgebouwd kan niet veilig als volledige spirituele reisruggengraat dienen.

De person-methode detecteert vooral waar geselecteerde personen fysiek verbleven, bezochten of samenkomen. Zij detecteert niet betrouwbaar plaatsen die hun zwaarte ontlenen aan een gebeurtenis, religieuze traditie, heilige geografie, pelgrimsfunctie of historische instelling.

## Zeker gemist / structureel ondergewaardeerd

### Bodh Gaya
- Waarom person-heatmap faalt: hoofdwaarde = Boeddha's verlichting en Mahabodhi/Bodhi Tree, niet Top-11-overlap.
- Projectwaarheid: bestaand 046 A + beschermde Bodh Gaya-keuzes.
- Consequentie: moet hard in master union blijven, onafhankelijk van person-score.

### Sarnath
- Waarom person-heatmap faalt: hoofdwaarde = eerste leerrede.
- Projectwaarheid: 006 A, LOCKED_BY_MARK-context via Varanasi-besluit.
- Consequentie: als Varanasi alleen op Top-person-count wordt geclusterd kan Sarnath ten onrechte als laagwaardige satelliet verdwijnen.

### Kushinagar
- Waarom person-heatmap faalt: hoofdwaarde = Mahaparinirvana.
- Projectstatus: geen bestaande permanente ID/A-B-C aangetroffen op toegestane GOUD-branch.
- Consequentie: expliciet als kandidaatcluster voor latere ID/A-B-C bewaren.

### Rajgir / Nalanda
- Waarom person-heatmap faalt: vroege boeddhistische geschiedenis, heilige plekken en monastiek-universitaire betekenis zijn niet afhankelijk van de Top-11.
- Projectstatus: README meldt dat deze eerder niet de actieve volgende regio waren; geen afwijzing.
- Consequentie: behouden in union; later door Mark laten wegen tegen capaciteit.

### Haridwar / Rishikesh
- Waarom person-heatmap faalt: zelfstandige Hindu/Ganga/yoga/pelgrimsfunctie kan sterk zijn bij geringe Top-11-overlap.
- Actuele officiële bronstatus: Uttarakhand Tourism noemt Haridwar een van India's belangrijkste Hindu-pelgrimsplaatsen/Kumbh-stad en Rishikesh een groot pelgrims- en yogacentrum.
- Consequentie: niet automatisch route-includen, maar ook niet laten verdwijnen door person-score.

## Bestaande clusters die person-score wél vindt, maar niet uitsluitend daarom mogen blijven

- **Arunachala/Tiruvannamalai:** personlaag vindt Ramana + Yogananda; daarnaast expliciet `LOCKED_BY_MARK` A-anker.
- **Varanasi/Kashi:** personlaag is sterk, maar Kashi Vishwanath, Ganga/ghats en Sarnath hebben zelfstandige religieuze zwaarte.
- **Prayagraj/Kumbh:** personlaag vindt historische Top-person events, maar Kumbh is zelfstandig religieus evenement/anker.
- **Kolkata/Belur/Dakshineswar:** sterke person-overlap én zelfstandige institutionele/historische betekenis.
- **Puri:** person-overlap via Sri Yukteswar/Hariharananda; daarnaast Jagannath/Puri als zelfstandige spirituele omgeving. Deze audit verheft Jagannath niet automatisch tot nieuwe Mark-bestemming; het signaleert alleen dat person-count niet de enige detector mag zijn.

## Methodische fout als alleen TURQUOISE/person-overlap wordt gebruikt

1. `person_count = 0/1` kan toch `spiritual_anchor_weight = very_high` zijn.
2. Een lokale satelliet zoals Sarnath kan geografisch in een groter cluster verdwijnen terwijl de inhoudelijke reden zelfstandig is.
3. Een bestaande Mark-lock kan lager scoren dan nieuwe overlapclusters en daardoor visueel wegzakken; locks moeten als aparte beschermde laag worden ge-unioned.
4. Historische gebeurtenissen (verlichting, eerste leerrede, parinirvana, Kumbh) zijn geen 'personenbezoek'-datamodel.
5. Traditieclusters (Ganga, yoga, Sikh/Hindu/Jain/Buddhist pilgrimage) vereisen een detector die niet aan de Top-11-selectie hangt.

## Branch-lokale beperking

De map `runs/active/INDIATURQUOISE-ALLPERSON-OVERLAP-001` is niet aanwezig op de door deze taak exclusief toegestane branch `agent/indiagoud-nonperson-anchor-audit`. Daarom is **geen cross-branch TURQUOISE-read** uitgevoerd. De vergelijking gebruikt:
- de taakpremisse dat TURQUOISE een person-heatmap is;
- de op deze branch aanwezige `PHASE2_SYNTHESIS.md` als person-driven referentielaag;
- bestaande Mark-besluiten en locks op dezelfde branch.

Dit voorkomt schending van de branchregel. Een latere integrator kan dit bestand lossless tegen de daadwerkelijke TURQUOISE-output unionen.

## Kritieke missing-cluster set voor de master union

Minimaal verplicht als aparte non-person/lock-laag:
- BODH_GAYA — bestaand, beschermd
- SARNATH — bestaand, beschermd
- KUSHINAGAR — kandidaatcluster voor later besluit
- RAJGIR_NALANDA — kandidaatcluster voor later besluit; intern twee inhoudelijke ankers
- HARIDWAR_RISHIKESH — kandidaatcluster/familie voor later besluit; niet automatisch één route-eenheid
- alle bestaande Mark-locks, met ARUNACHALA/TIRUVANNAMALAI expliciet beschermd

## Bronnen

Repo:
- runs/active/TOP11-INDIA-PERSON-CENTRIC-MEGASWEEP-001/PHASE2_SYNTHESIS.md
- runs/active/BODHGAYA-DISCOVERY-001/MARK_DECISIONS_2026-08-05.jsonl
- runs/active/VARANASI-GEO-DELIVERY-REPAIR-001/MARK_DECISIONS_2026-08-02.jsonl
- decisions/ARUNACHALA_TIRUVANNAMALAI_A_ANCHOR_2026-08-18.md

Actueel extern:
- https://whc.unesco.org/en/list/1056/
- https://whc.unesco.org/en/list/1502/
- https://www.uttarakhandtourism.gov.in/destination/haridwar
- https://www.uttarakhandtourism.gov.in/destination/rishikesh
