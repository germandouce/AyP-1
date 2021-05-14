#UNIDAD 2: Programas sencillos



#ej 2.1 - Ganancia
'''
Escribir una función que reciba una cantidad de pesos, una tasa de interés y un
número de años y devuelva el monto final a obtener. La fórmula a utilizar es:
Cn = C × (1 + x⁄100)^n
Donde C es el capital inicial, x es la tasa de interés y n es el número de años a calcular.
'''
'''
def ganancia(C, x, n):
    """
    ARG: C, x y n son ints
    RETURNS: Cn es un float
    """
    Cn = C * (1 + x/100)**n
    return Cn

def main():
    c = int(input('Ingrese monto: '))
    x = int(input('Ingrese tasa de interes: '))
    n = int(input('Ingrese años a calcular: '))
    print(ganancia(c,x,n))

main()
'''

#dj 2.2 - Ganancia de un cliente
'''
Utilizando la función del ejercicio anterior, escribir un programa que le pregunte al usuario la 
cantidad de pesos inicial, la tasa de interés y el número de años y muestre el monto final a obtener.

Ejemplo:

    > Ingrese la cantidad de pesos inicial: 15000
    > Ingrese la tasa de interes: 20
    > Ingrese el numero de anios: 2
    > El monto final a obtener es de: 21600.0
Tip: Recordar castear el valor recibido por el usuario (int(...), float(...), etc).
'''
'''
def ganancia(C, x, n):
    """
    ARG: C, x y n son ints
    RETURNS: Cn es un float
    """
    Cn = C * (1 + x/100)**n

    return Cn


def main():
    """
    Hace uso de la funcion `ganancia` recibiendo los datos de           entrada del usuario. 
    Muestra por pantalla el monto final a obtener.
    """
    c = int(input('Ingrese la cantidad de pesos inicial:: '))
    x = int(input('Ingrese la tasa de interes: '))
    n = int(input('Ingrese el numero de anios: '))
    print(f'El monto final a obtener es de: {ganancia(c,x,n)}')

main()
'''
#ej 2.3 - Conversor de temperaturas (Fahrenheit a Celsius)
'''
Escribir una función que convierta un valor dado en grados Fahrenheit a grados
Celsius. Recordar que la fórmula para la conversión es:

C = 5⁄9 × (F - 32)


Donde F es el valor a convertir en grados Fahrenheit.

Tip: Recordar utilizar paréntesis para garantizar el correcto órden de las operaciones aritméticas.
'''
'''
def fahrenheit_a_celsius(F):
    """
    DOC: Completar.
    """
    C = 5/9 * (F - 32)
    
    return C
'''

#ej 2.4 - Tabla de temperaturas
'''
Escribir un programa que utilice la función anterior para generar una tabla de
conversión de temperaturas, desde 0 °F hasta 120 °F, de 10 en 10.
Ejemplo:
0 °F |-17.77777777777778 °C
10 °F | -12.222222222222223 °C
20 °F | -6.666666666666667 °C
...
100 °F | 37.77777777777778 °C
110 °F | 43.333333333333336 °C
120 °F | 48.88888888888889 °C
Tip: Si se utiliza la función print con varios argumentos separados por , estos se imprimirán 
separados por espacios.'''
'''
def fahrenheit_a_celsius(F:int) -> float:
    """
    toma grados F y devuelve T en celsius
    """
    C = 5/9 * (F - 32)
    
    return C

def main() -> None:
    """
    Utiliza la funcion conversora para imprimir una tabla de conversión de temperaturas, 
    desde 0 °F hasta 120 °F, de 10 en 10.
    Por cada temperatura, se debe imprimir:
    f °F | c °C
    Donde `f` es el valor en grados Fahrenheit, y `c` su conversión en grados Celsius.
    """
    for f in range (0,130,10):
        print(f'{f} °F |',fahrenheit_a_celsius(f),'°C')
main()
'''
#ej 2.5 - Operaciones modulares
'''
a) Escribir una función es_impar que dado un número entero devuelva 1 si el mismo es impar y 0 si fuera par.
b) Escribir una función es_par que dado un número entero devuelva 0 si el mismo es impar y 1 si fuera par.
c) Escribir una función digito_de_unidad que dado un número entero devuelva el dígito de las unidades. Por ejemplo, para 153 debe devolver 3.
d) Escribir una función multiplo_10_inferior que dado un número devuelva el primer número múltiplo de 10 inferior a él. Por ejemplo, para 153 debe devolver 150.
Tip: Investigar como funciona el operador módulo (%).
'''
'''
def es_impar(n: int) -> bool:
    """
    Devuelve 1 si es impar y 0 si es par
    """
    es_impar = 1
    if n%2 == 0:
        es_impar = 0

    return es_impar


def es_par(n: int) -> bool:
    """
    Devuelve 0 si es impar y 1 si es par
    """
    es_par = 1
    if n%2 != 0:
        es_par = 0

    return es_par

def digito_de_unidad(n: int) -> int:
    """
    Hago trampa
    """
    n = str(n)
    n = int( n [(len(n)-1):] )
    return n

def multiplo_10_inferior(n: int) -> int:
    """
    devuelve el primer multiplo de 10 inferior a el
    """
    if n%10 == 0 :
        primero = (n // 10 - 1) * 10
    else:
        primero = ( n // 10) * 10
    
    return primero

def main():
    #print((es_impar(int(input()))))
    #print((es_par(int(input()))))
    print(digito_de_unidad(int(input())))    
    print(multiplo_10_inferior(int(input())))

main()
'''

#ej 2.6 - Imprimir Pares
'''
Escribir un programa que imprima todos los números pares entre dos números que se le pidan al usuario.
Ejemplo:
    > Ingrese el primer numero: 5
    > Ingrese el segundo numero: 10
    6
    8
    10
Tip: No olvidar llamar al main!
'''
'''
def imprimir_pares(inicio, fin):
    """
    imprime pares entre inicio y fin
    """
    for num in range (inicio, fin+1):
        if num%2 == 0:
            print(num)

def main():
    """
    El programa le pide dos numeros al usuario
    y luego imprime todos los pares entre ellos
    """
    n1 = int(input('ingrese primer par: '))
    n2 = int(input('ingrese primer par: '))
    imprimir_pares(n1,n2)

main()
'''

#ej 2.7 - Numeros triangulares
'''Escribir un programa que le pregunte al usuario un número n e imprima los primeros n números 
triangulares, junto con su índice.
Los números triangulares se obtienen
mediante la suma de los números naturales desde 1 hasta n.

Por ejemplo:

    > Ingrese un numero: 5
    1 - 1
    2 - 3
    3 - 6
    4 - 10
'''
'''

def calcular_numero_traingular(n):
    """
    n es un entero ingresado por el usuario, no devuelve nada, solo imprime lo pedido
    """
    for num_nat in range(1,n+1):
        num_triang = 0
        for num_suma in range(1,num_nat+1):
            num_triang += num_suma
        print(num_nat,'-',num_triang)

def main():
    """
    El programa le pide al usuario un numero n 
    e imprime por pantalla los primeros n numeros triangulares.
    """
    n = int(input('Ingrese un numero: '))
    calcular_numero_traingular(n)

main()
'''