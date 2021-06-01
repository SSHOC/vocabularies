import sys
sys.path.append("..")
from eosc import eoscskos

def createSkos():
    eosc = eoscskos.EoscSkos("COUNTRY", "eosc-geographical-availability", "EOSC Geographical Availability List", "EOSC Geographical Availability List from https://api.eosc-portal.eu/vocabulary/byType/COUNTRY")
    eosc.createSkos()

createSkos()