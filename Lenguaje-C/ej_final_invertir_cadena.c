/*
Dado un string, programe una función que invierta el string y lo imprima. Además, en caso de haber una e deberá ser
reemplazada por una a.
Ej.: void invertiString(char palabra []);
madera
>>> aradam
No se permite el uso de la función strrev.
*/
#include <stdio.h>
#include <string.h>

#define MAX_SIZE 100

void invertiString(char palabra[]){

    int tamanio = strlen(palabra);

    size_t j = tamanio; //m a d e r a -> 6

    for (int i = 0; i < tamanio/2 ; ++i) {

        char caracter =  palabra[i];    //guardo el caracter

        if (palabra[i] == 'e'){
            caracter =  'a';
        }
        //cambio por la q voy a reemplzar en caso de ser una 'a'
        if (palabra[tamanio -i - 1] == 'e'){ //6-5 (recordar que arranca en 0 y -1 xq es la anterior (solo doy
            palabra[tamanio -i -1] ='a';          // vuelta la mitad)
        }

        palabra[i] = palabra[tamanio - i -1]; //reemplzao la q guarde en caracter
        palabra[tamanio -1 -i] = caracter; //reemplazo por la q guarde en caracter
    }

}


int main() {

    char palabra[MAX_SIZE];

    strncpy(palabra,"madera", MAX_SIZE);

    printf("\nVariable 'palabra' antes del cambio: %s\n", palabra);

    invertiString(palabra);

    printf("\nVariable 'palabra' despues del cambio: %s\n", palabra);

    return 0;
}