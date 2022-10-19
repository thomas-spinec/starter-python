#boucle qui n'affiche qu'un chevron jusqu'à ce qu'on indique "Au revoir"
test = input("> ")
while test != "Au revoir":
    if test == "Bonjour":
        print ("Bonjour à toi ")
        test = input("> ")
    else:
        test = input("> ")

#dès que test = Au revoir, on sort de la boucle while
#la casse est importante
exit()
