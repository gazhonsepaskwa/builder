"""
QUI : Amory et Nathan

QUAND : 05/05/2024 Amory
        20/05/2024 Amory

QUOI : Les tests du fichier Jeu.py
"""

from Batiment import *

class TestBatiment():

    print(f"Test de la classe [Batiment]")
    print(f"==================================================================================== \n")

    #Tester la classe init

    def test_init(self):

        #On créer des objet aléatoires de différents type

        unObjet1:int = 0
        unObjet2:float = 0.0
        unObjet3:str = "Oui, bonjour"
        unObjet4:bool = True

        #Boucle qui permet de tester le init avec tout les objets

        for i in range(1, 5):

            try : 

                Batiment("unObjet" + str(i))

            except Exception as e:

                print(e)

        for i in range(1, 5):

            if i == 4:

                try:

                    Batiment("unObjet" + str(i), "unObjet" + str(i - 3))

                except Exception as e:

                    print(e)
            
            else:

                try:
                    
                    Batiment("unObjet" + str(i), "unObjet" + str(i + 1))

                except Exception as e:

                    print(e)
        
        print("Fin du test init de la classe [Batiment]")

    #Tester les accesseurs/mutateurs

    def testAccesseursMutateurs(self):

        print(f"Tester : accesseurs/mutateurs")
        print(f"------------------------------------------------------------------------------------")

        if not(isinstance(Batiment.construisible, bool)):

            print("contruisible doit être booléen !")

        elif not(isinstance(Batiment.quartier, int)):
            
            pass

        print("Fin des tests accesseurs/mutateurs")

if __name__ == '__main__':

    leTest = TestBatiment()
    leTest.test_init()