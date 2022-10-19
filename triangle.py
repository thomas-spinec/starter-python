#triangle d'une hauteur H donnée par l'utilisateur
H = int(input("Rentrez la hauteur du triangle : "))

a = 0 
for i in range(H,1, -1): #ajout de toutes les lignes du triangle sauf la base
    print(" " * i + "/" + " " * a * 2 + "\\") # double \ car un seul \ est un caractère d'échappement
    a = a +1
    print(i)

print(" /" + "__" * (H - 1) + "\\")  #ajout de la base du triangle
