#Validador de numero enteros o flotantes (ojo si es flotante cambiar texto)
def validar_numero(texto:str = '') -> str:
    #num = validar_numero(num, 'texto en str con pregunta')
    """
    PRE: "texto" es un parametro opcional con la pregunta
    xa el usuario

    POST: Devuelve en formato string la var "num" con un número 
    """
    num = input("{}".format(texto))
    while not num.isnumeric():
        num =  input('Ingrese un ... entero: ')

    return num
