from typing import Final
import pylint
#CLASE 01 - INTRO A LA COMPUTACION
#CLASE 02 - NUMERACION
#CLASE 03 - INTRO A LA PROGRAMACION
#CLASE 04 - DECISIONES

#CLASE 05 - CICLOS I

#ej 1: ingresar numeros y calcular su suma
'''
sum=0
for i in range(10):
    num=int(input('ingrese numero %s: '%(i+1)))
    sum+=num
print(sum)
'''
#ej 2: solicita ingresar mas gatos a preferencia del user
'''
gatos=0
gatos_tot=0
quiero=1
while gatos>=0 and quiero==1:
    gatos=int(input('ingrese numero de gatos: '))
    gatos_tot+=gatos
    quiero=int(input('quiere agregar mas gatos? 1/si 0/no: '))
print(gatos_tot)
'''             
#ej 3: ingresar numeros, determinar max y min
'''
num = int(input('ingrese un numero: '))
max = num
min = num
mas = input('agregar mas numeros (si/no): ')
while mas == 'si':
    num = int(input('ingrese un numero: '))
    if num >= max:
        max = num
    if num <= min:
        min = num
    mas = input('agregar mas numeros (si/no):')
print('el maximo es',max)
print('el minimo es',min)
'''
#Bruno Lanz
#ej 4
'''1- (nivel inicial)
Se pide hacer un programa que permita el ingreso de 10 números y 
muestre por pantalla el valor máximo, el mínimo y el promedio de los mismos.'''
#con for
'''
for i in range (10):
    n = int(input('ingrese numero: %s: '%(i+1)))
    if i == 0:
        max = n
        min = n
        sum = 0
    else:
        if n >= max:
            max = n
        if n <= min:
            min = n
    sum += n
prom = (sum/10)
print('el max es:',max,'y el min es:',min)
print('promedio:',prom)
'''
#con while
'''
vueltas = 1
n = int(input('ingrese numero 1: '))
max = n
min = n
sum=n
while vueltas <= 9:
    n=int(input('ingrese numero %s: '%(vueltas+1)))
    if n >= max:
        max=n
    if n <= min:
        min=n
    sum += n
    vueltas += 1
print('el mayor es', max, 'y el minimo es', min)
print('promedio =', sum/10)
'''
#ej 5
'''2- (nivel pro)
Hacer un programa que permita el ingreso de los alumnos y las notas correspondiente a 3 
cátedras de la materia Algoritmos de FIUBA. Para esto sabemos que cada cátedra tiene 
inscriptos a un número indeterminado a priori de alumnos, y que los datos que poseemos de 
cada alumno son Nombre y Apellido, padrón, nota final
Se pide:
   a- Calcular la nota más alta de cada curso y a qué alumno pertenece (mostrar padrón)
   b- Calcular la nota más baja entre todos los cursos.
   c- Calcular la cátedra cuyo promedio de nota sea el máximo.
   d- Mostar la cantidad total de alumnos de los 3 cursos.
'''
'''
sum_x3 = 0
tot_x3 = 0
min_nota_todos = 10
prom_best_cat = 0
for catedra in range(1,4):
    print('catedra',catedra)
    tot=0
    sum=0
    max_nota=0
    min_nota=10
    nuevo = '1'
    while nuevo == '1':
        nom = input('ingrese nombre: ')
        apel = input('ingrese apellido de %s: ' %nom)
        padron = input('padron: ')
        nota = int(input('ingrese nota: '))
        if nota >= max_nota:
            max_nota = nota
            chico_10 = padron
        if nota <= min_nota:
            min_nota = nota 
        sum += nota
        tot += 1
        nuevo = input('otro (1/si, otro/no): ')
    prom = sum/tot
    tot_x3 += tot

    if prom >= prom_best_cat:
        prom_best_cat = prom
        catedra_de_genios = catedra 

    if min_nota <= min_nota_todos:
        min_nota_todos = min_nota
    
    if catedra == 1:
        Nota_max_cat_1 = max_nota
        chico_10_cat_1 = chico_10
        prom_cat_1 = prom
    if catedra == 2:
        Nota_max_cat_2 = max_nota
        chico_10_cat_2 = chico_10
        prom_cat_2 = prom
    if catedra == 3:
        Nota_max_cat_3 = max_nota
        chico_10_cat_3 = chico_10
        prom_cat_3 = prom

print('nota max cat 1:', Nota_max_cat_1,'de padron:', chico_10_cat_1)
print('nota max cat 2:', Nota_max_cat_2,'de padron:', chico_10_cat_2)
print('nota max cat 3:', Nota_max_cat_3,'de padron:', chico_10_cat_3)
print('nota mas baja de todos los curso:', min_nota_todos)
print('la catedra con max promedio es la:', catedra_de_genios, 'con un promedio de',
prom_best_cat)
print('total de alumnos:', tot_x3)
'''

