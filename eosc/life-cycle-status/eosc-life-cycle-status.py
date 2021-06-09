import sys
sys.path.append("..")
from eoscskos import EoscSkos

translate_table = {ord('/'): 'SLASH', ord('+'): 'PLUS', ord('('): 'OPEN_PARENTHESIS', ord(')'): 'CLOSE_PARENTHESIS',
                   ord('&'): 'AMPERSAND', ord(','): 'COMMA'}

def createSkos():
    eosc = EoscSkos("LIFE_CYCLE_STATUS", "eosc-life-cycle-status", "EOSC Life Cycle Status List", "EOSC Life Cycle Status List from https://api.eosc-portal.eu/vocabulary/byType/LIFE_CYCLE_STATUS")
    eosc.createSkos()

createSkos()