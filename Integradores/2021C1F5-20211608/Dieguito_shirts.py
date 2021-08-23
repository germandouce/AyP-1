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

def obtener_stock(ruta_arch:str)->dict:
    """
    ruta_arch = "stock.txt"
    """
    #ESTRUCTURA ELEGIDA:
    #SKU; Código interno; Equipo; Tipo; Año; Marca; Talle; Ingresadas; Vendidas; Costo promedio;
    #Precio de venta actual
    #{cod_int: [ [sku, equipo, tipo, anio, marca, talle, ingresadas, vendidas, costo_prom, precio_ac] ]}
    #Para cada clave codigo interno tengo una lista de camisetas cada una con sus datos

    stock = dict()
    try:
        with open(ruta_arch, "r") as arch:
            #next(archivo, None)
            for linea in arch:   
                #print(linea)             
                linea = linea.strip('\n')
                datos = linea.split(',') #txt
                
                cod_int = datos[1].strip()
                
                sku = datos[0].strip()
                equipo = datos[2].strip()
                tipo = datos[3].strip()
                anio = int(datos[4].strip())
                marca = datos[5].strip()
                talle = datos[6].strip()
                ingresadas = int(datos[7].strip())
                vendidas = int(datos[8].strip())
                costo_prom = float(datos[9].strip())
                precio_ac = float(datos[10].strip())
                
                camiseta =  [sku, equipo, tipo, anio, marca, talle, ingresadas, vendidas, costo_prom, precio_ac]
                            
                if cod_int not in stock.keys():  #si no esta el cod_int de camiseta
                    stock[cod_int] = [camiseta] #xa cada cod_int tengo una lista de camisetas
                else: #si ya esta el codigo
                    stock[cod_int].append(camiseta) #le agrego una camiseta
        
        return stock
    #pruebo abrir el archivo si no lo encuentra le indico al usuario q no exite porque sino
    #tira error la carga de datos en el diccionario y al llamar el dict desde otras funciones 
    # del menu.

    except:        
        print("No se encontro el archivo alumnos.csv")

def equipos_mayor_stock(stock: dict)->None:
    # Mostrar por pantalla los 3 Equipos de los cuales se tienen mayor cantidad de 
    # unidades en stock, ordenados por cantidad de camisetas distintas en orden 
    # descendente
    # stock =
    # {cod_int: [ [sku, equipo, tipo, anio, marca, talle, ingresadas, vendidas, costo_prom, precio_ac] ]}
    # Para cada clave codigo interno tengo una lista de camisetas cada una con sus datos
    
    #QUEDO LARGUISIMA PERO GARANTIZO QUE FUNCIONA
    
    equipos_mas_stock = dict()  #{equipo: [cant, cod_int],[cant, co_int_n]} se repetiran codigos internos pero
                                            #estaran en distitnos eles de la lista
    camisetas_por_equipo = dict()

    for cod_int, camisetas in stock.items():
        cant_de_camisetas =  len(camisetas)
        for camiseta in camisetas:  #recordar q el valor camisetas es una lista de camisetas
            equipo = camiseta[1]
            ingresadas = camiseta[6]
            vendidas = camiseta[7]
            cant = ingresadas - vendidas
            if equipo not in equipos_mas_stock:
                equipos_mas_stock[equipo] = [ [cant, cod_int]  ]
            else:
                equipos_mas_stock[equipo].append([cant, cod_int]) #le agrego un tipo de camiseta
        
        camisetas_por_equipo[equipo] = cant_de_camisetas

    equipos_por_stock =  dict() #{equipo: stock}
    for equipo, camisetas in equipos_mas_stock.items():
        for camisetas in camisetas:
            cant = camisetas[0]
            if equipo not in equipos_por_stock:
                equipos_por_stock[equipo] = cant
            else:
                equipos_por_stock[equipo]+=cant
    
    equipos_aux = sorted(equipos_por_stock, key=equipos_por_stock.get, reverse= True) #SI, ESTO FUNCIONA. 
    #este metodo devuelve una lista con las claves ordenadas por stock

    tres_equipos = list()   #los tres equipos con mas stock
    #traigo las 3 primeras
    for i in range(3):
        tres_equipos.append(equipos_aux[i])

    tres_equipos_con_camisetas =  list()
    for equipo in tres_equipos:
        cant_cam = camisetas_por_equipo[equipo]
        tres_equipos_con_camisetas.append([cant_cam,equipo])
    
    tres_equipos_con_camisetas.sort(reverse=True)

    for equipo in tres_equipos_con_camisetas:
        print(f"{equipo[1]} con {equipo[0]} camisetas distintas")
    #observar que river no aparece (ver stock.txt adjuno)

    print()


