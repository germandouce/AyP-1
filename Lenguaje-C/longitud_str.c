//Implementar la función unsigned int strlen(const char *s) que devuelve la
//longitud de la cadena s (sin contar el último caracter '\0'). La función se puede escribir estar en forma
// iterativa o recursiva.

#include <stdio.h>
#include <string.h>

unsigned int strlen(const char *s) {
    int contador = 0;
    while (s[contador] != 0){       //el ultimo elememto del str es un 0!
        contador += 1;
    }
    return contador;
}

int main(){
    char* cadena = "hola";
    unsigned int len = strlen(cadena);
    printf("%i", len);
    return 0;
}
