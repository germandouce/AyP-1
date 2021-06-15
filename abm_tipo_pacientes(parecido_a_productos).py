'''
Un pequeño menú que permita :
a- La carga o modificación de un pedido (Un pedido puede estar compuesto por más de un artículo)
b- La carga o modificación de un stock existente
c- Listar los pedidos de un nro de cuenta o Razón Social dada
d- Mostrar el pedido cuya valorización sea la mayor
e- Listar todos los pedidos cargados.
'''

#estructura abm:
    # tratamientos = {
    #           {1:
    #              nombre:
    #              costo:             
    #              cantidad:     
    #            }    
    #           
    #                   }
    # pacientes = { 
    #            {dni:
    #                 nombre:    
    #                 consultas                     
    #                  tratamientos_realizados {tipo_tratamiento: cantidad 
    #                                                   
    #                    } 
    #               }



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

    #estructura abm:
    # tratamientos = {
    #           {1:
    #              nombre:
    #              costo:             
    #              cantidad:     
    #            }    
    #           
    #                   }
    # pacientes = { 
    #            {dni:
    #                 nombre:    
    #                 consultas                     
    #                  tratamientos_realizados {tipo_tratamiento: cantidad 
    #                                                   
    #                    } 
    #               }


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

