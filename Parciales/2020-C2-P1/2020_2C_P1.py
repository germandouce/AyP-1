#ej 1 y 2) 16:30 - 16:47

#ej1) 1986,0622(base 10) = 13110.0211234(base 6)
#ej2) D1E60.D105(base 16)= 3101321200.31010011(base 4)

#ej 3) 18:01 - 
'''
Yamila, la cosmetóloga furor en redes, tiene un consultorio donde realiza limpiezas y tratamientos 
para el cuidado de la piel. Debido a la alta demanda de sus pacientes y futuros pacientes, nos pidió
que realicemos un programa que la ayude con la planificación de su negocio. La información del 
paciente que Yami necesita analizar es la cantidad de consultas asistidas y que tratamientos fueron 
realizados. Asimismo, el catálogo de tratamientos que comercializa es el siguiente:  
- Higiene profunda $1500
- Tratamiento Acné $1500
- Tratamiento tensor con aparatología $1800    
- Tratamiento revitalizante $3000 
Hacer un programa que:     
a) Permita al usuario realizar el ingreso de un paciente. Para ello se solicita:         
- DNI         
- Nombre y Apellido         
- Cantidad de consultas asistidas        
- Tratamientos realizados (Tipo y cantidad. Puede ser ninguno)     

b) Emita un reporte que informe el tratamiento más solicitado por los pacientes.    
c) Emita un reporte que informe el monto total de tratamientos vendidos. 
d) Emita un reporte que informe el total de pacientes nuevos y viejos.     
e) Emita un reporte que informe cuál es el tratamiento más solicitado por los pacientes nuevos. 

A tener en cuenta: Se considera que un paciente es *nuevo* en caso de que el mismo haya asistido 
únicamente a 1 consulta con el profesional.
'''

def validar_opcion(opc_minimas: int, opc_maximas: int, texto: str = '') -> str:
    #ej: opc = int (validar_opcion(1, 2, 'texto en str con pregunta') )
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



#IMPRIMIR DATOS DE DICT
def mostrar_tabla(tabla : dict) -> None:
    for llave, dato in tabla.items():
        print(f"{llave}: {dato}")


#FUNCIONES XA MOSTRAR DATOS A USUARIO
def mostrar_tratamiento_pacientes_nuevos(pacientes:dict, tratamientos: dict) -> None:  
    
    print('Tratamiento mas solicitado por pacientes nuevos')
    
    tratamientos_pacientes_nuevos = {}
    
    for paciente in pacientes.values():
        if paciente['consultas'] == 1:
            for tratamiento, cantidad in paciente['tratamientos_realizados'].items():
                if tratamiento not in tratamientos_pacientes_nuevos:
                    tratamientos_pacientes_nuevos[tratamiento] = cantidad
                else:
                    tratamientos_pacientes_nuevos[tratamiento] += cantidad   

    max_cantidad = 0
    for cant in tratamientos_pacientes_nuevos.values():
        if cant> max_cantidad:
            max_cantidad = cant
    
    llave = 'nombre'
    for trat, cant in tratamientos_pacientes_nuevos.items():
        if cant == max_cantidad:
            print(f'El tratamiento mas solicitado fue {tratamientos[trat][llave]}, {cant} veces ')
    


def mostrar_tratamiento_mas_solicitado(tratamientos) -> None: #muestra cursos ordenados y el q tiene mas (hace todo)
    
    cantidad_de_tratamientos = [] #creo lista donde guradare los curso y sus repectivas vacantes
    
    for tratamiento in tratamientos.values():
        cantidad_de_tratamientos.append( [tratamiento['cantidad'], tratamiento['nombre'] ])
    cantidad_de_tratamientos.sort(reverse =  True, key= lambda tratamiento: tratamiento[0] ) #tratamiento [1] es la cantidad de veces q fue realizado
        
    max_cantidad =  max(cantidad_de_tratamientos)
    print()    

    for trata in cantidad_de_tratamientos:
        print(f'{trata[1]} fue solicitado {trata[0]} veces')                
    print()
    
    print('tratamiento (s) mas solicitado')
    for trata in cantidad_de_tratamientos:
        if trata[0] == max_cantidad[0]:
            print(f'{trata[1]} fue solicitado {trata[0]} veces')                

