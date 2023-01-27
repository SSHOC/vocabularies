# Provenance
* Original source: prepard already in PoolParty, harvested from https://spdx.org/licenses/
* Current source: export from PoolParty and manual addition:
  * added namespace (line 1): `@prefix : <http://spdx.org/licenses/> .`
  * added below schemas dcterms:title: `rdfs:label "Software License"@en;` (around line 29)

# What is it?
A list of software licenses retrieved from SPDX and prepared in the Semantic Web Company PoolParty tool.

Used in SSH Open Marketplace for the property `license` (beware that the filename of the import dump file is used in MP for the code of the vocabulary). Parts are also used in the SSH Conversion Hub (taxonomy `licenses`) and SSH Training Discovery Toolkit (taxonomy `licenses`).

# Version history:
* 0.1.0: Export from PoolParty with some necessary manual additions (prefix line 1 added)

## Notes
- As PoolParty export is not available anymore, it will be necessary to create a new harvest script if updates are needed (also there is the issue, that in the ttl it has http-urls whereas SPDX switched in the meantime to https-urls).
- It would be also necessary to Skosify the ttl-dump but currently this gives some warnings.

