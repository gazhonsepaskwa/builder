"""
QUI : Amory et Nathan

QUAND : 16/05/2024 Amory
        19/05/2024 Amory

QUOI : Les tests du fichier Banque.py
"""

from Banque import *

class TestBanque():

    print(f"Test de la classe [Banque]")
    print(f"==================================================================================== \n")

    #Tester la classe init

    def test_init(self, leObjetBanque):

        #On créer des objet aléatoires de différents type

        unObjet1:int = 0
        unObjet2:float = 0.0
        unObjet3:str = "Oui, bonjour"
        unObjet4:bool = True

        #Boucle qui permet de tester le init avec tout les objets

        for i in range(1, 5):

            try : 

                leObjetBanque("unObjet" + str(i))

            except Exception as e:

                print(e)

            finally:

                print("Test init de la classe [Banque], fini")

#Lancer le fichier

if __name__ == '__main__':

    objetBanque = Banque()
    leTest = TestBanque()
    leTest.test_init(objetBanque)