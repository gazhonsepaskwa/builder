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
from Case import *
from Case_propriete import *
from Case_chance import *
from CarteChances import *
from Case_police import *
from Case_ressource import *
from Case_vol import *
from Plateau import *  
from Banque import *

from ursina import *

import outils as outils

class Jeu():

    ################
    # constructeur #
    ################

    def __init__(self):

        # Initialisation du moteur graphique
        self.app = Ursina()

        # Creation de la camera libre
        self.camera = EditorCamera()

        self.__nbrDeJoueurs:int = 0
        self.__listeJoueurs:list = []
        self.__joueurActif = None
        self.__fini = False
        self.__listeCartesChances = []

        #Enfants
        self.__plateau = None
        self.__banque = None


    def update():
        # Move the camera using WASD keys
        if held_keys['z']:
            camera.position += camera.forward * time.dt
        if held_keys['s']:
            camera.position -= camera.forward * time.dt
        if held_keys['q']:
            camera.position -= camera.right * time.dt
        if held_keys['d']:
            camera.position += camera.right * time.dt

    def ursinaStart(self):
        self.app.run()


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
    
    #Liste qui stoque toute les cartes chances

    @property
    def listeCartesChances(self):
        return self.__listeCartesChances
    @listeCartesChances.setter
    def listeCartesChances(self, val):
        self.__listeCartesChances = val




    ############
    # methodes #
    ############
    
    # Détermine qui commence la partie

    def deterQuiCommence(self):
        self.__joueurActif = random.choice(self.__listeJoueurs)
        print(self.__listeJoueurs)
        print("Le joueur " + str(self.__joueurActif.ID) + " commence la partie")



    #Choix qui permet de déterminer le nombre de joueur au début de la partie (maximum 4)

    def choixNbrJoueur(self):
        self.__nbrDeJoueurs = int(input("Entrez le nombre de joueurs (minimum2, maximum 4): "))
        for i in range(self.__nbrDeJoueurs):
            self.__listeJoueurs.append(Joueur())
            self.__listeJoueurs[i].ID = i


    #Permet de générer les objets du jeu

    def genererObjects(self):
        self.__plateau = Plateau()
        self.__plateau.genererCases()
        self.__banque = Banque()
        
        carteChance0 = CarteChances("Donne la thune", "Tu me dois 100$ \n Payez 100$", 0)

        self.__listeCartesChances.append(carteChance0)


    #Permet de préparer le jeu

    def preparer(self):
        self.choixNbrJoueur()
        # self.__joueurActif.pion = GestionnaireDePion.choisir()
        for i in range(len(self.__listeJoueurs)):
            # self.__listeJoueurs[i].pion = GestionnaireDePion.choisir()
            self.__listeJoueurs[i].argent = 2000
 
        self.genererObjects()
        self.deterQuiCommence()


    #Permet de jouer un tour

    def jouerUnTour(self):
        print("")
        print("Le joueur " + str(self.__joueurActif.ID) + " joue son tour")
        print(f"Il a {self.__joueurActif.argent} d'argent | {self.__joueurActif.jetonsTractopelle} jetons tractopelle | {self.__joueurActif.jetonsBateau} jetons bateau | {self.__joueurActif.jetonsCamion} jetons camion | {self.__joueurActif.jetonsGrue} jetons grue")
        print("")

        self.__joueurActif.avancer(self.__plateau)
        if isinstance(self.__plateau.caseListe[self.joueurActif.numCaseActuelle], Case_propriete):
            self.__plateau.caseListe[self.joueurActif.numCaseActuelle].achat(self.__joueurActif, self.__banque)
        elif isinstance(self.__plateau.caseListe[self.joueurActif.numCaseActuelle], Case_chance):
            self.__plateau.caseListe[self.joueurActif.numCaseActuelle].chance()
        elif isinstance(self.__plateau.caseListe[self.joueurActif.numCaseActuelle], Case_police):
            self.__plateau.caseListe[self.joueurActif.numCaseActuelle].emprisonner()
        elif isinstance(self.__plateau.caseListe[self.joueurActif.numCaseActuelle], Case_ressource):
            self.__plateau.caseListe[self.joueurActif.numCaseActuelle].donnerResource(self.__joueurActif)
        # elif isinstance(self.__plateau.caseListe[self.joueurActif.numCaseActuelle], Case_vol):
            # self.__plateau.caseListe[self.joueurActif.numCaseActuelle].voler(self.__joueurActif, self.__listeJoueurs)    ### je sais pas comment faire pour le voleur et la victime
        else: pass
        
        if outils.ouiOuNon("Voulez vous construire (oui/non) ?"):
            # construire
            print("test")
            self.__joueurActif.tourEditionFini = False
            while self.__joueurActif.tourEditionFini  == False:
                print("test in while")
                for batiment in self.__listeBatiments:
                    if batiment.quartier.proprietaire == self.__joueurActif:
                        batiment.construisible = True





    #À la fin du tour d'un joueur, on passe au joueur suivant

    def changerJoueurActif(self):
        indiceJoueurActif = self.__listeJoueurs.index(self.__joueurActif)
        indiceJoueurSuivant = (indiceJoueurActif + 1) % len(self.__listeJoueurs)
        self.__joueurActif = self.__listeJoueurs[indiceJoueurSuivant]



    # Defini qui est le grand gagnant 
    
    def finDePartie():
        pass
