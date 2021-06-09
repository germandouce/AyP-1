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
#ej 7.3 
#c) - Vote por mi (con más parametros)
'''
Modificar la función anterior para que tengan en cuenta el género del destinatario,
para ello, deberán recibir una tupla de tuplas, conteniendo el nombre y el género 
('Masculino' o 'Femenino').
'''
'''
ejÑ >> imprimir_mensajes((('Juan', 'Masculino'), ('Pedro', 'Masculino'), ('Agus', 'Femenino')), 1, 2)
Estimado Pedro, vote por mi.
Estimada Agus, vote por mi.
'''
'''
def imprimir_mensajes(nombres, p, n) -> None:
    """
    imprime lo pedido segun lo pedido we
    """
    if len(nombres)>0 and (p + n !=0):
        indice = p
        while indice <= len(nombres)-1 and indice <=n:
            if nombres[indice][1] == "Masculino":
                print(f'Estimado {nombres[indice][0]}, vote por mi.')
            else:
                print(f'Estimada {nombres[indice][0]}, vote por mi.')
            indice += 1

imprimir_mensajes((('Juan', 'Masculino'), ('Pedro', 'Masculino'), ('Agus', 'Femenino')), 1, 2)
'''

# 7.6 - Clasificando números
'''
Dada una lista de números enteros y un entero k, escribir una función que:

a) Devuelva tres listas, una con los menores, otra con los mayores y otra con los iguales a k.

>> menores, mayores, iguales = menores_mayores_iguales([1, 2, 3, 4, 5, 6], 3)
>> menores
[1, 2]
>> mayores
[4, 5, 6]
>> iguales
[3]

b) Devuelva una lista con aquellos que son múltiplos de k.
'''
'''
def menores_mayores_iguales(enteros, k):
    """
    Devuelve lista con men may e ='s a k
    """
    menores: list = list()
    mayores: list = list()
    iguales: list = list()
    
    for num in enteros:
        if num < k:
            menores.append(num)
        elif num > k:
            mayores.append(num)
        else:
            iguales.append(num)

    return menores, mayores, iguales

# menores, mayores, iguales = menores_mayores_iguales([1, 2, 3, 4, 5, 6], 3)
# print(menores, mayores, iguales)

def multiplos(enteros, k):
    """
    Devuelve lista con multiplos de K
    """
    multiplos_de_k: list = list()
    for num in enteros:
        if num % k == 0:
            multiplos_de_k.append(num)
    
    return multiplos_de_k

#print(multiplos([10, 11, 12], 2))
'''

# ej 7.7 Listas de nombres
'''
Escribir una función que reciba una lista de tuplas (Apellido, Nombre, Inicial_segundo_nombre) 
y devuelva una lista de cadenas donde cada una contenga primero el nombre, luego la inicial 
con un punto, y luego el apellido.
Ejemplo:

>>>escribir_nombres([('Turing', 'Alan', 'M'), ('Liskov', 'Barbara', 'J')])
['Alan M. Turing', 'Barbara J. Liskov']
'''
'''
def escribir_nombres(lista):
    """
    Devulve los nombres bien escitos
    """
    lista_de_cadenas: list = list()
    for nombre in lista:
        lista_de_cadenas.append(f'{nombre[1]} {nombre[2]}. {nombre[0]}')
    return lista_de_cadenas

print(escribir_nombres([('Turing', 'Alan', 'M'), ('Liskov', 'Barbara', 'J')]))
'''

#ej 8 a) - Invertir Lista

'''
Realizar una función que, dada una lista, devuelva una nueva lista cuyo contenido sea igual a 
la original pero invertida.

Ejemplo:
>> invertir_lista(['Di', 'buen', 'dia', 'a', 'papa'])
['papa', 'a', 'dia', 'buen', 'Di']
'''
'''
def invertir_lista(lista):
    """
    Invierte la lista
    """
    lista = lista[::-1]
    return lista
print( invertir_lista(['Di', 'buen', 'dia', 'a', 'papa']) )
'''
#ej 7.8 
# b) 08b - Invertir Lista In-Place
'''
Realizar una función que invierta una lista, pero en lugar de devolver una nueva, modifique la 
lista dada, sin usar listas auxiliares.

Ejemplo:
'''
'''
def invertir_lista(lista):
    """
    igual q el anterior
    """
    #for ele in lista:
    #    print(lista)
    lista = lista[::-1]
    listita = lista
    return listita

print( invertir_lista(['papa', 'a', 'dia', 'buen', 'Di']) )
'''
#AssertionError: Lists differ: ['papa', 'a', 'dia', 'buen', 'Di'] != ['Di', 'buen', 'dia', 'a', 'papa']
#sin seguir consigna..
'''
def invertir_lista(lista):
    """
    igual q el anterior
    """
    
    lista_aux: list = list()

    for i in range (len (lista) ):
        lista_aux.append ( lista[i] )
    
    for i in range ( len(lista_aux) ):
        lista[i] = lista_aux[ len(lista_aux) -1 - i]
    
    return lista

print( invertir_lista(['papa', 'a', 'dia', 'buen', 'Di']) )
'''
# ej 7.9 - Empaquetar
'''
Escribir una función empaquetar para una lista, donde empaquetar significa indicar
la repetición de valores consecutivos mediante una tupla (valor, cantidad de repeticiones). 
Debe devolver una lista de tuplas.
Ejemplo:
>>>empaquetar([1, 1, 1, 3, 5, 1, 1, 3, 3])
[(1, 3), (3, 1), (5, 1), (1, 2), (3, 2)]
'''
'''
def empaquetar(lista):
    """
    empaqueta = cuento numero de numeros xd
    """
    lista_de_paquetes: list = list()
    if len (lista) >0:

        ultimo = lista[0]
        cont = 1
        for i in range (1, len(lista)):
            
            if lista[i] == ultimo:
                cont += 1
            
            else:
                lista_de_paquetes.append( ultimo, cont) )
                cont = 1
                ultimo = lista[i]
        
        lista_de_paquetes.append( (lista[i],cont) )    
    
    return lista_de_paquetes

print(empaquetar( [1, 1, 1, 3, 5, 1, 1, 3, 3]) )
'''

#ej 7.11 - Plegado de un texto

'''
Escribir una función que reciba un texto y una longitud y devuelva una lista de cadenas de como 
máximo esa longitud. Las líneas deben ser cortadas correctamente en los espacios (sin cortar 
las palabras).
Por ejemplo, para el texto 'Voy a aprobar Algoritmos 1' y la longitud 18, la función deberá 
devolver 'Voy a aprobar'.
'''
'''
def plegar_texto(texto, longitud):
    """
    hace cosas raras recortando los textos
    """
    lista_texto_cortado: list = list()

    list_texto_orig = texto.split()

    len_tot = 0
    for palabra in list_texto_orig:
        len_tot += len(palabra)
        if len_tot <= longitud:
            lista_texto_cortado.append(palabra)
    
    cadena_texto_cortado = ' '.join(lista_texto_cortado)
    
    return cadena_texto_cortado

print(plegar_texto ('Voy a aprobar Algoritmos 1', 21) )
'''