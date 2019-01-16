import sys
import validationJSON
import os


if len(sys.argv) == :7

    typefic = sys.argv[2]
    option = sys.argv[3]
    
    
    if option == '-h':
       	url = sys.argv[4]

    elif option == '-f':
       	monfichier = sys.argv[4]
        nomfic, ext = os.path.splitext(monfichier)
        ext = ext.lower()

    ficSVG = sys.argv[6]


    if __name__ == "__main__" :
    	if option == '-f':
    		if not(os.path.exists(monfichier)):
                print('!!!Ce fichier n\'existe pas!!!')
            else:
                if typefic == 'json':
                   
                    if (ext != '.json'):
                        print('!!!Ce fichier n\'est pas un fichier JSON!!!')
                    else:
                        if validationJSON.jsonvalide(monfichier):
                            import fichiersvgjson
                        else:
                            print(validationJSON.jsonvalide(monfichier))

                elif typefic == "xml":
                    if (ext != '.xml'):
                        print('!!!Ce fichier n\'est pas un fichier XML!!!')
                    else:
                        if validationXML.xmlvalide(monfichier):
                            import fichiersvgxml
                        else:
                            validationXML.xmlvalide(monfichier)
                else:
                    print("!!!Le type du fichier specifie est incorrect!!!")


        elif option == '-h':
        	
          
                    
else:
    print('!!!Nombre d\'arguments incorrect!!!')
