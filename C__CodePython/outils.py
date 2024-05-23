"""
Qui: Nathan
Quand: 
- 26/02/2024 Nathan
- 28/02/2024 Nathan
- 17/05/2024 Nathan
- 18/05/2024 Nathan
- 22/05/2024 Nathan
- 23/05/2024 Nathan
Description: outils de developpement
"""

# imports 
import shutil
from colorama import Fore, Style, init
import os
import sys


########################################
# retourne True si vrai et False sinon #
########################################

def ouiOuNon(question):
    oui = ["yes", "y", "oui", "o", "1"]
    non = ["no", "n", "non", "0"]

    while True:
        entree = input(question)

        if entree.lower() in oui:
            return True
        elif entree.lower() in non:
            return False
        else:
            print("Veuillez répondre par 'oui', 'non' ou une variante.")



###########################
# print avec des couleurs #
###########################

init(autoreset=True)

def colored_print(text, color):
    # couleurs dispo
    colors = {
        "black": Fore.BLACK,
        "red": Fore.RED,
        "green": Fore.GREEN,
        "yellow": Fore.YELLOW,
        "blue": Fore.BLUE,
        "magenta": Fore.MAGENTA,
        "cyan": Fore.CYAN,
        "white": Fore.WHITE,
        "reset": Style.RESET_ALL
    }
 
    if color not in colors:
        print(f"Invalid color '{color}'. Using default color.")
        color = "reset"

    print(f"{colors[color]}{text}{colors['reset']}")



############################
# séparateur pour terminal #
############################

def separator(caracter='-'):
    cols, _ = shutil.get_terminal_size()
    print(caracter * cols)



###################################
# Permet d'actualiser le terminal #
###################################S

def clear_terminal():
    if os.name == 'nt':  # Windows
        os.system('cls')
    else:  # Pour Linux, macOS, etc
        os.system('clear')



##########################
# Supp la dernière ligne # 
##########################

def delete_last_line():
    sys.stdout.write('\x1b[1A')  # Déplacer le curseur une ligne vers le haut
    sys.stdout.write('\x1b[2K')  # Effacer la ligne entière
    sys.stdout.flush()
