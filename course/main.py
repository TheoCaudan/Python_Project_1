import json
import nmap
import colorama
from colorama import init, Fore, Back, Style

# Initialisation de colorama
init(autoreset=True)

# declaration d'une variable globale accessible partout
configurations = []
# declaration d'une variable pour print le titre de menu
a = """

,-.                               
|  ) o                            
|-<  . ,-. ;-. . , ,-. ;-. . . ,-.
|  ) | |-' | | |/  |-' | | | | |-'
`-'  ' `-' ' ' '   `-' ' ' `-` `-'

"""
# fonction d'ajout de config
def add_config():
    print(Fore.CYAN + "Vous êtes dans le menu d'ajout de configuration \n")
    server_name = input("Entrez le nom du serveur: \n")
    IP_address = input("Entrez l'adresse IP: \n")
    os = input("Entrez le système d'exploitation (ex: Windows, centOS, Ubuntu, Debian, Mint): \n")
    services = input("Entrez les services en cours d'exécution (séparés par des virgules): \n").split(",")

    configuration = {
        "server_name": server_name,
        "IP_address": IP_address,
        "os": os,
        "services": [service.strip() for service in services]
    }

    configurations.append(configuration)

# fonction de modification d'adresse IP (pour le moment) pour le serveur donné
def mod_config():
    print(Fore.CYAN + "Vous êtes dans le menu de modification de configuration \n")
    new_server_name = input("Entrez le nom du serveur: \n")
    for config in configurations:
        if(config["server_name"] == new_server_name):
            new_server_name_actual = input(f"Entrez le nouveau nom du serveur (pressez Entrée pour ne pas modifier): \n")
            if new_server_name_actual:
                config['server_name'] = new_server_name_actual
            new_IP_address = input(f"Entrez la nouvelle IP pour {new_server_name} (pressez Entrée pour ne pas modifier): \n")
            if new_IP_address:
                config["IP_address"] = new_IP_address
            new_os = input(f"Entrez le nouvel système d'exploitation pour {new_server_name} (pressez Entrée pour ne pas modifier): \n")
            if new_os:
                config['os'] = new_os
            new_services = input(f"Entrez le(s) nouveau(x) services en cours d'exécution (séparés par des virgules) ou pressez Entrée pour ne pas modifier: \n").split(",")
            if new_services:
                config['services'] = [service.strip() for service in new_services]
            print(Fore.GREEN + f'Configuration mise à jour pour {new_server_name}!')
            return
        print(Fore.RED + f'Aucune configuration trouvée pour {new_server_name}.')

# fonction de suppression de config
def del_config():
    global configurations # necessaire pour que la fonction del_config accede à la variable globale
    print(Fore.CYAN + "Vous êtes dans le menu de suppression de configuration \n")
    new_server_name = input("Entrez le nom du serveur à supprimer: ")
    configurations = [config for config in configurations if config["server_name"] != new_server_name]
    print(Fore.GREEN + f'Configuration supprimée pour {new_server_name}!')

# fonction de listing des configs 
def ls_config():
    print("Vous êtes dans le menu de listage de configuration \n")
    if not configurations:
        print(Fore.RED + "Aucune configuration enregistrée.")
        return
    print(Fore.GREEN + "Configurations enregistrées: \n")
    for i, config in enumerate(configurations, 1):
        print(Fore.WHITE + f'\n{i}. {config["server_name"]}')
        print(Fore.WHITE + f" -Adresse IP: {config['IP_address']}")
        print(Fore.WHITE + f" -Système d'exploitation: {config['os']}")
        print(Fore.WHITE + f" -Services: {','.join(config['services'])}")

# fonction qui demande un nom de fichier et sauvegarde la config souhaitée dans un fichier .json
def sav_config():
    print(Fore.CYAN + "Vous êtes dans le menu de sauvegarde de configuration: \n")
    file = input("Entrez le nom du fichier de sauvegarde (ex: configurations.json): ")
    with open(file, 'w') as f:
        json.dump(configurations, f)
    print(Fore.GREEN + f"Configurations sauvegardées avec succès dans {file}!")

