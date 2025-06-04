def tri_insertion(etudiants):
    for i in range(1, len(etudiants)):
        cle = etudiants[i]
        j = i - 1
        while j >= 0 and etudiants[j]["moyenne"] > cle["moyenne"]:
            etudiants[j + 1] = etudiants[j]
            j -= 1
        etudiants[j + 1] = cle
    return etudiants

def tri_rapide(etudiants):
    if len(etudiants) <= 1:
        return etudiants
    pivot = etudiants[0]
    inferieur = [e for e in etudiants[1:] if e["moyenne"] <= pivot["moyenne"]]
    superieur = [e for e in etudiants[1:] if e["moyenne"] > pivot["moyenne"]]
    return tri_rapide(inferieur) + [pivot] + tri_rapide(superieur)

def afficher(etudiants):
    for e in etudiants:
        print(f"{e['nom']} - Moyenne : {e['moyenne']}")

if __name__ == "__main__":
    liste_etudiants = [
        {"nom": "Alice", "moyenne": 14.5},
        {"nom": "Bruno", "moyenne": 11.2},
        {"nom": "Claire", "moyenne": 16.3},
        {"nom": "David", "moyenne": 9.8},
        {"nom": "Eva", "moyenne": 13.0}
    ]

    print("Classement avec tri par insertion :")
    classement_insertion = tri_insertion(liste_etudiants.copy())
    afficher(classement_insertion)

    print("\nClassement avec tri rapide :")
    classement_rapide = tri_rapide(liste_etudiants.copy())
    afficher(classement_rapide)

