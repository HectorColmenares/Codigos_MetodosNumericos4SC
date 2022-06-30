from math import *

def RectaMinSq(datos):
    X = sum([p[0] for p in datos])
    Y = sum([p[1] for p in datos])
    XX = sum([(p[0])**2 for p in datos])
    XY = sum([p[0]*p[1] for p in datos])
    m = len(datos)

    def P(x):
         a0 = (Y*XX - X*XY)/(m*XX - X**2)
         a1 = (m*XY - X*Y)/(m*XX - X**2)
         return a0 + a1*x
    return P

def ErrorSq(f, datos):
    E = sum([(p[1] - f(p[0]))**2 for p in datos])
    return E


datos = [(-1, 2), (0, -1), (1, 1), (2, -2)]
f = RectaMinSq(datos)
print("Recta de ajuste. Evaluar en x = 1:")
print("{0:.10f}".format(f(1.0)))

datos = [(1.0, 1.3), (2.0, 3.5), (3.0, 4.2), (4.0, 5.0), (5.0, 7.0),
        (6.0, 8.8), (7.0, 10.1), (8.0, 12.5), (9.0, 13.0)]
f = RectaMinSq(datos)
print("Recta de ajuste. Evaluar en x = 1:")
print("{0:.10f}".format(f(1.0)))
