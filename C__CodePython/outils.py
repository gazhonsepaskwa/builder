"""
Qui: Nathan
Quand: 
- 18/01/2024
Description: outils de developpement
"""

# retourne True si vrai et False sinon
def ouiOuNon(question):
    oui = ["yes", "y", "oui", "o", "1"]
    non = ["no", "n", "non", "0"]

    while True:
        entree = input(question)

        if entree.lower() in oui:
            return True
        elif entree.lower() in non:
            return False
        else:
            print("Veuillez répondre par 'oui', 'non' ou une variante.")