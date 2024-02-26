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
from Case import *

class Case_propriete(Case):

    ################
    # constructeur #
    ################

    def __init__(self, num, pos, nom, prix, loyer):
        super().__init__(num, pos)
        self.__appartenu:Joueur = None
        self.__nom = nom
        self.__prix = prix
        self.__loyer = loyer



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
        return self.__appartenu
    @appartenu.setter
    def appartenu(self, val):
        self.__appartenu = val



    ############
    # methodes #
    ############
    
    def achat(self, joueur):

        if Case_propriete.apartenu == None:
            
            #Ici il y a la proposition d'acheter avec les boutons

            if joueur.argent > Case_propriete.prix :
        
                Banque.modifierBalance(joueur, - (Case_propriete.prix))
                Case_propriete.apartenu = joueur

            else:
                print("Vous êtes pauvre lol")

        else:

            Banque.envoyeur = joueur
            Banque.receveur = Case_propriete.apartenu

            if Banque.envoyer.argent > Case_propriete.loyer:

                Banque.transferer(Case_propriete.loyer)

            else:
                pass