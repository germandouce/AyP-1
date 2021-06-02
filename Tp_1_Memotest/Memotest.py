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


def proba_cartas() -> list:
    """
    PRE: No recibe argumentos
    POST: Defino proba de cada carta. solo va a devolver 5 valores que representan la probabilidad
    n una lista.
    """
    print("\nDefini la probabilidad de salida de las cartas especiales")
    print('0 - Tradcional\n1 - Piknte\n2 - Muy piknte')
    print()
    cartas = 'Replay', 'Layout', 'Toti', 'Fatality', 'No salga ninguna' 

    opc = int( validar_opcion(0,3) )

    if opc ==0:
        lista_probas = [0, 0, 0, 0, 0, 100] #0/10 turnos con carta
    elif opc == 1:
        lista_probas = [0, 10, 20, 30, 40, 100] #4/10 turnos con carta
    else:
        lista_probas = [0, 20, 40, 60, 80, 100] #8/10 turnos con carta
    
    #Esto se lee, 0 a 10 sale Replay, 10 a 20 sale Layout, 40 a 60 sale Toti, 60 a 80 sale Fatality, 80 a 100 
    #no sale ninguna carta. Asi, xa este caso en 8/10 turnos sale carta 
    
    print('\nLas cartas tendran la siguiente probabilidad de salir:')
    for i in range ( len(cartas) ) :
        print(f'{ cartas[i] }: { int(lista_probas[i+1] - lista_probas[i]) } %' )
    
    print()
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

#XA TESTEO!!!
def mostrar_tablero_xa_testeo(tablero):
       for i in range( len(tablero) ):
                        for j in range( len(tablero) ):
                            print( tablero [i][j], end ='  ')
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
    POST: devuelve el bool gano_juego y modifica el tablero segun lo q adivinado
    """
    gano_juego = False
    perdio = False
    while (not perdio) and (not gano_juego):   #debe cumplirse que no perdio y que no gano

        #xa testeo
        print('\nTablero (SOLO XA TESTEO!!)' )
        mostrar_tablero_xa_testeo( tablero)
        mostrar_tablero(tablero)
        
        ficha_1, ficha_2 = elegir_ficha(tablero)
        
        perdio = chequeo_pareja(tablero, ficha_1, ficha_2)
        
        gano_juego = gano_el_juego(tablero)
    
    return gano_juego


def carta_layout(tablero_a_molestar: list):
    """
    PRE: tablero_a_molestar es el tablero del oponente q busco modificar para hacerle mas dificil el juego
    POST: No devuelve nada, solo MEZCLA el tablero indicado por referencia
    """
    #xa testear
    print('tablero antes de mezclar')
    mostrar_tablero_xa_testeo(tablero_a_molestar)
    
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
    PRE: tablero_a_molestar es el tablero del oponente q busco modificar para hacerle mas dificil el juego
    POST: No devuelve nada, ESPEJA el tablero indicado por referencia, horizontal o verticalmente
    """
    sentido = randint(1,2)

    if sentido == 1:
        #ESPEJADO VERTICAL: "espejo colocado horizontal//" (lo de arriba pasa abajo y viceversa)

        #xa testear
        print('tablero antes de espejar verticalmente\n')
        for i in range( len(tablero_a_molestar) ):
            for j in range( len(tablero_a_molestar) ):
                print( tablero_a_molestar [i][j], end ='  ')
            print()
        
        
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

        # xa testear
        print('tablero antes de espejar horizontalmente \n')
        mostrar_tablero_xa_testeo(tablero_a_molestar) 

        for fila in range( len(tablero_a_molestar) ): # fila: 0, 1, 2, 3, 4, 5, 6, 7
        
            columnas_aux = []
        
            for columna in range ( len(tablero_a_molestar) ):    #columna: 0, 1, 2, 3, 4, 5, 6, 7
                if columna < (len(tablero_a_molestar) / 2):
                    columnas_aux.append (tablero_a_molestar [fila][columna] )    
                    tablero_a_molestar [fila][columna] = tablero_a_molestar [fila][ len(tablero_a_molestar) - 1 - columna]
            
                else:
                    tablero_a_molestar [fila][columna] = columnas_aux [ len(tablero_a_molestar) - 1 - columna ]
        

