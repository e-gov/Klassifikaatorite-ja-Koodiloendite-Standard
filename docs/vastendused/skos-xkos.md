# SKOS/XKOS vastendus (mustand)

## Põhiobjektide vastendus

| Standardi objekt | DDI Lifecycle | SKOS/XKOS | Olek |
| --- | --- | --- | --- |
| Klassifikaator | `StatisticalClassification` | <a href="https://www.w3.org/TR/skos-reference/#schemes" target="_blank" rel="noopener noreferrer"><code>skos:ConceptScheme</code></a> | Esialgne vaste |
| Klassifikaatori tase | `ClassificationLevel` + `LevelContext` | <a href="https://rdf-vocabulary.ddialliance.org/xkos.html#classification-levels" target="_blank" rel="noopener noreferrer"><code>xkos:ClassificationLevel</code></a> | Esialgne vaste |
| Klassifikaatori element | `ClassificationItem` | <a href="https://www.w3.org/TR/skos-reference/#concepts" target="_blank" rel="noopener noreferrer"><code>skos:Concept</code></a> | Esialgne vaste |
| Koodiloend | `CodeList` | <a href="https://www.w3.org/TR/skos-reference/#schemes" target="_blank" rel="noopener noreferrer"><code>skos:ConceptScheme</code></a> | Esialgne vaste |
| Koodiloendi element | `CodeType` + `Category` | <a href="https://www.w3.org/TR/skos-reference/#concepts" target="_blank" rel="noopener noreferrer"><code>skos:Concept</code></a> | Vajab täpsustamist |
| Klassifikaatorite sari | `ClassificationSeries` | <a href="https://rdf-vocabulary.ddialliance.org/xkos.html#classifications-and-classification-schemes" target="_blank" rel="noopener noreferrer">XKOS-i klassifikaatorisari</a> | Vajab täpsustamist |
| Vastavustabel | `ClassificationCorrespondenceTable` | <a href="https://rdf-vocabulary.ddialliance.org/xkos.html#correspondences-and-concept-associations" target="_blank" rel="noopener noreferrer"><code>xkos:Correspondence</code></a> | Esialgne vaste |
| Vastendus | `ClassificationMapType` | <a href="https://rdf-vocabulary.ddialliance.org/xkos.html#correspondences-and-concept-associations" target="_blank" rel="noopener noreferrer"><code>xkos:ConceptAssociation</code></a> | Esialgne vaste |

## Klassifikaatori elemendi esmane vastendus

| Standardi väli | SKOS/XKOS | Märkus |
| --- | --- | --- |
| `ItemCode` | <a href="https://www.w3.org/TR/skos-reference/#notations" target="_blank" rel="noopener noreferrer"><code>skos:notation</code></a> | Elemendi kood |
| `Label` | <a href="https://www.w3.org/TR/skos-reference/#labels" target="_blank" rel="noopener noreferrer"><code>skos:prefLabel</code></a> | Eelistatud nimetus |
| Ülem-element | <a href="https://www.w3.org/TR/skos-reference/#semantic-relations" target="_blank" rel="noopener noreferrer"><code>skos:broader</code></a> | Hierarhiline seos |
| `Includes` | <a href="https://rdf-vocabulary.ddialliance.org/xkos.html#documentation-properties" target="_blank" rel="noopener noreferrer"><code>xkos:coreContentNote</code></a> | Kaasa arvatud |
| `IncludesAlso` | <a href="https://rdf-vocabulary.ddialliance.org/xkos.html#documentation-properties" target="_blank" rel="noopener noreferrer"><code>xkos:additionalContentNote</code></a> | Lisaks kaasa arvatud |
| `Excludes` | <a href="https://rdf-vocabulary.ddialliance.org/xkos.html#documentation-properties" target="_blank" rel="noopener noreferrer"><code>xkos:exclusionNote</code></a> | Välja arvatud |

## Viited

- <a href="https://www.w3.org/TR/skos-reference/" target="_blank" rel="noopener noreferrer">SKOS Simple Knowledge Organization System Reference (W3C)</a>
- <a href="https://rdf-vocabulary.ddialliance.org/xkos.html" target="_blank" rel="noopener noreferrer">XKOS: Extended Knowledge Organization System (DDI Alliance)</a>
