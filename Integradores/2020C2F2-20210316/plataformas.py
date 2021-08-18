#El programa deberá tener un menú poder cumplir lo siguiente:
# 1. Procesar información de entrada
# 2. Determinar la plataforma que mayores ingresos generó en toda la historia
# 3. Determinar el usuario que mayor cantidad de plataformas puntuó y cuanto dinero lleva
# gastado en plataformas.
# 4. Ranking de plataformas por puntuación promedio
# 5. Determinar la plataforma mas utilizada, y luego indicar como es la distribución
# porcentual sobre los dispositivos que se utiliza ordenada del mas utilizado al menos
# utilizado
# 17:53 - 20:05 --> 2hrs 12 min___ 60% 
# 20:05 - 20:17 --> 12 min___80%
# 20:17 - 20:50 --> 33 min Fin__100%
#Total = 3 horas

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

def obtener_plataformas(ruta_arch:str)->dict:
    """
    ruta_arch = "plataformas.csv"
    """
    #ESTRUCTURA ELEGIDA:
    #Plataforma, costo mensual, años de actividad 
    # Netflix, 400, 8 
    # Spotify, 275, 6 
    #plataformas = {plataforma: [costo_mensual, anios] }
    
    plataformas = dict()
    try:
        with open(ruta_arch, "r") as arch:
            #next(archivo, None)
            for linea in arch:   
                #print(linea)             
                linea = linea.strip('\n')
                #datos =  linea.split(';') #csv
                datos = linea.split(',') #txt

                plataforma = datos[0].strip()
                costo = int(datos[1].strip()) 
                anios = int(datos[2].strip())
                
                #xa cada plataforma asumo viene una sola plataforma x linea de archivo
                plataformas[plataforma] = [costo, anios] 
            
            return plataformas
    except:        
            print("No se encontro el archivo alumnos.csv")

def obtener_usuarios(ruta_arch: str)->dict:
    """
    ruta_arch = "ususarios.csv"
    """
    #ESTRUCTURA ELEGIDA
    #plataformas = {plataforma: [costo_mensual, anios] }
    #Nombre, Plataforma, Puntuación, Meses suscrito, TipoDispositivo1, Horas1, Tipo Dispositivo2, Horas2, ... ,
    # TipoDispositivo N, horas N 
    # guidocosta, Netflix, 9, 18, Mobile, 73, PC, 42, TV, 179 
    # tomasvillegas, Spotify, 8.5, 12, Mobile, 123, PC, 49
    # usuarios = {nombre_plat:[[usuario, puntos, meses_uso, [tipo_dn, horas_n], etc ] [usuario,] ]etc}
    #  soy rebelde y en usaurios meto plaatformas como clave con todos sus usuarios, esto
    # facilita la resolucion del resto de los puntso

    usuarios = dict()
    with open(ruta_arch, "r") as arch:
        #next(archivo, None)
        for linea in arch:   
            #print(linea)             
            linea = linea.strip('\n')
            #datos =  linea.split(';') #csv
            datos = linea.split(',') #txt0

            usuario = datos[0].strip()
            nombre_plat = datos[1].strip()
            puntos = float(datos[2].strip())
            meses = int(datos[3].strip())
            
            #viene un usuario por linea con una platafroma por linea
            usuario =  [usuario, puntos, meses]
            
            for i in range(4, len(datos),2):
                dispositivo = datos[i].strip()
                horas = int(datos[i+1].strip())
                usuario.append([dispositivo, horas])  #agrego listitas con dispositvos e info
                            
            #xa cada plataforma
            if nombre_plat not in usuarios.keys():  #si no esta la plataforma
                usuarios[nombre_plat] = [usuario] # xa cada plataforma su valor es una lista de users
            else: #si ya esta
                usuarios[nombre_plat].append(usuario) #le agtego un usuario

        return usuarios

    print("No se encontro el archivo alumnos.csv")

