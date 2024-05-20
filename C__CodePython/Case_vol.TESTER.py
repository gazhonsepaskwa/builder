"""
QUI: Amory et Nathan

QUAND:  18/05/2024 Amory

QUOI: Le test de la case vol
"""

from Case_vol import *

class JoueurFake:

    def __init__(self, nom):
        self.nom = ""
        self.jetonsTractopelle = 5
        self.jetonsBateau = 5
        self.jetonsCamion = 5
        self.jetonsGrue = 5

class TestVol():

    def testAccesseurMutateurs(self):

        print(f"Tester : accesseurs/mutateurs")
        print(f"------------------------------------------------------------------------------------")

        if Case_vol.voleur is not None:

            print("L'accesseur/mutateur de voleur n'est pas bon")

        if Case_vol.victime is not None:

            print("L'accesseur/mutateur de victime n'est pas bon")

if __name__ == '__main__':

    leTest = TestVol()
    leTest.testAccesseurMutateurs()