
#include <stdio.h>  //#include: Estos headers dan la instrucción de inclusión de las bibliotecas indicadas


            //main: La ejecución del programa comienza por esta función.
int main() {          //“{}” indican el comienzo y final de un bloque de código
    printf("Hello world \n");    // “;“ indica el final de una sentencia
    //probando();
    return 0;      //Ordena que el programa termine su ejecución y devuelva 0 al contexto en el que fue ejecutado indicando una ejecución exitosa
};



// COMENTARIOS

//de una sola linea

/* de
varias
líneas
como este */


//INCLUDES

//#include <stdio.h>  //<> busca los ficheros en todos los directorios especificados en la llamada al compilador (normalmente con la opción -I)
//#include "pila.h"  // “” busca este fichero primero en el mismo directorio donde está el fichero actualmente compilado


//VARIABLES

int numero =4;
long int contador = 0;
char letra = 'a';
int contador_2, resultado;


//CONSTANTES

//const int MAX_LEN = 5;
//const char NOMBRE[5] = "Aylen";

/*  copiar arriba del main()
void probando() {
    const int MAX_LEN = 5;
    const char NOMBRE = 'Aylen';
    printf(NOMBRE);
};
 */


//COMO REGLA GENERAL...
//char[X] para constantes de tipo str
//char* para variables de tipo str


//MACROS
/*La directiva #define indica al preprocesador que debe sustituir, en el código fuente del programa,
 * todas las ocurrencias del nombre de la macro por su valor, antes de la compilación.
*/

#define PI 3.141592;
#define E  2.718281;


//BOOLEANOS
/* No existe tipo de dato como tal, el lenguaje C considera falsa toda expresión que evalúe a 0 y verdadera a cualquier otra.
La biblioteca <stdbool.h> nos permite declarar variables tipo bool y asignar los valores true y false
*/
//







