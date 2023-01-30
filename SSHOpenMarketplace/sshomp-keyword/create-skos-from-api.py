import requests
import json

translate_table = {ord('/'): 'SLASH', ord('+'): 'PLUS', ord('('): 'OPEN_PARENTHESIS', ord(')'): 'CLOSE_PARENTHESIS',
                   ord('&'): 'AMPERSAND', ord(','): 'COMMA'}

def createSkos():
    response = requests.get("https://marketplace-api.sshopencloud.eu/api/item-search/?f.keyword=*")
    keywords = response.json()['facets']['keyword']

    f = open("sshoc-keyword_original.ttl", "w", encoding="utf-8")
    f.write("@prefix rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#> .\n")
    f.write("@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .\n")
    f.write("@prefix skos: <http://www.w3.org/2004/02/skos/core#> .\n")
    f.write("@prefix dc: <http://purl.org/dc/elements/1.1/> .\n")
    f.write("@prefix dct: <http://purl.org/dc/terms/> .\n")
    f.write("@prefix : <https://vocabs.sshopencloud.eu/vocabularies/sshomp-keyword/> .\n\n")

    f.write(":Schema a skos:ConceptScheme;\n")
    f.write("\trdfs:label \"SSH Open Marketplace Keyword\"@en;\n")
    f.write("\tdct:title \"SSH Open Marketplace Keyword\"@en;\n")
    f.write("\tdc:title \"SSH Open Marketplace Keyword\"@en;\n")

    keyword_slugs = []
    for keyword in keywords:
        if slugify(keyword) not in keyword_slugs:
            keyword_slugs.append(slugify(keyword))
            f.write("\tskos:hasTopConcept :")
            f.write(slugify(keyword))
            f.write(";\n")
    f.write("\tdc:description \"All the keywords used in the SSH Open Marketplace: coming from various sources and from user input.\"@en ;\n")
    f.write("\trdfs:comment \"All the keywords used in the SSH Open Marketplace: coming from various sources and from user input.\"@en .\n\n")

    keyword_slugs = []
    for keyword in keywords:
        if slugify(keyword) not in keyword_slugs:
            keyword_slugs.append(slugify(keyword))
            f.write(":")
            f.write(slugify(keyword))
            f.write(" a skos:Concept;\n")
            f.write("\tskos:prefLabel \"")
            f.write(keyword)
            f.write("\"@en;\n")
            f.write("\trdfs:label \"")
            f.write(keyword)
            f.write("\"@en;\n")
            f.write("\tskos:topConceptOf :Schema ;\n")
            f.write("\tskos:inScheme :Schema .\n\n")

    f.close()

def slugify(text):
    text = text.translate(translate_table)
    text = u'_'.join(text.split())
    return text.lower()


createSkos()
