def mySort(myList):
    for i in range(len(myList)):
        for j in range(i+1, len(myList)):
            if myList[i] > myList[j]:
                myList[i], myList[j] = myList[j], myList[i]  #intervertion des éléments
    print(myList)

def myDisplay(affich):
    print(affich)

tri=[56, 12, 24, 11, 8, 7, 22, 17, 27]

look=[42, 69, 5, 10, 13, 4, 7, 2, 17, 27]

mySort(tri)

myDisplay(look)