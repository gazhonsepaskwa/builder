"""
Qui: Amory & Nathan
Quand: 
- 18/01/2024 Amory
- 19/01/24 Nathan 
- 25/01/2024 Nathan 
- 29/01/2024 Nathan 
- 12/02/2024 Nathan 
- 13/02/2024 Nathan
- 15/02/2024 Nathan
- 24/02/2024 Nathan
- 24/02/2024 Nathan
- 26/02/2024 Nathan
- 27/02/2024 Nathan
- 28/02/2024 Nathan
- 01/03/2024 Nathan
- 02/04/2024 Nathan
- 11/04/2024 Nathan
- 18/05/2024 Nathan
- 20/05/2024 Nathan
- 23/05/2024 Amory
Description: Le jeu Monopoly en lui même qui va pouvoir
être joué par les joueurs
"""

##########
# import #
##########

from Joueur import *
from random import randrange as random
from Case import *
from Case_propriete import *
from Case_chance import *
from Case_police import *
from Case_ressource import *
from Case_vol import *
from Plateau import *  
from Banque import *

from ursina import *
import mysql

from outils import *

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

        # Attributs
        self.__nbrDeJoueurs:int = 0
        self.__listeJoueurs:list = []
        self.__joueurActif = None
        self.__fini = False
        self.__tourEdition = False

        #Enfants
        self.__plateau = None
        self.__banque = None


    def update():
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
        print("Bonjour, je suis le jeu ! Je permet aux joueurs de jouer")
        
    ###########################
    # accesseurs et mutateurs #
    ###########################

    #La liste des joueurs qui sont dans la partie

    @property
    def listeJoueurs(self):
        return self.__listeJoueurs

    #Le joueur qui joue son tour sur le moment

    @property
    def joueurActif(self):
        return self.__joueurActif

    #La fin de la partie quand l'une des conditions est faite

    @property
    def fini(self):
        return self.__fini

    @property
    def tourEdition(self):
        return self.__tourEdition
    
    @tourEdition.setter
    def tourEdition(self, val):
        self.__tourEdition = val

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

        clear_terminal()
        
        while True:
        
            self.__nbrDeJoueurs = int(input("Entrez le nombre de joueurs (minimum2, maximum 4): "))
        
            if self.__nbrDeJoueurs > 4 or self.__nbrDeJoueurs < 2:

                print("Vous tenter de jouer à plus ou moins que le nombre de joueurs autorisé ! \n Veuillez recommencer.")

            else:

                break

        clear_terminal()

        for i in range(self.__nbrDeJoueurs):
            self.__listeJoueurs.append(Joueur())
            self.__listeJoueurs[i].ID = i
            self.__listeJoueurs[i].nom = input("Veuillez encoder votre pseudonyme : ")


    #Permet de générer les objets du jeu

    def genererObjects(self):
        self.__plateau = Plateau()
        self.__plateau.genererCases(self)
        self.__banque = Banque()


    #Permet de préparer le jeu

    def preparer(self):
        self.choixNbrJoueur()
        # self.__joueurActif.pion = GestionnaireDePion.choisir()
        for i in range(len(self.__listeJoueurs)):
            # self.__listeJoueurs[i].pion = GestionnaireDePion.choisir()
            self.__listeJoueurs[i].argent = 2000
            
            if i == 1:
                self.__listeJoueurs[i].jetonsTractopelle +=2
            elif i == 2:
                self.__listeJoueurs[i].jetonsBateau +=2
            elif i == 3:
                self.__listeJoueurs[i].jetonsCamion +=2
            elif i == 4:
                self.__listeJoueurs[i].jetonsGrue +=2
 
        self.genererObjects()
        self.deterQuiCommence()
    
    def modeConstruction(self):
        hamaux = self.__plateau.caseListe[self.__joueurActif.numCaseActuelle].numHamaux
        caseDansHamaux = []

        # récupérer les cases appartenant au même hamaux
        for case in self.__plateau.caseListe:
            if isinstance(case, Case_propriete):
                if case.numHamaux == hamaux:
                    if case.appartenu == self.joueurActif:
                        caseDansHamaux.append(case)
        
        
        if len(caseDansHamaux) >= 1: # a changer je garde pour test
            if outils.ouiOuNon("Voulez vous construire (oui/non) ?"):
                for case in caseDansHamaux:
                    case.batiment.construisible = True
                    case.batiment.color = color.red
                    self.__tourEdition = True
                    return()
            else: 
                self.__tourEdition = False
                return()
        else: 
            print("Vous n'avez pas la possibilitée de construire")
            self.__tourEdition = False
            return()

    #Permet de jouer un tour

    def jouerUnTour(self):
        clear_terminal()
        print("")
        separator()
        colored_print( f"{str(self.__joueurActif.nom)}, à vous de jouer !", "red")
        separator()
        colored_print("Vos ressources: ", "cyan")
        print(f"argent: {self.__joueurActif.argent} | {self.__joueurActif.jetonsTractopelle} jetons tractopelle | {self.__joueurActif.jetonsBateau} jetons bateau | {self.__joueurActif.jetonsCamion} jetons camion | {self.__joueurActif.jetonsGrue} jetons grue")
        separator()
        print("")

        input("Lancer les dés [ENTER] ")
        delete_last_line()
        self.__joueurActif.avancer(self.__plateau)
        if isinstance(self.__plateau.caseListe[self.joueurActif.numCaseActuelle], Case_propriete):
            self.__plateau.caseListe[self.joueurActif.numCaseActuelle].achat(self.__joueurActif, self.__banque)
            fini = self.modeConstruction()
            if fini: 
                print("partie finie")
                return()


        elif isinstance(self.__plateau.caseListe[self.joueurActif.numCaseActuelle], Case_chance):
            self.__plateau.caseListe[self.joueurActif.numCaseActuelle].chance(self)
        elif isinstance(self.__plateau.caseListe[self.joueurActif.numCaseActuelle], Case_police):
            self.__plateau.caseListe[self.joueurActif.numCaseActuelle].emprisonner(self.__joueurActif)
        elif isinstance(self.__plateau.caseListe[self.joueurActif.numCaseActuelle], Case_ressource):
            self.__plateau.caseListe[self.joueurActif.numCaseActuelle].donnerResource(self.__joueurActif)
        elif isinstance(self.__plateau.caseListe[self.joueurActif.numCaseActuelle], Case_vol):
            self.__plateau.caseListe[self.joueurActif.numCaseActuelle].voler(self.__joueurActif, self.__listeJoueurs) 
        else: pass
        

        if self.__joueurActif.argent == 0 or self.__joueurActif.argent < 0:

            joueurElimine = self.joueurActif.ID

            del(self.listeJoueurs[joueurElimine])

            #if len(set(self.listeJoueurs)) == 1:

           #     print("C'est la fin ! le joueur ")

        # attendre
        while self.__tourEdition:
            time.sleep(1)

        input("Terminer le tour [ENTER] ")





    #À la fin du tour d'un joueur, on passe au joueur suivant

    def changerJoueurActif(self):
        indiceJoueurActif = self.__listeJoueurs.index(self.__joueurActif)
        indiceJoueurSuivant = (indiceJoueurActif + 1) % len(self.__listeJoueurs)
        self.__joueurActif = self.__listeJoueurs[indiceJoueurSuivant]



    # Defini qui est le grand gagnant 
    
    def finDePartie():
        pass

        # la partie ne se finie pas, par manque de temps 
