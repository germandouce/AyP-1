#2020 1C P2
#07/07/20
#total ej num + 2 cortitos = 1 hr 5 min
# me quedan 55 min xa ABM (u 1hr 15 min si tengo suerte y dan mais tempo) 

#ej 1 + 2 ) 17:00 - 17:25 -> 25 min
'''
#ej 1)
 
#21 digits
#1101001111011,10100101 (base 2) = 1A7B, A5 (base 16)

#ej 2)
#2019(base 10) = 133203 (base 4)
#2019(base 10) = 11111100011 (base 4)
'''                 
#ej 3) 16:22 - 176:27 -> 5 min (10 min x enunciado raro..)
#(ya lo hice una vez)
'''
3) Se pide realizar una función que devuelva el número entero más pequeño de un listado ingresado 
por el usuario, tal que la suma de los N números exceda un valor pasado por parámetro en la función.
'''
'''
# def maspeq(max:int)->int:
#     suma=0
#     lista=[]
#     while suma<max:
#         n=int(input("Ingrese un numero entero: "))
#         suma+=n
#         lista.append(n)
#     return min(lista)

# print(maspeq(12))

def minimo(limite):
    sum = 0
    numeros: list = list()
    
    while sum <= limite:
        num =  int(input('Ingrese un numero: '))
        sum += num
        numeros.append(num)
    
    minimo = min (numeros)

    return minimo

print(minimo(12))
'''

#Ej 4 
#   19:35 - 23:30 --> 4horas XDN 'T 
#   13:30 - 14:52 --> 1:22 min XD
'''
Una importante empresa de cosmética nos solicita realizar un programa para la automatización de su 
producciónde cremas.  La línea de producción consta de 5 tipos de cremas (Humectante clásica {cod.100},  
Antiage colageno {cod.200},  Facial con UV {cod.300},  Desmaquillante{cod.400},  Vitamina A {cod. 10}) 
y   3 envases (200 cm3,  500cm3 y 1000 cm3).
El usuario comenzará introduciendo la cantidad de cm3 de 
cada tipo de crema disponible en la fábrica (estos  almacenados en 5 grandes tanques cisternas). 
están
Posteriormente el sistema le solicitará al usuario: -Ingresar  la  crema  para  ser  utilizados  en  la  
línea  de  producción (se  debe  ingresar  por  código),  por  una  cuestión de evitar contaminación en 
la línea de producción,  sólo se podrá procesar una crema a la vez.
-Cantidad y tipo de envases a utilizar por cada cremaEl sistema deberá determinar si alcanza la cantidad
de materia prima (cremas) en cada tanque para procesar lo pedido por el usuario
a)en el caso que NO se 
pueda, deberá solicitar nuevamente que se ingresen los datos
b)en caso que SI se pueda, deberá indicar: 

-¿Cuál fue la crema que más se produjo (mostrar código y nombre de la crema)
-Cuál es el envase que más se produjo sobre el total de tipos de cremas? 
-Y el sobrante en cada tanque por tipo de crema

Obs.
 
 -El programa deberá tener al menos 2 
 funciones.
 -Se deberá contemplar alguna estructura que permita guardar el código de color y el nombre
'''
'''
#pedidos = {codigo_crema: cantidad }
#tanques = {codigo_crema : [nombre, cantidad] }
#envases = {tipo_envase: cantidad_de_envases}
def datos_produccion(pedidos, envases, tanques) -> None:
    #cremas mas producida               
    cantidades_produc = list()

    for cantidad in pedidos.values():
        cantidades_produc.append(cantidad) 
    
    max_cant_produc = max(cantidades_produc)

    crema_mas_produc=''
    for crema, cantidad in pedidos.items():
        if cantidad == max_cant_produc:
            crema_mas_produc = crema
    
    print('las crema mas producida fue', tanques [crema_mas_produc][0],
    'con un total de',max_cant_produc,'cm3' )

    #envase mas producido
    envases_produc = list()

    for cantidad in envases.values():
        envases_produc.append(cantidad) 
    
    max_envase_produc = max(envases_produc)
       
    envase_mas_produc = ''
    for tipo_envase, cantidad_de_envases in envases.items():
        if cantidad_de_envases == max_envase_produc:
            envase_mas_produc = tipo_envase

    print('El envase mas producido fue el de', envase_mas_produc, 'cm3'),    
    
    #sobrante en tanques                            #pedidos = {codigo_crema: cantidad }
    sobrante_por_tanque = []
    for codigo_crema, cantidad in pedidos.items():      #tanques = {codigo_crema : [nombre, cantidad] }
        sobrante = tanques[codigo_crema][1] - cantidad
        sobrante_por_tanque.append( (tanques[codigo_crema][0],sobrante) )
    
    print('crema  sobrante en cm3')
    for sobra in sobrante_por_tanque:
        print(sobra[0].ljust(10), sobra[1])


def cargar_pedidos(tanques:dict) -> dict:

    pedidos: dict = dict()
    envases: dict = dict()

    basta = False
    while not basta:
        
        print('tanques')
        print(tanques)

        codigo_crema = int(input('Ingrese codigo de crema a producir: '))
            
        print('ingrese envase 1- 300 2- 500 3- 1000')
        opc = int (input('')) 
        if opc == 1:
            tipo_envase = 300
            
        elif opc == 2:
            tipo_envase = 500
        else: 
            tipo_envase = 1000
        
        cantidad_envases = int(input('Ingrese numero de envases a producir: '))        
            
        total_produc = cantidad_envases * tipo_envase

        if total_produc <= tanques[codigo_crema][1]:
            if codigo_crema not in pedidos:     #si la crema no fue pedida
                pedidos[codigo_crema] = total_produc       #pedidos = {codigo_crema: total }
            else:                               # si ya esta la crema chequeo el envase
                pedidos[codigo_crema] += total_produc
            
            if tipo_envase not in envases:
                envases[tipo_envase] = cantidad_envases
            else:
                envases[tipo_envase] += cantidad_envases
            
            opc = int( input( 'Quiere ingresar otra crema? 1-si 0-no: ') )
            if opc == 0:
                basta = True 

        else:
            print('\nNo alcanza la materia prima ingrese de nuevo\n')
        
        print(envases)
        print(pedidos)

    return pedidos, envases

def cargar_tanques() -> dict:
    tanques: dict = dict()

    tanques_llenos = 0

    while tanques_llenos < 5:
        nombre = input('Ingrese Nombre crema: ')
        codigo_crema = int( input(f'Ingrese codigo crema {nombre}: ') )
        cantidad = int ( input(f'Ingrese cantidad de crema {nombre}: ') )
        tanques [codigo_crema] = [nombre, cantidad]
        tanques_llenos += 1
    #print( cremas )
    return tanques


def main() -> None:
    
    tanques = cargar_tanques()
    pedidos,envases = cargar_pedidos(tanques)
    datos_produccion(pedidos,envases, tanques)

main()
'''

