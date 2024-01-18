"""
Qui: Nathan Amory
Quand: 2021-05-23
Description: 

"""

##########
# import #
##########

from Joueur import *

class Case():

    ################
    # constructeur #
    ################

    def __init__(self):
        self.__numero:int = 0

    #############
    # affichage #
    #############
        
    def __str__(self):
        print("")