#affiche "Fizz" si le nombre est un multiple de 3, Buzz si c'est un multiple de 5 et FizzBuzz si c'est un multiple des 2
for i in range(1,101):
    if i % 3 == 0 and i % 5 == 0:
        print ("FizzBuzz")
    elif i % 3 == 0:
        print ("Fizz")
    elif i % 5 == 0:
        print ("Buzz")
    else:
        print (i)

