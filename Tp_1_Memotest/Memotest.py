from random import randint, choice, shuffle 

def validar_opcion(opc_minimas: int, opc_maximas: int, texto: str = '') -> str:
    '''
    PRE: Recibe dos números enteros que simbolizan la cantidad de opciones posibles.
    Post: Retorna un número entero en formato str dentro del rango de opciones
    '''
    opc = input("{}".format(texto))
    while not opc.isnumeric() or int(opc) > opc_maximas or int(opc) < opc_minimas:
        opc = input("Por favor, ingrese una opcion valida: ")
    
    return opc


def duracion_juego() -> int:
    """
    PRE: no recibe argumentos
    POST: devuelve una entero con el tamaño de la matriz (correspondiente a la duracion)
    """
    print("\nDefini duracion del juego")
    print('0 - corto\n1 - Medio\n2 - Largo')
    opc = int( validar_opcion(0,2) )

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
    print("\nDefini la probabilidad de salida de las cartas especiales")
    print('0 - Tradcional\n1 - Piknte\n2 - Muy piknte')
    print()
    cartas = 'Replay', 'Layout', 'Toti', 'Fatality' 

    opc = int( validar_opcion(0,3) )

    if opc ==0:
        lista_probas = [0, 0, 0, 0]
    elif opc == 1:
        lista_probas = [0.3, 0.1, 0.2, 0.2]
    else:
        lista_probas = [0.4, 0.2, 0.3, 0.3]
    
    print('\nUsted eligio las siguientes probabilidades para sus cartas:')
    for i in range ( len(cartas) ) :
        print(f'{ cartas[i] }: { int( lista_probas[i] * 100 ) } %' )

    #"boton"acepetar

    return lista_probas


def crear_tablero(tam_matriz: int) -> list:
    """
    PRE: tam_matriz es un entero pedido en la funcion 'duracion_juego()'
    POST: devuelve la lista de listas 'tablero' con el tablero creado
    """
    tablero = []

    for fila in range(tam_matriz):
        tablero.append([])
        for columna in range(tam_matriz):
            tablero[fila].append('')
    
    return tablero


