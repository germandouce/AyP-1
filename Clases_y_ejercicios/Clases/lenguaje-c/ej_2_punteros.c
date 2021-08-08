//Crear un procedimiento que sume números ingresados por el usuario (los almacenará utilizando un puntero) y luego haga
// un print del resultado en el main.

//Aclaración mia: al ser un procedimiento no deberia devolver nada. solo suma y modifica el total de la suma a través
//del puntero
#include <stdio.h>

void sumar_numeros(int *suma){
    int seguir = 1;
    int num;
    while (seguir){
        printf("Ingrese numero\n");
        scanf("%i",&num);
        *suma += num;
        printf("mas numeros? 1-si/0-no\n");
        scanf("%i",&seguir);
    }

}

int main(){
    int suma_total = 0;

    int *ptr_suma_total = &suma_total; //creo el puntero y le asigno la direc de memoria de suma_total
    sumar_numeros(ptr_suma_total);   //le mando a sumar numeros el puntero con la direc de memoria de suma_total

    //lineas 23 y 24 equivalen a esto...
    //sumar_numeros(&suma_total); //mando la direc de memoria de suma_total

    printf("suma total: %i",suma_total);
}