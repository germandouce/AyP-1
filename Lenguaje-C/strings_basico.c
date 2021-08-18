                //STRINGS

//En C un string es un arreglo de datos tipo char
//cada string para estar correctamente declarado debe terminar con el caracter especial “\0”, por lo tanto SIEMPRE
//debemos reservar lugar para este!!! (longitud del str + 1)

#include <stdio.h>
#include <string.h>

//son equivalentes las siguientes expresiones:

void imprimir_cadenas(){
    char * cadena_salida = "Hello world!";
    char cadena_definida[14] = "Hello world!";

    char cadena_letra_x_letra[] = {'H','e','l','l','o',' ','w','o','r','l','d','!','\0'};
    //char * cadenota_letra_x_letra = {'H','e','l','l','o',' ','w','o','r','l','d','!','\0'};


    printf("%s\n",cadena_salida);
    printf("%s [14]\n", cadena_definida);
    printf("%s\n",cadena_letra_x_letra);
}
//FUNCIONES CLAVEEE


//CONCATENAR STRINGS

//char * strcat(char *dest, const char *src): Concatena ambas cadenas (python: dest + src)
//Parameters:
//dest: This is pointer to the destination array, which should contain a C string, and should be large enough to
// contain the concatenated resulting string.
//src: This is the string to be appended. This should not overlap the destination

//COPIAR STRINGS
//char * strcpy(char *dest, const char *src): Copia el string apuntado por src al lugar apuntado por dest
//dest: This is the pointer to the destination array where the content is to be copied.
//src: This is the string to be copied.

void concatenar_strings(){      //tambien esta copiar

    //char src[50];
    char dest[50];

    char * src = "finalsitoooohala";

    //strcpy(src, "final");       //copio el string de source ("final") al puntero src
    strcpy(dest, "Principio "); // copio el string de source ("principio") al puntero dest

    strcat(dest, src);

    printf("string total %s", dest);
}


//COMPARAR LARGO DE STRINGS
//int strcmp(const char *str1, const char *str2): Compara dos strings
// devolviendo 1 si str1 > str2, 0 str1 = str2 , -1 si str1 < str2 .

void comparar_strings(){

    char str1[15];
    char str2[15];
    int ret;

    strcpy(str1, "abcdef");
    strcpy(str2, "ABCDEF");

    ret = strcmp(str1, str2);   //1 si str1 es mayor a str2 , -1 al revés, 0 si son ='s

    printf("%i\n", ret);

    if(ret < 0) {
        printf("str2 is larger than str1");
    } else if(ret > 0) {
        printf("str1 is larger than str2");
    } else {
        printf("str1 is equal to str2");
    }

}


//CALCULAR LARGO DE UN STRING
//size_t strlen(const char *str): Calcula el largo del string sin incluir el carácter nulo

void calcular_longitud(){

    char str[50];
    unsigned int len;   //podria ser int

    strcpy(str, "mido 6");

    len = strlen(str);
    printf("Length of |%s| is |%d|\n", str, len);

}


int main() {
    //imprimir_cadenas();
    //concatenar_strings();
    //comparar_strings();
    //calcular_longitud();
    copiar_str();
    return(0);
}
