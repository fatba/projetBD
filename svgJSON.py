import pip
import svgwrite
import XJ_convertor
import requests

if XJ_convertor.option == '-f':
    donneesJSON = XJ_convertor.parseJSON(XJ_convertor.monfichier)
elif XJ_convertor.inputType == '-h':
    response = requests.get(url = XJ_convertor.url)
    donneesJSON = response.json()

listEntites = []
# Recuperation de la liste des entités

for i in range(len(donneesJSON)):
    keys = donneesJSON[i].keys()
    key = next(iter(keys))
    listEntites.append(key)


# Initiation du fichier SVG
svg_document = svgwrite.Drawing(filename = XJ_convertor.svgFile,
                                debug = True)

entityCoordsList = []
# Recuperation des noms des entités que l'on enregistre dans la variable "listEntites"
print('Liste des entites et leurs attributs: ')
for i in range(len(listEntites)):
    listAttributs = []
    listAssocs = []

    print('\t' + listEntites[i])

    # Recuperation des noms des attributs que l'on enregistre dans la variable "listAttributs"
    nbAttributs = len(donneesJSON[i][listEntites[i]][0].keys())

    for key in donneesJSON[i][listEntites[i]][0].keys():
        listAttributs.append(key)
        print('\t\t' + key)


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

# ---------------

# print(svg_document.tostring())

for i in range(len(listEntites)):
      nbAssocs = len(donneesJSON[i]['relation']['associations'])

    for j in range(nbAssocs):
           
            nomAutreEntite = donneesJSON[i]['relation']['associations'][j]["nomAutreEntite"]
             nomAssoc = donneesJSON[i]['relation']['associations'][j]["nomAssoc"]

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
import pip
import svgwrite
import XJ_convertor
import requests

if XJ_convertor.option == '-f':
    donneesJSON = XJ_convertor.parseJSON(XJ_convertor.monfichier)
elif XJ_convertor.inputType == '-h':
    response = requests.get(url = XJ_convertor.url)
    donneesJSON = response.json()

listEntites = []
# Recuperation de la liste des entités

for i in range(len(donneesJSON)):
    keys = donneesJSON[i].keys()
    key = next(iter(keys))
    listEntites.append(key)


# Initiation du fichier SVG
svg_document = svgwrite.Drawing(filename = XJ_convertor.svgFile,
                                debug = True)

entityCoordsList = []
# Recuperation des noms des entités que l'on enregistre dans la variable "listEntites"
print('Liste des entites et leurs attributs: ')
for i in range(len(listEntites)):
    listAttributs = []
    listAssocs = []

    print('\t' + listEntites[i])

    # Recuperation des noms des attributs que l'on enregistre dans la variable "listAttributs"
    nbAttributs = len(donneesJSON[i][listEntites[i]][0].keys())

    for key in donneesJSON[i][listEntites[i]][0].keys():
        listAttributs.append(key)
        print('\t\t' + key)


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

# ---------------

# print(svg_document.tostring())

for i in range(len(listEntites)):
      nbAssocs = len(donneesJSON[i]['relation']['associations'])

    for j in range(nbAssocs):
           
            nomAutreEntite = donneesJSON[i]['relation']['associations'][j]["nomAutreEntite"]
             nomAssoc = donneesJSON[i]['relation']['associations'][j]["nomAssoc"]

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
