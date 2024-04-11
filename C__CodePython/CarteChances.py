"""
Qui: Nathan
Quand: 
- 18/01/2024
Description: Carte qui quand tirée fait une action

"""

##########
# import #
##########

import random

class CarteChances():

    ################
    # constructeur #
    ################

    def __init__(self, titre: str, contenu: str, identifiant: int):
        self.__titre: str = titre
        self.__contenu: str = contenu
        self.__identifiant: int = identifiant



    #############
    # affichage #
    #############
        
    def __str__(self):
        print("")
        
    
    ###########################
    # accesseurs et mutateurs #
    ###########################
        
    """
    Titre en haut de la carte
    """
    @property
    def titre(self):
        return self.__titre
    @titre.setter
    def titre(self, val):
        self.__titre = val

    """
    contenu texte de la carte
    """
    @property
    def contenu(self):
        return self.__contenu
    @contenu.setter
    def contenu(self, val):
        self.__contenu = val

    """
    identifiant de la carte: 
    permet de distinguer les cartes de la même classe pour executer l'action adéquoite
    """
    @property
    def identifiant(self):
        return self.__identifiant
    @identifiant.setter
    def identifiant(self, val):
        self.__identifiant = val
    


    ############
    # methodes #
    ############
    
    """
    action faite par la carte de chance(difere en fonction de l'identifiant et donc de la carte)
    """
    def action(self, jActif, listeJoueurs):
        print(self.__titre)
        print(self.__contenu)

        val = random.randint(100,250)

        if self.__identifiant == 0:
            print("Vous avez gagné ", val)
            jActif.argent += 1000
        elif self.__identifiant == 1:
            print("Vous avez perdu ", val)
            jActif.argent -= 250
        elif self.__identifiant == 2:
            print("Vous avez mangé le joueur ayant jouer juste avant vous mouhahaha. Il ne oeu donc plus jouer, dommage.")
            precedent = listeJoueurs[listeJoueurs.index(jActif) - 1]
            listeJoueurs.pop(precedent)

        