import requests
import json
import csv

translate_table = {ord('/'): 'SLASH', ord('+'): 'PLUS'}

def createSkos():
    # Before anything, get the mapping between those media types and Humanities Data file endings
    mappingfile = open("humanities-data-same-csv/VOCABS_mapping - Yoann_Exports.csv")
    readermapping = csv.DictReader(mappingfile)
    mappings = {}
    for row in readermapping:
        if len(dict(row)["name"]) != 0:
            mappings[dict(row)["name"]] = dict(row)["fileending"]

    mimes = ['application', 'audio', 'font', 'image', 'message', 'model', 'multipart', 'text', 'video']

    f = open("iana_media-type_original.ttl", "w")
    f.write("@prefix rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#> .\n")
    f.write("@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .\n")
    f.write("@prefix skos: <http://www.w3.org/2004/02/skos/core#> .\n")
    f.write("@prefix dc: <http://purl.org/dc/elements/1.1/> .\n")
    f.write("@prefix dct: <http://purl.org/dc/terms/> .\n")
    f.write("@prefix media-type: <https://vocabs.dariah.eu/media-type/> .\n\n")

    f.write("media-type:Schema a skos:ConceptScheme;\n")
    f.write("\trdfs:label \"Media Types from IANA\"@en;\n")
    f.write("\tdc:title \"Media Types from IANA\"@en;\n")
    f.write("\tdct:title \"Media Types from IANA\"@en;\n")

    for mime in mimes:
        f.write("\tskos:hasTopConcept media-type:")
        f.write(mime)
        f.write(";\n")

    f.write("\tdc:description \"List of all Media Types from IANA with 9 top levels and all concepts below\"@en ;\n")
    f.write("\trdfs:comment \"List of all Media Types from IANA with 9 top levels and all concepts below\"@en .\n\n")

    # Get only the name of the keyword
    for mime in mimes:
        mimefile = open("iana-csv/" + mime + ".csv")
        reader = csv.DictReader(mimefile)
        narrowers = ""
        narrowerList = []
        for row in reader:
            template = dict(row).get('Template')
            if len(template) == 0:
                template = dict(row).get('Name')
            narrowers += ("media-type:" + slugify(template) + " ")
            narrowerList.append("media-type:" + slugify(template))
            f.write("media-type:")
            f.write(slugify(template))
            f.write(" a skos:Concept;\n")
            f.write("\tskos:prefLabel \"")
            f.write(template)
            f.write("\"@en;\n")
            f.write("\trdfs:label \"")
            f.write(template)
            f.write("\"@en;\n")
            if template != dict(row).get('Name'):
                f.write("\tskos:altLabel \"")
                f.write(mime + ": " + dict(row).get('Name'))
                f.write("\"@en;\n")
            if template in mappings:
                f.write("\tskos:altLabel \"")
                f.write("Humanities Data: " + mappings[template])
                f.write("\"@en;\n")
            f.write("\tskos:inScheme media-type:Schema;\n")
            f.write("\tskos:broader media-type:")
            f.write(slugify(mime))
            f.write(" .\n\n")

        f.write("media-type:")
        f.write(slugify(mime))
        f.write(" a skos:Concept;\n")
        f.write("\tskos:prefLabel \"")
        f.write(mime)
        f.write("\"@en;\n")
        f.write("\trdfs:label \"")
        f.write(mime)
        f.write("\"@en;\n")

        for narrower in narrowerList:
            f.write("\tskos:narrower ")
            f.write(narrower)
            f.write(" ;\n")

        f.write("\tskos:topConceptOf media-type:Schema .\n\n")

    f.close()

def slugify(text):
    text = text.translate(translate_table)
    text = u'_'.join(text.split())
    return text.lower()


createSkos()