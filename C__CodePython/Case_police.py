"""
Qui: Nathan 
Quand: 
- 18/01/2024 Nathan
- 26/02/2024 Nathan
- 27/02/2024 Nathan
- 19/05/2024 Nathan
Description: Case sur laquelle se trouve la police,
quand on tombe dessus on est envoyé en prison
"""

##########
# import #
##########

from Jeu import *
from Joueur import *
from Case import *

class Case_police(Case):

    ################
    # constructeur #
    ################

    def __init__(self, num, pos):
        super().__init__(num, pos)



    #############
    # affichage #
    #############
        
    def __str__(self):
        print("")

    ############
    # methodes #
    ############

    #Envoie le joueur se situant sur la case, en prison
    
    def emprisonner(self, joueurActif):

        joueurActif.caseActuelle = 8
        JoueurActif.enPrison = True