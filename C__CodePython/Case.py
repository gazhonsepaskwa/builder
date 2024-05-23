"""
Qui: Amory et Nathan
Quand: 
- 18/01/2024 Amory
- 15/02/2024 Nathan 
- 24/02/2024 Nathan
- 29/02/2024 Nathan
Description: Case du plateau avec ou sans spécificité ou influence
sur la partie
"""

##########
# import #
##########

from Joueur import *
from ursina import *

class Case(Entity):

    ################
    # constructeur #
    ################

    def __init__(self, num, pos, couleur = color.white, texture = "white_cube"):
        super().__init__(
                model="cube",
                color=couleur,
                texture= texture,
                scale=(1,0.2,1),
                position=pos,
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
        print("Bonjour, je suis la case !")