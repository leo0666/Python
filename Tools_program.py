import hashlib, os, random, string, re


def calculette():
    def addition():
        num1 = float(input("Premier Nombre : "))
        num2 = float(input("Second Nombre : "))
        result = num1 + num2
        print("Result :", result)

    def soustraction():
        num1 = float(input("Premier Nombre : "))
        num2 = float(input("Second Nombre : "))
        result = num1 - num2
        print("Result :", result)

    def division():
        while True:
            num1 = float(input("Premier Nombre : "))
            num2 = float(input("Second Nombre : "))

            if num2 == 0:
                print("erreur, division par 0 impossible !!!")

            else:
                result = num1 / num2
                print("Result :", result)
                break

    def multiplication():
        num1 = float(input("Premier Nombre : "))
        num2 = float(input("Second Nombre : "))
        result = num1 * num2
        print("Result :", result)

    def moyenne():
        n = int(input("Combien de nombres voulez-vous entrer ? "))
        total = 0
        for i in range(n):
            nombre = float(input(f"Entrez le nombre {i + 1}: "))
            total += nombre
        moyenne = total / n
        print(f"La moyenne est : {moyenne}")

    def pourcentage():
        part = float(input("Valeur : "))
        total = float(input("Valeur totale : "))

        pourcentage = (part / total) * 100
        pourcentage_str = str(pourcentage)

        if '.' in pourcentage_str:
            digits_after_decimal = len(pourcentage_str.split('.')[1])
            print(f"Résultat : {round(pourcentage, digits_after_decimal)} "
                  f"({digits_after_decimal} chiffres après la virgule)")
        else:
            print(f"Résultat :{pourcentage}")

    def puissance():
        num = float(input("Nombre : "))
        p = float(input("Puissance : "))
        result = num ** p
        print("Result :", result)

    def factorielle():
        n = int(input("nombre : "))
        resultat = 1
        for i in range(1, n + 1):
            resultat *= i
        print(f"résultat : {resultat}")

    while True:

        operation = input(
            "\n choisissez une operation : \n 1.addition \n 2.soustraction \n 3.division \n 4.multiplication \n "
            "5.moyenne \n 6.pourcentage \n 7.Puissance \n 8.factorielle \n 9.Fermer \n")

        if operation == '1':
            addition()

        elif operation == '2':
            soustraction()

        elif operation == '3':
            division()

        elif operation == '4':
            multiplication()

        elif operation == '5':
            moyenne()

        elif operation == '6':
            pourcentage()

        elif operation == '7':
            puissance()

        elif operation == '8':
            factorielle()

        elif operation == '9':
            break

        else:
            print("erreur, entrez un numéro valide !!!")


def calcul_intérêt():
    capital, taux, durée = float(input("Capital : ")), float(input("Taux : ")), float(input("durée : "))
    taux = taux / 100

    interet = capital * taux * durée
    print(f"Intérêt : {interet}")


