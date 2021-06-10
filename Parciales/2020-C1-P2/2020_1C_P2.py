#2020 1C P2
#07/07/20

#Ej 4 
#   19:35 - 
'''
4) Una importante empresa de cosmética nos solicita realizar un programa para la automatización de su 
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
def datos_produccion(pedidos, tanques) -> None:
    #cremas mas producida                #pedidos = {codigo_crema: {tipo_envase: cantiad_envases} }
    total_cremas = []                   #tanques = {codigo_crema : [nombre, cantidad] }
    for codigo_crema in pedidos:
        total_crema= 0
        for tipo_envase in codigo_crema.values():
            total_crema += tipo_envase.values()*tipo_envase
        total_cremas.append( [codigo_crema, total_crema] )

    max_cant = total_cremas[0][1]
    crema_mas_produc = ''
    for i in range( len(total_cremas) ):
        if total_cremas[i][1] >= max_cant:
            crema_mas_produc = total_cremas[i][0]
    
    for codigo, values in tanques:
        if codigo == crema_mas_produc:
            print(values[0]) # = nombre

    print('crema_mas_produc:',crema_mas_produc)
    
    #envase mas producido
    todos_los_envases = []
    for codigo_crema in pedidos:
        total_envases_crema = 0
        for tipo_envase in codigo_crema.values():
            total_envases_crema += tipo_envase.values()
        todos_los_envases.append( [tipo_envase, total_envases_crema] )
    
    max_cant = todos_los_envases[0][1]
    envase_mas_produc = ''
    for i in range( len(todos_los_envases) ):
        if todos_los_envases[i][1] >= max_cant:
            envase_mas_produc = todos_los_envases[i][0]
    
    print('envase mas producido:', envase_mas_produc)

    #for i in range()
    #de baja


def cargar_pedidos(tanques) -> dict:
        
    pedidos: dict = dict()           
    basta = False
    while not basta:

        sin_cantidad = False
        while not sin_cantidad:
            codigo_crema = input('Ingrese codigo de crema a producir: ')
            
            print('ingrese envase 1- 300 2- 500 3- 1000')
            opc = int (input('')) 
            if opc == 1:
                tipo_envase = 300
            
            elif opc == 2:
               tipo_envase = 500
            else: 
                tipo_envase = 1000
        
            cantidad_envases = input('Ingrese numero de envase a producir: ')        
            
            total = cantidad_envases * tipo_envase

            if tanques[codigo_crema][1] <= total:
                if codigo_crema not in pedidos:     #si la crema no fue pedida
                    pedidos[codigo_crema] = dict()
                    pedidos[codigo_crema][tipo_envase] = cantidad_envases

                else:                               # si ya esta la crema chequeo el envase
                    if tipo_envase not in pedidos[codigo_crema]:
                        pedidos[codigo_crema][tipo_envase] = cantidad_envases
                    else:
                        pedidos[codigo_crema][tipo_envase] += cantidad_envases

                basta = int( input( 'Quiere ingresar otra crema? 1-si 0-no: ') )
                if basta == 0:
                    basta = True                    
            else:
                print('\nNo alcanza la materia prima ingrese de nuevo\n')
    
    return pedidos

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
    pedidos = cargar_pedidos(tanques)
    datos_produccion(pedidos, tanques)

main()