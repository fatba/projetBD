import json

# with open('monfichier.json') as json_data:
#     data_dict = json.load(json_data)

# data_str = json.dumps(data_dict)
# print(data_str[0]['glossary'])


def parseJSON(filePath):
	fichier = open(filePath)
	données =fichier.read()
	j = json.loads(données)
	return j

myJsonData = parseJSON("monfichier.json")
print(myJsonData['glossary'])
# import json

# with open('monfichier.json') as json_data:
#     data_dict = json.load(json_data)


