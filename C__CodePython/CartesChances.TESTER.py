from CarteChances import *

class CartesChanceTEST():

    def test_init(self):

        unObjet1:int = 0
        unObjet2:float = 0.0
        unObjet3:str = "Oui, bonjour"
        unObjet4:bool = True

        for i in range(1, 5):

            try : 

                CarteChances("unObjet" + str(i))

            except Exception as e:

                print(e)

        for i in range(1, 5):

            if i == 4:

                try:

                    CarteChances("unObjet" + str(i), "Un objet" + str(i - 3))

                except Exception as e:

                    print(e)
            
                try:
                    
                    CarteChances("unObjet" + str(i), "Un objet" + str(i + 1))

                except Exception as e:

                    print(e)

if __name__ == '__main__':
     
    leTest = CartesChanceTEST()
    leTest.test_init()