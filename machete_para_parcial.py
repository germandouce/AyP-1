#MACHETE PARA PARCIAL
#FUNCIONES MUY UTILES Y USADAS


#MAIN SIMPLE
def main()-> None:
    #main()
    pass



#INGRESO DE NUMEROS ENTEROS O FLOTANTES CORTA CON CUALQUIER LETRA, NO VALIDA DIRECTAMENTE CORTA!
def ingreso_numeros_corta_letra() -> list:
    #lista_de_numeros = ingreso_numeros_corta_letra()
    #print(lista_de_numeros)

    """
    PRE: no contiene parametros

    POST: Devuelve lista con numeros enteros (¡Acepta negativos!)
    """

    print('Ingrese numeros corte con cualqueir letra')
    lista = list()

    num = input('')
    while num.strip('-').isnumeric():
        lista.append(int(num))
        num = input('')
    
    return lista


#DEVUELVE EL MENOR NUMERO DE UNA LISTA INGRESADA (comentado!!)
#PERMITE INGRESO NUMEROS NEG Y POS HASTA QUE LA SUMA LLEGUE A LIMITE Y LOS VALIDA!! 
# SI SE INGRESA LETRA SALTA PERO NO CORTA!
def menor_numero(limite: int) -> int:
    #print(menor_numero(100))
    """
    PRE: Limite es el valor en el cual se corta el ingreso
    POST: Devuelve el menor de los numeros ingresados
    """
    print('Ingrese numeros')
    
    # lista = list()
    sum = 0
    while sum <= limite:

        num = input('ingrese: ')
        while not num.strip('-').isnumeric() :
            num = input('Ingrese un numero valido: ')

        sum += int(num)
        # lista.append( int(num) )
    
    #minimo = min (lista)
    #return minimo
    return sum


#CICLO DE INGRESO DE ELEMENTOS CON CORTE MANUAL
def ingreso_elementos() -> list:
    #ingreso_elementos()
    lista = list()

    cortar = False
    while not cortar:
        
        print('Ingrese algo')
        
        #opc o funcion xa ingresar datos

        opc = int( validar_opcion(0,1, 'Desea seguir ingresando? 1- Si 0 - No: ') )
        if opc == 0:
            cortar = True
    
    return lista

