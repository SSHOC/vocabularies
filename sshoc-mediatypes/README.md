* Original source: https://www.iana.org/assignments/media-types/media-types.xhtml (processed with the script provided in this directory)
* Current source: export from PoolParty and manual addition:
** added namespace (line 1): `@prefix : <https://vocabs.dariah.eu/media-type/> .`

# What is it?
A list of the 9 top concepts of IANA and all their children concepts. The children concepts are inside CSV files 
downloaded from [IANA's website](https://www.iana.org/assignments/media-types/media-types.xhtml).

## Notes
- The names of the concepts are kind of "slugified" so most special characters are deleted
- The `skos:narrower` are created as a list and not as one predicate because it becomes too long and causes problems

# How to use
`python3 create-skos-from-iana.py`

It will create `media-type_original.ttl`

# How to update `VOCABS_mapping - Yoann_Exports.csv`
On the Google Spreadsheet, go to the tab "Yoann_Exports" and do "Download current sheet as csv" in the file options.

Put this csv document into the `humanities-data-same-csv` directory and launch the script.