def convert():

    def temperature():
        # Demande l'unité de température d'origine
        while True:
            original_unit = input(
                "Entrez l'unité de température d'origine (C pour Celsius, F pour Fahrenheit, K pour Kelvin) : ").upper()
            if original_unit in ['C', 'F', 'K']:
                break
            else:
                print("Erreur, utilisez C, F ou K !!!")

        # Demande la température à convertir
        original_temp = float(input(f"Entrez la température en {original_unit} : "))

        # Demande l'unité de température convertie
        while True:
            converted_unit = input(
                "Entrez l'unité de température convertie (C pour Celsius, F pour Fahrenheit, K pour Kelvin) : ").upper()
            if converted_unit in ['C', 'F', 'K']:
                break
            else:
                print("Erreur, utilisez C, F ou K !!!")

        # Convertit la température
        if original_unit == 'C':
            if converted_unit == 'F':
                converted_temp = (original_temp * 1.8) + 32
            elif converted_unit == 'K':
                converted_temp = original_temp + 273.15
            else:
                converted_temp = original_temp

        elif original_unit == 'F':
            if converted_unit == 'C':
                converted_temp = (original_temp - 32) / 1.8
            elif converted_unit == 'K':
                converted_temp = (original_temp + 459.67) * 5 / 9
            else:
                converted_temp = original_temp

        else:  # original_unit == 'K'
            if converted_unit == 'C':
                converted_temp = original_temp - 273.15
            elif converted_unit == 'F':
                converted_temp = (original_temp * 9 / 5) - 459.67
            else:
                converted_temp = original_temp

        # Affiche la température convertie
        print(f"{original_temp} {original_unit} = {converted_temp} {converted_unit}")

    def time():
        # Demande l'unité de temps
        while True:
            original_unit = input(
                "Entrez l'unité de temps d'origine (S pour Seconde, M pour Minute, H pour Heure) : ").upper()
            if original_unit in ['S', 'M', 'H']:
                break
            else:
                print("Erreur, utilisez S, M ou H !!!")

        # Demande le temps à convertir
        original_time = float(input(f"Entrez la valeur du temps en {original_unit} : "))

        # Demande l'unité de temps
        while True:
            converted_unit = input(
                "Entrez l'unité de temps convertie (S pour Seconde, M pour Minute, H pour Heure) : ").upper()
            if converted_unit in ['S', 'M', 'H']:
                break
            else:
                print("Erreur, utilisez S, M ou H !!!")

        # Convertit la température
        if original_unit == 'S':
            if converted_unit == 'M':
                converted_time = original_time / 60
            elif converted_unit == 'H':
                converted_time = original_time / 3600
            else:
                converted_time = original_time

        elif original_unit == 'M':
            if converted_unit == 'S':
                converted_time = original_time * 60
            elif converted_unit == 'H':
                converted_time = original_time / 60
            else:
                converted_time = original_time

        else:  # original_unit == 'H'
            if converted_unit == 'S':
                converted_time = original_time * 3600
            elif converted_unit == 'M':
                converted_time = original_time * 60
            else:
                converted_time = original_time

        # Affiche la température convertie
        print(f"{original_time} {original_unit} = {converted_time} {converted_unit}")

    def distance():
        # Demande l'unité de distance
        while True:
            original_unit = input(
                "Entrez l'unité de distance d'origine (CM pour CentiMétre, M pour Métre, KM pour KiloMétre) : ").upper()
            if original_unit in ['CM', 'M', 'KM']:
                break
            else:
                print("Erreur, utilisez CM, M ou KM !!!")

        # Demande la distance à convertir
        original_dist = float(input(f"Entrez la valeur de distance en {original_unit} : "))

        # Demande l'unité de distance
        while True:
            converted_unit = input(
                "Entrez l'unité de temps convertie (CM pour CentiMétre, M pour Métre, KM pour KiloMétre) : ").upper()
            if converted_unit in ['CM', 'M', 'KM']:
                break
            else:
                print("Erreur, utilisez CM, M ou KM !!!")

        # Convertit la distance
        if original_unit == 'CM':
            if converted_unit == 'M':
                converted_dist = original_dist / 100
            elif converted_unit == 'KM':
                converted_dist = original_dist / 10000
            else:
                converted_dist = original_dist

        elif original_unit == 'M':
            if converted_unit == 'CM':
                converted_dist = original_dist * 100
            elif converted_unit == 'KM':
                converted_dist = original_dist / 100
            else:
                converted_dist = original_dist

        else:  # original_unit == 'KM'
            if converted_unit == 'CM':
                converted_dist = original_dist * 10000
            elif converted_unit == 'M':
                converted_dist = original_dist * 100
            else:
                converted_dist = original_dist

        # Affiche la distance convertie
        print(f"{original_dist} {original_unit} = {converted_dist} {converted_unit}")

    while True:
        conv = input(
            "\n Choisesez un convertisseur :\n 1.Température \n 2.Temps \n 3.Distance \n 4.Retour \n")

        if conv == '1':
            temperature()

        elif conv == '2':
            time()

        elif conv == '3':
            distance()

        elif conv == '4':
            break

        else:
            print("Erreur, entrez un numéro valide !!!")


def random_num():
    first_num, last_num = int(input("premier nombre : ")), int(input("dernier nombre : "))
    number = random.randint(first_num, last_num)
    print(f"Nombre : {number}")


