"""
Qui: Nathan
Quand: 
- 18/01/2024 Nathan
- 29/02/2024 Nathan
- 01/03/2024 Nathan
- 14/03/2024 Nathan
Description: Classe Batiment, gere un batiment, ses etages et cetera.
"""

##########
# import #
##########

from ursina import *
import outils as outils


class Batiment(Button):

    ################
    # constructeur #
    ################

    def __init__(self, pos):
        super().__init__(
                model="cube",
                color=color.gray,
                texture= "white_cube",
                scale=(0.8,0.2,0.8),
                position=pos,
                parent=scene
            )
        
        self.__construisible: bool = False
        self.__nombreEtage: int = 0

        self.__tract = 0
        self.__bat = 0
        self.__cam = 0
        self.__grue = 0


    #############
    # affichage #
    #############
        
    def __str__(self):
        print("")
        
    

    ###########################
    # accesseurs et mutateurs #
    ###########################
    
    """
    definit si un batiment est construisible ou non 
    """
    @property
    def construisible(self):
        return self.__construisible
    @construisible.setter
    def construisible(self, val):
        self.__construisible = val


    """
    Le quartier auquel appartienst le batiment
    """
    @property
    def quartier(self):
        return self.__quartier
    @quartier.setter
    def nombreEtage(self, val):
        self.__quartier = val



    ############
    # methodes #
    ############
    
    """
    Verifie si le joueur a assez de pions pour construir un etage
    """
    def VerifQuantiteePion():
        pass

    def on_click(self):
         
        if self.construisible:
            if self.__nombreEtage == 0:
                self.__tract = 1
                self.__bat = 0
                self.__cam = 1
                self.__grue = 0

            elif self.__nombreEtage == 1:
                self.__tract = 0
                self.__bat = 1
                self.__cam = 0
                self.__grue = 1
        
            elif self.__nombreEtage == 2:
                self.__tract = 0
                self.__bat = 2
                self.__cam = 0
                self.__grue = 1
        
            elif self.__nombreEtage == 3:
                self.__tract = 1
                self.__bat = 1
                self.__cam = 1
                self.__grue = 1
        
            elif self.__nombreEtage == 4:
                self.__tract = 2
                self.__bat = 2
                self.__cam = 2
                self.__grue = 2
        
            if self.verifQuantiteePion():
                print("Le prix est de : " + self.__tract + " tractopelle, " + self.__bat + " bateau, " + self.__cam + " camion, " + self.__grue + " grue.")
                if outils.ouiOuNon("Voulez-vous construire un etage sur ce batiment? Oui/Non"):
                    self.__nombreEtage += 1
            else:
                print("Vous n'avez pas la possiblilite de vous offrir un etage sur ce batiment, le prix est de : " + self.__tract + " tractopelle, " + self.__bat + " bateau, " + self.__cam + " camion, " + self.__grue + " grue.")