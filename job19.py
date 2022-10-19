# def croissant(*args):
#     myList = []
#     for i in args:
#         myList.append(i)

#     for n in range(len(myList)):
#         #variable de décision
#         D = myList[n]
#         j=n-1
#         while j>=0 and myList[j]>D:
#             myList[j+1] = myList[j]  #on décale les éléments
#             j-=1
#         myList[j+1] = D
#     print(myList)

# croissant(9, 24, 5, 12, 11, 8, 7, 22, 17, 27)

################################################
# autre méthode
###############################################
def croissant(*args):
    myList = []
    for i in args:
        myList.append(i)

    for i in range(len(myList)):
        for j in range(i+1, len(myList)):
            if myList[i] > myList[j]:
                myList[i], myList[j] = myList[j], myList[i]  #intervertion des éléments
    print(myList)

croissant(9, 24, 5, 12, 11, 8, 7, 22, 17, 27)