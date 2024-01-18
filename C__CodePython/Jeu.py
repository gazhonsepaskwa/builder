"""
Qui: Nathan Amory
Quand: 2021-05-23
Description: 

"""

##########
# import #
##########

from Joueur import *

class Jeu():

    ################
    # constructeur #
    ################

    def __init__(self):
        self.__nbrDeJoueurs:int = 0
        self.__listeJoueurs = []
        self.__joueurActif


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