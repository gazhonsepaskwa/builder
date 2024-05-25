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
- 23/05/2024 Amory
- 24/05/2024 Amory
- 25/05/2024 Nathan
- 26/05/2024 Amory

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

        voleur = voleur_

        for joueur in listeJoueurs:

            listeDesJoueursVictime.append(joueur)
        
        while True:
        
            print("Choisissez une victime parmis ces joueurs (Pour choisir un joueur que vous voulez voler, il faut écrire le nombre qui lui est associé) :")

            for i, potentielleVictime in enumerate(listeDesJoueursVictime):

                print(f"{i} {potentielleVictime.nom} {potentielleVictime.jetonsTractopelle} {potentielleVictime.jetonsBateau} {potentielleVictime.jetonsCamion} {potentielleVictime.jetonsGrue}")

            try :

                victimeEncodage = int(input(""))

                if 0 <= victimeEncodage < len(listeDesJoueursVictime) and isinstance(victimeEncodage, int):
                    
                    victime = listeDesJoueursVictime[victimeEncodage]
                    
                    break

                else:
                    print("Veuillez recommencer en encodant un entier compris dans la liste des joueurs")

            except:
                pass

        # Demande le type de ressource à voler 
        while True:
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

                break 

            elif choix == "bateau":
                    
                voleur.jetonsBateau += 1 
                victime.jetonsBateau -= 1

                break


            elif choix == "camion":

                voleur.jetonsCamion += 1 
                victime.jetonsCamion -= 1

                break

            elif choix == "grue":

                voleur.jetonsGrue += 1 
                victime.jetonsGrue -= 1

                break