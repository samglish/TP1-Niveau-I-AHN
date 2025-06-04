from collections import deque

class FileClients:
    def __init__(self):
        self.file = deque()

    def inserer(self, client):
        self.file.append(client)

    def supprimer(self):
        if self.file:
            return self.file.popleft()
        else:
            print("File vide")
            return None

    def afficher(self):
        print("État de la file :", list(self.file))

if __name__ == "__main__":
    file = FileClients()
    file.inserer("Client1")
    file.inserer("Client2")
    file.inserer("Client3")

    print("Après insertion de 3 clients :")
    file.afficher()

    print("\nSuppression d'un client :")
    supprime = file.supprimer()
    print(f"Client supprimé : {supprime}")
    file.afficher()

    print("\nSuppression d'un client :")
    supprime = file.supprimer()
    print(f"Client supprimé : {supprime}")
    file.afficher()

    print("\nSuppression d'un client :")
    supprime = file.supprimer()
    print(f"Client supprimé : {supprime}")
    file.afficher()

    print("\nTentative suppression sur file vide :")
    supprime = file.supprimer()

