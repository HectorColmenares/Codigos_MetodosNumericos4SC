from math import *
import re

def Lagrange(datos):
    
    def L(k, x):
        """Implementa funciones   L_k(x)"""
        out = 1
        for i, p in enumerate (datos):
            if i!= k:
                out *= (x - p[0])/(datos[k][0] - p[0])
        return out
    
    def P(x):
        """Se implementa un polinomio P(x)"""
        lag = 0 
        for k, p in enumerate (datos):
            lag += p[1]*L(k, x)
        return lag 
    return P

datosf = [(2, 1/2), (11/4, 4/11), (4, 1/4)]
Pf = Lagrange(datosf)
print("Polinomio de Lagrange en x = 3:")
print("{0:.12f}".format(Pf(3)))

# datos g(x) = sin(3x), x0 = 1, x1 = 1.3, x2 = 1.6, x3 = 1.9 y x4 = 2.2
datosg = [(1, 0.1411), (1.3, -0.6878), (1.6, -0.9962),
(1.9, -0.5507), (2.2, 0.3115)]
Pg = Lagrange(datosg)

print("Polinomio de Lagrange en x = 1.5:")
print("{0:.12f}".format(Pg(1.5)))