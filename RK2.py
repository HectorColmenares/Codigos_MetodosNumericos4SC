from math import *

def dydx(x, y) :
   return (x + y - 2);
 

def rungeKutta(x0, y0, x, h) :
 
    # Cuenta el numero de iteraciones
    # usando el ancho o largo
    n = round((x - x0) / h);
     
        # iteracion del numero de iteraciones
    y = y0;
     
    for i in range(1, n + 1) :
         
        #Aplicando RK2
        # para encontrar el valor de la siguiente y
        k1 = h * dydx(x0, y);
        k2 = h * dydx(x0 + 0.5 * h, y + 0.5 * k1);
 
        # se actualiza el valor de y
        y = y + (1.0 / 6.0) * (k1 + 2 * k2);
 
        # se actualiza el nuevo valor de x
        x0 = x0 + h;
 
    return y;
 
# resultados
if __name__ == "__main__" :
 
    x0 = 0; y = 4;
    x = 3; h = 0.5;
 
    print("y(x) =",rungeKutta(x0, y, x, h));
 