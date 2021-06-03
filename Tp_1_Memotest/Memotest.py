from random import randint, choice, shuffle 

def validar_opcion(opc_minimas: int, opc_maximas: int, texto: str = '') -> str:
    """
    PRE: "opc_minimas" y "opc_maximas" son dos números enteros que simbolizan la cantidad de opciones posibles.
    Post: Devuelve en formato string en la var "opc" un número entero dentro del rango de opciones.
    """
    opc = input("{}".format(texto))
    while not opc.isnumeric() or int(opc) > opc_maximas or int(opc) < opc_minimas:
        opc = input("Por favor, ingrese una opcion valida: ")
    
    return opc


def duracion_juego() -> int:
    """
    PRE: No recibe argumentos.
    POST: Devuelve el entero "tam_matriz" con el tamaño de la matriz (correspondiente a la duracion).
    """
    print("\nDefini duracion del juego")
    print('0 - corto (Agua) \n1 - Medio (Glucosa) \n2 - Largo (Dipalmitoilfosfatidilcolina) ')
    opc = int( validar_opcion(0,2) )

    if opc ==0:
        tam_matriz = 4
    elif opc == 1:
        tam_matriz = 8
    elif opc == 2:
        tam_matriz = 12

    return tam_matriz


def proba_cartas() -> list:
    """
    PRE: No recibe argumentos
    POST: Defino probabilidad de cada carta. Devuelve 5 valores en la lista "lista_probas" que representan. 
    la probabilidad de que salga cada carta (o ninguna).
    """
    print("\nDefini la probabilidad de salida de las cartas especiales")
    print('0 - Tradcional (PH 7)\n1 - Acido! (PH 3)\n2 - Muy Acido! (PH 1)')
    print()
    cartas = 'Replay', 'Layout', 'Toti', 'Fatality', 'No salga ninguna' 

    opc = int( validar_opcion(0,3) )

    if opc ==0:
        lista_probas = [0, 0, 0, 0, 0, 100] #0/10 turnos con carta
          #0 REPLAY, 0 layout , 0 toti, 0 fatality
    elif opc == 1: 
        lista_probas = [0, 10, 20, 30, 40, 100] #4/10 turnos con carta
        #0 - 10 Replay, 10 - 20 Layout, 20 - 30 Toti, 30 - 40 Fatality, 40 - 100 'n'
    else:
        lista_probas = [0, 20, 40, 60, 80, 100] #8/10 turnos con carta
        #0 - 10 Replay, 10 - 20 Layout, 40 - 60 Toti, 60 - 80 Fatality, 80 - 100 'n'

    #Esto se lee, 0 a 20 sale Replay, 20 a 40 sale Layout, 40 a 60 sale Toti, 60 a 80 sale Fatality, 80 a 100 
    #no sale ninguna carta. Asi, xa este caso, en 8/10 turnos sale carta 
    
    print('\nLas cartas tendran la siguiente probabilidad de salir:')
    for i in range ( len(cartas) ) :
        print(f'{ cartas[i] }: { int(lista_probas[i+1] - lista_probas[i]) } %' )

    print()

    return lista_probas


def crear_tablero(tam_matriz: int) -> list:
    """
    PRE: El entero "tam_matriz" representa el tamaño del tablero.
    POST: Devuelve la lista de listas "tablero" con el tablero creado.
    """
    tablero = list()

    for fila in range(tam_matriz): 
        fila_nueva = list()
        for columna in range(tam_matriz):
            fila_nueva.append('')
        tablero.append(fila_nueva)

    return tablero


