                            //PUNTEROS

#include <stdio.h>
//Como las funciones devuelven UN y solo UN tipo de dato, si deseamos modificar más de uno en una función o procedimiento;
// debemos recurrir a los punteros.

//DEFINICIÓN: Un puntero es una variable que contiene como valor la dirección de memoria de otra variable.
//Entonces, decimos que la variable puntero apunta a dicha dirección de memoria.

//TIPO * nombre_puntero;


//OPERADORES

//Operando: elemento sobre el cual se aplica una operacion
//(+4: + es operador, 4 es operando; &hola: & es operador, hola es operando; *p, * es operador, p es operando)

//Operador dirección (&): devuelve la dirección de memoria del operando -> puntero = direc_memoria = &variable
//El operador indirección (*): devuelve el contenido de la variable apuntada por su operando. El operando,
//debe ser un puntero -> contenido_variable = *puntero = *direc_memoria

void my_first_pointer(){
    int numero = 50; //creo la variable numero

    int * ptr; // creo puntero apuntando a un entero
    //&numero -> devuelve la direc de memoria de numero
    ptr = &numero; //Apunto con el puntero ptr a la direc de memoria de "número"

    printf("El valor de numero es %d\n", *ptr); // devuelvo el contenido de la direc de memoria que está guardada
                                                // en el puntero ptr
}


//Ejemplos

void fin_cuarentena(int *fin, int *contador_cuarentena ){
    *fin = 15 + *fin; // el contenido de la variable fin es = a 15 + el contenido de la variable fin
    *contador_cuarentena += 1;
}

//El lenguaje C pasa los argumentos de funciones por valor, entonces no hay una forma directa de alterar las
// variables de la función a la que se llama, debido a que utilizaría copias de las mismas.
//No tenemos el concepto de datos mutables o inmutables, la única forma de alterar una variable que fue
// declarada en un scope desde otro es a través del uso de punteros

//Aquí está la función swap, de la manera en la que está escrita los cambios que haga dentro del procedimiento,
// no serán visibles en el programa principal, ya que los mismos suceden en el scope local de la función.

void swap_no_modif_ppal(int val_1, int val_2){
    int aux;
    aux = val_1;
    val_1 = val_2;
    val_2 = aux;
    printf("val_1: %d (dentro de swap)\n",val_1); //observar que aqui dentro de la funcion vale 7 pero al salir...
}

void swap_si_modif_ppal(int *val_1, int *val_2){
    int aux;
    aux = *val_1;
    *val_1 = *val_2;
    *val_2 = aux;
}

int main (){
    //my_first_pointer();

    int dias_faltantes = 0;
    int cantidad_alargues = 0;
    fin_cuarentena(&dias_faltantes, &cantidad_alargues); //le mando las direc de memoria de las vraiables dias_faltantes
                                                        // y cantidad_alargues ( es decir un puntero de cada uno )

    //printf("dias faltantes: %d, cantidad de alargues: %d\n", dias_faltantes, cantidad_alargues);

    //Esto último es equivalente a hacer esto:
    //int *ptr_dias_faltantes;
    //ptr_dias_faltantes = &dias_faltantes;
    //int *ptr_cantidad_alargues;
    //ptr_cantidad_alargues = &cantidad_alargues;
    //fin_cuarentena(ptr_dias_faltantes, ptr_cantidad_alargues);

    int val_1 = 1;
    int val_2 = 7;

    printf("SWAP SIN PUNTERO:\n");
    swap_no_modif_ppal(val_1, val_2);   //mando la variable
    printf("val_1: %i, val_2: %i (fuera de swap)\n",val_1, val_2); // observar que se mantienen iguales. Pero en la sig...

    printf("SWAP CON PUNTERO:\n");
    swap_si_modif_ppal(&val_1, &val_2); //mando las direc de memoria de val_1 y vaL_2
    printf("vale_1: %d, val_2: %d (fuera de swap)\n", val_1, val_2);

    return 0;
};