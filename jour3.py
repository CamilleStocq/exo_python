#---------------------- EXO 1 ----------------------------------------
#Écris une fonction qui prend une phrase et retourne une liste de tous les mots qui commencent par une voyelle.

def start_by_vowels():
    sentence = "Bonjour je aime apprendre" 
    splited_sentence = sentence.split()
    vowels = "aeiouyAEIOU"
    vowels_start =[]

    for s in sentence:
        if s[0] in vowels:
            vowels_start.append(s)

    return vowels_start

print(start_by_vowels())



#---------------------- EXO 2 ----------------------------------------
#Écris une fonction qui prend une phrase et retourne une liste de mots en minuscules, sans ponctuation.

#---------------------- EXO 3 ----------------------------------------
#Écris une fonction qui prend une phrase et retourne le nombre total de lettres (ignore les espaces et la ponctuation).

#---------------------- EXO 4 ----------------------------------------
#Écris une fonction qui prend une phrase et retourne une liste de tous les chiffres qu’elle contient.

#---------------------- EXO 5 ----------------------------------------
#Écris une fonction qui prend une phrase et retourne une liste de tous les chiffres qu’elle contient.

#---------------------- EXO 6 ----------------------------------------
#Écris une fonction qui prend une phrase et retourne un dictionnaire avec le nombre d’occurrences de chaque mot, insensible à la casse.

#---------------------- EXO 7 ----------------------------------------
#Écris une fonction qui prend une phrase et une liste de mots à exclure, et retourne une liste de tous les mots sauf ceux à exclure, insensible à la casse.

#---------------------- EXO 8 ----------------------------------------
#Écris une fonction qui prend une phrase et retourne le mot qui apparaît le plus. Si plusieurs mots sont à égalité, retourne-les tous.

#---------------------- EXO 9 ----------------------------------------
#Écris une fonction qui prend une phrase et retourne la somme de tous les nombres présents dans la phrase.

#---------------------- EXO 10 ----------------------------------------
#Écris une fonction qui prend une phrase et retourne une nouvelle phrase où chaque mot est inversé, mais l’ordre des mots reste le même.

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