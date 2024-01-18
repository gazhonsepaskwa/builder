"""
Qui: Amory
Quand: 
- 18/01/2024
Description: La case vol, est une case qui permet à un joueur de voler
l'une des ressources d'un autre joueur.

"""

##########
# import #
##########

from Joueur import *

class Case_vol():

    ################
    # constructeur #
    ################

    def __init__(self):

        self.__voleur:Joueur = None
        self.__victime:Joueur = None

    #############
    # affichage #
    #############
        
    def __str__(self):
        print("")