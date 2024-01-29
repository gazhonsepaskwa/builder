"""
Qui: Amory & Nathan
Quand: 
- 18/01/2024 Amory
- 25/01/2024 Nathan 
- 29/01/2024 Nathan 
Description: Le jeu Monopoly en lui même qui va pouvoir
être joué par les joueurs qui veulent bien y jouer
"""

##########
# import #
##########

from Joueur import *
from GestionnaireDePion import *
from random import randrange as random
from Case_propriete import *
from Case_chance import *
from Case_police import *
from Case_ressource import *
from Case_vol import *

class Jeu():

    ################
    # constructeur #
    ################

    def __init__(self):
        self.__nbrDeJoueurs:int = 0
        self.__listeJoueurs:list = []
        self.__joueurActif:Joueur = None
        self.__caseListe:list = []
        self.__fini = False
        self.__listeBatiments = []


    #############
    # affichage #
    #############
        
    def __str__(self):
        print("")
        
    ###########################
    # accesseurs et mutateurs #
    ###########################
        
    #Le nombre joueur dans la partie
    
    @property
    def nbrDeJoueurs(self):
        return self.__nbrDeJoueurs
    @nbrDeJoueurs.setter
    def nbrDeJoueurs(self, val):
        self.__nbrDeJoueurs = val 

    #La liste des joueurs qui sont dans la partie

    @property
    def listeJoueurs(self):
        return self.__listeJoueurs
    @listeJoueurs.setter
    def listeJoueurs(self, val):
        self.__listeJoueurs = val

    
    #Liste de cases disponible sur le plateau

    @property
    def caseListe(self):
        return self.__caseListe

    #Le joueur qui joue son tour sur le moment

    @property
    def joueurActif(self):
        return self.__joueurActif
    @joueurActif.setter
    def joueurActif(self, val):
        self.__joueurActif = val

    #La fin de la partie quand l'une des conditions est faite

    @property
    def fini(self):
        return self.__fini
    @fini.setter
    def fini(self, val):
        self.__fini = val

    
    #Liste qui stoque tout les batiments du jeu
    
    @property
    def nbrDeJoueurs(self):
        return self.__nbrDeJoueurs




    ############
    # methodes #
    ############
    
    # Détermine qui commence la partie

    def deterQuiCommence(self):
        self.__joueurActif = self.listeJoueurs(random.randrange(1,self.listeJoueurs.lenght()))
        print("Le joueur " + self.__joueurActif.ID + " commence la partie")



    #Choix qui permet de déterminer le nombre de joueur au début de la partie (maximum 4)

    def choixNbrJoueur(self):
        self.__nbrDeJoueurs = int(input("Entrez le nombre de joueurs (minimum2, maximum 4): "))



    #Permet de générer les objets du jeu

    def genererObjects():
        pass



    #Permet de préparer le jeu

    def preparer(self):
        self.choixNbrJoueur()
        self.__joueurActif.pion = GestionnaireDePion.choisir()
        for i in self.__listeJoueurs:
            self.__listeJoueurs[i].pion = GestionnaireDePion.choisir()
            self.__listeJoueurs[i].argent = 2000
        self.genererObjects()

        self.__joueurActif = self.deterQuiCommence()


    #Permet de jouer un tour

    def jouerUnTour(self):
        self.__joueurActif.avancer()
        if isinstance(self.__caseListe[self.joueurActif.numCaseActuelle], Case_propriete):
            self.joueurActif.caseLise[self.joueurActif.caseActuelle].Achat()
        elif isinstance(self.__caseListe[self.joueurActif.numCaseActuelle], Case_chance):
            self.joueurActif.caseLise[self.joueurActif.caseActuelle].chance()
        elif isinstance(self.__caseListe[self.joueurActif.numCaseActuelle], Case_police):
            self.joueurActif.caseLise[self.joueurActif.caseActuelle].emprisonner()
        elif isinstance(self.__caseListe[self.joueurActif.numCaseActuelle], Case_ressource):
            self.joueurActif.caseLise[self.joueurActif.caseActuelle].donnerResource()
        elif isinstance(self.__caseListe[self.joueurActif.numCaseActuelle], Case_vol):
            self.joueurActif.caseLise[self.joueurActif.caseActuelle].voler()
        else: pass
        
        tmp=""
        while(tmp!= "Y" or tmp!= "y" or tmp!= "YES" or tmp!= "yes" or tmp!= "Yes" or tmp!= "oui" or tmp!= "OUI" or tmp!= "Oui" or tmp == "N" or tmp == "n" or tmp == "NO" or tmp == "no" or tmp == "No" or tmp == "non"):
            tmp = input("Voulez vous construire? (Y/N)")

        if tmp == "N" or tmp == "n" or tmp == "NO" or tmp == "no" or tmp == "No" or tmp == "non":
            pass
        else:
            # construire
            self.__joueurActif.tourEditionFini = False
            while self.__joueurActif.tourEditionFini  == False:
                for batiment in self.__listeBatiments:
                    if batiment.quartier.proprietaire == self.__joueurActif:
                        batiment.construisible = True
                    

        # en courssss (c long putinnnn)




    #À la fin du tour d'un joueur, on passe au joueur suivant

    def changerJoueurActif(self):
        indiceJoueurActif = self.__listeJoueurs.index(self.__joueurActif)
        indiceJoueurSuivant = (indiceJoueurActif + 1) % self.__listeJoueurs.lenght()
        self.__joueurActif = self.__listeJoueurs[indiceJoueurSuivant]



    # Defini qui est le grand gagnant 
    
    def finDePartie():
        pass