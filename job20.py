#variable de vérification que les entrées sont des nombres
import re
num_format = re.compile(r'^\-?[1-9][0-9]*\.?[0-9]*')
###################################################################
#définition de la fonction
def myAddition(a,b):
    return a+b

#déclaration du premier nombre
num1 = input("Entrez le premier nombre pour l'addition : ")
#vérification que l'entrée est bien un nombre
while num_format.match(num1) == False:
    num1 = input("Ce n'est pas un nombre, veuillez entrer un nombre :")
num1=int(num1)

#déclaration du deuxième nombre
num2 = input("Entrez le deuxième nombre pour l'addition : ")
#vérification que l'entrée est bien un nombre
while num_format.match(num2) == False:
    num2 = input("Ce n'est pas un nombre, veuillez entrer un nombre :")
num2=int(num2)

#appel de la fonction et affichage du résultat
result = myAddition(num1,num2)
print("le résultat est :",result)