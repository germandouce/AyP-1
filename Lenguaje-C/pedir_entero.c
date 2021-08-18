//Implementar la función int pedir_entero(int min, int max, char mensaje), que debe imprimir el mensaje y luego esperar
// a que el usuario ingrese un valor. Si el valor ingresado no es un número entero, o no es un número entre min y max
// (inclusive), se le debe avisar al usuario y pedir el ingreso de otro valor. Una vez que el usuario ingresa un valor
// válido, la función lo debe devolver.
//
//Ejemplo con pedir_entero(-50, 50, "¿Cual es tu numero favorito?"):
//
//"//¿Cual es tu numero favorito? [-50..50]:
//"//100
//Por favor ingresa un numero entre -50 y 50.
//¿Cual es tu numero favorito? [-50..50]:
//-60
//Por favor ingresa un numero entre -50 y 50.
//¿Cual es tu numero favorito? [-50..50]:
//51
//Por favor ingresa un numero entre -50 y 50.
//¿Cual es tu numero favorito? [-50..50]:
//-16
//Nota: Se puede asumir que el valor ingresado siempre es un número

#include <stdio.h>

int pedir_entero(int min, int max, char mensaje[]){
    printf("%s\n", mensaje);
    float num;
    scanf("%f", &num);
    int val = (int)num;
    printf("%f\n",num);
    printf("%i\n", val);
    while( num != val || (num <min) || num>max){
        printf("Por favor ingresa un numero entre -50 y 50.\n");
        scanf("%f", &num);
        int val = (int)num;
    }
}


int main(){
    char * mensaje = "¿Cual es tu numero favorito?";
    pedir_entero(-50,50,mensaje);
    return 0;
}