def preparar_carga_tablero(tam_matriz: int) -> list:
    """
    PRE: 'tam_matrix' es el tamaño del tablero
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
    
    print('Elementos con los que se jugará (SOLO PARA TESTEO!)')   #(Verion Beta)solo xa facilitar testeo del juego
    print(elementos_xa_tablero)             

    return elementos_xa_tablero


def cargar_tablero(tablero:list, elementos_xa_tablero:list) -> list:
    """
    PRE: 'tablero' es el tablero ya creado pero vacio, 'elementos_xa_tablero' son los elemntos 
    que se cargaran en el tablero
    POST: devuelve la lista de listas 'tablero' con el tablero ya cargado
    """

    shuffle(elementos_xa_tablero) #mezclo los elementos antes de cargarlos

    indice = 0
    for fila in range(len(tablero)):
        for columna in range(len(tablero)): #en la pos i,j meto una lista con 2 elementos, el 1ero,
            tablero[fila][columna] = [elementos_xa_tablero[indice],'*']  #la ficha el 2do un 
            indice += 1     #indicador de si fue adivinada o no
                            #  *   signfica NO ADIVINADA; ' ' significa YA ADIVINADA
    return tablero


def nueva_partida(tam_matriz) -> tuple:
    """
    PRE: 'tam_matriz' es el tamaño del tablero
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
    POST: Muestra el tablero con las fichas adivinadas hasta el momento ya dadas vuelta. Las no
    adivinadas, aparecen como *
    """
    for i in range(len(tablero)):
                for j in range(len(tablero)):
                    if tablero[i][j][1] == ' ':   # en [1] está el indicador de adivinado (* o ' ')
                        print(tablero[i][j][0].ljust(2), end ='  ') # en [0] esta la ficha
                    else:
                        print('*'.ljust(2), end = '  ')
                print()


def ingreso_coordenadas(tablero) -> tuple:
    """
    PRE: recibe 'tablero', para conocer su tamaño
    POST: devuelve una tupla con las coordenadas de la ficha elegida
    """
    fila = int (validar_opcion (1, len(tablero),'Ingrese fila: ') ) - 1    #resto 1 puesto que en las listas de lisats
    
    columna =  int (validar_opcion (1, len(tablero), 'Ingrese columna: ' )) -1 #del tablero estas empiezan con indice "0"

    ficha = fila, columna

    return ficha


def mostrar_tablero_parcial(tablero:list, ficha: tuple) -> None:
    """
    PRE: 'tablero' es el tablero del juagador que corresponda
    POST: Muestra el tablero con las fichas adivinadas hasta el momento ya dadas vuelta junto con
    la ficha que se acaba de elegir en el turno
    """
    print()
    for i in range(len(tablero)):
        for j in range(len(tablero)):
            if i == ficha[0] and j == ficha[1] : 
                print(tablero[i][j][0].ljust(2), end ='  ')

            elif tablero[i][j][1] == ' ':   # en [1] está el indicador de adivinado (* o ' ')
                print(tablero[i][j][0].ljust(2), end ='  ') # en [0] esta la ficha

            else:
                print('*'.ljust(2), end = '  ')
        print()
    
    print()
                    

def elegir_ficha(tablero:list) -> tuple:
    """
    PRE: 'tablero', es necesario para conocer columnas y filas maximas
    POST: devuelve una tupla con las fichas elegidas, cada una de las cuales es una tupla 
    con coordenadas. Tambien muestra al usuario las fichas elegidas con mostrar_tablero_parcial()
    """
    print('INGRESE COORDENADAS FICHA 1')
    ficha_1 = ingreso_coordenadas(tablero)
    mostrar_tablero_parcial(tablero, ficha_1) 
    
    print('INGRESE COORDENADAS FICHA 2')
    ficha_2 = ingreso_coordenadas(tablero) 

    while ficha_1 == ficha_2:  #no quiero q ingrese 2 veces las mismas coordenadas xq me las destapa
        print('\nPor favor, ingresá un ficha distinta a la primera') #xa siempre (con mi algoritmo) 
        ficha_2 = ingreso_coordenadas(tablero)
    
    mostrar_tablero_parcial(tablero, ficha_2)

    return ficha_1, ficha_2


def chequeo_pareja(tablero: list, ficha_1: tuple, ficha_2: tuple) -> bool:
    """
    PRE: 'tablero' es el tablero de quien corresponda, 'ficha_1 / 2' son las fichas elegidas por el
    jugador
    POST: devuelve el bool 'perdio', (por si o por no). si no
    perdio, además desbloquea esa ficha del tablero
    """
    perdio = True
    
    if ( tablero[ ficha_1[0] ][ ficha_1[1] ] [0] ) == ( tablero [ficha_2[0] ][ ficha_2[1] ] [0] ) :
        
        tablero [ ficha_1[0] ][ ficha_1[1] ] [1] = ' '   #si adivino, cambio * por espacio ' '
        tablero [ ficha_2[0] ][ ficha_2[1] ] [1] = ' '
        
        perdio = False
        
        print('Muy bien!, puede elegir de nuevo\n')

    
    else:
        print('No eran iguales!\n')

    return perdio


def gano_el_juego(tablero):
    
    """
    PRE: 'tablero' es el tablero de quien corresponda
    POST: devuelve el bool gano_juego, True si gano, Falso si no gano
    """
    alguien_gano_juego = True #es decir, es verdadero que alguien gano

    for i in range(len(tablero)):
            for j in range(len(tablero)):   
                if tablero[i][j][1] == '*': #si llego a encontrar un * , es decir, un NO ADIVINADO
                    #entonces, es falso que alguien gano. En ese caso, 
                    alguien_gano_juego = False                  

    return alguien_gano_juego



def hacer_memoria(tablero:list) -> bool:
    """
    GRAL: muestra tableros y permite jugar. si encontro correcta// ( chequeo_pareja() ), corre de 
    nuevo hasta q pierda o hasta ganar el juego (gano_el_juego () ) 
    PRE: recibe el tablero del judaor 1 o 2
    POST: devuelve el tablero nuevo segun lo q adivinado
    """
    gano_juego = False
    perdio = False
    while (not perdio) and (not gano_juego):   #debe cumplirse que no perdio y que no gano

        
        print('\nTablero (SOLO XA TESTEO!!)',tablero) #Solo para facilitar testeo del juego. 
                             #Muestra la lista de listas del tablero 
                           #(copiarse xa hacer ganar a un jugador mas rápido)
        mostrar_tablero(tablero)
        
        ficha_1, ficha_2 = elegir_ficha(tablero)
        
        perdio = chequeo_pareja(tablero, ficha_1, ficha_2)
        
        gano_juego = gano_el_juego(tablero)
    
    return gano_juego

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


def jugando(tablero_cargado_1: list, tablero_cargado_2: list, jug_1: str, jug_2: str) -> str:
    """
    GRAL: el juego en si. Primero se inenta encontrar las cartas iguales. Dsps con otras funciones 
    se levanta la carta y se juega.
    PRE: recibe tableros cargados, LAS PROBABILIDADES de cada carta
    La carta se guarda predeterminada//. Dsps damos opcion de jugar carta inmediata// o no.
    POST: devuelve el ganador del juego en la variable 'ganador'

    """
    gano_juego = False
    turno = 1
    while not gano_juego :

            #print(turno)    #para facilitar testeo (turnos impares -> jug 1, turnos pares -> jug 2)

            if turno %2 != 0:
                print('Turno de {}\nTablero 1'.format(jug_1.upper() ) )
                tablero = tablero_cargado_1
                ganador = jug_1
            else:
                print('Turno de {}\nTablero 2'.format(jug_2.upper() ) )
                tablero = tablero_cargado_2
                ganador = jug_2

            gano_juego = hacer_memoria(tablero)

            levantar_carta()
            guardar_carta()
            jugar_carta()
            
            print('FIN DEL TURNO DE {}'.format(ganador.upper() ) ) 
            print('presione cualquier tecla para seguir jugando') #mas comodidad xa jugar
            input()                                           

            turno += 1
        
    return ganador

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
    GRAL: Menu principal del juego. cuando se acaba cada partida guarda el score de dicha partida.
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
                jug_1 = input ('\nIngrese nombre del jugador 1: ')
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
                
        ganador = jugando(tablero_cargado_1, tablero_cargado_2, jug_1, jug_2)

        print('¡Felicidades! Haz ganado {}'.format(ganador.upper() ) )

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
