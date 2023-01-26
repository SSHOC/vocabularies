# Provenance
* Original source: list of keywords of ingested items on development using endpoint /api/item-search/?f.keyword=*
* Current source: result of harvest script and applying Skosify on it

# What is it?
A list of all keywords retrieved from the SSHOC Marketplace

Used in SSH Open Marketplace for the property `keyword` (beware that the filename of the import dump file is used in MP for the code of the vocabulary).
Script to harvest the data in this directory (see instructions `How to use`).

# Version history:
* 0.1.0: Import of API harvest (file `_original.ttl`) into PoolParty and export from there with manual addition (prefix line 1 added)
* 0.1.1: Only use Skosify result of the API harvest (file `_original.ttl`)

## Notes
- Some keywords are very similar, e.g. `Metadata` and `metadata`, so only one is used, the second one is simply deleted as it creates problems with SKOS
- The names of the concepts are kind of "slugified" so most special characters are deleted

# How to use harvest script
`pip install requests` (if not already installed)
`python3 create-skos-from-api.py`

It will create `sshoc-keyword_original.ttl`
