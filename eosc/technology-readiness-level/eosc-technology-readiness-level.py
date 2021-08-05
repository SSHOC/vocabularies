import sys
sys.path.append("..")
from eoscskos import EoscSkos

def createSkos():
    eosc = EoscSkos("TRL", "eosc-technology-readiness-level", "EOSC Technology Readiness Level", "EOSC Technology Readiness Level from https://api.eosc-portal.eu/vocabulary/byType/TRL", "skos:definition")
    eosc.createSkos()

createSkos()