"""
Qui: Amory
Quand: 18/01/2023
Description: 

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
        
    @property
    def ID(self):
        return self.__ID
    @ID.setter
    def ID(self, val):
        self.__val

    @property
    def argent(self):
        return self.__argent
    @argent.setter
    def argent(self, val):
        self.__val

    @property
    def jetonsTractopelle(self):
        return self.__jetonsTractopelle
    @jetonsTractopelle.setter
    def jetonsTractopelle(self, val):
        self.__val

    @property
    def jetonsBateau(self):
        return self.__jetonsBateau
    @jetonsBateau.setter
    def jetonsBateau(self, val):
        self.__val

    @property
    def jetonsCamion(self):
        return self.__jetonsCamion
    @jetonsCamion.setter
    def jetonsCamion(self, val):
        self.__val

    @property
    def jetonsGrue(self):
        return self.__jetonsGrue
    @jetonsGrue.setter
    def jetonsGrue(self, val):
        self.__val

    @property
    def proprietes(self):
        return self.__proprietes
    @proprietes.setter
    def proprietes(self, val):
        self.__val

    @property
    def etagesRestants(self):
        return self.__etagesRestants
    @etagesRestants.setter
    def etagesRestants(self, val):
        self.__val

    @property
    def valeurPremierLance(self):
        return self.__valeurPremierLance
    @valeurPremierLance.setter
    def valeurPremierLance(self, val):
        self.__val

    @property
    def caseActuelle(self):
        return self.__caseActuelle
    @caseActuelle.setter
    def caseActuelle(self, val):
        self.__val

    @property
    def caseListe(self):
        return self.__caseListe
    @caseListe.setter
    def caseListe(self, val):
        self.__val

    @property
    def derniereSommeDE(self):
        return self.__derniereSommeDE
    @derniereSommeDE.setter
    def derniereSommeDE(self, val):
        self.__val

    @property
    def enPrison(self):
        return self.__enPrison
    @enPrison.setter
    def enPrison(self, val):
        self.__val

    @property
    def tourEditionFini(self):
        return self.__tourEditionFini
    @tourEditionFini.setter
    def tourEditionFini(self, val):
        self.__val

    @property
    def pion(self):
        return self.__pion
    @pion.setter
    def pion(self, val):
        self.__val

    ############
    # methodes #
    ############
    
    def lancerDE(self):
        pass

    def avancer(self):
        pass