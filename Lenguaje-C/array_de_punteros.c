#include <stdio.h>
#include <string.h>

#define MAX_CANT 10

/*char* invertirString(char* string){
    size_t largo;
    largo = strlen(string);
    char aDevolver[largo];
    for(size_t i = largo; i > 0; i--){
        strcat(aDevolver, &string[i-1]);
    }
    return aDevolver;
}*/

//char* invertirStringInPlace(char* string){
//    size_t largo = strlen(string);
//    char a = 'a';
//    strcat(string, &a);
//    for(size_t i = 0; i < largo/2; i++){
//        printf("%s", "Llegué acá");
//        string[largo] = string[i];
//        string[i] = string[largo-i];
//        string[largo-i] = string[largo];
//    }
//    string[largo] = '\0';
//    return string;
//}

void invertirString_2(char palabra[]) {

    /*
    PRE: 'palabra', debe ser una variable de tipo array de chars
    POST: Invierte las posiciones de la palabra contenida en el
          array de chars
    */
    //    char palabra[100];
    //
    //    strncpy(palabra, cadena, 100);

    int tamanio = strlen(palabra);

    for (size_t i = 0; i < tamanio / 2; i++) {
        //printf("%s",palabra);

        char caracter = palabra[i];

        palabra[i] = palabra[tamanio - i - 1];

        //palabra[tamanio -1] la ultima letra xq strlen da "1 +"
        //palabra[tamanio - i -1] la diferencia entre la pos en la q estoy y el ultimo
        //voy solo hasta la mitad xq invierto la mitdad de los caracteres

        palabra[tamanio - i - 1] = caracter;
    }
    printf("%s",palabra);
}

void invertir_array_numeros(int *array[], int tamanio){

    for (int i = 0; i < tamanio/2; ++i) {
        //printf("%i\n", array[i]);
        int *numero = array[i];  //guardo la q voy a reemplazar

        array[i] = array[ tamanio - i - 1]; //la posicion toma el valor de la ultima

        array[tamanio -i -1] = numero;
    }
}



int main() {
    char* palabra = "palabra";
    char* esperado = "arbalap";
    //invertirStringInPlace(palabra);
    //printf("%s", palabra);
    //printf((const char *) strcmp(palabra, esperado));

    //int array[MAX_CANT] = {1,2,3,4,5};  //escribir aca el array deseado max 10 numeros!!

    int uno = 1;
    int dos = 2;
    int tres = 3;
    int cuatro =4;
    int *array2[] = {&uno, &dos, &tres, &cuatro};

    int tamanio =  sizeof(array2) / sizeof(array2[0]);

    invertir_array_numeros(array2, tamanio);

    for (int i = 0; i < MAX_CANT; ++i) {
        printf("%i, ", *array2[i]);
        printf("direc mem: %p, ", &array2[i]);
    }


    return 0;
}
