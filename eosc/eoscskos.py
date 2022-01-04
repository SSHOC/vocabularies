import requests
import json

class EoscSkos:
    translate_table = {ord('/'): 'SLASH', ord('+'): 'PLUS', ord('('): 'OPEN_PARENTHESIS', ord(')'): 'CLOSE_PARENTHESIS',
                       ord('&'): 'AMPERSAND', ord(','): 'COMMA'}

    def __init__(self, data_type, schema_name, title, description, additional_description_tag = ''):
        self.data_type = data_type
        self.schema_name = schema_name
        self.title = title
        self.description = description
        self.additional_description_tag = additional_description_tag

    def slugify(self, text):
        text = text.translate(self.translate_table)
        text = u'_'.join(text.split())
        return text.lower()

    def createHeader(self):
        return("@prefix rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#> .\n"
            + "@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .\n"
            + "@prefix skos: <http://www.w3.org/2004/02/skos/core#> .\n"
            + "@prefix dc: <http://purl.org/dc/elements/1.1/> .\n"
            + "@prefix dct: <http://purl.org/dc/terms/> .\n"
            + "@prefix : <https://vocabs.sshopencloud.eu/vocabularies/" + self.schema_name + "/> .\n\n")

    def createSchema(self, topLevelConcepts):
        topLevel = ""
        for concept in topLevelConcepts:
            if not topLevel:
                topLevel +=  "\tskos:hasTopConcept "
            else:
                topLevel += ", "
            topLevel += ":" + self.slugify(concept)
        if topLevel:
            topLevel +=  " ;\n"
        return(":Schema a skos:ConceptScheme ;\n"
            + "\trdfs:label \"" + self.title + "\"@en ;\n"
            + "\tdct:title \"" + self.title + "\"@en ;\n"
            + "\tdc:title \"" + self.title + "\"@en ;\n"
            + topLevel
            + "\tdc:description \"" + self.description + "\"@en ;\n"
            + "\trdfs:comment \"" + self.description + "\"@en .\n\n")

    def createConcept(self, conceptId, conceptName, conceptDescription, isTopConcept = True, broaderConcept = "", narrowerConcept = ""):
        return (":" + self.slugify(conceptId) + " a skos:Concept ;\n"
            + "\tskos:prefLabel \"" + conceptName + "\"@en ;\n"
            + "\trdfs:label \""  + conceptName + "\"@en ;\n"
            + (("\tdc:description \"" + conceptDescription + "\"@en ;\n") if (conceptDescription is not None and conceptDescription != "") else "")
            + ((("\t" + self.additional_description_tag + " \"" + conceptDescription + "\"@en ;\n") if (conceptDescription is not None and conceptDescription != "") else "") if (self.additional_description_tag != "") else "")
            + ("\tskos:topConceptOf :Schema ;\n" if isTopConcept else "")
            + (("\tskos:broader :" + self.slugify(broaderConcept) + " ;\n") if broaderConcept else "")
            + (("\tskos:narrower " + narrowerConcept + " ;\n") if narrowerConcept else "")
            + "\tskos:inScheme :Schema .\n\n")

    def createSkos(self):
        response = requests.get("https://api.eosc-portal.eu/vocabulary/byType/" + self.data_type)
        results = response.json()
        f = open(self.schema_name + "_original.ttl", "w", encoding="utf-8")
        # write header
        f.write(self.createHeader())
        # write schema definition including topLevelConcepts
        topLevelConcept = []
        for result in results:
            topLevelConcept.append(result["id"])
        f.write(self.createSchema(topLevelConcept))
        # write concepts
        for result in results:
            f.write(self.createConcept(result["id"], result["name"], result["description"], True))
        f.close()

    def createSkosFromChilds(self, childs, broaderConcept, file):
        for concept in list(childs.keys()):
            narrowerConcepts = None
            if ('childs' in childs[concept] and childs[concept]['childs']):
                narrowerConcepts = ""
                for child in list(childs[concept]['childs'].keys()):
                    if (narrowerConcepts):
                        narrowerConcepts += ", "
                    narrowerConcepts += ":" + self.slugify(child)
            file.write(self.createConcept(concept, childs[concept]['name'], childs[concept]['description'], False, broaderConcept, narrowerConcepts))
            if narrowerConcepts:
                self.createSkosFromChilds(childs[concept]['childs'], concept, file)

    def createHierarchicalSkos(self, hierarchisedSkos):
        # no call to an api, to be compiled from a dict
        # the concept ids are in the keys and if there are childs, then there is an explizit child-dict, e.g hiearchisedSkos['conceptId']['childs']['conceptId']...
        file = open(self.schema_name + "_original.ttl", "w", encoding="utf-8")
        # write header
        file.write(self.createHeader())
        # write schema definition including topLevelConcepts
        topLevelConcept = []
        for concept in list(hierarchisedSkos.keys()):
            topLevelConcept.append(concept)
        file.write(self.createSchema(topLevelConcept))
        # write concepts
        for concept in list(hierarchisedSkos.keys()):
            narrowerConcepts = None
            if ('childs' in hierarchisedSkos[concept] and hierarchisedSkos[concept]['childs']):
                narrowerConcepts = ""
                for child in list(hierarchisedSkos[concept]['childs'].keys()):
                    if (narrowerConcepts):
                        narrowerConcepts += ", "
                    narrowerConcepts += ":" + self.slugify(child)
            file.write(self.createConcept(concept, hierarchisedSkos[concept]['name'], hierarchisedSkos[concept]['description'], True, None, narrowerConcepts))
            if narrowerConcepts:
                self.createSkosFromChilds(hierarchisedSkos[concept]['childs'], concept, file)
        file.close()
