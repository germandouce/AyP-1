//Realizar un programa que permita ingresar N valores enteros, donde N debe ser una constante declarada en el programa.
//Dicho programa debe tener dos funciones que permitan:
//1. Obtener promedio de todos los valores ingresados.
//2. El valor más grande ingresado.

#include <stdio.h>
#define N 3

void ingresar_valores(int numeros[],int tamanio){
    int num;
    printf("Ingrese %i numeros: \n", tamanio);
    for (int i = 0; i < tamanio ; ++i) {
        scanf("%i", &num);
        numeros[i] = num;
    }
}

double obtener_promedio(const int numeros[], int tamanio){
    double suma = 0;
    double cont = 0; //para hacer promedio = float/float "mas correcto"
    for (int i = 0; i < tamanio ; ++i) {
        suma += numeros[i];
        cont += 1;
    }
    double promedio = suma/cont;
    return promedio;
}

int obtener_maximo(int const numeros[], int tamanio){
    int maximo = numeros[0];
    for (int i = 0; i < tamanio ; ++i) {
        if(numeros[i]> maximo){
            maximo = numeros[i];
        }
    }
    return  maximo;
}

int main() {
    int numeros[N];

    ingresar_valores(numeros, N);

    double promedio = obtener_promedio(numeros, N);
    printf("El promedio de los numeros ingresados es %lf: \n",promedio);

    int maximo = obtener_maximo(numeros, N);
    printf("El maximo numero ingresado es %i: \n",maximo);

    return 0;
}
