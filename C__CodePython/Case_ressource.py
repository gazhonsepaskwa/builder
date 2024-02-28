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

class Case_ressource(Case):

    ################
    # constructeur #
    ################

    def __init__(self, num, pos, ressource):
        super().__init__(num, pos)
        self.__ressource_contenue:str = ressource

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

    def donnerResource(self, joueur):
        if (self.__ressource_contenue == "tractopelle"):
            joueur.jetonsTractopelle += 2
            print(f"Vous recevez 2 jetons tractopelle")
        
        elif (self.__ressource_contenue == "bateau"):
            joueur.jetonsBateau += 2
            print(f"Vous recevez 2 jetons bateau")

        elif (self.__ressource_contenue == "camion"):
            joueur.jetonsCamion += 2
            print(f"Vous recevez 2 jetons camion")

        elif (self.__ressource_contenue == "grue"):
            joueur.jetonsBateau += 2
            print(f"Vous recevez 2 jetons grue")
