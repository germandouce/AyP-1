#ej 1) 
# a)    NUMERACION
#b)     NUMERACION

#ej2) TEXTIL
'''
'''
#ejemplo de modelacion

#Articulos = {'id'}: [desc, color, cant, precio]}
#clientes = {'id': razon_social}
#pedidos = {'id': [id_articulo, id_cliente, cantidad, color]}


#Articulos = {'id_articulo':
#                           desc:
#                           color:
#                           cant:
#                           precio:

#clientes = {'id': razon_social}


#pedidos = {'id': id_cliente: id_cliente
#                {articulos_de_pedido: id_artculo: [cantidad, color] }
#                  }

def validar_opcion(opc_minimas: int, opc_maximas: int, texto: str = '') -> str:
    #ej: opc = int (validar_opcion(1, 2, 'texto en str con pregunta') )
    """
    PRE: "opc_minimas" y "opc_maximas" son dos números enteros que 
    simbolizan la cantidad de opciones posibles."texto" es un parametro
    opcional con la pregunta xa el usuario

    POST: Devuelve en formato string la var "opc" con un número 
    entero dentro del rango de opciones.
    """
    opc = input("{}".format(texto))
    while not opc.isnumeric() or int(opc) > opc_maximas or int(opc) < opc_minimas:
        opc = input("Por favor, ingrese una opcion valida: ")
    
    return opc



#IMPRIMIR DATOS DE DICT
def mostrar_tabla(tabla : dict) -> None:
    for llave, dato in tabla.items():
        print(f"{llave}: {dato}")


#FUNCIONES XA MOSTRAR DATOS A USUARIO
def mostrar_tratamiento_pacientes_nuevos(pacientes:dict, tratamientos: dict) -> None:  
    
    print('Tratamiento mas solicitado por pacientes nuevos')
    
    tratamientos_pacientes_nuevos = {}
    
    for paciente in pacientes.values():
        if paciente['consultas'] == 1:
            for tratamiento, cantidad in paciente['tratamientos_realizados'].items():
                if tratamiento not in tratamientos_pacientes_nuevos:
                    tratamientos_pacientes_nuevos[tratamiento] = cantidad
                else:
                    tratamientos_pacientes_nuevos[tratamiento] += cantidad   

    max_cantidad = 0
    for cant in tratamientos_pacientes_nuevos.values():
        if cant> max_cantidad:
            max_cantidad = cant
    
    llave = 'nombre'
    for trat, cant in tratamientos_pacientes_nuevos.items():
        if cant == max_cantidad:
            print(f'El tratamiento mas solicitado fue {tratamientos[trat][llave]}, {cant} veces ')
    


def mostrar_pedido_mas_caro(pedidos:dict, articulos:dict) -> None: 
    
    articulos_por_pedido = {} #creo lista donde guradare los articulos pedidos y su cant
                                #articulos_por_pedido : [id_articulo, cant]
    for pedido, datos in pedidos.items():                                
        for articulo in datos['articulos_de_pedido']:
            if pedido not in articulos_por_pedido:      
                articulos_por_pedido[pedido]= [ pedido['articulo_de_pedido'], pedido['articulo_de_pedido'][0] ]
            else: 
                articulos_por_pedido[pedido][0].append( pedido['articulo_de_pedido'])
                articulos_por_pedido[pedido][1].append (pedido['articulo_de_pedido'])
    
    precio_por_pedido = []
    for id_articulo, datos in articulos.items():
        for pedido in articulos_por_pedido:
            if id_articulo == articulos_por_pedido[0]:
                precio_por_pedido.append(pedido, articulos_por_pedido[1]*datos["precio"])

    print(precio_por_pedido)
    #max_cantidad =  max(cantidad_de_tratamientos)
    # print()    

    # for trata in cantidad_de_tratamientos:
    #     print(f'{trata[1]} fue solicitado {trata[0]} veces')                
    # print()
    
    # print('tratamiento (s) mas solicitado')
    # for trata in cantidad_de_tratamientos:
    #     if trata[0] == max_cantidad[0]:
    #         print(f'{trata[1]} fue solicitado {trata[0]} veces')                

