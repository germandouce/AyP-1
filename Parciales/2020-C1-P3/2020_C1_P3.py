#ej 1)
#a) 32442,51(base 6) -> 4490,86111(base 10) (TFN)

#b) 6658,633 (base 10) -> 10117,5624 (base 9) (BM/MD  con error menor a 10^-4)  

#c) 1223,24 (base 4) -> 6B,B (base 16) (BP mirando tablas! 4->16) NO USAR TFN Y MS/DS Xq tira error!
#Y ademas es muuy largo)

#ej 2) 15:12 - 15:45 33 mins
'''
Escriba una función que dada una lista de denominaciones de billetes de la moneda corriente de un 
país, permita descomponer un importe otorgado por el usuario en las cantidades correspondientes a 
cada una de las denominaciones cual si fuera un cajero automático y suponiendo que siempre elige 
otorgar billetes del mayor valor posible. La función debe controlar que el importe sea factible de 
ser descompuesto y devolver un diccionario con la descomposición. 
Construya el programa principal donde utiliza dicha función. 
Ej: Lista = [10,20,50,100,200,500,1000] 
Valor = 1690  Diccionario = {10:0,20:2,50:1;100:1;200:0;500:1;1000:1}
'''
'''
def validar_opcion(opc_minimas: int, opc_maximas: int, texto: str = '') -> str:
    """
    PRE: "opc_minimas" y "opc_maximas" son dos números enteros que 
    simbolizan la cantidad de opciones posibles.

    POST: Devuelve en formato string la var "opc" con un número 
    entero dentro del rango de opciones.
    """
    opc = input("{}".format(texto))
    while not opc.isnumeric() or int(opc) > opc_maximas or int(opc) < opc_minimas:
        opc = input("Por favor, ingrese una opcion valida: ")
    
    return opc


def ingreso_billetes()->list:
    lista_billetes = list()
    print('ingrese billetes')

    cortar = False
    while not cortar: 
        b = input('Ingrese billete: ')
        
        while not b.isnumeric():
            b = input('Ingrese un billete de denominacion numerica: ')
        
        b = int(b)
        
        lista_billetes.append(b)

        opc = int( validar_opcion(0,1,'Desea ingresar mas billetes? 1 - 0 - no: ') )
        if opc == 0: 
            cortar = True
    
    return lista_billetes


def cajero(lista: list) -> dict:
    importe = input('ingerse un importe: ')
    lista.sort(reverse=True)
    
    print(lista)
    
    while not importe.isnumeric():
        importe = input('Ingrese un billete de denominacion numerica: ')
        
    importe = int(importe)

    se_puede = False        #asumo q inicialmente  no se puede descomponer
    for billete in lista:
        if importe % billete == 0: # con q un solo billete divida enteramente al importe
            se_puede = True
    
    if se_puede:
        descomp = dict()
        for billete in lista:
            if importe >= billete:
                cantidad = importe//billete
                descomp[billete] = cantidad
                importe = importe%billete

    else:
        descomp = dict()
        print('no es posible descomponer dicho importe')

    return descomp

def main()-> None:
    lista_billetes = ingreso_billetes()
    print( cajero(lista_billetes) )     #devuelvo {denominacion: cantidad_de_billetes}

main()
'''

