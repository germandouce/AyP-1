from random import randint, choice, shuffle 

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

    print(int((tam_matriz**2)/2))
    shuffle(elementos_xa_tablero)
    print(elementos_xa_tablero)

    return elementos_xa_tablero

def cargar_tablero(tam_matriz, tablero, elementos_xa_tablero) -> list:
    """
    PRE: 'tam_matriz' es el tamaño de la matriz, 'tablero' es el tablero creado pero vacio, 
    'elementos_xa_tablero' son los elemntos que se cargaran en el tablero
    POST: devuelve la lista de listas 'tablero' con el tablero ya cargado
    """
    
    indice = 0
    for fila in range(tam_matriz):
        for columna in range(tam_matriz):
            tablero[fila][columna] = elementos_xa_tablero[indice]
            indice += 1 
    
    return tablero


def mostrar_tablero_temporal(tablero, tam_matriz) -> None:
    for i in range(tam_matriz):
        for j in range(tam_matriz):
            print(tablero[i][j].ljust(2), end ='  ')
        print()


def nueva_partida(tam_matriz) -> tuple:
    """
    PRE: cuando la funcion este terminada, va a recibir el numero de partida
    POST: crea una nueva partida, devolviendo 2 listas con  los tableros creados y cargados
    """
    tablero_1 = crear_tablero(tam_matriz)  
    tablero_2 = crear_tablero(tam_matriz)  

    elementos_xa_tablero = preparar_carga_tablero(tam_matriz)

    tablero_cargado_1 = cargar_tablero(tam_matriz, tablero_1, elementos_xa_tablero)
    tablero_cargado_2 = cargar_tablero(tam_matriz, tablero_2, elementos_xa_tablero)
 
    return tablero_cargado_1, tablero_cargado_2


def score():
    """
    PRE: por ahora nada...
    POST: no devuelve nada. solo printea que no se jugaron partidas si es la primera, 
    sino muestra ultimos 4 scores
    """
    pass


def menu_principal() -> tuple:
    """
    PRE: numero de partida
    POST: no devuelve nada, simplemente es un menu de opciones
    """
    tablero_cargado_1, tablero_cargado_2 = nueva_partida()
    

    iniciada = False
    salir = False
    while not salir:
        print("---MENU PRINCIPAL---")
        print("0 - Nueva partida\n1 - Comenzar partida\n2 - Mostrar scores")

        opc = input('')
        while (not opc.isnumeric) or (opc not in ('0','1','2') ):
            opc = input('Por favor ingrese una opcion valida: ')
        opc = int(opc)

        if opc == 0:
            jug_1 = input ('Ingrese nombre del jugador 1: ')
            jug_2 = input ('Ingrese nombre del jugador 2: ')
            tam_matriz = duracion_juego()
            probabilidades = proba_cartas()
            tablero_cargado_1, tablero_cargado_2 = nueva_partida(tam_matriz)

            iniciada = True

        elif opc == 1: 
            if iniciada:
                salir = True
            else:
                print('Debe crear una nueva partida antes de comenzarla')
                salir = False
        
        else:
            score()
    
    return tablero_cargado_1, tablero_cargado_2


def mostrar_tablero():
    """
    PRE:
    POST: no devuelve nada. Muestra el tablero
    """
    pass


def pareja_encontrada():
    """
    PRE: fichas del jugador
    POST: devuelve un bool si encontro o no la pareja
    """
    pass


def elegir_ficha():
    """
    PRE:
    POS: Eleccion de fichas xa ver si coinciden. De aca se deduciran otras funciones xa corrborar
    si fue correcta la eleccion o no y xa la consiguiente modificacion del tablero.
    """
    pareja_encontrada()
    pass


def hacer_memoria(tablero:list ):
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


def ganar():
    """
    GRAL: Chequea si el jugador gano o no, xa ver si arranco de nuevo el loop cambiando de turno
    OJO VER COMO CHEQUEO ESO...
    RETURN: un bool si gano o no
    """
    pass
    

def jugando(tablero_cargado_1: list, tablero_cargado_2: list):
    """
    GRAL: el juego en si. Primero se inenta encontrar las cartas iguales. Dsps con otras funciones 
    se levanta la carta ys juega.
    PRE: recibe el numero d ejuego (puede ser util), los tableros, LAS PROBABILIDADES de cada carta
    La carta se guarda predeterminada//. Dsps damos opcion de jugar carta inmediata// o no.
    POST: devuelve si gano alguien y quien
    """
    if turno = jug1
        tablero = tablero_cargado_1
    else:
        tablero = tablero_cargado_2

    hacer_memoria(tablero)
    levantar_carta()
    guardar_carta()
    jugar_carta()
    ganar()


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
    GRAL: con un for in range (4) corre xa cada partida
    definir variable con numero de partida (). cuando se acaba guarda el score de dicha partida.
    """
    menu_principal()
    jugando()
    guardar_score()

main()
