

import json

diction = {"nom": "Durand", "prenom": "Christophe", "date de naissance": "29/02/1981"}

#with open('json_file.json') as json_file:
#    json_to_dict = json.load(json_file)

def DictionnaireToJson(fiche):
    with open("dictionnaire.json", "a") as file:
        fichier = json.dump(fiche, file)



#print(diction)
#print(DictionnaireToJson(diction))