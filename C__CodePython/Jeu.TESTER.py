from Jeu import *

class TestJeu(): 

    print(f"Test de la classe [Jeu]")
    print(f"==================================================================================== \n")

    def test_init(self):

        unObjet1:int = 0
        unObjet2:float = 0.0
        unObjet3:str = "Oui, bonjour"
        unObjet4:bool = True

        for i in range(1, 5):

            try : 

                Jeu("unObjet" + str(i))

            except Exception as e:

                print(e)

    def testAccesseursMutateurs(self):

        objetJeu = Jeu()

        print(f"Tester : accesseurs/mutateurs")
        print(f"------------------------------------------------------------------------------------")   

        if not(isinstance(objetJeu.nbrDeJoueurs, int)):

            print("nbrDeJoueurs doit être un entier !")

        elif not(isinstance(objetJeu.listeJoueurs, list)):
        
            print("listeJoeurs doit être une liste !")

        elif not(isinstance(objetJeu.fini, bool)):
        
            print("La variable fini doit être booléenne")

        elif not(isinstance(objetJeu.listeCartesChances, list)):
        
            print("listeCartesChances n'est pas une liste")

        else :

            print(f"Accesseurs/mutateurs de la classe [Jeu] CORRECT ! :D")
    
    def choixNbrJoueurTEST(self):

        print("\n Test de la méthode choixNbrJoueur")
        print(f"------------------------------------------------------------------------------------")

        Jeu.listeJoueurs = [1, 2, 3]

        try :

            Jeu.choixNbrJoueur(self)

        except Exception as e:

            print("ça a pas trop fonctionné je t'avoue. \n La raison : ", e)

if __name__ == '__main__':
    
    leTest = TestJeu()
    leTest.test_init()
    leTest.testAccesseursMutateurs()
    leTest.choixNbrJoueurTEST()