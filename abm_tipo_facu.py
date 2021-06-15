'''
Luego el programa deberá permitir emitir los siguientes reportes:
a) Indicar la carrera que tiene los mejores alumnos en base al promedio de todos ellos
b) Determinar el promedio de materias aprobadas de los alumnos de una carrera que se le solicita al 
usuario
c) Determinar el apellido más frecuente en la facultad
d) Determinar la antigüedad promedio de los alumnos (en base a la fecha de hoy) que estén en el 
último cuarto de la carrera, suponiendo que todas las carreras tienen 48 materias
'''

# carreras = {
#   {nombre (de la carrera):
#              nota_total:             
#              total_alumnos:     
#              materias_aprobadas:  
#            }   
#
# alumnos = {
#   padron: {
#       nombre: str,
#       apellido: str
#       carrera: str
#       cantidad_de_materias_aprobadas: int,
#       Nota_promedio: int,
#       anio_de_ingreso: int
#   }
# }

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

#FUNCION PARA MOSTRAR NOMBRE DE UNA CLAVE SU VALOR DE UN DICT DE DICT
def mostrar_nombre_carreras(carreras:dict)->None:
    for carrera in carreras.keys():
        print(carrera)

#FUNCIONES XA MOSTRAR DATOS A USUARIO
def mostrar_promedio_materias_carrera_dada(carreras:dict) -> None:  
    # carreras = {
    #     {nombre (de la carrera):
    #               
    #              nota_total:             
    #              total_alumnos:     
    #              materias_aprobadas:  
    #            }   

    print('carreras de la facu\n')
    mostrar_nombre_carreras(carreras)

    nombre_carrera = input("Ingrse el nombre de la carrera cuyo promedio de materias quiere mostrar: ")

    for carrera, datos in carreras.items():
        if carrera == nombre_carrera:
            print(f'promedio matrias aprobadas: {datos["materias_aprobadas"]/ datos["total_alumnos"]}')

def mostrar_carrera_mejores_alumnos(carreras) -> None: #muestra cursos ordenados y el q tiene mas (hace todo)
    # carreras = {
    #     {nombre (de la carrera):
    #               
    #              nota_total:             
    #              total_alumnos:     
    #              materias_aprobadas:  
    #            }   

    promedio_carreras = [] #creo lista donde guradare las carreras y sus repectivos promedios
    
    for carrera, datos in carreras.items():
        promedio_carreras.append( [ datos['nota_total'] / datos['total_alumnos'] , carrera ] )
    #cantidad_de_tratamientos.sort(reverse =  True, key= lambda tratamiento: tratamiento[0] ) #tratamiento [1] es la cantidad de veces q fue realizado
        
    max_promedio =  max(promedio_carreras)
    print()    

    # for carrera in promedio_carreras:
    #     print(f'{trata[1]} fue solicitado {trata[0]} veces')                
    # print()
    
    print('carrera (s) con mejores alumnos')
    for carrera in promedio_carreras:
        if carrera[0] == max_promedio[0]:
            print(f'{carrera[1]} tiene un promedio de {carrera[0]}')                

def mostrar_antiguedad_promedio_ultimo_4to(alumnos) -> None:  
    # carreras = {
    # {nombre de la carrera:
    #              nota_total:             
    #              total_alumnos:     
    #              materias_aprobadas:  
    #            }   
    #
    # alumnos = {
    #   padron: {
    #       nombre: str,
    #       apellido: str
    #       carrera: str
    #       cantudad_de_materias: int,
    #       Nota_promedio: int,
    #       anio_de_ingreso: int
    #       antiguedad: int
    #   }
    # }
    antiguedad_total = 0
    total_alumnos = 0
    for datos in alumnos.values():
        if datos["cantudad_de_materias"] >= 36:
            antiguedad_total += datos["antiguedad"] 
            total_alumnos += 1 
    print('la antiguedad promedio de los alumnos en el ultimo cuarto es de', antiguedad_total/total_alumnos)       



def mostrar_apellido_mas_comun(alumnos: dict) -> None:   
    apellidos = dict()  #apellidos = {apellido: repes}

    # alumnos = {
    #   padron: {
    #       nombre: str,
    #       apellido: str
    #       carrera: str
    #       cantidad_de_materias_aprobadas: int,
    #       Nota_promedio: int,
    #       anio_de_ingreso: int
    #   }
    for alumno, datos in alumnos.items():
        if datos["apellido"] not in apellidos:
            apellidos[datos["apellido"]] = 1
        else:
            apellidos[datos["apellido"]] += 1
    
    apellidos_por_cant = []
    for apellido, cantidad in apellidos.items():
        apellidos_por_cant.append( [cantidad, apellido ]) 
                
    max_cantidad = max(apellidos_por_cant)
    
    print('Apellido (s) mas comun')
    print(f'El apellido {max_cantidad[1]} lo tienen {max_cantidad[0]} personas')   


