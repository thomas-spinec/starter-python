largeur = int(input ("Entrez la largeur du rectangle : "))
hauteur = int(input ("Entrez la hauteur du rectangle : "))
for i in range(hauteur):
    if i == 0 or i == hauteur-1:
        print ("|", end="") #ce end permet de ne pas retourner à la ligne à la fin de la boucle
        for i in range(largeur-2):
            print ("-", end="")
        print ("|")
    else :
        print ("|", end="")
        for i in range(largeur-2):
            print (" ", end="")
        print ("|")
