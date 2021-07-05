#ej3) 
'''
Arsène Lupin, el dueño de la panadería Arsène Lupin Baguettes, está teniendo graves problemas en el 
cobro de ventas con sus clientes. Tanto es así, que no le quedó más que hablar con el departamento 
de Computación de la Facultad de Ingeniería de la UBA para pedir por favor que alguno de nuestros 
programadores le confeccione algún sistema de administración rentable y que cumpla el régimen de 
buenas prácticas dictado en la clase de Algoritmos y Programación I.
Sabiendo que la panadería cuenta con un menú limitado, a saber:
- Baguette Clásica $250
- Baguette Rellena $350
- Baguette Vegana $250
- Baguette con Muzzarella (a la pizza) $500
- 1 Merlot $300
- 1 Vin rosé $300
- 1 Borgoña blanc $550
Se pide un menú que permita:
a. El ingreso de Pedidos por Cliente. En caso de que el Cliente no exista en los registros, deberá 
darse de alta según: Nombre y Apellido y DNI.
b. El ingreso del pago de un pedido por parte de un Cliente.

c. Top 5 de las deudas más importantes ordenadas descendentemente por monto. Se deberá imprimir:
[Nombre y Apellido] - [Monto de Deuda]

d. La impresión de un reporte donde indique en cuantos pedidos se encontró cada artículo. Se deberá imprimir
[Nombre del Artículo] - [Cant. Pedidos solicitados].

e. Indicar el % de pedidos superiores a $1000
'''
#estructura abm:
    # menu = {                              #guardo el nomrbe de los articulos
    #               {id_articulo:
    #                           nombre:
    #                           precio:             
    #                              
    #            }    
    #           
    #                   }
    # pedidos = {                           # guardo los pedidos con su respectivo total
    #            {id_pedido: id_cliente:
    #                        razon_social:
    #                        articulos_pedidos= {id_articulo: cantidad}                                               
    #                        total   
    #                     }                                      
    #               } 
    #
    # clientes = {'id_cliente':                   #Guardo las deuddas de cada cliente con su nombre
    #                           razon_social
    #                           deuda        
    #                                           }

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

def pedidos_por_articulo(pedidos, menu) -> None:
    pedidos_por_cada_articulo = dict()

    for id_articulo in menu.keys():
        for id_pedido in pedidos.keys():
            if id_articulo in pedidos[id_pedido]["articulos_pedidos"].keys():
                if id_pedido not in pedidos_por_cada_articulo:
                    pedidos_por_cada_articulo[id_articulo] = 1
                else:
                    pedidos_por_cada_articulo[id_articulo] +=1

    print(pedidos_por_cada_articulo)
    for key, value in pedidos_por_cada_articulo.items():
        print(key, value) 
            

def mostrar_pedido_mas_caro(pedidos:dict) -> None: 
    #ojo muy incompleto y tiene datos q no corresponden!!
    precio_pedidos = [] #creo lista donde guradare los pedidos y sus precios
    
    for pedido, datos in pedidos.items():
        precio_pedidos.append( [datos['total_pedido'], pedido ])
    
    precio_pedidos.sort(reverse =  True, key= lambda tratamiento: tratamiento[0] ) 
        
    max_precio =  max(precio_pedidos)
    print()    
    
    print('pedido (s) mas caro')
    for pedido in precio_pedidos:
        if pedido[0] == max_precio[0]:
            print(f'El pedido {pedido[1]} dio una ganancia de {pedido[0]} $')   
                   
def mostrar_nombre_clientes(clientes:dict)->None:
    for cliente, datos in clientes.items():
        llave = "razon_social"
        llave_2 = "deuda"
        print(f"{cliente} - {datos[llave]} - {datos[llave_2]}")


def mostrar_nombre_articulos(menu)->None:
    for articulo, datos in menu.items():
        llave = "nombre"
        print(f"{articulo} - {datos[llave]}")


def mostrar_deudas(clientes: dict) -> None:
    deudas_por_cliente = [] 
    
    for clientes, datos in clientes.items():
        deudas_por_cliente.append( [datos['deuda'], datos['razon_social'] ] )
    
    deudas_por_cliente.sort(reverse =  True, key= lambda deudor: deudor[0] ) 

    for deudor in deudas_por_cliente:
        print(f'{deudor[1]} - {deudor[0]}')    
              

def pagar_pedido(clientes:dict)->None:
    #(hago trampita y paga su deuda independientemente del pedido), es decir puede pagar un pedido del
    #por la mitad
    print('CLIENTES\n')
    mostrar_nombre_clientes(clientes)

    id_cliente = input('Ingrse el id del cliente cuya deuda quiere pagar: ')
    pago = int(input('ingrese cuanto desea pagar de su deueda: '))
    for cliente in clientes.keys():
        if cliente == id_cliente:
            clientes[cliente]["deuda"] -= pago 

