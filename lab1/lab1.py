import random

try:
    x=(int)(input("Podaj pierwsza liczbe z zakresu"))
except ValueError:
    print("Podano zły format liczby z zakresu 1")


try:
    y=(int)(input("Podaj druga liczbe z zakresu"))
except ValueError:
    print("Podano zły format liczby z zakresu 2")

swieradint=random.randint(x,y)

while True:
    try:
        z=(int)(input("Zgaduj dalyj"))
        if (z == swieradint):
            print("no pienknie")
            break
    except ValueError:
        print("no ale zgaduj zgodnie z zasadami")