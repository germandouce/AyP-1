# El programa deberá tener un menú poder cumplir lo siguiente:
# a- Determinar en qué eliminatorias se anotaron mas goles indicando año del
# mundial y cantidad de goles
# b- Determinar qué equipo tiene la mayor efectividad histórica (3 para la
# victoria, 1 para el empate, 0 para la derrota), indicando País y efectividad porcentual .
# efectividad = puntos obtenidos*100 / (partidos jugados *3)
# c- Pedir al usuario el ingreso de un año de mundial y generar un archivo de
# texto llamado clasificados.csv, que contenga la tabla de posiciones de dichas
# eliminatorias indicando: País, Puntos. Ordenado por puntos descendente.
# d- Mostrar quien es el máximo goleador histórico indicando: Nombre, País.


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


def obtener_goles(ruta_arch)->dict:
    """
    ruta_arch = "goles.csv"
    """
    goles = dict()
    #ESTRUCTURA ELEGIDA:
    #partidos = {id_partido: [Anio, P_loc, P_Visit, Goles_local, goles_visitante] 
    #goles = {nombre_jugador: {id_partido: [condicion, goles_jug]} }
    
    #OTRA!!! goles = {nombre_jugador: [[id_partido, condicion, goles],[id_n, cond_n, goles_n] ] }
    try:
        with open(ruta_arch, "r") as archivo:
            for linea in archivo:                
                linea = linea.strip('\n')
                datos =  linea.split(';') #csv
                #datos =  linea.split(',') #txt
                
                id_partido = datos[0].strip()
                condicion = datos[1].strip()
                nombre_jugador = datos[2].strip()
                goles_jug= int(datos[3].strip())

                if nombre_jugador not in goles.keys():
                    #creo el diccionario de jugador
                    jugador = dict()

                    #convierto en clave del jugador el partido   
                    #estoy seguro de q no voy a tener 2 id_partido's ='s por jugador
                    #pues el jugador juega un partido a la vez y cada uno es visitante o local
                    jugador[id_partido] = [condicion, goles_jug]
                    
                    #convierto en clave de goles el jugador
                    goles[nombre_jugador] = jugador
                else:
                    #estoy seguro de q no voy a tener 2 id_partido's ='s por jugador por
                    #eso no chequeo no exista ya el partdio
                    goles[nombre_jugador][id_partido] = [condicion, goles_jug]
        return goles
    except:
        print("No se encontro el archivo")


def obtener_partidos(ruta_arch)->dict:
    """
    ruta_arch = "partidos.csv"
    """
    #ESTRUCTURA ELEGIDA:
    #partidos = {id_partido: [Anio, P_loc, P_Visit, Goles_local, goles_visitante] 
    #goles = {nombre_jugador: {id_partido: [condicion, goles_jug]} }
    partidos = dict()

    try :
        with open(ruta_arch, "r") as arch:
            for linea in arch:                
                linea = linea.strip('\n')
                datos =  linea.split(';') #csv
                #linea = linea.split(',') #txt

                id_partido = datos[0].strip()
                anio = datos[1].strip().upper() #para el input
                p_local = datos[2].strip()
                p_visitante = datos[3].strip()
                goles_local = int(datos[4].strip())
                goles_visitante  = int(datos[5].strip())

                if id_partido not in partidos.keys():
                    partidos[id_partido] = [anio, p_local, p_visitante, goles_local, goles_visitante]
                #else:
                    #partidos[id_partido][n] += 
        return partidos
    except:
        print("No se encontro el archivo")

