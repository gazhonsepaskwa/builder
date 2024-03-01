"""
Qui: Amory
Quand: 
- 18/01/2024
Description: Le plateau de jeu sur lesquels les joueurs vont pouvoir
se déplacer lors de la partie
"""

##########
# import #
##########

from Joueur import *
from ursina import *
from Case import *
from Case_propriete import *
from Case_chance import *
from Case_police import *
from Case_ressource import *
from Case_vol import *

class Plateau(Entity):

    ################
    # constructeur #
    ################

    def __init__(self):
        super().__init__(
                model="cube",
                color=color.gray,
                scale=(8.5,0.1,8.5),
                position=(0,0,0),
            )

        self.__caseListe:list = []

    
    ################
    ### get, set ###
    ################
        
    @property
    def caseListe(self):
        return self.__caseListe



    #############
    # affichage #
    #############
        
    def __str__(self):
        print("")


    ############
    # methodes #
    ############
        
    # permet de genere les cases du jeu
    def genererCases(self):

        # se prendra de la DB en temps voulu
        c0 = Case           (0, (4, 0, -4),     couleur=color.green             )
        c1 = Case_propriete (1, (3, 0, -4),     "Nom a.1", 60, 10,  (2,0,0), 1  )
        c2 = Case_ressource (2, (2, 0, -4),     "camion" ,                      )
        c3 = Case_propriete (3, (1, 0, -4),     "Nom a.2", 60, 10,  (1,0,1), 1  )
        c4 = Case_vol       (4, (0, 0, -4)                                      )
        c5 = Case_propriete (5, (-1, 0, -4),    "Nom b.1", 100, 10, (1,0,0), 2  )
        c6 = Case_chance    (6, (-2, 0, -4)                                     )
        c7 = Case_propriete (7, (-3, 0, -4),    "Nom b.2", 100, 10, (0,0,1), 2  )
        c8 = Case           (8, (-4, 0, -4)                                     )
        c9 = Case_propriete (9, (-4, 0, -3),    "Nom c.1", 140, 10, (0,0,0), 3  )
        c10= Case_ressource (10,(-4, 0, -2),    "bateau"                        )
        c11= Case_propriete (11,(-4, 0, -1),    "Nom c.2", 140, 10, (1,0,-1), 3 )
        c12= Case_vol       (12,(-4, 0, 0),                                     )
        c13= Case_propriete (13,(-4, 0, 1),     "Nom d.1", 180, 10, (-1,0,0), 4 )
        c14= Case_chance    (14,(-4, 0, 2)                                      )
        c15= Case_propriete (15,(-4, 0, 3),     "Nom d.2", 180, 10, (0,0,-1), 4 )
        c16= Case           (16,(-4, 0, 4),                                     )
        c17= Case_propriete (17,(-3, 0, 4),     "Nom e.1", 220, 10, (-2,0,1), 5 )
        c18= Case_ressource (18,(-2, 0, 4),     "tractopelle"                   )
        c19= Case_propriete (19,(-1, 0, 4),     "Nom e.2", 220, 10, (-1,0,2), 5 )
        c20= Case_vol       (20,(0, 0, 4),                                      )
        c21= Case_propriete (21,(1, 0, 4),      "Nom f.1", 260, 10, (0,0,2), 6  )
        c22= Case_chance    (22,(2, 0, 4)                                       )
        c23= Case_propriete (23,(3, 0, 4),      "Nom f.2", 260, 10, (-1,0,1), 6 )
        c24= Case_police    (24,(4, 0, 4)                                       )
        c25= Case_propriete (25,(4, 0, 3),      "Nom g.1", 300, 10, (-2,0,-1), 7)
        c26= Case_ressource (26,(4, 0, 2),      "grue"                          )
        c27= Case_propriete (27,(4, 0, 1),      "Nom g.2", 300, 10, (-1,0,-2), 7)
        c28= Case_vol       (28,(4, 0, 0)                                       )
        c29= Case_propriete (29,(4, 0, -1),     "Nom h.1", 400, 10, (-1,0,-1), 8)
        c30= Case_chance    (30,(4, 0, -2)                                      )
        c31= Case_propriete (31,(4, 0, -3),     "Nom h.2", 400, 10, (0,0,-2), 8 )

        self.caseListe.append(c1)
        self.caseListe.append(c2)
        self.caseListe.append(c3)
        self.caseListe.append(c4)
        self.caseListe.append(c5)
        self.caseListe.append(c6)
        self.caseListe.append(c7)
        self.caseListe.append(c8)
        self.caseListe.append(c9)
        self.caseListe.append(c10)
        self.caseListe.append(c11)
        self.caseListe.append(c12)
        self.caseListe.append(c13)
        self.caseListe.append(c14)
        self.caseListe.append(c15)
        self.caseListe.append(c16)
        self.caseListe.append(c17)
        self.caseListe.append(c18)
        self.caseListe.append(c19)
        self.caseListe.append(c20)
        self.caseListe.append(c21)
        self.caseListe.append(c22)
        self.caseListe.append(c23)
        self.caseListe.append(c24)
        self.caseListe.append(c25)
        self.caseListe.append(c26)
        self.caseListe.append(c27)
        self.caseListe.append(c28)
        self.caseListe.append(c29)
        self.caseListe.append(c30)
        self.caseListe.append(c31)