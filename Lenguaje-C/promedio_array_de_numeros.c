//Escribir una función que reciba un arreglo de números y la cantidad de elementos, y devuelva el promedio

#include <stdio.h>

// DOC: Completar
float promedio(float numeros[], int n) {
    float total = 0;
    for (int i = 0; i < n; ++i) {
        total += numeros[i];
    }
    float promedio = total/n;

    return promedio;
}

int main() {
    float numeros[3] = {8,7,5};
    int n = 3;
    float prom = promedio(numeros, n);
    printf("%f", prom);
    return 0;
}
