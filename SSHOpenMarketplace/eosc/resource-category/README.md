* Original source: combination of https://api.eosc-portal.eu/vocabulary/byType/SUPERCATEGORY https://api.eosc-portal.eu/vocabulary/byType/CATEGORY https://api.eosc-portal.eu/vocabulary/byType/SUBCATEGORY (processed with the script provided in this directory)
* Current source: result of harvest script and applying Skosify on it

Used in SSH Open Marketplace for the property `resource-category` (beware that the filename of the import dump file is used in MP for the code of the vocabulary).
Script to harvest the data in this directory, library to use in the upper folder (see instructions `How to use`).

Version history:
* 0.1.0: Import of API harvest (file `_original.ttl`) into PoolParty and export from there with manual addition (prefix line 1 added)
* 0.1.1: Only use Skosify result of the API harvest (file `_original.ttl`)

# How to use harvest script
`pip install requests` (if not already installed)
`python3 eosc-resource-category.py`

It will create `eosc-life-category_original.ttl`
