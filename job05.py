#déclaration de l'interval
a = int(input("entrez la première valeur de l'interval : "))
b = int(input("entrez la deuxième valeur de l'interval : "))

#conditions pour vérifier que l'interval soit valide
if a < b:
    for i in range(a+1,b): #boucle avec incrémentation affichant les nombres inclus dans l'interval
        print (i)
elif a > b:
    for i in range(a-1,b,-1): #boucle avec décrémentation affichant les nombres inclus dans l'interval
        print (i)
else:
    print ("Valeurs égales")

