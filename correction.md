```python
# CORRECTION COMPLÈTE DU TPE - STRUCTURES DE DONNÉES EN PYTHON

# Groupe 1 : Tableaux dynamiques (Carnet de contacts)
class CarnetContacts:
    def __init__(self):
        self.contacts = []

    def ajouter_contact(self, nom):
        if nom not in self.contacts:
            self.contacts.append(nom)

    def supprimer_contact(self, nom):
        if nom in self.contacts:
            self.contacts.remove(nom)

    def trier_contacts(self):
        self.contacts.sort()

    def rechercher_contact(self, nom):
        return nom in self.contacts

    def afficher(self):
        print("Carnet:", self.contacts)


# Groupe 2 : Piles (Navigation Web)
class Navigateur:
    def __init__(self):
        self.retour = []
        self.suivant = []
        self.page_actuelle = None

    def visiter(self, page):
        if self.page_actuelle:
            self.retour.append(self.page_actuelle)
        self.page_actuelle = page
        self.suivant.clear()

    def precedent(self):
        if self.retour:
            self.suivant.append(self.page_actuelle)
            self.page_actuelle = self.retour.pop()

    def avancer(self):
        if self.suivant:
            self.retour.append(self.page_actuelle)
            self.page_actuelle = self.suivant.pop()

    def afficher(self):
        print("Page actuelle:", self.page_actuelle)


# Groupe 3 : Files (Agence)
from collections import deque

class FileClients:
    def __init__(self):
        self.file = deque()

    def ajouter_client(self, nom):
        self.file.append(nom)

    def servir_client(self):
        if self.file:
            return self.file.popleft()
        return None

    def afficher(self):
        print("File:", list(self.file))


# Groupe 4 : File de priorité (Mails urgents)
import heapq

class Mail:
    def __init__(self, urgence, contenu):
        self.urgence = urgence
        self.contenu = contenu

    def __lt__(self, other):
        return self.urgence < other.urgence

class GestionMails:
    def __init__(self):
        self.file_priorite = []

    def ajouter_mail(self, mail):
        heapq.heappush(self.file_priorite, mail)

    def traiter_mail(self):
        if self.file_priorite:
            return heapq.heappop(self.file_priorite)
        return None


# Groupe 5 : Arbre binaire (Calculatrice)
class Noeud:
    def __init__(self, valeur):
        self.valeur = valeur
        self.gauche = None
        self.droite = None

def evaluer(noeud):
    if noeud.valeur.isdigit():
        return int(noeud.valeur)
    g = evaluer(noeud.gauche)
    d = evaluer(noeud.droite)
    if noeud.valeur == '+': return g + d
    if noeud.valeur == '-': return g - d
    if noeud.valeur == '*': return g * d
    if noeud.valeur == '/': return g / d


# Groupe 6 : Arbre n-aire (Explorateur de fichiers)
class Dossier:
    def __init__(self, nom):
        self.nom = nom
        self.sous_elements = []

    def ajouter(self, element):
        self.sous_elements.append(element)

    def afficher(self, indent=0):
        print("  " * indent + self.nom)
        for e in self.sous_elements:
            e.afficher(indent + 1)


# Groupe 7 : Graphes pondérés (GPS)
import heapq

def dijkstra(graphe, depart):
    distances = {sommet: float('inf') for sommet in graphe}
    distances[depart] = 0
    file = [(0, depart)]
    while file:
        dist, courant = heapq.heappop(file)
        for voisin, poids in graphe[courant]:
            if dist + poids < distances[voisin]:
                distances[voisin] = dist + poids
                heapq.heappush(file, (dist + poids, voisin))
    return distances


# Groupe 8 : Table de hachage (Dictionnaire bilingue)
class Dictionnaire:
    def __init__(self):
        self.table = {}

    def ajouter(self, mot, traduction):
        self.table[mot] = traduction

    def traduire(self, mot):
        return self.table.get(mot, "Inconnu")


# Groupe 9 : Trie (Suggestions de mots)
class TrieNode:
    def __init__(self):
        self.enfants = {}
        self.fin_mot = False

class Trie:
    def __init__(self):
        self.racine = TrieNode()

    def inserer(self, mot):
        node = self.racine
        for char in mot:
            if char not in node.enfants:
                node.enfants[char] = TrieNode()
            node = node.enfants[char]
        node.fin_mot = True

    def rechercher(self, prefixe):
        node = self.racine
        for char in prefixe:
            if char not in node.enfants:
                return []
            node = node.enfants[char]
        return self._suggestions(prefixe, node)

    def _suggestions(self, prefixe, node):
        mots = []
        if node.fin_mot:
            mots.append(prefixe)
        for char, enfant in node.enfants.items():
            mots.extend(self._suggestions(prefixe + char, enfant))
        return mots


# Groupe 10 : Liste chaînée (Suivi de fabrication)
class Etape:
    def __init__(self, nom):
        self.nom = nom
        self.suivant = None

class Processus:
    def __init__(self):
        self.debut = None

    def ajouter_etape(self, nom):
        etape = Etape(nom)
        if not self.debut:
            self.debut = etape
        else:
            temp = self.debut
            while temp.suivant:
                temp = temp.suivant
            temp.suivant = etape

    def afficher(self):
        temp = self.debut
        while temp:
            print(temp.nom, end=" -> ")
            temp = temp.suivant
        print("Fin")


# Groupe 11 : Tri (Classement étudiants)
def tri_insertion(liste):
    for i in range(1, len(liste)):
        cle = liste[i]
        j = i - 1
        while j >= 0 and liste[j]['moyenne'] > cle['moyenne']:
            liste[j + 1] = liste[j]
            j -= 1
        liste[j + 1] = cle

def tri_rapide(liste):
    if len(liste) <= 1:
        return liste
    pivot = liste[0]
    inf = [x for x in liste[1:] if x['moyenne'] < pivot['moyenne']]
    sup = [x for x in liste[1:] if x['moyenne'] >= pivot['moyenne']]
    return tri_rapide(inf) + [pivot] + tri_rapide(sup)


# === TEST PRINCIPAL ===
if __name__ == '__main__':
    print("--- Groupe 1 ---")
    c = CarnetContacts()
    c.ajouter_contact("Alice")
    c.ajouter_contact("Bob")
    c.trier_contacts()
    c.afficher()

    print("\n--- Groupe 2 ---")
    n = Navigateur()
    n.visiter("page1")
    n.visiter("page2")
    n.precedent()
    n.afficher()

    print("\n--- Groupe 3 ---")
    f = FileClients()
    f.ajouter_client("Client1")
    f.ajouter_client("Client2")
    f.servir_client()
    f.afficher()

    print("\n--- Groupe 4 ---")
    gm = GestionMails()
    gm.ajouter_mail(Mail(1, "Urgent"))
    gm.ajouter_mail(Mail(3, "Normal"))
    print(gm.traiter_mail().contenu)

    print("\n--- Groupe 5 ---")
    racine = Noeud('/')
    racine.gauche = Noeud('*')
    racine.gauche.gauche = Noeud('+')
    racine.gauche.gauche.gauche = Noeud('2')
    racine.gauche.gauche.droite = Noeud('3')
    racine.gauche.droite = Noeud('4')
    racine.droite = Noeud('5')
    print("Résultat:", evaluer(racine))

    print("\n--- Groupe 6 ---")
    racine = Dossier("C:")
    dossier1 = Dossier("Documents")
    racine.ajouter(dossier1)
    dossier1.ajouter(Dossier("Cours"))
    racine.afficher()

    print("\n--- Groupe 7 ---")
    g = {
        'A': [('B', 1), ('C', 4)],
        'B': [('C', 2), ('D', 5)],
        'C': [('D', 1)],
        'D': []
    }
    print(dijkstra(g, 'A'))

    print("\n--- Groupe 8 ---")
    dico = Dictionnaire()
    dico.ajouter("chat", "cat")
    print(dico.traduire("chat"))

    print("\n--- Groupe 9 ---")
    t = Trie()
    t.inserer("chien")
    t.inserer("chat")
    t.inserer("chapeau")
    print(t.rechercher("cha"))

    print("\n--- Groupe 10 ---")
    p = Processus()
    p.ajouter_etape("Découpe")
    p.ajouter_etape("Assemblage")
    p.afficher()

    print("\n--- Groupe 11 ---")
    etudiants = [{'nom': 'Alice', 'moyenne': 12}, {'nom': 'Bob', 'moyenne': 15}]
    tri_insertion(etudiants)
    print(etudiants)
    print(tri_rapide(etudiants))
```