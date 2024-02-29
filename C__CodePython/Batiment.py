"""
Qui: Nathan
Quand: 
- 18/01/2024
Description: Classe Batiment, gere un batiment, ses etages et cetera.
"""

##########
# import #
##########

from ursina import *


class Batiment(Button):

    ################
    # constructeur #
    ################

    def __init__(self, pos):
        super().__init__(
                model="cube",
                color=color.gray,
                texture= "white_cube",
                scale=(0.8,0.2,0.8),
                position=pos,
                parent=scene
            )
        self.__construisible: bool = False
        self.__Etages: int = 0


    #############
    # affichage #
    #############
        
    def __str__(self):
        print("")
        
    

    ###########################
    # accesseurs et mutateurs #
    ###########################
    
    """
    definit si un batiment est construisible ou non 
    """
    @property
    def construisible(self):
        return self.__construisible
    @construisible.setter
    def construisible(self, val):
        self.__construisible = val


    """
    Le nombre d'etage d'un batiment
    """
    @property
    def nombreEtage(self):
        return self.__nombreEtage
    @construisible.setter
    def nombreEtage(self, val):
        self.__nombreEtage = val


    """
    Le quartier auquel appartienst le batiment
    """
    @property
    def quartier(self):
        return self.__quartier
    @quartier.setter
    def nombreEtage(self, val):
        self.__quartier = val



    ############
    # methodes #
    ############
    
    """
    Verifie si le joueur a assez de pions pour construir un etage
    """
    def VerifQuantiteePion():
        pass