#FUNCION PARA MOSTRAR NOMBRE DE UNA CLAVE SU VALOR DE UN DICT DE DICT
def mostrar_nombre_tratamientos(tratamientos)->None:
    for tratamiento, datos in tratamientos.items():
        llave = "nombre"
        print(f"{tratamiento} - {datos[llave]}")


def mostrar_monto_total_tratamientos_vendidos(tratamientos: dict) -> None:   #mostra todos los cursos (ordenados)
    #cursos = sorted(cursos)        
    monto_total = 0
    for tratamiento in tratamientos.values():
        monto_total += tratamiento['cantidad']*tratamiento['costo']
    
    print(f'Te hiciste unos {monto_total} $ en total entre todos los tratamientos')

def mostrar_pacientes(pacientes: dict) -> None:   
    
    pacientes_nuevos = list()
    pacientes_viejos = list()

    for paciente in pacientes.values():
        if paciente['consultas'] == 1:
            pacientes_nuevos.append(paciente['nombre'])
        else:
            pacientes_viejos.append(paciente['nombre'])
    
    print(f'pacientes nuevos: {len(pacientes_nuevos)}\n')
    
    for paciente in pacientes_nuevos:
        print(paciente)
    
    print(f'\npacientes viejos: {len(pacientes_viejos)}\n')
    for paciente in pacientes_viejos:
        print(paciente)

#FUNCIONES DE ALTA - BAJA - MODIFICACION
def alta_paciente(pacientes: dict, tratamientos:dict) -> None:
    
    paciente = dict()  #el nuevo paciente es un diccionario con datos q seran clave
    dni = int(input("Ingrese el DNI del nuevo paciente: ")) #sera el codigo o clave ppal de paciente
    
    #Pido datos del paciente
    nombre = input("Ingrese el nombre y apellido del paciente: ")    #estos datos se agregan al cursos[llave]
    consultas = int(input("Ingrese la cantidad de consultas asistidas: "))
    
    tratamientos_realizados = dict()    #tratamientos ={tipo_tratamiento: cantidad }
    
    mostrar_nombre_tratamientos(tratamientos)
    print('Ingreese el tratamiento realizado, si no realizo ninguno presione 0')

    continuar_ingreso = True
    
    while continuar_ingreso:
        tipo_tratamiento = int(input(f"Ingrese el tratamiento realizado: "))
        
        if tipo_tratamiento != 0:
            cantidad = int(input(f"Ingrese la cantidad de veces q se realizp dicho trtamiento: "))
            
            tratamientos_realizados[tipo_tratamiento] = cantidad # dentro del dict pacientes
            
            tratamientos[tipo_tratamiento]['cantidad'] = cantidad # dentro del dict tratamientos

            corte = input("¿Quiere seguir ingresando datos <s/n>? ")
            if corte != "s":
                continuar_ingreso = False
        
        else:
            continuar_ingreso = False

    #Guardo los datos en la tabla pacientes  
    paciente["nombre"] = nombre
    paciente["consultas"] = consultas
    paciente["tratamientos_realizados"] = tratamientos_realizados    

    #Convierto el paciente: pacientes[dni] en key de la tabla pacientes
    pacientes[dni] = paciente


def baja_curso(cursos: dict) -> None:

    #mostrar_nombre_cursos(cursos)

    opciones = list(cursos.keys())
    
    opc = input('¿Que curso desea DAR DE BAJA?: ')
    while ( not opc.isnumeric() ) or ( int(opc) not in opciones):
        opc = input('ingrse una opcion valida: ')
    opc = int(opc)

    cursos.pop(opc)


def modificar_curso(cursos: dict) -> None:
    
    #muestro cursos
    for curso, datos in cursos.items():
        llave = "nombre"
        print(f"{curso} - {datos[llave]}")
    
    opciones = list(cursos.keys())
    
    opc = input('¿Que curso desea modificar?: ')
    while ( not opc.isnumeric() ) or ( int(opc) not in opciones):
        opc = input('ingrse una opcion valida: ') 
    opc = int(opc)

    #muestro datos del curso elegido xa modificar
    for key, value in cursos[opc].items():
        print(f"{key} - {value}")
    
    #Pregunto q desea modificar
    entrada = input("¿Qué desea modificar del curso?: ")
    if entrada == "nombre":
        nombre = input(f"Ingrese el nuevo {entrada}: ")
        cursos[opc][entrada] = nombre

    elif entrada == "costo":
        costo = float(input(f"Ingrese el nuevo {entrada}"))
        cursos[opc][entrada] = costo

    elif entrada == "cantidad_de_dias":
        cantidad_de_dias = int(input(f"Ingrese la nueva {entrada}"))
        cursos[opc][entrada] = cantidad_de_dias

    elif entrada == "cantidad_de_vacantes":
        cantidad_de_vacantes = int(input(f"Ingrese la nueva {entrada}"))
        cursos[opc][entrada] = cantidad_de_vacantes

    elif entrada == "fechas_de_dictado": 
        
        cortar = False
        fechas_de_dictado = list()

        while not cortar:
            fecha = input(f"Ingrese las nuevas {entrada}: ")
            fechas_de_dictado.append(fecha)

            seguir = int(validar_opcion(0,1,"¿Quiere seguir ingresando fechas 1- Si 0- No ?: "))
            if seguir == 0:
                cortar = True
        
        cursos[opc][entrada] = fechas_de_dictado


