# SKOS/XKOS vastendus (mustand)

## Põhiobjektide vastendus

| Standardi objekt | DDI Lifecycle | SKOS/XKOS | Olek |
| --- | --- | --- | --- |
| Klassifikaatori perekond | `ClassificationFamily` | <a href="https://rdf-vocabulary.ddialliance.org/xkos.html#classifications-and-classification-schemes" target="_blank" rel="noopener noreferrer">XKOS-i katvusmudel (`xkos:covers`)</a> või `skos:Collection` | Vajab modelleerimisotsust |
| Klassifikaatorite sari | `ClassificationSeries` | <a href="https://rdf-vocabulary.ddialliance.org/xkos.html#classifications-and-classification-schemes" target="_blank" rel="noopener noreferrer"><code>skos:Concept</code> + versioonide <code>xkos:belongsTo</code></a> | Soovitatav esitus |
| Klassifikaator / versioon | `StatisticalClassification` | <a href="https://www.w3.org/TR/skos-reference/#schemes" target="_blank" rel="noopener noreferrer"><code>skos:ConceptScheme</code></a> | Otsene XKOS-i mudel |
| Klassifikaatori tase | `ClassificationLevel` + `LevelContext` | <a href="https://rdf-vocabulary.ddialliance.org/xkos.html#classification-levels" target="_blank" rel="noopener noreferrer"><code>xkos:ClassificationLevel</code></a> | Otsene |
| Klassifikaatori element | `ClassificationItem` | <a href="https://www.w3.org/TR/skos-reference/#concepts" target="_blank" rel="noopener noreferrer"><code>skos:Concept</code></a> | Otsene |
| Koodiloend | `CodeList` | <a href="https://www.w3.org/TR/skos-reference/#schemes" target="_blank" rel="noopener noreferrer"><code>skos:ConceptScheme</code></a> | Esialgne vaste |
| Koodiloendi element | `CodeType` + `Category` | <a href="https://www.w3.org/TR/skos-reference/#concepts" target="_blank" rel="noopener noreferrer"><code>skos:Concept</code></a> | Vajab identiteedireeglit |
| Vastavustabel | `ClassificationCorrespondenceTable` | <a href="https://rdf-vocabulary.ddialliance.org/xkos.html#correspondences-and-concept-associations" target="_blank" rel="noopener noreferrer"><code>xkos:Correspondence</code></a> | Otsene |
| Vastendus | `ClassificationMapType` | <a href="https://rdf-vocabulary.ddialliance.org/xkos.html#correspondences-and-concept-associations" target="_blank" rel="noopener noreferrer"><code>xkos:ConceptAssociation</code></a> | Otsene struktuurne vaste |

### Olekute tähendus

- **Otsene** – sihtmudelis on sama ülesandega klass või omadus.
- **Hea vaste** – praktiliselt sobiv vaste, kuid tähendus ei pruugi olla formaalselt identne.
- **Osaline / teisendusreegel** – info saab esitada, kuid teisendus vajab kokkulepitud reeglit.
- **Profiililaiendus** – SKOS/XKOS-is ei ole piisavalt täpset omadust. Peab otsustama, kas kasutada muud RDF-sõnavara või oma omadust.

---

# Atribuutide esialgne vastendus

## 1. Klassifikaatori perekond (`ClassificationFamily`)

| DDI-põhine atribuut | RDF/SKOS/XKOS vaste | Olek / märkus |
| --- | --- | --- |
| Tähis (`Name`) | <a href="http://purl.org/dc/terms/identifier" target="_blank" rel="noopener noreferrer"><code>dcterms:identifier</code></a> | Hea vaste |
| Nimetus (`Label`) | <a href="https://www.w3.org/TR/skos-reference/#labels" target="_blank" rel="noopener noreferrer"><code>skos:prefLabel</code></a> | Hea vaste, kui perekond on RDF-ressurss |
| Kirjeldus (`Description`) | <a href="http://purl.org/dc/terms/description" target="_blank" rel="noopener noreferrer"><code>dcterms:description</code></a> | Hea vaste |
| Klassifikaatorite sarjad (`ClassificationSeriesReference`) | `skos:member` **ainult siis**, kui perekond modelleeritakse `skos:Collection`-ina | Vajab modelleerimisotsust; XKOS ise käsitleb klassifikaatoriperekondi pigem katvuse (`xkos:covers`) kaudu |

