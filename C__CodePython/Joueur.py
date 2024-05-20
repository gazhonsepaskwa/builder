"""
Qui: Nathan
Quand: 
- 18/01/2024 Nathan
- 29/01/2024 Nathan
- 12/02/2024 Nathan
- 15/02/2024 Nathan
- 24/02/2024 Nathan
- 28/02/2024 Nathan
- 17/05/2024 Nathan
Description: Les joueurs/adversaires qui disputent une partie
(matérialisés par des pions.)
"""

##########
# import #
##########

from Jeu import *
from ursina import *
from random import randint
from time import sleep

class Joueur(Entity):

    ################
    # constructeur #
    ################

    def __init__(self):
        super().__init__(
                model="cube",
                color=color.red,
                scale=(0.3,0.5,0.3),
                position=(4,0.25,-4),
            )

        self.__ID:int = 0
        self.__argent:int = 0
        self.__jetonsTractopelle:int = 0
        self.__jetonsBateau:int = 0
        self.__jetonsCamion:int = 0
        self.__jetonsGrue:int = 0
        self.__proprietes = []
        self.__valeurPremierLance:int = 0
        self.__numCaseActuelle:int = 0
        self.__derniereSommeDE: int = 0
        self.__enPrison: bool = False

    #############
    # affichage #
    #############
        
    def __str__(self):
        return(f"Joueur {self.__ID}")
        
    ###########################
    # accesseurs et mutateurs #
    ###########################
        
    #Permet au joueur de s'identifier avec un pseudonyme

    @property
    def ID(self):
        return self.__ID
    @ID.setter
    def ID(self, leID:int) -> None:

        #Test de la valeur reçue.

        if not(isinstance(leID, int) and leID >= 0):

            raise TypeError("")

        self.__ID = leID

    #Argent qui permet d'acheter les diverses propriétés du jeu

    @property
    def argent(self):
        return self.__argent
    @argent.setter
    def argent(self, leArgent:int) -> None:

        #Test de la valeur reçue.

        if not(isinstance(leArgent, int) and leArgent >= 0):

            raise TypeError("")

        self.__argent = leArgent

    #Jetons qui pertmet de construire des étages sur les immeubles avec certaines combinaisons

    @property
    def jetonsTractopelle(self):
        return self.__jetonsTractopelle
    @jetonsTractopelle.setter
    def jetonsTractopelle(self, leJetonsTractopelle:int):

        #Test de la valeur reçue.

        if not(isinstance(leJetonsTractopelle, int) and leJetonsTractopelle >= 0):

            raise TypeError("")

        self.__jetonsTractopelle = leJetonsTractopelle

    #Jetons qui pertmet de construire des étages sur les immeubles avec certaines combinaisons

    @property
    def jetonsBateau(self):
        return self.__jetonsBateau
    @jetonsBateau.setter
    def jetonsBateau(self, leJetonsBateau:int):
        
        #Test de la valeur reçue.

        if not(isinstance(leJetonsBateau, int) and leJetonsBateau >= 0):

            raise TypeError("")

        self.__jetonsBateau = leJetonsBateau

    #Jetons qui pertmet de construire des étages sur les immeubles avec certaines combinaisons

    @property
    def jetonsCamion(self):
        return self.__jetonsCamion
    @jetonsCamion.setter
    def jetonsCamion(self, leJetonsCamion:int):
        
        #Test de la valeur reçue.

        if not(isinstance(leJetonsCamion, int) and leJetonsCamion >= 0):

            raise TypeError("")

        self.__jetonsCamion = leJetonsCamion

    #Jetons qui pertmet de construire des étages sur les immeubles avec certaines combinaisons

    @property
    def jetonsGrue(self):
        return self.__jetonsGrue
    @jetonsGrue.setter
    def jetonsGrue(self, leJetonsGrue:int):
        
        #Test de la valeur reçue.

        if not(isinstance(leJetonsGrue, int) and leJetonsGrue >= 0):

            raise TypeError("")

        self.__jetonsGrue = leJetonsGrue

    #Propriétés obtenues par le/les joueur(s)

    @property
    def proprietes(self):
        return self.__proprietes
    @proprietes.setter
    def proprietes(self, leProprietes):

        self.__proprietes = leProprietes

    #La valeur du premier lancé ?

    @property
    def valeurPremierLance(self):
        return self.__valeurPremierLance
    @valeurPremierLance.setter
    def valeurPremierLance(self, leValeurPremierLance:int):
    
        #Test de la valeur reçue.

        if not(isinstance(leValeurPremierLance, int) and leValeurPremierLance > 1 and leValeurPremierLance < 13):

            raise TypeError("")

        self.__valeurPremierLance = leValeurPremierLance

    #Case sur laquelle le joueur est actuellement

    @property
    def numCaseActuelle(self):
        return self.__numCaseActuelle
    @numCaseActuelle.setter
    def numCaseActuelle(self, leCaseActuelle):

        self.__numCaseActuelle = leCaseActuelle


    #Dernière somme retenu après le lancé de dé

    @property
    def derniereSommeDE(self):
        return self.__derniereSommeDE
    @derniereSommeDE.setter
    def derniereSommeDE(self, leDerniereSomme:int):
    
        #Test de la valeur reçue.

        if (isinstance(leDerniereSomme, int) and leDerniereSomme > 1 and leDerniereSomme < 13):

            self.__derniereSommeDE = leDerniereSomme
        else: 

            raise TypeError("")
        

    #Envoi le joueur en prison

    @property
    def enPrison(self):
        return self.__enPrison
    @enPrison.setter
    def enPrison(self, leEnPrison:bool):
        self.__enPrison = leEnPrison

    #fin du tour de construction

    @property
    def tourEditionFini(self):
        return self.__tourEditionFini
    @tourEditionFini.setter
    def tourEditionFini(self, val):
        self.__tourEditionFini = val


    ############
    # methodes #
    ############
    
    #Les dés se font lancer

    def lancerDE(self):
        self.derniereSommeDE = random.randrange(2, 13)

    #Le joueur avance par rapport à la somme des dés lancés

    def avancer(self, plateau):
        if self.__enPrison == False:
            self.lancerDE()
            self.__numCaseActuelle = self.__numCaseActuelle - 1 + self.__derniereSommeDE
            print(self.__derniereSommeDE)
            print(self.__numCaseActuelle)
        
            if self.__numCaseActuelle >= 32:

                self.__argent  += 200
                print("Vous avez gagné 200 d'argent")
                self.__numCaseActuelle -= 32
            
            # bouger le pion visuellement
            (x,y,z) = plateau.caseListe[self.__numCaseActuelle].position
            self.position = (x,y+0.25,z)

            time.sleep(1)
            print("Vous avez avancé de {} cases".format(self.__derniereSommeDE))

        else:
            print("VOUS ÊTES EN PRISON, RIP, on se revoie au tour prochain")
            self.__enPrison == False