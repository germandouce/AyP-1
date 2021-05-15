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