from math import *

def test1(t, y):
    return y - t**2 + 1 
def test2(t, y):
    return 2 - exp(-4*t) - 2*y

def Euler(a, b, y0, f, N):
    h = (b - a)/N
    t = a
    w = y0
    print("t0 = {0:.2f}, w0 = {1:.12f}".format(t, w))
    for i in range(1, N+1):
        w = w + h*f(t, w)
        t = a + i*h
        print("t{0:<2} = {1:.2f}, w{0:<2} = {2:.12f}".format(i, t, w))
    
    return w

print("Método de Euler:")
Euler(0, 2, 0.5, test1, 10)

print("Método de Euler:")
Euler(0, 1, 1, test2, 20)




