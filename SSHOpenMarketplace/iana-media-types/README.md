# Provenance
* Original source: https://www.iana.org/assignments/media-types/media-types.xhtml (processed with the script provided in this directory)
* Current source: result of harvest script and applying Skosify on it

# What is it?
A list of the 9 top concepts of IANA and all their children concepts. The children concepts are inside CSV files
downloaded from [IANA's website](https://www.iana.org/assignments/media-types/media-types.xhtml).

Used in SSH Open Marketplace for the property `object-format` (beware that the filename of the import dump file is used in MP for the code of the vocabulary).
It is also used for the SSH Conversion Hub taxonomy `formats` for the fields `Input format` and `Output format` (but only a subset is in use).
Script to harvest the data in this directory (see instructions `How to use`).

# Version history:
* 0.1.0: Import of API harvest (file `_original.ttl`) into PoolParty and export from there with manual addition (prefix line 1 added)
* 0.1.1: Only use Skosify result of the API harvest (file `_original.ttl`)

## Notes
- The names of the concepts are kind of "slugified" so most special characters are deleted
- The `skos:narrower` are created as a list and not as one predicate because it becomes too long and causes problems

# How to use harvest script
`python3 create-skos-from-iana.py`

It will create `iana-media-type_original.ttl`

# How to update `VOCABS_mapping - Yoann_Exports.csv`
On the Google Spreadsheet, go to the tab "Yoann_Exports" and do "Download current sheet as csv" in the file options.

Put this csv document into the `humanities-data-same-csv` directory and launch the script.
