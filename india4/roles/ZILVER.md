# ZILVER — BATCHCONTRACT

Missie: controleer uitsluitend het kandidaatbereik van de genoemde ZILVER-batch, maximaal twintig kandidaten.

Lees uitsluitend: `india4/START.md`, dit contract, de korte kernprotocollen, de runopdracht en de twee relevante BRONS-batchbestanden.

Controleer per kandidaat:
- is werkelijk een openbare Google Maps-marker gebruikt;
- hoort die marker bij dezelfde fysieke plaats;
- is niet een nabijgelegen organisatie, wijk of gebouw gekozen;
- zijn latitude en longitude exact uit die marker afkomstig;
- is onzekerheid eerlijk gemarkeerd.

Corrigeer fouten met traceerbare reden. Ken geen A/B/C toe en wijzig geen beschermd Mark-besluit.

Output: één volledig ZILVER-JSONL-batchbestand. Bij onvolledige uitvoering daarnaast `PROGRESS.yaml` met `next_candidate`; claim de batch niet als voltooid. Bij volledige uitvoering: readback, commit, batchstatus COMPLETED en exact één complete startvraag voor de volgende stap. Stop daarna.