def plataforma_mayores_ingresos(plataformas: dict, usuarios: dict)->None:
    #Determinar la plataforma que mayores ingresos generó en toda la historia 
    # plataformas = {plataforma: [costo_mensual, anios] }
    # usuarios = {nombre_plat:[[usuario, puntos, meses_uso, [tipo_dn, horas_n], etc ] [usuario,] ]etc}
    meses_por_plataforma = dict()

    for plataforma, utilizadores in usuarios.items():
        for utilizador in utilizadores:     #recordar q el valor es una lisra de users
            meses = utilizador[2]
            if plataforma not in meses_por_plataforma.keys():
                meses_por_plataforma[plataforma] = meses
            else:
                meses_por_plataforma[plataforma] += meses
    
    ganancias_por_plataforma =  list()
    
    for plataforma in meses_por_plataforma.keys():
        precio_mensual = plataformas[plataforma][0] #ver estructura
        meses_usada = meses_por_plataforma[plataforma]
        ganancia = precio_mensual*meses_usada
        ganancias_por_plataforma.append([ganancia,plataforma])
        
    plataforma_millo = max(ganancias_por_plataforma) #conozco la funcino y se q el  max es segun
                                                    #el primer ele de cada lista
    nombre = plataforma_millo[1]
    ganancias = plataforma_millo[0]
   
    print(f"La plataforma que mas plata hizo fue {nombre} con un total de {ganancias} $\n")

def usuario_mas_puntuador(plataformas: dict, usuarios: dict)->None:
    #UDeterminar el usuario que mayor cantidad de plataformas puntuó y cuanto dinero 
    # lleva gastado en plataformas. 
    # plataformas = {plataforma: [costo_mensual, anios] }
    # usuarios = {nombre_plat:[[usuario, puntos, meses_uso, [tipo_dn, horas_n], etc ] [usuario,] ]etc}
    
    plataformas_por_usuario = dict() #{ususario:[ [plat, meses ] [plat_2, meses ] ]}

    for plataforma, utilizadores in usuarios.items():
        for utilizador in utilizadores:  
            nombre_user = utilizador[0]
            meses = utilizador[2]
            
            plat = [plataforma, meses]

            if nombre_user not in plataformas_por_usuario.keys():
                plataformas_por_usuario[nombre_user] =[plat]
            else:
                plataformas_por_usuario[nombre_user].append(plat)
    
    #usuario q mas puntea
    plats_usuario_compulsivo = []
    for usuario, plats in plataformas_por_usuario.items():
        if len(plats) > len(plats_usuario_compulsivo): #plats = [ [plat, meses ] [plat_2, meses ] ] 
            plats_usuario_compulsivo = plats
            nombre_usuario = usuario

    #plata gastada
    total = 0
    for plat in plats_usuario_compulsivo:
        nombre_plat = plat[0]
        meses = plat[1]
        total += plataformas[nombre_plat][0]*meses

    print(f"El usuario q mas platafomras puntuo fue {nombre_usuario} y gasto {total}\n")
    #funciono bien xd

def plataformas_por_promedio_puntos(usuarios: dict)->None:
    #Ranking de plataformas por puntuación promedio 
    # plataformas = {plataforma: [costo_mensual, anios] }
    # usuarios = {nombre_plat:[[usuario, puntos, meses_uso, [tipo_dn, horas_n], etc ] [usuario,] ]etc}
    
    plataformas_por_puntos = list() #[ [plat, puntos], [plat, puntos]]

    for plataforma, utilizadores in usuarios.items():
        puntos_plat = 0
        total_usuarios = 0
        for utilizador in utilizadores:  
            puntos = utilizador[1]
            puntos_plat += puntos
            total_usuarios +=1
        puntos_prom = puntos_plat/ total_usuarios
        
        plataformas_por_puntos.append([puntos_prom, plataforma])
     
    plataformas_por_puntos.sort(reverse = True)
    for plat in plataformas_por_puntos:
        print(f"{plat[1]}: {plat[0]} puntos promedio")
    print()

