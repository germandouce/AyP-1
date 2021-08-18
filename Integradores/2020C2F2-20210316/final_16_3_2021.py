def menu()->None:
    m = [
        "1. Procesar información de entrada",
        "2. Determinar la plataforma que mayores ingresos generó en toda la historia",
        "3. Determinar el usuario que mayor cantidad de plataformas puntuó y cuanto dinero lleva gastado en plataformas.",
        "4. Ranking de plataformas por puntuación promedio",
        "5. Determinar la plataforma mas utilizada",
        "6. salir"
    ]
    for i in m:
        print(i)

def obtener_info_plataformas(archivo: str)->dict: ## p = {key : plataforma = value [ costo , meses activo ] }
    p = dict()
    with open(archivo, "r", encoding="UTF-8") as plataformas:
        for linea in plataformas:
            linea = linea.strip().split(",")
            plat = linea[0]
            costo = linea[1]
            meses_activo = linea[2]
            p[plat] = [costo, meses_activo]
    return p

def obtener_info_UP(archivo : str )->dict: ## u = { key : plataforma = value : meses_totales (entre todos los usuarios) }
    u = dict()

    with open(archivo, "r", encoding="UTF-8") as usuarios_p:
        for linea in usuarios_p: 
            linea = linea.strip().split(",")
            plataforma = linea[1]
            meses = int(linea[3])
            if plataforma in u.keys():
                u[plataforma] += meses
            else:
                u[plataforma] =  meses

    return u

def determinar_ingresos(plataforma: dict, i_usuarios_plataformas: dict)->None:
    mayores_ingresos = 0
    p_mayor = ""
    for k, v in plataforma.items():
        ingreso_plataforma = int(v[0]) * i_usuarios_plataformas[k]
        if ingreso_plataforma > mayores_ingresos: 
            mayores_ingresos = ingreso_plataforma
            p_mayor = k
    print(f"\n -> La plataforma que hizo mas guita es : {p_mayor}\n")

def obtener_info_u(archivo: str, info_plataforma: dict)->dict: ## usuarios = { key : usuario , value = [dinero gastado , cantidad_plataformas ]}
    usuarios = dict()
    with open(archivo , "r") as usuario:
        for linea in usuario:
            linea = linea = linea.strip().split(",")
            u = linea[0]
            p = linea[1]
            cant_plataformas = 1
            costo = 0
            for k, v in info_plataforma.items():
                if k == p:
                    costo = int(v[0])

            meses_uso = int(linea[3])
            dinero_gastado = meses_uso * costo
            nueva_info = [dinero_gastado, cant_plataformas]
            if u in usuarios.keys():
                for i in range(len(usuarios[u])):
                    usuarios[u][i] += nueva_info[i]
            else: usuarios[u] = [dinero_gastado, cant_plataformas]
    return usuarios

def obtener_usuario_mayoritario(info_usuario: dict)->None:
    u_mayor = ""
    cantidad_plataformas = 0
    mayor_dinero_gastado = 0
    for k, v in info_usuario.items():
        if v[1] > cantidad_plataformas:
            mayor_dinero_gastado = v[0]
            cantidad_plataformas = v[1]
            u_mayor = k

    print(f"\n -> El usuario con mayor cantidad de plataformas es : {u_mayor} , con ${mayor_dinero_gastado}  gastados\n")

def obtener_puntaciones(archivo: str)->dict: ## puntuaciones = { key: plataformas , values: [ puntuacion , cantidad_de_puntuaciones ]}
    puntuaciones = dict()
    with open(archivo , "r") as usuario:
        for linea in usuario:
            linea = linea = linea.strip().split(",")

            p = linea[1]
            puntuacion = float(linea[2])

            if p in puntuaciones:
                nueva_puntuacion = [puntuacion, 1]
                for i in range(len(puntuaciones[p])):
                    puntuaciones[p][i] += nueva_puntuacion[i]
            else:
                puntuaciones[p] = [puntuacion, 1]
    return puntuaciones

def ranking_plataformas(puntuaciones: dict)->None:
    lista_promedios = list()
    for k , v in puntuaciones.items():
        promedio = v[0] / v[1]
        lista_promedios.append((k, promedio))
    lista_promedios.sort(key= lambda x: x[1], reverse=True)
    print()
    for i in range(len(lista_promedios)):
        print(f" -> { i + 1 } -> {lista_promedios[i][0]} con {lista_promedios[i][1]} de puntuacion")
    print()

def obtener_dispositivos(archivo: str, p: str)->None: ## dic_dispositivos = {key : dispo , value : horas_totales}
    dic_dispositivos = dict()
    with open(archivo, "r") as usuarios:
        for linea in usuarios:
            lista_d = list()
            linea  = linea.strip().split(",")
            plataforma = linea[1]
            if p == plataforma:
                lista_d = linea[4::]
                for i in range(len(lista_d)):
                    if i % 2 == 0:
                        if lista_d[i] in dic_dispositivos.keys():
                            dic_dispositivos[lista_d[i]] += int(lista_d[i + 1])
                        else:
                            dic_dispositivos[lista_d[i]] = int(lista_d[i + 1])
    dispositivos_ordenados = sorted( dic_dispositivos.items(), key= lambda x: x[1], reverse= True)
    print(f"\nLa plataforma mas utilizada es {p} !!! :")
    for i in range(len(dispositivos_ordenados)):
        print(f"{dispositivos_ordenados[i][0]} -> {dispositivos_ordenados[i][1]} horas")
    print()

def main()->None:

    menu()
    eleccion = input("Elegir opcion : ")
    while eleccion != "6":

        if eleccion == "1":
            plataforma = obtener_info_plataformas("plataformas.csv")
            i_usuarios_plataformas = obtener_info_UP("usuarios.csv")
        try : 
            if eleccion == "2":
                determinar_ingresos(plataforma, i_usuarios_plataformas)

            elif eleccion == "3":
                info_usuario = obtener_info_u("usuarios.csv", plataforma)
                obtener_usuario_mayoritario(info_usuario)

            elif eleccion == "4":
                puntuaciones = obtener_puntaciones("usuarios.csv")
                ranking_plataformas(puntuaciones)

            elif eleccion == "5":
                plat_ordenada = sorted(i_usuarios_plataformas.items(), key= lambda x: x[1], reverse=True )
                plataformas_mas_usada = plat_ordenada[0][0]
                obtener_dispositivos("usuarios.csv", plataformas_mas_usada)
        except:
            print("\n --- Primero debe procesar la informacion ---\n")

        menu()
        eleccion = input("Elegir opcion : ")

main()