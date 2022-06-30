from numpy import array, zeros, fabs, linalg

#indicando las matrices y las demas variables
a = array([[0, 5, -5, 4, 6],
           [0, 2, 4, 11, 7],
           [6, 2, 0, 8, -2],
           [2, 4, 3, 0, 3],
           [7, 3, 1, -4, 2]], float)

 
b = array([6, 4, 2, 3, 5], float)


print(linalg.solve(a, b))

p = len(b)
q = zeros(p, float)

#primer for para la fila fija
for k in range(p-1):
    if fabs(a[k,k]) < 1.0e-12:
        
        for i in range(k+1, p):
            if fabs(a[i,k]) > fabs(a[k,k]):
                a[[k,i]] = a[[i,k]]
                b[[k,i]] = b[[i,k]]
                break

 #aplicando el metodo
    for i in range(k+1,p):
        if a[i,k] == 0:continue

        factor = a[k,k]/a[i,k]
        for j in range(k,p):
            a[i,j] = a[k,j] - a[i,j]*factor
            
#En este apartado se calcula el vector de cada fila
        b[i] = b[k] - b[i]*factor
print(a)
print(b)


q[p-1] = b[p-1] / a[p-1, p-1]
for i in range(p-2, -1, -1):
    sum_ax = 0
  
    for j in range(i+1, p):
        sum_ax += a[i,j] * q[j]
        
    q[i] = (b[i] - sum_ax) / a[i,i]

print("Solucion del sistema por Gauss:")
print(q)