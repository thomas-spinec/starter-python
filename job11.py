# ouverture du fichier
fichier = open("/home/thomas/Documents/La_plateforme/git/starter-python/domains.xml", "r") #en mode lecture
texte = fichier.readlines()

#déclaration de la variable de comptage
count = 0

#boucle pour compter le nombre de fois que "domain"
for i in texte:
    if i.find("domain") != -1: #-1 car find renvoie -1 si la chaine n'est pas trouvée
        count += 1

print ("Il y a", count, "domaines dans le fichier")

#fermeture du fichier
fichier.close()


###################################################################
# méthode avec count
###################################################################
# with open("c:/Users/sarhi/Desktop/la plateforme/python/domains.xml") as f: #ouverture du fichier domains.xml en mode lecture seule
#     contents = f.read() # lecture du contenu du fichier à l’aide de la fonction read() et stockage dans une variable contents
#     count = contents.count("domain") # utilisation de la fonction count pour trouver l'occurence du mot "domain"
#     print (count) # affichage du compte
#     f.close() #fermeture de fichier f