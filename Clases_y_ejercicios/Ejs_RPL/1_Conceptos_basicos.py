#ejs RPL-FIUBA:

#UNIDAD 1: Conceptos Basicos



#ej 1.1 - Producto
'''Escribir una función que reciba dos números y devuelva su producto

Ej:

    producto(2,2) == 4
    producto(1,2) == 2
    producto(8,5) == 40
'''
'''
def ingreso ():
    num1 = int ( input("Ingrese el primer número: ") )
    num2 = int ( input("Ingrese el segundo número: ") )

    return num1, num2

def producto (num1, num2) -> int:
    """
    hace el producto entre num1 y num2
    """
    resultado = num1*num2
    
    return resultado


def mostrar (resultado) -> None:
    """muestra por pantalla el resultado"""
    print(resultado)

def main ():
    num1, num2 = ingreso ()
    mostrar( producto ( num1, num2 ) ) 

main()
'''


#ej 1.2 - Mi primer programa
'''Utilizando la función del ejercicio anterior, escribir un programa que pida al usuario dos números, y luego muestre por pantalla el producto.

Ej:

    > Ingrese el primer número: 2
    > Ingrese el segundo número: 5
    El producto es 10
Tip: Pensar bien en qué función hay que usar print y en cual hay que usar return.
Tip2: No olvidar invocar la función main()
'''
'''
def ingreso ():
    num1 = int ( input("Ingrese el primer número: ") )
    num2 = int ( input("Ingrese el segundo número: ") )

    return num1, num2

def producto (num1, num2):
    """
    hace el producto entre num1 y num2
    """
    resultado = num1*num2
    
    return resultado


def mostrar (resultado):
    "muestra por pantalla el resultado"
    print ("El producto es", int(resultado))


def main ():
    """
    El programa le pide 2 números al usuario y luego imprime el producto.
    """
    num1, num2 = ingreso()
    resultado = producto(num1, num2)
    mostrar(resultado)

main()
'''


#EJ 1.3 - Funciones y Geometría
'''Escribir funciones que permitan:
a) Calcular el perímetro de un rectángulo dada su base y su altura.
b) Calcular el área de un rectángulo dada su base y su altura.
c) Calcular el área de un rectángulo (alineado con los ejes x e y) dadas sus coordenadas
x1, x2, y1, y2.
d) Calcular el perímetro de un círculo dado su radio.
e) Calcular el área de un círculo dado su radio.
f) Calcular el volumen de una esfera dado su radio.
g) Dados los catetos de un triángulo rectángulo, calcular su hipotenusa.'''
'''
from math import pi, sqrt

def rectangulo_perimetro(base, altura):
    rectangulo_perimetro = 2 * base + 2 * altura
    
    return rectangulo_perimetro

def rectangulo_area(base, altura):
    rectangulo_area = base * altura 

    return rectangulo_area

def rectangulo_area_coord(x1, x2, y1, y2):
    rectangulo_area_coord = ( x2 - x1 ) * ( y2 - y1 )

    return rectangulo_area_coord

def circulo_perimetro(radio):
    ciculo_perimetro = 2 * pi * radio

    return ciculo_perimetro 

def circulo_area(radio):
    circulo_area =  pi * ( radio ** 2 )

    return circulo_area

def esfera_volumen(radio):
    esfera_volumen = ( 4/3 ) * pi * radio **3 
    return esfera_volumen

def triangulo_rect_hipotenusa(cateto1, cateto2):
    triangulo_rect_hipotenusa = sqrt (cateto1**2 + cateto2**2 )
    return triangulo_rect_hipotenusa 

def main() -> None:
    """Fiaka el resto"""

    print (circulo_area(4))

main()
'''


#ej 1.4 - Ciclo for
'''Analizar los siguientes bloques de código. ¿Cuál será el resultado de ejecutarlos?
Verificar la respuesta con el intérprete.'''
'''
#a)

for i in range(5):
    print("print",'(',i * i,')')
#b)

for i in range(2, 6):
    print("print",'(',i, 2 ** i,')')

'''


#ej 1.5 - Factorial
'''Escribir una función que, dado un número entero n, permita calcular su factorial.
Ej:

    > factorial(1)
    1
    > factorial(3)
    6
    > factorial(17)
    40320
'''
'''
def factorial(n):
    resultado = 1
    for numero in range (1,n+1):
        resultado *= numero
        print(resultado)
    return resultado

n = int(input())
print(factorial(n))
'''


#ej 1.6 - Cuentas
''' a) Pida dos números, imprimir la suma, resta, división y multiplicación de ambos.

Ej:

    > Ingrese el primer número: 3
    > Ingrese el segundo número: 4
    Suma: 7
    Resta: -1
    División: 0.75
    Multiplicación: 12 '''
'''
def ingreso ():
    num1 = int ( input("Ingrese el primer número: ") )
    num2 = int ( input("Ingrese el segundo número: ") )

    return num1, num2


def suma (num1, num2) -> int:
    """
    hace el producto entre num1 y num2
    """
    resultado = num1 + num2
    
    return resultado

def resta (num1, num2) -> int:
    """
    hace el producto entre num1 y num2
    """
    resultado = num1 - num2
    
    return resultado

def division (num1, num2) -> int:
    """
    hace el producto entre num1 y num2
    """
    resultado = num1/num2
    
    return resultado

def multiplicacion (num1, num2) -> int:
    """
    hace el producto entre num1 y num2
    """
    resultado = num1*num2
    
    return resultado


def mostrar (num1, num2) -> None:
    """muestra por pantalla el resultado"""
    print('suma:',suma(num1,num2))
    print('resta:', resta(num1,num2) )
    print('división:', division(num1,num2) )
    print('multiplicación:', multiplicacion(num1,num2) )

def main ():
    num1, num2 = ingreso ()
    mostrar(num1, num2)

main()
'''

#ej 1.6 b - Tabla de multuplicar
'''
b) Pida un número natural n, imprimir su tabla de multiplicar.
Ej:
    > Ingrese un número: 3
    0
    3
    6
    9
    12
    15
    18
    21
    24
    27
    30
'''
'''
def tabla_de_multiplicar(n):
    for i in range (11):
        print(n*i)

def main():
    n = int( input('Ingrese un número: ') )
    tabla_de_multiplicar(n)
main()
'''

# ej 1.7 - 100 print
'''Escribir un programa que le pida una palabra al usuario, para luego imprimirla 100 veces, 
en una única línea, con espacios intermedios. 
Ayuda: Investigar acerca del parámetro end de la función print.'''
'''
def impresora(p):
    for i in range (5):
        print(p, end =' ')

def main():
    p = input( 'ingrese una palabra: ')
    impresora(p)

main()
'''