import json
import argparse

#main function
print("Choisir une option :")
print("1 - Ajouter configuration")
print("2 - Modifier configuration")
print("3 - Supprimer configuration")
print("4 - Lister configuration")
print("5 - Sauvegarder configuration")
print("6 - Restaurer configuration")
print("7 - Outils de scan")
choice = input(str("Selectionner le numero correspondant à l'option souhaitée\n"))
if(choice == "1"):
    print("Ajouter une configuration")
elif(choice == "2"):
    print("Modifier une configuration")
elif(choice == "3"):
    print("Supprimer une configuration")
elif(choice == "4"):
    print("Lister les configurations")
elif(choice == "5"):
    print("Sauvegarder une configuration")
elif(choice == "6"):
    print("Restaurer une configuration")
elif(choice == "7"):
    print("Outils de scan")

#add_config function

#modify_config function

#delete_config function

#list_config function

#save_config function

#rollback_config function

#scanning_tool function