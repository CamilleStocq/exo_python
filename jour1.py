
#---------------------- EXO 1 ----------------------------------------
#Écris une fonction qui prend une chaîne et retourne le nombre de voyelles (a, e, i, o, u, y).

def found_vowels():
    letters = "coucou ma puce"
    vowels = "a", "e", "i", "o", "u", "y"
    sum_vowels = 0
   
    for l in letters:
       if l in vowels:
           sum_vowels += 1
        
    return sum_vowels

print(found_vowels())

#---------------------- EXO 2 ----------------------------------------
#Écris une fonction qui prend une liste de nombres et retourne une nouvelle liste où les nombres pairs sont doublés, les impairs restent identiques.

def double_nummers ():
    nummers = [1,33,2,4,9,76,32]
    doubled = [] # liste vide
    for n in nummers :
        if n %2 == 0 :
            doubled.append(n * 2) # on rajoute le double dans la liste vide
        else: 
            doubled.append(n)

    return doubled

print (double_nummers())

#---------------------- EXO 3 ----------------------------------------
#Écris une fonction qui prend une chaîne HTML et retourne tout ce qui est entre <p> et </p>.
import re

def extract_p_tags(html):
    contents = re.findall(r'<p>(.*?)</p>', html)
    return contents

html_content = "<div><p>A</p><p>B</p></div>"
print(extract_p_tags(html_content))

#---------------------- EXO 4 ----------------------------------------
#Écris une fonction qui compte le nombre de voyelles dans une phrase.

def count_vowels():
    sentences = " Boujour à vous tous, j'espere que ca va " #16
    vowels = "aeiouy"
    count = 0

    for s in sentences.lower():
        if s in vowels :
            count += 1

    return count 

print (count_vowels())


#---------------------- EXO 5 ----------------------------------------
# #Écris une fonction qui compte le nombre de consonnes dans une phrase.

def count_consonnes():
    sentence = "oh c'est un chat" # 8
    vowels = "aeiouy"
    count = 0 

    for s in sentence : 
        if s not in vowels and s.isalpha() :
            count += 1
    return count

print (count_consonnes())

#---------------------- EXO 6 ----------------------------------------
# Écris une fonction qui retourne une nouvelle chaîne contenant uniquement les voyelles d’une phrase.

def found_vowels ():
    word = "ordinateur"
    vowels = "aeiouy"
    letters_found = []

    for w in word :
        if w in vowels :
            letters_found.append(w)

    return letters_found

print(found_vowels())

#---------------------- EXO 7 ----------------------------------------
#Écris une fonction qui met en majuscule toutes les lettres d’une chaîne.

def to_Upper () :
    word = "hello world"

    return word.upper()

print (to_Upper())

#---------------------- EXO 8 ----------------------------------------
#Écris une fonction qui inverse une chaîne de caractères sans utiliser de méthode Python spéciale ([::-1]).

def invert_char():
    char = "chat"
    invert_word = []

    for c in char:
        invert_word.insert(0, c)

    return invert_word

print(invert_char())

#---------------------- EXO 9 ----------------------------------------
#Écris une fonction qui compte combien de fois la lettre "a" apparaît dans une chaîne.

def found_a():
    word = "abracadabra" #5
    a_count = 0

    for w in word :
        if w == "a" :
            a_count += 1

    return a_count

print(found_a())

#---------------------- EXO 10 ----------------------------------------
#Écris une fonction qui remplace toutes les voyelles d’une phrase par *.  

def replace_vowels():
    sentence = "hello les amis je mange des pommes tous les jours" 
    vowels = "aeiouy"
    new_sentence = ""
    
    for s in sentence:
        if s in vowels:
            new_sentence += "*"
        else :
            new_sentence += s

    return new_sentence

print (replace_vowels())

#---------------------- EXO 11 ----------------------------------------
#Écris une fonction qui détecte si une chaîne contient la lettre "z" (retourne True ou False)

def found_Z():
    word = "zut gros zozo"

    for w in word :
        if w == "z":
            return True
    return False
        
print(found_Z())

#---------------------- EXO 12 ----------------------------------------
#Écris une fonction qui compte le nombre de mots dans une phrase (tu peux utiliser .split()).

def nombre_mots():
    sentence = "il y a huit mots dans ma phrase"
    
    mots = sentence.split()
    return len(mots)

print(nombre_mots())


#---------------------- EXO 13 ----------------------------------------
#Écris une fonction qui retourne une chaîne avec chaque lettre doublée.

def double_letter():
    word = "hello poulet"
    double_word = ""

    for w in word:
        double_word += w * 2

    return double_word

print (double_letter())

#---------------------- EXO RECAP ----------------------------------------
# Écris une fonction qui prend une phrase et retourne une nouvelle phrase où : Toutes les voyelles sont remplacées par *. 
# Chaque consonne qui apparaît plus d’une fois dans la phrase est doublée. Les espaces restent inchangés.

def weird_sentence():
    sentence = "voici la phrase a modifier"
    vowels = "aeiouy"
    new_sentence = ""

    for s in sentence :
        if s in vowels:
            new_sentence += "*"
        elif s.isalpha() and sentence.count(s)> 1 : 
            new_sentence += s * 2
        else : 
            new_sentence += s
            

    return new_sentence

print(weird_sentence())        