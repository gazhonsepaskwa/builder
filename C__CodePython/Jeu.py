"""
Qui: Amory
Quand: 
- 18/01/2024
Description: Le jeu Monopoly en lui même qui va pouvoir
être joué par les joueurs qui veulent bien y jouer
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
        
    #Le nombre joueur dans la partie
    
    @property
    def nbrDeJoueurs(self):
        return self.__nbrDeJoueurs
    @nbrDeJoueurs.setter
    def nbrDeJoueurs(self, val):
        self.__nbrDeJoueurs = val 

    #La liste des joueurs qui sont dans la partie

    @property
    def listeJoueurs(self):
        return self.__listeJoueurs
    @listeJoueurs.setter
    def listeJoueurs(self, val):
        self.__listeJoueurs = val

    #Le joueur qui joue son tour sur le moment

    @property
    def joueurActif(self):
        return self.__joueurActif
    @joueurActif.setter
    def joueurActif(self, val):
        self.__joueurActif = val

    #La fin de la partie quand l'une des conditions est faite

    @property
    def fini(self):
        return self.__fini
    @fini.setter
    def fini(self, val):
        self.__fini = val

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