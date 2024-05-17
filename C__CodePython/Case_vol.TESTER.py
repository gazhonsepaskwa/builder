from Case_vol import *
from Case import *

class TestVol():

    def testAccesseurMutateurs(self):

        objetCaseVol = Case_vol()

        print(f"Tester : accesseurs/mutateurs")
        print(f"------------------------------------------------------------------------------------")

        if not(isinstance(objetCaseVol.voleur, None)):

            print("L'accesseur/mutateur de voleur n'est pas bon")

        if not(isinstance(objetCaseVol.victime, None)):

            print("L'accesseur/mutateur de victime n'est pas bon")

if __name__ == '__main__':

    leTest = TestVol()
    leTest.testAccesseurMutateurs()