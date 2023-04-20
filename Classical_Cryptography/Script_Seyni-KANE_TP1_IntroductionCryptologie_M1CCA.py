


def EncredrerUnNombreEntre2PuissanceDe2(N):
    """Cette fonction prend en entree un entier quelquonc et retourn un entier k telque
    2^k <= N < 2^k+1"""
    k = 0
    #p = 2
    while( 2^(k)<=N):
        #p = 2^(k+1)
        k += 1
    return k -1


def fonctionTrieTableau(Tab):
    """Cette fonction prend en entree une liste donnee et retourn une copy de cette liste triee"""
    TabTrie = Tab.copy()
    for i in range(len(Tab)):
        for j in range(i+1, len(Tab)):
            if(TabTrie[i] > TabTrie[j]):
                TabTrie[i], TabTrie[j] = TabTrie[j], TabTrie[i]
    return TabTrie



def fonctionNumerotationClef(K):
    """Cette fonction prend en entree une liste a une dimension qui est la clef et routourn une
    liste a 2 dimension contenant les caractaire constituant par la clef, chacune associer a
    son ordre dans la l'alphabet"""
    #TabTrie = K.sort()
    TabTrie = fonctionTrieTableau(K.copy())
    Tab = []
    for i in range(len(K)):
        Tab.append([K[i], i])

    for i in range(len(K)):
        for j in range(len(K)):
            if(Tab[i][0] == TabTrie[j]):
                Tab[i][1] = j
    return Tab



def fonctionCompleteText(text, K):
    """Cette fonction prend en entree un text et une clef et puis retourne un text d'ont
    la taille est un multiple de la taille de la clef si ce n'est pas deja le cas"""
    tailleClef = len(K)
    tailleText = len(text)
    nombreBloc = tailleText//tailleClef

    if (tailleText%tailleClef != 0):
        rest = (nombreBloc + 1)*tailleClef - tailleText
        blocComplete = rest*'*'
        text += blocComplete
        nombreBloc = nombreBloc + 1

    return nombreBloc, text


def fonctionDecoupText(text, K):
    """Cette fonction prend en entree un text et une clef et puis retourne une liste contenant
    'k:=taille clef' bloc de longueur k"""
    textTab = []
    tailleClef = len(K)

    nombreBloc, text = fonctionCompleteText(text, K)
    for i in range(nombreBloc):
        bloc = ''
        for j in range(tailleClef):
            bloc += text[i*tailleClef + j]
        textTab.append(bloc)

    return textTab



def fonctionChiffrmentParTransposition(K):
    """Cette fonction prend en entree une clef et retourne un text chiffree selon l'algorithmique
    du chiffrement par transposition"""
    text = 'bonjourlaclasse'
    #input("Donner le text que vous voulez chiffrer :")
    textTab = fonctionDecoupText(text, K)
    clefNumTab = fonctionNumerotationClef(K)
    tailleClef = len(K)
    tailleText = len(text)
    textCrypt = ''

    for i in range(tailleClef):
        j = 0
        while(j < tailleClef and clefNumTab[j][1] != i):
            j +=1

        #textCrypt += textTab[0:][j]
        for p in range(len(textTab)):
            textCrypt += textTab[p][j]

    return textCrypt


def foctioncalculeNombreCleDeLongueurL(l,cardAlphabet):
    """Cette fonction prend en entree un 'l:=longueur cle' et 'cardAlphabet:=le cardinal d'un alphabet
    et retoune le nombre de clef possible"""
    n = cardAlphabet^l
    return n


def fonctiontionInitialisationEspceCle(l,cardAlphabet):
    """Cette fonction prend en entree une 'l:=longueur cle' et 'cardAlphabet:=le cardinal d'un alphabet'
    pour retourner une liste"""
    L = []
    for i in range(cardAlphabet):
        L.append([chr(i+97)])
    j = l
    while(j < foctioncalculeNombreCleDeLongueurL(l,cardAlphabet)):
        for i in range(cardAlphabet):
            L.append([chr(i+97)])
        j += cardAlphabet

    return L


def appendfonct(L, trs, l,n):
    """Cette fonction prend en entree une liste L le nombre de tour trs , l et 'n:=range' pour
    retourner une liste"""
    index = (trs-1)*n
    for i in range(n):
        L[index+i].append(chr(trs-1 + 97))

    return L


def fonctionGenereEspaceCle(l,cardAlphabet):
    """Cette fonction prend en entree une 'l:=longueur cle' et 'cardAlphabet:=le cardinal d'un alphabet'
    pour retourner une liste supposer etre l'espace des cles de longueur l
    cependant elle ne fonctionne pas comme voulus"""
    L = fonctiontionInitialisationEspceCle(l,cardAlphabet)

    #n = l*cardAlphabet
    j=1
    index = 0
    n = 0
    #while(j < l ):
    n = l*cardAlphabet
    while(len(L[index]) != l):
        for i in range(cardAlphabet):
            L = appendfonct(L, i+1, l,n)
        n = n//cardAlphabet
        #index += n
    return L
