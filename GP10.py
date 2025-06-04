class Etape:
    def __init__(self, nom):
        self.nom = nom
        self.suivant = None

class ProcessusFabrication:
    def __init__(self):
        self.tete = None

    def ajouter_etape(self, nom):
        nouvelle = Etape(nom)
        if not self.tete:
            self.tete = nouvelle
        else:
            courant = self.tete
            while courant.suivant:
                courant = courant.suivant
            courant.suivant = nouvelle

    def inserer_apres(self, nom_cible, nom_nouvelle):
        courant = self.tete
        while courant and courant.nom != nom_cible:
            courant = courant.suivant
        if courant:
            nouvelle = Etape(nom_nouvelle)
            nouvelle.suivant = courant.suivant
            courant.suivant = nouvelle

    def supprimer_etape(self, nom):
        if not self.tete:
            return
        if self.tete.nom == nom:
            self.tete = self.tete.suivant
            return
        precedent = self.tete
        courant = self.tete.suivant
        while courant and courant.nom != nom:
            precedent = courant
            courant = courant.suivant
        if courant:
            precedent.suivant = courant.suivant

    def afficher_processus(self):
        courant = self.tete
        etapes = []
        while courant:
            etapes.append(courant.nom)
            courant = courant.suivant
        print(" → ".join(etapes) if etapes else "Aucune étape")

if __name__ == "__main__":
    processus = ProcessusFabrication()
    processus.ajouter_etape("Découpe")
    processus.ajouter_etape("Assemblage")
    processus.ajouter_etape("Peinture")

    print("Étapes initiales :")
    processus.afficher_processus()

    print("\nInsertion après 'Assemblage' :")
    processus.inserer_apres("Assemblage", "Contrôle qualité")
    processus.afficher_processus()

    print("\nSuppression de l'étape 'Découpe' :")
    processus.supprimer_etape("Découpe")
    processus.afficher_processus()

