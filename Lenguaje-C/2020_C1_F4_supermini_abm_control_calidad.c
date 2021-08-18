//2) Se pide desarrollar un programa en lenguaje C, que cumpla con este enunciado:
//En el sector de calidad de nuestra industria se realizan mediciones de la concentración de un
//contaminante en ciertas muestras. Los valores que se registran son enteros.
//El sector nos pide que escribamos un programa que permita ingresar los valores de las mediciones
//(máximo 50) y le informe:
//1) Cantidad total de mediciones ingresadas.
//2) Los valores de las mediciones que son mayores al valor generado por la fórmula:
//Valor = (máximo - mínimo) / 2
//        Para esto nos brindan la función "asigna_max_min" que debemos utilizar para hallar el máximo y
//        el mínimo.
//        /*
//        Recibe un vector de enteros con su respectivo tope y asigna a max y min el valor máximo y
//        mínimo del vector.
//        */
//        //void asigna_max_min(int vec[MAX],int tope, int *max, int *min);

#include <stdio.h>
#include <string.h>

#define MAX_MEDICIONES 50

int ingresar_datos(int *mediciones){

    int cortar = 1;
    int cant_mediciones = 0;

    do {
        printf("\nIngrese la %d° medicion: ", cant_mediciones + 1);
        scanf(" %d", &mediciones[cant_mediciones]);

        printf("\n¿Desea seguir ingresando datos <1-s/0-n>?: ");
        scanf("%i",&cortar);

        cant_mediciones +=1;

    } while (cortar != 0 );

    return cant_mediciones;
}

void asigna_max_min(int mediciones[MAX_MEDICIONES],int cant_mediciones, int *max_medicion, int *min_medicion){
    *max_medicion = mediciones[0];
    *min_medicion = mediciones[0];

    for (int i = 0; i < cant_mediciones ; ++i) {
        if (mediciones[i] < *min_medicion){
            *min_medicion = mediciones[i];
        }
        if (mediciones[i] > *max_medicion){
            *max_medicion = mediciones[i];
        }
    }
}

void imprimir(int cant_mediciones,double valor_formula, int mediciones[MAX_MEDICIONES]){
    for (size_t i = 0; i < cant_mediciones ; ++i) {
        //printf("\n%i\n", mediciones[i]);
        if (mediciones[i] > valor_formula ){
            printf("\nMedición %i valor: %i", i+1,mediciones[i]);
        }
    }
    printf("\n");
}

int main() {
    int mediciones[MAX_MEDICIONES];

    int cant_mediciones = 0;
    int max_medicion = 0;
    int min_medicion = 0;
    double valor_formula = 0;

    cant_mediciones = ingresar_datos(mediciones);
    asigna_max_min(mediciones, cant_mediciones, &max_medicion, &min_medicion);

    valor_formula = (double)((max_medicion - min_medicion)/2 );

    //printf("%f", valor_formula);

    imprimir(cant_mediciones,valor_formula,mediciones);

    return 0;
}