## 2. Klassifikaatorite sari (`ClassificationSeries`)

XKOS-is on soovituslikult üks klassifikaatorit kui versioonidest sõltumatut tervikut tähistav `skos:Concept`, mille külge versioonid (`skos:ConceptScheme`) seotakse omadusega `xkos:belongsTo`.

| DDI-põhine atribuut | RDF/SKOS/XKOS vaste | Olek / märkus |
| --- | --- | --- |
| Tähis (`Name`) | `dcterms:identifier` | Hea vaste |
| Nimetus (`Label`) | `skos:prefLabel` | Hea vaste |
| Kirjeldus (`Description`) | `dcterms:description` | Hea vaste |
| Kontekst (`SeriesContext`) | `dcterms:description` või profiili eraldi omadus | Osaline; üldkirjeldusse liitmine võib tähendust nõrgendada |
| Teema (`SubjectArea`) | <a href="https://rdf-vocabulary.ddialliance.org/xkos.html#classifications-and-classification-schemes" target="_blank" rel="noopener noreferrer"><code>xkos:covers</code></a> → `skos:Concept` | Hea vaste, kui teema esitatakse kontrollitud mõistena |
| Sarja kuuluvad klassifikaatorid (`StatisticalClassificationReference`) | versioon → sari: <a href="https://rdf-vocabulary.ddialliance.org/xkos.html#classifications-and-classification-schemes" target="_blank" rel="noopener noreferrer"><code>xkos:belongsTo</code></a> | Otsene, kuid seose suund on DDI kirjeldusest vastupidine |
| Kehtiv versioon (`CurrentStatisticalClassificationReference`) | tuletatav versioonide kehtivusinfost (`dcterms:valid`) | Profiilireegel; XKOS-is eraldi `currentVersion` omadust ei ole |
| Omanik (`OwnerReference`) | otsene SKOS/XKOS vaste puudub | Profiililaiendus; omanik, haldaja ja avaldaja ei ole sama roll |

## 3. Klassifikaator / versioon (`StatisticalClassification`)

| DDI-põhine atribuut | RDF/SKOS/XKOS vaste | Olek / märkus |
| --- | --- | --- |
| Tähis (`Name`) | `dcterms:identifier` | Hea vaste |
| Nimetus (`Label`) | `skos:prefLabel` | Hea vaste |
| Kirjeldus (`Description`) | `dcterms:description` | Hea vaste |
| Kehtivus (`IsCurrent`) | tuletatav `dcterms:valid` väärtusest ja tänasest kuupäevast | Profiilireegel; eraldi boolean pole vajalik, kui kehtivusaeg on masinloetav |
| Kehtiv alates (`ReleaseDate`) | <a href="http://purl.org/dc/terms/valid" target="_blank" rel="noopener noreferrer"><code>dcterms:valid</code></a> | Osaline; profiilis tuleb kokku leppida algus- ja lõppkuupäeva esitus |
| Kehtiv kuni (`TerminationDate`) | `dcterms:valid` | Osaline; sama kehtivusintervalli lõpp |
| Õiguslik alus (`LegalBase`) | `dcterms:relation` | Üldine vaste; täpsem õigusaktide sõnavara võib olla parem |
| Autoriõigus (`Copyright`) | `dcterms:rights` | Hea vaste |
| Avaldamine (`Publication`) | `dcterms:relation` | Hea üldvaste; võib hiljem täpsustada |
| Levitamine on lubatud (`IsDisseminationAllowed`) | `dcterms:rights` / litsentsist tuletatav või profiili boolean | Profiilireegel |
| Tasemed (`LevelContext`) | <a href="https://rdf-vocabulary.ddialliance.org/xkos.html#classification-levels" target="_blank" rel="noopener noreferrer"><code>xkos:levels</code></a> + `xkos:numberOfLevels` | Otsene struktuurne vaste |
| Eelnev klassifikaator (`PredecessorReference`) | <a href="https://rdf-vocabulary.ddialliance.org/xkos.html#classifications-and-classification-schemes" target="_blank" rel="noopener noreferrer"><code>xkos:follows</code></a> | Otsene: uus versioon `xkos:follows` eelmist |
| Järgnev klassifikaator (`SuccessorReference`) | järgmine versioon → käesolev: `xkos:follows` | Otsene info, kuid RDF-tripi suund tuleb pöörata |
| Lähteklassifikaator (`DerivedFromReference`) | <a href="https://www.w3.org/TR/prov-o/#wasDerivedFrom" target="_blank" rel="noopener noreferrer"><code>prov:wasDerivedFrom</code></a> | Hea väline RDF-vastendus; XKOS-is otsest omadust pole |
| Muudatused võrreldes eelmisega (`ChangesFromPreceding`) | `skos:changeNote` | Hea vaste |
| Lisamaterjalid (`RelatedOtherMaterialReference`) | `dcterms:relation` | Hea üldvaste |
| Versioon (`IsVersion`) | esitus `skos:ConceptScheme`-ina ja `xkos:belongsTo` seos | Pigem tuletatav; eraldi boolean ei ole RDF-is vajalik |
| Aegpidevus (`IsFloating`) | otsene SKOS/XKOS vaste puudub | Profiililaiendus |
| Uuendus (`IsUpdate`) | otsene SKOS/XKOS vaste puudub | Profiililaiendus |
| Uuendused on lubatud (`UpdatesAllowed`) | otsene SKOS/XKOS vaste puudub | Profiililaiendus |
| Lubatavad uuendused (`PermissibleUpdates`) | `skos:editorialNote` või profiili eraldi omadus | Osaline; tähendus ei ole päris SKOS-i editorial note |
| Uuendused (`Updates`) | `skos:changeNote` | Hea vaste |
| Alusklassifikaator (`VariantOfReference`) | <a href="https://rdf-vocabulary.ddialliance.org/xkos.html#classifications-and-classification-schemes" target="_blank" rel="noopener noreferrer"><code>xkos:variant</code></a> | Otsene seos, kuid XKOS-i soovituslik suund on alus → variant |
| Muudatused võrreldes baasklassifikaatoriga (`VariantChangesFromBase`) | `skos:changeNote` | Hea esialgne vaste |
| Variandi loomise põhjus (`VariantPurpose`) | `dcterms:description` või `skos:note` | Osaline |
| Haldaja (`MaintenanceUnitReference`) | otsene SKOS/XKOS vaste puudub | Profiililaiendus; võib hiljem kasutada eraldi organisatsiooni/andmekataloogi sõnavara |
| Kontaktandmed (`ContactPersonReference`) | otsene SKOS/XKOS vaste puudub | Profiililaiendus; nt DCAT/vCard on võimalik lisasõnavara |

