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


def obtener_respuestas()->dict:
    ruta_arch = "respuestas.txt"
    respuestas = dict()
    #ESTRUCTURA ELEGIDA:
    #preguntas = {id_pregunta: [pregunta, dificultad]}
    #respuestas = {id_pregunta: [rta_1, rta_2, rta_n]}
    try :
        with open(ruta_arch, "r") as arch:
            for linea in arch:                
                linea = linea.strip()
                #linea =  linea.replace(' ','')
                datos =  linea.split(',')   #id_preg, rta1, rta2, rtan

                id_pregunta = datos[0]
                lista_opciones = list()
                for num in range(1,len(datos)): #salteo la primera xq es el id y voy h/ la ult
                    rta = datos[num]
                    lista_opciones.append(rta.strip())
                
                if id_pregunta not in respuestas.keys():
                    respuestas[id_pregunta]= lista_opciones
        return respuestas
    except:
        print("El archivo no existe")


def obtener_preguntas()->dict:
    ruta_arch = "preguntas.txt"
    preguntas = dict()
    #ESTRUCTURA ELEGIDA:
    #preguntas = {id_pregunta: [pregunta, dificultad]}
    #respuestas = {id_pregunta: [rta_1, rta_2, rta_n]}
    try :
        with open(ruta_arch, "r") as arch:
            for linea in arch:                
                linea = linea.strip('\n')
                #linea =  linea.replace(' ','')
                datos =  linea.split(',') 

                id_pregunta = datos[0]
                pregunta = datos[1].strip()
                dificultad = datos[2].strip() 
                
                if id_pregunta not in preguntas.keys():
                    preguntas[id_pregunta]= [pregunta, dificultad]
        return preguntas
    except:
        print("El archivo no existe")


def info_usuario()->None:
    nombre = input("Ingrese su nombre: ")
    cant_preg = int(input("Ingrese la cant de preg a mostar: "))
    dif = int(validar_opcion(0,1,"Ingrese la dificultad (0-baja/1-alta): "))
    if dif == 0:
        dificultad ="baja"
    else:
        dificultad ="alta"

    return  nombre, cant_preg, dificultad

def filtro_preg(preguntas, respuestas, dificultad, cant_preg):
    preguntas_a_mostar = dict() # {id_pregunta: pregunta}
    respuestas_a_mostrar = dict() #{id_pregunta: [rta1,rta2,rta,3]}
    cont = 0
    for id, pregunta in preguntas.items():
        if (pregunta[1] == dificultad) and (cont<= cant_preg):
            preguntas_a_mostar[id] = pregunta[0]
            respuestas_a_mostrar[id] = respuestas[id]   #cargo la lista de respuesta            
        #si no se cumple no agrega pero termina de recorrer el ciclo
        cont+=1

    return preguntas_a_mostar, respuestas_a_mostrar

def validar_respuesta(su_rta, rta_posibles):
    punto = 0
    for rta in rta_posibles:
        if "*" in rta:
            rta_correcta = rta.replace("*",'')
    print(rta_correcta)
    if su_rta == rta_correcta.upper():
        punto = 1
    
    return punto

def eleccion(preguntas_mostar, respuestas_mostrar):
    #preguntas =  {id_pregunta: pregunta}
    #respuestas = {id_pregunta: [rta1,rta2,rta,3]}
    puntos_totales = 0
    for id, pregunta in preguntas_mostar.items():
        print(f"{preguntas_mostar[id]}")    #la pregunta
        rta_posibles = respuestas_mostrar[id]
        for respuesta in rta_posibles:
            print(respuesta.replace("*",''))        #las rtas
        su_rta = input("ingrese su rta: ").upper()
        punto = validar_respuesta(su_rta, rta_posibles)
        puntos_totales += punto #0 si esta mal 1 si esta bien

    return puntos_totales


def jugar(preguntas:dict, respuestas:dict, cant, dificultad)->None:
    #ESTRUCTURA ELEGIDA:
    #preguntas = {id_pregunta: [pregunta, dificultad]}
    #respuestas = {id_pregunta: [rta_1, rta_2, rta_n]}
    
    preguntas_mostar, respuestas_mostrar = filtro_preg(preguntas, respuestas, dificultad, cant)
    puntos_totales = eleccion(preguntas_mostar, respuestas_mostrar)
    return puntos_totales
    
#a- Solicitar al usuario su nombre, cantidad de preguntas a mostrar y dificultad #OK!

def agregar_score(score:list)->None:
    #score = [efectividad, nombre]  
    with open('score.txt', 'a') as arch:
        linea = str(score[0])+","+ score[1]+"\n"
        arch.write(linea)

def mostrar_score_historico():
    #score = [[efectividad, nombre],]
    scores = list()  
    with open('score.txt', 'r') as arch:
        for linea in arch:                
            linea = linea.strip('\n')
            datos = linea.split(',')
            scores.append([float(datos[0]),datos[1]])
    ##print(scores)
    scores.sort(reverse = True)
    ##print(scores)
    print("puntaje  jugador")
    for partida in scores:
        print(f"{partida[0]} {partida[1]}")


def main():
    opciones = ["1) Comenzar partida  ",
                "2) Mostar score historico",
                "3) Sair del juego"
                ]   
    
    preguntas = obtener_preguntas()
    respuestas = obtener_respuestas()
    
    salir = False
    while not salir:
        for opc in opciones:
            print(opc)
        
        opc = validar_opcion(1,3,"Elija una opcion: ")        

        if opc == "1":
            nombre, cant_preg, dificultad = info_usuario()
            puntos_totales = jugar(preguntas, respuestas, cant_preg, dificultad)
            efectividad = (puntos_totales/cant_preg)*100
            print(f"Su efectividad fue del {efectividad} %")
            score = [efectividad, nombre]  
            agregar_score(score)

        elif opc == "2":
            mostrar_score_historico()

        elif opc == "3":
            salir = True
            
main()