def carta_fatality(tablero_a_molestar: list) -> list:
    """
    PRE: tablero_a_molestar es el tablero del oponente q voy a trasponer
    POST: OJO! Esta si devuelve el tablero nuevo traspuesto en la variable "tablero traspuesto"
    ya que use una lista auxiliar para hacerlo ysi no lo devilviese nada no podria guardar los cambios
    """
    #xa testear
    print('tablero antes de trasponer\n')
    mostrar_tablero_xa_testeo(tablero_a_molestar) 

    #creo un tablero aux de nuevo. Intente usar el metodo .copy() pero me tocaba el 
    #tablero original

    tablero_traspuesto = []  
    for fila in range(len (tablero_a_molestar) ):    #resto 1 xq len es 1 unidad mas grande q la cant de fil 
        tablero_traspuesto.append([])                    #y columnas
        for columna in range( len (tablero_a_molestar) ): 
            tablero_traspuesto[fila].append('AUX')
    
    #Cargo el tablero aux YA TRASPONIENDO los elementos
    for fila in range( len(tablero_traspuesto) ):
            for columna in range( len(tablero_traspuesto) ):

                tablero_traspuesto[fila][columna] = tablero_a_molestar[columna][fila]
                #la columna de la traspuesta, es la fila de la original y viceversa
    
    #vuelvo a cargar el tablero original (a molestar) con los elementos del tablero YA TRASPUESTO. Esto lo hago 
    # ya que es la mejor manera que encontre de modificarlo por "referencia" y asi no tener que returnear uno 
    # modificado. De hecho, si devolviese un tablero nuevo, con el algoritmo q yo plantie en el "jugando", no 
    # estaria guardando los cambios realizados en el tablero del oponente q quiero molestar xq utilizo una 
    # unica varaible tablero_a_molestar xa molestar a los 2 tableros y lo unico q voy haciendo es cambiar a 
    # donde apunta la flecha en la direc de memoria, modificando por referencia los tableros cargados 1 o 2.

    for fila in range( len(tablero_a_molestar) ):
        for columna in range( len(tablero_a_molestar) ):
            
            tablero_a_molestar[fila][columna] = tablero_traspuesto[fila][columna]


