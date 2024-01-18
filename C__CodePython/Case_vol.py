"""
Qui: Amory
Quand: 18/01/2024
Description: La case vol, est une case qui permet à un joueur de voler
l'une des ressources d'un autre joueur.

"""

##########
# import #
##########

from Joueur.py import *

class Case_vol():

    ################
    # constructeur #
    ################

    def __init__(self):

        self.__voleur:Joueur = None
        self.__victime:Joueur = None



    #############
    # affichage #
    #############
        
    def __str__(self):
        print("")
        
    

    ###########################
    # accesseurs et mutateurs #
    ###########################
        
    @property
    def nom(self):
        pass
    @nom.setter
    def nom(self, nom):
        self.__nom = nom



    ############
    # methodes #
    ############
    
    def methode(self):
        pass