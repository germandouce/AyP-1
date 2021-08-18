//2) (Se debe resolver en C)
//Cree un programa en C que permita invertir un vector de números. El mismo deberá contener una
//función que realice la inversión y un main donde se muestre un ejemplo.
//Obs: el vector original y el final deben ser el mismo. Solo puede utilizarse la librería stdio.h
//Ejemplo
//Vector antes: {1,2,3,4,5}
//Función
//Vector después: {5,4,3,2,1}

#include <stdio.h>
#define MAX_CANT 10

void invertir_array_numeros(int *array, int tamanio){

    //printf("ndiuiuwu %i\n", tamanio);

    for (int i = 0; i < tamanio/2; ++i) {
        //printf("%i\n", array[i]);
        int numero = array[i];  //guardo la q voy a reemplazar

        array[i] = array[ tamanio - i - 1]; //la posicion toma el valor de la ultima

        array[tamanio -i -1] = numero;
    }
}

int main() {

    int array[MAX_CANT] = {1,2,3,4,5,6,7,8,9,10};  //escribir aca el array deseado max 30 numeros!!

    for (int i = 0; i < MAX_CANT; ++i) {
        printf("%i, ", array[i]);
    }
    printf("\n");
    int tamanio =  sizeof(array) / sizeof(array[0]);

    //printf("tamaniosss %i, %i, %i", tamanio, sizeof(array), sizeof(array[0]));

    invertir_array_numeros(array, tamanio);

    for (int i = 0; i < MAX_CANT; ++i) {
        printf("%i, ", array[i]);
    }

    return 0;
}
