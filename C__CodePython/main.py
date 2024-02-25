"""
Qui: Nathan Amory
Quand: 
- 18/01/2024
Description: 

"""

##########
# import #
##########

import threading

from Jeu import *
from time import sleep



########
# Code #
########

jeu = Jeu()

def code():

    time.sleep(1)
    jeu.preparer()
    
    while not jeu.fini:
        jeu.jouerUnTour()

        if jeu.fini:
            jeu.finDePartie()
            break

        jeu.changerJoueurActif()


thread = threading.Thread(target=code)
thread.start()
jeu.ursinaStart()