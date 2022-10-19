#ouverture du fichier
fichier = open("/home/thomas/Documents/La_plateforme/git/starter-python/data.txt", "r") #en mode lecture
texte = fichier.read()

#déclaration de la variable de comptage
# nbspe = 0   # nombre de mot avec caractère spécial

#séparation de chaque mot
mot = texte.split()
#comptage du nombre de mot totaux
tot = len(mot)
print ("Il y a", tot, "mots dans le fichier")

# boucle pour compter le nombre de mots avec caractère spécial
# for ligne in texte:
#     #liste des caractères spéciaux
#     caractereSpeciaux = ['.', '^', '$', '*', '+', '?', '{', '}', '[', ']', '\\', '|', '(', ')']
    
#     #comptage du nombre de mot avec caractère spécial
#     for i in range(len(caractereSpeciaux)):
#         if ligne.find(caractereSpeciaux[i]) != -1:
#             nbspe += 1
fichier.close()

#comptage du nombre de mot sans caractère spécial
# nbmot = tot - nbspe

# print ("Il y a", nbmot, "mots sans caractères spéciaux dans le fichier")

# la partie commentée n'est pas nécessaire (du moins je pense)