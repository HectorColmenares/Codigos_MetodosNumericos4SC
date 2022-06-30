import numpy as np

# functions

def func(x):
    f = x * np.cosh((4 / x) - np.arccosh(8 / x)) - 9
    return f



def check(a, b):
    a1 = func(a)
    b1 = func(b)
    if ((a1 * b1) < 0) == False:
        return False
    else:
        return True





def get_repeticiones():

    m = int(input("digite el numero de repeticiones que guste: "))
    return m




def falsaposicion(a, b):
    if check(a, b) == True:
        n = get_repeticiones()
        i = 0
        
        while i < n:

            x = (a * func(b) - b * func(a)) / (func(b) - func(a))

            if func(x) == 0:
                break
            else:
                if check(a, x) == True:
                    b = x

                elif check(x, b) == True:
                    a = x
            i += 1
        return x
    else:
        print("Entrada Invalida")


print("RAIZ: {}".format(falsaposicion(7, 8)))