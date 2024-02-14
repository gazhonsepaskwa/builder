"""
Qui: Amory
Quand: 
- 18/01/2024
Description: La case ressource est une case qui permet de donner au
joueur qui tombe dessus, de choisir entre l'une des 4 ressources pour
en recevoir une

"""

##########
# import #
##########

from Jeu import *
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
        
    #Ressources donné par la case même

    @property
    def ressource_contenue(self):
        return self.__ressource_contenue
    @ressource_contenue.setter
    def ressource_contenue(self, val):
        self.__ressource_contenue = val

    ############
    # methodes #
    ############
    
    #Donne le type de ressource que la case propose quand on tombe dessus

    def donnerRessource(self):
        if (Case_ressource.ressource_contenue == "tractopelle"):
            Jeu.Joueur.Actif.jetonsTractopelle += 2
        
        elif (Case_ressource.ressource_contenue == "bateau"):
            Jeu.Joueur.Actif.jetonsBateau += 2

        elif (Case_ressource.ressource_contenue == "camion"):
            Jeu.Joueur.Actif.jetonsCamion += 2

        elif (Case_ressource.ressource_contenue == "grue"):
            Jeu.Joueur.Actif.jetonsBateau += 2