## 4. Klassifikaatori tase (`ClassificationLevel` + `LevelContext`)

| DDI-põhine atribuut | RDF/SKOS/XKOS vaste | Olek / märkus |
| --- | --- | --- |
| Tähis (`Name`) | `dcterms:identifier` | Hea vaste |
| Nimetus (`Label`) | `skos:prefLabel` | Hea vaste |
| Kirjeldus (`Description`) | `dcterms:description` | Hea vaste |
| Taseme number (`LevelContext/LevelNumber`) | <a href="https://rdf-vocabulary.ddialliance.org/xkos.html#classification-levels" target="_blank" rel="noopener noreferrer"><code>xkos:depth</code></a> | Otsene |
| Taseme koodi tüüp (`LevelCodeType`) | võib kajastuda `skos:notation` andmetüübis; otsene taseme omadus puudub | Osaline / profiilireegel |
| Taseme koodi struktuur (`LevelCodeStructure`) | <a href="https://rdf-vocabulary.ddialliance.org/xkos.html#classification-levels" target="_blank" rel="noopener noreferrer"><code>xkos:notationPattern</code></a> | Hea vaste, kui struktuur teisendatakse regulaaravaldiseks |
| Fiktiivne kood (`DummyCode`) | otsene XKOS-vastendus puudub | Profiililaiendus |
| Viide määratlevale mõistele (`DefiningConceptReference`) | <a href="https://rdf-vocabulary.ddialliance.org/xkos.html#classification-levels" target="_blank" rel="noopener noreferrer"><code>xkos:organizedBy</code></a> | Otsene |
| Tasemesse kuuluvad elemendid (`LevelContext` liikmesus) | `skos:member` | Otsene: tase → element |
| Klassifikaatori tasemete järjestus | `xkos:levels` RDF-loendina | Otsene XKOS-i struktuur |

## 5. Klassifikaatori element (`ClassificationItem`)

