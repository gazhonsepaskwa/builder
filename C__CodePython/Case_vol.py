"""
Qui: Amory
Quand: 
- 18/01/2024
Description: La case vol, est une case qui permet à un joueur de voler
l'une des ressources d'un autre joueur.

"""

##########
# import #
##########

from Joueur import *
from Jeu import *
from Ressource import *

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
        
    #Ressources donné par la case même

    @property
    def voleur(self):
        return self.__voleur
    @voleur.setter
    def voleur(self, val):
        self.__voleur = val

    @property
    def victime(self):
        return self.__victime
    @victime.setter
    def victime(self, val):
        self.__victime = val

    ############
    # methodes #
    ############
        
    def voler(self):

        '''
        Case_vol.victime = menuDeroulant(Jeu.listeJoueurs)

        choix = menuDeroulant(tractopelle, bateau, camion, grue)
        '''

        if choix == "tractopelle":

            Case_vol.voleur.jetonsTractopelle += 1 
            Case_vol.victime.jetonsTractopelle -= 1 

        elif choix == "bateau":

            Case_vol.voleur.jetonsBateau += 1 
            Case_vol.victime.jetonsBateau -= 1

        elif choix == "camion":

            Case_vol.voleur.jetonsCamion += 1 
            Case_vol.victime.jetonsCamion -= 1

        elif choix == "grue":

            Case_vol.voleur.jetonsGrue += 1 
            Case_vol.victime.jetonsGrue -= 1 