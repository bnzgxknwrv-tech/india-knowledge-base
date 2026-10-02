# TASK.md — INDIA5-ARCH-HARDEN-002

Bron: PR #23, CCI_TASK_ENVELOPE "INDIA5-ARCH-HARDEN-002" (INDIA2, architectuurtaak).
Overgenomen woordelijk uit de PR-comment, hier vastgelegd als canoniek taakbestand.

## Doel

Hard de in INDIA5-ARCH-TEST-001 gebouwde taakarchitectuur af vóór enig inhoudelijk
India-onderzoek. Controleer en herstel de concrete zwakke punten die uit de eerste
end-to-end-test zichtbaar zijn geworden.

## Verplicht onderzoeken en zo nodig repareren

1. `STATUS.yaml` toont na afronding nog `git_commit_at_claim: null` en
   `git_commit_at_complete: null`, terwijl er aantoonbaar claim- en completioncommits
   bestaan. Maak deze velden betrouwbaar en controleerbaar, of documenteer technisch waarom ze
   pas post-commit kunnen worden gevuld en ontwerp een niet-circulaire oplossing.
2. Controleer dat `expected_head` niet onbruikbaar wordt doordat het aanmaken/claimen van de
   taak zelf HEAD wijzigt. Definieer exact welk commitmoment wordt bedoeld en valideer dit
   zonder race of zelfreferentie.
3. Controleer exactly-once-semantiek: één actieve taak maximaal; dezelfde taak kan niet
   tweemaal geclaimd worden; een tweede CCI-sessie kan geen parallelle claim doen; voltooide
   taak kan niet opnieuw uitgevoerd worden.
4. Controleer crashherstel op minimaal vier toestanden: na queue-commit vóór claim; na
   claim-commit vóór uitvoering; na outputs vóór completion; na completion-move vóór
   resultaatcomment.
5. Voeg een expliciete instructieprecedentie toe voor conflicten: canonieke TASK.yaml/TASK.md
   op de bedoelde branch; expliciete HOLD/ABORT-status in taakbestanden; Mark-besluitenregister;
   PR-commenten alleen als envelop/signaal; chattekst en lokale hooks mogen nooit een actieve
   canonieke taak overschrijven.
6. Leg vast dat één regio-opdracht autonoom PRE-BRONS → BRONS → ZILVER → GOUD/TRAVEL kan
   doorlopen. Interne fasen mogen checkpoints hebben, maar Mark start niet iedere fase of batch
   opnieuw.
7. Scheid governance en regio-uitvoering: governance/canonieke architectuur in versiebeheerde
   bestanden; elke toekomstige regio krijgt een eigen run en bij voorkeur eigen PR; PR #23
   blijft Varanasi + architectuurmigratie en wordt niet de eeuwige queue voor alle regio's.
8. Voeg een globale nummeringsvalidator-architectuur toe die vanaf de volgende regio kan
   garanderen dat fysieke locatie-ID's repositorybreed uniek en immutable zijn. Raak de huidige
   001–040 niet aan.
9. Maak een vaste machineleesbare beoordelingsrubriek voor CCI-kennis/capability gates, zodat
   toekomstige vrijgave niet van één lange prose-comment afhangt.
10. Migreer de reeds genomen governancebesluiten uit PR-comments naar canonieke bestanden,
    minimaal: rolverdeling Mark / INDIA2 / CCI; PDF alleen op expliciet verzoek;
    detectorbibliotheek-governance; PRE-BRONS-output en verzadigingsregels; immutable numbering;
    instructieprecedentie; task-file relay in plaats van lange comments.
11. Behandel de bestaande ongecommitte PRE-BRONS/protocolbestanden voorzichtig: inventariseer
    ze; vergelijk ze met de canonieke besluiten; commit ze NIET stil als onderdeel van deze
    hardening tenzij ze uitsluitend noodzakelijk zijn voor de taakarchitectuur; zet inhoudelijke
    PRE-BRONS-wijzigingen apart in een reviewbaar voorstel/resultaatbestand.
12. Voer negatieve tests uit en leg bewijs vast: stale expected_head; dubbele claim; ontbrekende
    completion marker; gewijzigd TASK.md na hashvastlegging; verboden write-path; completed task
    opnieuw claimen; twee queued taken terwijl één active is; afgekapt/ontbrekend taakbestand.

## Verboden

- Geen Varanasi-discoveryonderzoek.
- Geen GEO-onderzoek.
- Geen wijziging aan A/B/C, hotel, KML, PDF of kandidaten 001–040.
- Geen merge van PR #23.
- Geen lange CCI_RESULT-comment; uitgebreid resultaat staat in RESULT.md, comment is alleen
  korte envelop.

## Eindrapport

`RESULT.md` bevat: bevindingen per punt; alle gewijzigde bestanden; testmatrix met PASS/FAIL;
resterende risico's; expliciete uitspraak `ARCHITECTURE_READY_FOR_CONTENT_TASKS: YES/NO`;
voorstel voor de eerstvolgende inhoudelijke taak (niet uitvoeren).
