//Ejercicio 5 Escribir en C la función int buscar(const char *aguja, const char *pajar) que
//devuelve la primera posición en la que la cadena aguja aparece en pajar, o -1 si no aparece.
//Ejemplo: buscar("def", "abcdefhijk abcdefhijk") → 3
//Solo se permite utilizar la función strlen de la biblioteca estándar de C.
//13:50 - 15:10 ---> 1hr 20 min


#include<stdio.h>
#include<string.h>

int search(char pajar[], char aguja[]) {
    int i, j, firstOcc;
    i = 0, j = 0;

    while (pajar[i] != '\0') {  //si no termine de recorrer la palabra completa

        while (pajar[i] != aguja[0] && pajar[i] != '\0')    //recorro el pajar hasta encontrar una letra q coincida
            i++;                            //con la primera de la aguja

            //siempre y cuando no se haya terminado la palabra
        if (pajar[i] == '\0')   //(en ese caso devuelvo -1 y se acabo)
            return (-1);

        firstOcc = i;
        // recorro el pajar y la aguja mientras no terminen ninguna de las 2 palabras y
        while (pajar[i] == aguja[j] && pajar[i] != '\0' && aguja[j] != '\0') {  //si coinciden dos letras,
            i++;        //avanzo en el pajar
            j++;       //avanzo en la aguja
        }

        if (aguja[j] == '\0')   //si termine de recorrer la aguja antes,
            return (firstOcc);  //devuelvo la primera pos (first ocurrencie creo)
        if (pajar[i] == '\0')   //si termine de recorrer antres el pajar,
            return (-1);    //devuelvo -1 xq significa q termine la palabra y no encontre la palabra

        i = firstOcc + 1;
        j = 0;
    }
}

int main() {
    int loc;

    char pajar[] = "afholahola";
    char aguja[] = "hola";

    loc = search(pajar, aguja);

    if (loc == -1)
        printf("\nNot found");
    else
        printf("\nFound at location %d", loc + 1);

    return (0);
}