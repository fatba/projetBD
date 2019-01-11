import json



try:
	json_file = open('monfichier.json').read()
	parsed_json = json.loads(json_file)	
	print('Fichier correct')
	#return True
except Exception as e:
	print ('le fichier est mal formate')
	#return False	
