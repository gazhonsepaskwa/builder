from Banque import *

class TestBanque():

    print(f"Test de la classe [Banque]")
    print(f"==================================================================================== \n")

    def test_init(self, leObjetBanque):

        unObjet1:int = 0
        unObjet2:float = 0.0
        unObjet3:str = "Oui, bonjour"
        unObjet4:bool = True

        for i in range(1, 5):

            try : 

                leObjetBanque("unObjet" + str(i))

            except Exception as e:

                print(e)

            finally:

                print("Test init de la classe [Banque], fini")

if __name__ == '__main__':

    objetBanque = Banque()
    leTest = TestBanque()
    leTest.test_init(objetBanque)