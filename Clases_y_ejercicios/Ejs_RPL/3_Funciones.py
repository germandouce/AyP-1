#UNIDAD 2: Programas sencillos



#ej 3.1.a - Horas minutos segundos a segundos
'''Escribir una función que permita calcular:
a) La duración en segundos de un intervalo dado en horas, minutos y 
segundos.'''
'''
def duracion_a_segundos(h, m, s):
    """
    devuelve el intervalo en segundos    
    """
    h_seg = h*60*60
    m_seg = m*60
    seg = s
    t_total = h_seg + m_seg + seg
    
    return t_total
'''

#ej 3.1.b - Pasar segundos a horas minutos y segundos
'''Escribir una función que reciba una cantidad de segundos y devuelva tres valores indicando 
cuántas horas, minutos y segundos representan.
NOTA: Recordar que se puede devolver más de un valor. Por ejemplo, return a, b, c.
Ej:
> segundos_a_hms(1)
(0, 0, 1)
> segundos_a_hms(60)
(0, 1, 0)
> segundos_a_hms(65)
(0, 1, 5)
> segundos_a_hms(3600)
(1, 0, 0)
> segundos_a_hms(3660)
(1, 1, 0)
> segundos_a_hms(3725)
(1, 2, 5)'''
'''
def segundos_a_hms(segundos):
    """
    Devuelve tupla con hrs mins y segs
    """
    hrs = (segundos// 60) // 60
    mins = segundos % (60*60) // 60 #el resto nuca sera mayor a 3600, segs //60 = mins. 
    segs = segundos % 60 #ak tampoco. nunca mayor a 60     #como siempre menor a 3600, dividir x 60 siempre menor a 60 

    print(hrs, mins, segs)


def main():
    segundos_a_hms(int(input('seg: ')))
main()
'''

#ej 3.2 - Calculadora de tiempo
''' Escribir un programa que pida al usuario dos intervalos expresados en horas, minutos y segundos,
sume sus duraciones, y muestre por pantalla la duración total en horas, minutos y segundos.
NOTA: Reutilizá las funciones que escribiste para los ejercicios 3.1a y 3.1b.
Tip: ¡No olvides llamar a la función principal de tu programa!
Ej:
$ python3 main.py
Ingrese horas del primer intervalo: 1
Ingrese minutos del primer intervalo: 45
Ingrese segundos del primer intervalo: 37
Ingrese horas del segundo intervalo: 3
Ingrese minutos del segundo intervalo: 16
Ingrese segundos del segundo intervalo: 5
5 horas 1 minutos 42 segundos '''
'''
def duracion_a_segundos(h, m, s):
    """
    devuelve el intervalo en segundos    
    """
    h_seg = h*60*60
    m_seg = m*60
    seg = s
    t_total = h_seg + m_seg + seg
    
    return t_total

def segundos_a_hms(segundos):
    """
    Devuelve tupla con hrs mins y segs
    """
    hrs = (segundos// 60) // 60
    mins = segundos % (60*60) // 60 #el resto nuca sera mayor a 3600, segs //60 = mins. 
    segs = segundos % 60 #ak tampoco. nunca mayor a 60     #como siempre menor a 3600, dividir x 60 siempre menor a 60 

    print(hrs,'horas', mins,'minutos',segs,'segundos')
  
def intervalos():
    h = int(input('Ingrese horas del primer intervalo: '))
    m = int(input('Ingrese minutos del primer intervalo: '))
    s = int(input('Ingrese segundos del primer intervalo: '))
    h_2 = int(input('Ingrese horas del segundo intervalo: '))
    m_2 = int(input('Ingrese minutos del segundo intervalo: '))
    s_2 = int(input('Ingrese segundos del segundo intervalo: '))
    
    total_en_seg = duracion_a_segundos(h, m, s) + duracion_a_segundos(h_2, m_2, s_2)
    
    return total_en_seg

def main():
    segundos_a_hms( intervalos() )

main()
'''

#ej 3.3 - Maximo Producto entre dos numeros
'''
Escribir una función que dados cuatro números, devuelva el mayor producto de dos de ellos.
Por ejemplo, si recibe los números 1,5,-2,-4, debe devolver 8, que es el producto mas grande
que se puede obtener entre ellos (-2 * -4 = 8).
    > maximo_producto(1,5,-2,-4)
    8 
'''
#medio rancio pero funciona
'''
def max_producto(num1, num2, num3, num4):
    numeros=[] 
    numeros.append(num1)
    numeros.append(num2)
    numeros.append(num3)
    numeros.append(num4)
    print('productos')
    for i in range(len(numeros)):
        for restante in range (i+1,len(numeros)):
            producto = numeros[i]*numeros[restante]
            print(producto)
            if restante == 1:
                mayor = producto
            else:
                if producto >= mayor:
                    mayor = producto
    print('el mayor producto es',mayor)
    return mayor

def main():
    num1 = int(input())
    num2 = int(input())
    num3 = int(input())
    num4 = int(input())
    max_producto(num1, num2, num3, num4)

main()
'''