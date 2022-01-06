import sys
sys.path.append("..")
from eoscskos import EoscSkos

def createSkos():
    eosc = EoscSkos("COUNTRY", "eosc-geographical-availability", "EOSC Geographical Availability List", "EOSC Geographical Availability List from https://api.eosc-portal.eu/vocabulary/byType/COUNTRY", "", "eoscGeographicalAvailabilityScheme")
    eosc.createSkos()

createSkos()
