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
                scale=(10,0.1,10),
                position=(0,0,0),
            )

        self.__caseListe:list = []


    
    ################
    ### get, set ###
    ################
        
    @property
    def caseListe(self):
        return self.__caseListe
    @caseListe.setter
    def caseListe(self, val):
        self.__caseListe = val



    #############
    # affichage #
    #############
        
    def __str__(self):
        print("")


    ############
    # methodes #
    ############
        
    # permet de genere les cases du jeu
    def genererCases():
        pass