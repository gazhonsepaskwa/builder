"""
Qui: Amory
Quand: 
- 18/01/2024
Description: Les joueurs/adversaires qui disputent une partie
(matérialisés par des pions.)
"""

##########
# import #
##########


class Joueur():

    ################
    # constructeur #
    ################

    def __init__(self):
        self.__ID:str = ""
        self.__argent:int = 0
        self.__jetonsTractopelle:int = 0
        self.__jetonsBateau:int = 0
        self.__jetonsCamion:int = 0
        self.__jetonsGrue:int = 0
        self.__proprietes = []
        self.__etagesRestants:int = 0
        self.__valeurPremierLance:int = 0
        self.__caseActuelle:int = 0
        self.__caseListe = ""
        self.__derniereSommeDE: int = 0
        self.__enPrison: bool = False
        self.__pion = ""

    #############
    # affichage #
    #############
        
    def __str__(self):
        print("")
        
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

        if not(isinstance(leID, int) and >= 0):

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

        if not(isinstance(leJetonsTractopelle, int) and >= 0):

            raise TypeError("")

        self.__jetonsTractopelle = leJetonsTractopelle

    #Jetons qui pertmet de construire des étages sur les immeubles avec certaines combinaisons

    @property
    def jetonsBateau(self):
        return self.__jetonsBateau
    @jetonsBateau.setter
    def jetonsBateau(self, leJetonsBateau:int):
        
        #Test de la valeur reçue.

        if not(isinstance(leJetonsBateau, int) and >= 0):

            raise TypeError("")

        self.__jetonsBateau = leJetonsBateau

    #Jetons qui pertmet de construire des étages sur les immeubles avec certaines combinaisons

    @property
    def jetonsCamion(self):
        return self.__jetonsCamion
    @jetonsCamion.setter
    def jetonsCamion(self, leJetonsCamion:int):
        
        #Test de la valeur reçue.

        if not(isinstance(leJetonsCamion, int) and >= 0):

            raise TypeError("")

        self.__jetonsCamion = leJetonsCamion

    #Jetons qui pertmet de construire des étages sur les immeubles avec certaines combinaisons

    @property
    def jetonsGrue(self):
        return self.__jetonsGrue
    @jetonsGrue.setter
    def jetonsGrue(self, leJetonsGrue:int):
        
        #Test de la valeur reçue.

        if not(isinstance(leJetonsGrue, int) and >= 0):

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

        if not(isinstance(leValeurPremierLance, int) and leValeurPremierLance > 2 and leValeurPremierLance < 12):

            raise TypeError("")

        self.__valeurPremierLance = leValeurPremierLance

    #Case sur laquelle le joueur est actuellement

    @property
    def caseActuelle(self):
        return self.__caseActuelle
    @caseActuelle.setter
    def caseActuelle(self, leCaseActuelle):

        self.__caseActuelle = leCaseActuelle

    #Liste de cases disponible sur le plateau

    @property
    def caseListe(self):
        return self.__caseListe
    @caseListe.setter
    def caseListe(self, leCaseListe):
        self.__caseListe = leCaseListe

    #Dernière somme retenu après le lancé de dé

    @property
    def derniereSommeDE(self):
        return self.__derniereSommeDE
    @derniereSommeDE.setter
    def derniereSommeDE(self, leDerniereSomme:int):
    
        #Test de la valeur reçue.

        if not(isinstance(leDerniereSomme, int) and leDerniereSomme > 2 and leDerniereSomme < 12):

            raise TypeError("")

        self.__derniereSommeDE = leDerniereSomme

    #Envoi le joueur en prison

    @property
    def enPrison(self):
        return self.__enPrison
    @enPrison.setter
    def enPrison(self, leEnPrison:bool):
        self.__enPrison = leEnPrison

    #???

    @property
    def tourEditionFini(self):
        return self.__tourEditionFini
    @tourEditionFini.setter
    def tourEditionFini(self, val):
        self.__tourEditionFini = val

    #L'apparence du joueur

    @property
    def pion(self):
        return self.__pion
    @pion.setter
    def pion(self, val):
        self.__pion = val

    ############
    # methodes #
    ############
    
    #Les dés se font lancer

    def lancerDE(self):
        pass

    #Le joueur avance par rapport à la somme des dés lancés

    def avancer(self):
        pass