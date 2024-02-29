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
from Batiment import *
import outils as outils
from ursina import *

class Case_propriete(Case):

    ################
    # constructeur #
    ################

    def __init__(self, num, pos, nom, prix, loyer, posBatiment, numHamaux):
        super().__init__(num, pos, couleur=color.blue)
        self.__appartenu:Joueur = None
        self.__nom = nom
        self.__prix = prix
        self.__loyer = loyer
        self.__batiments = Batiment(posBatiment)
        self.numHamaux = numHamaux



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
    
    def achat(self, joueur, banque):

        if self.__appartenu == None:
            
            #a modif pour mettre des boutons

            if outils.ouiOuNon("Voulez-vous acheter la propriété " + self.__nom + "?"):

                if joueur.argent > self.__prix :
            
                    banque.modifierBalance(joueur, - (self.__prix))
                    self.__appartenu = joueur

                else:
                    print("Désolé, vous n'êtes pas capable de payer, vous êtes trop pauvre lol")

        else:

            banque.envoyeur = joueur
            banque.receveur = self.__appartenu

            if banque.envoyer.argent > self.__loyer:

                banque.transferer(self.__loyer)

            else:
                pass