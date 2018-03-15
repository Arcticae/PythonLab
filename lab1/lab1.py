import random

try:
    x=int(input("Podaj pierwsza liczbe z zakresu"))
except ValueError:
    print("Podano zły format liczby z zakresu 1")
    exit()

try:
    y=int(input("Podaj druga liczbe z zakresu"))
except ValueError:
    print("Podano zły format liczby z zakresu 2")
    exit()


if (x>y):
    print("Zle podany zakres")
    exit()
else:
    swieradint = random.randint(x,y)
    while True:
        try:
            z=int(input("Zgaduj"))
            if(z == swieradint):
                print("no pienknie")
                exit()
        except ValueError:
            print("no ale zgaduj zgodnie z zasadami obrazam sie")
            exit()