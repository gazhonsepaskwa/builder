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
    
    def initialisationNbrJoueursTEST(self):
        jeu = Jeu()
        assert jeu.nbrDeJoueurs == 0

    def InitialisationListeJoueursVide(self):
        jeu = Jeu()
        assert jeu.listeJoueurs == []

    def choixNbrJoueursTEST(self):
        jeu = Jeu()
        jeu.choixNbrJoueur()
        assert jeu.nbrDeJoueurs >= 2 and jeu.nbrDeJoueurs <= 4
        assert len(jeu.listeJoueurs) == jeu.nbrDeJoueurs
        for joueur in jeu.listeJoueurs:
            assert joueur.ID >= 0

    def deterQuiCommenceTEST(self):
        
        leJeu = Jeu()
        leJeu.nbrDeJoueurs = 4 
        leJeu.listeJoueurs = [Joueur(), Joueur(), Joueur(), Joueur()]  # Simuler la création des joueurs
        leJeu.deterQuiCommence()
        assert leJeu.joueurActif in leJeu.listeJoueurs


if __name__ == '__main__':
    
    leTest = TestJeu()
    leTest.test_init()
    leTest.testAccesseursMutateurs()
    leTest.initialisationNbrJoueursTEST()
    leTest.InitialisationListeJoueursVide()
    leTest.choixNbrJoueursTEST()
    leTest.deterQuiCommenceTEST()