"""
Qui: Nathan
Quand: 
- 18/01/2024 Nathan
- 12/02/2024 Nathan
- 15/02/2024 Nathan
- 24/02/2024 Nathan
- 26/02/2024 Nathan
- 29/02/2024 Nathan
- 01/03/2024 Nathan
- 16/05/2024 Nathan
- 17/05/2024 Nathan
- 18/05/2024 Nathan
- 20/05/2024 Nathan
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
from outils import ouiOuNon

import mysql.connector

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
        print("Bonjour, je suis le plateau ! Les joueurs se déplacent sur moi, par le biais de cases.")


    ############
    # methodes #
    ############
        
    # permet de genere les cases du jeu
    def genererCases(self):
        
        if ouiOuNon("Taper 1 pour utiliser les données en dure pour la génération des cases ou 0 pour les données via l'acces à la base de donnée"): 

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

        else: 

            # connection a la db
            db = mysql.connector.connect(
            host="localhost",
            user="builderADMIN",
            password="p@sW0rDssss",
            database="builder"
            )

            curseur = db.cursor()

            for i in range(0, 31):

                parametre = ''
                
                sql = "SELECT type_case, nom, prix, loyer, resource_contenue FROM Cases WHERE id_Cases = %s"
                id_ = i + 1
                val = (id_,)

                curseur.execute(sql, val)
                retour = curseur.fetchone()

                # Assigner le retour au variables de générations
                if retour: type_case, nom_propriete, prix, loyer, resource_contenue = retour 
                else: raise ValueError(f"La base de donnée n'a rien retourner pour l'ID {i}")

                # en dure car pas dans la db
                pos_batt = "(2,0,0)"
                num_hamaux = "1"

                # position des cases dynamiquement "alouées"
                if i >= 0 and i <= 8:
                    pos_case = f"( {4-i}, 0, -4)"
                elif i >= 9 and i <= 16:
                    pos_case = f"( -4, 0, {-4 + (i-9)})"
                elif i >= 17 and i <= 24:
                    pos_case = f"( {-4 + (i-16)}, 0, 4)"
                elif i >= 25 and i <= 31:
                    pos_case = f"( 4, 0, {4 - (i-24)})"

                #génération des paramètres
                if type_case == "Case": parametre = 'couleur=color.green'
                elif type_case == "Case_propriete": parametre = f'"{nom_propriete}", {prix}, {loyer},  {pos_batt}, {num_hamaux}'
                elif type_case == "Case_ressource": parametre = f'"{resource_contenue}" '
                else : parametre = ''

                # execution de la génération
                exec(f"c{i} = {type_case} ({i}, {pos_case}, {parametre} )")
                exec(f"self.caseListe.append(c{i})")

            curseur.close()
            db.close()