def jugar_carta(cartas_guardadas: list, tablero: list) -> list:
    """
    PRE: cartas guardadas de guardar carta y el tablero
    POST: Devuelve la carta elegida o 'n' si no se eleigio ninguna carta para jugar
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

    #print('Jugaste: ',carta)

    return carta


def levantar_carta(lista_probas: list) -> str:
    """
    GRAL: ahora q termino el turno xq perdio, se levanta carta. Aca se calcula efectivamente q carta
    toca segun las probas definidas en funcion proba_carta()
    PRE:  IMPORTANTE, probabilidades de cada carta xa q aqui se haga efectivamente el calculo con 
    random
    POST: devuelve el str carta_levantada, 'n', si no se levanta, el nombre de la carta en caso de que si
    """
    cartas =  ['Replay', 'Layout', 'Toti', 'Fatality' ]
    #Xa testear
    #0 REPLAY, layout , toti, fatality     

    #TRADICIONAL: lista_probas = [0, 0, 0, 0, 0, 100] #0/10 turnos con carta 
    

    #PIKNTE: lista_probas = [0, 10, 20, 30, 40, 100] #4/10 turnos con carta]


    #MUY PIKNTE: lista_probas = [0, 20, 40, 60, 80, 100] #8/10 turnos con carta 
    #0 - 10 Replay, 10 - 20 Layout, 40 - 60 sale Toti, 60 - 80 sale Fatality, 80 a 100 'n'
    
    rango_carta = randint(1,100)
    print('rango carta:',rango_carta)

    if rango_carta >=  lista_probas[4]:
        print('Ups! No levantas carta')
        carta_levantada = 'n'     #si no toca carta pongo 'n'
    else:
        for i in range ( len (lista_probas) -2 ): # len (6 - 2) = len( 4)
                        #i puede valer 0, 1, 2, 3
            #print(i)
            #print('proba',lista_probas[i])
            
            if lista_probas[i] < rango_carta <= lista_probas[i+1] :
                print(f'Te toco la carta {cartas[i]}')
                carta_levantada = cartas[i]
    
    #xa testear
    #print('carta hardcodeada: Fatality')
    #carta_levantada ='Fatality' #xa testear
    
    return carta_levantada


def jugando(tablero_cargado_1: list, tablero_cargado_2: list, jug_1: str, jug_2: str, lista_probas: list) -> str:
    """
    GRAL: el juego en si. Primero se inenta encontrar las cartas iguales. Dsps con otras funciones 
    se levanta la carta y se juega.
    PRE: recibe tableros cargados, LAS PROBABILIDADES de cada carta
    La carta se guarda predeterminada//. Dsps damos opcion de jugar carta inmediata// o no.
    POST: devuelve el ganador del juego en la variable 'ganador'
    """
    #ACLARACION IMPORTANTE: Xa mejor comprension asumo q yo trato de adivinar MI tablero (tablero_a_adivinar)
    #q por supuesto no lo veo, y aplico cartas (salvo replay) para molestar al tablero del
    #oponente (tablero_a_molestar), q tampoco ve el suyo)

    gano_juego = False
    turno = 1

    cartas_guardadas_jug_1 = [] #Me parecio mas util crear estas 2 listas aqui puesto q no es necesario 
    cartas_guardadas_jug_2 = [] #devolverlas al menu ya q se borran cuando se acaba la partida
    
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

            if  carta_levantada  != 'n' : #a menos que no se levante carta (n), la carta se guarda automatica//
                print('Guardamos', carta_levantada)     #xa testear
                cartas_guardadas.append(carta_levantada)
                    
            if len (cartas_guardadas) >0 :
                carta = jugar_carta(cartas_guardadas, tablero)
                if carta != 'n':
                    cartas_guardadas.remove(carta)

                    if carta == 'Replay':
                        gano_juego = hacer_memoria(tablero)
                    
                    elif carta == 'Layout':
                        carta_layout(tablero_a_molestar)
                        #xa testear
                        print('tablero ya mezclado al azar FUERA DE FUNCION')
                        mostrar_tablero_xa_testeo(tablero_a_molestar) 

                    elif carta == 'Toti':
                        carta_toti(tablero_a_molestar)
                        #xa testear
                        print('tablero ya espejado FUERA DE FUNCION\n')
                        mostrar_tablero_xa_testeo(tablero_a_molestar) 
                    
                    else:
                        carta_fatality(tablero_a_molestar)
                        print('tablero ya tarspuesto FUERRA DE TRASPONGO')
                        mostrar_tablero_xa_testeo(tablero_a_molestar) 

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
                score()

            else:
                salir_del_menu_principal = True
                
        ganador = jugando(tablero_cargado_1, tablero_cargado_2, jug_1, jug_2, lista_probas)

        print('¡Felicidades! Haz ganado {}'.format(ganador.upper() ) )

        guardar_score()
        
        print('0 - Volver al menu principal\n1 - Salir del juego')
        opc = int(validar_opcion(0,1))
        if opc == 1:
            print('\nEsta seguro que desea salir del juego? Se perderan los scores')
            print('1 - Si\n2 - No')
            si_quiero_salir = int(validar_opcion(1,2))

            if si_quiero_salir == 1:
                #salir_del_menu_principal = True
                salir_del_juego = True

main()
