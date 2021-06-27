'''
Se tiene un archivo de texto(alumnos.txt) con el siguiente formato:
padron, nombre, apellido
Luego se tiene otro archivo de texto(notas.txt) con el siguiente formato:
padrón, materia, nota
A partir de esa información, deseamos saber lo siguiente:
* La materia con mayor cantidad de aprobados (nota >= 4).
* El promedio general de cada materia.
* Los alumnos con un promedio general mayor a 7.
* El alumno con el mayor promedio.
'''
#ESTRUCTURA ELEGIDA:
#alumnos = {padron: Nombre:
#                   Apellido:
#                  } 
#           }
#notas ={materia:  {calificaciones = {padron: nota}
#                   }
#       }

def mostrar_notas_por_curso(notas: dict) -> None:
    print('Notas por curso\n')
    for materia in notas.keys():
        print(materia)
        for padron, nota in notas[materia]['calificaciones'].items():
                print(f'{padron}: {nota}')
        print()

def mostrar_datos_alumnos(alumnos: dict)-> None:
    print('Listado de alumnos\n')
    for padron, datos in alumnos.items():
        key_1= 'nombre'
        key_2= 'apellido'
        print(f'{padron}: {datos[key_1]}, {datos[key_2]}')
    print()

def materia_con_mas_aprobados(notas: dict)-> None:
    aprobados_por_materia = []
    for materia in notas.keys():
        cant_de_aprobados = 0
        for nota in notas[materia]['calificaciones'].values():
            if nota >=4:
                cant_de_aprobados+=1
        aprobados_por_materia.append([cant_de_aprobados, materia])
    
    materia_descanso = max(aprobados_por_materia)

    print('La materia con mas aprobados es ', end = '') 
    print(f'{materia_descanso[1]}, con {materia_descanso[0]} aprobados')
    print()

def promedio_general_por_materia(notas: dict)-> None:
    
    print('Promedio general por materia\n')
    
    promedio_por_materia = dict()

    for materia in notas.keys():
        tot_alumnos = 0
        nota_total = 0
        for nota in notas[materia]['calificaciones'].values():
            tot_alumnos +=1
            nota_total += nota        #como ya tengo los datos separados por materia se q no se repite!
        promedio_por_materia[materia]= nota_total/tot_alumnos
    
    for mate, promedio in promedio_por_materia.items():
        print(f'{mate}:','%.2f' %promedio)
    print()

def alumnos_promedio_mayor_a(notas: dict, alumnos: dict)-> None:
    print('Alumnos con promedio mayor a 7\n')
    promedio_por_padron =  dict()

    for materia in notas.keys():
        for padron, nota in notas[materia]['calificaciones'].items():
            if padron not in promedio_por_padron:
                promedio_por_padron[padron] = [nota,1] #el segundo ele es la cant de materias
            else:
                promedio_por_padron[padron][0]+=nota
                promedio_por_padron[padron][1]+=1

    for padron, datos in promedio_por_padron.items():
        prome = datos[0]/datos[1]
        if prome>=7:
            print(alumnos[padron]['nombre'], alumnos[padron]['apellido'], end = ' ')
            print(f'tiene promedio: {prome}')
    print()

def chico_diez(notas: dict, alumnos:dict)-> None:
    print('Alumno con mejor promedio\n')
    
    promedio_por_padron =  dict()

    for materia in notas.keys():
        for padron, nota in notas[materia]['calificaciones'].items():
            if padron not in promedio_por_padron:
                promedio_por_padron[padron] = [nota,1] #el segundo ele es la cant de materias
            else:
                promedio_por_padron[padron][0]+=nota
                promedio_por_padron[padron][1]+=1
    #print(promedio_por_padron)
    max_prom = [0,0]    #la pos 0 contiene el padron, la pos 1 el promedio
    for padron, datos in promedio_por_padron.items():
        prome = datos[0]/datos[1]
        if prome >= max_prom[1]:  
            max_prom = [padron, prome]
            #print(max_prom)      
    
    print(alumnos[max_prom[0]]['nombre'], alumnos[max_prom[0]]['apellido'], end = ' ')
    print(f'tiene el mejor promedio. Este es: {max_prom[1]}')

def obtener_notas() -> dict:
    notas = dict()

    with open('archivos/notas.txt', 'r') as arch_notas:
        for linea in arch_notas:
            linea = linea.strip('\n')
            linea =  linea.replace(' ','')
            datos =  linea.split(',')   #datos = [padron, materia, nota]
            
            if datos[1] not in notas:   #si no esta la materia
                
                materia = dict()

                #creo el dict de calificaciones para esa materia
                calificaciones = dict()    
                #entinedo q no voy a tener mas de una nota por padron xa un amisma materia
                calificaciones[datos[0]] = int(datos[2])
                
                #convierto el dict de calificaiones en clave de la materia
                materia['calificaciones'] = calificaciones 

                #convierto en clave del dict notas a la materia
                notas[datos[1]] = materia  
            
            else:            #si ya esta la materia
                #agrego el padron con su nota
                notas[datos[1]]['calificaciones'][datos[0]] = int(datos[2])
                
    return notas


def obtener_alumnos() ->dict:
    
    alumnos = dict()

    with open('archivos/alumnos.txt', 'r') as arch_alumnos:
        for linea in arch_alumnos:
            linea = linea.strip('\n')
            linea =  linea.replace(' ','')
            datos =  linea.split(',')   #alumno = [padron, Nombre, Apellido]

            #alumnos = {padron: Nombre:
            #                   Apellido:
            #             }    
                    
            alumno = dict()

            alumno['nombre'] = datos[1]
            alumno['apellido'] = datos[2]

            #convierto en clave del dict notas a la materia
            alumnos[datos[0]] = alumno               
        
        return alumnos

def main():
    notas = obtener_notas()
    alumnos = obtener_alumnos()
    mostrar_datos_alumnos(alumnos)
    mostrar_notas_por_curso(notas)
    materia_con_mas_aprobados(notas)
    promedio_general_por_materia(notas)
    alumnos_promedio_mayor_a(notas,alumnos)
    chico_diez(notas,alumnos)

main()