#CLASE 06 - CICLOS II

#ej 1
'''Solicitar al usuario que ingrese números enteros positivos.
La condición de corte es que se ingrese el número -1.
Al finalizar, mostrar cuántos de los números ingresados por el usuario fueron 
números pares.'''
'''
num=0
pares = 0
while num !=-1:
    num=int(input('ingrese numeros enteros positivos: '))
    if num%2 == 0:
        pares += 1
print('se ingresaron', pares, 'numeros pares')
'''
#ej 2
'''Un número perfecto es aquel número que es igual a la suma de todos
sus divisores positivos excepto el mismo. El primer número perfecto es 6, ya 
que 1+2+3=6. Escribir un programa que muestre todos los números perfectos hasta
un número dado por el usuario.
Ayuda:
Entre 0-10.000 hay solo 3 números perfectos'''
'''
num= int(input('ingrese numero: '))
for dividendo in range (1,num+1):
    sum = 0
    for divisor in range (1,dividendo):
        if dividendo % divisor == 0:
            sum += divisor
    if sum == dividendo:
        print(dividendo,'es numero perfecto')
'''
#ej 3
'''
Realizar un programa que permita jugar a adivinar un número entero. El participante
A elige el número a adivinar y luego hace jugar al participante B, el cual 
deberá intentar adivinarlo arriesgando números. El programa debe guiar al 
participante B indicándole, en cada intento, si el número arriesgado es mayor o
menor al definido por el participante A. El juego debe concluir al acertar el 
número o superar los 20 intentos. Al acertar el número debe indicar la cantidad 
de intentos que fueron utilizados para lograrlo. En caso de no haber 
conseguido el objetivo, debe indicarle que ha superado los 20 intentos.
'''
'''
num = int(input('ingrese numero a adivinar: '))
n_a = int(input('ingrese un numero: '))

intentos=1
while intentos <= 20  and (n_a != num):
    if n_a > num:
        print('arriesgo un numero mayor')
    else: 
        print('arriesgo un numero menor')
    intentos += 1
    n_a = int(input('adivine el numero: '))

if n_a != num:
    print('perdiste, se acabaron los 20 intentos el numero era',num)
else:
    print('ADIVINASTE! utilizaste',intentos,'intentos')
'''
#tarea
#ej 1
'''Se pide hacer un programa que ingrese 8 juegos de n valores positivos cada uno. Considerar
un condiciòn de corte para el n. Calculando el promedio de cada juego, el máximo de cada 
juego y el mínimo de todos los juegos.'''
'''
min_todos_juegos = 0

for juego in range(1,9):
    print('juego',juego)
    tot = 0
    sum = 0
    n = int(input('ingrese numeros positivos cortar con -1: '))
    while n < 0 and n != -1:
            n= int(input('ingrese numero POSITIVO: '))
    if n == -1:
        n_max = 'NO SE INGRESARON NUMEROS'
        n_min = 'NO SE INGRESARON NUMEROS'
    else:
        n_max = n
        n_min = n
    while n != -1:
        if n >= n_max:
            n_max = n
        if n <= n_min:
            n_min = n
        sum += n
        tot += 1
        n = int(input('ingrese numeros positivos: '))
        while n < 0 and n != -1:
            n= int(input('ingrese numero POSITIVO: '))

    if tot >0 :
        prom = sum/tot
    else:
        prom = 0

    if n != -1:
        if n_min <= min_todos_juegos:
            min_todos_juegos = n_min
    
    if juego == 1:
        prom_juego_1 = prom
        max_juego_1 = n_max
    elif juego == 2:
        prom_juego_2 = prom
        max_juego_2 = n_max
    elif juego == 3:
        prom_juego_3 = prom
        max_juego_3 = n_max
    elif juego == 4:
        prom_juego_4 = prom
        max_juego_4 = n_max
    elif juego == 5:
        prom_juego_5 = prom
        max_juego_5 = n_max
    elif juego == 6:
        prom_juego_6 = prom
        max_juego_6 = n_max
    elif juego == 7:
        prom_juego_7 = prom
        max_juego_7 = n_max
    else:
        prom_juego_8 = prom
        max_juego_8 = n_max

print('max juego 1:', max_juego_1,'prom juego 1:', prom_juego_1)
print('max juego 2:', max_juego_2,'prom juego 2:', prom_juego_2)
print('max juego 3:', max_juego_3,'prom juego 3:', prom_juego_3)
print('max juego 4:', max_juego_4,'prom juego 4:', prom_juego_4)
print('max juego 5:', max_juego_5,'prom juego 5:', prom_juego_5)
print('max juego 6:', max_juego_6,'prom juego 6:', prom_juego_6)
print('max juego 7:', max_juego_7,'prom juego 7:', prom_juego_7)
print('max juego 8:', max_juego_8,'prom juego 8:', prom_juego_8)
print('El minimo de todos los juegos es: ', min_todos_juegos)
'''
#CLASE 07 - FUNCIONES I

