"""
Qui: Nathan
Quand: 
- 18/01/2024 Nathan
Description: Objet qui permet de gérer les transfert d'argent entre les joueurs

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
        print("Bonjour, je suis la banque ! Je sers principalement à permettre aux joueurs d'effectuer des paiements en eux si l'un d'eux tombe sur la propriété d'un autre")
        
    

    ###########################
    # accesseurs et mutateurs #
    ###########################
        

    """
    joueur qui envoie l'argent
    """
    @property
    def envoyeur(self):
        return self.__envoyeur
    @envoyeur.setter
    def envoyeur(self, val):
        self.__envoyeur = val


    """
    joueur qui reçois l'argent
    """
    @property
    def receveur(self):
        return self.__receveur
    @receveur.setter
    def receveur(self, nom):
        self.__receveur = nom



    ############
    # methodes #
    ############
    
    """
    méthode qui permet de transférer une somme d'argent à un joueur
    """
    def tranferer(self, somme):
        Banque.envoyeur.argent = Banque.envoyeur.argent - somme
        Banque.receveur.argent = Banque.receveur.argent + somme


    """
    méthode qui permet de modifier la balance d'un joueur
    """
    def modifierBalance(self, joueur, somme):
        
        joueur.argent = joueur.argent + somme