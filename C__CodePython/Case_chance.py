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
from random import randrange as random

class Case_chance(Case):

    ################
    # constructeur #
    ################

    def __init__(self,num ,pos):
        super().__init__(num, pos, couleur=color.gold)
        self.__carteChanceChoisis: int = 0
        self.__chance: int = 0




    #############
    # affichage #
    #############
        
    def __str__(self):
        print("")
        
    

    ###########################
    # accesseurs et mutateurs #
    ###########################

    #Permet de choisir un nombre random entre 1 et 3

    @property
    def carteChanceChoisis(self):
        return self.__carteChanceChoisis
    @carteChanceChoisis.setter
    def carteChanceChoisis(self, leCarteChanceChoisis:int):

        if (isinstance(leCarteChanceChoisis, int) and leCarteChanceChoisis > 1 and leCarteChanceChoisis < 3):

            self.__carteChanceChoisis = leCarteChanceChoisis

        else :

            raise TypeError("")
        
    @property
    def chance(self):
        return self.__chance
    @chance.setter
    def chance(self):
        self.__chance

    ############
    # methodes #
    ############
    """  
"""
"""
    def choixRandomCarteChance(self):
        self.carteChanceChoisis = random.randint(1,3)
"""
    
"""
    Permet de tirer une carte chance et faire l'action inscrite dessus
    """
"""
    def chance(self):

        self.choixRandomCarteChance()
    
"""
"""
    Prendre élément random de la liste, puis faire un if id = quelque chose
    alors, faire action
"""