def eliminatorias_mas_goles(partidos:dict)->None:  
    #eliminatorias se anotaron mas goles indicando año del mundial y cantidad de goles 
    #partidos = {id_partido: [Anio, P_loc, P_Visit, Goles_local, goles_visitante] 
    #goles = {nombre_jugador: {id_partido: [condicion, goles_jug]} }
    goles_por_eliminatoria = dict() #{anio: goles_tot}
    
    for id_partido in partidos.keys():
        anio = partidos[id_partido][0]  
        goles_partido = partidos[id_partido][3] + partidos[id_partido][4] 
        #print(goles_partido)
        if anio not in goles_por_eliminatoria.keys():
            goles_por_eliminatoria[anio] = goles_partido
        else:
            goles_por_eliminatoria[anio] += goles_partido

    anio_con_mas_goles = max(goles_por_eliminatoria, key=goles_por_eliminatoria.get)
    goles_tot = goles_por_eliminatoria[anio_con_mas_goles]

    print(f"El anio de eliminatoria con mas goles fue {anio_con_mas_goles} con {goles_tot} goles")

def sumar_puntos(equipo, puntos_por_pais: dict, puntos):
    #{pais: [puntos, partidos]} #saco max de valores y obtengo claves
    if equipo not in puntos_por_pais.keys():
        puntos_por_pais[equipo] = [puntos, 1]
    else:
        puntos_por_pais[equipo][0]+= puntos
        puntos_por_pais[equipo][1]+=1  #partido


def mayor_efectividad_historica (partidos:dict)->None:  
    #b-Determinar qué  equipo  tiene  la  mayor  efectividad  histórica  (3  para  
    # lavictoria, 1 para el empate, 0 para la derrota), indicando País y efectividad
    #  porcentual . efectividad = puntos obtenidos*100 / (partidos jugados *3)
 
    #partidos = {id_partido: [Anio, P_loc, P_Visit, Goles_local, goles_visitante] 
    #goles = {nombre_jugador: {id_partido: [condicion, goles_jug]} }
    
    puntos_por_pais = dict()   #{pais: [puntos, partidos]} #saco max de valores y obtengo claves                                                
    for id_partido in partidos.keys():
        equipo_local = partidos[id_partido][1]  
        equipo_visit = partidos[id_partido][2]

        goles_local = partidos[id_partido][3]
        goles_visit =  partidos[id_partido][4]
    
        if goles_local > goles_visit:
            puntos_local = 3
            puntos_visit = 0
        elif goles_local < goles_visit:
            puntos_visit = 3
            puntos_local = 0
        else:
            puntos_visit = 1
            puntos_local = 1    
        
        sumar_puntos(equipo_local, puntos_por_pais, puntos_local)
        sumar_puntos(equipo_visit, puntos_por_pais, puntos_visit)
    
    efectividad_por_pais = dict()
    for equipo, datos in puntos_por_pais.items():
        efectividad = ( (puntos_por_pais[equipo][0]*100) / (puntos_por_pais[equipo][1] *3) )
        efectividad_por_pais[equipo] = efectividad
    
    print(efectividad_por_pais)
    pais_mas_efectivo = max(efectividad_por_pais, key=efectividad_por_pais.get)
    efectividad = efectividad_por_pais[pais_mas_efectivo]

    print(f"\nEl pais mas efectivo fue {pais_mas_efectivo} con {efectividad} %\n")

def crear_lista_escribir_archivo(puntos_por_pais)->None:
    lista_puntajes = list() #[[puntaje, pais] ] #la di vuelta respecto al dict ojo! 
    for pais, info in puntos_por_pais.items():
        lista_puntajes.append([info[0], pais,])
    
    lista_puntajes.sort(reverse = True) #conozco la funcion y se q se ordena segun el primer elemento de cada sublista
    print(lista_puntajes)
    print()
    with open('clasificados.csv', 'w') as arch:
        for pais in lista_puntajes:
            linea = pais[1] + ";" + str(pais[0])+"\n"
            arch.write(linea)


