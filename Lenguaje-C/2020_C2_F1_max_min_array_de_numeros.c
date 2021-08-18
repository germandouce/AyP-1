//2) (Se debe resolver en C)
//Implementar una función en C que permita hallar el valor máximo y mínimo de un vector de enteros,
//sabiendo que la firma de la función es la siguiente:
//void hallar_max_min(int array[], int n, int* max, int* min);
//Se debe ejemplificar su uso desde una invocación a la misma en el programa principal.

//MI VERSION!!
//TIEMPO: 14:00 -
#include <stdio.h>
#define MAX_CANTIDAD 20

void hallar_max_min(int array[], int n, int* max, int* min){
    *max = array[0];
    *min = array[0];

    printf("longitud del array: %i\n", n);

    for (int i = 0; i < n ; ++i) {
        printf("%i\n", array[i]);
        if (array[i] >= *max){
            *max = array[i];
        }
        if(array[i] <= *min){
            *min = array[i];
        }
    }
}


int main() {
    int array[MAX_CANTIDAD] = {7,-42,4,5,1,-8,12,13,5,8,10,22,23};
    int max;
    int min;
    int n =  sizeof(array) / sizeof(array[0]);

    hallar_max_min(array, n, &max, &min);
    printf("max: %i\n", max);
    printf("min: %i\n", min);
    return 0;
}
