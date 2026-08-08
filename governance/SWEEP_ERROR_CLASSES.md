# FOUTKLASSENREGISTER

Status: **ACTIEF/CANONIEK**, onderdeel van `governance/SWEEP_PROTOCOL.md` (Deel 3). Versie-
onafhankelijke locatie — niet gebonden aan een specifieke regisseursessie. Doel: elke nieuwe,
generaliseerbare fout eerst tegen dit register leggen ("is dit een bekende klasse, of nieuw?") in
plaats van telkens een losse, steeds langere ad-hoc regel te schrijven. Bron van FK-001 t/m
FK-010: de root-cause-tabel in `governance/SWEEP_PROTOCOL.md`, Deel 1, ontstaan tijdens de
Bodh Gaya-sweep.

Bij een nieuwe fout: (1) checken of hij in een bestaande klasse past, zo ja daar de
voorbeelden-kolom aanvullen; (2) zo nee, een nieuwe klasse FK-0NN toevoegen met dezelfde
kolomstructuur; (3) de bijbehorende poort in `governance/SWEEP_PROTOCOL.md` (Deel 2) aanvullen
of, bij een echt nieuw type fout, een nieuwe poort voorstellen.

| Klasse | Naam | Kernpatroon | Voorbeeld (Bodh Gaya) | Preventiepoort |
|---|---|---|---|---|
| FK-001 | Verwachte-uitkomst-filter | Een kandidaat wordt afgewezen (of nooit opgenomen) op basis van een verwachte A/B/C-uitkomst i.p.v. één van de vijf harde uitsluitingsgronden | Vroege CORE_PASS/WATCHLIST-ronde filterde 9 locaties weg op verwachte kans | Poort E (MARK_WAARDIG-gate, verplichte koppeling aan harde grond) |
| FK-002 | Genegeerde saturatiestatus | Een zelf-gerapporteerde `NOT_YET_SATURATED` blokkeert de volgende stap niet automatisch | `SATURATION_REPORT.md` meldde NOT_YET_SATURATED, run ging toch door | Poort C/J (Coverage Matrix + Saturation-gate) |
| FK-003 | Ontbrekend dekkingsplan | Hele categorieën/lenzen blijven onontdekt tot een latere, expliciete heropening, omdat er geen vooraf vastgelegd verplicht dekkingsplan was | Sikhisme, Vuurpreek/post-verlichting, meerdere internationale kloosters, Gaya-stad-hindoeïsme pas laat ontdekt | Poort A (Pre-sweep dekkingsplan) + Poort C (Coverage Matrix) |
| FK-004 | Generieke-kandidaat-nummering | Een kandidaat krijgt een permanent nummer puur op grond van "nog een land/traditie erbij", zonder eigen verhaal | 069 Mongolian Temple; bijna ook 075 Jain Temple | Poort E (expliciete generiek-check vóór nummering) |
| FK-005 | Late identiteitsoplossing | Een identiteits-/dubbelingsvraag tussen twee gelijkende kandidaten wordt pas laat, na expliciete vraag, opgelost | 063 vs. 068; Daijokyo vs. Indosan Nippon; Akshayavat (076) vs. 051; Bakraur vs. Sujata | Poort F (verplichte overlap-scan vóór nummering) |
| FK-006 | Laat-ontdekte toegankelijkheid | Keuze-relevante toegankelijkheid wordt pas laat, soms pas na een correctieronde, onderzocht | Niet-hindoe-toegang bij 051; cursus-only bij 074; sublocatiestatus van 076 | Poort H (verplicht toegankelijkheidsveld vóór GOUD) |
| FK-007 | Claimgewicht-bronmismatch | Een zware historische claim steunt op een lichte bron (foto-caption, wiki zonder bronvermelding), omdat lichte en zware claims dezelfde bronstandaard kregen | Vuurpreek/Gayasisa-identificatie aanvankelijk op Alamy + fandom-wiki | Poort G (claimgewicht-afhankelijke bronregel) |
| FK-008 | Voorspellende A/B/C-taal | Formuleringen die A/B/C voorspellen sluipen in teksten die objectief moeten zijn | "eerder B/C", "A alleen als...", "B goed voorstelbaar" in 050-058-teksten | Poort L (letterlijke verbodslijst + grep-check vóór commit) |
| FK-009 | Impliciete PDF-toestemming | Een taak die naar een PDF-bestandsnaam verwijst wordt gelezen als toestemming om te bouwen, zonder ondubbelzinnig token | PDF twee keer gebouwd zonder expliciete `PDF_GO: JA` | Al ingevoerd: `PDF_STATUS: VERBODEN`/`PDF_GO: JA`-veld in INDIA5-PROTOCOL.md; hier herbevestigd als Poort M/N |
| FK-010 | Niet-auditeerbare saturatieclaim | CCI's eigen `SATURATED=JA` is een vrije-tekstconclusie i.p.v. een controleerbare, itemized matrix, waardoor INDIA herhaald handmatig moet speuren | Berichten 021, 024, 026, 028, 030 — telkens handmatig gaten gevonden door INDIA6 | Poort J (evidence-matrix) + Poort K (INDIA_ACCEPTED_SATURATION: JA) |

---
Geschreven door: CCI, geactiveerd na protocolreview (PR #23), als Deel 3-bijlage bij
`governance/SWEEP_PROTOCOL.md`. Geen PDF, geen nieuwe regionale sweep, geen A/B/C,
geen route/pacing. `PDF_STATUS: VERBODEN` gerespecteerd.
