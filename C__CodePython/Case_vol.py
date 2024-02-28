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
from Case import *

class Case_vol(Case):

    ################
    # constructeur #
    ################

    def __init__(self, num, pos):
        super().__init__(num, pos)
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
        
    def voler(self, voleur, listeJoueurs):

        '''
        self.__victime = menuDeroulant(Jeu.listeJoueurs)

        choix = menuDeroulant(tractopelle, bateau, camion, grue)
        '''

        # attribution de voleur et victime
        self.__voleur = voleur
        self.__victime = listeJoueurs[int(input(print(f"Choisissez le joueur victime parmis: {listeJoueurs} (via son numéro dans la liste) "))) -1]

        # Demande le type de ressource à voler | a changer !!!
        tmp = input("Quelle ressource voulez-vous voler ? ( 1: tractopelle | 2: bateau | 3: camion | 4: grue ) >>")
        if tmp == "1": choix = "tractopelle"
        elif tmp == "2": choix = "bateau"
        elif tmp == "3": choix = "camion"
        elif tmp == "4": choix = "grue"
        else: 
            print("Choix invalide")
            choix = "nada"

        

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