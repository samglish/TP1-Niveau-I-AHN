class NoeudNAire:
    def __init__(self, nom, est_dossier=True):
        self.nom = nom
        self.est_dossier = est_dossier
        self.enfants = []  # liste des Noeuds enfants

    def ajouter_enfant(self, enfant):
        if self.est_dossier:
            self.enfants.append(enfant)
        else:
            print(f"Impossible d'ajouter un enfant à un fichier: {self.nom}")

    def afficher(self, niveau=0):
        prefixe = "  " * niveau + ("[D] " if self.est_dossier else "[F] ")
        print(f"{prefixe}{self.nom}")
        for enfant in self.enfants:
            enfant.afficher(niveau + 1)

if __name__ == "__main__":
    racine = NoeudNAire("Racine", est_dossier=True)
    dossier1 = NoeudNAire("Documents", est_dossier=True)
    dossier2 = NoeudNAire("Images", est_dossier=True)
    fichier1 = NoeudNAire("cv.pdf", est_dossier=False)
    fichier2 = NoeudNAire("photo.jpg", est_dossier=False)

    racine.ajouter_enfant(dossier1)
    racine.ajouter_enfant(dossier2)
    dossier1.ajouter_enfant(fichier1)
    dossier2.ajouter_enfant(fichier2)

    print("Structure de fichiers :")
    racine.afficher()

