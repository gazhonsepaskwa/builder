"""
Qui: Nathan
Quand: 
- 18/01/2024 Nathan
- 26/02/2024 Nathan
- 27/02/2024 Nathan
- 29/02/2024 Nathan
- 02/04/2024 Nathan
- 10/05/2024 Nathan
- 18/05/2024 Nathan
Description: Case qui permet de tirer une carte
chance et faire l'action inscrite dessus via chance()

"""

##########
# import #
##########

from Case import *
from random import *

class Case_chance(Case):

    ################
    # constructeur #
    ################

    def __init__(self,num ,pos):
        super().__init__(num, pos, couleur=color.gold)




    #############
    # affichage #
    #############
        
    def __str__(self):
        print("")
        
    

    ############
    # methodes #
    ############


    # Permet de tirer une carte chance et faire l'action inscrite dessus

    def chance(self, jeu):

        db = mysql.connector.connect(
            host="localhost",
            user="root",
            password="root",
            database="builder"
            )
        
        curseur = db.cursor()

        curseur.execute("SELECT COUNT(*) FROM CarteChance")
        nombre_total_lignes = curseur.fetchone()[0]

        # Générer un id aléatoire
        id_ = random.randint(0, nombre_total_lignes - 1)
        val = (id_,)
        sql = "SELECT titre, contenu, action FROM CarteChance WHERE id_CarteChance = %s"

        curseur.execute(sql, val)
        retour = curseur.fetchone()

        # Assigner le retour au variables de générations
        if retour: titre, contenu, action = retour 
        else: raise ValueError(f"La base de donnée n'a rien retourner pour l'ID {i}")

        print(f"Titre: {titre}")
        print(f"description: {contenu}")
        exec(action)