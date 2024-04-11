"""
Qui: Nathan
Quand: 
- 18/01/2024
Description: Case qui permet de tirer une carte
chance et faire l'action inscrite dessus via chance()

"""

##########
# import #
##########

from Case import *
from random import randrange

class Case_chance(Case):

    ################
    # constructeur #
    ################

    def __init__(self,num ,pos):
        super().__init__(num, pos, couleur=color.gold)




    #############
    # affichage #
    #############
        
    def __str__(self):
        print("")
        
    

    ############
    # methodes #
    ############


    # Permet de tirer une carte chance et faire l'action inscrite dessus

    def chance(self, jeu):
        carteChanceChoisis = randint(0,len(jeu.listeCartesChances)-1)
        jeu.listeCartesChances[carteChanceChoisis].action(jeu.joueurActif, jeu.listeJoueurs)