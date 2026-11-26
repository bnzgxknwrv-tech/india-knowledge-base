# CLUSTER_RECALL_AUDIT — INDIA ZILVER

status: COMPLETE
scope: repo-state on `agent/indiazilver-cluster-completeness-audit`
rule: additief; geen bestaande locatie, permanent ID of Mark A/B/C gewijzigd.

## Executive count

- Eerder afgerond/bevroren/ABC-complete cluster dat nu inhoudelijk moet heropenen: **3**.
- `REOPEN_REQUIRED: JA`: **VARANASI**, **BODH GAYA / GAYA-CORRIDOR**, **KUMAON**.
- Tiruvannamalai/Arunachala telt NIET als heropening: het A-cluster is door Mark gelockt, maar de regionale METHOD_V2-sweep was expliciet nog niet gestart.

## Clusteraudit

| cluster | eerdere status | later reverse-discovery signaal | type | REOPEN_REQUIRED |
|---|---|---|---|---|
| VARANASI | 45 permanente locaties; Mark A/B/C afgerond; verblijf `VNS-HOTEL-001` locked | Lahiri: Rana Mahal Ghat bevestigd; Panchganga Ghat Ashram-signaal; Ramnagar-paleis/Kashi Naresh-link; postmortale/hostgraph-leads. Sri Yukteswar: Pranabashram Benares-lead. | 1 exact nieuwe fysieke kandidaat + same-site/identity checks + leads | **JA** |
| BODH GAYA | Mark-besluiten locked voor de open Bodh-Gaya-set; numbering registry aanwezig | Sri Yukteswar: monastieke geloften in Bodh Gaya onder Mahant Krishnadayal Giri, later tweedetector-plausible. Anandamayi Ma: Rajgir als nabij corridor-signaal, maar fysieke identiteit/persoonlijke aanwezigheid niet hard genoeg. | stad/regio/lead; nog geen nieuwe exacte site uit deze claims | **JA** |
| GAYA AIRPORT–BODH GAYA CORRIDOR | dubbele locatie-sweep gereconcilieerd, 0 nieuwe corridor-kandidaten | persoonslaag toont dat '0 nieuwe locatie-sweep-kandidaten' niet gelijkstaat aan persoons-compleet; Bodh-Gaya/Sri-Yukteswar-lead moet in lokale proximity-backfill worden meegenomen | lead / methodische reopen | **JA** (samen met BODH GAYA) |
| KUMAON | legacy `KUMAON-COMPLETE-001` had 46 genummerde locaties + LOCKED A/B/C | latere reverse/hostgraph-rescue vond Turiya Niwas en Bodh Ashram; beide inmiddels 080/081 A LOCKED. Vivekananda leverde daarnaast een Almora `REGION_MISS`-lead; Mayavati werd als bestaande `KB2-038` herkend | reeds bewezen fysieke misses + nieuwe city-level lead | **JA** |
| TIRUVANNAMALAI / ARUNACHALA | Mark: A-cluster locked | landelijke person sweep vond Arunachaleswarar, Virupaksha Cave, Skandashram, Sri Ramanasramam + Tiruchuzhi; Yogananda-link op Ramanasramam | nieuwe fysieke kandidaten | **NEE — geen 'reopen'; clusterresearch was nog niet regionaal afgerond** |

## Waarom Varanasi aantoonbaar niet meer 'travel-complete' is

De permanente Varanasi registry bevat al `VNS-CAND-004 Shri Tailanga Swami Math`, `011 Panchganga Ghat`, `044 Ramnagar Fort` en 001-045 zonder nummerwijziging. Latere Lahiri-reconciliatie bevestigt echter **Rana Mahal Ghat** als apart bezoek-/badpunt; die naam staat niet in de 001-045 registry. Panchganga Ghat Ashram moet eerst tegen 004/011 worden gededupliceerd; Ramnagar-paleis moet eerst tegen 044 worden gematcht. Geen nieuw nummer claimen voor die twee voordat identity-resolutie klaar is.

## Bodh Gaya nuance

De Sri-Yukteswar-claim 'Bodh Gaya monastieke geloften' is tweedetector-plausible maar heeft op deze branch nog geen voldoende specifieke fysieke klooster/site-identiteit. Daarom heropenen we de cluster voor lokale backfill, maar tellen we deze claim NIET als harde nieuwe-ID-kandidaat.

## Kumaon nuance

Kumaon is het bewijs dat heropening nodig kan zijn na een eerdere 'complete' sweep: Turiya Niwas en Bodh Ashram werden pas via latere host-/informele-verblijfslogica gered en hebben inmiddels 080/081. Zij worden hier dus niet opnieuw in de nieuwe-ID-queue gezet. De open Almora/Vivekananda-lead blijft een reden waarom `TRAVEL_COMPLETENESS_GATE` nog niet JA kan zijn.

## Niet als fysieke kandidaat geteld

- alleen stad/regio: Bareilly, Calcutta-familiehuis zonder adres, Danapur, Almora-lezingen, Rajgir-signaal;
- niet-bestaande historische plek: Lahiri's oorspronkelijke Ghurni-site die door rivierverlegging verdween;
- tijdelijk/vaag terrein: Kumbh Mela zonder vaste subsite, Ganga Sagar-kamp, Rajputana-bundel;
- postmortale/traditieclaim zonder identificeerbare huidige site;
- mogelijke duplicates van bestaande permanente locaties.
