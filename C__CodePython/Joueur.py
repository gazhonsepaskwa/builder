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
- 20/05/2024 Nathan
- 23/05/2024 Amory
- 24/05/2024 Nathan
- 25/05/2024 Nathan
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
                color= color.rgba(0, 0, 0, 0.5),
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
        self.__nom:str = ""

    #############
    # affichage #
    #############
        
    def __str__(self):
        return(f"Joueur {self.__ID}")
        
    ###########################
    # accesseurs et mutateurs #
    ###########################
        
    #Permet au joueur de s'identifier avec un pseudonyme

    def id_getter(self):
        return self.__ID

    def id_setter(self, val: int) -> None:
        self.__ID = val

    ID = property(id_getter, id_setter)
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

    def jetonsTractopelle_getter(self):
        return self.__jetonsTractopelle
    
    def jetonsTractopelle_setter(self, val: int):
        self.__jetonsTractopelle = val

    jetonsTractopelle = property(jetonsTractopelle_getter, jetonsTractopelle_setter)

    #Jetons qui pertmet de construire des étages sur les immeubles avec certaines combinaisons

    def jetonsBateau_getter(self):
        return self.__jetonsBateau

    def jetonsBateau_setter(self, val: int):
        self.__jetonsBateau = val
    
    jetonsBateau = property(jetonsBateau_getter, jetonsBateau_setter)

    #Jetons qui pertmet de construire des étages sur les immeubles avec certaines combinaisons

    def jetonsCamion_getter(self):
        return self.__jetonsCamion

    def jetonsCamion_setter(self, val: int):
        self.__jetonsCamion = val
    
    jetonsCamion = property(jetonsCamion_getter, jetonsCamion_setter)

    #Jetons qui pertmet de construire des étages sur les immeubles avec certaines combinaisons

    @property
    def jetonsGrue(self):
        return self.__jetonsGrue

    def jetonsGrue_setter(self, val: int):
        self.__jetonsGrue = val

    #Propriétés obtenues par le/les joueur(s)

    @property
    def proprietes(self):
        return self.__proprietes
    @proprietes.setter
    def proprietes(self, leProprietes):

        self.__proprietes = leProprietes


    #Case sur laquelle le joueur est actuellement

    def numCaseActuelle_getter(self):
        return self.__numCaseActuelle
    
    def numCaseActuelle_setter(self, val: int):
        self.__numCaseActuelle = val
    
    numCaseActuelle = property(numCaseActuelle_getter, numCaseActuelle_setter)
    #Dernière somme retenu après le lancé de dé

    def derniereSommeDE_getter(self):
        return self.__derniereSommeDE        
    
    def derniereSommeDe_setter(self, val: int):
        self.__derniereSommeDE = val
    
    derniereSommeDE =  property(derniereSommeDE_getter, derniereSommeDe_setter)

    #Envoi le joueur en prison

    @property
    def enPrison(self):
        return self.__enPrison
    @enPrison.setter
    def enPrison(self, val):
        self.__enPrison = val

    #fin du tour de construction

    @property
    def tourEditionFini(self):
        return self.__tourEditionFini
    @tourEditionFini.setter
    def tourEditionFini(self, val):
        self.__tourEditionFini = val


    @property
    def nom(self):
        return self.__nom
    
    @nom.setter
    def nom(self, leNom:str) -> None:
        
        if not(isinstance(leNom, str)):

            raise TypeError("")
        
        self.__nom = leNom

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
        
            if self.__numCaseActuelle >= 32:

                self.__argent  += 200
                print(f"{self.__nom} a gagné 200 d'argent")
                self.__numCaseActuelle -= 32
            
            # bouger le pion visuellement
            (x,y,z) = plateau.caseListe[self.__numCaseActuelle].position
            self.position = (x,y+0.25,z)

            time.sleep(1)
            print("Vous avez avancé de {} cases".format(self.__derniereSommeDE))

        else:
            print("VOUS ÊTES EN PRISON, RIP, on se revoie au tour prochain")
            self.__enPrison == False