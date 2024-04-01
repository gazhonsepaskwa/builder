from Joueur import *

class JoueurTEST():

    def testJoueur(self):
    
        objetJoueur = Joueur()

        print(f"Test de la classe [Jeu]")
        print(f"==================================================================================== \n")

        print(f"Tester : accesseurs/mutateurs")
        print(f"------------------------------------------------------------------------------------")   

        if not(isinstance(objetJoueur.ID, int)):

            print("ID doit être un entier !")

        elif not(isinstance(objetJoueur.argent, int)):
        
            print("argent doit être un entier !")

        elif not(isinstance(objetJoueur.jetonsTractopelle, int)):
        
            print("La variable jetonsTactopelle doit être un entier !")

        elif not(isinstance(objetJoueur.jetonsBateau, int)):
        
            print("La variable jetonsBateau doit être un entier !")

        elif not(isinstance(objetJoueur.jetonsCamion, int)):
        
            print("La variable jetonsCamion doit être un entier !")

        elif not(isinstance(objetJoueur.jetonsGrue, int)):
        
            print("La variable jetonsGrue doit être un entier !")    

        elif not(isinstance(objetJoueur.proprietes, list)):
        
            print("La variable proprietes doit être une liste !")

        elif not(isinstance(objetJoueur.valeurPremierLance, int)):
        
            print("La variable valeurPremierLance doit être un entier !")

        elif not(isinstance(objetJoueur.valeurPremierLance, int)):
        
            print("La variable valeurPremierLance doit être un entier !")

        elif not(isinstance(objetJoueur.numCaseActuelle, int)):
        
            print("La variable numCaseActuelle doit être un entier !")

        elif not(isinstance(objetJoueur.numCaseActuelle, int)):
        
            print("La variable numCaseActuelle doit être un entier !")

        elif not(isinstance(objetJoueur.derniereSommeDE, int)):
        
            print("La variable dernierSommeDE doit être un entier !")

        elif not(isinstance(objetJoueur.enPrison, bool)):
        
            print("La variable enPrison doit être booléenne !")

        else :

            print(f"Accesseurs/mutateurs de la classe [Joueur] CORRECT ! :D")

    
    def lancerDETEST(self):

        objetJoueur = Joueur()

        for i in range(69):
        
            objetJoueur.lancerDE()

            print("Chiffre tiré : ", objetJoueur.derniereSommeDE)

        assert 2 <= objetJoueur.derniereSommeDE <= 12, "les calculs sont pas bon là"

        print("On sait lancer un dé !")
    


if __name__ == '__main__':
    
    leTest = JoueurTEST()
    leTest.testJoueur()
    leTest.lancerDETEST()