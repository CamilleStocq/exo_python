#---------------------- EXO 1 ----------------------------------------
#

#---------------------- EXO 2 ----------------------------------------
#

#---------------------- EXO 3 ----------------------------------------
#

#---------------------- EXO 4 ----------------------------------------
#

#---------------------- EXO 5 ----------------------------------------
#

#---------------------- EXO 6 ----------------------------------------
#

#---------------------- EXO 7 ----------------------------------------
#

#---------------------- EXO 8 ----------------------------------------
#

#---------------------- EXO 9 ----------------------------------------
#

#---------------------- EXO 10 ---------------------------------------
#

#---------------------- EXO 11 ---------------------------------------
#

#---------------------- EXO 12 ---------------------------------------
#

#---------------------- EXO 13 ---------------------------------------
#

#---------------------- EXO 14 ---------------------------------------
#

#---------------------- EXO 15 ---------------------------------------
#

#---------------------- EXO test du niveau ---------------------------
#Écris un algorithme qui prend une liste de nombres et retourne le minimum sans utiliser min()

def plus_petit():
    liste = [8, 3, 10, 1, 6]
    petit = liste[0]

    for l in liste:
        if l < petit :
            petit = l

    return petit

print(plus_petit())

#Écris un algorithme qui prend une liste de nombres et retourne les deux plus grands nombres de la liste (dans l’ordre décroissant).

def plus_grand():
    list = [5, 9, 1, 7, 3]
    grand = list[0]
    grand2 = list[0]

    for l in list:
        if l > grand:
            grand2 = grand
            grand = l
        elif l > grand2 and l != grand:
            grand2 = l

    return [grand, grand2]

print(plus_grand())

#Écris un algorithme qui détermine si une liste est un palindrome

def palindrome():
    numbers = [4, 5, 6, 7, 3]

    n = len(numbers)
    
    for i in range(n // 2):  
        if numbers[i] != numbers[n - 1 - i]:
            return False  
    return True 

        
print(palindrome())