| DDI-põhine atribuut | RDF/SKOS/XKOS vaste | Olek / märkus |
| --- | --- | --- |
| Tähis (`Name`) | `dcterms:identifier` või `skos:altLabel` | Vajab reeglit: kas väärtus on identifikaator või alternatiivne nimetus |
| Nimetus (`Label`) | `skos:prefLabel` | Otsene; üks eelistatud nimetus ühe keele kohta |
| Kirjeldus (`Description`) | `skos:definition` või `dcterms:description` | Vajab reeglit: kas tekst on definitsioon või üldkirjeldus |
| Väärtus (`ItemCode / Value`) | <a href="https://www.w3.org/TR/skos-reference/#notations" target="_blank" rel="noopener noreferrer"><code>skos:notation</code></a> | Otsene |
| Kaasa arvatud (`Includes`) | <a href="https://rdf-vocabulary.ddialliance.org/xkos.html#documentation-properties" target="_blank" rel="noopener noreferrer"><code>xkos:coreContentNote</code></a> | Otsene |
| Lisaks kaasa arvatud (`IncludesAlso`) | <a href="https://rdf-vocabulary.ddialliance.org/xkos.html#documentation-properties" target="_blank" rel="noopener noreferrer"><code>xkos:additionalContentNote</code></a> | Otsene |
| Välja arvatud (`Excludes`) | <a href="https://rdf-vocabulary.ddialliance.org/xkos.html#documentation-properties" target="_blank" rel="noopener noreferrer"><code>xkos:exclusionNote</code></a> | Otsene |
| Tuleviku sündmused (`FutureEvents`) | `skos:changeNote` või profiili eraldi omadus | Osaline; changeNote ei erista tulevikku minevikust |
| Muudatused eelnevast versioonist (`ChangesFromPriorVersion`) | `skos:changeNote` | Hea vaste |
| Uuendused (`Updates`) | `skos:changeNote` | Hea vaste |
| Kehtiv alates (`ValidFrom`) | `dcterms:valid` | Osaline; algus/lõpp vajavad profiilireeglit |
| Kehtiv kuni (`ValidTo`) | `dcterms:valid` | Osaline |
| On genereeritud (`IsGenerated`) | otsene SKOS/XKOS vaste puudub | Profiililaiendus |
| On kehtiv (`IsValid`) | kehtivusinfost tuletatav | Profiilireegel |
| Kuulub klassifikaatorisse | `skos:inScheme` | Otsene struktuurne seos |
| Ülem-element (`ParentClassificationItemReference`) | <a href="https://www.w3.org/TR/skos-reference/#semantic-relations" target="_blank" rel="noopener noreferrer"><code>skos:broader</code></a> | Soovitatav lisada standardi nähtava väljana; spetsiifilisema suhte korral võib kasutada XKOS-i hierarhiasuhteid |
| Mõõtühik (`Measurement Unit`) | otsene SKOS/XKOS vaste puudub | Vajadusel eraldi mõõtühikute sõnavara (nt QUDT/OM) või profiililaiendus |

## 6. Klassifikaatori vastavustabel (`ClassificationCorrespondenceTable`)

| DDI-põhine atribuut | RDF/SKOS/XKOS vaste | Olek / märkus |
| --- | --- | --- |
| Tähis (`Name`) | `dcterms:identifier` | Hea vaste |
| Nimetus (`Label`) | `dcterms:title` | Hea vaste |
| Kirjeldus (`Description`) | `dcterms:description` | Hea vaste |
| Omanikud (`OwnerReference`) | otsene SKOS/XKOS vaste puudub | Profiililaiendus |
| Haldajad (`MaintenanceUnitReference`) | otsene SKOS/XKOS vaste puudub | Profiililaiendus |
| Kontaktisikud (`ContactPersonReference`) | otsene SKOS/XKOS vaste puudub | Profiililaiendus / lisasõnavara |
| Publikatsioonid (`Publication`) | `dcterms:relation` | Hea üldvaste |
| Aegpideva vastavuse kuupäev (`FloatingMapDate`) | `dcterms:date` | Hea esialgne vaste; see on hetktõmmise kuupäev, mitte tingimata kehtivusintervall |
| Lähteklassifikaator (`SourceClassificationReference`) | <a href="https://rdf-vocabulary.ddialliance.org/xkos.html#correspondences-and-concept-associations" target="_blank" rel="noopener noreferrer"><code>xkos:compares</code></a> | Osaline: `xkos:compares` ei väljenda lähte-/sihtsuunda |
| Sihtklassifikaator (`TargetClassificationReference`) | `xkos:compares` | Osaline: suuna säilitamiseks on vaja profiilireeglit või laiendust |
| Lähtetase (`SourceLevelReference`) | otsene XKOS Correspondence-vastendus puudub | Profiililaiendus |
| Sihttase (`TargetLevelReference`) | otsene XKOS Correspondence-vastendus puudub | Profiililaiendus |
| Kardinaalsus (`RelationshipMappingType`) | tuletatav `xkos:ConceptAssociation` lähte- ja sihtmõistete arvust | Profiilireegel; XKOS ei vaja eraldi 1:1/1:N välja |

