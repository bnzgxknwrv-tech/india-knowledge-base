# BRONS-B01 STARTOPDRACHT

GitHub BRONS-B01:

Activeer onmiddellijk de GitHub-connector en gebruik repository `bnzgxknwrv-tech/india-knowledge-base`.

Test vóór inhoudelijk werk daadwerkelijk GitHub-read en GitHub-write. Ontbreekt een van beide, antwoord uitsluitend exact: `MARK: IK MIS GITHUB CONNECTOR!`

Open:
- `india4/START.md`
- `india4/roles/BRONS.md`
- `runs/active/VARANASI-GEO-DELIVERY-REPAIR-001/RUN.yaml`
- de daarin genoemde kandidaatbron en oude GEO-vergelijkingsbron.

Voer uitsluitend batch `BRONS-B01` uit voor `VNS-CAND-001` t/m `VNS-CAND-010`. Onderzoek geen andere kandidaten.

Pas per kandidaat de GEO-kernregel toe: zoek de volledige kandidaatnaam als openbare Google Maps-zoekopdracht; selecteer alleen de marker die inhoudelijk dezelfde fysieke plaats is; controleer naam en waar nodig wijk, ghat, adres of plaatssoort; neem exact latitude en longitude van die marker over. Gebruik geen schatting, terreinmiddelpunt, oude KML-coördinaat, officieel websitecoördinaat als vervanging of nabijgelegen marker. Kan geen passende openbare Google Maps-marker worden vastgesteld, gebruik `GOOGLE_MAPS_MARKER_NOT_CONFIRMED`, leg kort uit waarom en ga door.

Bescherm Marks keuzes: 001=A, 002=A, 003=A, 007=A, 008=B; overige kandidaten blijven `DOOR_MARK_TE_BEOORDELEN`. Het voor VNS-CAND-008 afgewezen punt `25.3045, 82.979369` mag niet als eindpunt terugkeren.

Schrijf één volledig bestand naar:
`runs/active/VARANASI-GEO-DELIVERY-REPAIR-001/BRONS/BRONS-B01.jsonl`

Gebruik per kandidaat alle velden uit `india4/templates/BATCH_OUTPUT.md`. Voer readback uit en commit. Werk de batchstatus in `RUN.yaml` alleen bij naar COMPLETED wanneer alle tien geldige records aanwezig zijn. Schrijf daarna exact één volledige startvraag voor BRONS-B02 en stop.

Kan de batch niet volledig worden afgerond, schrijf alleen volledig afgeronde records en:
`runs/active/VARANASI-GEO-DELIVERY-REPAIR-001/BRONS/BRONS-B01-PROGRESS.yaml`
met afgeronde candidate_id’s en `next_candidate`. Claim BRONS-B01 dan niet als voltooid en geef exact één hervattingsvraag vanaf `next_candidate`. Onderzoek reeds afgeronde kandidaten niet opnieuw.
