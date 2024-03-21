from Jeu import *

def testJeu(): 

    objetJeu = Jeu()

    print(f"Test de la classe [Jeu]")
    print(f"==================================================================================== \n")

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

if __name__ == '__main__':
    testJeu()