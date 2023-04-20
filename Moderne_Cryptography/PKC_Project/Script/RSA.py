import random

# L'algorithm d'Euclid simple
def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

#L'algorithm d'Euclid etandue
def EuclideEtendue(e, phi):
    d = 0
    x1 = 0
    x2 = 1
    y1 = 1
    temp_phi = phi

    while e > 0:
        temp1 = temp_phi//e
        temp2 = temp_phi - temp1 * e
        temp_phi = e
        e = temp2
        x = x2- temp1* x1
        y = d - temp1 * y1
        x2 = x1
        x1 = x
        d = y1
        y1 = y

    if temp_phi == 1:
        return d + phi


# Une fonction qui verifie si un nombre est premier
def EstPremier(num):
    if num == 2:
        return True
    if num < 2 or num % 2 == 0:
        return False
    for n in range(3, int(num**0.5)+2, 2):
        if num % n == 0:
            return False
    return True


def generationDePaireDeClefs(p, q):
    if not (EstPremier(p) and EstPremier(q)):
        raise ValueError('Tous les deux doivent etre premier.')
    elif p == q:
        raise ValueError('p et q ne doivent pas etre egales')
    #n = pq
    n = p * q

    #Phi(n)
    phi = (p-1) * (q-1)

    #On chosit un entiere telque e et phi(n) coprimier
    e = random.randrange(1, phi)

    #On utilise l'algorithm d'Euclid pour nous rassurer de generer un e copremier avec phi(n)
    g = gcd(e, phi)
    while g != 1:
        e = random.randrange(1, phi)
        g = gcd(e, phi)

    #On utilise l'algorithm d'Euclid etendue pour generer la clef privé
    d = EuclideEtendue(e, phi)

    #On retourn la paire de clef clefPub et privé
    #La clef clefPub est (e, n) et la clef privé est (d, n)
    return ((e, n), (d, n))

def encrypt(clefPub, mesg):
    clef, n = clefPub
    #On converti chaque lettre du mesg en nombre basé sur le charactaire en utilisant a^b mod m
    cipher = [(ord(char) ** clef) % n for char in mesg]
    #On retourn le tableau de bits
    return cipher

def decrypt(clefPrive, mesg):
    clef, n = clefPrive
    #On genere le mesg correspondant aux texte chiffré et de la clef privé en utilisant a^b mod m
    clair = [chr((char ** clef) % n) for char in mesg]
    #On retourn le message en claire correspondant
    return ''.join(clair)

if __name__ == '__main__':
    print ("Une proposition d'implementation complete du chiffrement RSA\n")
    #Affichage de 20 entier premiers
    print("\nVoici les 20 premiers entier premiers, pour plus de commodité.\nMerci!")
    print("\n2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71\n")
    p = int(input("Donner un nombre premier: "))
    q = int(input("Donner un second nombre premier distinct du premier nombre:"))
    print ("\nGeneration de vos paires de clefs privé et clefPub . . .")
    clefPub, clefPrive = generationDePaireDeClefs(p, q)
    print ("\nVotre clef public est {} et votre clef privé est {}\n".format(clefPub, clefPrive))
    message = input("\nEnter un message que aimerai crypté avec votre clef public : ")
    mesgCrypte = encrypt(clefPub, message)
    print ("\n\nVotremessage crypté est: {}".format(''.join(map(lambda x:str(x), mesgCrypte))))

    p = 0
    while p != 1 and p != 2:
        print("\n\nVoulez decripter le message ?")
        print("\n\n#1->OUI\n#2:NON")
        p = int(input("\n\nDonner une instruction: "))

    if(p==1):
        print ("\nDecryptage du message avec votre clef privé", clefPrive ," . . .")
        print ("\n\nVotre message est: {}\n\n".format(decrypt(clefPrive, mesgCrypte)))
    else:
        print("\nMerci d'avoir utiliser notre programme\n\nBy By a bientot!!")
