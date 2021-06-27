'''
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

