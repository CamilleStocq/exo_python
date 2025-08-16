#---------------------- EXO 1 ----------------------------------------
#Écris une fonction qui prend une liste de nombres et retourne la somme de tous les nombres pairs.

def sum_pairs():
    numbers = [1,2,3,4,5,6,7,8,9,0] #20
    total = 0
    
    for n in numbers:
        if n% 2 == 0 :
            total += n
    return total

print (sum_pairs())

#---------------------- EXO 2 ----------------------------------------
#Écris une fonction qui prend une liste de lettres et retourne une nouvelle liste ne contenant que les voyelles (a, e, i, o, u, y).

def only_vowels():
    letters = ["a","z","e","r","t","y","u","i","o","p","q","s","d","i","i",]
    vowels = "aeiouy"
    vowels_only = []

    for l in letters :
        if l in vowels :
            vowels_only.append(l)
    return vowels_only

print (only_vowels())

#---------------------- EXO 3 ----------------------------------------
#Écris une fonction qui prend une liste de nombres et un multiplicateur, 
# et retourne une nouvelle liste avec chaque nombre multiplié par ce multiplicateur.

def multiplication ():
    numbers = [2,4,6,8,10]
    multiplicateur = 3
    calcul =[]

    for n in numbers:
        resultat = n * multiplicateur

        calcul.append(resultat)

    return calcul

print (multiplication())

#---------------------- EXO 4 ----------------------------------------
#Écris une fonction qui prend une liste et retourne une nouvelle liste sans doublons, en conservant l’ordre.

def no_double():
    letters = ["a","e","z","a","n","o","p","z"]
    sans_double = []

    for l in letters:
        if l not in sans_double :
            sans_double.append(l)
    return sans_double

print(no_double())

#---------------------- EXO 5 ----------------------------------------
#Écris une fonction qui prend une liste de caractères et retourne une nouvelle liste ne contenant que les lettres minuscules.

def only_mini():
    letters = ["A","z","R","s","q","O","P"]
    only_miniscule =[]

    for l in letters :
         if l.islower(): 
            only_miniscule.append(l)

    return only_miniscule

print(only_mini())

#---------------------- EXO 6 ----------------------------------------
#Écris une fonction qui prend une liste de nombres et retourne la somme des nombres impairs supérieurs à 10.

def sum_impairs():
    numbers = [10,29,38,47,56,65,74,8,92,0]
    total = 0

    for n in numbers:
        if n%2 == 1 and n>10:
            total += n
            
    return total

print(sum_impairs())

#---------------------- EXO 7 ----------------------------------------
#Écris une fonction qui prend une liste de mots et retourne seulement ceux qui commencent par une consonne.

def only_conson():
    words = ["avion", "Bateau", "orange", "chat", "ours"]
    vowels = "aeiouy"
    consones= []

    for w in words:
        if w[0] not in vowels:
            consones.append(w)

    return consones

print(only_conson())

#---------------------- EXO 8 ----------------------------------------
#Écris une fonction qui prend une liste de lettres et retourne une nouvelle liste où chaque lettre minuscule est doublée, les majuscules restent inchangées.

def double_mini():
    letters = ["A","z","R","s","q","o","P"]
    miniss= []

    for l in letters:
        if l.islower():
            miniss += l * 2
        else :
            miniss += l 

    return miniss

print (double_mini())

#---------------------- EXO 9 ----------------------------------------
#Écris une fonction qui prend une liste de nombres et retourne une nouvelle liste sans doublons et triée par ordre croissant.

def croissant():
    numbers = [10,92,29,38,47,56,65,29,8,92,0,2,76]
    nbr_trier = []

    for n in numbers:
        if n not in nbr_trier:
            nbr_trier.append(n)
            nbr_trier.sort()
    return nbr_trier

print(croissant())

#---------------------- EXO 10 ---------------------------------------
#Écris une fonction qui prend une liste de nombres et un diviseur, et retourne une liste avec uniquement les nombres multiples du diviseur.