def maximo_goleador_historico(partidos, goles)->None:
    #indicando pais y jugador 
    #primero saco el  nombre despues el pais
    #partidos = {id_partido: [Anio, P_loc, P_Visit, Goles_local, goles_visitante] 
    
    #goles = {nombre_jugador: {id_partido: [condicion, goles_jug]} }

    #OTRA!!! goles = {nombre_jugador: [[id_partido, condicion, goles],[id_n, cond_n, goles_n] ] }


    goles_por_jugador = dict()  #{jugador: [goles, id_part, condicino]}
    for jugador in goles.keys():
        for id_partido in goles[jugador].keys():
            if jugador not in goles_por_jugador.keys():
                condicion = goles[jugador][id_partido][0]   #con un id y conidcion me basta 
                goles_por_jugador[jugador] = [goles[jugador][id_partido][1], id_partido, condicion]
            else:
                goles_por_jugador[jugador][0] += goles[jugador][id_partido][1]

    max_goleador = max(goles_por_jugador, key = goles_por_jugador.get)  #trae segun el primer
    goles_tot = goles_por_jugador[max_goleador][0]                 #elememento de la lista (valor)
    id_partido = goles_por_jugador[max_goleador][1]
    condicion = goles_por_jugador[max_goleador][2]
    #ahora necesito su pais 
    if condicion == "V":
        pais = partidos[id_partido][2]
    else:
        pais = partidos[id_partido][1]
    print(f"el max goleador es {max_goleador} con {goles_tot} goles de {pais}")
    

def crear_archivo_clasificados(partidos,anio_mundial):
    #no tuve tiempo de modularizarla y me quedo casi igual a la anterior
    
    #c-Pedir al usuario el ingreso de un año de mundial y generar un archivo de texto  
    # llamado clasificados.csv,  que  contenga  la  tabla  de  posiciones  de  dichas 
    # eliminatorias indicando: País, Puntos. Ordenado por puntos descendente
    #partidos = {id_partido: [Anio, P_loc, P_Visit, Goles_local, goles_visitante] 
    puntos_por_pais = dict()   #{pais: [puntos, partidos]} #saco max de valores y obtengo claves                                                
    for id_partido in partidos.keys():
        if partidos[id_partido][0] == anio_mundial: #si corresponde al anio q ingreso el user 
            equipo_local = partidos[id_partido][1]  
            equipo_visit = partidos[id_partido][2]

            goles_local = partidos[id_partido][3]
            goles_visit =  partidos[id_partido][4]
        
            if goles_local > goles_visit:
                puntos_local = 3
                puntos_visit = 0
            elif goles_local < goles_visit:
                puntos_visit = 3
                puntos_local = 0
            else:
                puntos_visit = 1
                puntos_local = 1    
            
            sumar_puntos(equipo_local, puntos_por_pais, puntos_local)
            sumar_puntos(equipo_visit, puntos_por_pais, puntos_visit)
    
    crear_lista_escribir_archivo(puntos_por_pais)


def main():
    opciones = ["1 - Eliminatoria con maas goles con anio y cant de goles",
                "2 - Equipo con mayor efectividad historica",
                "3 - Archivo clasificados",
                "4 - maximo goleador historico",
                "5 - Sair del juego"
                ]   
    ruta_arch_1 = "partidos.csv"
    ruta_arch_2 = "goles.csv"
    partidos = obtener_partidos(ruta_arch_1)
    goles = obtener_goles(ruta_arch_2)
    
    # print(partidos)
    # print(goles)

    salir = False
    while not salir:
        for opc in opciones:
            print(opc)
        
        opc = int(validar_opcion(1,len(opciones),"Elija una opcion: "))       

        if opc == 0:
            print("Nothing here")

        elif opc == 1:
            eliminatorias_mas_goles(partidos)

        elif opc == 2:
            #b-Determinar qué  equipo  tiene  la  mayor  efectividad  histórica  (3  para  
            # lavictoria, 1 para el empate, 0 para la derrota), indicando País y efectividad
            #  porcentual . efectividad = puntos obtenidos*100 / (partidos jugados *3)
            #tiempo: 3hrs:15 min... 21:27....
            mayor_efectividad_historica(partidos)

        elif opc ==3:
            anio_mundial = input("ingrese el anio de un mundial: ").upper() 
            crear_archivo_clasificados(partidos, anio_mundial)
        elif opc ==4:
            maximo_goleador_historico(partidos, goles)

        elif opc == 5:
            salir = True

main()