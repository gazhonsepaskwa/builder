from Case import *

class TestCase():

    print(f"Test de la classe [Case_chance]")
    print(f"==================================================================================== \n")

    def test_init(self):

        unObjet1:int = 0
        unObjet2:float = 0.0
        unObjet3:str = "Oui, bonjour"
        unObjet4:bool = True

        for i in range(1, 5):

            try : 

                Case("unObjet" + str(i))

            except Exception as e:

                print(e)

    #Tester les accesseurs/mutateurs

    def testAccesseursMutateurs(self):

        print(f"Tester : accesseurs/mutateurs")
        print(f"------------------------------------------------------------------------------------")

        if not(isinstance(leObjetCase.numero, int)):

            print("numero doit être un entier !")

if __name__ == '__main__':

    leObjetCase = Case()
    leTest = TestCase()
    leTest.test_init()
    leTest.testAccesseursMutateurs(leObjetCase)