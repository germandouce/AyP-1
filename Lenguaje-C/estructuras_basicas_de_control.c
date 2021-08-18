#include <stdio.h>
#include <stdlib.h>
#include <string.h>

                        //ESTRUCTURAS BÁSICAS DE CONTROL: SINTAXIS BÁSICA


// SELECTIVAS: IF - ELSE

void condicional_0(){
    int a = 8;
    int b = 5;
    if (b>a){           //(condición)
        printf("%i es mayor que %d ", b, a);
    }
    else{       // ver que van {} antes y después de cada sentencia o acción
        printf("%i es mayor que %i",a, b ); //acción;
    };
};


//SELECTIVAS: SWITCH CASE

/*Las variables case pueden ser de tipo int o char
La sentencia default es opcional
Si no se pone un break en cada case se ejecutará desde la sentencia que matchee hacia abajo
 */

//N:B --->;
// switch labels must be constant expressions, they have to be evaluated at compile time. If you want to
// branch on run-time values, you must use an if.
//An integer constant expression shall have integer type and shall only have operands that are
// integer constants, enumeration constants, character constants, sizeof expressions whose results
// are integer constants, _Alignof expressions, and floating constants that are the immediate operands
// of casts. Cast operators in an integer constant expression shall only convert arithmetic types
// to integer types, except as part of an operand to the sizeof or _Alignof operator.

void func_switch(){
    int var = 4;

    switch (var){
        case 4:
            printf("es 5");
            break;
        case 7:
            printf("es 4");
            break;
        default:
            printf("no es ni 5 ni 4");

        }
}


//ITERATIVAS: DO-WHILE
//Util cuando depende de un input, asi se ejecuta el input una vez y dsps e actualiza el estado
//ejecutandose una segunda vez.
//El bloque do se ejecutará por única vez siempre antes de entrar o no al ciclo

void ciclo_do_while(){
    int i = 0;
    do{
        printf("%i\n",i);
        i++;
    }while(i<4);
};


//ITERATIVAS: WHILE

void ciclo_while(){
    int i =0;
    while(i < 4){
        printf("%d\n",i);
        i++;
    }
}


//ITERATIVAS: FOR
//Expresión_1: define cual es la variable de control del ciclo y su valor inicial, esta puede definirse en
//la misma sentencia.
//Expresión_2: define el valor de corte del ciclo, es una expresión booleana.
//Expresión_3: define cómo se incrementa la variable de control.

void ciclo_for(){

    for(size_t i = 0 ; i < 4; i++){
        printf("%i\n", i);
    }
}


// INPUT OUTPUT:
/*
*Formatos más usados:
%d o %i	signed int
%u		unsigned int
%c		char
%s		string
%f		float
%lf		double
%.2f    .n (n cant de decimales)
 */

func_input(){
    #define MAX_NAME_SZ 256

    int var; // declaro la variable

    printf("Ingrese un numero:"); //Escritura
    scanf(" %i", &var); //;lectura

    //printf("numero %d: ", var);
    //fgets( var, 2, stdin);

    printf("numero %d: ", var);

    return 0;

}


//FUNCIONES Y PROCEDIMIENTOS

//Ej. De PROCEDIMIENTO (se definen con void() no devuelve nada)
void imprimir_emoji(var){
    printf("UwU\n");
}

//Ej. De FUNCIÓN (se define como Type_a_devolver nombre_función y siempre devuelve algún tipo de dato)
int suma(int num_1, int num_2){
    int resultado;
    resultado =  num_1 + num_2;
    return resultado;
}

int main(){
    //condicional_0();
    //func_switch();
    //ciclo_do_while();
    //ciclo_while();
    //ciclo_for();
    //func_input();
    //imprimir_emoji();
    int num_1 = 4;
    int num_2 = 5;
    //int resultado = suma(num_1, num_2);
    //printf("%i + %i = %i", num_1, num_2, resultado);
    return 0;
};
