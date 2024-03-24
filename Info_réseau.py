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

print(f"IP réseau : {ip_reseau}\nMasque : {mask}\nBroadcast : {broadcast}\nplage d'adresse : {first_ip} - {last_ip}")