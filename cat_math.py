from package import *


def calcul():
    def addition():

        list_nb = []
        result = 0

        try:
            n = int(input("Combien de nombre(s) : "))
            for i in range(n):
                nb = float(input("valeur : "))
                list_nb.append(nb)
                result = result + nb

            print(f"Result : {result}")

        except:
            print("utilisé des chiffres !")

    def soustraction():
        list_nb = []
        result = 0

        try:
            n = int(input("Combien de nombre(s) : "))
            for i in range(n):
                nb = float(input("valeur : "))
                list_nb.append(nb)
                result = result - nb

            print(f"Result : {result}")
        except:
            print("utilisé des chiffres !")

    def division():

        list_nb = []
        result = 0

        try:
            n = int(input("Combien de nombre(s) : "))
            for i in range(n):
                nb = float(input("valeur : "))
                list_nb.append(nb)
                result = result + nb

            print(f"Result : {result}")

        except:
            print("erreur ! utilisé des chiffres ! impossible de diviser par 0")

    def multiplication():
        list_nb = []
        result = 1

        try:
            n = int(input("Combien de nombre(s) : "))
            for i in range(n):
                nb = float(input("valeur : "))
                list_nb.append(nb)
                result = result * nb

            print(f"Result : {result}")

        except:
            print("utilisé des chiffres !")

    def moyenne():
        try:
            n = int(input("Combien de nombres voulez-vous entrer ? "))
            total = 0
            for i in range(n):
                try:
                    nombre = float(input(f"Entrez le nombre {i + 1}: "))
                    total += nombre

                except:
                    print("utilisé des chiffres !")

            moyenne = total / n
            print(f"La moyenne est : {moyenne}")

        except:
            print("utilisé des chiffres !")

    def pourcentage():
        try:
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

        except:
            print("utilisé des chiffres !")

    def puissance():
        try:
            num = float(input("Nombre : "))
            p = float(input("Puissance : "))
            result = num ** p
            print("Result :", result)

        except:
            print("utilisé des chiffres !")

    def factorielle():
        try:
            n = int(input("nombre : "))
            resultat = 1
            for i in range(1, n + 1):
                resultat *= i
            print(f"résultat : {resultat}")

        except:
            print("utilisé des chiffres !")

    def poly_2nd_and_complexes():
        try:
            a = float(input("Entrez la première valeur (a = ax²) : "))
            b = float(input("Entrez la deuxième valeur (b = bx) : "))
            c = float(input("Entrez la troisième valeur (c = c) : "))

            delta = b ** 2 - 4 * a * c

            if a == 0:
                x = -c / b
                print(f"La solution est x = {x:.2f}")

            else:
                if delta < 0:
                    # Calcul de nombres complexes
                    x1 = (-b + cmath.sqrt(delta)) / (2 * a)
                    x2 = (-b - cmath.sqrt(delta)) / (2 * a)
                    x1_str = str(x1).replace("j", "i")
                    x2_str = str(x2).replace("j", "i")
                    print(f"Les solutions sont :\nx1 = {x1_str}\nx2 = {x2_str}")

                elif delta > 0:
                    x1 = (-b + sqrt(delta)) / (2 * a)
                    x2 = (-b - sqrt(delta)) / (2 * a)
                    print(f"Les solutions sont :\nx1 = {x1:.2f}\nx2 = {x2:.2f}")

                else:
                    x0 = - (b / (2 * a))
                    print(f"La solution unique a pour valeur x0 = {x0:.2f}")

        except:
            print("utilisé des chiffres !")

    while True:

        operation = input(
            "\n choisissez une operation : \n 1.addition         2.soustraction    3.division \n 4.multiplication "
            "  5.moyenne         6.pourcentage \n 7.Puissance        8.factorielle     "
            "9.polynome 2nd degré et complexes \n 10.Retour          11.Fermer \n")

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
            poly_2nd_and_complexes()

        elif operation == '10':
            break

        elif operation == '11':
            exit()

        else:
            print("erreur, entrez un numéro valide !!!")


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
        while True:
            try:
                original_temp = float(input(f"Entrez la température en {original_unit} : "))
                if original_temp == float():
                    break
                else:
                    print("utilisé des chiffres !")

            except:
                print("utilisé des chiffres !")

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
        while True:
            try:
                original_time = float(input(f"Entrez la valeur du temps en {original_unit} : "))
                if original_time == float():
                    break
                else:
                    print("utilisé des chiffres !")

            except:
                print("utilisé des chiffres !")

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
        while True:
            try:
                original_dist = float(input(f"Entrez la valeur de distance en {original_unit} : "))
                if original_dist == float():
                    break
                else:
                    print("utilisé des chiffres !")

            except:
                print("utilisé des chiffres !")

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
            "\n Choisesez un convertisseur :\n 1.Température    2.Temps    3.Distance \n 4.Retour         5.Fermer \n")

        if conv == '1':
            temperature()

        elif conv == '2':
            time()

        elif conv == '3':
            distance()

        elif conv == '4':
            break

        elif conv == '5':
            exit()

        else:
            print("Erreur, entrez un numéro valide !!!")


def temps_distance_vitesse():
    def temps():
        try:
            d = float(input("Distance (m) : "))  # distance en m
            v = float(input("Vitesse (m/s) : "))  # vitesse en m/s
            t = d / v
            print(f"\n temps : {t:.2f} s"
                  f"\n temps : {t / 3600:.2f} h")

        except:
            print("utilisé des chiffres !")

    def vitesse():
        try:
            d = float(input("Distance (m) : "))  # distance en m
            t = float(input("temps (s) : "))  # temps en s
            v = d / t
            print(f"\n vitesse : {v:.2f} m/s"
                  f"\n vitesse : {v / 3600:.2f} km/h")

        except:
            print("utilisé des chiffres !")

    def distance():
        try:
            v = float(input("vitesse (m/s) : "))  # vitesse en m/s
            t = float(input("temps (s) : "))  # temps en s
            d = v * t
            print(f"\n distance : {d:.3f} m"
                  f"\n distance : {d / 1000:.2f} km")

        except:
            print("utilisé des chiffres !")

    while True:
        opt = input("\n lequels utilisé : \n 1.temps    2.vitesse    3.distance \n 4.Retour     5.fermer \n")

        if opt == '1':
            temps()

        elif opt == '2':
            vitesse()

        elif opt == '3':
            distance()

        elif opt == '4':
            break

        elif opt == '5':
            exit()

        else:
            print("nombre non valide !!!")


def random_num():
    try:
        first_num, last_num = int(input("premier nombre : ")), int(input("dernier nombre : "))
        number = random.randint(first_num, last_num)
        print(f"Nombre : {number}")

    except:
        print("utilisé des chiffres !")