#FUNCION PARA MOSTRAR NOMBRE DE UNA CLAVE SU VALOR DE UN DICT DE DICT
def mostrar_nombre_articulos(articulos)->None:
    for articulo, datos in articulos.items():
        llave = "desc"
        print(f"{articulo} - {datos[llave]}")


def mostrar_monto_total_tratamientos_vendidos(tratamientos: dict) -> None:   #mostra todos los cursos (ordenados)
    #cursos = sorted(cursos)        
    monto_total = 0
    for tratamiento in tratamientos.values():
        monto_total += tratamiento['cantidad']*tratamiento['costo']
    
    print(f'Te hiciste unos {monto_total} $ en total entre todos los tratamientos')

def mostrar_pedidos_cuenta_dada(pedidos: dict) -> None:   
    
    id_cliente = input('Ingrse el id del cliente cuyos pedidos quiere mostrar: ')

    for pedido in pedidos.values():
        if pedido["id_cliente"] == id_cliente:
            print (pedido['articulos_de_pedido'])


#FUNCIONES DE ALTA - BAJA - MODIFICACION
def alta_pedido(articulos:dict, clientes:dict,  pedidos: dict,) -> None:
    
    pedido = dict()  
    id_pedido = int(input("Ingrese el id del nuevo pedido: ")) 
    
    #Pido datos del pedido y el cliente
    id_cliente = input("Ingrese id del cliente: ")   
    razon_social = input("Ingrese el nombre y apellido del cliente: ")    

    articulos_de_pedido = dict()    #articulos_de_pedido ={id_articulo: [cantidad, color] }
    
    print('lista de articulos disponibles')
    mostrar_nombre_articulos(articulos)

    
    print('Ingreese el articulo que desea comprar')

    continuar_ingreso = True
    
    while continuar_ingreso:
        id_articulo = int(input("Ingrese el id del articulo: "))
        cantidad = int(input(f"Ingrese la cantidad de articulos de ese tipo: ") )
        color = input("Ingrese el color del los articulos: ")

        articulos_de_pedido[id_articulo] = [cantidad, color] # dentro del dict pedidos
            
        clientes[id_cliente] = razon_social   # dentro del dict independiente clientes

        corte = input("¿Quiere seguir ingresando articulos <s/n>? ")
        if corte != "s":
            continuar_ingreso = False
        
        else:
            continuar_ingreso = False

    #Guardo los datos en la tabla pedidos y en clientes  
    pedido["id_cliente"] = id_cliente
    pedido["articulos_de_pedido"] = articulos_de_pedido

    #Convierto el pedido: pedido[id_pedido] en clave de la tabla pedidos
    pedidos[id_pedido] = pedido


#FUNCIONES DE ALTA - BAJA - MODIFICACION
def alta_articulo(articulos:dict) -> None:
    
    articulo = dict()  
    id_articulo = int(input("Ingrese el id del articulo: ")) 
    
    desc = input("Ingrese descripcion del articulo: ")   
    color = input("Ingrese color del articulo: ")    
    cantidad = int(input("ingrese el stock(numero de articulos disponibles: "))
    precio =  int(input('ingrese precio del articulo: '))
        
    #Guardo los datos en la tabla articulos
    articulo["desc"] = desc
    articulo["color"] = color
    articulo["cantidad"] = cantidad
    articulo["precio"] = precio

    #Convierto el articulo: articulos[id_articulo] en clave de la tabla articulos
    articulos[id_articulo] = articulo


def modificar_pedido(pedidos: dict) -> None:
    
    #muestro pedidos
    for pedido, datos in pedidos.items():
        llave = "id_cliente"
        print(f"{pedido} - {datos[llave]}")
    
    opciones = list(pedidos.keys())
    
    opc = input('¿Que pedido desea modificar?: ')
    while ( not opc.isnumeric() ) or ( int(opc) not in opciones):
        opc = input('ingrse una opcion valida: ') 
    opc = int(opc)

    #muestro datos del pedido elegido xa modificar
    for dato, valor in pedidos[opc].items():
        print(dato, valor)
    
    #Pregunto q desea modificar
    entrada = input("¿Qué desea modificar del pedido?: ")
    if entrada == "articulos_de_pedido":
        id_articulo = int(input(f"Ingrese el articulo: "))
        pedidos[opc][entrada][id_articulo][0] = int(input(f"Ingrese la cantidad: "))
        pedidos[opc][entrada][id_articulo][1] = input(f"Ingrese el color: ")

    elif entrada == "id_cliente":
        pedidos[opc][entrada] = int(input('ingrese el nuevo id del cliente: '))