def alta_pedido(pedidos:dict, clientes:dict,  menu: dict,) -> None:
    
    #cada pedido es un dict
    pedido = dict()  
    id_pedido = int(input("Ingrese el id del nuevo pedido: ")) 

    cliente = {}

    #datos cliente
    id_cliente = input("Ingrese id del cliente: ")   
    razon_social = input("Ingrese el nombre y apellido del cliente: ")    
    
    articulos_pedidos = {}

    print('lista de articulos disponibles\n')
    mostrar_nombre_articulos(menu)
    
    print('Ingreese el articulo que desea comprar')

    continuar_ingreso = True
    
    total_pedido = 0
    while continuar_ingreso:
        
        id_articulo = int(input("Ingrese el id del articulo: "))
        cantidad = int(input(f"Ingrese la cantidad de articulos de ese tipo: ") )

        articulos_pedidos[id_articulo] = cantidad

        total_pedido += cantidad * menu[id_articulo]["precio"]

        corte = input("¿Quiere seguir ingresando articulos <s/n>? ")
        if corte != "s":
            continuar_ingreso = False
        
        else:
            continuar_ingreso = True

    #Guardo los datos del pedido en pedidos
    pedido["id_cliente"] = id_cliente
    pedido["razon_social"] = razon_social
    pedido["articulos_pedidos"] = articulos_pedidos #diccionario con pedidos y sus cant
    pedido["total_pedido"] = total_pedido   #total del pedio

    #Convierto el pedido: pedido[id_pedido] en clave de la tabla pedidos
    pedidos[id_pedido] = pedido

    #guardo los datos del cliente en cliente (aprovecho y le cargo su deuda)

    if id_cliente not in clientes:
        clientes[id_cliente] = cliente
        cliente["razon_social"] = razon_social
        cliente["deuda"] = total_pedido
    else:
        clientes[id_cliente]["deuda"] += total_pedido


def abm_panaderia(opc, pedidos:dict, clientes: dict, menu:dict):
    '''
    #PRE: Recibe la opc elegida en el menu  y las estructura ppal 
    utilizada para guardar y operar con el ABM

    #POST: Redirige a la funcion q corresponda xa hacer lo pedido x el usuari
    '''
      
    if opc == 1:
        alta_pedido(pedidos, clientes, menu)

    elif(opc == 2):
        pagar_pedido(clientes)
    
    elif(opc == 3):
        mostrar_deudas(clientes)  

    elif(opc == 4):
        mostrar_pedido_mas_caro(pedidos) #muestra nuevos y viejos

    elif(opc ==5):
        pedidos_por_articulo(pedidos, menu)

#MAIN XA ABM
def main():
    cerrar = False
       
    #estructura abm:
    # menu = {                              #guardo el nomrbe de los articulos
    #               {id_articulo:
    #                           nombre:
    #                           precio:             
    #                              
    #            }    
    #           
    #                   }
    # pedidos = {                           # guardo los pedidos con su respectivo total
    #            {id_pedido: id_cliente:
    #                        razon_social:
    #                        articulos_pedidos= {id_articulo: cantidad}                                               
    #                        total   
    #                     }                                      
    #               } 
    #
    # clientes = {'id_cliente':                   #Guardo las deuddas de cada cliente con su nombre
    #                           razon_social
    #                           deuda        
    #                                           }
    
    
    menu ={   

        1: {
            "nombre": "Baguette Clásica",
            "precio": 250.0,
        },
        
        2: {
            "nombre": "Baguette Rellena",
            "precio":  350.0,
        
        },
        3: {
            "nombre": "Baguette vegana",
            "precio": 250.0,
        
        },
        4: {
            "nombre": "Baguette con Muzzarella (a la pizza)",
            "precio": 500,
        
        },
        5: {
            "nombre": "1 Merlot",
            "precio": 300.0,
        },  
        6: {
            "nombre": "1 Vin rosé",
            "precio": 300.0,      
            },       
        7: {
            "nombre": "1 Borgoña blanc",
            "precio":  550.0,      
            } 
    }
    clientes = {}
    pedidos = {}


    while not cerrar:

        #MENU DE OPCIONES DEL ABM:
        print('''
Bienvenido Arsène Lupin Baguette, ¿Que desea hacer? 
1.Dar de ALTA un pedido (si no esta el cliente se da de alta el cliente)
2.Ingreso del pago de un pedido     
3.Mostrar deudas mas importantes ordenadas por monto
4.Mostrar el pedido cuya valorizacion sea la mayor
5.Mostrar pedidos por articulo
7.Cerrar el programa (MUESTRA todo!!1) ''')

        opc = int( validar_opcion(0,7, 'Ingrese una opcion: '))

        if opc != 7:
            abm_panaderia(opc, pedidos, clientes, menu)
        
        else:
            mostrar_nombre_articulos(menu)
            mostrar_nombre_clientes(clientes)
            for pedido, datos in pedidos.items():
                print(f'\n{pedido}:')
                for llave in datos:
                    print(f'{llave}: {datos[llave]}')
            cerrar = True


main()