class DictionnaireBilingue:
    def __init__(self, taille=10):
        self.taille = taille
        self.table = [[] for _ in range(taille)]  # table de hachage avec chaînage

    def hachage(self, mot):
        return sum(ord(c) for c in mot) % self.taille

    def ajouter(self, mot, traduction):
        index = self.hachage(mot)
        for i, (m, _) in enumerate(self.table[index]):
            if m == mot:
                self.table[index][i] = (mot, traduction)
                return
        self.table[index].append((mot, traduction))

    def traduire(self, mot):
        index = self.hachage(mot)
        for m, t in self.table[index]:
            if m == mot:
                return t
        return "Mot non trouvé"

    def afficher(self):
        for i, case in enumerate(self.table):
            print(f"Case {i} : {case}")

if __name__ == "__main__":
    dico = DictionnaireBilingue()

    dico.ajouter("chat", "cat")
    dico.ajouter("chien", "dog")
    dico.ajouter("maison", "house")
    dico.ajouter("fromage", "cheese")
    dico.ajouter("livre", "book")

    print("Traductions :")
    print("  chat →", dico.traduire("chat"))
    print("  chien →", dico.traduire("chien"))
    print("  arbre →", dico.traduire("arbre"))  # mot non trouvé

    print("\nContenu de la table :")
    dico.afficher()

