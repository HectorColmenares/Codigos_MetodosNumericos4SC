from math import *

def expo(x):
    return x**2 + exp(-2*x) - 2*x*exp(-x)

def expoprima(x):
    return 2*x - 2*exp(-2*x) - 2*exp(-x) + 2*x*exp(-x)

def trig(x):
    return cos(x) - x

def trigprima(x):
    return -sin(x) - 1

def newton(f, fprima, p0, tol, n):
    i=1
    while i <=n:
        p= p0 - f(p0)/fprima(p0)
        print("Iter = {0:<2}, p = {1:.12f}".format(i, p))
        if abs(p - p0) < tol:
            return p
        p0 = p
        i+=1
    print ("ITeraciones maximas alcanzadas.")
    return None

print("Metodo de Newton para la funcion trig(x):")
newton(trig, trigprima, pi/4, 1e-8, 100)

print("Newton función expo(x):")
newton(expo, expoprima, 4, 1e-8, 100)

        