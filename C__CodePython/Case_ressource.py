"""
Qui: Amory
Quand: 18-01-2024
Description: La case ressource est une case qui permet de donner au
joueur qui tombe dessus, de choisir entre l'une des 4 ressources pour
en recevoir une

"""

##########
# import #
##########

from Joueur import *

class Case_ressource():

    ################
    # constructeur #
    ################

    def __init__(self):

        self.__ressource_contenue:str = ""

    #############
    # affichage #
    #############
        
    def __str__(self):
        print("")
        
    ###########################
    # accesseurs et mutateurs #
    ###########################
        
    @property
    def ressource_contenue(self):
        return self.__ressource_contenue
    @ressource_contenue.setter
    def nom(self, val):
        self.__nom = val



    ############
    # methodes #
    ############
    
    def donnerRessource(self):
        pass