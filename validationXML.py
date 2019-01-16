from lxml import etree
from io import StringIO
import sys

def xmlvalide(monfichier):

	with open(monfichier, 'r') as xml_file:
    	xml_to_check = xml_file.read()

	try:
    	doc = etree.parse(StringIO(xml_to_check))
    	#print('Fichier valide.Syntax ok.')
    	return True

	except:
    	print('Fichier invalide. Syntax incorrect.')
    	return False
