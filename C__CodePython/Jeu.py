"""
Qui: Amory
Quand: 18/01/2023
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
        self.__joueurActif = 0
        self.__fini = False


    #############
    # affichage #
    #############
        
    def __str__(self):
        print("")
        
    

    ###########################
    # accesseurs et mutateurs #
    ###########################
        
    @property
    def nbrDeJoueurs(self):
        return self.__nbrDeJoueurs
    @nbrDeJoueurs.setter
    def nbrDeJoueurs(self, val):
        self.__val = 

    @property
    def listeJoueurs(self):
        return self.__listeJoueurs
    @listeJoueurs.setter
    def listeJoueurs(self, val):
        self.__val

    @property
    def joueurActif(self):
        return self.__joueurActif
    @joueurActif.setter
    def joueurActif(self, val):
        self.__val

    @property
    def fini(self):
        return self.__fini
    @fini.setter
    def fini(self, val):
        self.__val

    ############
    # methodes #
    ############
    
    def preparer(self):
        pass

    def jouerUnTour(self):
        pass

    def choixNbrJoueur(self):
        pass

    def changerJoueurActif(self):
        pass