#déclaration par l'utilisateur de la longueur du mot recherché
from curses.ascii import isdigit


longueur = input("Entrez la longueur du mot recherché : ")

#vérification que ce soit un nombre
while longueur.isdigit() == False:
    longueur = input("Ce n'est pas un nombre, veuillez entrer un nombre :")
longueur = int(longueur)

#ouverture du fichier
fichier = open("/home/thomas/Documents/La_plateforme/git/starter-python/data.txt", "r") #en mode lecture
texte = fichier.read()

list = texte.split()

#déclaration et initialisation de la variable de comptage
mot = 0

for i in range(len(list)):
    if len(list[i]) == longueur:
        mot += 1
#fermeture du fichier
fichier.close()

print ("il y a", mot, "mots de", longueur, "lettres dans le fichier")