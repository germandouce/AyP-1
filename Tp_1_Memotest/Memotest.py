def datos_jugadores() -> tuple:
    """
    GRAL: pide datos de los jugadores jugadores
    ARGS: no recibe argumentos
    RETURNS: los nombres de los 2 jugadores
    """
    jug_1 = input ('Ingrese nombre del jugador 1: ')
    jug_2 = input ('Ingrese nombre del jugador 2: ')

    return jug_1, jug_2


def duracion():
    """
    ARGS: no recibe argumentos
    GRAL:defino duracion del juego
    RETURN: devuelve una variable con la duracion
    """
    print("Defini duracion del juego")

    pass


def proba_cartas():
    """
    ARGS: No recibe argumentos
    GRAl: Defino proba de cada carta. solo va a devolver 4 valores n una lista, 1 xa ca carta
    RETURNS: lista con 4 valores de probabilidad
    """
    pass


def parametros() -> tuple:
    """
    GRAL: define los parametros del juego n.
    ARGS: numero de juego
    RETURN: duarcion del juego en  una variable variable y lista con probabilidad de cada carta
    """
    duracion = duracion()
    #proba_cartas = proba_cartas()
    proba_cartas = [0.1,0.2,0.3,0.4]
    return duracion, proba_cartas 


def crear_tableros(duracion: int) -> list:
    """
    GRAL:crea los dos tableros
    ARGS: la duracion ingresada en parametros()
    RETURNS: 2 listas de listas con tableros
    """
    if duracion == 1:
        tablero_1 = []
    #elif duracion = 2:
    
    #else:

    pass


def cargar_tableros():
    """
    GRAL:carga los dos tableros
    RETURNS: 2 listas de listas con tableros
    """
    pass


def nueva_partida():
    """crea una nueva partida, solo trae el numero de partida como parametro xa mejor refrerencia
    """
    jug_1 ,jug_2 = datos_jugadores()
    duracion, proba_cartas = parametros()
    crear_tableros(duracion)
    cargar_tableros()
    pass


def score():
    """
    muestra lista vacia si es primera partida, sino muestra scores
    """
    pass


def menu_principal():
    """
    recibe numero de partida, xa el score, si es primera partida muestra lista vacia
    """
    seguir = True
    while seguir:
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

        seguir = input('Desea permanecer del menu principal? 1-Si otro-No: ')
        if seguir =='1':
            seguir = True       
        else:
            seguir = False


def mostrar_tablero():
    """
    muestra el tablero
    """
    pass


def elegir_ficha():
    """
    Eleccion de fichas a v er si coinciden
    """
    pass


def pareja_encontrada():
    """
    GRAL: devuelve un bool si encontro o no la pareja
    ARGS: fichas del jugador
    RETURNS: bool
    """
    pass


def hacer_memoria():
    """
    GRAL: muestra tableros y permite jugar. si encontro correcta// (pareja_enconyrada(), corre de nuevo
    hasta q pierda)
    ARGS: recibe el tablero del judaor a o b
    RETURNS: el tablero nuevo segun lo q adivini
    """
    mostrar_tablero()
    elegir_ficha()
    pareja_encontrada()
    pass


def levantar_carta():
    """
    GRAL: ahora q termino el turno, xq perdio levanta carta. aca se calcula efectivamente q carta toca
    segun las probas definidas en funcion  parametrso
    ARGS:  IMPORTANTE, probabilidades de cada carta xa q aqui se haga efectivamente el calculo con random
    RETURNS: devuelve la carta q toco
    """
    pass


def guardar_carta():
    """
    GRAL: nada, hacmos una lista xa cada jugador xa q guarde sus cartas
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
    Gral: se juega la carta q toco en levantar carta. incluir pocibilidad de jugar mas de una carta
    de las q se guardaron en guardar carta.
    ARGS: cartas guardadas de guardar carta
    Returns: devuelve el tablero cambiado segun la carta, sino, s epierde los cambios ojo
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
    GRAL:el juego en si
    ARGS: recibe el numero d ejuego (puede ser util), los tableros, LAS PROBABILIDADES de cada carta
    damos opcion de jugar carta inmediatamente o guardarla.
    RETURNS: gano o alguien o no y quien
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
    ARGS: datos jugador
    RETURNS: nada. solo guarda,
    """
    pass


def main():
    """
    con un for in range (4) corre xa cada partida
    defino variable con nuemero de partida ()
    """
    menu_principal()
    jugando()
    guardar_score()

main()
