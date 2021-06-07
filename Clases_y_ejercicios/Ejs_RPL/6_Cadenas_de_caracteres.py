#UNIDAD 6: Cadenas de caracteres



#ej 6.1 - Seleccion de caracteres
#Para practicar un poco de slicing...

#SINTAXI GENERAL XA SLICING
# s[i:j:k] Referencia la porción de la secuencia s que va del elemento i al j-1, con paso k

'''
completar estas funciones. Especifiaciones en rpl...
'''
'''
def primeros_dos_c(cadena):
    """
    Devuelve los 2 primeros caracteres
    """
    cadena = cadena[:2]
    
    return cadena

#print( primeros_dos_c('123') ) # ok

def ultimos_tres_c(cadena):
    """
    La función ultimos_tres_c() devuelve 
    sus tres últimos caracteres
    """
    cadena = cadena[len(cadena)-3:] # retrocede 
    return cadena

#print( ultimos_tres_c('1234567899') ) # ok

def cada_dos_c(cadena):
    """
    La función cada_dos_c() devuelve 
    solo cada dos caracteres de la cadena.
    """
    cadena = cadena[::2] 
    
    return cadena

#print( cada_dos_c('1234567899') ) # ok


def sentido_inverso(cadena):
    """
    La función sentido_inverso() devuelve 
    la cadena en sentido inverso.
    """
    cadena = cadena[::-1]
    
    return cadena

#print( sentido_inverso('1234567899') ) # ok


def normal_e_inversa(cadena):
    """
    Devuelve la cadena en sentido 
    normal seguida de la misma en sentido inverso.
    """
    cadena = cadena+cadena[::-1]
    
    return cadena
#print( normal_e_inversa('1234567899') ) # ok
'''
#ej 6.1 - 02 - Manipular cadenas
'''
Escribir las siguientes funciones que reciben una cadena, un caracter y 
de vuelven una cadena nueva:
'''
'''
def insertar_entre_letras(cadena, caracter):
    """
    La función insertar_entre_letras() inserta el caracter entre cada letra de la cadena 
    original.    
    """
    cadena_aux = cadena
    cadena_nueva = ''
    for i in range ( len(cadena_aux) ):
        cadena_nueva += cadena_aux[i]+caracter
    
    cadena_nueva = cadena_nueva[:len(cadena_nueva)-1]
    
    return cadena_nueva

#es muy malo pero funciona...
#print( insertar_entre_letras('algoritmos','#') ) # ok

#REPLACE!!!

def reemplazar_espacios(cadena, caracter):
    """
    Reemplaza todos los espacios de la cadena 
    original por el caracter.    
    """
    cadena = cadena.replace(' ',caracter)

    return cadena

#print( reemplazar_espacios('una  con  doble   espaciado', '&') ) # ok


def reemplazar_digitos(cadena, caracter):
    """
    La función reemplazar_digitos(' reemplaza todos los dígitos de la cadena 
    original por el caracter.
    """
    for char in cadena:
        if char.isnumeric():
            cadena = cadena.replace(char,caracter)

    return cadena

#print( reemplazar_digitos('D1g1t05' , '$') ) # ok
'''
#ej 6.4 - 02 - Separador de miles
'''
Escribir una función que reciba una cadena que contiene un largo número entero y devuelva una 
cadena con el número y las separaciones de miles. Por ejemplo, si recibe '1234567890', debe 
devolver '1.234.567.890'.
'''
'''
def agregar_separador_miles(numero):
    """
    separa con ptos
    """
    numero_aux = numero[::-1] 
    
    numero_nuevo = ''

    for i in range(1,len(numero_aux)+1):
        numero_nuevo += numero_aux[i-1]

        if i%3 == 0 and i< len(numero):   
            numero_nuevo += '.'
    
    numero_nuevo = numero_nuevo[::-1]
    
    return numero_nuevo

print( agregar_separador_miles('1234') )
'''
#OJO ACORDARSE EXISTIA .JOIN() !!!
#CON ITERABLES COMO EL STR...
'''
tup=('a','b','c')
print('-'.join(tup))

plbra = 'hola'
print('-'.join(plbra))
'''

#ej 6.5 - Primeras letras
'''
def primeras_letras(cadena):
    """
    devuelbe primera letra de cada plbra
    """
    lista_cadena = cadena.split()
    plbra = ''
    for palabra in lista_cadena:
        plbra += palabra[0]
    
    return plbra

print(primeras_letras('universal serial bus'))


def primera_letra_mayus(cadena):
    """
    Dicha cadena con la primera letra de cada palabra en mayúsculas. 
    """
    lista_cadena = cadena.title()
    return lista_cadena

print(primera_letra_mayus('universal serial bus'))

def comienzan_con_a(cadena):
    """
    Las palabras que comiencen con la letra ‘A’ (en mayúsculas o minúsculas).
    """
    lista_cadena = cadena.split()
    palabras_con_a = ''
    for palabra in lista_cadena:
        if (palabra[0]).upper() == 'A':
            palabras_con_a += palabra + ' '
    palabras_con_a = palabras_con_a[:len(palabras_con_a)-1]
    return palabras_con_a

print(comienzan_con_a('Antes de ayer Asfalte la calle'))
'''
