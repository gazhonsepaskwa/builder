"""
Qui: Nathan
Quand: 
- 18/01/2024
Description: case pouvant etre acheté et qui permet de construire 
les batiments quand le hamaux sont complet
"""

##########
# import #
##########

from Joueur import *
from Banque import *

class Case_propriete():

    ################
    # constructeur #
    ################

    def __init__(self):
        self.__appartenu:Joueur = None
        self.__prix:int = 0
        self.__loyer:int = 0



    #############
    # affichage #
    #############
        
    def __str__(self):
        print("")
        
    

    ###########################
    # accesseurs et mutateurs #
    ###########################

    """
    Joueur à qui appartient la case
    """  
    @property
    def appartenu(self):
        pass
    @appartenu.setter
    def appartenu(self, val):
        self.__appartenu = val



    ############
    # methodes #
    ############
    
    def achat(self):

        if Case_propriete.apartenu == None:
            
            #Ici il y a la proposition d'acheter avec les boutons

            if Jeu.joueurActif.argent > Case_propriete.prix :
        
                Banque.modifierBalance(Jeu.joueurActif, - (Case_propriete.prix))
                Case_propriete.apartenu = Jeu.joueurActif

            else:
                print("Vous êtes pauvre")

        else:

            Banque.envoyeur = Jeu.joueurActif
            Banque.receveur = Case_propriete.apartenu

            if Banque.envoyer.argent > Case_propriete.loyer:

                Banque.transferer(Case_propriete.loyer)

            else:
                pass