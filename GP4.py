import heapq

class Mail:
    def __init__(self, sujet, priorite):
        self.sujet = sujet
        self.priorite = priorite  # plus petit nombre = plus haute priorité

    def __lt__(self, other):
        return self.priorite < other.priorite

    def __repr__(self):
        return f"({self.sujet}, priorité={self.priorite})"

class FilePriorite:
    def __init__(self):
        self.heap = []

    def inserer(self, mail):
        heapq.heappush(self.heap, mail)

    def extraire(self):
        if self.heap:
            return heapq.heappop(self.heap)
        else:
            print("File prioritaire vide")
            return None

    def afficher(self):
        print("État de la file prioritaire :", self.heap)

if __name__ == "__main__":
    file = FilePriorite()
    file.inserer(Mail("Réunion", 2))
    file.inserer(Mail("Urgent: panne serveur", 1))
    file.inserer(Mail("Info hebdo", 5))
    file.inserer(Mail("Demande congé", 3))

    print("Après insertion de mails :")
    file.afficher()

    print("\nExtraction du mail prioritaire :")
    mail = file.extraire()
    print(mail)
    file.afficher()

    print("\nExtraction du mail prioritaire :")
    mail = file.extraire()
    print(mail)
    file.afficher()

