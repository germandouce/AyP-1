def duracion():
    """
    PRE: no recibe argumentos
    POST: devuelve una variable con la duracion del juego
    """
    print("Defini duracion del juego")

    pass


def proba_cartas():
    """
    PRE: No recibe argumentos
    POST: Defino proba de cada carta. solo va a devolver 4 valores  de probabilidad
    n una lista, 1 xa cada carta
    """
    pass


def crear_tableros(duracion: int) -> list:
    """
    PRE: duarcion es un entero pedido en la funcion duracion()
    POST: devuelve 2 listas de listas con tableros
    """
    if duracion == 1:
        tablero_1 = []
    #elif duracion = 2:
    
    #else:

    pass


def cargar_tableros():
    """
    PRE: No recibe argumentos
    RETURNS: devuelve 2 listas de listas con los tableros cargados
    """
    pass


def nueva_partida():
    """
    PRE: cuando este terminada, va a recibir el numero de partida
    POST: crea una nueva partida, devolviendo 2 listas con  los tableros creados y cargados
    """
    jug_1 = input ('Ingrese nombre del jugador 1: ')
    jug_2 = input ('Ingrese nombre del jugador 2: ')

    duracion()
    proba_cartas()
    crear_tableros(duracion)
    cargar_tableros()
    pass


def score():
    """
    PRE: por ahora nada...
    POST: no devuelve nada. solo printea que no se jugaron partidas si es la primera, 
    sino muestra ultimos 4 scores
    """
    pass


def menu_principal():
    """
    PRE: numero de partida
    POST: no devuelve nada, simplemente es un menu de opciones
    """
    salir = False
    while not salir:
        print("MENU PRINCIPAL")
        print("0 - nueva partida\n1 - mostrar ultimos 4 scores")

        opc = input('')
        while (not opc.isnumeric) or (opc not in ('0','1') ):
            opc = input('Por favor ingrese una opcion valida: ')
        opc = int(opc)

        if opc == 0:
            nueva_partida()
        else:
            score()

        salir = input('Desea salir del menu principal? 1-Si otro-No: ')
        if salir =='1':
            salir = True       
        else:
            salir = False 


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
    
    RETURNS: bool
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


def hacer_memoria():
    """
    GRAL: muestra tableros y permite jugar. si encontro correcta// (pareja_enconyrada(), corre de 
    nuevo hasta q pierda)
    PRE: recibe el tablero del judaor a o b
    POST: devuelve el tablero nuevo segun lo q adivinado
    """
    mostrar_tablero()
    elegir_ficha()
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
    Returns: en principio, si no entendi mal, no devuelve nada. xq el tablero se modifica x 
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
    


def jugando():
    """
    GRAL: el juego en si. Primero se inenta encontrar las cartas iguales. Dsps con otras funciones 
    se levanta la carta ys juega.
    PRE: recibe el numero d ejuego (puede ser util), los tableros, LAS PROBABILIDADES de cada carta
    La carta se guarda predeterminada//. Dsps damos opcion de jugar carta inmediata// o no.
    POST: devuelve si gano alguien y quien
    """
    hacer_memoria()
    levantar_carta()
    guardar_carta()
    jugar_carta()
    ganar()


def guardar_score():
    """
    GRAL: cuando alguien gano, se guarda su score. va a haber 4 scores en total. Aqui tengo q crear la
    lista con los scores xa consultar dsps.
    PRE: datos jugador
    POSTS: nada. solo guarda scores
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
