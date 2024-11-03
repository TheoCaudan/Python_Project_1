# Network Configuration and Scanning Tool

This project is a Python-based command-line tool for managing network configurations and performing port scans using Nmap. It allows users to add, modify, delete, list, save, and restore configurations of servers, as well as scan IP addresses for active services and operating systems.

## Features

- **IP Address Validation**: Ensures that entered IP addresses are in a valid format.
- **Configuration Management**:
  - Add new server configurations.
  - Modify existing server configurations.
  - Delete server configurations.
  - List all saved server configurations.
  - Save configurations to a JSON file.
  - Restore configurations from a JSON file.
- **Port Scanning**: Utilize Nmap to scan specified IP addresses or ranges for open ports and services, including OS detection.

## Requirements

To run this project, you'll need:

- Python 3.6 or higher
- Nmap installed on your system
- Required Python packages:
  - `nmap`
  - `colorama`

You can install the required packages using pip:

```bash
pip install python-nmap colorama
```

## Installation

1. Clone the repository or download the source code.

   ```bash
   git clone https://github.com/yourusername/network-scanner.git
   cd network-scanner
   ```

2. Ensure that Nmap is installed on your system. For installation instructions, visit [Nmap's official site](https://nmap.org/download.html).

## Usage

1. **Run the Program**:

   Execute the script from your terminal:

   ```bash
   python main.py
   ```

2. **Menu Options**:

   Upon starting the program, you'll see the main menu with the following options:

   ```
   ╔═════════════════════════╗
   ║        MAIN MENU        ║
   ╚═════════════════════════╝

   1. Ajouter une configuration
   2. Modifier une configuration
   3. Supprimer une configuration
   4. Lister les configurations
   5. Sauvegarder les configurations
   6. Restaurer les configurations
   7. Outils de Scan (Nmap)
   8. Quitter le programme
   ```

3. **Adding a Configuration**:

   Choose option 1 to add a new server configuration. You'll be prompted to enter the server name, IP address, operating system, and running services.

4. **Modifying a Configuration**:

   Choose option 2 to modify an existing configuration by entering the server name and the new details.

5. **Deleting a Configuration**:

   Choose option 3 to remove a configuration by providing the server name.

6. **Listing Configurations**:

   Option 4 allows you to display all saved configurations.

7. **Saving Configurations**:

   With option 5, you can save all configurations to a JSON file for later retrieval.

8. **Restoring Configurations**:

   Option 6 lets you restore configurations from a previously saved JSON file.

9. **Scanning IPs**:

   Choose option 7 to perform a port scan on a specific IP address or range. You will see a list of active ports and detected services.

10. **Exiting the Program**:

    Select option 8 to exit the program gracefully.

## Code Overview

The main functionalities are implemented as follows:

- **IP Validation**: Uses regex to validate IP addresses.
- **Configuration Management Functions**:
  - `add_config()`: Adds a new server configuration.
  - `mod_config()`: Modifies an existing configuration.
  - `del_config()`: Deletes a configuration.
  - `ls_config()`: Lists all configurations.
  - `sav_config()`: Saves configurations to a JSON file.
  - `rol_config()`: Restores configurations from a JSON file.
- **Port Scanning**:
  - `scan_ports(target)`: Scans specified IPs and retrieves open ports and services.
  - `scan_config()`: Manages user input for IP scanning.

## Troubleshooting

- If you encounter an error regarding Nmap not being found, ensure Nmap is installed and properly added to your system's PATH.
- For issues with IP validation, make sure you input valid IP formats.

## License

This project is open source and available under the [MIT License](LICENSE).

## Acknowledgements

- [Nmap](https://nmap.org/) for providing the powerful network scanning tool.
- [Colorama](https://pypi.org/project/colorama/) for enhancing terminal output.