def preparar_carga_tablero(tam_matriz: int) -> list:
    """
    PRE: el int "tam_matrix" es el tamaño del tablero.
    POST: Devuelve la lista de listas "elementos_xa_tablero" con los elementos a cargar en los 
    tableros (ambos tableros tienen los mismos elementos).
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
    
    #print('Elementos con los que se jugará (SOLO PARA TESTEO!)') #xa testear
    #print(elementos_xa_tablero)     #xa testear         

    return elementos_xa_tablero


def cargar_tablero(tablero:list, elementos_xa_tablero:list) -> list:
    """
    PRE: La lista de listas "tablero" es el tablero ya creado pero vacio, "elementos_xa_tablero" son los 
    elemntos que se cargarán en el tablero.
    POST: Devuelve la lista de listas "tablero" con el tablero ya cargado.
    """

    shuffle(elementos_xa_tablero) #mezclo los elementos antes de cargarlos

    indice = 0
    for fila in range(len(tablero)):
        for columna in range(len(tablero)): #en la pos i,j meto una lista con 2 elementos, el 1ero,
            tablero[fila][columna] = [elementos_xa_tablero[indice],'*']  #el 1ero, la ficha
            indice += 1                                                  #el 2do, un indicador de 
        #   *   signfica NO ADIVINADA; ' ' significa YA ADIVINADA         #si fue adivinada o no
    return tablero


def nueva_partida(tam_matriz: int) -> tuple:
    """
    PRE: el entero "tam_matriz" es el tamaño del tablero.
    POST: Crea una nueva partida, devolviendo las listas de listas "tablero_cargado_1" y "tablero_cargado_2"
    con los ya tableros creados y cargados.
    """
    tablero_1 = crear_tablero(tam_matriz)  
    tablero_2 = crear_tablero(tam_matriz)  

    elementos_xa_tablero = (preparar_carga_tablero(tam_matriz))

    tablero_cargado_1 = cargar_tablero(tablero_1, elementos_xa_tablero)
    tablero_cargado_2 = cargar_tablero(tablero_2, elementos_xa_tablero)
 
    return tablero_cargado_1, tablero_cargado_2


def mostrar_scores(scores:list) -> None:
    """
    PRE: la lista "scores" contiene los nombres de lo ganadores con la cantidad de partidas ganadas
    por cada uno.
    POST: No devuelve nada. Muestra en orden descendiente segun el puntaje, los nombres de los ganadores con
    la cantidad de partidas ganadas. Si no se han jugado partidas, se lo informa al usuario.
    """                               
    if len(scores)>0:       #Ordeno la lista "scores", mandandole con "key" las filas de la tabla es decir los
        scores.sort(reverse = True, key = lambda jugador: jugador[1] ) #jugadores "jugador". Luego, con Lambda
        for i in range( len(scores) ):                  #ordeno descendente// segun el puntaje de cada jugador     
            print(scores[i][0].ljust(10),scores[i][1])   #("jugador [1]")
    
    else:
       print('No se ha jugado ninguna partida todavía')


def mostrar_tablero(tablero:list) -> None:
    """
    PRE: La lista de listas "tablero" es el tablero del juagador que corresponda.
    POST: No devuelve nada. Muestra el tablero con las fichas adivinadas hasta el momento ya dadas vuelta. 
    Las no adivinadas, aparecen como *.
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
    PRE: La lista de listas "tablero" es necesaria para conocer su tamaño.
    POST: Devuelve la tupla "ficha" con las coordenadas de la ficha elegida.
    """
    fila = int (validar_opcion (1, len(tablero),'Ingrese fila: ') ) - 1    #resto 1 puesto que en las listas de lisats
    
    columna =  int (validar_opcion (1, len(tablero), 'Ingrese columna: ' )) -1 #del tablero estas empiezan con indice "0"

    ficha = fila, columna

    return ficha


def mostrar_tablero_parcial(tablero:list, ficha: tuple) -> None:
    """
    PRE: la lista de listas "tablero" es el tablero del jugador que corresponda, "ficha" es una tupla con las
    coordenadas de la ficha elegida.
    POST: No devuelve nada. Muestra el tablero con las fichas adivinadas hasta el momento ya dadas vuelta 
    junto con la ficha que se acaba de elegir en el turno. Las no adivinadas aparecen como *.
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
    PRE: La lista de listas "tablero", es necesaria para conocer columnas y filas maximas.
    POST: Devuelve la tupla ("ficha_1","ficha_2" ) con las fichas elegidas, cada una de las cuales es a su vez 
    una tupla con coordenadas. Tambien muestra al usuario las fichas elegidas con "mostrar_tablero_parcial()".
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
    PRE: La lista de listas "tablero" es el tablero de quien corresponda, "ficha_1" y "ficha_2" son las fichas 
    elegidas por el jugador.
    POST: Chequea y modifica el tablero cambiando * por ' ' para desbloquar la ficha del tablero en caso de 
    que las fichas hayan coincidido. Finalmente, devuelve el booleano "perdio" con True si acertó y False si
    adivino. 
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
    PRE: La lista de listas "tablero" es el tablero de quien corresponda.
    POST: Devuelve el booleano "alguien_gano_juego" con True si gano el juego, False si no gano el juego.
    """
    alguien_gano_juego = True #es decir, es verdadero que alguien gano

    for i in range(len(tablero)):
            for j in range(len(tablero)):   
                if tablero[i][j][1] == '*': #si llego a encontrar un * , es decir, un NO ADIVINADO
                    #entonces, es falso que alguien gano. En ese caso, 
                    alguien_gano_juego = False    #Modificar xa probar guardado y muestra de puntajes                  

    return alguien_gano_juego


def mostrar_tablero_xa_testeo(tablero: list) -> None:       #XA TESTEAR!!!
    """
    GRAL: FUNCION SOLO XA TESTEAR DEL JUEGO!!
    PRE: la lista de listas "tablero" es el tablero de quien corresponda.
    POST: No devuelve nada. Solo muestra rusticamente el tablero correspondiente.
    """
    for i in range( len(tablero) ):
        for j in range( len(tablero) ):
            print( tablero [i][j], end ='  ')
        print()                    


def hacer_memoria(tablero:list) -> bool:
    """
    GRAL: Muestra tableros y permite elegir fichas. Si se encontro correctamente la pareja con 
    "chequeo_pareja()" se ejecuta de nuevo hasta que las fichas elegidas no coincidan o hasta ganar el 
    juego, lo que se verifica con "gano_el_juego() ". 
    
    PRE: La lista de listas "tablero" es el tablero de quien corresponda.
    POST: Devuelve el booleano "gano_juego" con True si gano el juego y False en caso contrario. 
    Finalmente, modifica el tablero segun lo adivinado.
    """
    gano_juego = False
    perdio = False
    while (not perdio) and (not gano_juego):   #debe cumplirse que no perdio y que no gano

        
        # print('\nTablero (SOLO XA TESTEAR!!)' ) # #xa testear
        # mostrar_tablero_xa_testeo( tablero) #xa testear
        
        mostrar_tablero(tablero)
        
        ficha_1, ficha_2 = elegir_ficha(tablero)
        
        perdio = chequeo_pareja(tablero, ficha_1, ficha_2)
        
        gano_juego = gano_el_juego(tablero)
    
    return gano_juego


def carta_layout(tablero_a_molestar: list):
    """
    PRE: La lista de listas "tablero_a_molestar" es el tablero del oponente que busco modificar para hacerle 
    más dificil el juego.
    POST: No devuelve nada, MEZCLA ALEATORIAMENTE el tablero del oponente, "por referencia".
    """

    # print('tablero antes de mezclar') #xa testear
    # mostrar_tablero_xa_testeo(tablero_a_molestar) #xa testear
    
    print()

    elementos_xa_tablero_a_molestar = []
    
    for fila in range ( len(tablero_a_molestar) ):
        for columna in  range (len(tablero_a_molestar) ):
            elementos_xa_tablero_a_molestar.append(tablero_a_molestar[fila][columna]) #cargo los elementos
    
    shuffle(elementos_xa_tablero_a_molestar) #los mezclo
    
    #vuelvo a cargar el tablero original con los elementos mezclados
    indice = 0
    for fila in range(len(tablero_a_molestar)):
        for columna in range(len(tablero_a_molestar)): 
            tablero_a_molestar[fila][columna] = elementos_xa_tablero_a_molestar[indice] #y lo vulevo a cargar 
            indice += 1     
   

    return tablero_a_molestar


def carta_toti(tablero_a_molestar: list):
    """
    PRE: la lista de listas "tablero_a_molestar" es el tablero del oponente que busco modificar para hacerle 
    más dificil el juego
    POST: No devuelve nada, ESPEJA HORIZONTAL o VERTICALMENTE el tablero indicado, "por referencia".
    """
    sentido = randint(1,2)

    if sentido == 1:
        #ESPEJADO VERTICAL: "espejo colocado horizontal//" (lo de arriba pasa abajo y viceversa)

        # print('tablero antes de espejar verticalmente\n')      #xa testear
        # mostrar_tablero_xa_testeo(tablero_a_molestar)          #xa testear        
        
        filas_aux = [] # contendra las primeras n/2 filas (matriz de n x n)

        for fila in range( len(tablero_a_molestar)): # fila: 0, 1, 2, 3, 4, 5, 6, 7
            if fila < (len(tablero_a_molestar) / 2): #si la fila es de las primeras; hasta n/2
                
                filas_aux.append(tablero_a_molestar [fila]) #guardo la fila
                
                tablero_a_molestar[fila] = tablero_a_molestar [ len(tablero_a_molestar)-1 - fila ] 
                #y esa misma fila pasa a valer "la complementaria"
                #print(tablero_1[fila])                  
            else:
                tablero_a_molestar [fila] = filas_aux [len(tablero_a_molestar)-1 - fila]
                #las q me quedan (dsps de la mitad, pasan a valer lo q valian respectiva// las 1eras n filas )
        
        
    else:
         #ESPEJADO HORIZONTAL: "espejo colocado vertical//" (lo de la izq pasa a la der y viceversa)

        # print('tablero antes de espejar horizontalmente \n') #xa testear
        # mostrar_tablero_xa_testeo(tablero_a_molestar)   #xa testear

        for fila in range( len(tablero_a_molestar) ): # fila: 0, 1, 2, 3, 4, 5, 6, 7
        
            columnas_aux = []
        
            for columna in range ( len(tablero_a_molestar) ):    #columna: 0, 1, 2, 3, 4, 5, 6, 7
                if columna < (len(tablero_a_molestar) / 2):
                    columnas_aux.append (tablero_a_molestar [fila][columna] )    
                    tablero_a_molestar [fila][columna] = tablero_a_molestar [fila][ len(tablero_a_molestar) - 1 - columna]
            
                else:
                    tablero_a_molestar [fila][columna] = columnas_aux [ len(tablero_a_molestar) - 1 - columna ]
        

def carta_fatality(tablero_a_molestar: list):
    """
    PRE: la lista de listas "tablero_a_molestar" es el tablero del oponente q voy a modificar.
    POST: No devuelve nada. TRASPONE el tablero que busco molestar. Uso un tablero auxiliar y despues vuelvo 
    a cargar el original "por referencia".
    """

    #print('tablero antes de trasponer\n') #xa testear
    #mostrar_tablero_xa_testeo(tablero_a_molestar) #xa testear

    #creo un tablero aux vacio. Intenté usar el metodo .copy() pero me tocaba el 
    #tablero original

    tablero_traspuesto = list()  

    for fila in range( len(tablero_a_molestar) ): 
        fila_nueva = list()
        for columna in range( len(tablero_a_molestar) ):
            fila_nueva.append('AUX')
        tablero_traspuesto.append(fila_nueva)


    #Cargo el tablero aux YA TRASPONIENDO los elementos
    for fila in range( len(tablero_traspuesto) ):
            for columna in range( len(tablero_traspuesto) ):

                tablero_traspuesto[fila][columna] = tablero_a_molestar[columna][fila]
                #la columna de la traspuesta, es la fila de la original y viceversa
    
    #vuelvo a cargar el tablero original (a molestar) con los elementos del tablero YA TRASPUESTO. Esto lo hago 
    #ya que es la mejor manera que encontre de modificarlo por "referencia" y asi no tener que returnear uno 
    #modificado. De hecho, si devolviese un tablero nuevo, con el algoritmo q yo plantie en "jugando()", no 
    #estaria guardando los cambios realizados en el tablero del oponente q quiero molestar xq utilizo una 
    #unica varaible "tablero_a_molestar" xa molestar a los 2 tableros y lo unico q voy haciendo es cambiar a 
    #donde apunta la flecha en la direc de memoria, modificando por referencia los tableros cargados 1 o 2.

    for fila in range( len(tablero_a_molestar) ):
        for columna in range( len(tablero_a_molestar) ):
            
            tablero_a_molestar[fila][columna] = tablero_traspuesto[fila][columna]


def jugar_carta(cartas_guardadas: list) -> list:
    """
    PRE: la lista "cartas_guardadas" es una lista de strings con las cartas que le fueron tocando al jugador
    y todavia no se han jugado. 
    POST: Devuelve la carta elegida o 'n' si no se eleigio ninguna carta para jugar.
    """
    print('\nEste es su mazo de cartas:')
    for i in range ( len(cartas_guardadas) ):
        print(f'{i+1}-{cartas_guardadas[i]}')
    print()

    opc = int(validar_opcion(0, 1, 'Desea jugar alguna carta 1-Si 0-No?: '))
    if opc == 1:
        carta = cartas_guardadas [ int (validar_opcion (1, len(cartas_guardadas),
        '¿Que carta queres jugar?: ') ) - 1 ]  
        #resto 1 xq en cartas guardadas la lista arranca en 0
    
    else:
        carta ='n'

    #print('Jugaste: ',carta) #xa testeo

    return carta


def levantar_carta(lista_probas: list) -> str:
    """
    PRE: La lista "lista_probas" contiene las probabilidades de cada carta xa q aqui se haga efectivamente 
    el calculo con random para ver si sale carta o no, y en el primer caso, cual.
    POST: Devuelve el string "carta_levantada" con el nombre de la carta o con 'n' en caso de que no se
    levante carta.
    """
    cartas =  ['Replay', 'Layout', 'Toti', 'Fatality' ]

    #0 REPLAY, layout , toti, fatality     

    #TRADICIONAL: lista_probas = [0, 0, 0, 0, 0, 100] #0/10 turnos con carta 
    #0 - 100 'n'
    
    #ACIDO: lista_probas = [0, 10, 20, 30, 40, 100] #4/10 turnos con carta]
    #0 - 10 Replay, 10 - 20 Layout, 20 - 30 Toti, 30 - 40 Fatality, 40 - 100 'n'

    #MUY ACIDO: lista_probas = [0, 20, 40, 60, 80, 100] #8/10 turnos con carta 
    #0 - 10 Replay, 10 - 20 Layout, 40 - 60 Toti, 60 - 80 Fatality, 80 - 100 'n'
    
    rango_carta = randint(1,100)
    
    #print('rango carta:',rango_carta) #xa testear
    print()
    
    if rango_carta >=  lista_probas[4]:
        print('Ups! No levantas carta')
        carta_levantada = 'n'     #si no toca carta pongo 'n'
    else:
        for i in range ( len (lista_probas) -2 ): # len (6 - 2) = len(4)
                        #i puede valer 0, 1, 2, 3
            if lista_probas[i] < rango_carta <= lista_probas[i+1] :
                print(f'Te toco la carta {cartas[i]}')
                carta_levantada = cartas[i]
    
    #print('carta hardcodeada: Fatality') #xa testear cada carta por separado
    #carta_levantada ='Fatality' #xa testear
    
    return carta_levantada


def jugando(tablero_cargado_1: list, tablero_cargado_2: list, jug_1: str, jug_2: str, lista_probas: list) -> str:
    """
    GRAL: El juego en si. Primero se inenta encontrar las cartas iguales. Dsps con otras funciones 
    se levantan las cartas. Estas se guardan predeterminadamente y luego se da la opcion de jugarlas o no.
    
    PRE: las listas de listas "tablero_cargado_1" y "tablero_cargado_2" son los tableros cargados, los strings
    "jug_1" y "jug_2" son los nombres de los jugadores, "lista_probas" es la lista con las probabilidades de
    cada carta.
    POST: Devuelve el string "ganador" con el nombre del ganador del juego.
    """
    #ACLARACION IMPORTANTE: Xa mejor comprension asumo q yo trato de adivinar MI tablero (tablero_a_adivinar)
    #q por supuesto no lo veo, y aplico cartas (salvo replay) para molestar al tablero del
    #oponente (tablero_a_molestar), q tampoco ve el suyo)

    gano_juego = False
    turno = 1

    cartas_guardadas_jug_1: list = list() # Me parecio mas util crear estas 2 listas aqui puesto q no es necesario  
    cartas_guardadas_jug_2: list = list() # devolverlas al menu ya q se borran cuando se acaba la partida
    
    while not gano_juego :

            #print(turno)    #para facilitar testeo (turnos impares -> jug 1, turnos pares -> jug 2)

            if turno %2 != 0:
                print('Turno de {}\nTablero 1'.format(jug_1.upper() ) )
                tablero = tablero_cargado_1
                tablero_a_molestar = tablero_cargado_2
                cartas_guardadas = cartas_guardadas_jug_1
                ganador = jug_1

            else:
                print('Turno de {}\nTablero 2'.format(jug_2.upper() ) )
                tablero = tablero_cargado_2
                tablero_a_molestar = tablero_cargado_1
                cartas_guardadas = cartas_guardadas_jug_2
                ganador = jug_2

            gano_juego = hacer_memoria(tablero)
     
            carta_levantada = levantar_carta(lista_probas)

            if  carta_levantada  != 'n' : #a menos que no se levante carta ('n'), se guarda automatica//
                #print('Guardamos', carta_levantada)     #xa testear
                cartas_guardadas.append(carta_levantada)
                    
            if len (cartas_guardadas) >0 :  #siempre y cunado tenga cartas en el mazo...
                carta = jugar_carta(cartas_guardadas)

                if carta != 'n':    #si el jugador eligio carta...
                    cartas_guardadas.remove(carta)

                    if carta == 'Replay':
                        gano_juego = hacer_memoria(tablero)
                    
                    elif carta == 'Layout':
                        carta_layout(tablero_a_molestar)
                        # print('tablero ya mezclado al azar FUERA DE FUNCION') #xa testear
                        # mostrar_tablero_xa_testeo(tablero_a_molestar) #xa testear

                    elif carta == 'Toti':
                        carta_toti(tablero_a_molestar)
                        # print('tablero ya espejado FUERA DE FUNCION\n') #xa testear
                        # mostrar_tablero_xa_testeo(tablero_a_molestar) #xa testear
                    
                    else:
                        carta_fatality(tablero_a_molestar)
                        # print('tablero ya tarspuesto FUERRA DE TRASPONGO') #xa testear
                        # mostrar_tablero_xa_testeo(tablero_a_molestar) #xa testear

            print('FIN DEL TURNO DE {}'.format(ganador.upper() ) ) 
            print('presione cualquier tecla para seguir jugando') #más comodidad xa jugar
            input()                                           

            turno += 1
        
    return ganador

def guardar_score(scores:list,ganador:str) -> None:
    """
    PRE: La lista "scores" contiene los nombres de los ganadores y la cantidad de partidas que gano
    cada uno.
    POST: No devuelve nada. Guarda el nombre de los jugadores y la cantidad de partidas que gano en "scores".
    """
    esta = False
    for i in range ( len(scores) ): #len = numero de jugadores
        if scores[i][0] == ganador.upper():
            scores[i][1] = scores[i][1] + 1
            esta = True
    
    if not esta:
        scores.append([ganador.upper(),1])


def main() -> None:
    """
    GRAL: Menu principal del juego. Esta dividido en tres partes importantes. Las siguientes funciones pueden
    servir de indice: "nueva_partida()" crea una nueva partida creando y cargando tableros; "jugando()" 
    contiene la logica principal del juego y "mostrar_scores()" muestra en orden los punatajes de los 
    ganadores. 
    """
    salir_del_juego = False
    scores: list = list()

    #scores es una lista de listas, con 2 "columnas" (jugadores | puntaje) y tantas filas como jugadores.
    #Esta da la ventaja de q pueden jugar tantos jugadores distintos como quiera pero como inconveniente si 
    # alguno de ellos ingresa su nombre escrito en forma "distinta", los puntajes iran a dos personas 
    # distintas. EJ: Juan 1, Juansito 1, Juansote 1. De esta forma no restrinjo la cantidad de jugadores por
    #partida a 2 pero si doy espacio a un error de tipeo en los nombres de jugadores.

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
                
                lista_probas = proba_cartas()
                
                tablero_cargado_1, tablero_cargado_2 = nueva_partida(tam_matriz)

                iniciada = True

            elif opc == 1:
                if iniciada:
                    salir_del_menu_principal = True
                else:
                    print('\nDebe crear una nueva partida antes de comenzarla\n')
                    salir_del_menu_principal = False
            
            elif opc == 2:
                mostrar_scores(scores)

            else:
                salir_del_menu_principal = True
                
        ganador = jugando(tablero_cargado_1, tablero_cargado_2, jug_1, jug_2, lista_probas)

        print('¡Felicidades! Haz ganado {}'.format(ganador.upper() ) )

        
        guardar_score(scores, ganador)
        
        print('1 - Volver al menu principal\n0 - Salir del juego')
        opc = int(validar_opcion(0,1))
        if opc == 0:
            print('\nEsta seguro que desea salir del juego? Se perderan los scores')
            print('1 - Si\n2 - No')
            si_quiero_salir = int(validar_opcion(1,2))

            if si_quiero_salir == 1:
                #salir_del_menu_principal = True
                salir_del_juego = True

main()
