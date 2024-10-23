import json
import nmap
import colorama
from colorama import init, Fore, Back, Style

# Initialisation de colorama
init(autoreset=True)

# Déclaration d'une variable globale accessible partout
configurations = []

# Fonction d'ajout de config
def add_config():
    print(Fore.CYAN + "Vous êtes dans le menu d'ajout de configuration \n")
    server_name = input("Entrez le nom du serveur: ")
    IP_address = input("Entrez l'adresse IP: ")
    os = input("Entrez le système d'exploitation (ex: Windows, centOS, Ubuntu, Debian, Mint): \n")
    services = input("Entrez les services en cours d'exécution (séparés par des virgules): ").split(",")

    configuration = {
        "server_name": server_name,
        "IP_address": IP_address,
        "os": os,
        "services": [service.strip() for service in services]
    }

    configurations.append(configuration)

# Fonction de modification d'adresse IP
def mod_config():
    print(Fore.CYAN + "Vous êtes dans le menu de modification de configuration \n")
    new_server_name = input("Entrez le nom du serveur: ")
    for config in configurations:
        if config["server_name"] == new_server_name:
            new_IP_address = input(f"Entrez la nouvelle IP pour {new_server_name}: \n")
            config["IP_address"] = new_IP_address
            print(Fore.GREEN + f'Configuration mise à jour pour {new_server_name}!')
            return
    print(Fore.RED + f'Aucune configuration trouvée pour {new_server_name}.')

# Fonction de suppression de config
def del_config():
    global configurations
    print(Fore.CYAN + "Vous êtes dans le menu de suppression de configuration \n")
    new_server_name = input("Entrez le nom du serveur à supprimer: ")
    configurations[:] = [config for config in configurations if config["server_name"] != new_server_name]
    print(Fore.GREEN + f'Configuration supprimée pour {new_server_name}!')

# Fonction de listing des configs
def ls_config():
    print(Fore.CYAN + "Vous êtes dans le menu de listage de configuration \n")
    if not configurations:
        print(Fore.YELLOW + "Aucune configuration enregistrée.")
        return
    print(Fore.GREEN + "Configurations enregistrées: \n")
    for i, config in enumerate(configurations, 1):
        print(f'{i}. {config["server_name"]}')
        print(f" - Adresse IP: {config['IP_address']}")
        print(f" - Système d'exploitation: {config['os']}")
        print(f" - Services: {', '.join(config['services'])}")

# Fonction de sauvegarde de configuration
def sav_config():
    print(Fore.CYAN + "Vous êtes dans le menu de sauvegarde de configuration: \n")
    file = input("Entrez le nom du fichier de sauvegarde (ex: configurations.json): ")
    with open(file, 'w') as f:
        json.dump(configurations, f)
    print(Fore.GREEN + f"Configurations sauvegardées avec succès dans {file}!")

# Fonction de restauration de configuration
def rol_config():
    global configurations
    print(Fore.CYAN + "Vous êtes dans le menu de restauration de configuration: \n")
    file = input("Entrez le nom du fichier de sauvegarde à restaurer (ex: configurations.json): ")
    with open(file, 'r') as f:
        configurations[:] = json.load(f)
    print(Fore.GREEN + f"Configurations restaurées avec succès depuis {file}!")

# Outil de scan de port
def scan_ports(target):
    nm = nmap.PortScanner()
    print(Fore.CYAN + f"Scan en cours sur {target}... \n")
    
    try:
        nm.scan(target, '1-1024')
        if target in nm.all_hosts():
            print(Fore.GREEN + f"Serveur actif: {target}")
            print(" - Services détectés:")
            for proto in nm[target].all_protocols():
                lport = nm[target][proto].keys()
                for port in sorted(lport):
                    service_name = nm[target][proto][port].get('name', 'Unknown')
                    print(f"    - Port: {port} : {service_name}")
        else:
            print(Fore.YELLOW + f"Aucune donnée trouvée pour {target}. Peut-être que l'hôte est hors-ligne.")
    except Exception as e:
        print(Fore.RED + f"Erreur lors du scan de {target} : {e}")

# Fonction de scan de configuration
def scan_config():
    print(Fore.CYAN + "Vous êtes dans le menu de scan \n")
    ip_range = input("Entrez la plage d'adresses IP à scanner (ex: 192.168.1.1 ou 192.168.1.1-192.168.1.10): \n")

    if '-' in ip_range:
        start_ip, end_ip = ip_range.split('-')
        start_ip_parts = list(map(int, start_ip.split('.')))
        end_ip_parts = list(map(int, end_ip.split('.')))

        print(Fore.GREEN + "Résultats du scan: \n")
        for i in range(start_ip_parts[2], end_ip_parts[2] + 1):
            ip_to_scan = f"{start_ip_parts[0]}.{start_ip_parts[1]}.{start_ip_parts[2]}.{i}"
            scan_ports(ip_to_scan)
    else:
        print(Fore.GREEN + "Résultats du scan: \n")
        scan_ports(ip_range)

# Menu et display
def afficher_menu():
    print(Fore.BLUE + "\n--- Menu ---")
    print(Fore.YELLOW + "1. Ajouter une configuration")
    print(Fore.YELLOW + "2. Modifier une configuration")
    print(Fore.YELLOW + "3. Supprimer une configuration")
    print(Fore.YELLOW + "4. Lister les configurations")
    print(Fore.YELLOW + "5. Sauvegarder les configurations")
    print(Fore.YELLOW + "6. Restaurer les configurations")
    print(Fore.YELLOW + "7. Outils de Scan (Nmap)")
    print(Fore.YELLOW + "8. Quitter le programme")

    while True:
        try:
            choix = int(input(Fore.MAGENTA + "Sélectionnez une option (1-8) : "))
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
            print(Fore.GREEN + "Fin du programme.")
            break  
 
        print(Fore.CYAN + "\nOpération terminée. Reproposition du menu...\n")