#test isnumeric()
'''
a='0'
if a.isnumeric():
    print(a)
# isnumeric() -> true if int #false 4 the rest (float or letters )
'''
#function ex
'''
num_1 = int(input('ingrese un numero: '))
num_2 = int(input('ingrese un numero: '))

def suma (n_1:int,n_2:int) -> str:
    sum = n_1 + n_2
    return sum
print(suma(num_1,num_2))
'''
#debugging test
'''
a=4
for i in range(10):
    for j in range(2):
        print('a')
'''

#CLASE 08 - FUNCIONES II

'''1. Escribir una función que permita calcular la duración en segundos de un intervalo 
dado en horas, minutos y segundos.
2. Usando la función del ejercicio anterior, escribir un programa que pida al 
usuario dos intervalos expresados en horas, minutos y segundos, sume sus 
duraciones, y muestre por pantalla la duración total en horas, minutos y segundos.
'''

#ej:
''' 1. Escribir una función que permita calcular la duración en segundos de un intervalo dado en horas,
 minutos y segundos.
2. Usando la función del ejercicio anterior, escribir un programa que pida al usuario dos intervalos
 expresados en horas, minutos y segundos, sume sus duraciones, y muestre por pantalla la duración total en horas,
  minutos y segundos.'''
'''
def convertir_a_segundos(hora : int, minuto : int, segundo : int) -> int:
    return (hora*3600 + minuto*60 + segundo)

def convertir_a_formato(total : int) -> tuple:
    hora = (total // 3600)
    minutos = (total % 3600) // 60
    segundos = (total % 60)
    return hora,minutos,segundos

def ingresar_intervalo() -> int:
    hora = input("Ingresar hora: ")
    while not (hora.isnumeric() and int(hora) >= 0):
        hora = input("Error! Ingrese un valor válido: ")
    minuto = input("Ingrese minutos: ")
    while not (minuto.isnumeric() and int(minuto) >= 0 and int(minuto) < 60):
        minuto = input("Error! Ingrese un valor válido: ")
    segundo = input("Ingrese segundos: ")
    while not (segundo.isnumeric() and int(segundo) >= 0 and int(segundo) < 60):
        segundo = input("Error! Ingrese un valor válido: ")
    print(f"\n\n Ingresó la hora {hora}:{minuto}:{segundo}\n\n")
    return hora, minuto, segundo

def main() -> None:
    CANT_INTERVALOS = 2
    suma = 0
    for i in range(CANT_INTERVALOS):
        print(f"\t\tDATOS DE INTERVALO {i+1}")
        hora, minuto, segundo = ingresar_intervalo()
        suma += convertir_a_segundos(int(hora), int(minuto), int(segundo))
    
    horas, minutos, segundos = convertir_a_formato(suma)
    print(f"La suma de los tiempos da {horas}:{minutos}:{segundos}")
main()
'''

