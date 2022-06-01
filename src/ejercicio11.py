################
# Nombre - @fersoria001
# UNRN Andina - Introducción a la Ingenieria en Computación
################

"""
### 11. Multiplos de
Escribir una función que indique con `True` si un número entero
es multiplo de otro, utilizando sumas y restas.
"""


def es_multiplo(numero, multiplo):
    """ Esta funcion comprueba si el segundo numero ingresado
    es multiplo del primero utilizando restas sucesivas.
        Precondiciones = Ingresar dos numeros enteros,positivos.
        Postcondiciones = Se retorna un valor booleano
    """
    while multiplo >= numero:
        multiplo = multiplo - numero
    if multiplo == 0:
        comprueba = True
    else:
        comprueba = False
    return comprueba


def principal():
    """
    Esta función es la que se encarga de la parte 'interactiva' del ejercicio
    (La entrada, la llamada al algoritmo y la salida)
    """
    num = int(input("Ingrese un numero: "))
    mult = int(input("Es multiplo de..?: "))
    comprobacion = es_multiplo(num,mult)
    print(f"{num} es multiplo de {mult} ? {comprobacion}")

if __name__ == "__main__":
    principal()
