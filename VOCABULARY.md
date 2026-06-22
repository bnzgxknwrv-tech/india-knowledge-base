# VOCABULARY - Gecontroleerde woordenlijsten

Deze woordenlijsten gelden voor de aangegeven velden in alle records. Een veld met een gecontroleerde
lijst mag uitsluitend waarden uit die lijst bevatten. Nieuwe waarden worden nooit zomaar toegevoegd:
een kunstmatig intelligentiesysteem stelt een nieuwe waarde voor via een AUDIT-record, en alleen Mark
voegt hem toe via een DECISION-record. Pas daarna mag de waarde in records gebruikt worden.

## type  (PLACE - lijst toegestaan; een plek kan meerdere typen stapelen)
- grot - een grot
- samadhi - samadhi-, mahasamadhi- of as-plek van een meester
- ashram - ashram of math, een levende spirituele gemeenschap
- tempel - tempel
- woonhuis - woonhuis of geboorteplaats van een meester
- ghat - oever- of crematieghat
- gebeurtenisplek - plek van een specifieke gebeurtenis (verschijning, inwijding) die niet in bovenstaande vormen valt

## axis  (PLACE - lijst toegestaan; een plek kan meerdere lijnen raken)
- kriya-lijn - Babaji, Lahiri Mahasaya, Sri Yukteswar, Yogananda, de AOAY-meesters en de bredere Lahiri-Kriya-lijn
- persoonlijke-brug - Ram Dass, Neem Karoli Baba, Shri Mataji Nirmala Devi
- grote-magneet - grote heiligen buiten de eigen lijn (Boeddha, Vivekananda, Ramakrishna, Anandamayi Ma)

Let op: axis registreert uitsluitend tot welke lijn(en) een plek feitelijk behoort. Prioriteit of
voorkeur wordt hier niet vastgelegd; dat doet alleen Mark via een DECISION-record.

## visitable  (PLACE - enkele waarde) - de harde bezoekbaarheidspoort van regel 10
- yes - er bestaat een fysieke plek die te bereiken is
- no - geen aanwijsbare of bereikbare fysieke plek; in strijd met regel 10, moet een AUDIT-record openen
- unknown - nog niet vastgesteld

## access  (PLACE - lijst toegestaan) - de toegangsnuance die visitable niet kan dragen
- open - vrij toegankelijk voor het publiek
- restricted - toegang beperkt (alleen leden, vergunning, niet-hindoes geweerd); detail in de prozasectie Toegang
- seasonal - toegang hangt af van tijd van het jaar of vaste data (bijvoorbeeld alleen op Guru Purnima, of winterkou); detail in de prozasectie Toegang
- unknown - nog niet geverifieerd

## reliability  (SOURCE - enkele waarde) - evidentieel gewicht
- primair - primaire traditiebron (bijvoorbeeld Autobiography of a Yogi, eigen geschriften van een meester)
- lijn-organisatie - officiele organisatie binnen de lijn; gezaghebbend over feiten en toegang, maar belanghebbend
- secundair - onafhankelijke secundaire bron (wetenschap, journalistiek, naslagwerk)
- devotioneel - devotionele of gemeenschapsbron (blogs, hagiografie); weinig onafhankelijke verificatie
- onbevestigd - bewering zonder solide bron
