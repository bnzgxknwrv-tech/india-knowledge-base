# INDIA5 GOUD-PDF-TEMPLATE (VERPLICHT vanaf 2026-08-02)

status: VERPLICHT -- goedgekeurd door Mark op 2026-08-02, vastgelegd in `INDIA5-PROTOCOL.md`
geldigheidsbereik: alle toekomstige GOUD-keuze-PDF's, voor elke stad/regio in INDIA5-PROTOCOL
gebaseerd op: analyse van `VARANASI_40_KEUZE.pdf` (GEO-validatierapport-stijl); eerste toepassing
in `VARANASI_40_KEUZE_REISGIDS.pdf` (runs/active/VARANASI-GEO-DELIVERY-REPAIR-001/GOUD/REGIONAL/USER/)

## Kernprobleem met het huidige formaat

De huidige GOUD-PDF is opgebouwd als GEO-validatierapport: per kandidaat eerst de bevestigingsstatus
(CONFIRMED/PROVISIONAL), dan adres, dan een technische "reason"-tekst uit BRONS/ZILVER, dan pas een
open vraag. Dat is correct als audittrail, maar onbruikbaar als iets waar Mark een middag mee de stad
in kan. Dit template keert de volgorde om: de PDF wordt een reisgids met een klein technisch blok
achteraan, niet andersom.

## Documentstructuur (stad-niveau)

1. **Voorblad**: titel, regio, datum, één zin leeswijzer -- "Dit is een reisgids. Voor de volledige
   geo-validatie, zie GEO_AUDIT.md / CORRECTIERAPPORT.md / BESLISOVERZICHT.md."
2. **Samenvattingstabel** (kort, 1 pagina): aantal kandidaten, hoeveel bevestigd/voorlopig, en een
   mini-legenda van de statusaanduidingen die in de PDF zelf gebruikt worden (geen GEO-jargon, zie
   hieronder).
3. **Kandidaten gegroepeerd per wijk/ghat-cluster, niet op candidate_id-volgorde.** Mark plant een
   bezoek per wijk, niet per interne ID. Binnen elk cluster: kandidaten die letterlijk dicht bij
   elkaar liggen (looproute), ook als hun ruwe `cluster`-veld in de data verschilt -- zie de
   voorbeeldkandidaat hieronder, waar de data-clusters "MANIKARNIKA" / "GHATS_OLD_CITY" /
   "SCINDIA_GHAT" / "VISHWANATH_OLD_CITY" in werkelijkheid een aaneengesloten wandeling langs de
   ghats zijn. GOUD moet dit geografisch groeperen, niet blind het `cluster`-label volgen.
4. **Sluitstuk**: korte verwijzing naar de technische bijlagen (GEO_AUDIT.md, CORRECTIERAPPORT.md,
   BESLISOVERZICHT.md) voor wie de onderbouwing wil zien. Die bijlagen blijven ongewijzigd
   Markdown-documenten, apart van de PDF -- de PDF zelf wordt licht en leesbaar gehouden.

## Kandidaatstructuur (per plek, in deze volgorde)

1. **Titel**: kandidaatnaam + korte pakkende aanduiding tussen haakjes (bestaande
   `recognition_hook`-stijl, bv. "Ratneshwar Mahadev Temple (de scheve tempel van Kashi)").
2. **Waarom hier naartoe?** -- 1-2 zinnen, de emotionele/ervaringsgerichte kern. Geen adres, geen
   GEO-jargon.
3. **Spirituele / historische betekenis** -- kort narratief blok (2-4 zinnen): oorsprong, legende,
   religieuze of historische rol. Geput uit de bestaande BRONS/ZILVER-evidence en reason-teksten,
   herschreven als lopende tekst i.p.v. brontechnische opsomming.
4. **Wat zie je hier?** -- concrete, zintuiglijke beschrijving: architectuur, sfeer, geluid, drukte,
   wat maakt het herkenbaar op straat.
5. **Hoe bijzonder is het?** -- één heldere kwalificerende zin (geen numerieke score): bv. "Uniek in
   Kashi -- er is er maar één van", "Een van de zeven belangrijkste ghats, verwacht drukte", "Klein en
   rustig, weinig toeristen". Dit vervangt de technische CONFIRMED/PROVISIONAL-badge als eerste
   indruk.
