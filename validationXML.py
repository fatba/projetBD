from lxml import etree
from io import StringIO
import sys

filename_xml = 'monfichier.xml'

with open(filename_xml, 'r') as xml_file:
    xml_to_check = xml_file.read()

try:
    doc = etree.parse(StringIO(xml_to_check))
    print('Fichier valide.Syntax ok.')

except:
    print('Fichier invalide. Syntax incorrect.')
