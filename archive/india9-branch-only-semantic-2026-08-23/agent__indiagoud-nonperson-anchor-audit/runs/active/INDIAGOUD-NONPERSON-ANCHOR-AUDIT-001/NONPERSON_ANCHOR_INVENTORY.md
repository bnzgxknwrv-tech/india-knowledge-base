# NONPERSON_ANCHOR_INVENTORY — INDIA GOUD

Datum audit: 2026-08-19
Scope: reisrelevante spirituele/historische ankers die niet veilig door person-count alleen worden gedetecteerd.
Regel: bestaande IDs/A-B-C/locks blijven exact staan; nieuwe ankers krijgen hier GEEN ID en GEEN A/B/C.

## Kernconclusie

De person-driven laag is onvoldoende als enige reisruggengraat. Op deze branch zijn minstens twee zwaarwegende niet-persoonsgedreven ankers al aantoonbaar door Mark beschermd maar methodisch kwetsbaar in een person-heatmap: **Bodh Gaya** en **Sarnath**. Daarnaast zijn **Kushinagar**, **Rajgir/Nalanda** en **Haridwar/Rishikesh** inhoudelijk grote spirituele clusters die expliciet in deze audit moeten blijven staan als union-input, ook als hun Top-11-person overlap laag of nul is.

## Bestaande beschermde ankers

| cluster / anker | projectstatus op deze branch | bestaande ID / lock | auditstatus |
|---|---|---|---|
| Bodh Gaya / Mahabodhi Temple Complex | volledig eerder discovery-traject | 046 Mahabodhi Temple Complex = A, LOCKED_BY_MARK; 047-049 eveneens A; 050-078 bestaande besluiten behouden | BESTAAND — nooit dupliceren |
| Sarnath sacred complex | bestaand Varanasi-cluster | 006 = A, cluster SARNATH, Mark-besluit 2026-08-02 | BESTAAND — nooit dupliceren |
| Varanasi/Kashi kern | uitgebreid bestaand regionaal cluster | 001-040 canoniek beoordeeld; o.a. Kashi Vishwanath 007 A, Dashashwamedh 009 A | BESTAAND |
| Arunachala / Tiruvannamalai | expliciet zelfstandig A-anker | LOCKED_BY_MARK 2026-08-18; geen route-lock | BESTAAND, person + non-person betekenis |
| Kumaon kern | bestaand zwaar spiritueel cluster | 079 Babaji Cave A; 080 Turiya Niwas A; 081 Bodh Ashram A volgens repo-snapshot | BESTAAND |

## Expliciet te behouden niet-person / laag-person ankers

### 1. Bodh Gaya
Niet alleen relevant via een persoon, maar als wereldhistorische plaats van Boeddha's verlichting. UNESCO noemt Mahabodhi een van de vier heilige plaatsen die direct met het leven van de Boeddha verbonden zijn, specifiek met de verlichting. Het bestaande Mark-besluit maakt dit bovendien projectmatig onmiskenbaar.

Status: **REISBEPALEND BESTAAND ANKER**.

### 2. Sarnath
Plaats van de eerste leerrede; projectmatig al ID 006 A. Person-overlap is hier niet de juiste maatstaf: de kernbetekenis is gebeurtenis-/traditiegedreven.

Status: **REISBEPALEND BESTAAND ANKER**.

### 3. Kushinagar
Plaats geassocieerd met de Mahaparinirvana van de Boeddha. Op de toegestane branch is geen bestaand permanent ID/Mark-A-B-C voor het Kushinagar-cluster aangetroffen in de geraadpleegde canonieke bestaande clusters.

Status: **SIGNALEREN VOOR LATERE ID/A-B-C**, niet nu beslissen.

### 4. Rajgir
Oud Magadha/Buddhist cluster met o.a. Gridhakuta/Vulture Peak, Venuvan en vroege sangha-context. Bihar Tourism behandelt Rajgir/Nalanda als actief Buddhist-circuitgebied; Venuvan wordt daar gekoppeld aan Boeddha en Bimbisara.

