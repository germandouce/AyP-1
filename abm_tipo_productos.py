#ejemplo de modelacion



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
    


def mostrar_pedido_mas_caro(pedidos:dict) -> None: 
    
    precio_pedidos = [] #creo lista donde guradare los pedidos y sus precios
    
    for pedido, datos in pedidos.items():
        precio_pedidos.append( [datos['total_pedido'], pedido ])
    
    precio_pedidos.sort(reverse =  True, key= lambda tratamiento: tratamiento[0] ) 
        
    max_precio =  max(precio_pedidos)
    print()    

    # for pedido in cantidad_de_tratamientos:
    #     print(f'{trata[1]} fue solicitado {trata[0]} veces')                
    # print()
    
    print('pedido (s) mas caro')
    for pedido in precio_pedidos:
        if pedido[0] == max_precio[0]:
            print(f'El pedido {pedido[1]} dio una ganancia de {pedido[0]} $')   
                   

#FUNCION PARA MOSTRAR NOMBRE DE UNA CLAVE SU VALOR DE UN DICT DE DICT
def mostrar_nombre_articulos(articulos)->None:
    for articulo, datos in articulos.items():
        llave = "desc"
        print(f"{articulo} - {datos[llave]}")


def mostrar_todos_los_pedidos(pedidos: dict, articulos: dict) -> None:   #mostra todos los cursos (ordenados)
    for pedido, datos in pedidos.items():
        print(f'\n{pedido}:')
        for llave in datos:
            print(f'{llave}: {datos[llave]}')


def mostrar_pedidos_cuenta_dada(pedidos: dict) -> None:   
    
    id_cliente = input('Ingrse el id del cliente cuyos pedidos quiere mostrar: ')

    for pedido in pedidos.values():
        if pedido["id_cliente"] == id_cliente:
            for art, datos in pedido["articulos_pedidos"].items():
                print(f'{art}: {datos}')
        print('total pedido en $:',pedido["total_pedido"])

#FUNCIONES DE ALTA - BAJA - MODIFICACION
def alta_pedido(articulos:dict, clientes:dict,  pedidos: dict,) -> None:
    
    pedido = dict()  
    id_pedido = int(input("Ingrese el id del nuevo pedido: ")) 


    id_cliente = input("Ingrese id del cliente: ")   
    razon_social = input("Ingrese el nombre y apellido del cliente: ")    
    
    articulos_pedidos = {}

    print('lista de articulos disponibles\n')
    mostrar_nombre_articulos(articulos)
    
    print('Ingreese el articulo que desea comprar')

    continuar_ingreso = True
    
    total_pedido = 0
    while continuar_ingreso:
        
        id_articulo = int(input("Ingrese el id del articulo: "))
        cantidad = int(input(f"Ingrese la cantidad de articulos de ese tipo: ") )
        color = input("Ingrese el color del los articulos: ")

        articulos_pedidos[id_articulo] = [cantidad, color]

        total_pedido += cantidad * articulos[id_articulo]["precio"]

        corte = input("¿Quiere seguir ingresando articulos <s/n>? ")
        if corte != "s":
            continuar_ingreso = False
        
        else:
            continuar_ingreso = True

    #Guardo los datos del pedido
    pedido["id_cliente"] = id_cliente
    pedido["razon_social"] = razon_social
    pedido["articulos_pedidos"] = articulos_pedidos #dicciionario con pedidos 
    pedido["total_pedido"] = total_pedido   #total del pedio

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
        mostrar_pedido_mas_caro(pedidos) #muestra nuevos y viejos

    elif(opc == 5):
         mostrar_monto_total_tratamientos_vendidos(tratamientos,articulos) #muestra total vendido en sopes

    elif(opc == 6):
        mostrar_todos_los_pedidos(pedidos,articulos) #muestra tratamiento mas solicitado entre todos


#MAIN XA ABM
def main():
    cerrar = False
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

    #estructura abm:
    # articulos = {
    #               {id_articulo:
    #                           desc:
    #                           color:             
    #                           cantidad: 
    #                           precio:    
    #            }    
    #           
    #                   }
    # pedidos = { 
    #            {id_pedido: id_cliente:
    #                        razon_social:
    #                        articulos_pedidos= {id_articulo} [cantidad, color]                                               
    #                        total   
    #                     }                                      
    #               } 
    #
    # clientes = {'id': razon_social}

    
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
6.Listar todos los pedidos cargados
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
