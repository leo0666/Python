"""
def creer_matrice():
    lignes = int(input("Entrez le nombre de lignes de la matrice : "))
    colonnes = int(input("Entrez le nombre de colonnes de la matrice : "))

    matrice = []
    for i in range(lignes):
        ligne = []
        for j in range(colonnes):
            valeur = float(input(f"Entrez la valeur pour la position ({i + 1}, {j + 1}) : "))
            ligne.append(valeur)
        matrice.append(ligne)

    return matrice


def afficher_matrice(matrice):
    for ligne in matrice:
        print(ligne)


def additionner_matrices(matrice1, matrice2):
    resultat = []
    for i in range(len(matrice1)):
        ligne_resultat = [matrice1[i][j] + matrice2[i][j] for j in range(len(matrice1[0]))]
        resultat.append(ligne_resultat)
    return resultat


def multiplier_matrices(matrice1, matrice2):
    resultat = []
    for i in range(len(matrice1)):
        ligne_resultat = [sum(matrice1[i][k] * matrice2[k][j] for k in range(len(matrice2))) for j in range(len(matrice2[0]))]
        resultat.append(ligne_resultat)
    return resultat


print("Matrice 1 :")
matrice1 = creer_matrice()

print("\nMatrice 2 :")
matrice2 = creer_matrice()

print("\nMatrice 1 :")
afficher_matrice(matrice1)

print("\nMatrice 2 :")
afficher_matrice(matrice2)

# Addition des matrices
resultat_addition = additionner_matrices(matrice1, matrice2)
print("\nAddition des matrices :")
afficher_matrice(resultat_addition)

# Multiplication des matrices
resultat_multiplication = multiplier_matrices(matrice1, matrice2)
print("\nMultiplication des matrices :")
afficher_matrice(resultat_multiplication)
"""

"""
from passlib.hash import bcrypt_sha256

print(bcrypt_sha256.hash('test!'))
"""
