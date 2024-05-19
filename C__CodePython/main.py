"""
Qui: Nathan
Quand: 
- 25/01/2024 Nathan
- 26/01/2024 Nathan
- 12/02/2024 Nathan
- 13/02/2024 Nathan
- 24/02/2024 Nathan
- 25/02/2024 Nathan
- 17/05/2024 Nathan
Description: script permettant le multi-threading et de les démarrer

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