def password_hash():
    # Initialise les listes de caractères possibles
    chars = string.ascii_uppercase + string.ascii_lowercase + string.digits + string.punctuation

    # Génère les mots de passe
    def password_generator():
        passwords = []
        for i in range(x_password):
            password = "".join(random.choice(chars) for i in range(length))
            passwords.append(password)
        return passwords

    # Hash les mots de passe générés
    def hash_passwords(passwords):
        hashed_passwords = []
        for password in passwords:
            hashed_password = hashlib.sha256(password.encode()).hexdigest()
            hashed_passwords.append(hashed_password)
        return hashed_passwords

    # Demande le nombre de mot de passe, leurs longueur du mot de passe et si l'utilisateur veut leur hash
    while True:
        hash_choice = input("Voulez-vous les hash de chaque MDP (y/n) : ")
        if hash_choice in ['y', 'n']:
            break
        else:
            print("Erreur, utilisez 'y' ou 'n' !!!")

    x_password = int(input("Nombre de MDP : "))
    length = int(input("Longueur de MDP : "))

    # Affiche les mots de passe générés et leurs hash
    passwords = password_generator()
    if hash_choice == 'y':
        hashed_passwords = hash_passwords(passwords)
        for i in range(len(passwords)):
            print(f"Mot de passe {i + 1} : {passwords[i]} - Hash : {hashed_passwords[i]}")
    else:
        for i in range(len(passwords)):
            print(f"Mot de passe {i + 1} : {passwords[i]}")


def verif_carte_credit():
    def verif(num_carte):
        # convertir le numéro de carte en une liste de chiffres
        chiffres = [int(c) for c in str(num_carte)]
        # doubler les chiffres en partant de la droite (en commençant par l'avant-dernier chiffre)
        for i in range(len(chiffres) - 2, -1, -2):
            chiffres[i] = 2 * chiffres[i]
            # si le résultat du doublement est supérieur à 9, soustraire 9
            if chiffres[i] > 9:
                chiffres[i] -= 9
        # calculer la somme de tous les chiffres
        somme_chiffres = sum(chiffres)
        # vérifier si la somme est un multiple de 10
        if somme_chiffres % 10 == 0:
            return True
        else:
            return False

    num_carte = int(input("Numéro de carte de crédit : "))
    if verif(num_carte):
        print("Le numéro de carte de crédit est valide.")
    else:
        print("Le numéro de carte de crédit est invalide.")


def password_security():
    def password_strength(password):
        # Vérifier la longueur du mot de passe
        if len(password) < 8:
            return "Faible"

        # Vérifier la présence de caractères spéciaux
        if not re.search("[@_!#$%&*()<>?/}{:]", password):
            return "Moyen"

        # Vérifier la présence de chiffres
        if not re.search("[0-9]", password):
            return "Moyen"

        # Vérifier la présence de lettres minuscules et majuscules
        if not re.search("[a-z]", password) or not re.search("[A-Z]", password):
            return "Moyen"

        # Si toutes les conditions sont remplies, le mot de passe est considéré comme fort
        return "Fort"

    print(password_strength(input("Entre ton mot de passe : ")))


def password_manager():
    # Fonction pour stocker le mot de passe dans un fichier
    def save_password(username, platform, password):
        with open('passwords.txt', 'a') as f:
            f.write(username + ',' + platform + ',' + password + '\n')

    # Fonction pour récupérer les mots de passe à partir du nom d'utilisateur et de la plateforme
    def get_passwords(username):
        passwords = []
        with open('passwords.txt', 'r') as f:
            for line in f:
                u, p, pw = line.strip().split(',')
                if u == username:
                    passwords.append((p, pw))
        if not passwords:
            print('Aucun mot de passe trouvé pour cet utilisateur!')
        return passwords

    # Code principal
    print('Bienvenue dans le gestionnaire de mots de passe!')

    while True:
        choix = input(
            'Voulez-vous enregistrer un nouveau mot de passe (1) ou récupérer des mots de passe existants (2) ? ')
        if choix == '1':
            username = input('Entrez un nom d\'utilisateur pour enregistrer ce mot de passe : ')
            platform = input(
                'Entrez la plateforme pour laquelle vous souhaitez enregistrer ce mot de passe (ex : Twitter) : ')
            password = input('Entrez le mot de passe : ')
            save_password(username, platform, password)
            print('Le mot de passe a été enregistré avec succès!')
        elif choix == '2':
            username = input('Entrez le nom d\'utilisateur pour récupérer les mots de passe : ')
            passwords = get_passwords(username)
            if passwords:
                print('Les mots de passe pour', username, 'sont :')
                for platform, password in passwords:
                    print('-', platform + ' : ' + password)
            else:
                print('Aucun mot de passe trouvé pour cet utilisateur.')
        else:
            print('Entrée invalide. Veuillez entrer 1 ou 2.')


