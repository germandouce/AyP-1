#ej 2)
'''
Escriba una función que dada una lista de denominaciones de billetes de la moneda corriente de un 
país, permita descomponer un importe otorgado por el usuario en las cantidades correspondientes a 
cada una de las denominaciones cual si fuera un cajero automático y suponiendo que siempre elige 
otorgar billetes del mayor valor posible. La función debe controlar que el importe sea factible de 
ser descompuesto y devolver un diccionario con la descomposición. 
Construya el programa principal donde utiliza dicha función. 
Ej: Lista = [10,20,50,100,200,500,1000] 
Valor = 1690  Diccionario = {10:0,20:2,50:1;100:1;200:0;500:1;1000:1}
'''
def validar_opcion(opc_minimas: int, opc_maximas: int, texto: str = '') -> str:
    """
    PRE: "opc_minimas" y "opc_maximas" son dos números enteros que 
    simbolizan la cantidad de opciones posibles.

    POST: Devuelve en formato string la var "opc" con un número 
    entero dentro del rango de opciones.
    """
    opc = input("{}".format(texto))
    while not opc.isnumeric() or int(opc) > opc_maximas or int(opc) < opc_minimas:
        opc = input("Por favor, ingrese una opcion valida: ")
    
    return opc


def ingreso_billetes()->list:
    lista_billetes = list()
    print('ingrese billetes')

    cortar = False
    while not cortar: 
        b = input('Ingrese billete: ')
        
        while not b.isnumeric():
            b = input('Ingrese un billete de denominacion numerica: ')
        
        b = int(b)
        
        lista_billetes.append(b)

        opc = int( validar_opcion(0,1,'Desea ingresar mas billetes? 1 - 0 - no: ') )
        if opc == 0: 
            cortar = True
    
    return lista_billetes


def cajero(lista: list) -> dict:
    importe = input('ingerse un importe: ')
    lista.sort(reverse=True)
    
    print(lista)
    
    while not importe.isnumeric():
        importe = input('Ingrese un billete de denominacion numerica: ')
        
    importe = int(importe)

    se_puede = False        #asumo q inicialmente  no se puede descomponer
    for billete in lista:
        if importe % billete == 0: # con q un solo billete divida enteramente al importe
            se_puede = True
    
    if se_puede:
        descomp = dict()
        for billete in lista:
            if importe >= billete:
                cantidad = importe//billete
                descomp[billete] = cantidad
                importe = importe%billete

    else:
        descomp = dict()
        print('no es posible descomponer dicho importe')

    return descomp

def main()-> None:
    lista_billetes = ingreso_billetes()
    print( cajero(lista_billetes) )     #devuelvo {denominacion: cantidad_de_billetes}

main()