6. **Verwachte bezoektijd** -- praktische tijdsindicatie (bv. "15-30 minuten", "reken op een uur rond
   zonsondergang voor de aarti").
7. **Goed te combineren met** -- 2-4 nabijgelegen kandidaten (candidate_id + naam), gebaseerd op
   werkelijke geografische nabijheid (looproute), met één zin waarom ze samen te doen zijn. Gebruik
   bestaande coordinaten (final of old_comparison) om nabijheid te bepalen -- geen nieuw onderzoek.
8. **Praktische tips** -- kleding/schoeisel, drukke/rustige momenten, toegankelijkheid, fotoregels,
   veiligheid -- uitsluitend voor zover al af te leiden uit bestaande evidence/bronnen, anders
   weglaten (geen invulling verzinnen).
9. **Technisch blok (klein, onderaan, visueel duidelijk gescheiden -- klein lettertype/grijs kader)**:
   candidate_id, GEO-status, coordinaat (of "onbevestigd -- indicatief punt"), Mark-keuze
   (A/B/DOOR_MARK_TE_BEOORDELEN), laatste controledatum. Dit is het ENIGE technische onderdeel op
   kandidaatniveau; geen "reason"-tekst, geen brontabel in de hoofd-PDF.

## Wat NIET meer in de hoofd-PDF komt (verplaatst naar de technische bijlagen)

- Volledige BRONS/ZILVER `reason`-tekst woord voor woord.
- Brontabellen met URL's en "supports"-velden.
- ZILVER-controlevelden (`zilver_check`, `nearby_substitute_check`, enz.).
- Statuslabels als hoofdkenmerk (CONFIRMED/PROVISIONAL blijven bestaan, maar uitsluitend in het kleine
  technische blok, niet als eerste regel van de kandidaat).

## Stijlregels

- Nederlands, lopende tekst, geen ambtelijke opsomming van GEO-velden in de hoofdtekst.
- Eén kandidaat = maximaal circa driekwart tot één pagina (korter dan het huidige formaat, dat door de
  volledige reason-tekst en brontabel al snel een halve pagina aan puur technische tekst kostte).
- Kleurgebruik consistent met de KML-conventie (groen=A, oranje=B, neutraal=DOOR_MARK_TE_BEOORDELEN)
  uitsluitend in het technische blok, niet in de reisgids-tekst zelf.
- Geen nieuwe feiten verzinnen: elke uitspraak in de reisgids-secties moet herleidbaar zijn tot
  bestaande BRONS/ZILVER-evidence. Als informatie ontbreekt (bv. exacte bezoektijd, praktische tip),
  wordt het veld weggelaten in plaats van ingevuld met een aanname.

## Invoering

Dit is per 2026-08-02 het VERPLICHTE standaardformaat voor de GOUD-keuze-PDF, voor Varanasi en alle
volgende steden/regio's. De oorspronkelijke Varanasi-PDF (`GOUD/REGIONAL/USER/VARANASI_40_KEUZE.pdf`,
GEO-validatierapport-stijl) blijft voorlopig ter vergelijking bestaan naast de nieuwe
`VARANASI_40_KEUZE_REISGIDS.pdf`; de KML en de onderliggende BRONS/ZILVER-data zijn niet gewijzigd.
Voor elke volgende stad/regio is de reisgids-PDF de ENIGE GOUD-keuze-PDF die wordt opgeleverd.

## Gevolg voor BRONS (verplicht vanaf de volgende sweep)

Om te voorkomen dat GOUD deze reisgidsinhoud achteraf moet reconstrueren (zoals bij Varanasi is
gebeurd), verzamelt BRONS voortaan per kandidaat -- naast de bestaande GEO-onderzoeksvelden --
minimaal:
- een korte, begrijpelijke omschrijving (het "recognition_hook"-veld bestaat al in `candidates.jsonl`
  voor Varanasi; dit wordt voortaan een verplicht BRONS-onderzoeksveld, niet alleen inputmetadata);
- minstens één zin over spirituele/historische betekenis, brononderbouwd;
- minstens één zin over wat er fysiek te zien/ervaren is;
- indien uit de bronnen af te leiden: een uniekheidsopmerking, een indicatie van bezoektijd, en
  praktische toegangsinformatie.
Ontbreekt een van deze punten in de bronnen, dan noteert BRONS expliciet "NOG NIET ONDERZOCHT" in
plaats van dit veld leeg te laten of GOUD dit later te laten verzinnen.
