#---------------------- EXO 1 ----------------------------------------
#Écris une fonction qui prend une phrase et retourne un dictionnaire avec le nombre d’occurrences de chaque mot, insensible à la casse.

def repetition():
    mots = "Chat chien chat oiseau"

    mots = mots.lower()
    mots = mots.split()

    recurrence = {}

    for m in mots:
        if m in recurrence:
            recurrence[m] += 1
        else :
            recurrence[m] = 1

    return recurrence

print(repetition())
            

#---------------------- EXO 2 ----------------------------------------
#Écris une fonction qui prend une liste de nombres et retourne une nouvelle liste avec uniquement les nombres pairs, mais multipliés par 2

def nbr_paire():
    nombres = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0] 
    paires =[]

    for n in nombres:
        if n% 2 == 0 :
            paires.append(n*2)
    return paires

print (nbr_paire())

#---------------------- EXO 3 ----------------------------------------
#Écris une fonction qui prend une liste et retourne :
#le plus petit élément
#le plus grand élément
#et la moyenne de tous les éléments.

def elements():
    numbers = [5, 10, 3, 8] 
    petit = numbers[0]
    grand = numbers[0]
    somme = 0


    for n in numbers:
        if n < petit :
            petit = n
        if n > grand :
            grand = n
        
        somme += n

    moyenne = somme /len(numbers)

    return [petit, grand, moyenne]


print(elements())

#---------------------- EXO final level hard ---------------------------
#Écris une fonction qui prend une phrase et retourne un dictionnaire avec :
#le mot le plus long,
#le mot le plus court,
#le nombre total de mots,
#la moyenne de la longueur des mots.

def mots_math():
    phrase = "Je fais beaucoup d'exercices aujourd'hui"
   
    phrase = phrase.lower()
    phrase = phrase.split()
   
    max_len = 0
    min_len = len(phrase[0])  # longueur du 1er mot
    longest = phrase[0]
    shortest = phrase[0]
    compteur = 0

    for p in phrase:
        compteur += len(p)

        if len(p) > max_len:
            max_len = len(p)
            longest = p

        if len(p) < min_len:
            min_len = len(p)
            shortest = p

    total_mots = len(phrase)
    moyenne = compteur / total_mots

    return {
        "mot_plus_long": longest,
        "mot_plus_court": shortest,
        "total_mots": total_mots,
        "moyenne_longueur": round(moyenne, 2)
    }

print(mots_math())
        


print(mots_math())

# #---------------------- EXO test du niveau ---------------------------
# #Écris un algorithme qui prend une liste de nombres et retourne le minimum sans utiliser min()

# def plus_petit():
#     liste = [8, 3, 10, 1, 6]
#     petit = liste[0]

#     for l in liste:
#         if l < petit :
#             petit = l

#     return petit

# print(plus_petit())

# #Écris un algorithme qui prend une liste de nombres et retourne les deux plus grands nombres de la liste (dans l’ordre décroissant).

# def plus_grand():
#     list = [5, 9, 1, 7, 3]
#     grand = list[0]
#     grand2 = list[0]

#     for l in list:
#         if l > grand:
#             grand2 = grand
#             grand = l
#         elif l > grand2 and l != grand:
#             grand2 = l

#     return [grand, grand2]

# print(plus_grand())

# #Écris un algorithme qui détermine si une liste est un palindrome

# def palindrome():
#     numbers = [4, 5, 6, 7, 3]

#     n = len(numbers)
    
#     for i in range(n // 2):  
#         if numbers[i] != numbers[n - 1 - i]:
#             return False  
#     return True 

        
# print(palindrome())