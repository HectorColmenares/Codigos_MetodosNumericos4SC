import numpy as np
# Metodo de determinantes

a= np.array([[4.,-0.2,-0.4],
            [0.5,5,-0.6],
            [0.7,-0.4,10.]])

AB= np.copy(a)

contador=0

sz = np.shape(AB)
h=sz[0]
l=sz[1]

for i in range(0, h-1, 1):
    columna = abs(AB[i:, i])
    max= np.argmax(columna)
    if(max !=0):
        contador=contador +1   
        tiempo = np.copy(AB[i, :])
        AB[i, :]= AB[max +i,:]
        AB[max + i,:]= tiempo

AB1= np.copy(AB)

for i in range(0, h-1, 1):
    pivote= AB[i, i]
    adelante= i+1
    for k in range(adelante, h-1):
        fact=AB[k,i]/pivote
        AB[k, :]= AB[k, :]- AB[i,:]*fact
    
    mult=1
    
for i in range  (0, h, 1):
    mult=mult * AB[i, i]
determinante = ((-1)**contador)*mult

print("pivoteo parcial por filas")
print(AB1)
print("elimi. hacia adelante")
print(AB)
print("determinante")
print(determinante)
    
    
          