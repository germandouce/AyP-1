    //Arreglos - Arrays - Vectores

#include <stdio.h>

// Los arrays son bloques consecutivos de memoria para una cierta variable.
//Se pueden definir de la siguiente manera: TIPO nombre[#elementos]; # = "numero de"
//En C el nombre de un vector es un puntero al primer elemento del mismo

//Un ejemplo:

void definir_un_vector(){
    int vec[10];
    int * p_vec = &vec[0]; //defino un puntero apuntando al primer elemento del array
}


//Operaciones
// Se deben realizar elemento por elemento. (No es posible asignar un vector a otro, por ejemplo).
//Definiciones: La longitud de los vectores ES FIJA, por lo que es una buena práctica que sean definidos
// con constantes.


//Inicialización y algunos ejemplos:

void inicializar_un_vector(){
    int vector[4] = {10,5,2,3};
    int vectorcito[]={10,5,2,3};
    int array[7] = {0}; //me reservo un espacio de 7

//    printf("%i\n", vectorcito[1]);
//    printf("%i\n",vector[0]);
}


//Pasaje de vectores por parametro

//No es necesario aclarar la longitud del vector al momento de llamar a la función.
//El pasaje de vectores SIEMPRE se hace por referencia, ya que como dijimos el nombre del mismo es una referencia a la
// primera posición de este.


void modif_vector(int vector[]){
    vector[0] = 9;
}


//Arrays multidimensionales

//Es bastante simple declarar un array de varias dimensiones, un array bidimensional, por ejemplo, es visualizable como
// una matriz.

void matriz(){
    int matrix[2][2];
    int super_matrix[2][2]={1,2,5,3};
    int mega_matrix[2][2] = {{1,0},{0,1}};
}


int main() {
    definir_un_vector();
    inicializar_un_vector();

    int vec[3] = {1, 8, 2};
    modif_vector(vec);  //por referencia, no es necesario pasar la direc de memoria con &
    printf("%i %i %i\n",vec[0],vec[1],vec[2]);

    matriz();

    return 0;
}



