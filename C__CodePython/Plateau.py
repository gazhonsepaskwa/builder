"""
Qui: Amory
Quand: 
- 18/01/2024
Description: Le plateau de jeu sur lesquels les joueurs vont pouvoir
se déplacer lors de la partie
"""

##########
# import #
##########

from Joueur import *
from ursina import *

class Plateau(Entity):

    ################
    # constructeur #
    ################

    def __init__(self):
        super().__init__(
                model="cube",
                color=color.gray,
                scale=(5,0.1,5),
                position=(0,-1,0),
            )

    #############
    # affichage #
    #############
        
    def __str__(self):
        print("")