import heapq

class Graphe:
    def __init__(self):
        self.adjacence = {}  # dictionnaire {noeud: [(voisin, poids), ...]}

    def ajouter_sommet(self, sommet):
        if sommet not in self.adjacence:
            self.adjacence[sommet] = []

    def ajouter_arete(self, u, v, poids):
        self.ajouter_sommet(u)
        self.ajouter_sommet(v)
        self.adjacence[u].append((v, poids))
        self.adjacence[v].append((u, poids))  # graphe non orienté

    def dijkstra(self, depart):
        distances = {sommet: float('inf') for sommet in self.adjacence}
        distances[depart] = 0
        file = [(0, depart)]

        while file:
            distance_actuelle, sommet = heapq.heappop(file)
            if distance_actuelle > distances[sommet]:
                continue

            for voisin, poids in self.adjacence[sommet]:
                distance = distance_actuelle + poids
                if distance < distances[voisin]:
                    distances[voisin] = distance
                    heapq.heappush(file, (distance, voisin))

        return distances

if __name__ == "__main__":
    g = Graphe()
    g.ajouter_arete("A", "B", 4)
    g.ajouter_arete("A", "C", 2)
    g.ajouter_arete("B", "C", 1)
    g.ajouter_arete("B", "D", 5)
    g.ajouter_arete("C", "D", 8)
    g.ajouter_arete("C", "E", 10)
    g.ajouter_arete("D", "E", 2)

    print("Plus courts chemins depuis A :")
    distances = g.dijkstra("A")
    for ville, distance in distances.items():
        print(f"  A → {ville} = {distance}")

