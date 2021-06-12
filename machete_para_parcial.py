#MACHETE PARA PARCIAL
#FUNCIONES MUY UTILES Y USADAS


#MAIN SIMPLE
def main()-> None:
    #main()
    pass


#VALIDADOR DE OPCIONES PARA MENU
#Util para menus y para corte de ciclos tipo seguir ingresando( 1- si  0- no)

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


#INGRESO DE NUMEROS ENTEROS O FLOTANTES CORTA CON CUALQUIER LETRA
def ingreso_numeros_corta_letra()-> list:
    #lista_de_numeros = ingreso_numeros_corta_letra()
    """
    PRE: no contiene parametros

    POST: Devuelve lista con numeros enteros (¡Acepta negativos!)
    """

    print('Ingrese numeros corte con cualqueir letra')
    lista = list()

    num = input('')
    while num.strip('-').isnumeric():
        lista.append(num)
        num = input('')
    
    return lista


#CICLO DE INGRESO DE ELEMENTOS CON CORTE MANUAL
def ingreso_elementos() -> list:
    #ingreso_elementos()
    lista = list()

    cortar = False
    while not cortar:
        
        print('Ingrese algo')
        
        #opc o funcion xa ingresar datos

        opc = int( validar_opcion(0,1, 'Desea seguir ingresando? 1- Si 0 - No: ') )
        if opc == 0:
            cortar = True
    
    return lista

#FUNCIONES XA MOSTRAR DATOS A USUARIO
def listar_cursos_max_precio(cursos) -> None:  #listar_cursos_condicion_del_ejercicio
    pass

def cargar_asistentes(cursos) -> None:      # funcion especifica de modificacion y o alta mmm
    pass

def mostrar_cursos_ordenados(cursos) -> None:   #mostra todos los cursos (ordenados)
    pass


#FUNCIONES DE ALTA - BAJA - MODIFICACION
def alta_curso(cursos: dict) -> None:
    
    curso = dict()  #el nuevo curso es un diccionario con datos q seran clave
    llave = int(input("Ingrese el código del nuevo curso: ")) #sera el codigo o clave ppal del curso
    
    #Pido datos del curso
    nombre = input("Ingrese el nombre del curso: ")    #estos datos se agregan al cursos[llave]
    costo = float(input("Ingrese el costo del curso: "))        #como claves
    dias = int(input("Ingrese la cantidad de días del curso: "))
    vacantes = int(input("Ingrese la cantidad de vacantes del curso: "))
    
    fechas = list()
    flag_seguir_ingresando = True
    while flag_seguir_ingresando:
        fecha = ""
        fecha = input(f"Ingrese una fecha para el curso: ")
        fechas.append(fecha)
        ingresar_corte = input("¿Quiere seguir ingresando datos <s/n>? ")
        if ingresar_corte != "s":
            flag_seguir_ingresando = False
    
    #Guardo los datos en la tabla del curso  
    curso["nombre"] = nombre
    curso["costo"] = costo
    curso["cantidad_de_dias"] = dias
    curso["cantidad_de_vacantes"] = vacantes
    curso["fechas_de_dictado"] = fechas

    #Convierto el curso: cursos[llave] en key de la tabla cursos
    cursos[llave] = curso   



def baja_curso(cursos: dict) -> None:
    for curso, datos in cursos.items():
        
        llave = "nombre"
        print(f"{curso} - {datos[llave]}")

    opciones = list(cursos.keys())
    
    opc = input('¿Que curso desea modificar?: ')
    while ( not opc.isnumeric() ) or ( int(opc) not in opciones):
        opc = input('ingrse una opcion valida: ')
    opc = int(opc)

    cursos.pop(opc)


