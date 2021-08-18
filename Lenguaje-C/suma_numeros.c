//Pedir al usuario que ingrese números y mostrar su suma. Usar -1 como condición de corte.

#include <stdio.h>

int sumar_numeros(){
    int num = 0;
    int suma = 0;
    printf("Ingrese numeros, corte con -1\n");
    while (num != -1){
        suma = suma + num;
        printf("ingrese un numero: \n");
        scanf("%i", &num);
    }
    return suma;
}

int main(){
    printf ("la suma es: %i", sumar_numeros());
    return 0;
}


