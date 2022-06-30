from math import *
def pol(x):
     return x**3 + 4*x**2 - 10
 
def trig(x):
    return x*cos(x-1) - sin(x)

def bisec(f,a,b,tol,n):
    i=1
    while i <= n:
        p = a + (b-a)/2
        print("i = {0:<2}, p = {1:.12f}".format(i, p))
        if abs(f(p)) <= 1e-15 or (b - a)/2 < tol:
            return p
        i +=1
        if f(a)*f(p) >0:
            a = p
        else:
            b = p
    print("Iteraciones agotadas")
    return None
    
print("biseccion funcion pol(x)")
bisec (pol, 1, 2, 1e-8, 100)
print("Biseccion funcion trig(x)")
bisec (trig, 4, 6, 1e-8, 100)
