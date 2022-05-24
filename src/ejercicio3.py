################
# Nombre - @fersoria001
# UNRN Andina - Introducción a la Ingenieria en Computación
################
"""
### 3. Comparación de números
Escribir una función que utilizando sumas y restas
, reciba dos valores y retorne:
 * Retornar `-1` si el primero es menor que el segundo
 * Retornar `0` si son iguales
 * Retornar `1` si el primero es mayor que el segundo
"""

def comparacion_de_numeros(numero,otro_numero):
    """ Esta funcion compara dos numeros mediante
    el uso de sumas y restas  y devuelve un valor:
    Precondiciones: Ingresar una tupla de dos numeros.
    Postcondiciones: Devuelve un valor entre -1 y 1.
    """
    resta = numero - otro_numero
    suma = otro_numero + (numero * -1)
    if resta > suma:
        salida = "1"
    elif suma > resta:
        salida = "-1"
    elif resta == 0:
        salida = "0"
    return salida


def principal():
    """
    Esta función es la que se encarga de la parte 'interactiva' del ejercicio
    (La entrada, la llamada al algoritmo y la salida)
    """
    numero = int(input(" Ingrese un numero: "))
    otro_numero = int(input("Ingrese otro numero: "))
    comp = comparacion_de_numeros(numero
                                  ,otro_numero)
    print(f" {comp}")

if __name__ == "__main__":
    principal()
