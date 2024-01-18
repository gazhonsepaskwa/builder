"""
Qui: Nathan
Quand: 2021-05-23
Description: Carte qui quand tirée fait une action "choisie au hasard"

"""

##########
# import #
##########


class CarteChances():

    ################
    # constructeur #
    ################

    def __init__(self):
        self.__titre: str = ""
        self.__contenu: str = ""
        self.__identifiant: int = 0



    #############
    # affichage #
    #############
        
    def __str__(self):
        print("")
        
    

    ###########################
    # accesseurs et mutateurs #
    ###########################
        
    """
    Titre en haut de la carte
    """
    @property
    def titre(self):
        return self.__titre
    @titre.setter
    def titre(self, val):
        self.__titre = val

    """
    contenu texte de la carte
    """
    @property
    def contenu(self):
        return self.__contenu
    @contenu.setter
    def contenu(self, val):
        self.__contenu = val

    """
    identifiant de la carte: 
    permet de distinguer les cartes de la même classe pour executer l'action adéquoite
    """
    @property
    def identifiant(self):
        return self.__identifiant
    @identifiant.setter
    def identifiant(self, val):
        self.__identifiant = val
    


    ############
    # methodes #
    ############
    
    """
    action faite par la carte de chance(difere en fonction de l'identifiant et donc de la carte)
    """
    def action(self):
        pass