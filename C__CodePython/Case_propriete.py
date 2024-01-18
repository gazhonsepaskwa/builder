"""
Qui: Nathan
Quand: 
- 18/01/2024
Description: case pouvant etre acheté et qui permet de construire 
les batiments quand le hamaux sont complet
"""

##########
# import #
##########

from Joueur import *

class Case_propriete():

    ################
    # constructeur #
    ################

    def __init__(self):
        self.__appartenu:Joueur = None
        self.__prix:int = 0
        self.__loyer:int = 0



    #############
    # affichage #
    #############
        
    def __str__(self):
        print("")
        
    

    ###########################
    # accesseurs et mutateurs #
    ###########################

    """
    Joueur à qui appartient la case
    """  
    @property
    def appartenu(self):
        pass
    @appartenu.setter
    def appartenu(self, val):
        self.__appartenu = val



    ############
    # methodes #
    ############
    
    def achat(self):
        pass