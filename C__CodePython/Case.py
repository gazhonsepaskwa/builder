"""
Qui: Amory
Quand: 
- 18/01/2024
Description: Case du plateau avec ou sans spécificité ou influence
sur la partie
"""

##########
# import #
##########

from Joueur import *

class Case():

    ################
    # constructeur #
    ################

    def __init__(self):
        self.__numero:int = 0

    #############
    # affichage #
    #############
        
    def __str__(self):
        print("")