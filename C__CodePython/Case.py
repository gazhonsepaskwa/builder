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
from ursina import *

class Case():

    ################
    # constructeur #
    ################

    def __init__(self, num):
        super().__init__(
                model="cube",
                color=color.blue,
                scale=(1,0.2,1),
                position=(1,0,1),
            )
        
        self.__numero:int = num



    ################
    ### get, set ###
    ################

    @property
    def numero(self):
        return self.__numero
    

    #############
    # affichage #
    #############
        
    def __str__(self):
        print("")