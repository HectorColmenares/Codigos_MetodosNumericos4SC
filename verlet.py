from math import *

def test1(x):
    return x
def test2(x):
    return -x

def Verlet(a, b, x0, v0, f, N):
     h = (b - a)/N
     p0 = x0
     p1 = p0 + v0*h + 0.5*f(p0)*h**2
     print("a0 = {0:0.2f}, p0 = {1:0.12f}".format(a, p0))
     for i in range(1, N+1):
         p = 2*p1 - p0 + f(p1)*h**2
         s = a + i*h
         print("a{0:<2} = {1:0.2f}, p{0:<2} = {2:.12f}".format(i, s, p1))
         p0 = p1
         p1 = p
     return p1

print("Método de Verlet:")
Verlet(0, 1, 1, 1, test1, 20)






