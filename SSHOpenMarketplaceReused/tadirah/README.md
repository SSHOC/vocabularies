* Original source: https://vocabs.dariah.eu/rest/v1/tadirah2/data?format=text/turtle
* Current source: export from PoolParty and manual addition:
** added namespace (line 1): `@prefix : <https://vocabs.dariah.eu/tadirah/> .`
** added in schema below dcterms:title (around line 27): `rdfs:label "TaDiRAH 2"@en;` (should contain the same value as dcterms:title)
** added in schema below dcterms:description (around line 30): `rdfs:comment "Taxonomy of Digital Research Activities in the Humanities"@en;` (should contain the same value as dcterms:description)

Contains the current version 2 of TaDiRAH https://vocabs.dariah.eu/tadirah2/en/ that is in use for the MP.

We used before the old version 0.5.x of TaDiRAH (http://tadirah.dariah.eu/ resp. https://github.com/dhtaxonomy/TaDiRAH) but agreed on only using version 2, so there is a mapping between old and new version (as some sources like Tapor deliver the old version). For documentation reasons the old version is stored in the dedicated subdirectory.
