#fonction pour mettre en majuscule
def myUpper(phrase):
    alphabet = 'abcdefghijklmnopqrstuvwxyzàâéèêëîïABCDEFGHIJKLMNOPQRSTUVWXYZAAEEEEII'
    result = ""
    for x in phrase:
        if x not in alphabet or alphabet.index(x)>=34:
            result += x
        else:
            result += alphabet[alphabet.index(x)+34]
    return result

#fonction pour mettre en minuscule
def myLower(phrase):
    alphabet = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    result = ""
    for x in phrase:
        if x not in alphabet or alphabet.index(x)<=26:  #cherche dans l'alphabet si la lettre est en majuscule
            result += x
        else:
            result += alphabet[alphabet.index(x)-26]
    return result

#fonction pour mettre une majuscule au début de chaque mot
def myTitle(phrase):
    result = ""
    mot = phrase.split()

    for i in range(len(mot)):
        carac = mot[i][0]

        titre= myUpper(carac)+mot[i][1:]
        result += titre + " "
    return result


#fonction pour enlever les espaces inutiles
def myClean(phrase):
    result = ""
    mot = phrase.split()
    for i in range(len(mot)):
        result += mot[i] + " "
    return result

texte = input("Entrez un phrase : ")
param = input("Entrez un paramètre parmis : \n-upper \n-lower \n-title \n-clean \nvotre sélection :")


while param != "upper" and param != "lower" and param != "title" and param != "clean":
    print("Paramètre invalide")
    param = input("\nEntrez un paramètre parmis : \n-upper \n-lower \n-title \n-clean \nvotre sélection :")


if param == "upper":
    print(myUpper(texte))
elif param == "lower":
    print(myLower(texte))
elif param == "title":
    print(myTitle(texte))
elif param == "clean":
    print(myClean(texte))

