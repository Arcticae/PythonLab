#równanie kwadratowe

def quadratic_solve(a,b,c):

    delta=(b*b)-4*(a*c)
    if(delta==0):
        sol= -b/(2*a)
        print("there is one Solution :",sol)
        exit()
    elif(delta<0):
        print("there are no solutions! goodbye")
        exit()
    elif(delta>0):
        sol1=(-b-delta)/(2*a)
        sol2=(-b+delta)/(2*a)
        print("Solution 1 is :",sol1)
        print("Solution 2 is :",sol2)
        exit()


try:
    a=int(input("Podaj a rownania"))
except ValueError:
    print("Podano zły format liczby ")
    exit()
try:
    b=int(input("Podaj b rownania"))
except ValueError:
    print("Podano zły format liczby ")
    exit()
try:
    c=int(input("Podaj c rownania"))
except ValueError:
    print("Podano zły format liczby ")
    exit()

quadratic_solve(a,b,c)