##########
# import #
##########


class Nom():

    ################
    # constructeur #
    ################

    def __init__(self, nom):
        self.__nom = nom



    #############
    # affichage #
    #############
        
    def __str__(self):
        print("")
        
    

    ###########################
    # accesseurs et mutateurs #
    ###########################
        
    @property
    def nom(self):
        pass
    @nom.setter
    def nom(self, nom):
        self.__nom = nom



    ############
    # methodes #
    ############
    
    def methode(self):
        pass