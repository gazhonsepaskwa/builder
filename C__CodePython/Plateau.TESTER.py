from Plateau import *

class TestPlateau():

    print(f"Test de la classe [Plateau]")
    print(f"==================================================================================== \n")

    def test_init(self):

        unObjet1:int = 0
        unObjet2:float = 0.0
        unObjet3:str = "Oui, bonjour"
        unObjet4:bool = True

        for i in range(1, 5):

            try : 

                Plateau("unObjet" + str(i))

            except Exception as e:

                print(e)

    def testAccesseursMutateurs(self):

        if not(isinstance(Plateau.caseListe, list)):

            print("Case Liste doit être une liste")