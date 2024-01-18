"""
Qui: Nathan
Quand: 2021-05-23
Description: Classe Batiment, gere un batiment, ses etages et cetera.
"""

##########
# import #
##########

from Quartier import *



class Batiment():

    ################
    # constructeur #
    ################

    def __init__(self, quartier):
        self.__construisible: bool = False
        self.__nombreEtage: int = 0
        self.__quartier: Quartier = quartier


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
        pass
    @construisible.setter
    def construisible(self, val):
        self.__construisible = val


    """
    Le nombre d'etage d'un batiment
    """
    @property
    def nombreEtage(self):
        pass
    @construisible.setter
    def nombreEtage(self, val):
        self.__nombreEtage = val



    ############
    # methodes #
    ############
    
    def VerifQuantiteePion():
        pass