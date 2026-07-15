# LONG_RUNNING_EXECUTION_PROTOCOL v1.0

## Doel

Voorkom dat een lange BRONS-, ZILVER- of GOUD-uitvoering onverwacht eindigt, Mark handmatig technisch herstel moet organiseren of reeds verricht onderzoek opnieuw wordt uitgevoerd.

## Kernregel

Een worker behandelt context- of uitvoeringsruimte als een eindige resource. Hij wacht niet tot afbreken onvermijdelijk is. Zodra redelijkerwijs niet meer zeker is dat alle resterende artifacts, heropening, validatie, manifest, COMPLETED, state en events binnen dezelfde sessie kunnen worden afgerond, schakelt hij vóór nieuw inhoudelijk werk over op een gecontroleerd checkpoint.

## Werkblokken

Iedere lange fase wordt uitgevoerd in afzonderlijk afsluitbare werkblokken, bijvoorbeeld:

1. context en predecessorvalidatie;
2. claim en kandidaten-/broninventaris;
3. inhoudelijke onderzoeksblokken;
4. registers en rapportdelen;
5. technische heropening en validatie;
6. completion, state en events.

Na ieder groot werkblok worden alle geschreven bestanden op GitHub opgeslagen. Reeds gevalideerde blokken worden bij hervatting niet opnieuw onderzocht, behalve bij concrete drift, fout of expliciete loss-control-trigger.

## Verplicht checkpoint

Wanneer afronding in dezelfde sessie onzeker wordt, schrijft de worker vóór stoppen:

`research/active/<run-id>/<ROLE>/CHECKPOINT.yaml`

Minimale velden:

- run_id;
- role;
- claim_identity;
- checkpoint_commit;
- completed_blocks;
- validated_files;
- incomplete_blocks;
- exact_next_step;
- files_that_must_be_reopened;
- content_research_must_not_be_repeated;
- created_at;
- status: `RESUME_REQUIRED`.

De worker:

- behoudt de bestaande claim;
- maakt geen tweede claim;
- zet `pipeline/NEXT_ACTION.yaml` op `RESUME_<ROLE>` wanneer write-scope dit toestaat;
- schrijft geen COMPLETED en geen fase-completionevent;
- noemt geen fase `BLOCKED` wanneer alleen een gecontroleerde sessieoverdracht nodig is;
- geeft Mark uitsluitend de standaardstartvraag voor een nieuwe chat.

## Hervatting

Een hervattende worker:

1. test GitHub-read en GitHub-write;
2. leest ENTRYPOINT, NEXT_ACTION, state, events en CHECKPOINT;
3. bevestigt dat dezelfde claim nog actief is;
4. controleert het checkpoint_commit en de genoemde bestanden;
5. maakt geen nieuwe claim;
6. hervat exact bij `exact_next_step`;
7. herhaalt geen afgerond onderzoek zonder concrete fout of drift;
8. verwijdert of archiveert CHECKPOINT pas na geldige fasecompletion.

## Zelfroutering

Bij `RESUME_REQUIRED` toont de chat uitsluitend:

- status: gecontroleerd checkpoint opgeslagen;
- geen werk verloren;
- één standaardstartvraag voor dezelfde rol.

Alle commit-, bestand- en claimdetails blijven in GitHub.

## Beperkingen

Een ChatGPT-chat kan niet zelf een nieuwe chat openen of zichzelf na beëindiging opnieuw activeren. Dit protocol elimineert dubbel onderzoek en technisch uitzoekwerk, maar Mark moet zonder externe orchestrator nog één nieuwe chat openen en de vaste startvraag plakken.

## Proportionaliteit

Dit protocol voegt geen nieuwe onderzoeksfase toe. Het is alleen een runtime-regel voor lange bestaande fasen en mag inhoudelijke voortgang niet vertragen.

END_OF_ARTIFACT