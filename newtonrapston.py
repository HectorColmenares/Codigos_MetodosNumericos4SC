import numpy as np



t = []
tr = abs(2*max)
x0 = 2
xi = x0
max= 0.001

F= lambda x: x**6 + 12*(x**2) - 10
f= lambda x: 6*(x**5) + 24*x


while (tr >= max):
    x = xi - F(xi)/f(xi)
    tr = abs(x-xi)
    t.append([xi,x,tr])
    xi = x
    

tabla = np.array(t)
n = len(tabla)


np.set_printoptions(precision = 4)
print(tabla)
print('raiz en: ', xi)
print('con error de: ',tr)
