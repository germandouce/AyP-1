//Dada la siguiente firma de función:
//void productoria(int vector[], int* producto, int tam); //Permite calcular la productoria de los
//elementos de un vector de enteros y el resultado debe ser guardado en el puntero 'resultado'.
//Se pide completar dicha función y utilizarla en un programa donde el usuario pueda especificar
//el tamaño y los elementos de un vector de enteros. El programa debe mostrar el resultado de la
//operación.
//Se garantiza que el tamaño del vector estará entre 1 y 100

#include <stdio.h>

#define MAX_TAM 100

void cargar_vector(int vector[], int tam){

    int num;
    printf("Ingrese numeros del vector: \n");
    for (int i = 0; i < tam; ++i) {
        scanf("%i", &num);
        vector[i] = num;
    }
}


void productoria(int vector[], int* producto, int tam){

    for (int i = 0; i < tam; i++){
        *producto = *producto * vector[i];
    }
}


int main() {

    int vector[MAX_TAM];
    int tam;

    printf("Ingrese el tamanio del vector de enteros: ");

    scanf("%i", &tam);

    cargar_vector(vector, tam);

    //Chequeo vector bien cargado
    //    for (int i = 0; i < tam; ++i) {
    //        printf("%i ", vector[i]);
    //    }

    int resultado = 1 ;

    productoria(vector, &resultado, tam);

    printf("El resultado de la productoria es: %i", resultado);

    return 0;
}
