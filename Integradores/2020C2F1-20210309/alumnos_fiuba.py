#El programa deberá tener un menú poder cumplir lo siguiente:
# a- Procesar información de entrada
# b- Determinar la antigüedad promedio por carrera de los alumnos activos
# indicando la fecha actual
# c- Indicar cual es el mejor alumno activo de la facultad (en base a su promedio)
# d- Determinar el promedio de materias aprobadas de los alumnos de una
# carrera que se le solicita al usuario
# e- Indicar cual es el departamento con mayor cantidad de materias aprobadas
# por alumnos (Recordar que el departamento son los primeros dos dígitos de la materia.
# Ej: Si un alumno tiene aprobadas N materias del departamento de computación (75) se
# deben contar esas N).

#TIEMOS: 18:55 - 19:35 procesamiento de archivos (40 min)
#        19:35 - 19:55 consigna b) (20 min)
#        19:55 - 20:17 consigna c) (22 min)____60% en teoria aprobado -> 1hr 22 min
#        20:17 - 20:40 consigna d) (23 min)____80% aprobado seguro -> 1hr 45 min
#        20:40 - 21:00 consigna e) (20 min)____100% XD -> 2hr 05 min

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

def obtener_alumnos(ruta_arch:str)->dict:
    """
    ruta_arch = "alumnos.csv"
    """
    #ESTRUCTURA ELEGIDA:
    #Padrón, Nombre, Apellido, Carrera, Año de Ingreso 
    # 77024, Guido, Costa, Ing. en Informática, 1997
    #alumnos = {carrera: [ [padron, nombre, apellido, anio], [padron, nobre..., etc] }

    alumnos = dict()
    try:
        with open(ruta_arch, "r") as arch:
            #next(archivo, None)
            for linea in arch:   
                #print(linea)             
                linea = linea.strip('\n')
                #datos =  linea.split(';') #csv
                datos = linea.split(',') #txt

                padron = datos[0].strip()
                nombre = datos[1].strip() 
                apellido = datos[2].strip()
                carrera = datos[3].strip().upper()  #para el input!!
                anio = int(datos[4].strip())
                
                #cada alumnos es una lista
                info_alumno = [padron, nombre, apellido, anio]
                
                #xa cada carrera...
                if carrera not in alumnos.keys():
                    alumnos[carrera] = [info_alumno]  #el valor es una lista de listas con alumnos
                else:   #si ya esta la carrera
                    alumnos[carrera].append(info_alumno)   #le agrego un alumno a la lista
            
            return alumnos
    except:
        print("No se encontro el archivo alumnos.csv")


def obtener_materias(ruta_arch: str)->dict:
    """
    ruta_arch = "materias.csv"
    """
    #ESTRUCTURA ELEGIDA
    #alumnos = {carrera: [ [padron, nombre, apellido, anio], [padron, nobre..., etc] }
    #Padrón, materia1, nota1, materia2, nota2, materia3, nota3, ... , materiaN , notaN 
    # 77024, 75.40, 9, 62.01, 7, 61.03, 6, 75.12, 4
    #materias = {padron:[ [materia, nota], [materia, nota], [etc] ] }

    materias = dict()
    try:
        with open(ruta_arch, "r") as arch:
            #next(archivo, None)
            for linea in arch:   
                #print(linea)             
                linea = linea.strip('\n')
                #datos =  linea.split(';') #csv
                datos = linea.split(',') #txt

                padron = datos[0].strip()

                asignaturas = list()    #[[materia, nota], [materia, nota], etc]
                for i in range(1, len(datos),2):
                    materia = datos[i].strip()
                    nota = int(datos[i+1].strip())
                    asignaturas.append([materia, nota])
                              
                #xa cada alumno -> Se q no se repiten...
                materias[padron] = asignaturas # para cada alumno, su valor es una lista de listas
                                                    #de materias
            return materias
    except:
        print("No se encontro el archivo alumnos.csv")