#ej tarea:
'''Les dejo un ejercicio para que practiquen:
(El ejercicio se llama: ODIO A LOS IMPARES) Crear un programa que:
Permita ingresar 5 números enteros positivos.
Calcule el máximo entre esos números; lo muestre.
Calcule el mínimo; lo muestre.
Calcule el promedio; lo muestre.
Sume el máximo, el mínimo; y el promedio (Resultando en un entero. Para eso pueden castear 
el resultado a int. Ejemplo: int(resultado)) y en caso de que el resultado sea par; 
salude al usuario tantas veces como número resultante de esa cuenta, si es impar; 
vuelve a empezar *ToDo* el programa DE NUEVO.'''
'''
#funciones 
#ingrese 5 numeros positivos
#calcule min y muestre
#calcule promedio y lo muestre
#sume max min y promedio y devuelva un entero (sume?)
#si es par salude y si es impar empieze el programa de nuevo

def ingreso() -> int:
    #PRE:
    #POST: devuelve un numero entero positivo 
    num = int(input('ingrese numero: '))
    while num <= 0 or num % 1 != 0:
            num = int(input('ingrese numero: '))
    return num


def max_y_min (num: int, maximo:int, minimo:int) -> tuple:
    #PRE: num es un numero entero positivos
    #POST: devuelve el maximo y el minimo numero cargado hasta el momento
    if num >= maximo:
        maximo = num

    if num <= minimo:
        minimo = num
    
    return maximo, minimo


def promedio_num(suma_num) -> float:
    #PRE: suma_num es la suma de los 5 numeros enteros positivos ingresados
    #POST: devuelve el promedio de esos 5 numeros como float 
    promedio = suma_num/5
        
    return promedio


def suma(maximo:int, minimo: int, promedio: float) -> float:
    #PRE: maximo y minimo son enetros positivos, promedio es un float
    #POST:devuelve un float resultado de la suma de los parametros ingresados:
    total = maximo + minimo + promedio

    return total


def mostrar(maximo:int, minimo:int, promedio:int) -> None:
    #PRE: maximo minimo y promedio son enetros previamente calculados
    #POST: muestar por panatallo lo siguiente:
    print(f"El máximo es {maximo}")
    print(f"El mínimo es {minimo}")
    print(f"El promedio es {promedio}")
  

def es_par(suma_total: int) -> bool: 
    #PRE: suma_total es un entero
    #POST: devuelve un booleano dependiendo si es par o no
    lo_es = True
    if suma_total %2 != 0:
        lo_es = False

    return lo_es


def main() -> None:
    for i in range(5):
        num = ingreso()
        if i == 0:
            maximo = num
            minimo = num
            suma_num = 0
        suma_num += num #me parecio demasiado crear un funcion especial xa sumar los numeros ingresados
        maximo, minimo = max_y_min(num, maximo, minimo,)

    promedio = promedio_num(suma_num)
    suma_total = int(suma(maximo, minimo, promedio)) #casteo a entero aqui 
    mostrar(maximo, minimo, int(promedio))
    print()
    
    if es_par(suma_total):
        print()
        for i in range(suma_total):
            print('hola, ', end = '')
    else:
        main()

main()

'''