#DERIVADOR DE OPCIONES abm_cursos
def abm_textil (opc, articulos:dict, clientes: dict, pedidos: dict):
    '''
    #PRE: Recibe la opc elegida en el menu  y las estructura ppal 
    utilizada para guardar y operar con el ABM

    #POST: Redirige a la funcion q corresponda xa hacer lo pedido x el usuari
    '''
    if opc == 0:
        alta_articulo(articulos)
    
    elif opc == 1:
        alta_pedido(articulos, clientes, pedidos)

    if(opc == 2):
         modificar_pedido(pedidos)
    
    elif(opc == 3):
        mostrar_pedidos_cuenta_dada(pedidos)   #tratamiento mas elegido por pacientes

    elif(opc == 4):
        mostrar_pedido_mas_caro(pedidos, articulos) #muestra nuevos y viejos

    elif(opc == 5):
         mostrar_monto_total_tratamientos_vendidos(tratamientos) #muestra total vendido en sopes

    elif(opc == 6):
        mostrar_tratamiento_mas_solicitado(tratamientos) #muestra tratamiento mas solicitado entre todos


#MAIN XA ABM
def main():
    cerrar = False

    #Estructura a usar en el ABM xa guardar y modificar los datos {}, [] etc:
    # cursos = [["Aprende  a hacer tu propio compost",1 ,950],
    # ["Los niños y el medioambiente(para padres e hijes)",2,990],
    # ["Tu huerta orgánica",4,2500]]

    
    articulos = {}
    clientes = {}
    pedidos = {}


    while not cerrar:

        #MENU DE OPCIONES DEL ABM:
        print('''
Bienvenido  al sistema de registros de cursos de RumboCircular, ¿Que desea hacer? 
0.Dar de ALTA un articulo
1.Dar de ALTA un pedido
2.MODIFICAR uno de los pedidos  #modificar valores de las claves de dict dentro de dict        
3.Mostrar pedidos de una cuenta dada #Mostrar valores dentro del dict chico q cumplen x condicion
4.Mostrar el pedido cuya valorizacion sea la mayor
5.Mostrar monto total ganado con tratamientos vendidos  #muestra varios datos ESPECIFICOS SI LO HAY
6.Mostrar el tratamiento mas solicitado por los pacientes #mostrar datos segun el max de ellos
7.Cerrar el programa (MUESTRA todo!!1) ''')

        opc = int( validar_opcion(0,7, 'Ingrese una opcion: '))

        if opc != 7:
            abm_textil(opc, pedidos, clientes, articulos)
        
        else:
            mostrar_nombre_articulos(articulos)
            for pedido, datos in pedidos.items():
                print(f'\n{pedido}:')
                for llave in datos:
                    print(f'{llave}: {datos[llave]}')
            cerrar = True


main()

#ej 3) INGRESO  NUMEROS H/ LIMITE DEVUELVE MENOR
'''
Se pide realizar una función que devuelva el número entero más pequeño de un listado ingresado por 
el usuario, tal que la suma de los N números exceda un valor pasado por parámetro en la función
'''
'''
def menor_numero(limite: int) -> int:
    """
    PRE: Limite es el valor en el cual se corta el ingreso
    POST: Devuelve el menor de los numeros ingresados
    """
    print('Ingrese numeros')
    
    lista = list()
    sum = 0
    while sum <= limite:
        num = input('ingrese: ')
        while not num.strip('-').isnumeric() :
            num = input('Ingrese un numero valido: ')

        sum += int(num)
        lista.append( int(num) )
    
    minimo = min (lista)

    return minimo

print(menor_numero(12))
'''