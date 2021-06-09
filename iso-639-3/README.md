* Original source: https://vocabs.dariah.eu/rest/v1/iso639_3/data?format=text/turtle
* Prepared source: deleted explicite reverse relations to iso-639-1 / added dct:title for schema (necessary for PoolParty)
* Current source: export from PoolParty and manual addition:
** added namespace (line 1): `@prefix : <https://vocabs.acdh.oeaw.ac.at/iso6393/> .`
** put in schema rdfs:label and rdfs:comment the @en-language on first place otherwise it will not show up in english in the import

# What is it?
A list of langauge codes based on ISO-639-3
