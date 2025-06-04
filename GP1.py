class Contact:
    def __init__(self, nom, telephone):
        self.nom = nom
        self.telephone = telephone

    def __repr__(self):
        return f"{self.nom} : {self.telephone}"

class CarnetContacts:
    def __init__(self):
        self.contacts = []

    def ajouter(self, contact):
        if contact.nom not in [c.nom for c in self.contacts]:
            self.contacts.append(contact)

    def supprimer(self, nom):
        self.contacts = [c for c in self.contacts if c.nom != nom]

    def rechercher(self, nom):
        return [c for c in self.contacts if nom.lower() in c.nom.lower()]

    def trier(self):
        self.contacts.sort(key=lambda c: c.nom)

if __name__ == "__main__":
    carnet = CarnetContacts()
    carnet.ajouter(Contact("Beidi", "697241071"))
    carnet.ajouter(Contact("Dina", "620601651"))
    carnet.ajouter(Contact("Samuel", "697241071"))
    carnet.ajouter(Contact("Alice", "620601651"))  # doublon, ne doit pas être ajouté

    print("Liste initiale :")
    print(carnet.contacts)

    print("\nAprès tri :")
    carnet.trier()
    print(carnet.contacts)

    print("\nRésultat de recherche 'Di' :")
    print(carnet.rechercher("Di"))

    print("\nAprès suppression de Alice :")
    carnet.supprimer("Alice")
    print(carnet.contacts)