#CLASE 09 FUNCIONES III

#ej de parametro por defecto
'''
def saludar(saludo: str, receptor: str = 'mundo') -> None:  #el segundo parametro es 'mundo' x default
    print(saludo + " " + receptor)                 #si no se manda el primero     

def main () -> None:
    saludar('hola')     #si no le mando los 2 parametros (uno solo, )
    saludar('hola', 'juan')

main()
'''
#Otro ejemplo con comentario de documentacion
#al comentario se le llama Docsstrings y va entre """"docsstring """"
#OJO! el comentario asi ' ' ' falla en las funciones. USAR """" !!!
'''
def saludar(saludo: str = 'adios', receptor: str = 'mundo') -> None:  #el segundo parametro es 'mundo' x default
    """T saluda""" # ejemplo de comentario de documentacion
    """esto ya no lo toma"""
    print(saludo + " " + receptor)                 #si no se manda el primero     

def main () -> None:
    #asi no toma la documentacion, es un comentario
    saludar()     #si no le mando ninguno, necesito 2 parametrso x defecto. ver arriba...
    saludar('hola', 'juan')

main()
'''

#CLASE 10 - MAYUSCULA

#Se vio pptx
#ejs propuestos

#CLASE 11 - BUENAS PRACTICAS + PRACTICA MATRICES
'''
def generar_matriz_identidad(tam_matriz: int) -> list: #A completar
    """
    Pre: Recibe el tamaño deseado de la matriz a generar.
    Post: Retorna una matriz identidad de tamaño N.
    """
    matriz_identidad = []
    for i in range(tam_matriz):
        fila = []
        for j in range(tam_matriz):
            if i == j:
                fila.append(1)
            else:
                fila.append(0)
        matriz_identidad.append(fila)
    return matriz_identidad

m1 = generar_matriz_identidad(3)
m2 = generar_matriz_identidad(3)
for i in range (len(m1)):
    print (m1[i])
print()
for i in range (len(m2)):
    print (m2[i])

matriz_suma = []
for i in range (3):
    matriz_suma.append([])
for i in range (len(m1)):
    for j in range (len(m2)):
        matriz_suma[i][j]= i+j

for i in range (len(matriz_suma)):
    print (matr[i])
'''

#CLASE 12 -  Dict, Set DUDAS TP

#Hubo martes feriado => martes pares jueves impares

#CLASE 13 - Sets, Sort, search + funciones especiales (map, filter, lambda) 
'''
a= set()
a.add(1)

b={1,2}

print(a.intersection(b))
'''

#CLASE 14 - Recurrencia basico.
#Discos de Hanoi
'''
paso = 1
def hanoi(discos, origen, destino, aux):
    if discos == 0: return
    hanoi(discos-1, origen, aux, destino)
    global paso #Perdon bruno
    print(paso, "- Mover disco de palo", origen, "hacia", destino)
    paso += 1
    hanoi(discos-1, aux, destino, origen)

hanoi(5,1,3,2) #Mover 5 discos del palo 1 al palo 3, usando el palo 2 como auxiliar y siguiendo las reglas de las Torres de Hanoi 
'''
#Un par de algos mas...
'''
#Factorial recursivo!

def factorial(n):
    if n == 0: 
        return 1
    else: 
        return ( n * factorial(n-1) )

#Fibonacai recursivo!

def fibonacci(n):
    if n <= 1: return n
    return fibonacci(n-1) + fibonacci(n-2)


#MCD (maximo comun divisor) recursivo!

def gcd(x, y):
    if x == 0: return y
    return gcd(y%x, x)

#Demo
print("0!","3!","5!")
print(factorial(0), factorial(3), factorial(5))
print("\nPrimeros diez numeros de fibonacci:")
for i in range(10):
    print(fibonacci(i), end = " ")
print("\n\nDivisor comun mas grande de 25 y 15")
print(gcd(25, 15))
print("Divisor comun mas grande de 25 y 17")
print(gcd(25, 17))
'''

