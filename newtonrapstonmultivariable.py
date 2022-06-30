import numpy as np

def f(x):
    res = np.cos(x)-4*x**2
    return res
 
def dfdx(x):
    res = -np.sin(x)-6*x
    return res
# Newton-Raphson 
# maximo de iteraciones
max_iter = 20  
# Tolerancia
tol = 1E-15  
i = 0 
# ajuste inicial 
x0 = 1  
xi_1 = x0
print("Iteracion " + str(i) + ": x = " + str(x0) + ", f(x) = " + str(f(x0)))
# Iterando hasta que se alcance la tolerancia o las iteraciones máximas
while abs(f(xi_1)) > tol or i > max_iter:
    i = i + 1
    # Newton-Raphson (ecuacion)
    xi = xi_1-f(xi_1)/dfdx(xi_1)  
    print("Iteracion " + str(i) + ": x = " + str(xi) + ", f(x) = <" + str(f(xi)))
    xi_1 = xi

