#1- Poseer un menú con los siguientes reportes:
# a. Procesar archivo (esta opción debe permitir cargar el archivo “radares.txt”)
# b. Mostrar por pantalla la provincia con mayor cantidad de infracciones indicando
# Provincia y cantidad de infracciones
# c. Mostrar por pantalla los radares donde se haya un volumen de mediciones
# mayor al promedio de la de todos los radares y donde el % de infractores sea
# mayor al 5%.
# d. Mostrar por pantalla todos los radares de CABA ordenados por velocidad
# promedio medida descendente.
# e. Determinar los radares donde la velocidad promedio medida sea mayor a la
# máxima admitida y guardarlos en un archivo por provincia indicando el Nro de
# radar y cantidad de infracciones separados por punto y coma. Ej:
# BUENOS AIRES.txt
# 2;54

#TIEMPO: 16:45 - 18:36 = 1hr 50 min hay 3/5 60% ejercicio completo
#Tarde 16:20 - 18:00 solo xa abrir archivo!! 1hr 20 min
#consignas: 2, 3 de 5 18:00 - 18:35 = 35 min
#resto: 4,5 18:35 - 19:10 = 35 min
#consgignas en si 1hr: 10 min
#COMPLETO: 3 HRS 15 MIN

import csv

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

def escribir_archivo(ruta_arch, lista_radares)->None:
    header = ["Nro de Radar","Provincia","Velocidad Máxima admitida","Velocidad promedio medida","Cantidad de mediciones","Cantidad infracciones"]
    titulo = ";".join(header)
    with open(ruta_arch, "w") as arch:
        arch.write(titulo+"\n")
        for radar in lista_radares:  #[nro, juris, vel_max...]
            #print(radar)
            linea = ";".join(radar)
            arch.write(linea+'\n')

def cargar_radares(ruta_arch: str)->dict:
    """
    ruta_arch = "radares.txt"
    """
    #1;CABA;130;117;1734;25 
    # 2;BUENOS AIRES;80;87;2125;54 
    # 3;CORDOBA;120;108;1371;13 

    cortar = False
    lista_radares = list()
    while not cortar:
        nro_radar = input("Ingrse el numero de radar: ")
        jurisdiccion = input("Ingrese la jurisdiccion: ").upper()
        vel_max_ad = input("Ingrese la velocidad maxima permitida: ")
        vel_prom_med = input("Ingrese la velocidad promedio medida: ")
        cant_med = input("Ingrese la cantidad de mediciones del radar: ")
        cant_infrac = input("Ingrese la cantidad de infracciones que detecto: ")
        radar = [nro_radar, jurisdiccion, vel_max_ad, vel_prom_med, cant_med, cant_infrac]
        lista_radares.append(radar)
        
        opc = int(validar_opcion(0,1,"Desea ingresar otro radar? 1-Si 0 - No: "))
        if opc == 0:
            cortar = True 
    
    escribir_archivo(ruta_arch, lista_radares)

def obtener_radares(ruta_arch:str)->dict:
    """
    ruta_arch = "radares.csv"
    """
    #1;CABA;130;117;1734;25 
    #ESTRUCTURA ELEGIDA:
    #radares = {jurisdiccion:[ [nro_radar, vel_max_ad, vel_prom_med, cant_med, cant_infrac] ] 
    radares = dict()
    try:
        with open(ruta_arch, "r") as archivo:
            next(archivo, None)
            for linea in archivo:   
                #print(linea)             
                linea = linea.strip('\n')
                datos =  linea.split(';') #csv
                #linea = linea.split(',') #txt

                nro_radar = datos[0].strip()
                jurisdiccion = datos[1].strip().upper() #para el input!!
                vel_max_ad = int(datos[2].strip())
                vel_prom_med = int(datos[3].strip())
                cant_med = int(datos[4].strip())
                cant_infrac = int(datos[5].strip())
                info_radar = [nro_radar, vel_max_ad, vel_prom_med, cant_med, cant_infrac]
                #cada radar es una lista
                if jurisdiccion not in radares.keys():
                    radares[jurisdiccion] = [info_radar]  #el valor es una lista de listas
                else:   #si ya esta la jurisdccion
                    radares[jurisdiccion].append(info_radar)   #le agrego un radar a la lista
            
            return radares
    except:
        print("No se encontro el archivo radares.csv, por favor cree el y cargue los radares con la opc procesar archivo")

def prov_mas_infracciones(radares:dict)->None:
    #Mostrar por pantalla la provincia con mayor cantidad de infracciones indicando Provincia 
    #y cantidad de infracciones
    #ESTRUCTURA ELEGIDA:
    #radares = {jurisdiccion:[ [nro_radar, vel_max_ad, vel_prom_med, cant_med, cant_infrac] ] 
    infracciones_por_provincia = list() #[ [prov, cant_infrac], ... ]    
    for prov, medidores in radares.items():
        cant_infrac = 0
        for medidor in medidores:   #medidor = radar pero no puedo usar palara x nombre dict
            cant_infrac += medidor[4] 
        infracciones_por_provincia.append([cant_infrac, prov])
    
    prov_mas_peligrosa = max(infracciones_por_provincia) #se qe le max es segun 1er ele de c/ lista
    prov = prov_mas_peligrosa[1]
    cant = prov_mas_peligrosa[0]
    
    print(f"La provincia con mas infracciones es {prov} con {cant} infracciones")