#CLASE: 15: ejs varios
#Jueves 1/6/2021        A partir de aca empiezo a poner fechas...

#EJ 1

'''
Cree un programa que permita al usuario elegir entre las siguientes opciones:
1 - Agregar un alumno: debe solicitarse nombre, padrón y nota.
2 - Consultar aprobados: debe mostrar los alumnos con nota mayor a 4.
3 - Cantidad de alumnos totales y promedio general.
4 - Quitar a un  alumno.
5 - Salir
'''
#notas o metodo x estos ejs tipicos de parcial tipo abm

#*1ero, menu, print (ctrl copy enunciado)
#una funcion xa agrgegar alumno, estructura xa cargar alumnos
#ej litsa_de_alumnos
#aprobados --> recorrrer la estructura y ver si aprobo o no

#PUNTOS 1 Y 2 
'''
def consultar_nota(alumnos: list) -> None:
    for i in range ( len (alumnos) ):
        if alumnos[i][2] >= 4:
            print(alumnos[i])


def agregar_alumno() -> list:
    """
    """
    alumnos = list()
    basta = False
    while not basta:
        nombre = input('Ingrese Nombre del alumno: ')    
        padron = input(f'Ingrese padron de {nombre}: ')
        nota = int( input(f'Ingrese nota de {nombre}: ') )   
        
        alumnos.append( (nombre, padron, nota) )
        
        opc = int(input('desea ingresar otro alumno? 1- si 0- No: '))
        
        if opc == 0:
            basta = True
    
    return alumnos

def main():
    salir = False
    while not salir:
        print('1 - Agregar un alumno: debe solicitarse nombre, padrón y nota')
        print('2 - Consultar aprobados: debe mostrar los alumnos con nota mayor a 4.')
        print('3 - Cantidad de alumnos totales y promedio general.')
        print('4 - Quitar a un  alumno.')
        print('5 - Salir ')
        
        opc = int(input(''))
        if opc == 1:
            alumnos = agregar_alumno()
            print('Alumnos ingresados')
            print(alumnos)
        
        if opc ==2:
            consultar_nota(alumnos)
        
        opc = int(input('Desea salir del menu? 0 - no 1 - si: '))
        
        if opc ==1:
            salir = True
main()
'''
#COMPLETO
#Constantes que servirán de índices más adelante.
'''
PADRON = 0
NOTA = 1
def agregar_alumno(alumnos : dict) -> None:
    """
    Agrega el alumno al diccionario alumnos
    """
    nombre = input("Nombre del alumno: ")
    padron = int(input("Padron del alumno: "))
    nota = float(input("Nota del alumno: "))
    alumnos[padron] = [nombre, nota]
def mostrar_aprobados(alumnos):
    """
    Recibe un diccionario con los alumnos. Muestra en pantalla todos los alumnos con nota > 4
    """
    print("Los alumnos aprobados son: ")
    for padron, datos in alumnos.items():
        if datos[NOTA] > 4:
            print(f"{alumnos[padron][0]}, nota: {datos[1]}") 
def quitar_alumno(alumnos : dict, padron : int) -> None:
    """
    Elmina el alumno del diccionario alumnos
    """
    del alumnos[padron]
def calcular_promedio(alumnos: dict) -> float:
    """
    Calcular el promedio general
    """
    cant_alumnos = 0
    suma_notas = 0
    for alumno in alumnos:
        cant_alumnos += 1
        suma_notas += alumnos[alumno][NOTA]
    return suma_notas / cant_alumnos
def main():
    alumnos = {}
    print("""
        1 - Agregar un alumno: debe solicitarse nombre, padrón y nota.
        2 - Consultar aprobados: debe mostrar los alumnos con nota mayor a 4.
        3 - Cantidad de alumnos totales y promedio general.
        4 - Quitar a un  alumno.
        5 - Salir
        """)
    opcion = int(input("Elige una opcion: "))
    while opcion != 5:
        if opcion == 1:
            #Pido al usuario los datos del alumno
            agregar_alumno(alumnos)
            print("Alumno agregado con exito")
        if opcion == 2:
            mostrar_aprobados(alumnos)
        if opcion == 3:
            suma_notas = 0
            for _, nota in alumnos.values():
                suma_notas += nota
            print(f"Alumnos totales: {len(alumnos)}, promedio general: {suma_notas/len(alumnos)}")
        if opcion == 4:
            padron = int(input("Ingrese el padron del alumno que desea eliminar: "))
            quitar_alumno(alumnos, padron)
            print("Alumno quitado con éxito")
        opcion = int(input("Vuelva a ingresar una opcion: "))
    print("Saliendo...")
main()
'''
#EJERCICIO 2: 
#19:13 - 
#a) 
'''
Se solicita crear una función en la cual reciba un texto(string) como parámetro,
y que devuelva un diccionario con las palabras como clave y como valor la cantidad de veces que 
se repite dicha palabra, a modo de ejemplo, dado el siguiente texto:
    Auto Casa Avion Auto casa casa
la función deberá devolver el siguiente diccionario:
    {"Auto":2, "Casa":1, "Avion":1, "casa":2}
'''
#b)
'''
def palabras_repes(texto: str) -> dict:
    plbrs_repes = {}
    texto = texto.split(' ')
    for palabra in texto:
        if palabra not in plbrs_repes.keys():
            plbrs_repes[palabra] = 1
        else:
            plbrs_repes[palabra] +=1

    return plbrs_repes

#texto =  input('Ingrese un texto: ')
#print( palabras_repes(texto))
'''
'''
Una vez se haya implementado la función, se solicita crear otra función que en vez de contar 
cada palabra, cuente cada letra, es decir que del texto anterior debe salir el sig. diccionario:
    {'A': 3, 'u': 2, 't': 2, 'o': 3, 'C': 1, 'a': 6, 's': 3, 'v': 1, 'i': 1, 'n': 1, 'c': 2}
'''
'''
def letras_repes(texto: str) -> dict:
    letras_repes = {}
    for letra in texto:
        if letra not in letras_repes.keys():
            letras_repes[letra] = 1
        else:
            letras_repes[letra] +=1

    return letras_repes

texto =  input('Ingrese un texto: ')
print( letras_repes(texto))
'''
#ej de parcial
#ejemplo de modelacion
'''
#numero de articulo, descripcion, color cantidad, precio
#Articulos = {'id'}: [desc, color, cant, precio]}
#clientes = {'id': razon_social}

#Nro de cuenta, Razon Social, Articulos, color, cantidades pedidas
#pedidos = {'id': [id_articulo, id_cliente, cantidad, color]}
'''

