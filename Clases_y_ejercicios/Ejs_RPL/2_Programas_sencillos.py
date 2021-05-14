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