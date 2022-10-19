def croissant(*args):
    myList = []
    for i in args:
        myList.append(i)
    myList.sort()
    print(myList)

croissant(9, 24, 5, 12, 11, 8, 7, 22, 17, 27)
