#CLASE 20: MANEJO DE ARCHIVOS
#Martes 22/06/2021

#Ej 1
'''
Se les proporcionará un archivo cadenas.txt donde cada línea contiene una cadena generada de forma 
aleatoria. Lo que se les pide es que lean cada línea del archivo y mostrar mediante consola el primer 
carácter de cada cadena.
'''
'''
ruta_archivo =  'archivos/cadenas.txt'
with open(ruta_archivo,'r') as archivo:
    for linea in archivo:
        print(linea[0], end = ' ')
'''
#Exepciones: 
#raise exception
'''
raise Exception('ola')
'''
#assert
'''
def multipliar(a,b):
    return a-b

assert(4 == multipliar(2,2) )
'''
#ejemplo con funcion isinstance
'''
def division(a:int, b:int) ->float :
    if not isinstance(a, int) or not isinstance(b, int):
        raise ValueError("a y b deben ser enteros")
    else:
        resultado = a/b

    return resultado

print(division('a',5 ))
'''
#Ej 2
'''
Se les proporcionará un archivo numeros.txt, donde cada línea contiene un número de forma aleatoria. Lo 
que les pedimos es leer el archivo y calcular la suma de todos esos números y mediante un assert 
verificar que la suma sea igual a 2.613.60
'''
'''
def suma():
    ruta = 'archivos/numeros.txt'
    with open(ruta,'r') as arch:
        sum = 0
        for num in arch:         #cada linea es un numero
            sum += int(num)
    return sum

assert(suma() == 2613600)
'''
'''
import os

BASE_DIR = os.path.abspath(os.path.dirname(__file__))
NOMBRE_DEL_ARCHIVO = "cadenasv2.txt"
RUTA = os.path.join(BASE_DIR, NOMBRE_DEL_ARCHIVO)
'''

#APUNTES Y RELECTURA DESPUES DE CLASE. PSEUDORESUMEN DE LA CLASE

'''
archivo = open(“nombre_del_archivo.extensión”, “modo_de_apertura”)

Por defecto, el archivo se abre en el modo de lectura ‘r’, pero hay otros modos de apertura 
tales como:

Solo lectura ‘r’ (Por defecto), archivo = open(“archivo.txt”, “r”)
Solo escritura ‘w’ (Si el archivo existe, borra su contenido para comenzar de cero y si no, crea 
uno nuevo)
Solo escritura al final del archivo ‘a’. (Si el archivo no existe, lo crea).

Existe otros modos de apertura tales como ‘r+’, ‘w+’, ’a+’. 
Que cumplen las dos funciones de leer-escribir. Pero cumplen
las mismas características de cada modo.
'''
#ejemplos`:
'''
ruta = 'archivos/entrada.txt'
arch = open(ruta, 'r') #ojo son tods str los args!!
'''
#Una vez q abierto leemos las lineas usando ciclos
#con while:

#opcion 1
'''
linea = arch.readline() #readline() devuelve un str con cada linea del archivo
while linea != '':
    print(linea)
    linea = arch.readline()

#por ultimo hay q cerar al archivo
arch.close()
'''
#opcion 2 #con for
'''
for linea in arch:
    print(linea)
'''
# readlines() devuelve una lista con las lineas del arhivos (cada linea es un ele)
#ejemplo 2 # MEJOR!! con with open
'''
ruta = 'archivos/entrada.txt'
with open(ruta,'r') as archivo:
    for linea in archivo:
        # linea = linea.rstrip('\n')
        # linea = linea.lstrip('\n')
        # linea = linea.strip('\n')
        print(linea) 

#Con este metodo el archivo se cierra automatica// !! 
'''
#IMPORTANTE
'''
Al momento de leer las líneas de un archivo, también se incluirá el salto de línea ‘\n’. 
Los siguientes métodos de strings sirven para eliminar los saltos de línea:
1. linea.rstrip(‘\n’)(Elimina el salto de línea del lado derecho).
2. linea.lstrip(‘\n’)(Del lado izquierdo)
3. linea.strip(‘\n’)(De ambos lados)
'''