#FUNCIONES DE ALTA - BAJA - MODIFICACION
def alta_alumno(alumnos: dict, carreras:dict) -> None:
    

    alumno = dict()  #el nuevo alumno es un diccionario con datos q seran clave
    padron = int(input("Ingrese el padron del nuevo alumno: ")) #sera el codigo o clave ppal de alumno
    
    carrera = dict()

    #Pido datos del alumno
    nombre = input("Ingrese el nombre del alumno: ")   
    apellido = input("ingresa el apelldio del alumno: ")
    carrera_alumno = input("ingersa la carrera del alumno: ")
    cantudad_de_materias = int(input("Ingrese la cantidad de materias aprobadas: "))
    nota_promedio =  int(input("Ingrese la nota promdio del alumno: "))
    anio_de_ingreso = int(input("Inrese el anioo de ingreso del alumno: "))

        #OJO DICE CANTUDAD DE MATERIAS NO LO CAMBIE XA NO HACER
    #Guardo los datos en la tabla alumnos  
    alumno["nombre"] = nombre
    alumno["apellido"] = apellido
    alumno["carrera"] = carrera_alumno
    alumno["cantudad_de_materias"] = cantudad_de_materias  
    alumno["nota_promedio"] = nota_promedio 
    alumno["anio_de_ingreso"] = anio_de_ingreso
    alumno["antiguedad"] = (2021 - anio_de_ingreso)

    #guardo datos en la tabla carreras
    ##Convierto la carrera carera: carreras[carerra] en key de la tabla carreras
    if carrera_alumno not in carreras:
        carreras[carrera_alumno] = carrera
        carrera["nota_total"] = nota_promedio
        carrera["total_alumnos"] = 1
        carrera["materias_aprobadas"] = cantudad_de_materias
    else:
        carrera["nota_tota"] += nota_promedio
        carrera["total_alumnos"] +=1 
        carrera["materias_aprobadas"] += cantudad_de_materias

    #Convierto el alumno: alumnos[padron] en key de la tabla alumnos
    alumnos[padron] = alumno
    

def baja_alumno(cursos: dict) -> None:

    #mostrar_nombre_cursos(cursos)

    opciones = list(cursos.keys())
    
    opc = input('¿Que curso desea DAR DE BAJA?: ')
    while ( not opc.isnumeric() ) or ( int(opc) not in opciones):
        opc = input('ingrse una opcion valida: ')
    opc = int(opc)

    cursos.pop(opc)


def modificar_alumno(cursos: dict) -> None:
    
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
def abm_alumnos (opc, alumnos:dict, carreras:dict):
    '''
    #PRE: Recibe la opc elegida en el menu  y las estructura ppal 
    utilizada para guardar y operar con el ABM

    #POST: Redirige a la funcion q corresponda xa hacer lo pedido x el usuari
    '''
    if opc == 0:
        alta_alumno(alumnos, carreras)
    
    #elif opc == 1:
    #     baja_paciente(pacientes)
    
    # if(opc == 2):
    #     modificar_pacientes(pacientes)
    
    elif(opc == 2):
        mostrar_promedio_materias_carrera_dada(carreras)   #tratamiento mas elegido por pacientes

    elif(opc == 3):
        mostrar_apellido_mas_comun(alumnos) #muestra nuevos y viejos

    elif(opc == 4):
        mostrar_antiguedad_promedio_ultimo_4to(alumnos) #muestra total vendido en sopes

    elif(opc == 1):
        mostrar_carrera_mejores_alumnos(carreras) #muestra tratamiento mas solicitado entre todos


#MAIN XA ABM
def main():
    cerrar = False

    # carreras = {
    # {nombre de la carrera:
    #              nota_total:             
    #              total_alumnos:     
    #              materias_aprobadas:  
    #            }   
    #
    # alumnos = {
    #   padron: {
    #       nombre: str,
    #       apellido: str
    #       carrera: str
    #       cantidad_de_materias_aprobadas: int,
    #       Nota_promedio: int,
    #       anio_de_ingreso: int
    #       antiguedad: int
    #   }
    # }


    alumnos ={}

    carreras = {}    


    while not cerrar:

        #MENU DE OPCIONES DEL ABM:
        print('''
Bienvenido  al sistema de registros de cursos de RumboCircular, ¿Que desea hacer? 
0.Dar de ALTA un alumno
1.Indicar carrera con mejores alumnos en base a promedio
2.Indicar promedio alumnos carrera pedida       
3.mostrar apellido mas comun
4.Mostrar antiguedad promedio alumnos en el ultimo 4to carrera
5.Mostrar monto total ganado con tratamientos vendidos  #muestra varios datos ESPECIFICOS SI LO HAY
6.Mostrar el tratamiento mas solicitado por los pacientes #mostrar datos segun el max de ellos
7.Cerrar el programa (MUESTRA todo!!1) ''')

        opc = int( validar_opcion(0,7, 'Ingrese una opcion: '))

        if opc != 7:
            abm_alumnos(opc, alumnos, carreras)
        
        else:
            mostrar_nombre_carreras(carreras)
            for alumno, datos in alumnos.items():
                print(f'\n{alumno}:')
                for llave in datos:
                    print(f'{llave}: {datos[llave]}')
            cerrar = True


main()
