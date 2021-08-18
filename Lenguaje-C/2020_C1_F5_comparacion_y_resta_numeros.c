//Dados dos números verificar que el primero sea mayor al segundo. En caso de no serlo, el
//programa deberá devolver -1. En caso de serlo, deberá sustraerse al primer número los números
//anteriores hasta llegar al segundo número. Finalmente, el programa deberá devolver el total de
//esa resta.
//Ej.:
//Num1: 10
//Num2: 5
//10 - 9 - 8 - 7 - 6 - 5 = -25

#include <stdio.h>

void restar_numeros(int num_1, int num_2, int *resultado){
    *resultado = num_1;
    for(int i = num_1-1; i >= num_2; i--){
        *resultado -= i;
        printf("%i\n", *resultado);
    }
}

int main() {
    int num_1;
    int num_2;
    int resultado;
    printf("Ingrese el 1er numero:");
    scanf("%i", &num_1);
    printf("Ingrese el 2do numero: ");
    scanf("%i", &num_2);
    if (num_1 > num_2){
        restar_numeros(num_1, num_2, &resultado );
    }
    else{
        resultado = -1;
    }
    printf("devolucion del programa: %i", resultado);

    return 0;
}
