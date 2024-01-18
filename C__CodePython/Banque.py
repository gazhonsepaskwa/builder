"""
Qui: Nathan
Quand: 
- 18/01/2024
Description: Objet qui permet de gérer les transfert entre les joueurs

"""


##########
# import #
##########

from Joueur import *

class Banque():

    ################
    # constructeur #
    ################

    def __init__(self):
        self.__envoyeur:Joueur = None
        self.__receveur:Joueur = None



    #############
    # affichage #
    #############
        
    def __str__(self):
        print("")
        
    

    ###########################
    # accesseurs et mutateurs #
    ###########################
        

    """
    joueur qui envoie l'argent
    """
    @property
    def envoyeur(self):
        pass
    @envoyeur.setter
    def envoyeur(self, val):
        self.__envoyeur = val


    """
    joueur qui reçois l'argent
    """
    @property
    def receveur(self):
        pass
<<<<<<< Updated upstream
    @envoyeur.setter
    def receveur(self, val):
        self.__receveur = val
=======
    @receveur.setter
    def receveur(self, nom):
        self.__receveur = nom
>>>>>>> Stashed changes



    ############
    # methodes #
    ############
    
    """
    méthode qui permet de transférer une somme d'argent à un joueur
    """
    def tranferer(self, somme):
        pass


    """
    méthode qui permet de modifier la balance d'un joueur
    """
    def modifierBalance(self, joueur, somme):
        pass