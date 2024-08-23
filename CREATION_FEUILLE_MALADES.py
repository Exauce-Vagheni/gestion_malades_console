# importer le module openpy
from openpyxl import Workbook
# creation du classeur
classeur=Workbook()
# creation de la feuille des personnes malades
malades=classeur.create_sheet("MALADES_LIST")
# creation de l'entete comme premiere ligne de la feuille des personnes malades
entete=["NOM","POSTNOM","PRENOM","MALADIE","ETAT","DOCTEUR","ADRESSE","TEMPS DE CONVENLESCENCE"]
malades.append(entete)
# enregistrement du fichier 
classeur.save("MALADES.xlsx")