#ej 3) # 19:05 -
'''
Para  celebrar  el  Día  del  Niño,  en  una  plaza  de  gran  extensión,  se  ha  construido  un  
caminito  de  baldosas  cuadradas  de  hormigón  de  3  colores:  blanco,  gris  y  negro.  El  
caminito  no  tiene  bifurcaciones  y  para  que  quedase  más  vistoso,  se  cuidó  que  las  
baldosas contiguas tuvieran ***diferente color***. 

Lamentablemente el caminito ha perdido muchas de sus baldosas, ya que debieron ser quitadas  para  
realizar  un  complejo  tendido  de  cañerías. La  figura  muestra  el  estado  actual del caminito. 

Los  huecos  dejados  por  las  baldosas  removidas  se  muestran  cuadriculados.  Quienes  deben  
reconstruir  el  caminito  desean  dejarlo  tal  como  estaba,  pero  no  se  llevó  el  registro de
los colores y ubicaciones de las baldosas removidas. Por lo tanto, se decide reconstruirlo
respetando  las  que  quedaron  siguiendo  la  consigna  original  de  que  las  contiguas no queden
del mismo color, comprando las baldosas nuevas que hagan falta.Para ayudar en la reconstrucción se 
pide que escriba una 
función caminito(BALDOSAS)que  devuelva  un  posible  diseño  para  reconstruir  el  caminito y  
que  también  lo  escriba  por pantalla. Su  parámetro  es  “baldosas”:  una  PALABRA  conteniendo  
caracteres  ‘B’  (blanco),  ‘N’  (negro), ‘G’ (gris) o ‘R’ (removido) separadas con coma “,” 
describiendo la vereda en su estado actual, esperando que sustituyas las ‘R’ por las letras que 
describan los colores de tu propuesta. La longitud de la palabra no es conocida.Tu propuesta de 
caminito deberá ser devuelta por la función y  escrita por pantalla la palabra con la propuesta.

Ejemplo:El parámetro BALDOSAS describe la figura y contiene: R,G ,N ,R,R,N,R ,R,R,B,R,N 
El programa deberá escribir por pantalla una línea como la siguiente BGNBGNGBGBGN
'''
#"baldosas" una palavra = es str
#CASOS BORDE:
#
'''
import random

def caminito(baldosas:str)->str:
    baldosas_splitted = baldosas.split(',')
    while 'R' in baldosas_splitted:
        for b in range( len(baldosas_splitted) ):
            if baldosas_splitted[b] == 'R':
                if baldosas_splitted[b] == 0 and baldosas_splitted[b+1]!='R': #si es la primera me fijo en la contigua
                    baldosas_splitted[b] = 'B'
                elif baldosas_splitted[b] == baldosas_splitted[ len(baldosas_splitted)-1]: 
                    #si es a ultima solo miro la anterior
                    if baldosas_splitted[b-1] =='B':
                        baldosas_splitted[b] = random.choice(['N','G'])
                    elif baldosas_splitted[b-1] =='N':
                        baldosas_splitted[b] = random.choice(['G','B'])
                    if baldosas_splitted[b-1] =='G':
                        baldosas_splitted[b] = random.choice(['N','B'])
                else: # 0 < b < len(baldosas_splitted) -1 
                    if baldosas_splitted[b+1] =='B' and baldosas_splitted[b-1] == 'N':
                        baldosas_splitted[b] = 'G'
                    elif baldosas_splitted[b+1] =='N' and baldosas_splitted[b-1] == 'B':
                        baldosas_splitted[b] = 'G'
                    elif baldosas_splitted[b+1] =='G' and baldosas_splitted[b-1] == 'N':
                        baldosas_splitted[b] = 'B'
                    elif baldosas_splitted[b+1] =='N' and baldosas_splitted[b-1] == 'G':
                        baldosas_splitted[b] = 'B'
                    elif baldosas_splitted[b+1] =='G' and baldosas_splitted[b-1] == 'B':
                        baldosas_splitted[b] = 'N'
                    elif baldosas_splitted[b+1] =='B' and baldosas_splitted[b-1] == 'G':
                        baldosas_splitted[b] = 'N'
    return baldosas_splitted

baldosas = 'R,G,N,R,R,N,R,R,N,R,R,B' 
print(caminito(baldosas))

  
#                     no_2 = baldosas_splitted[b+1]
#                     conj = set()
#                     conj.add(no_1)
#                     conj.add(no_2)
#                     est = {'B','N','G'} - conj
#                     baldosas_splitted[b] = est
'''