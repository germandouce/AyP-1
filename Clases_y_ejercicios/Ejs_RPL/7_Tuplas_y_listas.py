#UNIDAD 7: Tuplas y Listas



#ej 7.1 - En orden 
'''
Escribir una función que reciba una tupla de elementos e indique si se encuentran ordenados de 
menor a mayor o no.
'''
'''
def esta_ordenada(tupla):
    """
    dice si esta ordenada o no la tuplita menor a mayor o no
    """
    ordenada = True
    if len(tupla) > 0:
        mayor = tupla[0]
        for i in range(1, len(tupla) ):
            if tupla[i] < mayor:
                ordenada = False
            else:
                mayor = tupla[i]
        
    return ordenada

# tupla = ()
# print( esta_ordenada(tupla ))
'''

#Ej 7.3
#a) - Vote x mi
'''Escribir una función que reciba una tupla con nombres, y para cada nombre imprima el 
mensaje Estimado <nombre>, vote por mi..
'''
'''
def imprimir_mensaje(nombres):
    """
    imprime lo pedido segun lo pedido we
    """
    for nombre in nombres:
        print(f'Estimado {nombre}, vote por mi.')
'''

#Ej 7.3b - Vote por mi (con parametros)
'''
Escribir una función que reciba una tupla con nombres, una posición de origen p y una
cantidad n, e imprima el mensaje anterior para los n nombres que se encuentran a partir
de la posición p.
'''
'''
def imprimir_mensajes(nombres, p, n) -> None:
    """
    imprime lo pedido segun lo pedido we
    """
    if len(nombres)>0 and (p + n !=0):
        indice = p
        while indice <= len(nombres)-1 and indice <=n:
            print(f'Estimado {nombres[indice]}, vote por mi.')
            indice += 1
imprimir_mensajes(('juan', 'pepe','carlos', 'german', 'sherman'),0,0)
'''