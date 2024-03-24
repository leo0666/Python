def period_freq():
    def period():

        unit = input("Unité : 1.Hz 2.KHz 3.MHz\n")

        if unit == '1':
            try:
                f = float(input("entre la frequence en Hz : "))

                result = 1 / f

                print(f"la période est {result:.2f} s")

            except:
                print("utilisé des chiffres !")

        elif unit == '2':
            try:
                f = float(input("entre la frequence en KHz : "))

                result = 1 / (f * 1000)

                print(f"la période est {result:.2f} s")

            except:
                print("utilisé des chiffres !")

        elif unit == '3':
            try:
                f = float(input("entre la frequence en MHz : "))

                result = 1 / (f * 1000000)

                print(f"la période est {result:.2f} s")

            except:
                print("utilisé des chiffres !")

        else:
            print("Erreur ! utilisé des chiffres valides !!")

    def freq():

        unit = input("Unité : 1.µs 2.ms 3.s\n")

        if unit == '1':
            try:
                T = float(input("entre la période en µs : "))

                result = 1 / (T * (10 ** (- 6)))

                print(f"la fréquence est {result:.2f} Hz")

            except:
                print("utilisé des chiffres !")

        elif unit == '2':
            try:
                T = float(input("entre la période en ms : "))

                result = 1 / (T * (10 ** (- 3)))

                print(f"la fréquence est {result:.2f} Hz")

            except:
                print("utilisé des chiffres !")

        elif unit == '3':
            try:
                T = float(input("entre la période en s : "))

                result = 1 / T

                print(f"la fréquence est {result:.2f} Hz")

            except:
                print("utilisé des chiffres !")

        else:
            print("Erreur ! utilisé des chiffres valides !!")

    while True:
        fonct = input("\n Choisesez une fonction :\n 1.fréquence    2.période    3.Retour \n 4.Fermer \n")

        if fonct == '1':
            freq()

        elif fonct == '2':
            period()

        elif fonct == '3':
            break

        elif fonct == '4':
            exit()

        else:
            print("Erreur, entrez un numéro valide !!!")
