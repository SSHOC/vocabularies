import requests
import json


class EoscSkos:
    translate_table = {ord('/'): 'SLASH', ord('+'): 'PLUS', ord('('): 'OPEN_PARENTHESIS', ord(')'): 'CLOSE_PARENTHESIS',
                       ord('&'): 'AMPERSAND', ord(','): 'COMMA'}

    def __init__(self, data_type, schema_name, title, description):
        self.data_type = data_type
        self.schema_name = schema_name
        self.title = title
        self.description = description

    def createSkos(self):
        response = requests.get("https://api.eosc-portal.eu/vocabulary/byType/" + self.data_type)
        results = response.json()

        f = open(self.schema_name + "_original.ttl", "w", encoding="utf-8")
        f.write("@prefix rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#> .\n")
        f.write("@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .\n")
        f.write("@prefix skos: <http://www.w3.org/2004/02/skos/core#> .\n")
        f.write("@prefix dc: <http://purl.org/dc/elements/1.1/> .\n")
        f.write("@prefix dct: <http://purl.org/dc/terms/> .\n")
        f.write("@prefix : <https://vocabs.dariah.eu/" + self.schema_name + "/> .\n\n")

        f.write(":Schema a skos:ConceptScheme;\n")
        f.write("\trdfs:label \"" + self.title + "\"@en;\n")
        f.write("\tdct:title \"" + self.title + "\"@en;\n")
        f.write("\tdc:title \"" + self.title + "\"@en;\n")

        for result in results:
            f.write("\tskos:hasTopConcept :")
            f.write(self.slugify(result["id"]))
            f.write(";\n")
        f.write("\tdc:description \"" + self.description + "\"@en ;\n")
        f.write("\trdfs:comment \"" + self.description + "\"@en .\n\n")

        for result in results:
            f.write(":")
            f.write(self.slugify(result["id"]))
            f.write(" a skos:Concept;\n")
            f.write("\tskos:prefLabel \"")
            f.write(result["name"])
            f.write("\"@en;\n")
            f.write("\trdfs:label \"")
            f.write(result["name"])
            f.write("\"@en;\n")
            if result["description"] is not None:
                f.write("\tdc:description \"")
                f.write(result["description"])
                f.write("\"@en;\n")
            f.write("\tskos:topConceptOf :Schema ;\n")
            f.write("\tskos:inScheme :Schema .\n\n")

        f.close()

    def slugify(self, text):
        text = text.translate(self.translate_table)
        text = u'_'.join(text.split())
        return text.lower()
