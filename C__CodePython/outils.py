# retourne True si vrai et False si non
def ouiOuNon(question):
    oui = ["yes", "y", "oui", "o"]
    non = ["no", "n", "non"]

    entree = input(question)

    while True:
        if entree.lower() in oui:
            return True
        elif entree.lower() in non:
            return False
        else:
            print("Veuillez répondre par 'oui' ou 'non'.")