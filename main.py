from cat_informatique import gen_pwd_hash, level_pwd_security, password_manager, bruteforce, file_encrypt_decrypt, réseau
from cat_math import calcul, convert, temps_distance_vitesse, random_num
from cat_physic import period_freq

while True:
    cat = input(
        "\n Choisesez une catégorie :\n 1.Informatique   2.Math   3.Physique \n 4.Autre          5.Fermer \n")

    if cat == '666':

        while True:
            fonct = input(
                "\n Choisesez une fonction :\n 1.Bruteforce   2.Retour   3.Fermer \n")

            if fonct == '1':
                bruteforce()

            elif fonct == '2':
                break

            elif fonct == '3':
                exit()

            else:
                print("Erreur, entrez un numéro valide !!!")

    elif cat == '1':

        while True:
            fonct = input(
                "\n Choisesez une fonction :\n 1.Générateur de mot de passe    2.Test de sécurité de mot de passe     "
                "3.gestionnaire de mot de passe \n 4.chiffrage/déchiffrage fichier        5.réseau     6.retour \n 7.Fermer \n")

            if fonct == '1':
                gen_pwd_hash()

            elif fonct == '2':
                level_pwd_security()

            elif fonct == '3':
                password_manager()

            elif fonct == '4':
                file_encrypt_decrypt()

            elif fonct == '5':
                réseau()

            elif fonct == '6':
                break

            elif fonct == '7':
                exit()

            else:
                print("Erreur, entrez un numéro valide !!!")

    elif cat == '2':

        while True:
            fonct = input("\n Choisesez une fonction :\n 1.Calcul     "
                          "2.temps/distance/vitesse     3.Convertisseur \n 4.Retour     5.Fermer \n")

            if fonct == '1':
                calcul()

            elif fonct == '2':
                temps_distance_vitesse()

            elif fonct == '3':
                convert()

            elif fonct == '4':
                break

            elif fonct == '5':
                exit()

            else:
                print("Erreur, entrez un numéro valide !!!")

    elif cat == '3':

        while True:
            fonct = input("\n Choisesez une fonction :\n 1.période/fréquence    2.Retour    3.Fermer \n")

            if fonct == '1':
                period_freq()

            elif fonct == '2':
                break

            elif fonct == '3':
                exit()

            else:
                print("Erreur, entrez un numéro valide !!!")

    elif cat == '4':

        while True:
            fonct = input("\n Choisesez une fonction :\n 1.nombre aléatoire \n 2.Retour \n 3.Fermer \n")

            if fonct == '1':
                random_num()

            elif fonct == '2':
                break

            elif fonct == '3':
                exit()

            else:
                print("Erreur, entrez un numéro valide !!!")

    elif cat == '5':
        exit()

    else:
        print("Erreur, entrez un numéro valide !!!")
