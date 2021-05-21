from random import randint, choice, shuffle 

def validar_opcion(opc_minimas: int, opc_maximas: int) -> str:
    '''
    PRE:Recibe dos números enteros que simbolizan la cantidad de opciones posibles.
    Post: Retorna un número entero dentro del rango de opciones.
    '''
    opc = input("Ingrese una opción: ")
    while not opc.isnumeric() or int(opc) > opc_maximas or int(opc) < opc_minimas:
        opc = input("Por favor, ingrese una opcion valida: ")
    
    return opc


def duracion_juego() -> int:
    """
    PRE: no recibe argumentos
    POST: devuelve una entero con el tamaño de la matriz (correspondiente a la duracion)
    """
    print("Defini duracion del juego")
    print('0 - corto\n1 - Medio\n2 - Largo')
    opc = input('')
    while (not opc.isnumeric) or (opc not in ('0','1','2') ):
        opc = input('Por favor ingrese una opcion valida: ')
    opc = int(opc)

    if opc ==0:
        tam_matriz = 4
    elif opc == 1:
        tam_matriz = 8
    elif opc == 2:
        tam_matriz = 12

    return tam_matriz


def proba_cartas():
    """
    PRE: No recibe argumentos
    POST: Defino proba de cada carta. solo va a devolver 4 valores  de probabilidad
    n una lista, 1 xa cada carta
    """
    pass


def crear_tablero(tam_matriz: int) -> list:
    """
    PRE: tam_matriz es un entero pedido en la funcion 'duracion_juego()'
    POST: devuelve la lista de listas 'tablero' con el tablero creado
    """
    tablero=[]
    for fila in range(tam_matriz):
        tablero.append([])
        for columna in range(tam_matriz):
            tablero[fila].append('')
    
    return tablero


def preparar_carga_tablero(tam_matriz: int) -> list:
    """
    PRE: tam_matrix es el tamaño de la matriz
    POST: devuelve la lista 'elementos_xa_tablero' con los elementos a cargar en los 
    tableros (ambos tableros tienen los mismos elementos)
    """
    elementos =['H', 'He', 'Li', 'Be', 'B', 'C', 'N', 'O', 'F', 'Ne', 'Na', 'Mg', 'Al', 'Si', 'P', 
    'S', 'Cl', 'Zr', 'Ar', 'K', 'Ca', 'Sc', 'Ti', 'V','Cr', 'Mn', 'Fe', 'Co', 'Ni', 'Cu', 'Zn', 
    'Ga',  'Ge', 'As', 'Se', 'Br', 'Kr', 'Rb', 'Sr', 'Y', 'Ru', 'Ag', 'Cd', 'In', 'Sn', 'Sb', 'Te', 
    'I', 'Xe', 'Cs', 'Ba', 'Ce', 'Pr', 'Nd', 'Pm', 'Sm', 'Eu', 'Gd', 'Lu', 'Pt', 'Au', 'Hg', 'Pb', 
    'Bi', 'Po', 'Rn', 'Fr', 'Ra', 'U', 'Np','Es', 'Rf']
    
    elementos_xa_tablero =[]

    for i in range(int((tam_matriz**2)/2)):
        elegido = choice(elementos)
        elementos_xa_tablero.append(elegido)
        elementos_xa_tablero.append(elegido)
        elementos.pop(elementos.index(elegido))
    
    return elementos_xa_tablero


def cargar_tablero(tablero:list, elementos_xa_tablero:list) -> list:
    """
    PRE: 'tam_matriz' es el tamaño de la matriz, 'tablero' es el tablero creado pero vacio, 
    'elementos_xa_tablero' son los elemntos que se cargaran en el tablero
    POST: devuelve la lista de listas 'tablero' con el tablero ya cargado
    """

    shuffle(elementos_xa_tablero)
    print(elementos_xa_tablero)

    indice = 0
    for fila in range(len(tablero)):
        for columna in range(len(tablero)): #en la pos i,j meto una lista con 2 elementos, el 1ero,
            tablero[fila][columna] = [elementos_xa_tablero[indice],'*']  #la ficha el 2do un 
            indice += 1     #indicador de si fue adivinada o no
                            #  *   signfica NO ADIVINADA; ' ' significa YA ADIVINADA
    return tablero


def nueva_partida(tam_matriz) -> tuple:
    """
    PRE: cuando la funcion este terminada, va a recibir el numero de partida
    POST: crea una nueva partida, devolviendo 2 listas con  los tableros creados y cargados
    """
    tablero_1 = crear_tablero(tam_matriz)  
    tablero_2 = crear_tablero(tam_matriz)  

    elementos_xa_tablero = (preparar_carga_tablero(tam_matriz))

    tablero_cargado_1 = cargar_tablero(tablero_1, elementos_xa_tablero)
    tablero_cargado_2 = cargar_tablero(tablero_2, elementos_xa_tablero)
 
    return tablero_cargado_1, tablero_cargado_2


def score():
    """
    PRE: por ahora nada...
    POST: no devuelve nada. solo printea que no se jugaron partidas si es la primera, 
    sino muestra ultimos 4 scores
    """
    pass


def mostrar_tablero(tablero:list) -> None:
    """
    PRE: 'tablero' es el tablero del juagador que corresponda
    POST: No devuelve nada solo muestra el tablero
    """
    for i in range(len(tablero)):
                for j in range(len(tablero)):
                    if tablero[i][j][1] == ' ':   # en [1] está el indicador de adivinado (* o ' ')
                        print(tablero[i][j][0].ljust(2), end ='  ') # en [0] esta la ficha
                    else:
                        print('*'.ljust(2), end = '  ')
                print()


