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

class Case_chance(Case):

    ################
    # constructeur #
    ################

    def __init__(self,num ,pos):
        super().__init__(num, pos)



    #############
    # affichage #
    #############
        
    def __str__(self):
        print("")
        
    

    ###########################
    # accesseurs et mutateurs #
    ###########################



    ############
    # methodes #
    ############
    
    """
    Permet de tirer une carte chance et faire l'action inscrite dessus
    """
    def chance(self):
        pass