def radares_condicion_dada(radares: dict)->None:
    #c.Mostrar por pantalla los radares donde se haya un volumen de mediciones
    #mayor al promedio de la de todos los radares y donde el % de 
    #infractores sea mayor al 5%.
    #radares = {jurisdiccion:[ [nro_radar, vel_max_ad, vel_prom_med, cant_med, cant_infrac] ] } 

    radares_condicion = list() #[ [cant_med, nro_radar, prov] ]

    total_mediciones = 0
    cant_radares = 0
    for prov, medidores in radares.items():
        for medidor in medidores:   #medidor = radar pero no puedo usar palara x nombre dict
            if (medidor[4]/ medidor[3]) > 0.05 : 
                total_mediciones += medidor[3]
                cant_radares +=1
                radares_condicion.append([medidor[3], medidor[0], prov])                
    promedio_mediciones = (total_mediciones/cant_radares)
    print(radares_condicion)
    print(promedio_mediciones)
    print("radares que cumplen condicion dada:\n")
    for medidor in radares_condicion:
        if medidor[0] > promedio_mediciones:    #volumen mayor al promedio
            print(f"radar {medidor[1]} - {medidor[2]} con {medidor[0]} mediciones")
    print()

def radares_caba_vel_descendiente(radares, provincia)->None:
    #radares = {jurisdiccion:[ [nro_radar, vel_max_ad, vel_prom_med, cant_med, cant_infrac] ] } 
    #Mostrar por pantalla todos los radares de CABA ordenados por velocidad 
    # promedio medida descendente.
    #CON EXTRA!!!!
    radares_prov = list()

    for prov, medidores in radares.items():
        if prov == provincia:
            for medidor in medidores:   #medidor = radar pero no puedo usar palara x nombre dict
                vel_promedio = medidor[2]
                nro_radar = medidor[0]
                radares_prov.append([vel_promedio,nro_radar])       
    radares_prov.sort(reverse = True)

    print(f"Radares de {provincia} vel promedio descendiente\n")
    
    for radar in radares_prov:
        print(f"radar nro {radar[1]} con vel promedio de {radar[0]} km/h")

    print()

def crear_archivo_prov(medidores_prov, nombre_arch)->None:  #creo q es = a escribir archivo...
    with open(nombre_arch, "w") as arch:
        #csv_writer = csv.writer(arch, delimiter = ';')
        for medidor in medidores_prov:  #medidores = [ [nro, cant_infrac], ]
            #csv_writer.writerow(medidor)
            #arch.writelines(medidor)   #no agrega el delimiter entre elementos de la lista
            #print(medidor)
            linea = ";".join(medidor)   #agrego el delimiter para cada row
            arch.write(linea+'\n')  
    print("Se creo correctamente el archivo con los datos pedidos")  

def radares_vel_mayor_permitida(radares)->None:
    #Determinar los radares donde la velocidad promedio medida sea mayor a la máxima 
    # admitida y guardarlos en un archivo por provincia indicando el Nro de radar y 
    # cantidad de infracciones separados por punto y coma. Ej: BUENOS AIRES.txt 2;54 
    #radares = {jurisdiccion:[ [nro_radar, vel_max_ad, vel_prom_med, cant_med, cant_infrac] ] } 
    for prov, medidores in radares.items():
        medidores_prov = list()
        for medidor in medidores:   #medidor = radar pero no puedo usar palara x nombre dict
            if (medidor[2] > medidor[1]):
                nro_radar = medidor[0]
                cant_infrac = medidor[4]
                nombre_arch = prov+".csv"
                medidores_prov.append([nro_radar, str(cant_infrac)])
        if medidores_prov:  #si no esta vacia la lista (osea hay medidores con vel promedio may a max)
            crear_archivo_prov(medidores_prov, nombre_arch)


def main():
    opciones = ["1 - Procesar archivo (permite cargar radares)",
                "2 - Prov con mas infracciones",
                "3 - Volumen may a promedio y infractores may a 5%",
                "4 - Mostrar radares de X ciudad CON Velocidad promedio medida decendiente",
                "5 - radares con vel mayor a permitida por provincia",
                "6 - Sair del programa"
                ]   
    
    # radares = obtener_radares(ruta_arch_1)
    # goles = obtener_goles(ruta_arch_2)

    # print(partidos)
    # print(goles)

    salir = False
    while not salir:
        for opc in opciones:
            print(opc)
        opc = int(validar_opcion(1,len(opciones),"Elija una opcion: "))       

        if opc == 1:
            ruta_arch_1 = "radares.csv"
            cargar_radares(ruta_arch_1)
        else:
            ruta_arch_1 = "radares.csv"
            radares = obtener_radares(ruta_arch_1)

            if opc == 2:
                #Mostrar por pantalla la provincia con mayor cantidad de infracciones 
                # indicando Provincia y cantidad de infracciones
                prov_mas_infracciones(radares)
                            
            elif opc ==3:
                #c.Mostrar por pantalla los radares donde se haya un volumen de mediciones
                #mayor al promedio de la de todos los radares y donde el % de 
                # infractores sea mayor al 5%.
                radares_condicion_dada(radares)

            elif opc ==4:
                #Mostrar por pantalla todos los radares de CABA ordenados por velocidad 
                # promedio medida descendente.
                #CON EXTRA!! PERMOTE ELEGIR PROVINCIA
                provincia = input("Ingerse una provincia: ").upper()
                radares_caba_vel_descendiente(radares, provincia)
            elif opc ==5:
                #Determinar los radares donde la velocidad promedio medida sea mayor a la 
                # máxima admitida y guardarlos en un archivo por provincia indicando el Nro 
                # de radar y cantidad de infracciones separados por punto y coma. 
                # Ej: BUENOS AIRES.txt 2;54 
                radares_vel_mayor_permitida(radares)

            elif opc == 6:
                salir = True

main()