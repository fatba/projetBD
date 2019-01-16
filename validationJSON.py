import json


def jsonvalide(monfichier):
	try:
		json_file = open(monfichier).read()
		parsed_json = json.loads(json_file)	
		return True
	except Exception as e:
		print ('le fichier est invalide.')
		return False	
