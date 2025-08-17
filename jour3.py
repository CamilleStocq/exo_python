# import re

# #---------------------- EXO 1 ----------------------------------------
# #Écris une fonction qui prend une phrase et retourne une liste de tous les mots qui commencent par une voyelle.

# def start_by_vowels():
#     sentence = "Bonjour j' aime apprendre" 
#     splited_sentence = sentence.split()
#     vowels = "aeiouyAEIOU"
#     vowels_start =[]

#     for s in splited_sentence:
#         if s[0] in vowels:
#             vowels_start.append(s)

#     return vowels_start

# print(start_by_vowels())



# #---------------------- EXO 2 ----------------------------------------
# #Écris une fonction qui prend une phrase et retourne une liste de mots en minuscules, sans ponctuation.

# def tout_petit():
#     phrase = "Bonjour, je Suis Camille!"

#     phrase = phrase.lower()
#     phrase = re.sub(r"[^\w\s]", "", phrase)
#     mots = phrase.split()
    
#     return mots

# print(tout_petit())

# #---------------------- EXO 3 ----------------------------------------
# #Écris une fonction qui prend une phrase et retourne le nombre total de lettres (ignore les espaces et la ponctuation).

# def nombre_lettres():
#     phrase = "Bonjour, je Suis Camille!"
#     compteur = 0

#     phrase = phrase.lower()
#     phrase = re.sub(r"[^\w\s]", "", phrase)

#     mots = phrase.split()

#     for m in mots :
#         compteur += len(m)

#     return compteur

# print(nombre_lettres())

# #---------------------- EXO 4 ----------------------------------------
# #Écris une fonction qui prend une phrase et retourne une liste de tous les chiffres qu’elle contient.

# def sort_chiffres():

#     sentence = "J’ai 2 chats et 5 poissons"
#     chiffre_phrase = []
#     sentence = sentence.split()

#     for s in sentence :
#         if s.isdigit():
#             chiffre_phrase.append(s)
#     return chiffre_phrase

# print(sort_chiffres())

# #---------------------- EXO 5 ----------------------------------------
# #Écris une fonction qui prend une phrase et retourne une liste des mots de plus de 4 lettres.

# def more_than_four():
#     sentence = "Je mange une orange délicieuse"
#     sentence = sentence.lower()
#     word = sentence.split()

#     four_of_more = []

#     for w in word:
#         if len(w) > 4: 
#             four_of_more.append(w)

#     return four_of_more

# print(more_than_four())

#---------------------- EXO 6 ----------------------------------------
#Écris une fonction qui prend une phrase et retourne un dictionnaire avec le nombre d’occurrences de chaque mot, insensible à la casse.

def recurrence_mot():
    mots = "Chat chat Chien"
    recurrence = {}

    mots = mots.lower()
    mots = mots.split()

    for m in mots:
        if m in recurrence:
            recurrence[m] += 1

        else :
            recurrence[m] = 1
    return recurrence

print(recurrence_mot())

#---------------------- EXO 7 ----------------------------------------
#Écris une fonction qui prend une phrase et une liste de mots à exclure, et retourne une liste de tous les mots sauf ceux à exclure, insensible à la casse.

def exclure_mot():
    phrase = "Je mange une pomme et un citron"
    exclude = ["une", "et"]
    new_thing = []

    phrase = phrase.lower()
    phrase = phrase.split()

    for p in phrase:
        if p not in exclude:
            new_thing.append(p)
    return new_thing

print(exclure_mot())

#---------------------- EXO 8 ----------------------------------------
#Écris une fonction qui prend une phrase et retourne le mot qui apparaît le plus. Si plusieurs mots sont à égalité, retourne-les tous.

def plus_apparu():
    mots = "chat chien chat oiseau chien chat"
    mots = mots.split()
    compteur = {}

    for m in mots:
        if m in compteur:
            compteur[m] += 1
        else:
            compteur[m] = 1

    max_rep = max(compteur.values())
    more = [mot for mot, nb in compteur.items() if nb == max_rep]

    return more

print(plus_apparu())

#---------------------- EXO 9 ----------------------------------------
#Écris une fonction qui prend une phrase et retourne la somme de tous les nombres présents dans la phrase.

def sum_sentence():
    sentence = "J’ai 2 chats et 5 poissons"
    words = sentence.split()
    total = 0

    for w in words:
        if w.isdigit():
            total += int(w)
    return total

print (sum_sentence())

#---------------------- EXO 10 ----------------------------------------
#Écris une fonction qui prend une phrase et retourne une nouvelle phrase où chaque mot est inversé, mais l’ordre des mots reste le même.

def inversed_sentence():
    sentence = "Bonjour je cours"
    sentence = sentence.lower()
    mots = sentence.split()

    invert_words = []
    for mot in mots:
        mot_inverse = mot[::-1]  
        invert_words.append(mot_inverse)

    result = " ".join(invert_words)

    return result

print(inversed_sentence())

#---------------------- EXO 11 ----------------------------------------
#Écris une fonction qui prend une phrase et retourne un dictionnaire où chaque mot est associé à sa longueur, insensible à la casse et sans doublons.

#---------------------- EXO 12 ----------------------------------------
#Écris une fonction qui prend une phrase et retourne une liste de tous les mots palindromes (mots qui se lisent de la même façon à l’endroit et à l’envers), insensible à la casse.

#---------------------- EXO 13 ----------------------------------------
#Écris une fonction qui prend une phrase et retourne un dictionnaire avec, pour chaque mot, le nombre d’occurrences de chaque lettre.

#---------------------- EXO 14 ----------------------------------------
#Écris une fonction qui prend une phrase et retourne tous les nombres (entiers et décimaux) présents dans la phrase sous forme de liste de floats.

#---------------------- EXO 15 ----------------------------------------
#Écris une fonction qui prend une phrase, supprime toute ponctuation, convertit tout en minuscules, et retourne une liste de mots propres.

# #---------------------- EXO test du niveau -------------------------
# #Écris une fonction qui prend une phrase en entrée et retourne une liste de tous les mots séparés par des espaces.

# def sentence_to_list():
#     sentence = "Bonjour je m’appelle Camille"
#     list_words = sentence.split()
#     return list_words

# print(sentence_to_list())

# #Écris une fonction qui prend une chaîne et retourne le nombre de chiffres qu’elle contient.

# def found_numbers():
#     sentence = "Je cours 4 fois par semaine et j’ai 2 chats"
#     numbers_found = 0

#     for s in sentence:
#         if s.isdigit():  # Vérifie si le caractère est un chiffre
#             numbers_found += 1
#     return numbers_found

# print(found_numbers())

# #Écris une fonction qui prend une chaîne et retourne un dictionnaire avec le nombre d’occurrences de chaque mot (insensible à la casse).


# def dico_repetitions():
#     words = "Chat,chien,chat,CHAT,oiseau,chien"
#     listWords = words.split(",")
#     recurrence = {}

#     for w in listWords:
#         w_lower = w.lower()
#         if w_lower in recurrence:
#             recurrence[w_lower] += 1
#         else:
#             recurrence[w_lower] = 1
#     return recurrence

# print(dico_repetitions())