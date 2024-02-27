"""
Qui: Amory
Quand: 
- 18/01/2024
Description: Case dans laquel le joueur est envoyer quand son status est "en prison"
"""

##########
# import #
##########

from Case import *

class Case_prison(Case):

    ################
    # constructeur #
    ################

    def __init__(self,num,pos):
        super().__init__(num, pos)

    #############
    # affichage #
    #############
        
    def __str__(self):
        print("")
        