def antiguedad_prom_por_carrera(fecha_actual: int, alumnos: dict) ->None:
    ##b-Determinar la antigüedad promedio por carrera de los alumnos activos 
    # #indicando la fecha actual 
    #ESTRUCTURA ELEGIDA
    #alumnos = {carrera: [ [padron, nombre, apellido, anio], [padron, nobre..., etc] }

    lista_antiguedad_por_carrera = list() #[ [cant_med, nro_radar, prov] ]

    for carrera, estudiantes in alumnos.items(): #estudiantes = [ [padron, nombre, apellido, anio], [padron, nobre..., etc]
        antiguedad_tot = 0
        for estudiante in estudiantes:   #estudiante = alumnos pero no puedo usar palara x nombre dict
            antiguedad_tot += (fecha_actual - estudiante[3])
        ant_promedio = antiguedad_tot/ len(estudiantes)
        lista_antiguedad_por_carrera.append([ant_promedio, carrera])
    
    for carrera in lista_antiguedad_por_carrera:
        print(f"{carrera[1]} : {carrera[0]}")

def mejor_alumno(materias:dict, alumnos:dict)->None:
    #ESTRUCTURA ELEGIDA
    #alumnos = {carrera: [ [padron, nombre, apellido, anio], [padron, nobre..., etc] }
    ##materias = {padron:[ [materia, nota], [materia, nota], [etc] ] }
    #c-Indicar cual es el mejor alumno activo de la facultad (en base a 
    # su promedio) 
    promedio_por_padron = list() #[ [prov, cant_infrac], ... ]    
    for padron, asignaturas in materias.items():    
        nota_total = 0
        for asignatura in asignaturas:  #asignaturas = [ [materia, nota], [materia, nota], [etc] ]
            nota_total += asignatura[1]
        
        promedio_padron = nota_total/len(asignaturas)
        promedio_por_padron.append([promedio_padron, padron])

    mejor_alumno = max(promedio_por_padron) #Conozco max y se q ordena segun el primer ele de c/ lista
    padron_einstein = mejor_alumno[1]

    #Ahora buscco el nombre del alumno en alumnos
    for carrera, estudiantes in alumnos.items():
        for estudiante in estudiantes: 
            if estudiante[0] == padron_einstein: #lo voy encontrar una sola vez
                nombre = estudiante[1]+' '+estudiante[2]
    
    print(f"El mejor alumno de la fiuba es {padron_einstein}: {nombre}\n")

def promedio_materias_carrera(carrera_usuario:str, alumnos:dict, materias:dict)->None:
    #d-Determinar el promedio de materias aprobadas de los alumnos de 
    #una carrera que se le solicita al usuario
    ##ESTRUCTURA ELEGIDA
    #alumnos = {carrera: [ [padron, nombre, apellido, anio], [padron, nobre..., etc] }
    ##materias = {padron:[ [materia, nota], [materia, nota], [etc] ] }
    #c-Indicar cual es el mejor alumno activo de la facultad (en base a 
    # su promedio) 
    #1º traigo alumnos de la carrera
    #2º Saco el promedio de sus materias
    lista_estudiantes_carrera = list()    #[padron_1, padron_2, et]

    for carrera, estudiantes in alumnos.items():
        if carrera == carrera_usuario: #solo me la encuentro una vez xq son clave
            for estudiante in estudiantes: 
                lista_estudiantes_carrera.append(estudiante[0])
    
    total_materias_carrera = 0
    for estudiante in lista_estudiantes_carrera:    #estudiante = padron
        for padron, asignaturas in materias.items():
            if padron == estudiante: #ecnontre al alumno
                total_materias_carrera += len(asignaturas) #sumo todas las asignaturas q aprobo 

    print(lista_estudiantes_carrera)
    if lista_estudiantes_carrera: #evitar 0 division en caso de mal ingreso
        promedio_aprobadas = total_materias_carrera / len(lista_estudiantes_carrera)
        print(F"El promedio de materias aprobadas de {carrera_usuario} es {promedio_aprobadas}\n")