#CLASE: 16: práctica parcial
#Martes 8/6/2021
#ej 3) parcial
'''
Se pide realizar una función que devuelva el número entero más pequeño de un listado 
ingresado por el usuario, tal que la suma de los N números exceda un valor pasado por parámetro
en la función.
'''
#cunado la smatoria supera al numero valor del usuario, hay q devolver el menor numero ingresao
'''
def mas_pequenio(limite: int) -> int:
    
    numeros: list = list()
    sum = 0
    
    while sum<= limite:
        num = int(input('Ingrese numeros: '))
        
        numeros.append(num)
        sum += num

    menor = numeros[0]
    for i in range (1, len(numeros) ):
        if numeros[i] <0:
            menor = numeros[i]
    return menor

print(mas_pequenio(12))
'''
#usar funcion min!!

#ej 5)
'''
Escribir un programa que primero solicite una palabra al usuario y luego le permita al usuario 
ingresar 5 palabras. El sistema deberá calcular cuántas y cuáles palabras de las 5 ingresadas 
pueden escribirse exactamente con las letras de la palabra ingresada al principio (utilizando 
todas las letras y sin repetir ninguna).
Ej: Palabra inicial: CASO
5 palabras: MAMA, CLASE, SACO, COSA, PEPE
EL sistema deberá devolver 2 palabras (SACO y COSA).
'''
#resolucion: supongo correcta...
'''
def chequeo(letras_base):
    
    palabras: list = list()
    posibles: list = list()

    for i in range(5):
        palabra = input('Ingrese palabra: ')
        palabras.append(palabra)
    
    print(letras_base)
    for i in range (len(palabras)):
        for letra in letras_base:
            vale = True
            if palabras[i].count(letra) != 1:   
                vale = False                    
        if vale:
            posibles.append(palabras[i])
    
    print(posibles)

def palabra_inicial()-> list:
    palabra = input('Ingrese una palabra: ')
    letras_base:list = list()

    for letra in palabra:
        letras_base.append(letra)
    
    return letras_base

def main():
    letras_base = palabra_inicial()
    chequeo(letras_base)
main()
'''
'''
Bruno Lanzillotta  19:49
Ejercicio) “@RumboCircular” es un emprendimiento que enseña a cuidar el medioambiente. Rumbo Circular además de dictar cursos de capacitación sobre medioambiente en empresas, lanzó un conjunto de cursos para la comunidad general.
Estos cursos son los siguientes:
- Aprendé a hacer tu propio compost (1 día de curso). Costo $950
- Los niños y el medioambiente (para padres e hijes) (2 días de curso). Costo $990
- Tu huerta orgánica (4 días de curso). Costo $2500
El gran éxito de de estos cursos hizo que RumboCircular nos consultara para que los asesoremos para la creación de un pequeño sistema que permita organizar la asistencia de los participantes.
Los requerimientos que nos solicitan son los siguientes:
a- ABM (Alta – Baja – Modificación) de cursos. Se podrá cargar la siguiente infomación de los cursos. Nombre, cantidad de días, costo, cantidad de vacantes, fechas de dictado.
b- Listar todos los cursos cuyo costo sea superior a 1150 pesos.
c- Mostrar el o los cursos cuya cantidad de vacantes se la máxima.
d- Mostrar todos los cursos que tengan al menos 3 fechas de dictado.
'''
#CLASE: 17: práctica parcial
#jueves 10/6/2021

