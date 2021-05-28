# What is it?
A list of the 9 top concepts of IANA and all their children concepts. The children concepts are inside CSV files 
downloaded from [IANA's website](https://www.iana.org/assignments/media-types/media-types.xhtml).

## Notes
- The names of the concepts are kind of "slugified" so most special characters are deleted
- The `skos:narrower` are created as a list and not as one predicate because it becomes too long and causes problems

# How to use
`python3 create-skos-from-iana.py`

It will create `sshoc-media.ttl`