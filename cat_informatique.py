from package import *


def gen_pwd_hash():
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

    while True:
        try:
            x_password = int(input("Nombre de MDP : "))
            length = int(input("Longueur de MDP : "))
            break

        except:
            print("utilisé des chiffres !")

    # Affiche les mots de passe générés et leurs hash
    passwords = password_generator()
    if hash_choice == 'y':
        hashed_passwords = hash_passwords(passwords)
        for i in range(len(passwords)):
            print(f"Mot de passe {i + 1} : {passwords[i]} - Hash (sha256) : {hashed_passwords[i]}")
    else:
        for i in range(len(passwords)):
            print(f"Mot de passe {i + 1} : {passwords[i]}")


def level_pwd_security():
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


def bruteforce():
    # Génère des mots de passe et les compare au mot de passe donné
    def bruteforce_program(password):
        chars = string.ascii_uppercase + string.ascii_lowercase + string.digits + string.punctuation
        attempts = 0
        for password_length in range(1, len(password) + 1):
            for guess in itertools.product(chars, repeat=password_length):
                attempts += 1
                guess = ''.join(guess)
                print(guess, " : ", attempts)
                if guess == password:
                    return guess, attempts

    # Hashe le mot de passe correspondant à celui qui doit être trouvé
    def hash_password(password):
        hashed_password = hashlib.sha256(password.encode()).hexdigest()
        return hashed_password

    # Demande le mot de passe qui doit être trouvé
    password = input("Entrez le mot de passe à deviner : ")

    while True:
        hash_choice = input("Voulez-vous le hash du MDP (y/n) : ")
        if hash_choice in ['y', 'n']:
            break
        else:
            print("Erreur, utilisez 'y' ou 'n' !!!")

    # Mesure le temps d'exécution du bruteforce
    start_time = time.time()
    guess, attempts = bruteforce_program(password)
    end_time = time.time()

    # Affiche le mot de passe et son hash
    if hash_choice == 'y':
        hashed_password = hash_password(guess)
        print(f"Mot de passe : {guess} - Hash (sha256) : {hashed_password}")
        print(f"Nombre d'essais : {attempts}")
        print(f"Temps : {end_time - start_time} s")

    # Affiche le mot de passe
    else:
        print(f"Mot de passe : {guess}")
        print(f"Nombre d'essais : {attempts}")
        print(f"Temps : {end_time - start_time} s")


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
            '\n 1.enregistrer un nouveau mot de passe    2.récupérer des mots de passe existants ?    3.Retour \n ')

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

        elif choix == '3':
            break

        else:
            print('erreur ! entrez un chiffre valide !!')


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


def réseau():
    def informations_reseau():
        def convert_ip_bin(ip):
            return ''.join(format((int(x)), '08b') for x in ip.split('.'))

        def info_reseau(ip):
            sep = ip.split('/')
            ip_, mask = sep[0], int(sep[1])
            ip_bin = convert_ip_bin(ip_)

            ip_reseau_bin = ip_bin[:mask] + '0' * (32 - mask)
            broadcast_bin = ip_bin[:mask] + '1' * (32 - mask)
            mask_bin = ('1' * int(mask)) + ('0' * (32 - int(mask)))

            ip_reseau_dec = '.'.join([str(int(ip_reseau_bin[i:i + 8], 2)) for i in range(0, 32, 8)])
            broadcast_dec = '.'.join([str(int(broadcast_bin[i:i + 8], 2)) for i in range(0, 32, 8)])
            mask_ = '.'.join([str(int(mask_bin[i:i + 8], 2)) for i in range(0, 32, 8)])

            first_ip = ip_reseau_dec[:-1] + str(int(ip_reseau_dec[-1]) + 1)
            last_ip = broadcast_dec[:-1] + str(int(broadcast_dec[-1]) - 1)

            return ip_reseau_dec, broadcast_dec, mask_, first_ip, last_ip

        while True:
            ip = input("Entrez une IP (192.168.1.1/24) : ")
            ip_test = ip.split('/')
            if ip_test[1] >= '32':
                print("Le CIDR doit être inférieure ou égal à 31")

            else:
                break

        ip_reseau, broadcast, mask, first_ip, last_ip = info_reseau(ip)

        print(
            f"IP réseau : {ip_reseau}\nMasque : {mask}\nBroadcast : {broadcast}\nplage d'adresse : {first_ip} - {last_ip}")

    while True:
        fonct = input("\n Choisesez une fonction :\n 1.info réseau    2.Retour    3.Fermer \n")

        if fonct == '1':
            informations_reseau()

        elif fonct == '2':
            break

        elif fonct == '3':
            exit()

        else:
            print("Erreur, entrez un numéro valide !!!")
