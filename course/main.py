import json
import nmap

configurations = []

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
        "services": [service.strip() for service in services]
    }

    configurations.append(configuration)

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

def del_config():
    print("Vous êtes dans le menu de suppression de configuration \n")
    new_server_name = input("Entrez le nom du serveur à supprimer: ")
    configurations = [config for config in configurations if config["server_name"] != new_server_name]
    print(f'Configuration supprimée pour {new_server_name}!')

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

def sav_config():
    print("Vous êtes dans le menu de sauvegarde de configuration: \n")
    file = input("Entrez le nom du fichier de sauvegarde (ex: configurations.json): ")
    with open(file, 'w') as f:
        json.dump(configurations, f)
    print(f"Configurations sauvegardées avec succès dans {file}!")

def rol_config():
    print("Vous êtes dans le menu de restauration de configuration: \n")
    file = input("Entrez le nom du fichier de sauvegarde à restaurer (ex: configurations.json): ")
    with open(file, 'r') as f:
        configurations = json.load(f)
    print(f"Configurations restaurées avec succès depuis {file}!")

#scanning_tool function for scan_config to use after getting ips
def scan_ports(target):
    nm = nmap.PortScanner()
    print(f"Scan en cours sur {target}... \n")    
    
    try:
        nm.scan(target, '1-1024')

        if target in nm.all_hosts():
            print(f"Serveur actif: {target}")
            print(" - Services détectés:")
            for proto in nm[target].all_protocols():
                lport = nm[target][proto].keys()
                for port in sorted(lport):
                    service_name = nm[target][proto][port]['name'] if 'name' in nm[target][proto][port] else 'Unknown'
                    print(f"    - Port: {port} : {service_name}")
        else:
            print(f"Aucune donnée trouvée pour {target}. Peut-être que l'hôte est hors-ligne.")
    except Exception as e:
        print(f"Erreur lors du scan de {target} : {e}")

def scan_config():
    print("Vous êtes dans le menu de scan \n")
    ip_range = input("Entrez la plage d'adresses IP à scanner (ex: 192.168.1.1 ou 192.168.1.1-192.168.1.10): \n")

    if '-' in ip_range:
        start_ip, end_ip = ip_range.split('-')
        start_ip_parts = list(map(int, start_ip.split('.')))
        end_ip_parts = list(map(int, end_ip.split('.')))

        print("Résultats du scan: \n")
        for i in range(start_ip_parts[2], end_ip_parts[2] + 1):
            ip_to_scan = f"{start_ip_parts[0]}.{start_ip_parts[1]}.{start_ip_parts[2]}.{i}"
            scan_ports(ip_to_scan)
    else:
        print("Résultats du scan: \n")
        scan_ports(ip_range)

def afficher_menu():
    print("\n--- Menu ---")
    print("1. Ajouter une configuration")
    print("2. Modifier une configuration")
    print("3. Supprimer une configuration")
    print("4. Lister les configurations")
    print("5. Sauvegarder les configurations")
    print("6. Restaurer les configurations")
    print("7. Outils de Scan (Nmap)")
    print("8. Quitter le programme")
 
    while True:
        try:
            choix = int(input("Sélectionnez une option (1-8) : "))
            if 1 <= choix <= 8:
                return choix
            else:
                print("Erreur : Veuillez entrer un chiffre entre 1 et 8.")
        except ValueError:
            print("Erreur : Veuillez entrer un chiffre valide.")
 
# Main : Manage user choice
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
            print("Fin du programme.")
            break  
 
        #Everytime menu is coming back
        print("\nOpération terminée. Reproposition du menu...\n")