def depto_mas_materias_aprobadas(materias)->None:
    #e-Indicar cual es el departamento con mayor cantidad de materias 
    # aprobadas por alumnos (Recordar que el departamento son los 
    # primeros dos dígitos de la materia. Ej: Si un alumno tiene 
    # aprobadas N materias del departamento de computación (75) se 
    # deben contar esas N).
    #77024, 75.40, 9, 62.01, 7, 61.03, 6, 75.12, 4
    #materias = {padron:[ [materia, nota], [materia, nota], [etc] ] }
    
    materias_por_depto = dict() #{depto: cant_materias_aprobadas }
    
    for padron, asignaturas in materias.items():    
        for asignatura in asignaturas:  #asignaturas = [ [materia, nota], [materia, nota], [etc] ]
            codigo = asignatura[0][:2]
            if codigo not in materias_por_depto.keys():
                materias_por_depto[codigo] = 1   #1 alumno aprobo una materia del depto
            else: # si ya esta
                materias_por_depto[codigo] += 1  # le agrego 1 xq o el alumno aprobo otra de ese depto
                                                # u otro alumno aprobo algun de ahi
    
    depto_no_asesino = max(materias_por_depto,  key = materias_por_depto.get)
    cant_de_materias = materias_por_depto[depto_no_asesino]
    print("El depto con mas materias aprobadas por alumno es: ", end ="")
    print(f"{depto_no_asesino} con {cant_de_materias}\n")


def main():
    opciones = ["1 - Procesar archivos (alumnos.csv materias.csv)",
                "2 - Antiguedad promedio",
                "3 - Mejor alumno activo (promedio!)",
                "4 - Promeido materias aprobadas carrera X usuario",
                "5 - Depto mas materias aprobadas",
                "6 - Sair del programa"
                ]   
    
    salir = False
    while not salir:
        for opc in opciones:
            print(opc)
        opc = int(validar_opcion(1,len(opciones),"Elija una opcion: "))       

        if opc == 1:
            ruta_arch_1 = "alumnos.csv"
            ruta_arch_2 = "materias.csv"
            alumnos = obtener_alumnos(ruta_arch_1)
            #print(alumnos)
            materias = obtener_materias(ruta_arch_2)
            #print(materias)

        else:
                if alumnos and materias: #si existen los dicts. Quedaria mas lindo un try except
                    #pero los archivos no los abro xa cada opcion...

                    if opc == 2:
                        #b-Determinar la antigüedad promedio por carrera de los alumnos activos 
                        # indicando la fecha actual 
                        fecha_actual = int(input('Ingrese anio actual: '))
                        antiguedad_prom_por_carrera(fecha_actual, alumnos)
                                    
                    elif opc ==3:
                        #c-Indicar cual es el mejor alumno activo de la facultad (en base a 
                        # su promedio) 
                        mejor_alumno(materias, alumnos)

                    elif opc ==4:
                        #d-Determinar el promedio de materias aprobadas de los alumnos de 
                        #una carrera que se le solicita al usuario
                        #(NINGUN EXTRA XD)! PERMOTE ELEGIR carrera
                        carrera_usuario = input("Ingerse una carrera: ").upper()
                        promedio_materias_carrera(carrera_usuario, alumnos, materias)

                    elif opc ==5:
                        #e-Indicar cual es el departamento con mayor cantidad de materias 
                        #aprobadas por alumnos (Recordar que el departamento son los primeros 
                        # dos dígitos de la materia. Ej: Si un alumno tiene aprobadas N 
                        # materias del departamento de computación (75) se deben contar 
                        # esas N).
                        depto_mas_materias_aprobadas(materias)

                    elif opc == 6:
                        salir = True

main()