#UNIDAD 4: Funciones



#ej 4.1 
# a) - Es par
'''Escribir una función indique si un determinado número entero es par o no'''
'''
n=4
def es_par(n):
    """
    dice si es par o no
    """
    # if n%2 == 0:
    #     return (n%2 + 1)
    # else:
    #     return (n%2 - 1)
    return (n%2 == 0)

print(es_par(n))
'''

#4.1 
# b) -  Es primo
'''Escribir una función que indique si un número natural es primo.

Recordar: Un número es primo cuándo tiene exactamente dos divisores (sólo se puede dividir por 1 y 
por sí mismo).'''
'''
def es_primo(n):
    """
    dice si es primo o no
    """
    es_primo = True
    divisor = n-1
    while divisor >1:    
        
        if n % divisor == 0:
            es_primo = False
        
        divisor -=1
    
    return es_primo

print( es_primo( int (input('n:') ) ) )
'''

#4.2 - Abs
'''
Escribir una implementación propia de la función abs, que devuelva el valor absoluto de
cualquier valor que reciba.'''
'''
def mi_abs(x):
    """
    devuelve el valor absoluto
    """
    if x<0:
        x = -x
    return x

print(mi_abs(int(input('n: '))))
'''

#4.3 - Matrzi matriz identidad
'''
Escribir una función que reciba por parámetro una dimensión n, e imprima la matriz identidad 
correspondiente a esa dimensión.'''
'''
def matriz_identidad(n) -> None:
    """
    DOC: Completar.
    """
    for i in range(n):
        fila = list()
        for j in range(n):
            if i ==j:
                print(1, end = ' ')
                #fila.append(1)
            else:
                print(0, end = ' ')
                #fila.append(0)
        print()
matriz_identidad(int(input('n:')))
'''

#4.4 a) - Extremos de un polinomio
'''
Escribir una función que permita encontrar el máximo o mínimo de un polinomio de segundo grado.
La función deberá devolver la posición del extremo y un booleano indicando si es un máximo.
El polinomio estará representado por sus coeficientes en la forma a x² + b x + c. Por ejemplo, 
para el polinomio 2 x² + 3 x + 4 los coeficientes serían a = 2, b = 3, c = 4.

Se deberá validar que el polinomio sea de segundo grado (a != 0). Si la validación falla, la 
función deberá devolver None.
'''
#FIACA
#maximo o minimo es el vertice -b/2a
'''
def buscar_extremo(a, b, c) -> tuple:
    """
    max y min de p(x)
    """
    if a == 0:
        maxi_mini = None
    else:
        maxi_mini = -b/(2*a)

    return maxi_mini

'''