def create_file():
    file_name = input("Nom du fichier : ")

    # Ouvre le fichier en mode écriture
    file = open(file_name, "w")

    # Écrit du texte dans le fichier
    while True:
        line = input("Entrez une ligne de texte (ou 'q' pour quitter) : ")
        if line == 'q':
            break
        file.write(line + '\n')

    # Ferme le fichier
    file.close()

    print(f"Le fichier {file_name} a été créé avec succès !")


def read_file():
    file_name = input("nom du fichier : ")
    try:
        with open(file_name, 'r') as f:
            lignes = f.readlines()
            for ligne in lignes:
                print(ligne.strip())
    except FileNotFoundError:
        print("Erreur : Le fichier n'existe pas.")


def file_encrypt_decrypt():
    basic_file, final_file, key = input("Entrez le nom du fichier à crypter ou décrypter : "), \
        input("Entrez le nom du fichier final : "), input("Entrez la clé : ")
    keys = hashlib.sha256(key.encode('utf-8')).digest()
    with open(basic_file, 'rb') as f_basic_file, open(final_file, 'wb') as f_final_file:
        i = 0
        while True:
            c = f_basic_file.read(1)
            if not c:
                break
            j = i % len(keys)
            b = bytes([c[0] ^ keys[j]])
            f_final_file.write(b)
            i += 1

    os.remove(basic_file)


while True:
    cat = input(
        "\n Choisesez une catégorie :\n 1.Math \n 2.Mot de passe \n 3.Fichier \n 4.Autre \n 5.Fermer \n")

    if cat == '1':

        while True:
            fonct = input("\n Choisesez une fonction :\n 1.Calculatrice \n 2.Convertiseur \n 3.Vérif de CB \n "
                          "4.Calculateur d'intérêt \n 5.Retour \n")

            if fonct == '1':
                calculette()

            elif fonct == '2':
                convert()

            elif fonct == '3':
                verif_carte_credit()

            elif fonct == '4':
                calcul_intérêt()

            elif fonct == '5':
                break

            else:
                print("Erreur, entrez un numéro valide !!!")

    elif cat == '2':

        while True:
            fonct = input("\n Choisesez une fonction :\n 1.Générateur de mot de passe \n "
                          "2.Test de sécurité de mot de passe \n 3.Gestionnaire de mot de passe \n 4.Retour \n")

            if fonct == '1':
                password_hash()

            elif fonct == '2':
                password_security()

            elif fonct == '3':
                password_manager()

            elif fonct == '4':
                break

            else:
                print("Erreur, entrez un numéro valide !!!")

    elif cat == '3':

        while True:
            fonct = input("\n Choisesez une fonction :\n 1.créer un fichier \n 2.lire un fichier \n "
                          "3.chiffrer/déchiffrer un fichier \n 4.Retour \n")

            if fonct == '1':
                create_file()

            elif fonct == '2':
                read_file()

            elif fonct == '3':
                file_encrypt_decrypt()

            elif fonct == '4':
                break

            else:
                print("Erreur, entrez un numéro valide !!!")

    elif cat == '4':

        while True:
            fonct = input("\n Choisesez une fonction :\n 1.nombre aléatoire \n 2.Retour \n")

            if fonct == '1':
                random_num()

            elif fonct == '2':
                break

            else:
                print("Erreur, entrez un numéro valide !!!")

    elif cat == '5':
        exit()

    else:
        print("Erreur, entrez un numéro valide !!!")