def diviseur_multiples ():
    numbers = [3,4,6,8,9,10,12,13,16]
    diviseur = 3
    calcul =[]

    for n in numbers:
        if n % diviseur == 0 :
            calcul.append(n)

    return calcul

print (diviseur_multiples())

#---------------------- EXO 11 ---------------------------------------
#Écris une fonction qui prend une liste de mots et retourne le mot le plus long. Si plusieurs mots ont la même longueur maximale, retourne-les tous dans une liste.

def longest_word():
    words = ["avion", "Bateau", "orange", "chat", "ours"]
    longest = []
    max_len = 0 

    for w in words:
        if len(w) > max_len:
            max_len = len(w)
            longest = [w] 
        elif len(w) == max_len: 
            longest.append(w)

    return longest

print(longest_word())

#---------------------- EXO 12 ---------------------------------------
#Écris une fonction qui prend une liste de nombres et retourne une nouvelle liste où les nombres pairs sont doublés et les impairs sont inversés en signe.

def strange_numbers():
    numbers = [3,4,6,8,9,10,12,-13,16]
    new_numbers = []

    for n in numbers:
        if n %2 == 0 :
            new_numbers.append(n*2)
        elif n%2 == 1 :
            new_numbers.append(-n)
    return new_numbers

print (strange_numbers())

#---------------------- EXO 13 ---------------------------------------
#Écris une fonction qui prend une liste de mots et retourne une nouvelle liste :
# mots de plus de 3 lettres
# mots contenant au moins une voyelle
# mots ne commençant pas par la lettre "a".

def perfect_word():
    mots = ["papa","avion", "Bateau", "orange", "cht", "ours", "oui","o" ]
    vowels = "aeiouy"
    perfect =[]

    for m in mots:
        if len(m)>3 and m[0] != "a" or "A" and m == vowels:
            perfect.append(m)
    
    return perfect

print(perfect_word())
                

#---------------------- EXO 14 ---------------------------------------
#Écris une fonction qui prend une liste de lettres et retourne un dictionnaire avec le nombre d’occurrences de chaque lettre.

def combien_de_lettres():
    lettres = ["a","e","z","a","n","o","p","z","z","z"]
    compteur = {}

    for l in lettres:
        if l in compteur:
            compteur[l] += 1
        else:
            compteur[l] = 1

    return compteur

print(combien_de_lettres())

#---------------------- EXO 15 ---------------------------------------
#Écris une fonction qui prend une liste de listes de nombres et retourne une seule liste avec tous les nombres supérieurs à 5, triés par ordre décroissant.

def plus_que_cinq():
    listes = [[3,4,6],[8,9,10],[12,-13,16]]
    que_plus_cinq = []

    for sublist in listes:
        for n in sublist:
            if n > 5:
                que_plus_cinq.append(n)

    que_plus_cinq.sort(reverse=True)
    return que_plus_cinq

print(plus_que_cinq())

#---------------------- EXO test du niveau -------------------------
#Écris une fonction even_numbers() qui prend une liste de nombres et retourne uniquement les nombres pairs.

def even_numbers():
    numbers= [1,34,3,54,22,16,79,62]
    pair_numbers = []

    for n in numbers :
        if n % 2 == 0 :
            pair_numbers.append(n)

    return pair_numbers

print(even_numbers())

# Écris une fonction long_words() qui prend une liste de mots et retourne uniquement les mots ayant plus de 5 lettres.

def long_word() :
    words = ["chat", "éléphant", "maison", "lit", "avion"]
    long_word_list = []

    for w in words:
        if len(w) > 5 :
            long_word_list.append(w)
    return long_word_list

print(long_word())

#Écris une fonction filter_vowels() qui prend une liste de mots et retourne uniquement ceux qui commencent par une voyelle (a, e, i, o, u, y).

def filter_vowels():
    words = ["avion", "bateau", "orange", "chat", "ours"]
    vowels = "aeiouy"
    start_by_vowel = []

    for w in words :
        if w[0] in vowels:
            start_by_vowel.append(w)

    return start_by_vowel

print(filter_vowels())