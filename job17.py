def nbpair(*args):
    myList = []
    for i in args:
        myList.append(i)
    pair = []
    for i in myList:
        if i % 2 == 0:
            pair.append(i)
    print ("les nombres pairs sont :",pair)
#appel de la fonction
nbpair(1,2,3,4,5,6,7,8,9,10)