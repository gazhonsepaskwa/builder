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



# Initialisation du moteur graphique
app = Ursina()



########
# Code #
########

Jeu.joueurActif = Jeu.deterQuiCommence()
Jeu.preparer()

while not Jeu.fini:
    Jeu.jouerUnTour()

    if Jeu.fini:
        Jeu.finDePartie()
        break

    Jeu.joueurSuivant()