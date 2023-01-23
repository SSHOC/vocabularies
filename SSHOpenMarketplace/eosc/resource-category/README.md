* Original source: combination of https://api.eosc-portal.eu/vocabulary/byType/SUPERCATEGORY https://api.eosc-portal.eu/vocabulary/byType/CATEGORY https://api.eosc-portal.eu/vocabulary/byType/SUBCATEGORY (processed with the script provided in this directory)
* Current source: export from PoolParty and manual addition:
** added namespace (line 1): `@prefix : <https://vocabs.dariah.eu/eosc-resource-category/> .`

# How to use
`pip install requests` (if not already installed)
`python3 eosc-resource-category.py`

It will create `eosc-life-category_original.ttl`