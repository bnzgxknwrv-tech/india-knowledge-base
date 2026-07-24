# INDIA 4 START — BATCHMODEL

1. Activeer GitHub en test vóór inhoudelijk werk daadwerkelijk read en write voor `bnzgxknwrv-tech/india-knowledge-base`.
2. Ontbreekt read of write, antwoord exact: `MARK: IK MIS GITHUB CONNECTOR!`
3. Open de genoemde `runs/active/<run_id>/RUN.yaml`, het korte rolcontract en uitsluitend de input die voor de eigen batch is genoemd.
4. Iedere chat heeft een harde werklimiet: BRONS maximaal 10 kandidaten; ZILVER maximaal 20 kandidaten; GOUD integreert bestaande batchoutputs.
5. Een batch schrijft één volledig batchbestand, voert readback uit, commit en stopt. Geen controllertransition, SHA-matrix, claimmanager of metadata-herstel.
6. Kan een batch niet volledig worden afgerond, schrijf alleen volledig afgeronde records plus `PROGRESS.yaml` met `next_candidate`; claim de batch niet als voltooid. Een vervolgchat hervat zonder afgeronde kandidaten opnieuw te onderzoeken.
7. Kandidaatgebonden onzekerheid wordt gemarkeerd en blokkeert andere kandidaten niet.
8. Na iedere voltooide stap schrijft de rol exact één volledige startvraag voor de volgende stap. Mark plakt alleen die vraag in een nieuwe chat.
9. Aparte ChatGPT-chats kunnen elkaar niet automatisch starten. GitHub is bron van waarheid, voortgangsopslag en overdrachtskanaal.

Route: BRONS-B01 → BRONS-B02 → BRONS-B03 → BRONS-B04 → ZILVER-Z01 → ZILVER-Z02 → GOUD → KLAAR.
