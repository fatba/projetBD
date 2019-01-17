import xml.etree.cElementTree as ET
import pip
import svgwrite
import parsingXml
import XJ_convertor


donnéesXml = parsingXml.getEntites(XJ_convertor.monfichier)
relations = parsingXml.Relations(XJ_convertor.monfichier)
listEntites = []

# Recuperation de la liste des entités

for entite in myJsonData:
    
    listEntites.append(entite)


# Initiation du fichier SVG
svg_document = svgwrite.Drawing(filename = XJ_convertor.svgFile,
                                debug = True)


# Recuperation des noms des entités que l'on enregistre dans la variable "listEntites"
i=0
entityCoordsList = []
for entite in myJsonData:
    listAttributs = []


    # Recuperation des noms des attributs que l'on enregistre dans la variable "listAttributs"

    for key in myJsonData[entite]['attributs']:
        listAttributs.append(key)
        


    if (i % 2 == 0):
        # Creation du rectangle contenant les infos de l'entité
        svg_document.add(svg_document.rect(insert = (10, i*150 + 10),
                                           size = ("150px", "130px"),
                                           stroke_width = "1",
                                           stroke = "black",
                                           fill = "rgb(205, 205, 40)"))
        entityCoords = {
            "nomEntite": listEntites[i],
            "coordX": 10,
            "coordY": i*150 + 10
        }
        entityCoordsList.append(entityCoords)

        svg_document.add(svg_document.rect(insert = (10, i*150 + 10),
                                           size = ("150px", "26px"),
                                           stroke_width = "1",
                                           stroke = "black",
                                           fill = "rgb(205, 205, 40)"))


        # Affichage du nom de l'entité
        svg_document.add(svg_document.text(listEntites[i],
            insert=(20, i*150 + 30),
            stroke='none',
            fill="rgb(42, 42, 42)",
            font_size='15px',
            font_weight="bold")
        )

        # Affichage de la liste des attributs
        for k in range(len(listAttributs)):
            svg_document.add(svg_document.text(listAttributs[k],
                insert=(20, i*150 + 40 + (k+1)*20),
                stroke='none',
                fill="rgb(15, 15, 15)",
                font_size='15px',
                font_weight="bold")
            )
    else:
        # Creation du rectangle contenant les infos de l'entité
        svg_document.add(svg_document.rect(insert = (400, (i - 1)*150 + 10),
                                           size = ("150px", "130px"),
                                           stroke_width = "1",
                                           stroke = "black",
                                           fill = "rgb(205, 205, 40)"))

        entityCoords = {
            "nomEntite": listEntites[i],
            "coordX": 400,
            "coordY": (i - 1)*150 + 10
        }
        entityCoordsList.append(entityCoords)

        svg_document.add(svg_document.rect(insert = (400, (i - 1)*150 + 10),
                                           size = ("150px", "26px"),
                                           stroke_width = "1",
                                           stroke = "black",
                                           fill = "rgb(209, 250, 46)"))



        # Affichage du nom de l'entité
        svg_document.add(svg_document.text(listEntites[i],
            insert=(410, (i - 1)*150 + 30),
            stroke='none',
            fill="rgb(15, 15, 15)",
            font_size='15px',
            font_weight="bold")
        )

        # Affichage de la liste des attributs
        for k in range(len(listAttributs)):
            svg_document.add(svg_document.text(listAttributs[k],
                insert=(410, (i - 1)*150 + 40 + (k+1)*20),
                stroke='none',
                fill="rgb(15, 15, 15)",
                font_size='15px',
                font_weight="bold")
            )
    i++

# ---------------

# print(svg_document.tostring())

for i in range(len(listEntites)):
    # Recuperations des differentes associations
    # nbAssocs = len(myJsonData[i]['relation']['associations'])
    nbAssocs = len(myJsonData[i]['relation']['associations'])

    for j in range(nbAssocs):
            
            nomAutreEntite = myJsonData[i]['relation']['associations'][j]["nomAutreEntite"]
            
            nomAssoc = myJsonData[i]['relation']['associations'][j]["nomAssoc"]

            for k in range(len(entityCoordsList)):
                if entityCoordsList[k]['nomEntite'] == listEntites[i]:
                        debutLigneX = entityCoordsList[k]['coordX'] 
                        debutLigneY = entityCoordsList[k]['coordY'] + 65
                if entityCoordsList[k]['nomEntite'] == nomAutreEntite:
                        finLigneX = entityCoordsList[k]['coordX'] + 150
                        finLigneY = entityCoordsList[k]['coordY'] + 65

                        svg_document.add(svg_document.line(
                            (debutLigneX, debutLigneY),
                            (finLigneX, finLigneY),
                            stroke_width = "3",
                            stroke="rgb(15, 15, 15)"))

                            


                            # Affichage du nom de l'association
                        svg_document.add(svg_document.text(nomAssoc,
                            insert=((finLigneX - debutLigneX) / 2 + debutLigneX, finLigneY - 10),
                            stroke='none',
                            fill="rgb(15, 15, 15)",
                            font_size='15px',
                            font_weight="bold")
                        )

svg_document.save()

