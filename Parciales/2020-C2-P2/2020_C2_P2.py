#ej 1) 
# a)    NUMERACION
#b)     NUMERACION

#ej2) TEXTIL
'''
'''

#ej 3) INGRESO  NUMEROS H/ LIMITE DEVUELVE MENOR
'''
Se pide realizar una función que devuelva el número entero más pequeño de un listado ingresado por 
el usuario, tal que la suma de los N números exceda un valor pasado por parámetro en la función
'''
'''
def menor_numero(limite: int) -> int:
    """
    PRE: Limite es el valor en el cual se corta el ingreso
    POST: Devuelve el menor de los numeros ingresados
    """
    print('Ingrese numeros')
    
    lista = list()
    sum = 0
    while sum <= limite:
        num = input('ingrese: ')
        while not num.strip('-').isnumeric() :
            num = input('Ingrese un numero valido: ')

        sum += int(num)
        lista.append( int(num) )
    
    minimo = min (lista)

    return minimo

print(menor_numero(12))
'''