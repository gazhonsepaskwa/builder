"""
Qui: Nathan
Quand: 
- 18/01/2024
Description: outils de developpement
"""

# retourne True si vrai et False si non
def ouiOuNon(question):
    oui = ["yes", "y", "oui", "o"]
    non = ["no", "n", "non"]

    while True:
        entree = input(question)

        if entree.lower() in oui:
            return True
        elif entree.lower() in non:
            return False
        else:
            print("Veuillez répondre par 'oui' ou 'non'.")