//Pedir al usuario que ingrese 10 numeros mostrar cuál fue el mayor y el menor ingresados.

#include <stdio.h>

void may_men(){
    int num;
    printf("Ingrese 10 numeros\n");
    scanf("%i", &num);
    int mayor = num;
    int menor = num;
    for (int i=0; i<9; i++ ){
        scanf("%i", &num);
        if (num >= mayor){
            mayor = num;
        }
        else if (num<= menor){
            menor = num;
        }
    }
    printf("El mayor es: %i\n", mayor);
    printf("El menor es: %i\n", menor);
}


int main() {
    may_men();
    return 0;
}