def relacion_venta_talles(stock: dict)->None:
    #Mostrar por pantalla la distribución porcentual de ventas respecto a talles ordenado 
    # descendentemente por porcentaje
    # {cod_int: [ [sku, equipo, tipo, anio, marca, talle, ingresadas, vendidas, costo_prom, precio_ac] ]}

    ventas_por_talle = dict()   #cada talle es una clave
    ventas_totales = 0
    for cod_int, camisetas in stock.items():
        for camiseta in camisetas:  #recordar q el valor camisetas es una lista de camisetas
            talle = camiseta[5]
            vendidas = camiseta[7]
            ventas_totales += vendidas
            if talle not in ventas_por_talle.keys():
                ventas_por_talle[talle] = vendidas           
            else:
                ventas_por_talle[talle]+=vendidas

    lista_ventas_por_talle = list()

    for talle, cant_vendida in ventas_por_talle.items():
        porcentaje = (cant_vendida/ventas_totales)*100
        lista_ventas_por_talle.append([porcentaje, talle])

    lista_ventas_por_talle.sort(reverse = True)

    for talle in lista_ventas_por_talle:
        print(f"El talle {talle[1]} compone un {talle[0]} % de las ventas\n")

def antiguedad_promedio_stock(stock: dict)->None:
    #Mostrar por pantalla la antigüedad promedio ponderada del stock actual, 
    # contemplando que las camisetas del año 2021 tienen 0 años de antigüedad, 
    # las del  2020  tienen  1  año  de  antigüedad  y  así  sucesivamente.  
    # Contemplar únicamente artículos que se hayan vendido alguna vez.
    #{cod_int: [ [sku, equipo, tipo, anio, marca, talle, ingresadas, vendidas, costo_prom, precio_ac] ]}
    
    camisetas_totales = 0
    antiguedad_total_ponderada = 0 #camiseta*antiguedad + camiseta_2*antigueda etc
    for cod_int, camisetas in stock.items():
        for camiseta in camisetas:  #recordar q el valor camisetas es una lista de camisetas
            if camiseta[7]>0:   #si sevendio aunq sea una
                antiguedad = 2021 - camiseta[3]
                stock_actual = camiseta[6]- camiseta[7]

                antiguedad_total_ponderada += stock_actual * antiguedad
                camisetas_totales += stock_actual
    
    var_antiguedad_prom_stock = antiguedad_total_ponderada/camisetas_totales
    print("Antiguedad promedio del stock: %.3f anios\n"%var_antiguedad_prom_stock)
        #59
        #19 59/19 = 3.105

def escribir_archivo_ochenta(lista_articulos_ochenta)->None:
    #lista_articulos_ochenta = [valor_tot_articulo,sku,stock_actual, porcentaje]    
    #consigna:  SKU, Cantidad en stock actual, Valor total, % cubierto
    with open("ochenta.txt", "w") as arch:
        for articulo in lista_articulos_ochenta:
            sku = articulo[1]
            stock_actual = articulo[2]
            valor_tot = articulo[0]
            porcentaje = articulo[3]
            lista_linea = [sku,str(stock_actual),str(valor_tot), str(porcentaje)[:5]]
            
            linea = ";".join(lista_linea)
            arch.write(linea+'\n')

