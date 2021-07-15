import sys
sys.path.append("..")
from eoscskos import EoscSkos
import requests
import json

def getData(data):
  populatedData = {}
  populatedData['name'] = ""
  if 'name' in data:
    populatedData['name'] = data['name']
  populatedData['description'] = ""
  if 'description' in data:
    populatedData['description'] = data['description']
  populatedData['type'] = ""
  if 'type' in data:
    populatedData['type'] = data['type']
  return populatedData

def findParentAndWriteData(parentId, vocabCategories, data):
  for idCat in list(vocabCategories.keys()):
    if (idCat == parentId):
      if "childs" not in vocabCategories[parentId]:
        vocabCategories[parentId]['childs'] = {}
      vocabCategories[idCat]['childs'][data['id']] = getData(data)
      return True
    if ('childs' in vocabCategories[idCat]):
      if findParentAndWriteData(parentId, vocabCategories[idCat]['childs'], data):
        return True
  return False

def getApiDataByType(apiType, vocabCategories):
  response = requests.get("https://api.eosc-portal.eu/vocabulary/byType/" + apiType)
  results = response.json()
  for result in results:
    if (result['parentId']):
      if not findParentAndWriteData(result['parentId'], vocabCategories, result):
        print("didn't found the parentId " + result['parentId'])
    else:
      vocabCategories[result['id']] = getData(result)

def constructHierarchy(vocabCategories):
  getApiDataByType("SUPERCATEGORY", vocabCategories)
  getApiDataByType("CATEGORY", vocabCategories)
  getApiDataByType("SUBCATEGORY", vocabCategories)
  print(vocabCategories)

def createSkos(vocabCategories):
  eosc = EoscSkos("SUPERCATEGORY", "eosc-resource-category", "EOSC Resource Category List",
    ("EOSC Resource Category List compiled from https://api.eosc-portal.eu/vocabulary/byType/SUPERCATEGORY, " +
    "https://api.eosc-portal.eu/vocabulary/byType/CATEGORY, and https://api.eosc-portal.eu/vocabulary/byType/SUBCATEGORY"))
  eosc.createHierarchicalSkos(vocabCategories)

vocabCategories = {}
constructHierarchy(vocabCategories)
createSkos(vocabCategories)

# todo: type should become a collection
