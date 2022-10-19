#demander à l'utilisateur d'écrire du texte qui sera enregistré dans un fichier
texte = input("Entrez votre texte : ")

###  ouvrir (crée si besoin) le fichier output.txt
#fichier = open("output.txt", "w") #w = write, crée le fichier s'il n'existe pas, écrase le contenu s'il existe

fichier = open("output.txt", "a") #a = append, crée le fichier s'il n'existe pas, ajoute le contenu à la fin s'il existe

###  écrire le texte dans le fichier
fichier.write(texte)
fichier.write("\n") # ajout d'un retour à la ligne

### afficher le contenue du fichier dans le terminal
fichier = open("output.txt", "r") #r = read, ouvre le fichier en lecture
print (fichier.read())

###  fermer le fichier
fichier.close()
