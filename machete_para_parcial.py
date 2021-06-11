
#Validador de ocpiones para menu
#Util para menus y para corte de ciclos tipo seguir ingresando( 1- si  0- no)

def validar_opcion(opc_minimas: int, opc_maximas: int, texto: str = '') -> str:
    #ej: opc = validar_opcion(1, 2, 'texto en str con pregunta')
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



def ingreso_numeros_corta_letra():
    #lista_de_numeros = ingreso_numeros_corta_letra()
    """
    PRE: no contiene parametros

    POST: Devuelve lista con numeros enteros (¡Acepta negativos!)
    """

    print('Ingrese numeros corte con cualqueir letra')
    lista = list()

    num = input('')
    while num.strip('-').isnumeric():
        lista.append(num)
        num = input('')
    
    return lista

#Ciclo xa ingreso con corte manual:

def ingreso_elementos() -> list:
    #ingreso_elementos()
    lista = list()

    cortar = False
    while not cortar:
        
        print('Ingrese algo')

        opc = int( validar_opcion(0,1, 'Desea seguir ingresando? 1- Si 0 - No: ') )
        
        if opc == 0:
            cortar = True

    return lista