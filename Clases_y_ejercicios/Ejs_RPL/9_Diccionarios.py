#UNIDAD 9: Diccionarios

#METODOS CLAVE!


# diccionario.keys() :Devuelve una secuencia desordenada, con todas las claves que se hayan 
# ingresado al diccionario

# diccionario.values(): Devuelve una secuencia desordenada, con todos los valores que se hayan 
# ingresado al diccionario.

# diccionario.items(): Devuelve una secuencia desordenada con tuplas de dos elementos, en las 
# que el primer elemento es la clave y el segundo el valor.

# diccionario.get(clave,[]) # devuelve el valor de la clave dada, en el caso de que la clave no 
# exista, devuelve el parámetro por omisión (2do parametro)

#NO OLVIDAR .lower() en claves! EN TODOS LADOS!!


#ej 9.1 - Tuplas a diccionario
'''
Escribir una función que reciba una lista de tuplas, y que devuelva un diccionario
en donde las claves sean los primeros elementos de las tuplas, y los valores una lista con los
segundos.

Por ejemplo:
>> l = [ ('Hola', 'don Pepito'), ('Hola', 'don Jose'), ('Buenos', 'días') ]
>> print(tuplas_a_diccionario(l))
{ 'Hola': ['don Pepito', 'don Jose'], 'Buenos': ['días'] }
'''
'''
def tuplas_a_diccionario(lista):
    """
    devuelbe diccionario con lo pedido
    """   
    palabras:dict = dict()
    
    for i in range( len(lista) ):
        if lista[i][0] not in palabras:
            palabras[ lista[i][0] ] = [lista[i][1]]
        else:
            palabras[ lista[i][0] ].append(lista[i][1])

    return palabras

l = [ ('Hola', 'don Pepito'), ('Hola', 'don Jose'), ('Buenos', 'días') ]
print(tuplas_a_diccionario(l))
'''

#ej 2 
# a) contador de palabras
'''
Escribir una función que reciba una cadena y devuelva un diccionario con la cantidad de 
apariciones de cada palabra en la cadena. Por ejemplo, si recibe ”Qué lindo día que hace hoy” 
debe devolver { 'qué': 2, 'lindo': 1, 'día': 1, 'hace': 1, 'hoy': 1}.
'''
'''
def contar_palabras(cadena:str) ->dict :
    """
    Devuelve dict con numero de apariciones de cada palabra
    """
    lista_de_palabras = cadena.split()
    contador_palabras: dict = dict()

    for palabra in lista_de_palabras:
        if palabra.lower() not in contador_palabras:
            contador_palabras[palabra.lower()] = 1
        else:
            contador_palabras[palabra.lower()] += 1
    
    return contador_palabras

texto = 'Qué lindo día que hace hoy' 
print(contar_palabras(texto))
'''

#ej 2
#b) Contador de caracteres
'''
Escribir una función que cuente la cantidad de apariciones de cada
caracter en una cadena de texto, y los devuelva en un diccionario.
Por ejemplo, si se recibe "Qué lindo día que hace hoy" debe devolver:

{'u': 2, 'd': 2, 'o': 2, 'a': 2, 'e': 2, 'h': 2, 'Q': 1, 
'é': 1, 'l': 1, 'i': 1, 'n': 1, 'í': 1, 'q': 1, 'c': 1, 'y': 1}
'''
'''
def contar_caracteres(cadena) -> dict:
    """
    cuenta caracteres
    """
    contador_caracteres: dict = dict()
    
    for letra in cadena:
        if letra != ' ':
            if letra.lower() in contador_caracteres:
                contador_caracteres[letra.lower()] += 1
            else:
                contador_caracteres[letra.lower()] = 1
        
    return contador_caracteres

texto = 'Qué lindo día que hace hoy' 
print(contar_caracteres(texto))
'''

#ej 2
# c) - Contar resultados de dados
'''
Escribir una función que reciba una cantidad de iteraciones de una tirada de 2 dados a realizar
y devuelva la cantidad de veces que se observa cada valor de la suma de los dos dados.
Nota: utilizar el módulo random para obtener tiradas aleatorias.

Algunos posibles resultados:

>> contar_resultados_dados(1)
{3: 1, 5: 1}
>> contar_resultados_dados(1)
{4: 2}
>> contar_resultados_dados(3)
{2: 1, 5: 1, 4: 2, 6: 1, 3: 1}
>> contar_resultados_dados(3)
{6: 1, 4: 2, 3: 2, 5: 1}
>> contar_resultados_dados(3)
{1: 2, 2: 2, 6: 1, 3: 1}
'''
'''
#entiendo q es: tiro 2 dados 'n' veces y quiero saber cuantas veces sale la suma de ellos.
la suma son claves, las veces, sus respectivos valores.

import random

# La siguiente línea de código hace que random.randint siempre genere la misma secuencia de 
# números. Es necesaria para que cada vez que se corran las pruebas se obtengan los mismos 
# resultados. En un programa "real" no debería estar. 
random.seed(123)

def contar_resultados_dados(n):
    """
    real// no se q hace
    """
    observaciones: dict = dict()

    for i in range(n):
        dado_1 = random.randint(1,7)
        dado_2 = random.randint(1,7)
        print(dado_1,dado_2)
        suma = dado_1 + dado_2
        if suma not in observaciones:
            observaciones[suma] = 1
        else:
            observaciones[suma] += 1
    return observaciones

n = 3
print( contar_resultados_dados(n) )
'''

#ej 3 - Agenda telefonica
'''
Escribir un programa que vaya solicitando al usuario que ingrese nombres.

Si el nombre se encuentra en la agenda (implementada con un diccionario), debe mostrar
el teléfono y, opcionalmente, permitir modificarlo si no es correcto.
Si el nombre no se encuentra, debe permitir ingresar el teléfono correspondiente.
El usuario puede utilizar la cadena ”*”, para salir del programa.
Algunas aclaraciones para la implementación en RPL:

No hace falta verificar que el teléfono sea un número de teléfono válido.
No se agrega la persona a la agenda si el número ingresado es vacío.
De la misma forma, no se modifica el número si el nuevo número ingresado es vacío.
Hay un enter (\n) entre cada iteración que no se muestra en la pantalla de resultados 
(estamos viendolo, comparar con el ejemplo que se ve a continuación)

Ingrese un nombre, o * para salir: Fede
Persona no agendada
Ingrese el telefono para Fede: 1111
Nuevo telefono registrado para Fede, 1111

Ingrese un nombre, o * para salir: Agus
Persona no agendada
Ingrese el telefono para Agus: 2222
Nuevo telefono registrado para Agus, 2222

Ingrese un nombre, o * para salir: Fede
Telefono de Fede es 1111
Ingrese el telefono para Fede: 3333
Telefono actualizado para Fede, 3333

Ingrese un nombre, o * para salir: Agus
Telefono de Agus es 2222
Ingrese el telefono para Agus: 

Ingrese un nombre, o * para salir: Agus
Telefono de Agus es 2222
Ingrese el telefono para Agus: 4444
Telefono actualizado para Agus, 4444

Ingrese un nombre, o * para salir: *
'''