#DERIVADOR DE OPCIONES abm_cursos
def abm_cursos (opc, pacientes:dict, tratamientos:dict):
    '''
    #PRE: Recibe la opc elegida en el menu  y las estructura ppal 
    utilizada para guardar y operar con el ABM

    #POST: Redirige a la funcion q corresponda xa hacer lo pedido x el usuari
    '''
    if opc == 0:
        alta_paciente(pacientes, tratamientos)
    
    # elif opc == 1:
    #     baja_paciente(pacientes)
    
    # if(opc == 2):
    #     modificar_pacientes(pacientes)
    
    elif(opc == 3):
        mostrar_tratamiento_pacientes_nuevos(pacientes, tratamientos)   #tratamiento mas elegido por pacientes

    elif(opc == 4):
        mostrar_pacientes(pacientes) #muestra nuevos y viejos

    elif(opc == 5):
         mostrar_monto_total_tratamientos_vendidos(tratamientos) #muestra total vendido en sopes

    elif(opc == 6):
        mostrar_tratamiento_mas_solicitado(tratamientos) #muestra tratamiento mas solicitado entre todos


#MAIN XA ABM
def main():
    cerrar = False

    #Estructura a usar en el ABM xa guardar y modificar los datos {}, [] etc:
    # cursos = [["Aprende  a hacer tu propio compost",1 ,950],
    # ["Los niños y el medioambiente(para padres e hijes)",2,990],
    # ["Tu huerta orgánica",4,2500]]

    pacientes ={}

    tratamientos = {
        1: {
            "nombre": "Higiene profunda",
            "costo": 1500.0,
            "cantidad":0
        },
        
        2: {
                "nombre": "Tratamiento Acné",
                "costo": 1500.0,
                "cantidad":0
        },
                
        3: {
                "nombre": "Tratamiento tensor con aparatología",
                "costo": 1800.0,
                "cantidad":0

        },
        
        4:{
                "nombre": "Tratamiento revitalizante",
                "costo": 3000,
                "cantidad":0

            }
        }    


    while not cerrar:

        #MENU DE OPCIONES DEL ABM:
        print('''
Bienvenido  al sistema de registros de cursos de RumboCircular, ¿Que desea hacer? 
0.Dar de ALTA un paciente
1.Dar de BAJA un paciente
2.MODIFICAR uno de los pacientes  #modificar valores de las claves de dict dentro de dict        
3.Mostrar el tratamiento mas solicitado por los pacinetes nuevos #Mostrar valores dentro del dict chico q cumplen x condicion
4.Mostrar el total de pacientes nuevos y viejos
5.Mostrar monto total ganado con tratamientos vendidos  #muestra varios datos ESPECIFICOS SI LO HAY
6.Mostrar el tratamiento mas solicitado por los pacientes #mostrar datos segun el max de ellos
7.Cerrar el programa (MUESTRA todo!!1) ''')

        opc = int( validar_opcion(0,7, 'Ingrese una opcion: '))

        if opc != 7:
            abm_cursos(opc, pacientes, tratamientos)
        
        else:
            mostrar_nombre_tratamientos(tratamientos)
            for paciente, datos in pacientes.items():
                print(f'\n{paciente}:')
                for llave in datos:
                    print(f'{llave}: {datos[llave]}')
            cerrar = True


main()



