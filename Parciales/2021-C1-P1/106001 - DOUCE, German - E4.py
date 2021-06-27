#ej 4)
'''
Crear una función que reciba un string que contiene números y los ordene de menor a mayor; pero 
teniendo las siguientes consideraciones:
Si hay números repetidos (solo van a poder estar repetidos 1 vez):
o Los números repetidos pares irán copiados en otra lista. (Además de estar en la ordenada)
o Los números repetidos impares deberán ir en la misma lista que los anteriores (además de estar en 
la ordenada), pero escritos como el número menor y par más próximo que tengan. 
Ejemplo: Si es 5, su par menor más cercano es 4.
La función debe devolver un string con los números ordenados, separados por comas y además los 
repetidos ordenados al final.
Ejemplo: cadena = '275217'
>>>1, 2, 2, 5, 7, 7, 2, 6
'''
#los comentrarios son muy obvios pero son xa mi

def ordena_numeros(num:str) ->str:
    
    lista_num = list()
    repetidos = list()
    

    for n in num:
        lista_num.append(n) #guardo todos
        if lista_num.count(n) == 2 :        #si esta dos veces, es decir repetdio 1,  
            if int(n)%2 == 0:   #si es par
                repetidos.append(n)  #va a repetidos
            else:       #si es impar
                repetidos.append( str (int(n)-1 ) ) #tmb va a repess pero escrito como el par menor mas prox
            
    lista_num.sort()    #ordeno todos
    repetidos.sort()    #ordeno los repes
    
    for n in repetidos:
        lista_num.append(n)     #cargo los repes al final de la lista grande

    cadena_num = ','.join(lista_num)    
    return cadena_num


def main()-> None: 
    numero = '275217'
    print(ordena_numeros(numero))

main()