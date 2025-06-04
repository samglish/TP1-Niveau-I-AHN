class NavigationWeb:
    def __init__(self):
        self.pile_retour = []
        self.pile_suivant = []
        self.page_courante = None

    def visiter(self, url):
        if self.page_courante:
            self.pile_retour.append(self.page_courante)
        self.page_courante = url
        self.pile_suivant.clear()

    def retour(self):
        if self.pile_retour:
            self.pile_suivant.append(self.page_courante)
            self.page_courante = self.pile_retour.pop()
        else:
            print("Pas de page précédente")

    def suivant(self):
        if self.pile_suivant:
            self.pile_retour.append(self.page_courante)
            self.page_courante = self.pile_suivant.pop()
        else:
            print("Pas de page suivante")

    def afficher_etat(self):
        print(f"Page courante : {self.page_courante}")
        print(f"Historique retour : {self.pile_retour}")
        print(f"Historique suivant : {self.pile_suivant}")

if __name__ == "__main__":
    nav = NavigationWeb()
    nav.visiter("google.com")
    nav.visiter("wikipedia.org")
    nav.visiter("openai.com")

    print("Etat initial après visites :")
    nav.afficher_etat()

    print("\nAction : retour")
    nav.retour()
    nav.afficher_etat()

    print("\nAction : retour")
    nav.retour()
    nav.afficher_etat()

    print("\nAction : suivant")
    nav.suivant()
    nav.afficher_etat()

    print("\nAction : visite nouvelle page (github.com)")
    nav.visiter("github.com")
    nav.afficher_etat()

    print("\nAction : tentative de suivant (devrait être vide)")
    nav.suivant()
    nav.afficher_etat()

