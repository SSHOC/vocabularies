# What is it?
A list of all keywords retrieved from the SSHOC Marketplace

## Notes
- Some keywords are very similar, e.g. `Metadata` and `metadata`, so only one is used, the second one is simply 
  deleted as it creates problems with SKOS
- The names of the concepts are kind of "slugified" so most special characters are deleted

# How to use
`python3 create-skos-from-api.py`

It will create `sshoc-keywords.ttl`