# permet de recuperer le json sauvegardé et le remettre à porter de main dans le menu
def rol_config():
    global configurations # necessaire pour que la fonction rol_config accede à la variable globale
    print(Fore.CYAN + "Vous êtes dans le menu de restauration de configuration: \n")
    file = input("Entrez le nom du fichier de sauvegarde à restaurer (ex: configurations.json): ")
    with open(file, 'r') as f:
        configurations = json.load(f)
    print(Fore.GREEN + f"Configurations restaurées avec succès depuis {file}!")

# outil de scan de port appelé par la fonction de scan 
def scan_ports(target):
    nm = nmap.PortScanner()
    print(Fore.MAGENTA + f"Scan en cours sur {target}... \n")    
    
    try: #permet de gerer les exceptions et continuer a executer meme si l'iteration precedente à echoué
        nm.scan(target, '1-1024')

        if target in nm.all_hosts():
            print(Fore.GREEN + f"Serveur actif: {target}")
            print(Fore.GREEN + " - Services détectés:")
            for proto in nm[target].all_protocols():
                lport = nm[target][proto].keys()
                for port in sorted(lport):
                    service_name = nm[target][proto][port]['name'] if 'name' in nm[target][proto][port] else 'Unknown'
                    print(Fore.GREEN + f"    - Port: {port} : {service_name}")
        else:
            print(Fore.RED + f"Aucune donnée trouvée pour {target}. Peut-être que l'hôte est hors-ligne.")
    except Exception as e: # gestion exception : ici elle signale l'erreur
        print(Fore.RED + f"Erreur lors du scan de {target} : {e}")

# fonction de scan : recupere une IP ou une plage d'IP et la decoupe pour identifier depart et arrivee dans le scan
def scan_config():
    print(Fore.CYAN + "Vous êtes dans le menu de scan \n")
    ip_range = input("Entrez la plage d'adresses IP à scanner (ex: 192.168.1.1 ou 192.168.1.1-192.168.1.10): \n")

    if '-' in ip_range:
        start_ip, end_ip = ip_range.split('-')
        start_ip_parts = list(map(int, start_ip.split('.')))
        end_ip_parts = list(map(int, end_ip.split('.')))

        print(Fore.CYAN + "Résultats du scan: \n")
        for i in range(start_ip_parts[2], end_ip_parts[2] + 1):
            ip_to_scan = f"{start_ip_parts[0]}.{start_ip_parts[1]}.{start_ip_parts[2]}.{i}"
            scan_ports(ip_to_scan)
    else:
        print(Fore.CYAN + "Résultats du scan: \n")
        scan_ports(ip_range)

# menu et display
def afficher_menu():
    global a
    print(Fore.CYAN + a)
    print(Fore.WHITE + "--- Menu ---")
    print(Fore.CYAN + "1. Ajouter une configuration")
    print(Fore.CYAN + "2. Modifier une configuration")
    print(Fore.CYAN + "3. Supprimer une configuration")
    print(Fore.CYAN + "4. Lister les configurations")
    print(Fore.CYAN + "5. Sauvegarder les configurations")
    print(Fore.CYAN + "6. Restaurer les configurations")
    print(Fore.CYAN + "7. Outils de Scan (Nmap)")
    print(Fore.CYAN + "8. Quitter le programme")
 
    while True:
        try:
            choix = int(input("Sélectionnez une option (1-8) : "))
            if 1 <= choix <= 8:
                return choix
            else:
                print(Fore.RED + "Erreur : Veuillez entrer un chiffre entre 1 et 8.")
        except ValueError:
            print(Fore.RED + "Erreur : Veuillez entrer un chiffre valide.")
 
# Main : gestion des choix utilisateurs
if __name__ == "__main__":
    while True:
        choix = afficher_menu()
 
        if choix == 1:
            add_config()
        elif choix == 2:
            mod_config()
        elif choix == 3:
            del_config()
        elif choix == 4:
            ls_config()
        elif choix == 5:
            sav_config()
        elif choix == 6:
            rol_config()
        elif choix == 7:
            scan_config()
        elif choix == 8:
            print(Fore.MAGENTA + "Fin du programme.")
            break  
 
        # une fois une operation executée on recharge le menu
        print(Fore.MAGENTA + "\nOpération terminée. Reproposition du menu...\n")
