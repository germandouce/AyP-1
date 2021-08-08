                    //STRUCTS
//Un struct es una colección de una o más variables, que pueden ser de tipos diferentes, agrupadas bajo un solo nombre.
//El uso de estructuras ayuda a organizar datos complicados organizando un grupo de variables relacionadas entre sí.
// Asimismo permite distintos niveles de abstracción.

//Para codear éstos structs, vamos a hacer uso de la palabra reservada typedef para poder, luego, utilizar la
// estructura de una manera más prolija Cada vez que definimos un struct estamos creando nuestro propio
// tipo de dato, como convención nombramos a nuestro tipo de dato como nombre_t

#include <stdio.h>
#include <stdbool.h>


//Inicialización

typedef struct{
    int capacidad;
    char destino[30];
    char empresa[30];
    int as_ocupados;
    bool es_internacional;
}avion_t;


int modificar_con_puntero(avion_t *marca_avion){
    //marca_avion.as_ocupados = 30; //MAL!!! HAY Q USAR -> PUES ESTOY MODIFICANDO CON PUNTERO!
    marca_avion -> as_ocupados = 130;
}

int main() {
    avion_t airbus = {
            .destino = "Cordoba",
            .capacidad = 200,
            .empresa = "Aerolineas Argentinas",
            .as_ocupados = 10,
            .es_internacional = false,
            };

    //modificar con puntero
    avion_t *ptr_avion = &airbus;
    modificar_con_puntero(ptr_avion);

    printf("asientos ocupados en Airbus: %i\n", airbus.as_ocupados);

    avion_t boeing = {
        .destino = "Suva",
        .capacidad = 200,
        .empresa = "Fiyi Airways",
        .as_ocupados = 20,
        .es_internacional = false,
    };

    avion_t * ptr_boeing = &boeing;

    (*ptr_boeing).as_ocupados = 180;   //deja en 180
    //modificar_con_puntero(&boeing); //deja en 130 equivalente a...
    modificar_con_puntero(ptr_boeing); // deja en 130

    boeing.es_internacional = true;

    printf("el vuelo es internacional: %i\n", boeing.es_internacional); // 1= True
    printf("asientos ocupados en Boeing: %i\n", boeing.as_ocupados);

    return 0;
}

