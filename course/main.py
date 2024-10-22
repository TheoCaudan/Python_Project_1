import json
import argparse
import nmap

configurations = []
#add_config function
def add_config():
    print("Vous êtes dans le menu d'ajout de configuration \n")
    server_name = input("Entrez le nom du serveur: ")
    IP_address = input("Entrez l'adresse IP: ")
    os = input("Entrez le système d'exploitation: ")
    services = input("Entrez les services en cours d'exécution (séparés par des virgules): ").split(",")

    configuration = {
        "server_name": server_name,
        "IP_address": IP_address,
        "os": os,
        "services": [services.strip() for service in services]
    }

    configurations.append(configuration)

#modify_config function
def mod_config():
    print("Vous êtes dans le menu de modification de configuration \n")
    new_server_name = input("Entrez le nom du serveur: ")
    for config in configurations:
        if(config["server_name"] == new_server_name):
            new_IP_address = input("Entrez la nouvelle IP pour {new_IP_address}")
            config["IP_address"] = new_IP_address
            print(f'Configuration mise à jour pour {new_server_name}!')
            return
        print(f'Aucune configuration trouvée pour {new_server_name}.')

#delete_config function
def del_config():
    print("Vous êtes dans le menu de suppression de configuration \n")
    new_server_name = input("Entrez le nom du serveur à supprimer: ")
    configurations = [config for config in configurations if config["server_name"]!= new_server_name]
    print(f'Configuration supprimée pour {new_server_name}!')
            
#list_config function
def ls_config():
    print("Vous êtes dans le menu de listage de configuration \n")
    if not configurations:
        print("Aucune configuration enregistrée.")
        return
    print("Configurations enregistrées: \n")
    for i, config in enumerate(configurations, 1):
        print(f'{i}. {config["server_name"]}')
        print(f" -Adresse IP: {config['IP_address']}")
        print(f" -Système d'exploitation: {config['os']}")
        print(f" -Services: {','.join(config['services'])}")

#save_config function
def sav_config():
    print("Vous êtes dans le menu de sauvegarde de configuration: \n")
    file = input("Entrez le nom du fichier de sauvegarde (ex: configurations.json): ")
    with open(file, 'w') as f:
        json.dump(configurations, f)
    print(f"Configurations sauvegardées avec succès dans {file}!")

#rollback_config function
def rol_config():
    print("Vous êtes dans le menu de restauration de configuration: \n")
    file = input("Entrez le nom du fichier de sauvegarde à restaurer (ex: configurations.json): ")
    with open(file, 'r') as f:
        configurations = json.load(f)
    print(f"Configurations restaurées avec succès depuis {file}!")

#scanning_tool function
#def scan_config():













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
    add_config()
elif(choice == "2"):
    mod_config()
elif(choice == "3"):
    del_config()
elif(choice == "4"):
    ls_config()
elif(choice == "5"):
    sav_config()
elif(choice == "6"):
    rol_config
elif(choice == "7"):
    print("Outils de scan")
