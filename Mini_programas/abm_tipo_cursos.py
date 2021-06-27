
#ABM TIPO SIMPLE:
#preguntas tip
'''
0.Dar de ALTA un curso
1.Dar de BAJA un curso
2.MODIFICAR uno de los tres cursos  #modificar valores de las claves de dict dentro de dict        
3.Mostrar los cursos con un coste mayor a 1150 #Mostrar valores dentro del dict chico q cumplen x condicion
4.Cargar asistentes para un curso   #Agregar clave a dict dentro de dict
5.Mostrar el listado de cursos ORDENADOS y sus asistentes   #muestra varios datos ESPECIFICOS SI LO HAY
6.Mostrar el o los cursos cuya cantidad de vacantes sea la máxima #mostrar datos segun el max de ellos
7.Cerrar el programa (MUESTRA CURSOS!!1)
'''
# cursos = {
#   codigo: {
#       nombre: str,
#       costo: float,
#       cantidad_de_dias: int,
#       cantidad_de_vacantes: int,
#       fechas_de_dictado: list(str(dd/mm/yy))
#   }
# }

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

#IMPRIMIR DATOS DE DICT
def mostrar_curso(curso : dict) -> None:
    for llave, dato in curso.items():
        print(f"{llave}: {dato}")


#FUNCIONES XA MOSTRAR DATOS A USUARIO
def listar_cursos_precio_mayor(cursos:dict) -> None:  #listar_cursos_condicion_del_ejercicio
    print('Cursos con precio mayor a: ')
    limite = int(input('Ingrese valor de referencia: '))

    cantidad = 0    
    for curso in cursos.values():
        if curso['costo'] >= limite:
            mostrar_curso(curso)
            print()
            cantidad += 1
    print(f'Hay {cantidad}, cursos con precio mayor a {limite}')

def mostrar_curso_con_max_vacantes(cursos) -> None: #muestra cursos ordenados y el q tiene mas (hace todo)
    
    vacantes_por_curso = [] #creo lista donde guradare los curso y sus repectivas vacantes
    
    for curso in cursos.values():
        vacantes_por_curso.append( [curso['cantidad_de_vacantes'], curso['nombre'] ])
    vacantes_por_curso.sort(reverse =  True, key= lambda curso: curso[0] ) #curso [1] es la cantidad de vacantes de cda curso q agregu
    
    max_cantidad =  max(vacantes_por_curso)
    print()    

    for cursito in vacantes_por_curso:
        print(f'{cursito[0]} tiene {cursito[1]} vacantes')                
    print()
    
    print('Curso (s) con max cantidad de vacantes')
    for cursito in vacantes_por_curso:
        if cursito[1] == max_cantidad[1]:
            print(f'{cursito[0]} con {cursito[1]} vacantes')                

#FUNCION PARA MOSTRAR NOMBRE DE UNA CLAVE SU VALOR DE UN DICT DE DICT
def mostrar_nombre_cursos(cursos)->None:
    for curso, datos in cursos.items():
        llave = "nombre"
        print(f"{curso} - {datos[llave]}")


def mostrar_cursos_ordenados_con_asistentes(cursos: dict) -> None:   #mostra todos los cursos (ordenados)
    #cursos = sorted(cursos)        
    for datos in cursos.values():
        nombre = 'nombre'
        if 'asistentes' in datos.keys():
            asistentes = 'asistentes'
            print(f'{datos[nombre]} - Asistentes: {datos[asistentes]}')
        else:
            print(f'{datos[nombre]} - No tiene asistentes')


def cargar_asistentes(cursos: dict) -> None:   
    
    mostrar_nombre_cursos(cursos)

    opc = int(input('¿A que curso desea agregar asistentes?: '))
    nombre_asistente = input('Igrese nombre del asistente: ')
    
    if 'asistentes' not in cursos[opc].keys():
        cursos[opc]['asistentes'] = [nombre_asistente]
    else:
        cursos[opc]['asistentes'].append(nombre_asistente)


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

    mostrar_nombre_cursos(cursos)

    opciones = list(cursos.keys())
    
    opc = input('¿Que curso desea DAR DE BAJA?: ')
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
    
    elif(opc == 3):
        listar_cursos_precio_mayor(cursos)    #Que cuesten mas de 1150$  ( segun x condicion)

    elif(opc == 4):
        cargar_asistentes(cursos)

    elif(opc == 5):
        mostrar_cursos_ordenados_con_asistentes(cursos)

    elif(opc == 6):
        mostrar_curso_con_max_vacantes(cursos)


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
            "nombre": "Los niños y el medio ambiente",
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
2.MODIFICAR uno de los tres cursos  #modificar valores de las claves de dict dentro de dict        
3.Mostrar los cursos con un coste mayor a 1150 #Mostrar valores dentro del dict chico q cumplen x condicion
4.Cargar asistentes para un curso   #Agregar clave a dict dentro de dict
5.Mostrar el listado de cursos ORDENADOS y sus asistentes   #muestra varios datos ESPECIFICOS SI LO HAY
6.Mostrar el o los cursos cuya cantidad de vacantes sea la máxima #mostrar datos segun el max de ellos
7.Cerrar el programa (MUESTRA CURSOS!!1) ''')

        opc = int( validar_opcion(0,7, 'Ingrese una opcion: '))

        if opc != 7:
            abm_cursos(opc, cursos)
        
        else:
            
            for curso, datos in cursos.items():
                print(f'\n{curso}:')
                for llave in datos:
                    print(f'{llave}: {datos[llave]}')
            cerrar = True
main()