def plataforma_mas_usada(usuarios:dict)->None:
    #MAS USADA = mas usuarios
    #Determinar  la  plataforma  mas  utilizada, y  luego  indicar  como  es  la  distribución 
    # porcentual sobre los dispositivos que se utiliza ordenada del mas utilizado al menos 
    # utilizado 
    # plataformas = {plataforma: [costo_mensual, anios] }
    # usuarios = {nombre_plat:[[usuario, puntos, meses_uso, [tipo_dn, horas_n], etc ] [usuario,] ]etc}
    
    # plataforma_mas_usada = []
    # for plataforma, utilizadores in usuarios.items():
    #     for utilizador in utilizadores:
    #         if len(utilizadores)> len(plataforma_mas_usada):
    #             plataforma_mas_usada = utilizadores
    #             nombre_plat = plataforma
    #dispositivo = usuario[i][0]

    plataformas_por_h = dict() #{plataforma: horas}
    for plataforma, utilizadores in usuarios.items():
        for usuario in utilizadores: #usuario = [nombre, ptos, meses, [tipo_dn, horas_n], etc ]
            for i in range(3,len(usuario)):
                horas = usuario[i][1]
                if plataforma not in plataformas_por_h.keys():
                    plataformas_por_h[plataforma] = horas
                else:
                    plataformas_por_h[plataforma] += horas
    
    plataforma_mas_utilizada = max(plataformas_por_h, key = plataformas_por_h.get)
    #devuelve la clave con max valor
    print("horas por plataforma:")
    print(plataformas_por_h)
    print()

    dispositivos = dict()
                            #lista
    for usuario in usuarios[plataforma_mas_utilizada]: #usuario = [nombre, ptos, meses, [tipo_dn, horas_n], etc ]
            for i in range(3,len(usuario)):
                horas = usuario[i][1]
                dispositivo = usuario[i][0]
                if dispositivo not in  dispositivos.keys():
                    dispositivos[dispositivo] = horas
                else:
                    dispositivos[dispositivo] += horas

    nombres_disp = sorted(dispositivos, key=dispositivos.get, reverse= True) #SI, ESTO FUNCIONA. 
    #Devuelve las claves ordendas segun sus valores
    
    print(f"Uso por dispotivo de {plataforma_mas_utilizada}\n")
    for nombre in nombres_disp:
        print(f"{nombre}: {dispositivos[nombre]} hrs")

    print()

def main():
    opciones = ["1 - Procesar informacion (usuarios.csv plataformas.csv)",
                "2 - plataforma mayores ingresos",
                "3 - Usuario mas plataformas puntuo y plata que gasto",
                "4 - Ranking plataformas por puntuacion promedio",
                "5 - Plataforma mas usada",
                "6 - Sair del programa"
                ]   
    
    salir = False
    while not salir:
        for opc in opciones:
            print(opc)
        opc = int(validar_opcion(1,len(opciones),"Elija una opcion: "))       

        if opc == 1:
            ruta_arch_1 = "plataformas.csv"
            ruta_arch_2 = "usuarios.csv"
            plataformas = obtener_plataformas(ruta_arch_1)
            #print(plataformas)
            usuarios = obtener_usuarios(ruta_arch_2)
            #print(usuarios)

    #try:
        if plataformas and usuarios: #si existen los dicts. Quedaria mas lindo un try except
            #pero los archivos no los abro xa cada opcion...

                if opc == 2:
                    #Determinar la plataforma que mayores ingresos generó en toda la 
                    # historia 
                    plataforma_mayores_ingresos(plataformas, usuarios)

                elif opc ==3:
                    #Determinar el usuario que mayor cantidad de plataformas puntuó y 
                    # cuanto dinero lleva gastado en plataformas.
                    usuario_mas_puntuador(plataformas, usuarios)

                elif opc ==4:
                    #Ranking de plataformas por puntuación promedio 
                    plataformas_por_promedio_puntos(usuarios)

                elif opc ==5:
                    #Determinar  la  plataforma  mas  utilizada, y  luego  indicar  como  
                    # es  la  distribución porcentual sobre los dispositivos que se 
                    # utiliza ordenada del mas utilizado al menos utilizado 
                    plataforma_mas_usada(usuarios)

                elif opc == 6:
                    salir = True
#except:
        else:
            print('debe cargar los datos primero')

main()