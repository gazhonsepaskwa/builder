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
        pass
    @nbrDeJoueurs.setter
    def nbrDeJoueurs(self):
        pass

    @property
    def listeJoueurs(self):
        pass
    @listeJoueurs.setter
    def listeJoueurs(self):
        pass

    @property
    def joueurActif(self):
        pass
    @joueurActif.setter
    def joueurActif(self):
        pass

    @property
    def fini(self):
        pass
    @fini.setter
    def fini(self):
        pass

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