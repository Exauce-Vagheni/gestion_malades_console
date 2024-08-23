# importer le module openpy
from openpyxl import load_workbook
# ouvrir le fichier excel deja enregistré
classeur=load_workbook("MALADES.xlsx")
# ouvrir la feuille des personnes malades
malades=classeur["MALADES_LIST"]
while True:
    print("Veuillez remplir le formulaire du nouveau malade")
    nom=input("Entrez le nom du malade: ")
    postnom=input("Entrez le postnom du malade: ")
    prenom=input("Entrez le prenom du malade: ")
    maladie=input("Entrez le nom de la maladie: ")
    etat=input("Le malade est dans quel etat: ")
    docteur=input("Quel est le docteur chargé du malade ?: ")
    adresse=input("Entrez l'adresse du malade': ")
    conv=input("Entrez le temps de convenlescence du malade: ")
    profil=[nom,postnom,prenom,maladie,etat,docteur,adresse,conv]
    # ajouter le tableau identite dans la feuille des personnes malades
    malades.append(profil)
    # enregistrer les donnees entrés 
    classeur.save('MALADES.xlsx')                                                          