#Escritura de archivos para

#Para escribir una línea utilizamos:
'''
archivo_b = open('archivos/archivo_b','w')

linea = 'hola como va?'
archivo_b.write(linea)
'''
# Para escribir varias líneas utilizamos:
'''
lineas = ['hola','q','onda']
archivo_b.writelines(lineas)    #OJO!!! Concatena los strings en una sola linea. NO grega /n al final!
'''
#usando write()
'''
lines = ['line1', 'line2']
with open('archivos/archivo_b.txt', 'w') as f:
    f.write('\n'.join(lines))       #Uno las lineas con un \n q lo intepreta como salto de linea
'''
#usando writelines
'''
lines = ['line1', 'line']
with open('arhivos/archivo_b.txt', 'w') as f:
    # for l in lines:
    #     f.writelines('%s\n' %l)
    f.writelines("%s\n" % l for l in lines)
'''

#para pasar info d eun archivo a otro
'''
archivo_a = open('archivos/archivo_a.txt', 'r')
lineas_a = archivo_a.readlines()    #guardo una lista con los las lineas
archivo_a.close()

with open('archivos/archivo_b.txt', 'w') as archivo_b:
    for linea in lineas_a:          #dsps la recorro y las imprimo en archivo_b
	    archivo_b.write(linea)
'''

#LIBRERIA OS

import os
'''
A veces necesitamos saber el directorio en el que estamos, si en una ruta dada tenemos un archivo 
o un directorio, también podemos verificar si un archivo o directorio existe y demás cosas.
'''
#ej de verificacion de exitencia de un directorio,
#os.path.isdir: devuelve 
'''
directorio = input('Ingrese el nombre del directorio utilizando ‘\’: ')
if not os.path.isdir(directorio):       #isdir devuelve true si existe el directorio
	print('Directorio invalido')        #OJIIIISMO! RUTA COMPLETA!!
else:
	print('este es el directorio: ',directorio)
'''
#Lo mismo podemos hacer con archivos
'''
nombre_archivo = input('Ingrese el nombre del archivo: ') 
if not os.path.isfile(nombre_archivo):
	print('Nombre de archivo invalido')
else:
    print(nombre_archivo)
    with open(nombre_archivo,'r') as tareas:
        for linea in tareas:
            linea = linea.rstrip('\n')
            print(linea)         
'''
#directorio en donde estamos utilizamos: os.getcwd
'''
Ahora que tenemos la ruta del directorio en el que estamos, podemos concatenar rutas 
de la siguiente forma:
'''
'''
directorio = os.getcwd()
print('Usted esta en:',directorio)


nombre_del_archivo = input('Ingrese el nombre del archivo: ')
ruta_del_archivo = os.path.join(directorio, nombre_del_archivo)
if not os.path.exists(ruta_del_archivo):
	print('Directorio invalido')
else:
	print('el archivo es:',ruta_del_archivo)
'''
#MANEJO DE ERRORES EN PYTHON

#Tipos de errores en Python 
'''
Exception (Error genérico)
AssertionError (Falló un assert)
IndexError (Acceder a una posición inválida)
KeyError (Clave inexistente en un diccionario/conjunto)
TypeError (Realizar una operación con un tipo incorrecto)
ValueError (Realizar una operación con un tipo válido pero un valor inválido)
ZeroDivisionError (División por cero)
IOError (Error de entrada/salida, por ejemplo apertura de archivo inexistente)
'''
#Una vez q salta el error se detiene la ejecucion del programa
# ejemplos:

#raise exception: levanta la excepcion con el nombre que querramos
'''
raise Exception('Error controlado por nosotros')
'''
#asserts
'''
Los asserts también son un tipo de ruptura controlada. Se utilizan para realizar 
pruebas de las funcionalidades en un programa'''
'''
def suma(a: int, b: int) -> int:
	return a - b

assert(suma(3,5) == 8)
'''
#Validaciones de tipo con error "personalizado"
#por ejemplo si una función acepta un unico tipo de dato
#Ejemplo:

#isinstance(variable, tipo de dato): devuelve True si es correcto, False si no lo es.
'''
def suma(a: int, b: int):
	if not isinstance(a,int) or not isinstance(b,int):
		raise ValueError('A y B deben de ser int')
	return a + b

print(suma('1',2))
'''
#Estructura de un try/except
'''
l=[1,2]
try:
    a=8
    a=l[3]
    b='1'/2
    #Acá iría el código que estaremos
	#controlando
except TypeError:
    print('Hubo type error')
    b=4
	#Código en caso de que se levante una excepción de TypeError
except IndexError:
    print('Hubo index error')
	#Código en caso de que se levante una excepción de ValueError
else:
    print('no hubo error')
	#Código que se ejecuta si no se levante ninguna excepción
finally:
	print('Finally, ni nos vimo')
    #Código que SIEMPRE se ejecuta.
'''

#ACLRACIONES IMPORTANTES:
#La estructura del try except es similar (ojo no igual) a la de un if. La logica corresponde
#al primer try, es decir, si el error es tipo a) se ejecuta except error tipo a, si el error
#e tipo b, se produce se ejecuta except error tipo b. Entonces si tengo otro error dentro de
#un except xa manejar el mismo necesito una nueva estructura de try except!!

#Otros ejemplos:
#Division por 0
'''
dividendo = int(input('Ingrese el dividendo: '))
divisor = int(input('Ingrese el divisor: '))
try:
	resultado = dividendo / divisor
except ZeroDivisionError:
	print('No se puede dividir por cero.')
else:
	print(f'{dividendo}/{divisor} = {resultado}')
'''

#Errores al abrir archivos
'''
ruta_archivo = input('Ingrese ruta del archivo: ')
try:
    archivo = open(ruta_archivo, 'r')
except IOError: #No se encontró el archivo
    #En caso de darse la excepción, entramos en este bloque de código
    print('No se encontro el archivo')
except:
	#En caso de que cualquier otra excepción.
    print('todo no ok')
else:
	print('Procesando archivo')
    #Procesamos el archivo
	#Y lo cerramos.
finally:
    print('terminamos')
'''

#ej de tarea 1
'''
Se tiene un archivo de texto(alumnos.txt) con el siguiente formato:
padron, nombre, apellido
Luego se tiene otro archivo de texto(notas.txt) con el siguiente formato:
padrón, materia, nota
A partir de esa información, deseamos saber lo siguiente:
* La materia con mayor cantidad de aprobados (nota >= 4).
* El promedio general de cada materia.
* Los alumnos con un promedio general mayor a 7.
* El alumno con el mayor promedio.
'''
#ESTRUCTURA ELEGIDA:
#alumnos = {padron: Nombre:
#                   Apellido:
#                  } 
#           }
#notas ={materia:  {calificaciones = {padron: nota}
#                   }
#       }

#RESTO DEL CODIGO EN Mini_programas/abm_tipo_notas_con_archivos.py

#otro ej de tarea:
'''
EJERCICIO PARA LA CLASE QUE VIENE!
Se pide hacer un programa que abra un archivo de texto llamado entrada.txt el mismo contiene el 
siguiente poema de Ruben Dario
--poema--
y permita al usuario poder buscar palabras. Si las mismas se encuentran deberá:
a- indicar cuántas veces aparece y en qué línea del poema está.
b- copiar la línea a un archivo llamado salida.txt
Además se deberá implementar try except para la apertura de archivos
'''
'''
with open('archivos/entrada.txt','r') as poema:
    for linea in poema:
        print(linea)    
'''

#CLASE 21: GIT Y GITHUB

#CLASE 22:       

#CLASE 23 ---> FIN CURSADA: LENGUAJE C + TP DRIVEHUB
#VER EN CARPETA LENGUAJE C