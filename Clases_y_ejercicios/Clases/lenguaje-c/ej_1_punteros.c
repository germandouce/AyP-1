#include <stdio.h>

//Crear una variable de tipo int
//Crear un puntero a int y almacenar en él, la dirección de memoria de la variable.
//Crear un procedimiento que reciba un puntero a int y modifique el número almacenado en la dirección de memoria.
//Pasarle a ese procedimiento; la dirección de memoria de la variable creada en (1).
//Pasarle a ese procedimiento; el puntero a int creado en (2).


void modif_numero(int *var){        //aca simepre el "valor de la direc de memoria" si quiero modificar x referencia
    *var = 132;
}


int main() {
    int var =83;

    //paso drirec de memoria de var (1)
    //modif_numero(&var);

    int *ptr_var;   //creo el puntero
    ptr_var = &var; //le guardo la direc de memoria

    //paso puntero a int (que ya contiene la direc de memoria) (2)
    //modif_numero(ptr_var);

    printf("%d" ,var);
    return 0;
}