def modificar_curso(cursos: dict) -> None:
    
    #muestro cursos
    for curso, datos in cursos.items():
        llave = "nombre"
        print(f"{curso} - {datos[llave]}")
    
    opciones = list(cursos.keys())
    
    opc = input('¿Que curso desea modificar?: ')
    while ( not opc.isnumeric() ) or ( int(opc) not in opciones):
        opc = input('ingrse una opcion valida: ') 
    opc = int(opc)

    #muestro datos del curso elegido xa modificar
    for key, value in cursos[opc].items():
        print(f"{key} - {value}")
    
    #Pregunto q desea modificar
    entrada = input("¿Qué desea modificar del curso?: ")
    if entrada == "nombre":
        nombre = input(f"Ingrese el nuevo {entrada}: ")
        cursos[opc][entrada] = nombre

    elif entrada == "costo":
        costo = float(input(f"Ingrese el nuevo {entrada}"))
        cursos[opc][entrada] = costo

    elif entrada == "cantidad_de_dias":
        cantidad_de_dias = int(input(f"Ingrese la nueva {entrada}"))
        cursos[opc][entrada] = cantidad_de_dias

    elif entrada == "cantidad_de_vacantes":
        cantidad_de_vacantes = int(input(f"Ingrese la nueva {entrada}"))
        cursos[opc][entrada] = cantidad_de_vacantes

    elif entrada == "fechas_de_dictado": 
        
        cortar = False
        fechas_de_dictado = list()

        while not cortar:
            fecha = input(f"Ingrese las nuevas {entrada}: ")
            fechas_de_dictado.append(fecha)

            seguir = int(validar_opcion(0,1,"¿Quiere seguir ingresando fechas 1- Si 0- No ?: "))
            if seguir == 0:
                cortar = True
        
        cursos[opc][entrada] = fechas_de_dictado


#DERIVADOR DE OPCIONES abm_cursos
def abm_cursos (opc, cursos):
    '''
    #PRE: Recibe la opc elegida en el menu  y las estructura ppal 
    utilizada para guardar y operar con el ABM

    #POST: Redirige a la funcion q corresponda xa hacer lo pedido x el usuari
    '''
    if opc == 0:
        alta_curso(cursos)
    
    elif opc == 1:
        baja_curso(cursos)
    
    if(opc == 2):
        modificar_curso(cursos)
    
    elif(opc == 2):
        listar_cursos_max_precio(cursos)    #Que cuesten mas de 1150$  ( segun x condicion)

    elif(opc == 3):
        cargar_asistentes(cursos)

    elif(opc == 4):
        mostrar_cursos_ordenados(cursos)
    #AGREGAR MAS OPCIONES O QUITAR SI ES NECESARIO


#MAIN XA ABM
def main():
    cerrar = False

    #Estructura a usar en el ABM xa guardar y modificar los datos {}, [] etc:
    # cursos = [["Aprende  a hacer tu propio compost",1 ,950],
    # ["Los niños y el medioambiente(para padres e hijes)",2,990],
    # ["Tu huerta orgánica",4,2500]]

    cursos ={   

        1: {
            "nombre": "Aprendé a hacer tu propio compost",
            "costo": 950.0,
            "cantidad_de_dias": 1,
            "cantidad_de_vacantes": 4,
            "fechas_de_dictado": ["10/06/2021"]
        },
            2: {
            "nombre": "Los niños y el medioambiente",
            "costo": 990.0,
            "cantidad_de_dias": 2,
            "cantidad_de_vacantes": 5,
            "fechas_de_dictado": ["09/06/2021", "15/06/2021"]
        },
            3: {
            "nombre": "Tu huerta orgánica",
            "costo": 2500.0,
            "cantidad_de_dias": 4,
            "cantidad_de_vacantes": 10,
            "fechas_de_dictado": ["01/06/2021", "04/06/2021", "21/06/2021"]
        }    
    }

    while not cerrar:

        #MENU DE OPCIONES DEL ABM:
        print('''
        Bienvenido  al sistema de registros de cursos de RumboCircular, ¿Que desea hacer? 
        0.Dar de ALTA un curso
        1.Dar de BAJA un curso
        2.MODIFICAR uno de los tres cursos    #1 alta          
        3.Mostrar los cursos con un coste mayor a 1150  #2 baja
        4.Seleccionar asistentes para un curso          #3 modificacion
        5.Mostrar el listado de cursos y asistentes     #4 mostrar
        6.Cerrar el programa (MUESTRA CURSOS!!1) ''')       #última opcion es cerrar programa

        opc = int( validar_opcion(0,6, 'Ingrese una opcion: '))

        if opc != 6:
            abm_cursos(opc, cursos)
        
        else:
            
            for curso, datos in cursos.items():
                print(f'\n{curso}:')
                for llave in datos:
                    print(f'{llave}: {datos[llave]}')
            cerrar = True
main()
