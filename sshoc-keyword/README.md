* Original source: List of keywords of ingested items on development using endpoint /api/item-search/?f.keyword=*
* Current source: export from PoolParty and manual addition:
** added namespace (line 1): `@prefix : <https://vocabs.dariah.eu/sshoc-keyword/> .`

# What is it?
A list of all keywords retrieved from the SSHOC Marketplace

## Notes
- Some keywords are very similar, e.g. `Metadata` and `metadata`, so only one is used, the second one is simply 
  deleted as it creates problems with SKOS
- The names of the concepts are kind of "slugified" so most special characters are deleted

# How to use
`pip install requests` (if not already installed)
`python3 create-skos-from-api.py`

It will create `sshoc-keyword_original.ttl`