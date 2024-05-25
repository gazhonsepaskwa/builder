"""
Qui: Amory et Nathan
Quand: 
- 18/01/2024 Amory
- 26/02/2024 Nathan
- 27/02/2024 Nathan
- 28/02/2024 Nathan
- 29/02/2024 Nathan
- 01/03/2024 Nathan
- 20/05/2024 Nathan
- 25/05/2024 Nathan

Description: La case vol, est une case qui permet à un joueur de voler
l'une des ressources d'un autre joueur.

"""

##########
# import #
##########

from Joueur import *
from Jeu import *
from Case import *

class Case_vol(Case):

    ################
    # constructeur #
    ################

    def __init__(self, num, pos):
        super().__init__(num, pos, texture="img/vol.png")

    #############
    # affichage #
    #############
        
    def __str__(self):
        print("Bonjour, je suis la case vol ! Je permet aux joueurs de se voler des ressources entre eux. Mouhahahaha !")


    ############
    # methodes #
    ############
        
    def voler(self, voleur_, listeJoueurs):
        
        listeDesJoueursVictime = []

        # attribution de voleur et victime
        voleur = voleur_

        for i in listeJoueurs:

            if Joueur.nom != Jeu.joueurActif.nom:
                listeDesJoueursVictime.append(Joueur.nom)
        
        while True:
        
            print("Choisissez une victime parmis ces joueurs (Pour choisir un joueur que vous voulez voler, il faut écrire le nombre qui lui est associé) :")

            for i in listeDesJoueursVictime:

                print(f"{i} + {listeDesJoueursVictime[i]}")

            victime = int(input(""))

            if not(isinstance(victime, int)):

                print("Veuillez recommencer en encodant le nombre associé à la personne que vous désirez voler")
            
            else :
            
                break

        # Demande le type de ressource à voler 
        tmp = input("Quelle ressource voulez-vous voler ? ( 1: tractopelle | 2: bateau | 3: camion | 4: grue ) >>")
        if tmp == "1": choix = "tractopelle"
        elif tmp == "2": choix = "bateau"
        elif tmp == "3": choix = "camion"
        elif tmp == "4": choix = "grue"
        else: 
            print("Choix invalide")
            choix = ""

        

        if choix == "tractopelle":

            voleur.jetonsTractopelle += 1 
            victime.jetonsTractopelle -= 1 

        elif choix == "bateau":

            voleur.jetonsBateau += 1 
            victime.jetonsBateau -= 1

        elif choix == "camion":

            voleur.jetonsCamion += 1 
            victime.jetonsCamion -= 1

        elif choix == "grue":

            voleur.jetonsGrue += 1 
            victime.jetonsGrue -= 1 