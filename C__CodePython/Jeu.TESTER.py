from Jeu import *

class TestJeu(): 

    print(f"Test de la classe [Jeu]")
    print(f"==================================================================================== \n")

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

        try :

            Jeu.choixNbrJoueur(self)

        except Exception as e:

            print("ça a pas trop fonctionné je t'avoue. \n La raison : ", e)


    """
    def deterQuiCommenceTEST(self):

        print("\n Test de la méthode deterQuiCommence")
        print(f"------------------------------------------------------------------------------------")
        
        try:

            leListeTest = []
            Jeu.deterQuiCommence(leListeTest)

        except Exception as e:
            print("ça a pas trop fonctionné je t'avoue. \n La raison : ", e)
    """
if __name__ == '__main__':
    
    leTest = TestJeu()
    leTest.testAccesseursMutateurs()
    leTest.choixNbrJoueurTEST()
    #leTest.deterQuiCommenceTEST()