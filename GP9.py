class NoeudTrie:
    def __init__(self):
        self.enfants = {}
        self.fin_mot = False

class Trie:
    def __init__(self):
        self.racine = NoeudTrie()

    def inserer(self, mot):
        noeud = self.racine
        for lettre in mot:
            if lettre not in noeud.enfants:
                noeud.enfants[lettre] = NoeudTrie()
            noeud = noeud.enfants[lettre]
        noeud.fin_mot = True

    def rechercher(self, mot):
        noeud = self.racine
        for lettre in mot:
            if lettre not in noeud.enfants:
                return False
            noeud = noeud.enfants[lettre]
        return noeud.fin_mot

    def autocompletion(self, prefixe):
        resultats = []
        noeud = self.racine
        for lettre in prefixe:
            if lettre not in noeud.enfants:
                return resultats
            noeud = noeud.enfants[lettre]
        self._explorer(noeud, prefixe, resultats)
        return resultats

    def _explorer(self, noeud, prefixe, resultats):
        if noeud.fin_mot:
            resultats.append(prefixe)
        for lettre, enfant in noeud.enfants.items():
            self._explorer(enfant, prefixe + lettre, resultats)

if __name__ == "__main__":
    trie = Trie()
    mots = ["chat", "chien", "chou", "champ", "chance", "chapeau", "livre"]
    for mot in mots:
        trie.inserer(mot)

    print("Recherche exacte :")
    print("  'chien' trouvé :", trie.rechercher("chien"))
    print("  'chouette' trouvé :", trie.rechercher("chouette"))

    print("\nAuto-complétion pour 'cha' :")
    suggestions = trie.autocompletion("cha")
    print("  Suggestions :", suggestions)

    print("\nAuto-complétion pour 'liv' :")
    print("  Suggestions :", trie.autocompletion("liv"))

