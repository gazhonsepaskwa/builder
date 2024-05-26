"""
Qui: Nathan
Quand: 
- 18/01/2024 Nathan
- 29/02/2024 Nathan
- 01/03/2024 Nathan
- 14/03/2024 Nathan
- 20/05/2024 Nathan
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

    def __init__(self, pos, jeu):
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

        # import de l'instace de jeu pour éviter l'iport circulaire
        self.__jeu = jeu


    #############
    # affichage #
    #############
        
    def __str__(self):
        print("Bonjour, je suis le batiment ! Je permet aux joueurs de pouvoir construire des bâtiments au milieu du plateau et j'impose des conditions pour pouvoir construire un étage")
        
    

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

    def on_click(self):

        # mettre le prix en fonction de l'étage en cours  
        if self.construisible:
            if self.__nombreEtage == 0:
                tract = 1
                bat = 0
                cam = 1
                grue = 0

            elif self.__nombreEtage == 1:
                tract = 0
                bat = 1
                cam = 0
                grue = 1
        
            elif self.__nombreEtage == 2:
                tract = 0
                bat = 2
                cam = 0
                grue = 1
        
            elif self.__nombreEtage == 3:
                tract = 1
                bat = 1
                cam = 1
                grue = 1
        
            elif self.__nombreEtage == 4:
                tract = 2
                bat = 2
                cam = 2
                grue = 2
        

            # Si le joueurs à les ressources, proposer de construire.
            if self.__jeu.joueurActif.jetonsTractopelle >= tract and self.__jeu.joueurActif.jetonsBateau >= bat and self.__jeu.joueurActif.jetonsCamion >= cam and self.__jeu.joueurActif.jetonsGrue >= grue:
                print("Le prix est de : " + str(tract) + " tractopelle, " +  str(bat) + " bateau, " +  str(cam) + " camion, " +  str(grue) + " grue.")
                if outils.ouiOuNon("Voulez-vous construire un etage sur ce batiment? Oui/Non"):

                    self.__nombreEtage += 1
                    
                    # update visuelle
                    (x,y,z) = self.scale
                    if self.__nombreEtage > 0:
                        self.scale = (x, self.__nombreEtage,z)
                
                    # verifier la pause de l'étage final
                    if self.__nombreEtage == 5:
                        outils.colored_print("Vous Avez gagné !!","red")
                        return()

                # Débiter les ressources au joueur
                self.__jeu.joueurActif.jetonsTractopelle -= tract
                self.__jeu.joueurActif.jetonsBateau -= bat
                self.__jeu.joueurActif.jetonsCamion -= cam
                self.__jeu.joueurActif.jetonsGrue_setter(self.__jeu.joueurActif.jetonsGrue - grue ) 

                # fin
                self.__construisible = False
                self.color = color.gray
            else:

                # afficher qu'il ne lui est pas possible d'achetter
                input("Vous n'avez pas la possiblilite de vous offrir un etage sur ce batiment, le prix est de : " + str(tract) + " tractopelle, " + str(bat) + " bateau, " + str(cam) + " camion, " + str(grue) + " grue. [ENTER] ")
                self.__construisible = False
                self.color = color.gray

            self.__jeu.tourEdition = False