#ej 4) 16:52 - 17:05 -> 13 minutos... sospechoso..
'''
4) Lucho adora las zanahorias. Podría pasar horas contándonos sobre las diferentes variedades de 
zanahorias, con sus diferentes sabores, colores, olores, texturas...  
Nos ha contratado para que lo ayudemos a realizar la compra. Luego de investigar, ha reducido su 
interés a únicamente dos proveedores de zanahorias: Sus nombres comerciales son “ZANAHORÍN” y 
“ZANAHORÓN”.  ZANAHORÍN  y  ZANAHORÓN  son  los  proveedores  de  máxima  calidad,  y  como  la  
calidad  de  ambos  es  indistinguible (¡Incluso para un experto en zanahorias de la talla de Lucho!),
lo importante es comprar al que tenga menor precio de los dos.  Lucho  quiere  que  lo  ayudes  con 

Una  función  llamada  zanahorias,  que  reciba  los  precios  en  pesos (por tonelada de zanahorias)
de cada proveedor en UN string, y escriba el nombre del proveedor al cual conviene comprar. Si ambos
venden a igual precio, se debe escribir el texto “DA IGUAL”. 
Datos de entrada: Se reciben en un único string con dos enteros entre 1 y 100000 inclusive, 
separados por un espacio: 

• El primero indica el precio al que vende “ZANAHORÍN”  
• El segundo el precio al que vende “ZANAHORÓN”.  

Datos de salida: Se debe escribir una única línea, con la palabra “ZANAHORÓN” o “ZANAHORÍN” (sin 
las comillas), según quién tenga mejor  precio.  Si  ambos  venden  al  mismo  precio,  se  debe  
escribir  en  una  única  línea  la  frase  “DA  IGUAL”  (sin  las comillas). 
Nota: Toda la salida debe estar en letras mayúsculas, como se ha indicado.  
Ejemplo:  Si la entrada por parámetro fuera: 15223 17250  La salida debería ser: ZANAHORÍN
'''
'''
#Esto sospechosa// facil no se si me comi algo de la consigna o q onda...

def zanahorias(num_1: str, num_2: str) -> None:
    num_1 = int(num_1)
    num_2 = int(num_2)
    
    if num_1 < num_2:
        print('ZANAHORÍN')
    elif num_2 < num_1:
        print('ZANAHORÓN')
    else:
        print('DA IGUAL')

# num_1 = 15223 
# num_2 = 17250
# zanahorias(num_1, num_2)
'''

#ej 5) 17:05 - 17:59 -> 44 min
'''
Números escalonados: 
Un número es escalonado, si sus dígitos están en orden estrictamente creciente. Por ejemplo, 359 es 
escalonado, 34 también, pero 5674 no es, y tampoco 5667. Se recibe un número entero por parámetro 
N > 10 (lo cual se debe validar). La salida debe decir si es un número escalonado o no lo es y a 
continuación indicar la cantidad de dígitos cuya secuencia fue escalonada. 

Datos de entrada: Se recibe un parámetro con el número entero N.  
Datos de salida:  El  programa  debe  imprimir  por  pantalla  en  una  línea,  conteniendo  un  
único  número:  la  cantidad  de  números escalonados que hay entre 10 y N, inclusive. 

Ejemplo1: Entrada: 359 - Salida: “Es escalonado”, 3 
Ejemplo2: Entrada: 24893471 - Salida:  “No es escalonada”, 4 
'''
'''
def numeros_escalonados(num: int) -> None:
    
    num = str(num)    
    
    num_digits_orig = list()

    for digit in num:
        num_digits_orig.append( int(digit) )

    cantidad_digitos_escalonados = 0
    i = 0
    while (i <= len(num_digits_orig) -2) and (num_digits_orig[i] <= num_digits_orig[i+1]):
        if i==0:
            cantidad_digitos_escalonados += 2
        else:
            cantidad_digitos_escalonados += 1
        i += 1

    if len(num_digits_orig) == cantidad_digitos_escalonados:
        print(f'{num} es escalonadao, tiene {cantidad_digitos_escalonados} digitos escalonados')
    else:
        print(f'{num} no es escalonadao, tiene {cantidad_digitos_escalonados} digitos escalonados')

def ingreso_numero() -> int:
    num = input('Ingrese un numero mayor a 10: ')
    while not ( num.strip('-').isnumeric() ) or ( int(num) <= 10 ):
        num = input('No valido. Ingrese un numero mayor a 10: ')
    return num

def main() -> None:
    num = ingreso_numero()
    numeros_escalonados(num)

main()
'''