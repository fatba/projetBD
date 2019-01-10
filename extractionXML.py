from lxml import etree

tree = etree.parse("monfichier.xml")
for personne in tree.xpath("personne/nom"):
    print(personne.text)