#parcial 11/08/20
#ej 2) (corto??)
'''
Escriba una función que dada una lista de denominaciones de billetes de la moneda corriente de un 
país, permita descomponer un importe otorgado por el usuario en las cantidades correspondientes a 
cada una de las denominaciones cual si fuera un cajero automático y suponiendo que siempre elige 
otorgar billetes del mayor valor posible. La función debe controlar que el importe sea factible de 
ser descompuesto y devolver un diccionario con la descomposición.  Construya el programa principal 
donde utiliza dicha función.  
Ej: Lista = [10,20,50,100,200,500,1000]  
Valor = 1690  Diccionario = {10:0,20:2,50:1;100:1;200:0;500:1;1000:1}
'''
#20:00 - 20:25 --> 25 minutos
#hacer q usuario ingrese lista y ordenarla
'''
def cajero(lista)-> dict:
    importe = int(input('Ingrese importe a descomponer: '))
    
    es_posible = False
    for billete in lista:
        if importe%billete == 0: #con q alguno divida enteramente ya puedo descomponer
            es_posible = True
    if es_posible:
        lista = lista[::-1] #doy vuelta suponiendo q ingreso de menor a mayor
        descomp =  dict()
        for billete in lista:
            descomp[billete] = 0

        for billete in lista:
            if importe>= billete:
                cantidad = importe//billete
                resto = importe%billete
                descomp[billete] = cantidad
                importe = resto

    else:
        print('no es posible descomponer')

    return descomp

lista = [10,20,50,100,200,500,1000]
print(cajero(lista))

'''

#CLASE 18: PARCIAL
#Martes 15/06/2021

#CLASE 19: REVISION DEL PARCIAL
#Jueves 17/06/2021                    
