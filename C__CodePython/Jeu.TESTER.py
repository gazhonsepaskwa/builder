"""
QUI : Amory et Nathan

QUAND : 21/03/2024 Amory
        22/03/2024 Amory
        25/03/2024 Amory
        01/04/2024 Amory
        11/04/2024 Amory
        16/05/2024 Amory
        19/05/2024 Amory

QUOI : Les tests du fichier Jeu.py
"""
from Jeu import *

class TestJeu(): 

    print(f"Test de la classe [Jeu]")
    print(f"==================================================================================== \n")

    def test_init(self):

        #Tester la classe init

        unObjet1:int = 0
        unObjet2:float = 0.0
        unObjet3:str = "Oui, bonjour"
        unObjet4:bool = True

        for i in range(1, 5):

            try : 

                Jeu("unObjet" + str(i))

            except Exception as e:

                print(e)

    #Tester les accesseurs/mutateurs

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
    
    #Initialiser le nombre de joueurs pour s'assurer qu'il y en bien 0 à la base
    
    def initialisationNbrJoueursTEST(self):

        jeu = Jeu()
        assert jeu.nbrDeJoueurs == 0

    #Initialiser la liste de joueur pour qu'elle soit vide

    def InitialisationListeJoueursVide(self):
        jeu = Jeu()
        assert jeu.listeJoueurs == []

    #Tester le choix du nombre de joueurs en lançant le début du jeu

    def choixNbrJoueursTEST(self):

        print("\n Test de choix de nombre de joueurs \n")

        jeu = Jeu()
        jeu.choixNbrJoueur()
        assert jeu.nbrDeJoueurs >= 2 and jeu.nbrDeJoueurs <= 4
        assert len(jeu.listeJoueurs) == jeu.nbrDeJoueurs
        for joueur in jeu.listeJoueurs:
            assert joueur.ID >= 0

    #Tester la méthode déter qui commence

    def deterQuiCommenceTEST(self):
        
        print("\n Test de la méthode déterminer qui commence \n")

        leJeu = Jeu()
        leJeu.__nbrDeJoueurs = 4 
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