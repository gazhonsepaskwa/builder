"""
Qui: Nathan Amory
Quand: 
- 18/01/2024
Description: 

"""

##########
# import #
##########

from ursina import *
from Jeu import *



########
# Code #
########

# Initialisation du moteur graphique
app = Ursina()

jeu = Jeu()
jeu.preparer()

while not jeu.fini:
    jeu.jouerUnTour()

    if jeu.fini:
        jeu.finDePartie()
        break

    jeu.joueurSuivant()