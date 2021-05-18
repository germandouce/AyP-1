def datos_jugadores():
    """
    pide datos jugadores
    """
    pass


def duracion():
    """
    defino duracion del juego
    """
    pass


def proba_cartas():
    """
    defino proba de cada carta. solo va a devolver 4 valores n una lista, 1 xa ca carta
    """
    pass


def parametros():
    """
    define los parametros del juego n.
    Args:
    returns: duarcion del juego en variable y lista con probabilidad de cada carta
    """
    duracion()
    proba_cartas() 
    pass


def crear_tableros():
    """
    GRAL:crea los dos tableros
    RETURNS: 2 listas de listas con tableros
    """
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
    datos_jugadores()
    parametros()
    crear_tableros()
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
    nueva_partida()
    score()


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
