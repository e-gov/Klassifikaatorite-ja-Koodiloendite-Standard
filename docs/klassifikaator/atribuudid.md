# Klassifikaatorite kirjeldamine

Klassifikaatori kirjeldamisel lähtutakse Statistikaameti klassifikaatorite kirjeldamise juhistest ja DDI Lifecycle 3.3 klassifikaatorite mudelist. Standard kirjeldab, millised klassifikaatori objektid ja atribuudid tuleb esitada.

| Standardi osa | DDI objekt |
|---|---|
| Klassifikaatori perekond | `ClassificationFamily` |
| Klassifikaatorite sari | `ClassificationSeries` |
| Statistiline klassifikaator | `StatisticalClassification` |
| Klassifikaatori tase | `ClassificationLevel` |
| Klassifikaatori element | `ClassificationItem` |
| Vastavustabel | `ClassificationCorrespondenceTable` |
| Klassifikaatori indeks | `ClassificationIndex` |

## 1. Klassifikaatori perekond
DDI viide: [ClassificationFamily](https://docs.ddialliance.org/DDI-Lifecycle/3.3/model/item-types/ClassificationFamily/)

Klassifikaatori valdkond/perekond on teatud ühise tunnuse alusel koondatud rühm klassifikaatorite sarju. Statistiliste klassifikaatorite perekonna aluseks on ühendav mõiste (nt majandustegevus). Kuna ühtset kokkulepitud klassifikaatorite liigitust ei ole, võivad erinevates andmebaasides olla valdkonnad/perekonnad liigitatud erinevatel alustel ja kanda erinevaid nimetusi. Klassifikaatorite sarju ei pea koondama valdkondadeks, kuid see hõlbustab nii nende haldamist kui ka kasutamist, mh annab infot, millised klassifikaatorid on mingil viisil omavahel seotud.

| # | Atribuudi nimetus | Määratlus | Kohustuslik | Välja tüüp | Mitmesus | Näide |
|---|---|---|---|---|---|---|
| 1 | Tähis (Name) | Klassifikaatori valdkonna unikaalne identifikaator, (lühi)nimi, enamasti lühend nimetusest | Ei | [NameType](https://docs.ddialliance.org/DDI-Lifecycle/3.3/model/composite-types/NameType/) | 0..n | „Geograafia“ valdkonna tähis võib olla „Geo“ vmt |
| 2 | Nimetus (Label) | Valdkonna/perekonna nimetus, mille määrab perekonna/valdkonna haldaja/omanik | **Jah** | [LabelType](https://docs.ddialliance.org/DDI-Lifecycle/3.3/model/composite-types/LabelType/) | 0..n | TOOTED; HARIDUS; AMETID |
| 3 | Kirjeldus (Description) | Klassifikaatori valdkonna sisu ja loomise või kasutamise eesmärki kokku võttev kirjeldus | **Jah** | [StructuredStringType](https://docs.ddialliance.org/DDI-Lifecycle/3.3/model/composite-types/StructuredStringType/) | 0..1 | Klassifikaatorite perekond TOOTED sisaldab klassifikaatoreid, mille alusel liigitatakse tooteid ja teenuseid, arvutatakse ekspordi-, impordi- ja tarbijahinnaindeksit ning kaupade ja teenuste väliskaubanduse näitajaid. |
| 4 | Klassifikaatorite sarjad (ClassificationSeriesReference) | Viide valdkonda kuuluva(te)le klassifikaatori(te) sarja(de)le | **Jah** | [ClassificationSeries](https://docs.ddialliance.org/DDI-Lifecycle/3.3/model/item-types/ClassificationSeries/) | 0..n | Nt Statistikaameti klassifikaatorite perekonda TOOTED kuuluvad järgmised klassifikaatorid: Kombineeritud nomenklatuur; maksebilansi laiendatud teenuste klassifikaator; majanduslike põhikategooriate klassifikaator; standardne väliskaubanduse klassifikaator; toodete ja teenuste klassifikaator; tööstustoodete loetelu; tööstustoodete nimistu; teenuste väliskaubandus |

## 2. Klassifikaatorite sari
DDI viide: [ClassificationSeries](https://docs.ddialliance.org/DDI-Lifecycle/3.3/model/item-types/ClassificationSeries/)

Sama klassifikaatori versioonid moodustavad sarja. Sarja kuuluvatel klassifikaatori versioonidel on üldjuhul sama nimetus, nt Eesti haldus- ja asustusjaotuse klassifikaator (EHAK). 

| # | Atribuudi nimetus | Määratlus | Kohustuslik | Välja tüüp | Mitmesus | Näide |
|---|---|---|---|---|---|---|
| 1 | Tähis (Name) | Klassifikaatori sarja tähis või lühinimi, tavaliselt lühend sarja nimetusest. Tähis võib koosneda tähtedest, numbritest või olla nende kombinatsioon. | **Jah** | [NameType](https://docs.ddialliance.org/DDI-Lifecycle/3.3/model/composite-types/NameType/) | 0..n | AK |
| 2 | Nimetus (Label) | Klassifikaatori sarja nimetus, mille määrab klassifikaatori haldaja või omanik. | **Jah** | [LabelType](https://docs.ddialliance.org/DDI-Lifecycle/3.3/model/composite-types/LabelType/) | 0..n | Ametite klassifikaator |
| 3 | Kirjeldus (Description) | Sarja üldine lühiseloomustus, mis sisaldab eesmärki, peamist valdkonda, ülevaadet struktuurist ja seotud klassifikaatoritest. | **Jah** | [StructuredStringType](https://docs.ddialliance.org/DDI-Lifecycle/3.3/model/composite-types/StructuredStringType/) | 0..1 | „Ametite klassifikaator“ (AK) on Eesti-sisene klassifikaator, mis põhineb Rahvusvahelise Tööorganisatsiooni (ILO) hallataval klassifikaatoril International Standard Classification of Occupations ISCO-08. Klassifikaatorit kasutatakse selleks, et esitada, võrrelda ja vahetada statistilisi ja administratiivandmeid nii Eestis, Euroopa Liidus kui ka laiemal rahvusvahelisel tasemel. |
| 4 | Kontekst (SeriesContext) | Loomis- ja kasutuskonteksti kirjeldus, nt kas tegemist on Eesti-sisese, rahvusvahelise või muu klassifikaatoriga; viide õiguslikule alusele, standardile või alusdokumendile juhul, kui see on olemas. | Ei | [CodeValueType](https://docs.ddialliance.org/DDI-Lifecycle/3.3/model/composite-types/CodeValueType/) | 0..1 | Eesti-sisene klassifikaator, mis põhineb rahvusvahelisel ISCO klassifikaatoril. |
| 5 | Teema (SubjectArea) | Tegevusvaldkond või valdkonnad, kus klassifikaatorit rakendatakse. | Ei | [CodeValueType](https://docs.ddialliance.org/DDI-Lifecycle/3.3/model/composite-types/CodeValueType/) | 0..n | Tööturg; ametid; statistika; administratiivandmed |
| 6 | Sarja kuuluvad klassifikaatorid (StatisticalClassificationReference) | Viide sarja kuuluvatele klassifikaatoritele. Tavaliselt on kehtiv klassifikaator sarja kuuluvate klassifikaatorite loetelus esimesel kohal ja klassifikaatorid esitatakse ajaliselt kahanevas järjestuses. | **Jah** | [StatisticalClassification](https://docs.ddialliance.org/DDI-Lifecycle/3.3/model/item-types/StatisticalClassification/) | 0..n | Ametite klassifikaator 2008; Ametite klassifikaator 1999 |
| 7 | Kehtiv versioon (CurrentStatisticalClassificationReference) | Viide hetkel kehtivale klassifikaatori versioonile. Viide kehtivale klassifikaatori versioonile võib olla toodud ka eraldi väljal või tähisena selle nimetuse juures. | **Jah** | [StatisticalClassification](https://docs.ddialliance.org/DDI-Lifecycle/3.3/model/item-types/StatisticalClassification/) | 0..1 | Ametite klassifikaator 2008 |
| 8 | Omanik (OwnerReference) | Viide organisatsioonile, kes vastutab sarja kuuluvate klassifikaatorite koostamise ja haldamise eest. | **Jah** | [Agent](https://docs.ddialliance.org/DDI-Lifecycle/3.3/model/topics/Agent/) | 0..n | Statistikaamet |
| 9 | Kontaktandmed (ContactPersonReference) | Sarja omaniku või haldaja kontaktandmed. | **Jah** | [Agent](https://docs.ddialliance.org/DDI-Lifecycle/3.3/model/topics/Agent/) | 0..n | klassifikaatorid@stat.ee |

## 3. Statistiline klassifikaator

DDI: [StatisticalClassification](https://docs.ddialliance.org/DDI-Lifecycle/3.3/model/item-types/StatisticalClassification/)

Statistiline klassifikaator on konkreetne klassifikaator või klassifikaatori versioon, mis kuulub klassifikaatorite sarja. See kirjeldab klassifikaatori tähist, nimetust, kehtivust, õiguslikku alust, seoseid teiste klassifikaatoritega, tasemeid, avaldamist, keeli, haldust ja versioonidega seotud muudatusi.

| # | Atribuudi nimetus | Määratlus | Kohustuslik | Välja tüüp | Mitmesus | Näide |
|---|---|---|---|---|---|---|
| 1 | Tähis (Name) | Klassifikaatoril on unikaalne tähis, mis tavaliselt on lühend nimetusest. Sageli eristatakse ühe sarja eri klassifikaatoreid kas versiooni numbri või kehtima hakkamise aastaarvuga. Kui klassifikaatori versioon muutub ühes aastas mitu korda, lisatakse ka versiooni järjekorranumber. Hea tava on tähises tühikuid mitte kasutada. | **Jah** | [NameType](https://docs.ddialliance.org/DDI-Lifecycle/3.3/model/composite-types/NameType/) | 0..n | AK2008ap; EHAK2023v1 |
| 2 | Nimetus (Label) | Klassifikaatori nimetus, mille määrab omanik või haldaja. | **Jah** | [LabelType](https://docs.ddialliance.org/DDI-Lifecycle/3.3/model/composite-types/LabelType/) | 0..n | Eesti haldus- ja asustusjaotuse klassifikaator 2017 aegpidev; Eesti majanduse tegevusalade klassifikaator |
| 3 | Kirjeldus (Description) | Klassifikaatori versiooni lühiiseloomustus. | **Jah** | [StructuredStringType](https://docs.ddialliance.org/DDI-Lifecycle/3.3/model/composite-types/StructuredStringType/) | 0..1 | Ametite klassifikaatoris on ametid liigitatud selgelt määratletud rühmadesse töö sisu, tööga seotud ülesannete ja nõutava kvalifikatsiooni alusel. Klassifikaator on 5-tasemelise hierarhiaga. |
| 4 | Kehtivus (IsCurrent) | Viide, kas klassifikaatori versioon on hetkel kehtiv. | **Jah** | `boolean` | 0..1 | Jah |
| 5 | Kehtiv alates (ReleaseDate) | Kuupäev, millest alates on klassifikaatori versioon kehtiv. | **Jah** | `cogsDate` | 0..1 | 2017-12-01 |
| 6 | Kehtiv kuni (TerminationDate) | Klassifikaatori kehtivuse viimane kuupäev. Kohustuslik juhul, kui klassifikaatori versioon on kehtetu. | Ei | `cogsDate` | 0..1 |  |
| 7 | Õiguslik alus (LegalBase) | Viide, millise õigusaktiga või muu kokkuleppega on klassifikaator või selle versioon kinnitatud või mille alusel loodud. | **Jah** | [StructuredStringType](https://docs.ddialliance.org/DDI-Lifecycle/3.3/model/composite-types/StructuredStringType/) | 0..n | EHAK alus – Riigihalduse ministri määrus „Asustusüksuste nimistu kinnitamine ning nende lahkmejoonte määramine“ ning link dokumendile Riigi Teatajas. |
| 8 | Autoriõigus (Copyright) | Klassifikaatoril võivad olla piiratud autoriõigused, näiteks ei ole neid võimalik alla laadida. Ametlikes väljaannetes tuleb viidata autoriõiguste omanikule. | Ei | [InternationalStringType](https://docs.ddialliance.org/DDI-Lifecycle/3.3/model/composite-types/InternationalStringType/) | 0..1 |  |
| 9 | Avaldamine (Publication) | Viide dokumendile, veebilehele või muule väljaandele, kus klassifikaator on avaldatud. | Ei | [PublicationType](https://docs.ddialliance.org/DDI-Lifecycle/3.3/model/composite-types/PublicationType/) | 0..n | Kui klassifikaatori haldamine ja avaldamine toimub erinevates keskkondades, siis viide veebilehele, kus klassifikaator on leitav. |
| 10 | Levitamine on lubatud (IsDisseminationAllowed) | Näitab, kas klassifikaatorit tohib avaldada elektrooniliselt, trükitult või muul viisil. | Ei | `boolean` | 0..1 | Jah |
| 11 | Keeled (LanguagesAvailable) | Loetelu keeltest, milles klassifikaatorit on võimalik kasutada. Klassifikaator võib olla paralleelselt ühes või mitmes keeles. Mitmekeelse klassifikaatori korral peaksid olema tõlgitud kõik selle elemendid. | **Jah** | [StructuredStringType](https://docs.ddialliance.org/DDI-Lifecycle/3.3/model/composite-types/StructuredStringType/) | 0..1 | eesti; inglise |
| 12 | Klassifikaatori sari (ClassificationSeriesReference) | Viide sarjale, kuhu antud klassifikaatori versioon kuulub. | **Jah** | [StatisticalClassification](https://docs.ddialliance.org/DDI-Lifecycle/3.3/model/item-types/StatisticalClassification/) | 0..1 | AK |
| 13 | Tasemed (LevelContext) | Klassifikaatori struktuuri määravad selle tasemed. Tasemete kirjeldus või link kohale, kus klassifikaatori tasemed on kirjeldatud. | **Jah** | [LevelContextType](https://docs.ddialliance.org/DDI-Lifecycle/3.3/model/composite-types/LevelContextType/) | 0..n | 1 AK pearühm – 1-kohaline kood; 2 AK allpearühm – 2-kohaline kood; 3 AK allrühm – 3-kohaline kood; 4 AK ametirühm – 4-kohaline kood; 5 AK ametinimetus – 8-kohaline kood |
| 14 | Eelnev klassifikaator (PredecessorReference) | Nende klassifikaatorite puhul, mis on versioonid või uuendused, viide eelnevale klassifikaatorile või versioonile, mille järglane antud klassifikaator on. | Ei | [StatisticalClassification](https://docs.ddialliance.org/DDI-Lifecycle/3.3/model/item-types/StatisticalClassification/) | 0..1 |  |
| 15 | Järgnev klassifikaator (SuccessorReference) | Nende klassifikaatorite puhul, mis on versioonid või uuendused, viide järgmisele kehtivale klassifikaatorile või selle versioonile. | Ei | [StatisticalClassification](https://docs.ddialliance.org/DDI-Lifecycle/3.3/model/item-types/StatisticalClassification/) | 0..1 |  |
| 16 | Lähteklassifikaator (DerivedFromReference) | Näitab klassifikaatori versiooni, millest antud klassifikaator on tuletatud. Klassifikaator võib lähtuda mõnda teise sarja kuuluvast klassifikaatorist. Üle võib olla võetud teise klassifikaatori struktuur, millele võib olla lisatud detailsemaid tasemeid, või kasutatakse teise klassifikaatori elemente. | Ei | [StatisticalClassification](https://docs.ddialliance.org/DDI-Lifecycle/3.3/model/item-types/StatisticalClassification/) | 0..1 | Rahvusvaheline ametite klassifikaator ISCO-08 |
| 17 | Muudatused võrreldes eelmise versiooni või uuendusega (ChangesFromPreceding) | Kokkuvõte muudatuste olemusest või sisust võrreldes eelmise versiooni või uuendusega. | Ei | [StructuredStringType](https://docs.ddialliance.org/DDI-Lifecycle/3.3/model/composite-types/StructuredStringType/) | 0..1 |  |
| 18 | Lisamaterjalid (RelatedOtherMaterialReference) | Viide lisamaterjalidele, näiteks failidele kas klassifikaatori enda või selgitavate märkustega. | Ei | [OtherMaterial](https://docs.ddialliance.org/DDI-Lifecycle/3.3/model/item-types/OtherMaterial/) | 0..n | Klassifikaator .xlsx-failina |
| 19 | Versioon (IsVersion) | Viide, kas klassifikaator on versioon. | Ei | `boolean` | 0..1 |  |
| 20 | Aegpidevus (IsFloating) | Viide, kas klassifikaator on aegpidev. | Ei | `boolean` | 0..1 | Jah |
| 21 | Uuendus (IsUpdate) | Viide, kas klassifikaator on uuendus. | Ei | `boolean` | 0..1 | Ei |
| 22 | Uuendused on lubatud (UpdatesAllowed) | Viide, kas klassifikaatori versioonis on lubatud teha uuendusi ilma uut versiooni loomata. | Ei | `boolean` | 0..1 | Jah |
| 23 | Lubatavad uuendused (PermissibleUpdates) | Kirjeldus selle kohta, missugused muudatused on lubatud versiooni sees nii, et klassifikaatorist ei looda uut versiooni. Näiteks aegpideva klassifikaatori korral viide, et klassifikaatorisse on lubatud lisada uusi elemente ning kas neid saab uuesti kehtivaks või kehtetuks tunnistada. | Ei | [StructuredStringType](https://docs.ddialliance.org/DDI-Lifecycle/3.3/model/composite-types/StructuredStringType/) | 0..1 |  |
| 24 | Uuendused (Updates) | Pärast viimase klassifikaatori versiooni või klassifikaatori uuenduse jõustumist toimunud muudatuste kokkuvõtlik kirjeldus. | Ei | [StructuredStringType](https://docs.ddialliance.org/DDI-Lifecycle/3.3/model/composite-types/StructuredStringType/) | 0..1 |  |
| 25 | Alusklassifikaator (VariantOfReference) | Nende klassifikaatorite puhul, mis on variandid, viide klassifikaatorile, mille variandiks see on, ning järgmistele selle klassifikaatori versioonidele, mille kohta see on samuti kehtiv. | Ei | [StatisticalClassification](https://docs.ddialliance.org/DDI-Lifecycle/3.3/model/item-types/StatisticalClassification/) | 0..1 |  |
| 26 | Muudatused võrreldes baasklassifikaatoriga (VariantChangesFromBase) | Klassifikaatori variandis alusklassifikaatoriga võrreldes tehtud muudatused, variandi ja baasklassifikaatori vahelist seost, sh rühmitamiste, lisatud koondavate või laiendavate elementide kirjeldus. | Ei | [StructuredStringType](https://docs.ddialliance.org/DDI-Lifecycle/3.3/model/composite-types/StructuredStringType/) | 0..1 |  |
| 27 | Variandi loomise põhjus (VariantPurpose) | Kui klassifikaator on variant, siis kirjeldatakse selle loomise põhjus. | Ei | [StructuredStringType](https://docs.ddialliance.org/DDI-Lifecycle/3.3/model/composite-types/StructuredStringType/) | 0..1 |  |
| 28 | Haldaja (MaintenanceUnitReference) | Organisatsioon või üksus, kes vastutab klassifikaatori haldamise, st selle uuendamise ja muutmise eest. | **Jah** | [Agent](https://docs.ddialliance.org/DDI-Lifecycle/3.3/model/topics/Agent/) | 0..n | Statistikaamet |
| 29 | Kontaktandmed (ContactPersonReference) | Haldaja kontaktandmed täiendava info saamiseks klassifikaatori kohta. | **Jah** | [Agent](https://docs.ddialliance.org/DDI-Lifecycle/3.3/model/topics/Agent/) | 0..n | klassifikaatorid@stat.ee |

## 4. Klassifikaatori tase

DDI: [ClassificationLevel](https://docs.ddialliance.org/DDI-Lifecycle/3.3/model/item-types/ClassificationLevel/)

Klassifikaatoril on struktuur, mis koosneb ühest või mitmest tasemest. Tase seostatakse sageli mõistega, mis seda defineerib. Hierarhilises klassifikaatoris rühmitatakse iga taseme klassifikaatori elemendid, välja arvatud kõrgeima taseme elemendid, lähima kõrgema taseme alla. Lineaarsel klassifikaatoril on ainult üks tase.

| # | Atribuudi nimetus | Määratlus | Kohustuslik | Välja tüüp | Mitmesus | Näide |
|---|---|---|---|---|---|---|
| 1 | Tähis (Name) | Taseme tähis või lühinimi. | Ei | [NameType](https://docs.ddialliance.org/DDI-Lifecycle/3.3/model/composite-types/NameType/) | 0..n | `maakond`; `pearühm`; `ametirühm` |
| 2 | Nimetus (Label) | Taseme nimetus, mis kuvatakse kasutajale. | **Jah** | [LabelType](https://docs.ddialliance.org/DDI-Lifecycle/3.3/model/composite-types/LabelType/) | 0..n | EHAK maakond; AK pearühm; AK ametirühm |
| 3 | Kirjeldus (Description) | Taseme sisu ja eesmärgi kirjeldus. Siin ei dubleerita koodi struktuuri, vaid selgitatakse, mida vastav tase klassifikaatoris tähistab. | Ei | [StructuredStringType](https://docs.ddialliance.org/DDI-Lifecycle/3.3/model/composite-types/StructuredStringType/) | 0..n | Tase kirjeldab EHAK klassifikaatoris maakonda. |
| 4 | Taseme koodi tüüp (LevelCodeType) | Näitab, kas taseme kood on täheline, numbriline või tähtnumbriline. Toetab välise kontrollsõnastiku kasutamist. | Ei | [CodeValueType](https://docs.ddialliance.org/DDI-Lifecycle/3.3/model/composite-types/CodeValueType/) | 0..1 | numberkood araabia numbritega; tähtkood; tähtnumberkood |
| 5 | Taseme koodi struktuur (LevelCodeStructure) | Näitab, mitmekohaline kood on ning kuidas taseme kood koosneb numbritest, tähtedest ja eraldajatest. Toetab välise kontrollsõnastiku kasutamist. | Ei | [CodeValueType](https://docs.ddialliance.org/DDI-Lifecycle/3.3/model/composite-types/CodeValueType/) | 0..1 | 4-kohaline numberkood; 2-kohaline tähtkood; 3-kohaline punktiga eraldatud numberkood |
| 6 | Fiktiivne kood (DummyCode) | Reegel fiktiivsete koodide konstrueerimiseks järgmise kõrgema taseme koodidest. Kasutatakse juhul, kui üks või mitu elementi on kahel järjestikusel tasemel samad või kui klassifikaatori struktuuri korrektseks kuvamiseks on vaja tehnilist koodi. | Ei | [StructuredStringType](https://docs.ddialliance.org/DDI-Lifecycle/3.3/model/composite-types/StructuredStringType/) | 0..n | KN-is on vahepealkirju, millel puuduvad koodid; portaali korrektseks kuvamiseks lisatakse neile fiktiivsed koodid, mida andmekogumise rakendustes ei tohi valida. |
| 7 | Mõiste määratlemine (DefiningConceptReference) | Viide mõistele, mis kirjeldab või defineerib klassifikaatori taset. | Ei | [Concept](https://docs.ddialliance.org/DDI-Lifecycle/3.3/model/item-types/Concept/) | 0..n | Maakond; ametirühm; tegevusala |

## 5. Klassifikaatori element

DDI: [ClassificationItem](https://docs.ddialliance.org/DDI-Lifecycle/3.3/model/item-types/ClassificationItem/)

Klassifikaatori element tähistab kategooriat klassifikaatori teatud tasemel ning määratleb kategooria sisu ja piirid. Objekti või üksuse saab klassifitseerida ühe ja ainult ühe klassifikaatori elemendi alla igal klassifikaatori tasemel. Kasutatakse ka mõistet „kategooria“.

### 5.1. Klassifikaatori elemendi atribuudid

| # | Atribuudi nimetus | Määratlus | Kohustuslik | Välja tüüp | Mitmesus | Näide |
|---|---|---|---|---|---|---|
| 1 | Tähis (Name) | Klassifikaatori elemendi tähis või lühinimi. Üldjuhul ei kirjeldata, sest elementi tähistab väärtus/kood. | Ei | [NameType](https://docs.ddialliance.org/DDI-Lifecycle/3.3/model/composite-types/NameType/) | 0..n |  |
| 2 | Nimetus (Label) | Klassifikaatori elemendi või kategooria nimetus, mis kuvatakse kasutajale. | **Jah** | [LabelType](https://docs.ddialliance.org/DDI-Lifecycle/3.3/model/composite-types/LabelType/) | 0..n | Elamute ja mitteeluhoonete ehitus |
| 3 | Kirjeldus (Description) | Klassifikaatori elemendi sisu ja eesmärgi kirjeldus. | Ei | [StructuredStringType](https://docs.ddialliance.org/DDI-Lifecycle/3.3/model/composite-types/StructuredStringType/) | 0..1 | Siia klassi kuuluvad elamute või mitteeluhoonete ehitamine ning juurde- ja ümberehitustööd. |
| 4 | Väärtus (ItemCode / Value) | Klassifikaatori elementi tähistav täht-, number- või tähtnumbriline kood, mis on kooskõlas taseme koodistruktuuriga. Kood on unikaalne selles klassifikaatoris, millesse klassifikaatori element kuulub. | **Jah** | `string` | 0..1 | 41.00 |
| 5 | Siia kuulub (Includes) | Klassifikaatori elemendi või kategooria sisu täpsustus. | Ei | [StructuredStringType](https://docs.ddialliance.org/DDI-Lifecycle/3.3/model/composite-types/StructuredStringType/) | 0..1 |  |
| 6 | Siia kuulub ka (IncludesAlso) | Kirjeldatud kategooriasse kuuluvate piiripealsete juhtumite loetelu. | Ei | [StructuredStringType](https://docs.ddialliance.org/DDI-Lifecycle/3.3/model/composite-types/StructuredStringType/) | 0..1 | Siia klassi kuulub ka olemasolevate elamute või mitteeluhoonete täielik ümberehitus või renoveerimine. |
| 7 | Välja arvatud (Excludes) | Kirjeldatud kategooriasse mittekuuluvate juhtumite loetelu. Võib sisaldada viidet klassifikaatori elemendile, kuhu vastavad juhtumid liigitatakse. | Ei | [StructuredStringType](https://docs.ddialliance.org/DDI-Lifecycle/3.3/model/composite-types/StructuredStringType/) | 0..1 | Siia klassi ei kuulu tööstusrajatiste, v.a hoonete ehitamine; ehitusprojektide arendamine; arhitektuuri- ja insenertegevus. |
| 8 | Tuleviku sündmused (FutureEvents) | Kehtetu klassifikaatori elemendiga seotud tulevaste muudatuste kirjeldus. Üldjuhul ei kirjeldata. | Ei | [StructuredStringType](https://docs.ddialliance.org/DDI-Lifecycle/3.3/model/composite-types/StructuredStringType/) | 0..1 |  |
| 9 | Muudatused eelnevast versioonist (ChangesFromPriorVersion) | Kirjeldab muudatusi, mille suhtes klassifikaatori element on võrreldes eelmise versiooniga muutunud. Üldjuhul ei kirjeldata. | Ei | [StructuredStringType](https://docs.ddialliance.org/DDI-Lifecycle/3.3/model/composite-types/StructuredStringType/) | 0..1 |  |
| 10 | Uuendused (Updates) | Kirjeldab muudatusi, mis on klassifikaatori kehtivusajal klassifikaatori elemendiga tehtud. Üldjuhul ei kirjeldata. | Ei | [StructuredStringType](https://docs.ddialliance.org/DDI-Lifecycle/3.3/model/composite-types/StructuredStringType/) | 0..1 |  |
| 11 | Kehtiv alates (ValidFrom) | Klassifikaatori elemendi kehtivuse alguse kuupäev. Kuupäev tuleb määratleda, kui klassifikaatori element kuulub aegpidevasse klassifikaatorisse. | Tingimuslik | `cogsDate` | 0..1 | 2017-12-01 |
| 12 | Kehtiv kuni (ValidTo) | Klassifikaatori elemendi kehtetuks tunnistamise kuupäev. Kuupäev tuleb määratleda, kui klassifikaatori element kuulub aegpidevasse klassifikaatorisse ja see ei ole enam kehtiv. | Tingimuslik | `cogsDate` | 0..1 | 2023-12-31 |
| 13 | On genereeritud (IsGenerated) | Märkeruut, mida kasutatakse juhul, kui klassifikaatorisse on struktuuri hoidmiseks lisatud koode madalamale tasemele. Kasutatakse näiteks `dummy` koodide puhul. | Ei | `boolean` | 0..1 | Jah |
| 14 | On kehtiv (IsValid) | Märkeruut, mis näitab, kas klassifikaatori element on hetkel kehtiv. | Automaatne | `boolean` | 0..1 | Jah |

### 5.2. Viited

| # | Atribuudi nimetus | Määratlus | Kohustuslik | Välja tüüp | Mitmesus | Näide |
|---|---|---|---|---|---|---|
| 1 | Vanemelement (ParentClassificationItemReference / Parent) | Viide vanemelemendile. Kirjeldatakse objektitüübis „Klassifikaatori element“. Kui laadimisfailis on emakood määratud, tekib viide automaatselt. | Automaatne | [ClassificationItem](https://docs.ddialliance.org/DDI-Lifecycle/3.3/model/item-types/ClassificationItem/) | 0..1 | Lääne-Harju vald kui Keila-Joa aleviku vanemelement |
| 2 | Määrav mõiste (DefiningConceptReference / Defining Concept) | Viide mõistele, mis kirjeldab või defineerib klassifikaatori elementi. Mõiste kirjeldatakse objektitüübis „Mõiste“. | Ei | [Concept](https://docs.ddialliance.org/DDI-Lifecycle/3.3/model/item-types/Concept/) | 0..n | Alevik |
| 3 | Välistatud elemendid (ExcludedClassificationItemReference / Excludes) | Viide välistatud elementidele. Kirjeldatakse objektitüübis „Klassifikaatori element“. | Ei | [ClassificationItem](https://docs.ddialliance.org/DDI-Lifecycle/3.3/model/item-types/ClassificationItem/) | 0..n | Viide elemendile, kuhu välistatud juhtum liigitatakse |
| 4 | Järgnev element (SuccessorClassificationItemReference / Successor) | Viide ajaliselt järgnevale elemendile. Kirjeldatakse objektitüübis „Klassifikaatori element“. | Ei | [ClassificationItem](https://docs.ddialliance.org/DDI-Lifecycle/3.3/model/item-types/ClassificationItem/) | 0..n | Kehtetu elemendi asendanud uus element |

### 5.3. Erijuhtumid

Erijuhtumite all kirjeldatakse klassifikaatori elemendiga seotud kodeerimisotsuseid. Neid kasutatakse juhul, kui on vaja dokumenteerida, kuidas konkreetne piiripealne või tõlgendamist vajav juhtum klassifikaatori elemendi alla liigitatakse.

| # | Atribuudi nimetus | Määratlus | Kohustuslik | Välja tüüp | Mitmesus | Näide |
|---|---|---|---|---|---|---|
| 1 | Nimetus (Name) | Kodeerimisotsuse nimetus. | Ei | [NameType](https://docs.ddialliance.org/DDI-Lifecycle/3.3/model/composite-types/NameType/) | 0..n | Kombineeritud nomenklatuuri koodi 210310 juurde: SOY SAUCE LIGHT |
| 2 | Kirjeldus (Description) | Kodeerimisotsuse kirjeldus. Siia võib lisada ka lingi otsusele või allikale. | Ei | [StructuredStringType](https://docs.ddialliance.org/DDI-Lifecycle/3.3/model/composite-types/StructuredStringType/) | 0..1 | „SOY SAUCE LIGHT” is described as a liquid sauce manufactured from the following ingredients: water 41.91%, soya 30%, salt 18%, wheat 10%, potassium sorbate (E202) 0.09%. |
| 3 | Kuupäev (Date) | Kodeerimisotsuse kuupäev. | Ei | `cogsDate` | 0..1 | September 2025 |

### 5.4. Täiendavad andmeväljad

Täiendavad andmeväljad on Statistikaameti kasutuses olevad lisaväljad. Need ei ole DDI `ClassificationItem` põhiatribuudid.

| # | Atribuudi nimetus | Määratlus | Kohustuslik | Välja tüüp | Mitmesus | Näide |
|---|---|---|---|---|---|---|
| 1 | Mõõtühik (Measurement Unit) | Mõõtühikud on kirjeldatud kontrollsõnastikuna kasutatava koodiloendina „Kategooriate ja klassifikaatorite elementide mõõtühikud – lineaarne“. Koodiloendisse elemendi lisamise vajaduse korral tuleb ühendust võtta peakasutajaga. | Ei | Kontrollsõnastik / mitmekeelne tekst | 0..n | kg; euro; protsent |
| 2 | Annotatsioon (Annotation) | Annotatsiooni või märkuse lisamine. Siia lisatakse info, mis ei ole otseselt objekti kirjeldus, kuid on vajalik selle kasutamiseks või põhjendamiseks. | Ei | Tekst | 0..n | Märkus klassifikaatori elemendi kasutamise kohta |

## 6. Klassifikaatori vastavustabel

DDI: [ClassificationCorrespondenceTable](https://docs.ddialliance.org/DDI-Lifecycle/3.3/model/item-types/ClassificationCorrespondenceTable/)

Klassifikaatori vastavustabel väljendab seost kahe klassifikaatori vahel. Vastavustabeleid kasutatakse tavaliselt sama klassifikaatorite sarja eri versioonide, erinevate klassifikaatorite sarjade klassifikaatorite, klassifikaatori ja selle variandi või variandi eri versioonide võrdlemiseks. Vastavussuhted esitatakse mõlemas suunas.

### 6.1. Klassifikaatori vastavustabeli atribuudid

| # | Atribuudi nimetus | Määratlus | Kohustuslik | Välja tüüp | Mitmesus | Näide |
|---|---|---|---|---|---|---|
| 1 | Tähis (Name) | Vastavustabeli tähis või lühinimi. | Ei | [NameType](https://docs.ddialliance.org/DDI-Lifecycle/3.3/model/composite-types/NameType/) | 0..n | EHAK2019v1_Lääne-Harju_vs_EHAK2019v2_Lääne-Harju |
| 2 | Nimetus (Label) | Vastavustabeli nimetus, mis kuvatakse kasutajale. | **Jah** | [LabelType](https://docs.ddialliance.org/DDI-Lifecycle/3.3/model/composite-types/LabelType/) | 0..n | Vastavustabel EHAK2019v1 Lääne-Harju ja EHAK2019v2 Lääne-Harju vahel |
| 3 | Kirjeldus (Description) | Vastavustabeli sisu ja eesmärgi kirjeldus. | Ei | [StructuredStringType](https://docs.ddialliance.org/DDI-Lifecycle/3.3/model/composite-types/StructuredStringType/) | 0..1 | Vastavustabel kirjeldab kahe EHAK versiooni vahelisi seoseid. |
| 4 | Omanikud (OwnerReference / Owners) | Viide organisatsioonile või isikule, kes on vastavustabeli omanik. | Ei | [Agent](https://docs.ddialliance.org/DDI-Lifecycle/3.3/model/topics/Agent/) | 0..n | Statistikaamet |
| 5 | Haldajad (MaintenanceUnitReference / Maintenance Units) | Viide üksusele või isikutele, kes vastutavad vastavustabeli haldamise ja uuendamise eest. | Ei | [Agent](https://docs.ddialliance.org/DDI-Lifecycle/3.3/model/topics/Agent/) | 0..n | klassifikaatorid@stat.ee |
| 6 | Kontaktisikud (ContactPersonReference / Contact People) | Viide kontaktisikule või kontaktisikutele, kelle poole saab vastavustabeli kohta lisainfo saamiseks pöörduda. | Ei | [Agent](https://docs.ddialliance.org/DDI-Lifecycle/3.3/model/topics/Agent/) | 0..n | EHAK asjatundja |
| 7 | Publikatsioonid (Publication / Publications) | Viide dokumendile, veebilehele või väljaandele, kus vastavustabel on avaldatud. | Ei | [PublicationType](https://docs.ddialliance.org/DDI-Lifecycle/3.3/model/composite-types/PublicationType/) | 0..n | Vastavustabeli avaldamise veebileht |
| 8 | Aegpideva vastavuse kuupäev (FloatingMapDate) | Kuupäev, mis tuleb märkida juhul, kui lähte- ja/või sihtklassifikaator on aegpidev. Vastavustabel väljendab kahe klassifikaatori seoseid sellisena, nagu need eksisteerisid täpsustatud kuupäeval. | Tingimuslik | `cogsDate` | 0..1 | 2019-04-15 |

### 6.2. Klassifikaatorid

| # | Atribuudi nimetus | Määratlus | Kohustuslik | Välja tüüp | Mitmesus | Näide |
|---|---|---|---|---|---|---|
| 1 | Lähteklassifikaator (SourceClassificationReference / Source Classification) | Viide statistilisele klassifikaatorile, millest vastavus tehakse. | **Jah** | [StatisticalClassification](https://docs.ddialliance.org/DDI-Lifecycle/3.3/model/item-types/StatisticalClassification/) | 0..1 | EHAK2019v1_Lääne-Harju |
| 2 | Sihtklassifikaator (TargetClassificationReference / Target Classification) | Viide sihtklassifikaatorile või sihtklassifikaatoritele, millele vastavus on suunatud. Vastavustabeliga võib olla seotud mitu sihtklassifikaatorit. | **Jah** | [StatisticalClassification](https://docs.ddialliance.org/DDI-Lifecycle/3.3/model/item-types/StatisticalClassification/) | 0..n | EHAK2019v2_Lääne-Harju |
| 3 | Lähtetase (SourceLevelReference / Source Level) | Viide lähteklassifikaatori tasemele, mille piires vastavus koostatakse. Kui taset ei näidata, saab sihtklassifikaatori elemente määrata igale lähteklassifikaatori tasemele. | Ei | [ClassificationLevel](https://docs.ddialliance.org/DDI-Lifecycle/3.3/model/item-types/ClassificationLevel/) | 0..1 | 3. tase |
| 4 | Sihttase (TargetLevelReference / Target Level) | Viide sihtklassifikaatori tasemele, mille piires vastavus koostatakse. Kui taset ei näidata, saab lähteklassifikaatori elemente määrata sihtklassifikaatori mis tahes tasemele. | Ei | [ClassificationLevel](https://docs.ddialliance.org/DDI-Lifecycle/3.3/model/item-types/ClassificationLevel/) | 0..1 | 3. tase |
| 5 | Kardinaalsus (RelationshipMappingType / Cardinality) | Määrab lähte- ja sihtklassifikaatori elementide vahelise suhte tüübi. Vastavustabelis võib määratleda 1:1, 1:N, N:1 või M:N suhte. Toetab välise kontrollsõnastiku kasutamist. | Ei | [CodeValueType](https://docs.ddialliance.org/DDI-Lifecycle/3.3/model/composite-types/CodeValueType/) | 0..1 | 1:1 |

### 6.3. Vastendus/kaardistus

Kaardistus ehk vastendus väljendab seost lähteklassifikaatori elemendi ja sihtklassifikaatori elemendi vahel. Vastendus peaks täpsustama, kas kahe klassifikaatori elemendi vaheline seos on osaline või täielik. Sõltuvalt vastavustabeli seose tüübist võib ühe lähte- või sihtklassifikaatori elemendi kohta olla mitu vastendust. DDI-s vastab sellele `Maps` / `ClassificationMapType`. :contentReference[oaicite:2]{index=2}

| # | Atribuudi nimetus | Määratlus | Kohustuslik | Välja tüüp | Mitmesus | Näide |
|---|---|---|---|---|---|---|
| 1 | Lähteelement (SourceClassificationItemReference / Source Item) | Viide klassifikaatori elemendile lähteklassifikaatoris. | **Jah** | [ClassificationItem](https://docs.ddialliance.org/DDI-Lifecycle/3.3/model/item-types/ClassificationItem/) | 0..1 | Keila-Joa alevik |
| 2 | Sihtelement (TargetClassificationItemReference / Target Item) | Viide klassifikaatori elemendile sihtklassifikaatoris. | **Jah** | [ClassificationItem](https://docs.ddialliance.org/DDI-Lifecycle/3.3/model/item-types/ClassificationItem/) | 0..1 | Keila-Joa alevik |
| 3 | On lõplik (IsComplete) | Märkeruut, mis määrab, kas kahe klassifikaatori elemendi vaheline seos on osaline või täielik. | Ei | `boolean` | 0..1 | Jah |
| 4 | Kehtiv alates (ValidFrom) | Kuupäev, millest alates vastendus kehtib. Kuupäev tuleb määrata, kui vastendus kuulub aegpidevasse vastavustabelisse. | Tingimuslik | `cogsDate` | 0..1 | 2019-04-15 |
| 5 | Kehtiv kuni (ValidTo) | Kuupäev, mil vastendus muutus kehtetuks. Kuupäev tuleb määrata, kui vastendus kuulub aegpidevasse vastavustabelisse ja see ei ole enam kehtiv. | Tingimuslik | `cogsDate` | 0..1 |  |

## 7. Klassifikaatori indeks

DDI: [ClassificationIndex](https://docs.ddialliance.org/DDI-Lifecycle/3.3/model/item-types/ClassificationIndex/)

Klassifikaatori indeks on klassifikaatori indeksi kirjete järjestatud loend, näiteks tähestikulises või koodi järjestuses. Klassifikaatori indeks võib olla seotud ühe konkreetse või mitme klassifikaatoriga. Indeks näitab seost andmeallikatest leitud teksti, näiteks küsitluste vastuste, haldusdokumentide või vabatekstiliste kirjete, ja ühe või mitme klassifikaatori vahel. Klassifikaatori indeksit võib kasutada statistika kogumisel vastuste klassifikaatori elementidele koodide määramiseks.

### 7.1. Klassifikaatori indeksi atribuudid

| # | Atribuudi nimetus | Määratlus | Kohustuslik | Välja tüüp | Mitmesus | Näide |
|---|---|---|---|---|---|---|
| 1 | Tähis (Name) | Klassifikaatori indeksi tähis või lühinimi. | Ei | [NameType](https://docs.ddialliance.org/DDI-Lifecycle/3.3/model/composite-types/NameType/) | 0..n | AK ametinimetuste indeks |
| 2 | Nimetus (Label) | Klassifikaatori indeksi nimetus, mis kuvatakse kasutajale. | **Jah** | [LabelType](https://docs.ddialliance.org/DDI-Lifecycle/3.3/model/composite-types/LabelType/) | 0..n | Ametite klassifikaatori indeks |
| 3 | Kirjeldus (Description) | Klassifikaatori indeksi sisu ja eesmärgi kirjeldus. | Ei | [StructuredStringType](https://docs.ddialliance.org/DDI-Lifecycle/3.3/model/composite-types/StructuredStringType/) | 0..1 | Indeks sisaldab ametinimetusi ja nende seoseid Ametite klassifikaatori elementidega. |
| 4 | Parandused (Corrections) | Klassifikaatori indeksi juures tehtud paranduste kokkuvõtlik kirjeldus. Parandused hõlmavad klassifikaatori indeksi kirjega seotud klassifikaatori elemendi koodi muutmist. | Ei | [StructuredStringType](https://docs.ddialliance.org/DDI-Lifecycle/3.3/model/composite-types/StructuredStringType/) | 0..1 | Parandati kirje „raamatupidaja“ seos klassifikaatori elemendiga. |
| 5 | Kodeerimisjuhised (CodingInstructions) | Lisateave, mis juhib kõigi klassifikaatori indeksi kirjete kodeerimisprotsessi. | Ei | [StructuredStringType](https://docs.ddialliance.org/DDI-Lifecycle/3.3/model/composite-types/StructuredStringType/) | 0..1 | Kui vabatekst sisaldab nii ametinimetust kui tööülesandeid, lähtuda kodeerimisel tööülesannete sisust. |
| 6 | Avaldamise kuupäev (ReleaseDate) | Kuupäev, mil praegune klassifikaatori indeks avaldati. | Ei | `cogsDate` | 0..1 | 2024-12-23 |
| 7 | Haldaja (MaintenanceUnitReference / Maintenance Unit) | Viide üksusele või isikutele, kes vastutavad klassifikaatori indeksi haldamise, sh kirjete lisamise, muutmise või kustutamise eest. | Ei | [Agent](https://docs.ddialliance.org/DDI-Lifecycle/3.3/model/topics/Agent/) | 0..n | Statistikaamet |
| 8 | Kontaktisikud (ContactPersonReference / Contact Person(s)) | Viide kontaktisikule või kontaktisikutele, kelle poole saab indeksi kohta lisainfo saamiseks pöörduda. | Ei | [Agent](https://docs.ddialliance.org/DDI-Lifecycle/3.3/model/topics/Agent/) | 0..n | klassifikaatorid@stat.ee |
| 9 | Publikatsioonid (Publication / Publications) | Viide dokumendile, veebilehele või väljaandele, kus klassifikaatori indeks on avaldatud. | Ei | [PublicationType](https://docs.ddialliance.org/DDI-Lifecycle/3.3/model/composite-types/PublicationType/) | 0..n | Indeksi avaldamise veebileht |

### 7.2. Klassifikaatori indeksi kirjed

DDI: [ClassificationIndexEntryType](https://docs.ddialliance.org/DDI-Lifecycle/3.3/model/composite-types/ClassificationIndexEntryType/)

Klassifikaatori indeksi kirje on sõna või lühike tekst, näiteks paikkonna nimi, majandustegevus või ametinimetus, mis kirjeldab objekti, üksuse tüüpi või objekti omadust, mille suhtes klassifikaatori element kehtib, koos vastava klassifikaatori elemendi koodiga.

| # | Atribuudi nimetus | Määratlus | Kohustuslik | Välja tüüp | Mitmesus | Näide |
|---|---|---|---|---|---|---|
| 1 | Kirje tekst (EntryText / Name) | Objekt või üksuse tüüpi või objekti omadust kirjeldav tekst. | **Jah** | [InternationalStringType](https://docs.ddialliance.org/DDI-Lifecycle/3.3/model/composite-types/InternationalStringType/) | 0..1 | raamatupidaja; maksualane nõustamine; Keila-Joa alevik |
| 2 | Klassifikaatori elemendi koodid (CodesClassificationItemReference / Codes Classification Item) | Viide klassifikaatori elemendile, millega klassifikaatori indeksi kirje on seotud. | **Jah** | [ClassificationItem](https://docs.ddialliance.org/DDI-Lifecycle/3.3/model/item-types/ClassificationItem/) | 0..1 | Viide ametirühma või asustusüksuse klassifikaatori elemendile |
| 3 | Kodeerimisjuhised (CodingInstructions) | Lisainformatsioon, mis juhib konkreetse indeksi kirje kodeerimise protsessi. Nõutav juhul, kui kodeerimine sõltub ühest või mitmest muust tegurist. | Tingimuslik | [StructuredStringType](https://docs.ddialliance.org/DDI-Lifecycle/3.3/model/composite-types/StructuredStringType/) | 0..1 | Kui kirje võib kuuluda mitme elemendi alla, lähtuda tööülesannete kirjeldusest. |
| 4 | Kehtiv alates (ValidFrom) | Klassifikaatori indeksi kirje jõustumise kuupäev. Kuupäev tuleb määratleda, kui klassifikaatori indeksi kirje kuulub aegpidevasse klassifikaatori indeksisse. | Tingimuslik | `cogsDate` | 0..1 | 2024-01-01 |
| 5 | Kehtiv kuni (ValidTo) | Klassifikaatori indeksi kirje kehtetuks muutumise kuupäev. Kuupäev tuleb määratleda, kui klassifikaatori indeksi kirje kuulub aegpidevasse klassifikaatori indeksisse ja pole enam kehtiv. | Tingimuslik | `cogsDate` | 0..1 | 2024-12-31 |