Status: **SIGNALEREN VOOR LATERE CLUSTERBEOORDELING**. Niet automatisch toevoegen aan route.

### 5. Nalanda
Archaeological Site of Nalanda Mahavihara is UNESCO Werelderfgoed en een van de belangrijkste historische monastiek-universitaire boeddhistische sites. De repo-snapshot zegt expliciet dat Rajgir/Nalanda eerder nog niet als actieve volgende regio stond; dat is geen inhoudelijke afwijzing en mag niet worden vertaald naar C.

Status: **SIGNALEREN VOOR LATERE CLUSTERBEOORDELING**.

### 6. Haridwar
Uttarakhand Tourism classificeert Haridwar als een van de belangrijkste Hindu-pelgrimsplaatsen, Kumbh-stad en gateway naar Char Dham. Dit is een klassiek voorbeeld van een cluster dat door een Top-person-count te laag kan eindigen ondanks zelfstandige religieuze zwaarte.

Status: **SIGNALEREN / UNION BEHOUDEN**, geen A/B/C toegekend.

### 7. Rishikesh
Uttarakhand Tourism beschrijft Rishikesh als een groot pelgrims- en spiritueel centrum en als 'yoga capital of the world', met talrijke ashrams en meditatiecentra.

Status: **SIGNALEREN / UNION BEHOUDEN**, geen A/B/C toegekend.

## Person-driven clusters die óók zelfstandig clustergewicht hebben

Deze blijven in de union omdat ze in de personlaag sterk zijn én zelfstandig spiritueel/historisch gewicht hebben: Kolkata/Belur/Dakshineswar/Cossipore/Serampore, Puri/Odisha, Tiruvannamalai/Arunachala, Prayagraj/Kumbh, Ranchi/YSS, Kumaon en Varanasi. Hun aanwezigheid in een person-heatmap maakt de non-person laag niet overbodig; het zijn overlappende detectoren.

## Niet als nieuw projectbesluit opgenomen

Grote Indiase pelgrimsplaatsen zoals Amritsar/Golden Temple, Ajmer, Shirdi, Kedarnath/Badrinath, Jain tirthas enz. worden hier **niet automatisch tot Mark-bestemming verheven**. TASK.md vraagt te beginnen bij repo/reisintentie en niet blind heel India opnieuw te onderzoeken. Alleen wanneer een dergelijke plek uit bestaande repo-intentie of een latere gecontroleerde non-person sweep naar voren komt, moet zij als kandidaat naar ID/A-B-C.

## Bronnen

Repo:
- runs/active/BODHGAYA-DISCOVERY-001/MARK_DECISIONS_2026-08-05.jsonl
- runs/active/BODHGAYA-DISCOVERY-001/MARK_DECISIONS_2026-08-08.jsonl
- runs/active/VARANASI-GEO-DELIVERY-REPAIR-001/MARK_DECISIONS_2026-08-02.jsonl
- decisions/ARUNACHALA_TIRUVANNAMALAI_A_ANCHOR_2026-08-18.md
- runs/active/TOP11-INDIA-PERSON-CENTRIC-MEGASWEEP-001/PHASE2_SYNTHESIS.md
- README.md

Actuele externe controle (2026-08-19):
- UNESCO Mahabodhi Temple Complex: https://whc.unesco.org/en/list/1056/
- UNESCO Nalanda Mahavihara: https://whc.unesco.org/en/list/1502/
- Bihar Tourism Nalanda/Rajgir: https://tourism.bihar.gov.in/en/destinations/nalanda
- Uttarakhand Tourism Haridwar: https://www.uttarakhandtourism.gov.in/destination/haridwar
- Uttarakhand Tourism Rishikesh: https://www.uttarakhandtourism.gov.in/destination/rishikesh