def pareja_encontrada(tablero: list):
    """
    PRE: fichas del jugador
    POST: devuelve un bool si encontro o no la pareja
    """
    pass


def elegir_ficha(tablero:list):
    """
    PRE:
    POS: Eleccion de fichas xa ver si coinciden. De aca se deduciran otras funciones xa corrborar
    si fue correcta la eleccion o no y xa la consiguiente modificacion del tablero.
    """
    pareja_encontrada(tablero)
    pass


def hacer_memoria(tablero:list):
    """
    GRAL: muestra tableros y permite jugar. si encontro correcta// (pareja_enconyrada(), corre de 
    nuevo hasta q pierda)
    PRE: recibe el tablero del judaor a o b
    POST: devuelve el tablero nuevo segun lo q adivinado
    """
    mostrar_tablero(tablero)
    elegir_ficha(tablero)
    pass


def levantar_carta():
    """
    GRAL: ahora q termino el turno xq perdio, se levanta carta. Aca se calcula efectivamente q carta
    toca segun las probas definidas en funcion proba_carta()
    PRE:  IMPORTANTE, probabilidades de cada carta xa q aqui se haga efectivamente el calculo con 
    random
    POST: devuelve la carta o no carta q haya tocado
    """
    pass


def guardar_carta():
    """
    PRE: recibe la carta
    GRAL: hacemos listas xa q cada jugador guarde sus cartas
    POST: no devuelve nada. solo guarda la carta
    """
    pass


def carta_replay():
    """
    """
    pass


def carta_layout():
    """
    """
    pass


def carta_toti():
    """
    """
    pass


def carta_fatality():
    """
    """
    pass


def jugar_carta():
    """
    si el jugador así lo deseó
    GRAL: incluir posibilidad de jugar mas de una carta e las q se guardaron en guardar carta.
    Las funciones se ejecutan segun la carta q se juegue
    PRE: cartas guardadas de guardar carta y el tablero
    POST: en principio, si no entendi mal, no devuelve nada. xq el tablero se modifica x 
    referencia.
    """
    carta_replay()
    carta_layout()
    carta_toti()
    carta_fatality()
    pass


def gano_alguien() -> bool:
    """
    GRAL: Chequea si el jugador gano o no, xa ver si arranco de nuevo el loop cambiando de turno
    OJO VER COMO CHEQUEO ESO...
    RETURN: un bool si gano o no
    # """
    gano = False
    print('gano? 1\n1 - si\n2 - no')
    lo_hizo = int(validar_opcion(1,2))

    if lo_hizo == 1:
        gano = True
    
    return gano      

def jugando(tablero_cargado_1: list, tablero_cargado_2: list):
    """
    GRAL: el juego en si. Primero se inenta encontrar las cartas iguales. Dsps con otras funciones 
    se levanta la carta ys juega.
    PRE: recibe el numero d ejuego (puede ser util), los tableros, LAS PROBABILIDADES de cada carta
    La carta se guarda predeterminada//. Dsps damos opcion de jugar carta inmediata// o no.
    POST: devuelve si gano alguien y quien
    """
    no_gano = False
    while  no_gano:
        turno = 0
        while turno !=2 and no_gano:
            print(turno)
            if turno == 0:
                print('trablero 1')
                tablero = tablero_cargado_1
            else:
                print('tablero 2')
                tablero = tablero_cargado_2
            no_gano = hacer_memoria(tablero)
            levantar_carta()
            guardar_carta()
            jugar_carta()
            turno += 1


def guardar_score():
    """
    GRAL: cuando alguien gano, se guarda su score. va a haber 4 scores en total. Aqui tengo q crear la
    lista con los scores xa consultar dsps.
    PRE: datos jugador
    POST: nada. solo guarda scores
    """
    pass


def main() -> None:
    """
    GRAL: Menu principal del juego.
     con un for in range (4) corre xa cada partida
    definir variable con numero de partida (). cuando se acaba guarda el score de dicha partida.
    """
    salir_del_juego = False
    while not salir_del_juego:        
        salir_del_menu_principal = False
        iniciada = False
        while not salir_del_menu_principal:
            print("---MENU PRINCIPAL---")
            print("0 - Nueva partida\n1 - Comenzar partida\n2 - Mostrar scores")

            opc = int(validar_opcion(0,2))

            if opc == 0:
                jug_1 = input ('Ingrese nombre del jugador 1: ')
                jug_2 = input ('Ingrese nombre del jugador 2: ')
                
                tam_matriz = duracion_juego()
                
                probabilidades = proba_cartas()
                
                tablero_cargado_1, tablero_cargado_2 = nueva_partida(tam_matriz)

                iniciada = True

            elif opc == 1: 
                if iniciada:
                    salir_del_menu_principal = True
                else:
                    print('\nDebe crear una nueva partida antes de comenzarla\n')
                    salir_del_menu_principal = False
            
            elif opc == 2:
                score()

            else:
                salir_del_menu_principal = True
                
        jugando(tablero_cargado_1, tablero_cargado_2)
        guardar_score()
        
        print('0 - Volver al menu principal\n1 - Salir del juego')
        opc = int(validar_opcion(0,1))
        if opc == 1:
            print('Esta seguro que desea salir del juego? Se perderan los scores')
            print('1-Si\n2 - No')
            si_quiero_salir = int(validar_opcion(1,2))

            if si_quiero_salir == 1:
                #salir_del_menu_principal = True
                salir_del_juego = True

main()
