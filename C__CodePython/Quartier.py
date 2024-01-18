"""
Qui: Amory
Quand: 
- 18/01/2024
Description: Zone où les joueurs peuvent construire leurs bâtiments
s'ils ont les matériaux suffisant pour ajouter leurs bâtiments
"""

##########
# import #
##########

from Joueur import *

class Quartier():

    ################
    # constructeur #
    ################

    def __init__(self):
        pass

    #############
    # affichage #
    #############
        
    def __str__(self):
        print("")
        
    ###########################
    # accesseurs et mutateurs #
    ###########################
        
    @property
    def proprietaire(self):
        pass
    @proprietaire.setter
    def proprietaire(self, val):
        self.__proprietes = val