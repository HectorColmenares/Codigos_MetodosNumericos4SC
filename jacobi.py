from math import *
from pprint import pprint

def distinf(x, y):
    return max([abs(x[i] - y[i]) for i in range(len(x))])

def Jacobi(A, b, x0, TOL, MAX):
    n = len(A)
    x = [0.0 for x in range(n)]
    k = 1
    
    while k <= MAX:
            for i in range(n):
                if abs(A[i][i]) <= 1e-15:
                    print("Imposible iterar")
                    return None
                s = sum([A[i][j]*x0[j] for j in range(n) if j != i])
                x[i] = (b[i] - s)/A[i][i]
            pprint(x)
            if distinf(x, x0) < TOL:
                print(r"Solución encontrada")
                return x
            k += 1
            for i in range(n):
                x0[i] = x[i]
    print("Iteraciones agotadas")
    return None

A = [[2, 1], [5, 7]]
b = [11, 13]
x0 = [1, 1]
print("Matriz A:")
pprint(A)
print("Vector b:")
pprint(b)
print("Semilla x0:")
pprint(x0)
print("Iteración de Jacobi")
# TOL = 10−5, MAX = 50
Jacobi(A, b, x0, 1e-5, 50)









