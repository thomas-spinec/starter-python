#déclaration par l'utilisateur de la longueur du mot recherché
longueur = int(input("Entrez la longueur du mot recherché : "))

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