Lisaks seotakse vastavustabel selle vastendustega omaduse `xkos:madeOf` abil.

## 7. Vastendus (`ClassificationMapType` → `xkos:ConceptAssociation`)

| DDI-põhine atribuut | RDF/SKOS/XKOS vaste | Olek / märkus |
| --- | --- | --- |
| Lähteelement (`SourceClassificationItemReference`) | <a href="https://rdf-vocabulary.ddialliance.org/xkos.html#correspondences-and-concept-associations" target="_blank" rel="noopener noreferrer"><code>xkos:sourceConcept</code></a> | Otsene |
| Sihtelement (`TargetClassificationItemReference`) | <a href="https://rdf-vocabulary.ddialliance.org/xkos.html#correspondences-and-concept-associations" target="_blank" rel="noopener noreferrer"><code>xkos:targetConcept</code></a> | Otsene |
| On lõplik (`IsComplete`) | otsene XKOS vaste puudub | Profiililaiendus; **ei tohi automaatselt teisendada `skos:exactMatch`-iks** |
| Kehtiv alates (`ValidFrom`) | `dcterms:valid` | Osaline; profiilis määrata intervalli esitus |
| Kehtiv kuni (`ValidTo`) | `dcterms:valid` | Osaline |

## 8. Koodiloend (`CodeList`)

| DDI-põhine atribuut | RDF/SKOS/XKOS vaste | Olek / märkus |
| --- | --- | --- |
| Tähis (`Name`) | `dcterms:identifier` | Hea vaste |
| Nimetus (`Label`) | `skos:prefLabel` | Hea vaste |
| Kirjeldus (`Description`) | `dcterms:description` | Hea vaste |
| Kehtivuse algus (`ValidFrom`) | `dcterms:valid` | Osaline; intervalli esitus vajab reeglit |
| Kehtivuse lõpp (`ValidTo`) | `dcterms:valid` | Osaline |
| Omanik/haldaja (`MaintenanceUnitReference`) | otsene SKOS/XKOS vaste puudub | Profiililaiendus |
| Kontaktandmed (`ContactPersonReference`) | otsene SKOS/XKOS vaste puudub | Profiililaiendus / lisasõnavara |

## 9. Koodiloendi element (`CodeType` + `Category`)

| DDI-põhine atribuut | RDF/SKOS/XKOS vaste | Olek / märkus |
| --- | --- | --- |
| Tähis (`Name`) | `dcterms:identifier` või `skos:altLabel` | Vajab semantilist reeglit |
| Kood (`ItemCode`) | `skos:notation` | Otsene |
| Nimetus (`Label`) | `skos:prefLabel` | Otsene |
| Kirjeldus (`Description`) | `skos:definition` või `dcterms:description` | Vajab reeglit |
| Tase (`Level`) | hierarhilise loendi korral võimalik `xkos:ClassificationLevel` + `skos:member` | XKOS-i kasutamisel hea esitus; puhtas SKOS-is taseme konstruktsiooni ei ole |
| Kuulub koodiloendisse | `skos:inScheme` | Otsene struktuurne seos |

---

## Kasutatavad põhisõnavarad

- <a href="https://www.w3.org/TR/skos-reference/" target="_blank" rel="noopener noreferrer">SKOS Simple Knowledge Organization System Reference (W3C)</a>
- <a href="https://rdf-vocabulary.ddialliance.org/xkos.html" target="_blank" rel="noopener noreferrer">XKOS: Extended Knowledge Organization System (DDI Alliance)</a>
- <a href="https://www.dublincore.org/specifications/dublin-core/dcmi-terms/" target="_blank" rel="noopener noreferrer">DCMI Metadata Terms</a>
- <a href="https://www.w3.org/TR/prov-o/" target="_blank" rel="noopener noreferrer">PROV-O: The PROV Ontology</a>
