import os
import string
from random import sample

BASE_DIR = os.path.abspath(os.path.dirname(__file__))
NOMBRE_DEL_ARCHIVO = "cadenas.txt"
RUTA = os.path.join(BASE_DIR, NOMBRE_DEL_ARCHIVO)
TAMANIO = 6
LINEAS = 100

def escribir_archivo(letras: str) -> None:

    with open(RUTA, 'w') as archivo:
        for i in range(LINEAS):
            string_random =  "".join(sample(letras, TAMANIO))      
            archivo.write(string_random + '\n')
    
    
def main() -> None:
    letras = string.ascii_lowercase
    escribir_archivo(letras)
main()