#ej 5) (ya lo habia hecho jeje) 
#16:31 - 16:59 (con detallesitos..) -> 28 min
'''
Escribir un programa que primero solicite una palabra al usuario y luego le permita al usuario 
ingresar 5 palabras. El sistema deberá calcular cuántas y cuáles palabras de las 5 ingresadas pueden
escribirse exactamente con las letras de la palabra ingresada al principio (utilizando todas las 
letras y sin repetir ninguna). 
Ej: Palabra inicial: CASO palabras
5 palabras: MAMA, CLASE, SACO, COSA, PEPE EL sistema deberá devolver 2 palabras (SACO y COSA)
'''
'''
def cinco_palabras()-> list:
    print('ingrese 5 palabras')
    
    palabras_a_chequear: list = list()
    for i in range(5):
        pal = input('Ingrese palalabra: ').lower()
        palabras_a_chequear.append(pal)
    
    print('palabras a chequear:',palabras_a_chequear)
    
    return palabras_a_chequear

def chequeo_palabras(palabras_a_chequear: list, pal_inicial:str)->list:    
    posibles=[]

    for palabra in palabras_a_chequear:
        vale = True
        for letra in pal_inicial:
            if palabra.count(letra) != pal_inicial.count(letra):
                vale = False
        if vale:
            posibles.append(palabra.upper())

    return posibles
     
def main()-> None:
    pal_inicial = input('ingrese una palabra: ').lower()
    palabras_a_chequear = cinco_palabras() 
    posibles = chequeo_palabras(palabras_a_chequear, pal_inicial)
    print('se pueden escribir:',posibles)
main()
'''