'''
Ejercicio) "@RumboCircular" es un emprendimiento que enseña a cuidar el medioambiente. Rumbo Circular además de dictar cursos de capacitación sobre medioambiente en empresas, lanzó un conjunto de cursos para la comunidad general.
Estos cursos son los siguientes:
- Aprendé a hacer tu propio compost (1 día de curso). Costo $950
- Los niños y el medioambiente (para padres e hijes) (2 días de curso). Costo $990
- Tu huerta orgánica (4 días de curso). Costo $2500
El gran éxito de de estos cursos hizo que RumboCircular nos consultara para que los asesoremos para la creación de un pequeño sistema que permita organizar la asistencia de los participantes.
Los requerimientos que nos solicitan son los siguientes:
a- ABM (Alta – Baja – Modificación) de cursos. Se podrá cargar la siguiente infomación de los cursos. Nombre, cantidad de días, costo, cantidad de vacantes, fechas de dictado.
b- Listar todos los cursos cuyo costo sea superior a 1150 pesos.
c- Mostrar el o los cursos cuya cantidad de vacantes sea la máxima.
d- Mostrar todos los cursos que tengan al menos 3 fechas de dictado.
'''
# cursos = {
#   codigo: {
#       nombre: str,
#       costo: float,
#       cantidad_de_dias: int,
#       cantidad_de_vacantes: int,
#       fechas_de_dictado: list(str(dd/mm/yy))
#   }
# }
# cursos = [
#   [
#       nombre,
#       costo,
#       dias,
#       vacantes,
#       fechas = [
#           dia,
#           dia
#       ]
#   ]
# ]
#PRE:  No tiene
#POST: Va a dar de alta un nuevo curso, la llave del curso
#      debe ser distinta a las demas
'''
def dar_de_alta_curso(cursos:dict):
    curso = dict()
    llave = 0
    nombre = ""
    costo = 0.0
    dias = 0
    vacantes = 0
    fechas = list()
    flag_seguir_ingresando = True
    llave = int(input("Ingrese el código del nuevo curso: "))
    nombre = input("Ingrese el nombre del curso: ")
    costo = float(input("Ingrese el costo del curso: "))
    dias = int(input("Ingrese la cantidad de días del curso: "))
    vacantes = int(input("Ingrese la cantidad de vacantes del curso: "))
    while flag_seguir_ingresando:
        fecha = ""
        fecha = input(f"Ingrese una fecha para el curso: ")
        fechas.append(fecha)
        ingresar_corte = input("¿Quiere seguir ingresando datos <s/n>? ")
        if ingresar_corte != "s":
            flag_seguir_ingresando = False
    curso["nombre"] = nombre
    curso["costo"] = costo
    curso["cantidad_de_dias"] = dias
    curso["cantidad_de_vacantes"] = vacantes
    curso["fechas_de_dictado"] = fechas
    cursos[llave] = curso
def modificar_curso(cursos: dict):
    opcion = 0
    entrada = ""
    for key, value in cursos.items():
        llave = "nombre"
        print(f"{key} - {value[llave]}")
    opcion = int(input("Ingrese una opción: "))
    for key, value in cursos[opcion].items():
        print(f"{key} - {value}")
    entrada = input("¿Qué desea modificar del curso?: ")
    if entrada == "nombre":
        nombre = input(f"Ingrese el nuevo {entrada}: ")
        cursos[opcion][entrada] = nombre
    elif entrada == "costo":
        costo = float(input(f"Ingrese el nuevo {entrada}"))
        cursos[opcion][entrada] = costo
    elif entrada == "cantidad_de_dias":
        cantidad_de_dias = int(input(f"Ingrese la nueva {entrada}"))
        cursos[opcion][entrada] = cantidad_de_dias
    elif entrada == "cantidad_de_vacantes":
        cantidad_de_vacantes = int(input(f"Ingrese la nueva {entrada}"))
        cursos[opcion][entrada] = cantidad_de_vacantes
    elif entrada == "fechas_de_dictado": 
        flag_seguir_ingresando = True
        fechas_de_dictado = []
        ingreso_corte = ""
        while flag_seguir_ingresando:
            fecha = int(input(f"Ingrese las nuevas {entrada}"))
            fechas_de_dictado.append(fecha)
            ingresar_corte = input("¿Quiere seguir ingresando datos <s/n>? ")
            if ingresar_corte != "s":
                flag_seguir_ingresando = False
        cursos[opcion][entrada] = fechas_de_dictado
def dar_de_baja_curso(cursos: dict):
    opcion = 0
    entrada = ""
    for key, value in cursos.items():
        llave = "nombre"
        print(f"{key} - {value[llave]}")
    opcion = int(input("¿Qué curso desea eliminar?: "))
    cursos.pop(opcion)
def ABMCursos(cursos: dict) -> None:
    dar_de_alta_curso(cursos)
def ingresar_opcion(opciones: list):
    opcion = 0
    for x in range(len(opciones)):
        print(f"{x + 1} - {opciones[x]}")
    opcion = int(input("Ingrese una opción: "))
    return opcion
def main() -> None:
    opciones = [
        "ABM (Alta – Baja – Modificación) de cursos",
        "Listar todos los cursos cuyo costo sea superior a 1150 pesos",
        "Mostrar el o los cursos cuya cantidad de vacantes sea la máxima",
        "Mostrar todos los cursos que tengan al menos 3 fechas de dictado"
    ]
    cursos = {
        1: {
            "nombre": "Aprendé a hacer tu propio compost",
            "costo": 950.0,
            "cantidad_de_dias": 1,
            "cantidad_de_vacantes": 4,
            "fechas_de_dictado": ["10/06/2021"]
        },
        2: {
            "nombre": "Los niños y el medioambiente",
            "costo": 990.0,
            "cantidad_de_dias": 2,
            "cantidad_de_vacantes": 5,
            "fechas_de_dictado": ["09/06/2021", "15/06/2021"]
        },
        3: {
            "nombre": "Tu huerta orgánica",
            "costo": 2500.0,
            "cantidad_de_dias": 4,
            "cantidad_de_vacantes": 10,
            "fechas_de_dictado": ["01/06/2021", "04/06/2021", "21/06/2021"]
        }    
    }
    opcion = 0
    opcion = ingresar_opcion(opciones)
    while opcion != 5:
        if opcion == 1:
            ABMCursos(cursos)
            opcion = ingresar_opcion(opciones)
        elif opcion == 2:
            pass
            opcion = ingresar_opcion(opciones)
        elif opcion == 3:
            pass
            opcion = ingresar_opcion(opciones)
        elif opcion == 4:
            pass
            opcion = ingresar_opcion(opciones)
main()
'''