def articulos_ochenta_stock(stock: dict)->None:
    #Determinar que artículos conforman al menos el 80% del stock valorizado 
    # (contemplado a precio de costo promedio) y exportarlos a un archivo de texto 
    # llamado “ochenta.txt” indicando 
    # SKU, Cantidad en stock actual, Valor total, % cubierto
    # {cod_int: [ [sku, equipo, tipo, anio, marca, talle, ingresadas, vendidas, costo_prom, precio_ac] ]}

    # 4059322286834;3;22.83;35 
    # 1234567891234;4;45.37;46 
    # Aclaración: La suma de los % tiene que ser igual o superior al 80%

    valor_stock_total = 0 #camiseta*antiguedad + camiseta_2*antigueda etc
    
    lista_articulos_por_valor = list() #[ [sku,stock_actual,valor_tot_articulo], [etc]]
    
    for cod_int, camisetas in stock.items():
        for camiseta in camisetas:  #recordar q el valor camisetas es una lista de camisetas
            sku = camiseta[0]
            stock_actual = camiseta[6]- camiseta[7]
            precio_prom = camiseta[8]
            valor_tot_articulo = stock_actual *precio_prom
            valor_stock_total += valor_tot_articulo
            #se q no se repiten x como lo ordene
            lista_articulos_por_valor.append([valor_tot_articulo,sku,stock_actual])

    lista_articulos_por_valor.sort(reverse = True)
    #ordenados de mayor a menor segun valor_tot

    lista_articulos_ochenta = list()
    suma_porcentajes = 0
    i = 0
    while suma_porcentajes <= 80: #lista_articulos_por_valor[i][0] = valor_tot_articulo "i"
        porcentaje = (lista_articulos_por_valor[i][0]/valor_stock_total)*100
        suma_porcentajes += porcentaje
        lista_articulos_por_valor[i].append(porcentaje) #le agrego el porcentaje q representa
        lista_articulos_ochenta.append(lista_articulos_por_valor[i])
        i +=1
    
    #lista_articulos_ochenta = [valor_tot_articulo,sku,stock_actual, porcentaje]
    #print(lista_articulos_ochenta)

    escribir_archivo_ochenta(lista_articulos_ochenta)



def main():
    opciones = ["1 - Procesar el archivo (stock.txt)",
                "2 - Equipo Mayor stock",
                "3 - Distribucion porcentual ventas respecto a talles",
                "4 - Antiguedad promedio stock",
                "5 - Articulos conforman 80 stock valorizado",
                "6 - Sair del programa"
                ]

    salir = False
    while not salir:
        for opc in opciones:
            print(opc)
        opc = int(validar_opcion(1,len(opciones),"Elija una opcion: "))       

        if opc == 1:
            ruta_arch_1 = "stock.txt"
            stock = obtener_stock(ruta_arch_1)
            #print(stock)
            # for cod, camiseta in stock.items():
            #     print(f"{cod} - {camiseta}")
    
    #Usari este try except que salta en caso de q no se hayan cargado los datos en el dict 
    # stock para q no tire error al abrirlo. Pero x algun error q no encuentro no
    #funciona.
    #try:
        if opc == 2:
            #Mostrar por pantalla los 3 Equipos de los cuales se tienen mayor 
            # cantidad de unidades en stock, ordenados por cantidad de camisetas 
            # distintas en orden descendente
            equipos_mayor_stock(stock)

        elif opc == 3:
            #Mostrar por pantalla la distribución porcentual de ventas respecto a 
            #talles ordenado descendentemente por porcentaje
            relacion_venta_talles(stock)

        elif opc == 4:
            #Mostrar por pantalla la antigüedad promedio ponderada del stock actual, 
            # contemplando que las camisetas del año 2021 tienen 0 años de antigüedad, 
            # las del  2020  tienen  1  año  de  antigüedad  y  así  sucesivamente.  
            # Contemplar únicamente artículos que se hayan vendido alguna vez. 
            antiguedad_promedio_stock(stock)

        elif opc == 5:
            #Determinar que artículos conforman al menos el 80% del stock valorizado 
            # (contemplado a precio de costo promedio) y exportarlos a un archivo de 
            # texto llamado “ochenta.txt” indicando SKU, Cantidad en stock actual, 
            # Valor total, % cubierto.  Ejemplo:
            articulos_ochenta_stock(stock)

        elif opc == 6:
            salir = True
    #except:
        #print("Po favor cargue los datos")

main()