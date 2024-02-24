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
from Case import *

class Plateau(Entity):

    ################
    # constructeur #
    ################

    def __init__(self):
        super().__init__(
                model="cube",
                color=color.gray,
                scale=(10.5,0.1,10.5),
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
    def genererCases(self):

        # se prendra de la DB en temps voulu
        liste_positions = [ (4, 0, -4), 
                            (3, 0, -4), (2, 0, -4), (1, 0, -4), (0, 0, -4), (-1, 0, -4), (-2, 0, -4), (-3, 0, -4),
                            (-4, 0, -4),
                            (-4, 0, -3), (-4, 0, -2), (-4, 0, -1), (-4, 0, 0), (-4, 0, 1), (-4, 0, 2), (-4, 0, 3),
                            (-4, 0, 4),
                            (-3, 0, 4), (-2, 0, 4), (-1, 0, 4), (0, 0, 4), (1, 0, 4), (2, 0, 4), (3, 0, 4),
                            (4, 0, 4),
                            (4, 0, 3), (4, 0, 2), (4, 0, 1), (4, 0, 0), (4, 0, -1), (4, 0, -2), (4, 0, -3) ]
        i=0
        for i in range(len(liste_positions)):
            case = Case(i, liste_positions[i])
            self.caseListe.append(case)